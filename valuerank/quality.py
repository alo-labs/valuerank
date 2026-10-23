"""ValueRank v3 quality: the leaf table, normalisation, coverage and the provisional rule.

Every leaf is normalised on its raw magnitude with frozen anchors (never by rank),
so a model's quality does not move when another model enters or leaves the
cohort. Missing leaves stay missing: the displayed quality is the weighted mean
of the observed leaves, and the formal bounds put each missing leaf anywhere in
its 0-100 domain (owner decision O25: the interval outputs protect the published
record, so observed leaves contribute only their reporting-precision intervals).
"""

from __future__ import annotations

import math
from contextlib import contextmanager
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
AICD_POINTS = 60.0  # AI Coding Daily's Laravel quality, React-TS quality and edge-case columns (20 points each)


@dataclass(frozen=True)
class Leaf:
    key: str
    label: str
    group: str
    weight: float  # percent of quality
    source: str  # "aa" (AA-run) or "independent"


# The six leaves outside software engineering, shared by every ranking.
COMMON_LEAVES = (
    Leaf("gdpval", "GDPval-AA v2.1", "professional", 10.0, "aa"),
    Leaf("automationBench", "AutomationBench-AA", "professional", 10.0, "aa"),
    # LiveBench instruction following is retired (owner decision O26): Omniscience takes the group's 10%.
    Leaf("omniscience", "AA-Omniscience", "reliability", 10.0, "aa"),
    Leaf("lcr", "AA-LCR v1.1", "knowledge", 5.0, "aa"),
    Leaf("hle", "Humanity's Last Exam", "knowledge", 5.0 / 3.0, "aa"),
    Leaf("scicode", "SciCode", "knowledge", 5.0 / 3.0, "aa"),
    Leaf("critpt", "CritPt", "knowledge", 5.0 / 3.0, "aa"),
)
# Owner decisions O53-O55 (2026-10-23): ValueRank publishes two rankings, each over the configurations with its complete
# leaf set (O36, O52). The max-effort ranking adds LiveBench 2.0 Overall (O61, 2026-10-23: the mean of its seven
# categories, all needed in the SDLC, weighted above every single AA leaf) and two Vals boards, run at each vendor's top effort;
# the AI Coding Daily ranking adds AI Coding Daily (its bug-finding column excluded: it overlaps Bug Hunt). O49 dropped
# DeepSWE; software engineering stays 60% of quality in both.
TRACKS = {
    "max": (
        Leaf("frontierCode", "FrontierCode 1.1", "swe", 15.0, "aa"),
        Leaf("terminalBench", "Terminal-Bench 4.0 (AA run)", "swe", 11.0, "aa"),
        Leaf("bugHunt", "Bug Hunt Bench", "swe", 8.0, "independent"),
        Leaf("vibeCode", "Vibe Code Bench v1.1 (Vals)", "swe", 5.0, "independent"),
        Leaf("codeMigration", "Code Migration v1.1 (Vals)", "swe", 6.0, "independent"),
        Leaf("livebench2Overall", "LiveBench 2.0 Overall", "swe", 15.0, "independent"),
        *COMMON_LEAVES,
    ),
    "aicd": (
        Leaf("frontierCode", "FrontierCode 1.1", "swe", 21.0, "aa"),
        Leaf("terminalBench", "Terminal-Bench 4.0 (AA run)", "swe", 17.0, "aa"),
        Leaf("bugHunt", "Bug Hunt Bench", "swe", 12.0, "independent"),
        Leaf("aiCodingDaily", "AI Coding Daily (excl. bug finding)", "swe", 10.0, "independent"),
        *COMMON_LEAVES,
    ),
}
TRACK_LABELS = {"max": "Max-effort ranking", "aicd": "AI Coding Daily ranking"}
TRACK_NAMES = {"max": "max-effort ranking", "aicd": "AI Coding Daily ranking"}  # in a sentence
DEFAULT_TRACK = "max"  # O54: the max-effort ranking leads
# Every leaf of every ranking, for labels and domains.
ALL_LEAVES = {leaf.key: leaf for track in TRACKS.values() for leaf in track}

# The active ranking's leaves; every scoring function reads these, and ``active_track`` switches them.
TRACK = DEFAULT_TRACK
LEAVES = TRACKS[TRACK]
LEAF_BY_KEY = {leaf.key: leaf for leaf in LEAVES}


@contextmanager
def active_track(track: str):
    """Score inside one ranking: the module's leaf table is that ranking's for the duration of the block."""

    global TRACK, LEAVES, LEAF_BY_KEY
    previous = TRACK
    TRACK, LEAVES, LEAF_BY_KEY = track, TRACKS[track], {leaf.key: leaf for leaf in TRACKS[track]}
    try:
        yield TRACKS[track]
    finally:
        TRACK, LEAVES, LEAF_BY_KEY = previous, TRACKS[previous], {leaf.key: leaf for leaf in TRACKS[previous]}


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


# E181: the specification-layer alternative for GDPval-AA, the win probability against AA's pinned scale anchor
# (DeepSeek V4.1 Flash (max) at 1600) on the conventional Elo scale (AA does not state its scale factor).
GDPVAL_ANCHOR_ELO = 1600.0
ELO_SCALE = 400.0


def gdpval_logistic_z(elo: float) -> float:
    """z = 100 / (1 + 10^((E_A - E) / 400)): the logistic win probability against AA's anchor, in percent."""

    return 100.0 / (1.0 + 10.0 ** ((GDPVAL_ANCHOR_ELO - elo) / ELO_SCALE))


def aicd_z(points: float) -> Observation:
    """AI Coding Daily points out of 60 (bug-finding column excluded), on anchors 0 and 60."""

    return Observation(clip(100.0 * points / AICD_POINTS))


def bug_hunt_z(bugs_fixed: float, half_width_bugs: float = 0.0) -> Observation:
    """Bugs fixed out of 105 (release test vector: 52 -> 49.52)."""

    return Observation(clip(100.0 * bugs_fixed / BUG_HUNT_BUGS), 100.0 * half_width_bugs / BUG_HUNT_BUGS)


def omniscience_index_z(index: float) -> Observation:
    """Owner decision O28: z = (I + 100) / 2 for AA's Omniscience Index I in [-100, 100] (monotone in outcomes)."""

    return Observation(clip((index + 100.0) / 2.0))


def omniscience_index_from_rates(accuracy: float, hallucination_rate: float) -> float:
    """I = 100 [A - h (1 - A)] from AA's accuracy and conditional hallucination rate (fractions): the reconciliation check."""

    return 100.0 * (accuracy - hallucination_rate * (1.0 - accuracy))


def omniscience_from_counts(correct: int, partial: int, incorrect: int, abstained: int) -> tuple[float, float]:
    """(I, z) from AA's counts: I = 100 (correct - incorrect) / all questions; partial answers and abstentions count zero."""

    index = 100.0 * (correct - incorrect) / (correct + partial + incorrect + abstained)
    return index, omniscience_index_z(index).z


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


# E110: each leaf's documented raw domain (unit, low, high); a value outside it is a data-validation error.
LEAF_DOMAINS = {
    "bugHunt": ("bugs fixed of 105", 0.0, BUG_HUNT_BUGS),
    "frontierCode": ("fraction", 0.0, 1.0),
    "terminalBench": ("percent", 0.0, 100.0),
    "gdpval": ("Elo", -math.inf, math.inf),
    "automationBench": ("fraction", 0.0, 1.0),
    "omniscience": ("AA Omniscience Index", -100.0, 100.0),
    "lcr": ("fraction", 0.0, 1.0),
    "hle": ("fraction", 0.0, 1.0),
    "scicode": ("fraction", 0.0, 1.0),
    "critpt": ("fraction", 0.0, 1.0),
    "vibeCode": ("percent", 0.0, 100.0),
    "codeMigration": ("percent", 0.0, 100.0),
    "livebench2Overall": ("percent", 0.0, 100.0),
    "aiCodingDaily": ("points of 60", 0.0, AICD_POINTS),
}


def unclipped_z(key: str, raw) -> float:
    """The leaf's z before clipping to 0-100 (the value kept in the data release)."""

    if key == "omniscience":
        return (raw + 100.0) / 2.0
    if key == "gdpval":
        return 100.0 * (raw - GDPVAL_ELO_LOW) / GDPVAL_ELO_SPAN
    if key == "bugHunt":
        return 100.0 * raw / BUG_HUNT_BUGS
    if key == "aiCodingDaily":
        return 100.0 * raw / AICD_POINTS
    return raw if LEAF_DOMAINS[key][0] == "percent" else 100.0 * raw


def clip_audit(key: str, raw) -> dict:
    """E110: domain validity, anchor position, clipping amount, affected weight and action for one observation."""

    unit, low, high = LEAF_DOMAINS[key]
    valid = isinstance(raw, (int, float)) and not isinstance(raw, bool) and math.isfinite(raw) and low <= raw <= high
    z = unclipped_z(key, raw) if valid else None
    position = None if z is None else "below" if z < 0.0 else "above" if z > 100.0 else "inside"
    if not valid:
        action = "reject: outside the metric's documented domain"
    else:
        action = "none" if position == "inside" else "disclose saturation"
    return {
        "leaf": key,
        "raw": raw,
        "unit": unit,
        "domainValid": valid,
        "anchorPosition": position,
        "unclippedZ": z,
        "clippingAmount": None if z is None else z - clip(z),
        "weight": LEAF_BY_KEY[key].weight if key in LEAF_BY_KEY else ALL_LEAVES[key].weight,
        "action": action,
    }


def source_shares() -> dict:
    """Share of nominal quality weight by data source (AA-run vs independent)."""

    shares: dict[str, float] = {}
    for leaf in LEAVES:
        shares[leaf.source] = shares.get(leaf.source, 0.0) + leaf.weight / 100.0
    return shares
