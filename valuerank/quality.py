"""ValueRank v3 quality: the leaf table, normalisation, coverage and the provisional rule.

Every leaf is normalised on its raw magnitude with frozen anchors (never by rank),
so a model's quality does not move when another model enters or leaves the
cohort. Missing leaves stay missing: the displayed quality is the weighted mean
of the observed leaves, and the formal bounds put each missing leaf anywhere in
its 0-100 domain (owner decision O25: the interval outputs protect the published
record, so observed leaves contribute only their reporting-precision intervals).
"""

from __future__ import annotations

from dataclasses import dataclass

# Group shares of the quality score (percent); the leaf weights below sum to them.
GROUPS = {"swe": 60.0, "professional": 20.0, "reliability": 10.0, "knowledge": 10.0}
GROUP_LABELS = {
    "swe": "Software engineering",
    "professional": "General professional work",
    "reliability": "Reliability",
    "knowledge": "Long context, science & knowledge",
}
# Provisional rule thresholds (shares of total quality weight).
MIN_COVERAGE = 0.70
MIN_SWE_LEAVES = 2
MIN_SWE_WEIGHT = 0.40
REQUIRED_LEAF_WEIGHT = 20.0  # leaves at or above this nominal weight must be observed
GDPVAL_ELO_LOW = 500.0
GDPVAL_ELO_SPAN = 2000.0
BUG_HUNT_BUGS = 105.0


@dataclass(frozen=True)
class Leaf:
    key: str
    label: str
    group: str
    weight: float  # percent of quality
    source: str  # "aa" (AA-run) or "independent"


LEAVES = (
    Leaf("deepswe", "DeepSWE v1.1", "swe", 30.0, "aa"),
    Leaf("bugHunt", "Bug Hunt Bench", "swe", 10.0, "independent"),
    Leaf("frontierCode", "AA FrontierCode 1.1", "swe", 10.0, "aa"),
    Leaf("terminalBench", "Terminal-Bench 4.0 (tbench.ai)", "swe", 10.0, "independent"),
    Leaf("gdpval", "GDPval-AA v2.1", "professional", 10.0, "aa"),
    Leaf("automationBench", "AutomationBench-AA", "professional", 10.0, "aa"),
    # LiveBench instruction following is retired (owner decision O26): Omniscience takes the group's 10%.
    Leaf("omniscience", "AA-Omniscience", "reliability", 10.0, "aa"),
    Leaf("lcr", "AA-LCR v1.1", "knowledge", 5.0, "aa"),
    Leaf("hle", "Humanity's Last Exam", "knowledge", 5.0 / 3.0, "aa"),
    Leaf("scicode", "SciCode", "knowledge", 5.0 / 3.0, "aa"),
    Leaf("critpt", "CritPt", "knowledge", 5.0 / 3.0, "aa"),
)
LEAF_BY_KEY = {leaf.key: leaf for leaf in LEAVES}


@dataclass(frozen=True)
class Observation:
    """A published leaf value on its z scale with its reporting-precision half-width."""

    z: float
    half_width: float = 0.0

    @property
    def low(self) -> float:
        return max(0.0, self.z - self.half_width)

    @property
    def high(self) -> float:
        return min(100.0, self.z + self.half_width)


def clip(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def percent_z(value: float, half_width_pct: float = 0.0) -> Observation:
    """A 0-100 percentage on anchors 0 and 100."""

    return Observation(clip(value), half_width_pct)


def fraction_z(value: float, half_width: float = 0.0) -> Observation:
    """A 0-1 fraction on anchors 0 and 100%."""

    return Observation(clip(100.0 * value), 100.0 * half_width)


def gdpval_z(elo: float, half_width_elo: float = 0.0) -> Observation:
    """AA's integration transform for GDPval-AA: (Elo - 500) / 2000, clipped to 0-100%."""

    return Observation(clip(100.0 * (elo - GDPVAL_ELO_LOW) / GDPVAL_ELO_SPAN), 100.0 * half_width_elo / GDPVAL_ELO_SPAN)


def bug_hunt_z(bugs_fixed: float, half_width_bugs: float = 0.0) -> Observation:
    """Bugs fixed out of 105 (release test vector: 52 -> 49.52)."""

    return Observation(clip(100.0 * bugs_fixed / BUG_HUNT_BUGS), 100.0 * half_width_bugs / BUG_HUNT_BUGS)


def omniscience_z(accuracy: float, non_hallucination: float) -> Observation:
    """z = (2A + N) / 3 with A and N in percent (AA's Index integrates them 2:1 too)."""

    return Observation(clip((2.0 * 100.0 * accuracy + 100.0 * non_hallucination) / 3.0))


def omniscience_from_counts(correct: int, partial: int, incorrect: int, abstained: int) -> tuple[float, float, float]:
    """(A, N, z) from AA's counts; AA's hallucination rate is incorrect / all non-correct responses."""

    total = correct + partial + incorrect + abstained
    accuracy = 100.0 * correct / total
    non_correct = partial + incorrect + abstained
    non_hallucination = 100.0 if non_correct == 0 else 100.0 * (1.0 - incorrect / non_correct)
    return accuracy, non_hallucination, (2.0 * accuracy + non_hallucination) / 3.0


@dataclass(frozen=True)
class QualitySummary:
    observations: dict
    coverage: float  # observed share of total quality weight, 0-1
    displayed: float | None  # observed-only quality, 0-100
    lower: float  # formal bound with missing leaves at 0 and observed leaves at their low ends
    upper: float  # formal bound with missing leaves at 100 and observed leaves at their high ends
    provisional: bool
    provisional_reasons: tuple
    swe_leaves: int
    swe_weight: float  # observed SWE share of total quality weight, 0-1


def summarize(observations: dict) -> QualitySummary:
    """Coverage, displayed quality, formal bounds and the provisional rule for one row."""

    unknown = set(observations) - set(LEAF_BY_KEY)
    if unknown:
        raise ValueError(f"unknown quality leaves: {', '.join(sorted(unknown))}")
    observed = [leaf for leaf in LEAVES if leaf.key in observations]
    coverage = sum(leaf.weight for leaf in observed) / 100.0
    weighted = sum(leaf.weight * observations[leaf.key].z for leaf in observed)
    displayed = weighted / (100.0 * coverage) if coverage else None
    lower = sum(leaf.weight * observations[leaf.key].low for leaf in observed) / 100.0
    upper = (sum(leaf.weight * observations[leaf.key].high for leaf in observed) + 100.0 * (100.0 - 100.0 * coverage)) / 100.0
    swe = [leaf for leaf in observed if leaf.group == "swe"]
    swe_weight = sum(leaf.weight for leaf in swe) / 100.0
    reasons = []
    if coverage < MIN_COVERAGE - 1e-12:
        reasons.append(f"coverage {coverage:.0%} below {MIN_COVERAGE:.0%}")
    if len(swe) < MIN_SWE_LEAVES:
        reasons.append(f"{len(swe)} SWE leaves observed (need {MIN_SWE_LEAVES})")
    if swe_weight < MIN_SWE_WEIGHT - 1e-12:
        reasons.append(f"observed SWE weight {swe_weight:.0%} below {MIN_SWE_WEIGHT:.0%}")
    for leaf in LEAVES:
        if leaf.weight >= REQUIRED_LEAF_WEIGHT and leaf.key not in observations:
            reasons.append(f"{leaf.label} missing")
    return QualitySummary(
        observations=dict(observations),
        coverage=coverage,
        displayed=displayed,
        lower=lower,
        upper=upper,
        provisional=bool(reasons),
        provisional_reasons=tuple(reasons),
        swe_leaves=len(swe),
        swe_weight=swe_weight,
    )


def composite(values: dict) -> float:
    """Full-composite quality for one state: every leaf must have a value (observed or a missing-leaf draw)."""

    missing = [leaf.key for leaf in LEAVES if leaf.key not in values]
    if missing:
        raise ValueError(f"full composite needs every leaf; missing: {', '.join(missing)}")
    return sum(leaf.weight * values[leaf.key] for leaf in LEAVES) / 100.0


def source_shares() -> dict:
    """Share of nominal quality weight by data source (AA-run vs independent)."""

    shares: dict[str, float] = {}
    for leaf in LEAVES:
        shares[leaf.source] = shares.get(leaf.source, 0.0) + leaf.weight / 100.0
    return shares
