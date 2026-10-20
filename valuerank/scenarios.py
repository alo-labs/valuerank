"""The scenario engine (Uncertainty layers S0/S1/S2, draw kernels E25, sequential precision E72/E77).

Each scenario draws:

- S0 (measurement): observed leaf values and cost from their reporting-precision
  kernels (uniform on the published record's rounding interval); quality is the
  observed-only renormalised composite. The stream's target profile is an
  explicit allowlist (E145): a kernel concerning anything else (a fitted-rating
  interval, a run range, an analyst range) fails validation.
- S1 (identification): S0 plus a value for every missing leaf from the declared
  convention (uniform on 0-100; the published alternative draws uniformly on
  the cohort's observed range for that leaf); quality is the full composite.
- S2 core: S1 plus a hierarchical Dirichlet weight draw around the nominal
  weights (group ~ Dirichlet(100 x group shares), within group ~
  Dirichlet(50 x within-group proportions)).

Results are scenario frequencies per stratum, never probabilities, each with a
Monte Carlo standard error. Threshold labels (90%) use the sequential rule:
looks every 10,000 scenarios up to 160,000, an exact Clopper-Pearson interval at
error allocation alpha/16 per look (confidence 1 - alpha/16, equal tails), "met" when the lower bound >= 0.90, "not met" when the
upper bound < 0.90, otherwise continue, ending "unresolved" at the cap.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import random
import re
from dataclasses import dataclass, field

from valuerank import anchors as anchor_math
from valuerank import quality as q

# E143: what each v1 stream concerns, separately from its uncertainty layer.
TARGET_PROFILES = {
    "S0": "published-record reporting precision",
    "S1": "published-record reporting precision + conventional identification of missing leaves",
    "S2": "published-record reporting precision + conventional identification of missing leaves + weight-specification stress",
    # E162/E165: the separately named stream that draws inside published 95% confidence intervals (Terminal-Bench's)
    # under a conventional kernel: a range sensitivity, not a source-estimated distribution of expected performance.
    "S1M": "published-record reporting precision + conventional identification of missing leaves + conventional range sensitivity inside published 95% confidence intervals (no tail model)",
}
STRATA = ("S0", "S1", "S2", "S1M")
# E161: every stream's events name the quality equation they use, so S0-to-S1 changes are never read as uncertainty alone.
QUALITY_EQUATIONS = {
    "S0": "observed leaves, renormalised (observed-only score)",
    "S1": "full composite, nominal weights",
    "S2": "full composite, hierarchical weight draw",
    "S1M": "full composite, nominal weights",
}
FRONTIER_EVENTS = {
    "S0": "observed-only score frontier frequency",
    "S1": "full-composite frontier frequency under conventional missing-evidence draws",
    "S2": "full-composite frontier frequency under missing-evidence and weight-stress draws",
    "S1M": "full-composite frontier frequency under missing-evidence draws and conventional draws inside published intervals",
}
# E145: the target profile governs which inputs a stream may vary (an explicit allowlist); source-supported
# uncertainty about expected performance or future runs enters only separately named streams (none in v1).
REPORTING_PRECISION = "reporting precision"
IDENTIFICATION_CONVENTION = "identification convention"
SPECIFICATION_STRESS = "specification stress"
EXPECTED_PERFORMANCE = "expected performance"
# E165: draws inside a published confidence interval whose estimand, method and sampling unit the source does not
# document are a conventional range sensitivity; they never stand in for expected-performance uncertainty.
INTERVAL_RANGE = "published-interval range (conventional)"
STREAM_TARGETS = {
    "S0": frozenset({REPORTING_PRECISION}),
    "S1": frozenset({REPORTING_PRECISION, IDENTIFICATION_CONVENTION}),
    "S2": frozenset({REPORTING_PRECISION, IDENTIFICATION_CONVENTION, SPECIFICATION_STRESS}),
    "S1M": frozenset({REPORTING_PRECISION, IDENTIFICATION_CONVENTION, INTERVAL_RANGE}),
}
GROUP_CONCENTRATION = 100.0
LEAF_CONCENTRATION = 50.0
BATCH = 10_000
MAX_SCENARIOS = 160_000
LOOKS = MAX_SCENARIOS // BATCH
ALPHA = 0.05
THRESHOLD = 0.90


# E134: where a kernel's parameters come from; an S0 draw must rest on published evidence, never on an analyst convention alone.
PUBLISHED_PRECISION = "published reporting precision"
ANALYST_CONVENTION = "analyst convention"


@dataclass(frozen=True)
class Kernel:
    """A draw kernel: 'fixed' (value), 'uniform' (low, high), 'split-uniform' (low, point, high), 'uniform-sum'
    (offset, (low, high), ...) or 'runs' (public run values)."""

    family: str
    params: tuple
    alternative: str | None = None  # 'endpoint-heavy' for interval-only inputs
    target: str = REPORTING_PRECISION  # E145: what the kernel's variation is uncertainty about
    derivation: str = PUBLISHED_PRECISION  # E134: what its parameters are derived from

    def __post_init__(self):
        if self.family == "runs" and self.target == REPORTING_PRECISION:
            raise ValueError("a run-level bootstrap concerns expected performance or future runs, never reporting precision")
        if self.family == "split-uniform" and not self.params[0] <= self.params[1] <= self.params[2]:
            raise ValueError("a split-uniform kernel's published point must lie inside its interval (E182)")

    def draw(self, rng: random.Random, *, use_alternative: bool = False) -> float:
        if self.family == "fixed":
            return self.params[0]
        if self.family == "uniform":
            low, high = self.params
            if use_alternative and self.alternative == "endpoint-heavy":
                return low + (high - low) * rng.betavariate(0.5, 0.5)
            return rng.uniform(low, high)
        if self.family == "split-uniform":
            # E182: half the mass on each side of the published point, so an asymmetric interval keeps it as the median.
            low, point, high = self.params
            start, end = (low, point) if rng.random() < 0.5 else (point, high)
            if use_alternative and self.alternative == "endpoint-heavy":
                return start + (end - start) * rng.betavariate(0.5, 0.5)
            return rng.uniform(start, end)
        if self.family == "runs":
            values = self.params
            return sum(rng.choice(values) for _ in values) / len(values)
        if self.family == "uniform-sum":
            # E154: a derived sum of independently rounded primitives (an exact offset plus one interval per record).
            offset, *intervals = self.params
            heavy = use_alternative and self.alternative == "endpoint-heavy"
            return offset + sum(low + (high - low) * rng.betavariate(0.5, 0.5) if heavy else rng.uniform(low, high) for low, high in intervals)
        raise ValueError(f"unknown kernel family: {self.family}")


@dataclass
class RowInputs:
    row: str
    leaves: dict  # leaf key -> Kernel on the z scale (observed leaves only)
    cost: Kernel  # cost in USD
    provisional: bool = False
    meta: dict = field(default_factory=dict)


def dirichlet(rng: random.Random, alphas: list[float]) -> list[float]:
    draws = [rng.gammavariate(alpha, 1.0) for alpha in alphas]
    total = sum(draws)
    return [value / total for value in draws]


def hierarchical_weights(rng: random.Random) -> dict:
    """Leaf weights (percent) from the hierarchical Dirichlet that preserves the nominal means."""

    groups = list(q.GROUPS)
    group_shares = dirichlet(rng, [GROUP_CONCENTRATION * q.GROUPS[group] / 100.0 for group in groups])
    weights = {}
    for group, share in zip(groups, group_shares):
        leaves = [leaf for leaf in q.LEAVES if leaf.group == group]
        total = sum(leaf.weight for leaf in leaves)
        if len(leaves) == 1:
            weights[leaves[0].key] = 100.0 * share
            continue
        within = dirichlet(rng, [LEAF_CONCENTRATION * leaf.weight / total for leaf in leaves])
        for leaf, part in zip(leaves, within):
            weights[leaf.key] = 100.0 * share * part
    return weights


def nominal_weights() -> dict:
    return {leaf.key: leaf.weight for leaf in q.LEAVES}


def missing_ranges(rows: list[RowInputs]) -> dict:
    """The published alternative convention: the cohort's observed range for each leaf."""

    ranges = {}
    for leaf in q.LEAVES:
        values = [row.leaves[leaf.key].params[0] for row in rows if leaf.key in row.leaves and row.leaves[leaf.key].family == "fixed"]
        values += [sum(row.leaves[leaf.key].params) / len(row.leaves[leaf.key].params) for row in rows if leaf.key in row.leaves and row.leaves[leaf.key].family != "fixed"]
        ranges[leaf.key] = (min(values), max(values)) if values else (0.0, 100.0)
    return ranges


NOT_ESTABLISHED = "not established from the captured documentation"
INTERVAL_CONTRACT_FIELDS = ("sourceEstimand", "sourceIntervalMethod", "samplingUnit", "repeatedTaskTreatment")
INTERVAL_LABELS = {
    True: "source-supported expected-performance uncertainty",
    False: "conventional CI-range sensitivity (endpoint-conditioned; no tail model)",
}


def interval_interpretation(contract: dict) -> dict:
    """E165: the label a stream drawing inside a published interval may carry, derived from what the source documents.

    Only a source-derived kernel whose estimand, interval method, sampling unit and treatment of
    repeated tasks are all documented supports "expected-performance uncertainty"; anything else
    is a conventional sensitivity over the interval's range, with no mass outside it.
    """

    supported = contract["kernelStatus"] == "source-derived" and all(contract[field] != NOT_ESTABLISHED for field in INTERVAL_CONTRACT_FIELDS)
    return {**contract, "permittedLabel": INTERVAL_LABELS[supported]}


# E155: the release-text lint. A published sentence that puts a source interval or a run range into scenario
# shares must name a stream whose allowlist admits that target, or state that the target is outside the shares.
_SHARES = re.compile(r"scenario (?:share|frequenc)|\bS[0-2]M?\b|\bstreams?\b", re.IGNORECASE)
_SOURCE_INTERVAL = re.compile(r"confidence interval|published interval|source interval", re.IGNORECASE)
_RUN_RANGE = re.compile(r"run-to-run|run ranges?\b|run values|repeated runs", re.IGNORECASE)
_OUTSIDE = re.compile(r"\bnot quantified\b|\boutside\b|\bnever\b|\bnot\b", re.IGNORECASE)


def lint_release_text(text: str) -> list[str]:
    """E155: sentences that claim a source interval or run range enters scenario shares without an admitting stream."""

    admitting = [stratum for stratum in STRATA if INTERVAL_RANGE in STREAM_TARGETS[stratum]]
    violations = []
    for sentence in re.split(r"(?<=[.;])\s+|\n+", text):
        interval, runs = _SOURCE_INTERVAL.search(sentence), _RUN_RANGE.search(sentence)
        if not (interval or runs) or not _SHARES.search(sentence) or _OUTSIDE.search(sentence):
            continue
        if runs or not any(re.search(rf"\b{stratum}\b", sentence) for stratum in admitting):
            violations.append(sentence.strip())
    return violations


def validate_stream(rows: list[RowInputs], stratum: str) -> list[str]:
    """E145: every varying input must be one the stratum's target profile allows; returns the varied targets.

    Fixed inputs never vary and always pass. A kernel whose target the profile
    does not list (a fitted-rating interval, a run range, an analyst range in S0)
    fails the build instead of entering a stream labelled for something else.
    """

    if stratum not in STRATA:
        raise ValueError(f"unknown stratum: {stratum}")
    varied = set()
    for row in rows:
        for name, kernel in [*sorted(row.leaves.items()), ("cost", row.cost)]:
            if kernel.family == "fixed":
                continue
            if kernel.target not in STREAM_TARGETS[stratum]:
                raise ValueError(f"{stratum} ({TARGET_PROFILES[stratum]}) cannot vary {row.row} {name}: its kernel concerns {kernel.target}")
            if stratum == "S0" and kernel.derivation == ANALYST_CONVENTION:
                raise ValueError(f"S0 cannot vary {row.row} {name}: its parameters derive only from an analyst convention (E134)")
            varied.add(kernel.target)
    if stratum != "S0":
        varied.add(IDENTIFICATION_CONVENTION)  # missing-leaf domains (drawn in the scenario)
    if stratum == "S2":
        varied.add(SPECIFICATION_STRESS)  # hierarchical weights
    return sorted(varied)


def dependency_components(rows: list[RowInputs]) -> list[list[str]]:
    """E147: rows that share a varying primitive (``meta['sharedPrimitives']``) form one dependency component.

    Compiled from the stream's inputs, never asserted: a shared price list or
    donor multiple that is drawn once per scenario links every row it feeds.
    """

    parent = {row.row: row.row for row in rows}

    def find(item):
        while parent[item] != item:
            item = parent[item]
        return item

    owner = {}
    for row in rows:
        for primitive in row.meta.get("sharedPrimitives", ()):
            if primitive in owner:
                parent[find(row.row)] = find(owner[primitive])
            else:
                owner[primitive] = row.row
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(find(row.row), []).append(row.row)
    return sorted(sorted(group) for group in groups.values())


def draw_scenario(rows: list[RowInputs], stratum: str, rng: random.Random, *, alternative: bool = False, ranges: dict | None = None, alternative_rows: frozenset | None = None) -> dict:
    """One scenario: {row: (cost, quality)} for the stratum.

    ``alternative_rows`` (E121) assigns the endpoint-heavy kernels per row block;
    without it, ``alternative`` applies to every row.
    """

    if stratum not in STRATA:
        raise ValueError(f"unknown stratum: {stratum}")
    weights = hierarchical_weights(rng) if stratum == "S2" else nominal_weights()
    scenario = {}
    for row in rows:
        heavy = alternative if alternative_rows is None else row.row in alternative_rows
        values = {key: kernel.draw(rng, use_alternative=heavy) for key, kernel in row.leaves.items()}
        if stratum == "S0":
            observed = sum(weights[key] for key in values)
            quality = sum(weights[key] * value for key, value in values.items()) / observed
        else:
            for leaf in q.LEAVES:
                if leaf.key not in values:
                    # A missing leaf's score domain is an interval-only input: uniform, with the E25 endpoint-heavy alternative.
                    low, high = (ranges or {}).get(leaf.key, (0.0, 100.0))
                    values[leaf.key] = Kernel("uniform", (low, high), "endpoint-heavy", IDENTIFICATION_CONVENTION).draw(rng, use_alternative=heavy)
            quality = sum(weights[key] * values[key] for key in weights) / 100.0
        scenario[row.row] = (row.cost.draw(rng, use_alternative=heavy), quality)
    return scenario


def scenario_values(scenario: dict, anchors: dict, beta: float) -> dict:
    return {row: anchor_math.value_score(anchor_math.cost_score(cost, anchors), quality, beta) for row, (cost, quality) in scenario.items()}


def ranks(values: dict) -> dict:
    """Competition ranks (1 = best); equal values share the better rank."""

    ordered = sorted(values.values(), reverse=True)
    return {row: 1 + sum(1 for other in ordered if other > value) for row, value in values.items()}


def frontier_rows(scenario: dict) -> set:
    """Rows not dominated in this scenario (lower cost and higher quality, at least one strict)."""

    members = set()
    for row, (cost, quality) in scenario.items():
        dominated = any(
            other_cost <= cost and other_quality >= quality and (other_cost < cost or other_quality > quality)
            for other, (other_cost, other_quality) in scenario.items()
            if other != row
        )
        if not dominated:
            members.add(row)
    return members


def cheapest_qualifier(scenario: dict, reference: str) -> str | None:
    """The strictly cheapest row qualifying against the reference in this scenario, or None on a tie or no qualifier."""

    bar = scenario[reference][1]
    qualifiers = sorted((cost, row) for row, (cost, quality) in scenario.items() if quality >= bar)
    if not qualifiers or (len(qualifiers) > 1 and qualifiers[0][0] == qualifiers[1][0]):
        return None
    return qualifiers[0][1]


LABEL_STRATUM = "S1"


def scenario_supported_cheapest(rows: list[RowInputs], candidate: str, reference: str, stratum: str, rng: random.Random, *, alternative: bool = False, alternative_rows: frozenset | None = None, **rule) -> dict:
    """E92: the scenario-supported unique-cheapest label for one bar and one candidate.

    The event is "the candidate qualifies and is strictly cheaper than every other
    qualifier in the same scenario"; every row, provisional or not, competes in it.
    The label also needs UniqueLabelEligible (a provisional candidate keeps its
    published event frequency but never receives the label) and the authorising
    branch, S1 core (E100); other strata and branches publish the frequency only.
    """

    varied = validate_stream(rows, stratum)

    def event(generator):
        scenario = draw_scenario(rows, stratum, generator, alternative=alternative, alternative_rows=alternative_rows)
        return cheapest_qualifier(scenario, reference) == candidate

    outcome = sequential_threshold(event, rng, **rule)
    eligible = not next(row.provisional for row in rows if row.row == candidate)
    # E100/E112: only the full-composite S1 core branch, under each of its pre-registered kernels, authorises the label.
    authorized = stratum == LABEL_STRATUM
    signature = {
        "qualityEquation": QUALITY_EQUATIONS[stratum],
        "scenarioStratum": stratum,
        "scenarioTargetProfileId": TARGET_PROFILES[stratum],
        "variedTargets": varied,
        "specificationBranch": "core",
        "kernel": "endpoint-heavy alternative" if alternative else "primary" if alternative_rows is None else "block assignment",
        "endpointHeavyRows": sorted(alternative_rows) if alternative_rows is not None else None,
        "referenceObjectId": reference,
    }
    return {
        **outcome,
        "uniqueLabelEligible": eligible,
        "labelAuthorized": authorized,
        "decisionTarget": signature,
        "label": authorized and eligible and outcome["status"] == "met",
    }


BLOCKS = ("candidate", "reference", "competitors")


def kernel_assignments(rows: list[RowInputs], candidate: str, reference: str) -> list[dict]:
    """E121: every uniform/arcsine assignment over the event-relevant blocks (candidate, reference, competitors).

    Rows of one block share one kernel family; when the candidate is the
    reference, the two blocks coincide and duplicate assignments are dropped.
    """

    members = {
        "candidate": {candidate},
        "reference": {reference},
        "competitors": {row.row for row in rows} - {candidate, reference},
    }
    components = dependency_components(rows)
    assignments, seen = [], set()
    for flags in itertools.product((False, True), repeat=len(BLOCKS)):
        heavy = frozenset().union(*(members[block] for block, flag in zip(BLOCKS, flags) if flag))
        light = frozenset().union(*(members[block] for block, flag in zip(BLOCKS, flags) if not flag))
        # E147: rows of one dependency component share primitives, so they always take one kernel family.
        split = any(heavy.intersection(component) and not heavy.issuperset(component) for component in components)
        if heavy & light or split or heavy in seen:
            continue
        seen.add(heavy)
        assignments.append({"id": "".join("H" if flag else "U" for flag in flags), "endpointHeavyRows": heavy})
    return assignments


def kernel_robust_cheapest(rows: list[RowInputs], candidate: str, reference: str, seed: int, **rule) -> dict:
    """E112/E121: the scenario-supported label needs the S1 threshold met under every registered block assignment.

    Each assignment is resolved by the E77 sequential rule; the frequency range
    across assignments is published, never its minimum as a probability. A
    primary-kernel pass that fails under another assignment reads
    "kernel-sensitive" without the label.
    """

    runs = {}
    assignments = kernel_assignments(rows, candidate, reference)
    for index, assignment in enumerate(assignments):
        runs[assignment["id"]] = scenario_supported_cheapest(
            rows, candidate, reference, LABEL_STRATUM, random.Random(seed + index), alternative_rows=assignment["endpointHeavyRows"], **rule
        )
    primary = runs["UUU"]
    met = all(run["status"] == "met" for run in runs.values())
    unresolved = any(run["status"] == "scenario threshold unresolved" for run in runs.values())
    eligible = primary["uniqueLabelEligible"]
    # E137: distinct outcomes; the label needs every registered assignment met.
    if not eligible:
        reading = "frequency only (provisional row)"
    elif met:
        reading = "supported under all registered role-group kernel checks"
    elif unresolved:
        reading = "scenario threshold unresolved"
    elif primary["status"] == "met":
        reading = "primary-kernel frequency >= 90%; kernel-sensitive"
    else:
        reading = "not scenario-supported"
    shares_ = [run["share"] for run in runs.values()]
    components = dependency_components(rows)
    blocks = {"candidate": {candidate}, "reference": {reference}, "competitors": {row.row for row in rows} - {candidate, reference}}
    check = {
        # E133/E147: components are compiled from the stream's shared primitives; kernels switch by role group,
        # and role groups linked by one component switch together.
        "dependencyComponents": components,
        "dependencyGraphHash": hashlib.sha256(json.dumps(components).encode()).hexdigest()[:16],
        "mergedBlocks": [sorted(block for block in BLOCKS if blocks[block] & set(component)) for component in components if sum(1 for block in BLOCKS if blocks[block] & set(component)) > 1],
        "switchGroups": {"candidate": [candidate], "reference": [reference], "competitors": sorted({row.row for row in rows} - {candidate, reference})},
        "assignments": [{"id": item["id"], "endpointHeavyRows": sorted(item["endpointHeavyRows"])} for item in assignments],
        "assignmentSetHash": hashlib.sha256(json.dumps(sorted(item["id"] for item in assignments)).encode()).hexdigest()[:16],
        "coverage": "role-group (competitor components switch together; not exhaustive over dependency components)",
        "executionStatus": "threshold unresolved" if any(run["status"] == "scenario threshold unresolved" for run in runs.values()) else "completed",
    }
    return {"assignments": runs, "kernelCheck": check, "frequencyRange": [min(shares_), max(shares_)], "label": met and eligible, "reading": reading}


def standard_error(share: float, n: int) -> float:
    return math.sqrt(share * (1.0 - share) / n) if n else 0.0


DISPERSION_LABEL = "scenario dispersion under the declared kernels"


class Comoments:
    """Running means, variances and covariance of (S_C, Q) over a stream's scenarios (Welford's update)."""

    def __init__(self):
        self.count, self.mean_cost, self.mean_quality = 0, 0.0, 0.0
        self.square_cost, self.square_quality, self.cross = 0.0, 0.0, 0.0

    def add(self, cost_score: float, quality: float) -> None:
        self.count += 1
        cost_step = cost_score - self.mean_cost
        self.mean_cost += cost_step / self.count
        quality_step = quality - self.mean_quality
        self.mean_quality += quality_step / self.count
        self.square_cost += cost_step * (cost_score - self.mean_cost)
        self.square_quality += quality_step * (quality - self.mean_quality)
        self.cross += cost_step * (quality - self.mean_quality)

    def decomposition(self, beta: float) -> dict:
        """E87: Var_s(V) = beta^2 Var_s(S_C) + (1 - beta)^2 Var_s(Q) + 2 beta (1 - beta) Cov_s(S_C, Q), terms published separately."""

        if not self.count:
            return {"status": "no scenario SD defined", "label": DISPERSION_LABEL}
        cost_term = beta * beta * self.square_cost / self.count
        quality_term = (1.0 - beta) ** 2 * self.square_quality / self.count
        covariance_term = 2.0 * beta * (1.0 - beta) * self.cross / self.count
        variance = max(0.0, cost_term + quality_term + covariance_term)
        return {
            "status": "defined", "label": DISPERSION_LABEL, "scenarios": self.count,
            "valueVariance": variance, "valueSd": math.sqrt(variance),
            "costTerm": cost_term, "qualityTerm": quality_term, "covarianceTerm": covariance_term,
        }


def shares(rows: list[RowInputs], stratum: str, n: int, seed: int, anchors: dict, beta: float, *, references: tuple = (), pairs: tuple = (), alternative: bool = False) -> dict:
    """Per-row scenario frequencies for one stratum: rank <= 3, rank 1, frontier, per-bar qualification.

    E96: the panel is the declared row set, fixed for every scenario; ranks are
    competition ranks (ties share the better rank, so more than k rows can hold
    rank <= k); each declared pair (i, j) reports win, tie and loss frequencies
    for V_i against V_j.
    """

    varied = validate_stream(rows, stratum)
    rng = random.Random(seed)
    ranges = None
    counts = {row.row: {"top3": 0, "top1": 0, "frontier": 0} for row in rows}
    qualify = {reference: {row.row: 0 for row in rows} for reference in references}
    outcomes = {pair: {"win": 0, "tie": 0, "loss": 0} for pair in pairs}
    moments = {row.row: Comoments() for row in rows}
    for _ in range(n):
        scenario = draw_scenario(rows, stratum, rng, alternative=alternative, ranges=ranges)
        values = scenario_values(scenario, anchors, beta)
        for row_id, (cost, quality) in scenario.items():
            moments[row_id].add(anchor_math.cost_score(cost, anchors), quality)
        rank = ranks(values)
        for first, second in pairs:
            gap = values[first] - values[second]
            outcomes[(first, second)]["win" if gap > 0 else "loss" if gap < 0 else "tie"] += 1
        front = frontier_rows(scenario)
        for row in rows:
            counts[row.row]["top3"] += rank[row.row] <= 3
            counts[row.row]["top1"] += rank[row.row] == 1
            counts[row.row]["frontier"] += row.row in front
        for reference in references:
            bar = scenario[reference][1]
            for row in rows:
                qualify[reference][row.row] += scenario[row.row][1] >= bar
    result = {}
    for row in rows:
        entry = {}
        for key, count in counts[row.row].items():
            share = count / n
            entry[key] = {"share": share, "monteCarloSe": standard_error(share, n)}
        entry["qualifies"] = {reference: qualify[reference][row.row] / n for reference in references}
        entry["dispersion"] = moments[row.row].decomposition(beta)
        result[row.row] = entry
    pairwise = [{"pair": list(pair), **{key: count / n for key, count in counts_.items()}} for pair, counts_ in outcomes.items()]
    panel = sorted(row.row for row in rows)
    return {
        "stratum": stratum, "targetProfile": TARGET_PROFILES[stratum], "permittedTargets": sorted(STREAM_TARGETS[stratum]), "variedTargets": varied,
        "qualityEquation": QUALITY_EQUATIONS[stratum],
        "events": {
            "top1": "rank-1 frequency (competition ranks on value)", "top3": "rank 3 or better frequency (competition ranks on value)",
            "frontier": FRONTIER_EVENTS[stratum], "qualifies": f"qualifying-at-the-bar frequency ({QUALITY_EQUATIONS[stratum]})",
        },
        "scenarios": n, "seed": seed, "alternative": alternative,
        "panel": panel, "panelSize": len(panel), "rows": result, "pairwise": pairwise,
    }


def _beta_continued_fraction(a: float, b: float, x: float) -> float:
    """Continued fraction for the regularized incomplete beta function (modified Lentz)."""

    tiny = 1e-300
    c, d = 1.0, 1.0 - (a + b) * x / (a + 1.0)
    d = 1.0 / (d if abs(d) > tiny else tiny)
    result = d
    m, converged = 0, False
    while not converged:
        m += 1
        m2 = 2 * m
        for numerator in (m * (b - m) * x / ((a + m2 - 1.0) * (a + m2)), -(a + m) * (a + b + m) * x / ((a + m2) * (a + m2 + 1.0))):
            d = 1.0 + numerator * d
            d = 1.0 / (d if abs(d) > tiny else tiny)
            c = 1.0 + numerator / c
            c = c if abs(c) > tiny else tiny
            result *= d * c
        converged = abs(d * c - 1.0) < 1e-15 or m >= 10_000
    return result


def regularized_beta(x: float, a: float, b: float) -> float:
    """I_x(a, b), the CDF of Beta(a, b) at x."""

    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    front = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _beta_continued_fraction(a, b, x) / a
    return 1.0 - front * _beta_continued_fraction(b, a, 1.0 - x) / b


def _beta_quantile(target: float, a: float, b: float) -> float:
    low, high = 0.0, 1.0
    for _ in range(80):
        middle = (low + high) / 2.0
        low, high = (middle, high) if regularized_beta(middle, a, b) < target else (low, middle)
    return (low + high) / 2.0


def clopper_pearson(successes: int, n: int, alpha: float) -> tuple[float, float]:
    """Exact equal-tailed binomial interval with error allocation ``alpha`` (confidence 1 - alpha, alpha/2 per tail).

    ``alpha`` is the error allocation, not the confidence level (E150): SciPy's
    equivalent call takes ``confidence_level=1 - alpha``.
    """

    lower = 0.0 if successes == 0 else _beta_quantile(alpha / 2.0, successes, n - successes + 1)
    upper = 1.0 if successes == n else _beta_quantile(1.0 - alpha / 2.0, successes + 1, n - successes)
    return lower, upper


def sequential_threshold(event, rng: random.Random, *, threshold: float = THRESHOLD, alpha: float = ALPHA, batch: int = BATCH, looks: int = LOOKS) -> dict:
    """The E77 rule for one event: batches until the interval clears the threshold, else unresolved at the cap."""

    successes = trials = 0
    error = alpha / looks  # E150: Bonferroni error allocation per look; confidence level 1 - alpha / looks
    for look in range(1, looks + 1):
        for _ in range(batch):
            successes += bool(event(rng))
            trials += 1
        lower, upper = clopper_pearson(successes, trials, error)
        certificate = {
            "share": successes / trials, "successes": successes, "scenarios": trials, "interval": (lower, upper),
            "perLookError": error, "confidenceLevel": 1.0 - error, "tailAllocation": "equal (half the per-look error in each tail)",
        }
        if lower >= threshold:
            return {"status": "met", **certificate, "looks": look}
        if upper < threshold:
            return {"status": "not met", **certificate, "looks": look}
    return {"status": "scenario threshold unresolved", **certificate, "looks": looks}
