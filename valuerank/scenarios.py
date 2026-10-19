"""The scenario engine (Uncertainty layers S0/S1/S2, draw kernels E25, sequential precision E72/E77).

Each scenario draws:

- S0 (measurement): observed leaf values from their kernels (uniform on a
  published interval, or a run-level bootstrap of public repeated runs) and
  cost from its kernel; quality is the observed-only renormalised composite.
- S1 (identification): S0 plus a value for every missing leaf from the declared
  convention (uniform on 0-100; the published alternative draws uniformly on
  the cohort's observed range for that leaf); quality is the full composite.
- S2 core: S1 plus a hierarchical Dirichlet weight draw around the nominal
  weights (group ~ Dirichlet(100 x group shares), within group ~
  Dirichlet(50 x within-group proportions)).

Results are scenario frequencies per stratum, never probabilities, each with a
Monte Carlo standard error. Threshold labels (90%) use the sequential rule:
looks every 10,000 scenarios up to 160,000, an exact Clopper-Pearson interval at
level alpha/16 per look, "met" when the lower bound >= 0.90, "not met" when the
upper bound < 0.90, otherwise continue, ending "unresolved" at the cap.
"""

from __future__ import annotations

import itertools
import math
import random
from dataclasses import dataclass, field

from valuerank import anchors as anchor_math
from valuerank import quality as q

STRATA = ("S0", "S1", "S2")
GROUP_CONCENTRATION = 100.0
LEAF_CONCENTRATION = 50.0
BATCH = 10_000
MAX_SCENARIOS = 160_000
LOOKS = MAX_SCENARIOS // BATCH
ALPHA = 0.05
THRESHOLD = 0.90


@dataclass(frozen=True)
class Kernel:
    """A draw kernel: 'fixed' (value), 'uniform' (low, high) or 'runs' (public run values to bootstrap)."""

    family: str
    params: tuple
    alternative: str | None = None  # 'endpoint-heavy' for interval-only inputs

    def draw(self, rng: random.Random, *, use_alternative: bool = False) -> float:
        if self.family == "fixed":
            return self.params[0]
        if self.family == "uniform":
            low, high = self.params
            if use_alternative and self.alternative == "endpoint-heavy":
                return low + (high - low) * rng.betavariate(0.5, 0.5)
            return rng.uniform(low, high)
        if self.family == "runs":
            values = self.params
            return sum(rng.choice(values) for _ in values) / len(values)
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
                    values[leaf.key] = Kernel("uniform", (low, high), "endpoint-heavy").draw(rng, use_alternative=heavy)
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

    def event(generator):
        scenario = draw_scenario(rows, stratum, generator, alternative=alternative, alternative_rows=alternative_rows)
        return cheapest_qualifier(scenario, reference) == candidate

    outcome = sequential_threshold(event, rng, **rule)
    eligible = not next(row.provisional for row in rows if row.row == candidate)
    # E100/E112: only the full-composite S1 core branch, under each of its pre-registered kernels, authorises the label.
    authorized = stratum == LABEL_STRATUM
    signature = {
        "qualityEquation": "observed leaves" if stratum == "S0" else "full composite",
        "scenarioStratum": stratum,
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
    assignments, seen = [], set()
    for flags in itertools.product((False, True), repeat=len(BLOCKS)):
        heavy = frozenset().union(*(members[block] for block, flag in zip(BLOCKS, flags) if flag))
        light = frozenset().union(*(members[block] for block, flag in zip(BLOCKS, flags) if not flag))
        if heavy & light or heavy in seen:
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
    for index, assignment in enumerate(kernel_assignments(rows, candidate, reference)):
        runs[assignment["id"]] = scenario_supported_cheapest(
            rows, candidate, reference, LABEL_STRATUM, random.Random(seed + index), alternative_rows=assignment["endpointHeavyRows"], **rule
        )
    primary = runs["UUU"]
    met = all(run["status"] == "met" for run in runs.values())
    eligible = primary["uniqueLabelEligible"]
    if met and eligible:
        reading = "supported under the registered kernel checks (block-exhaustive over candidate, reference and competitors)"
    elif primary["status"] == "met":
        reading = "primary-kernel frequency >= 90%; kernel-sensitive" if eligible else "frequency only (provisional row)"
    else:
        reading = "not scenario-supported"
    shares_ = [run["share"] for run in runs.values()]
    return {"assignments": runs, "coverage": "block-exhaustive", "frequencyRange": [min(shares_), max(shares_)], "label": met and eligible, "reading": reading}


def standard_error(share: float, n: int) -> float:
    return math.sqrt(share * (1.0 - share) / n) if n else 0.0


def shares(rows: list[RowInputs], stratum: str, n: int, seed: int, anchors: dict, beta: float, *, references: tuple = (), pairs: tuple = (), alternative: bool = False) -> dict:
    """Per-row scenario frequencies for one stratum: rank <= 3, rank 1, frontier, per-bar qualification.

    E96: the panel is the declared row set, fixed for every scenario; ranks are
    competition ranks (ties share the better rank, so more than k rows can hold
    rank <= k); each declared pair (i, j) reports win, tie and loss frequencies
    for V_i against V_j.
    """

    rng = random.Random(seed)
    ranges = None
    counts = {row.row: {"top3": 0, "top1": 0, "frontier": 0} for row in rows}
    qualify = {reference: {row.row: 0 for row in rows} for reference in references}
    outcomes = {pair: {"win": 0, "tie": 0, "loss": 0} for pair in pairs}
    for _ in range(n):
        scenario = draw_scenario(rows, stratum, rng, alternative=alternative, ranges=ranges)
        values = scenario_values(scenario, anchors, beta)
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
        result[row.row] = entry
    pairwise = [{"pair": list(pair), **{key: count / n for key, count in counts_.items()}} for pair, counts_ in outcomes.items()]
    panel = sorted(row.row for row in rows)
    return {"stratum": stratum, "scenarios": n, "seed": seed, "alternative": alternative, "panel": panel, "panelSize": len(panel), "rows": result, "pairwise": pairwise}


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
    """Exact two-sided binomial interval at level alpha, from Beta quantiles."""

    lower = 0.0 if successes == 0 else _beta_quantile(alpha / 2.0, successes, n - successes + 1)
    upper = 1.0 if successes == n else _beta_quantile(1.0 - alpha / 2.0, successes + 1, n - successes)
    return lower, upper


def sequential_threshold(event, rng: random.Random, *, threshold: float = THRESHOLD, alpha: float = ALPHA, batch: int = BATCH, looks: int = LOOKS) -> dict:
    """The E77 rule for one event: batches until the interval clears the threshold, else unresolved at the cap."""

    successes = trials = 0
    for look in range(1, looks + 1):
        for _ in range(batch):
            successes += bool(event(rng))
            trials += 1
        lower, upper = clopper_pearson(successes, trials, alpha / looks)
        if lower >= threshold:
            return {"status": "met", "share": successes / trials, "scenarios": trials, "interval": (lower, upper), "looks": look}
        if upper < threshold:
            return {"status": "not met", "share": successes / trials, "scenarios": trials, "interval": (lower, upper), "looks": look}
    return {"status": "scenario threshold unresolved", "share": successes / trials, "scenarios": trials, "interval": (lower, upper), "looks": looks}
