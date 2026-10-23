"""Frozen cost anchors, the log-scale cost score, the clip gate and the exchange-rate disclosures (E20, E60).

Anchors are frozen per basis and workload from a named reference cohort: c_L is
half the cheapest reference cost and c_H twice the dearest, so the reference
cohort itself never clips. Scores keep their unclipped value alongside the
clipped one. The clip gate is the single governing predicate: a basis holds the
release (owner decision O12) when more than max(1, 10% of ranked rows) clip, or
any row lies beyond an anchor by more than a factor of 2.
"""

from __future__ import annotations

import math
import statistics

PADDING = 2.0
CLIP_SHARE_LIMIT = 0.10
BEYOND_FACTOR_LIMIT = 2.0
LOW_INFLUENCE_FLAG = 0.10
MIN_ALLOCATION_ROWS = 3  # I38: a two-row variance split is determined by construction
HIGH_INFLUENCE_FLAG = 0.90  # E126: the mirror flag, quality not discriminating


def scoreable(value) -> bool:
    """E109: a cost or multiple usable on the log scale or as a divisor: finite and strictly positive."""

    return isinstance(value, (int, float)) and not isinstance(value, bool) and 0 < value < math.inf


def anchor_object(reference_costs: dict, *, basis: str, workload: str | None) -> dict:
    """The versioned anchor object: reference ids and costs, padded anchors, basis and workload."""

    costs = {key: float(value) for key, value in reference_costs.items() if value is not None}
    if not costs:
        raise ValueError(f"no reference costs for the {basis} anchors")
    if not all(scoreable(value) for value in costs.values()):
        raise ValueError("anchor reference costs must be finite and positive")
    return {
        "basis": basis,
        "workload": workload,
        "units": "USD per workload pass",
        "referenceIds": sorted(costs),
        "referenceCosts": {key: costs[key] for key in sorted(costs)},
        "low": min(costs.values()) / PADDING,
        "high": max(costs.values()) * PADDING,
        "padding": PADDING,
    }


def unclipped_score(cost: float, anchors: dict) -> float:
    low, high = math.log(anchors["low"]), math.log(anchors["high"])
    return 100.0 * (high - math.log(cost)) / (high - low)


def cost_score(cost: float | None, anchors: dict) -> float | None:
    """S_C = 100 * clip((ln c_H - ln c) / (ln c_H - ln c_L), 0, 1); a missing or non-positive cost has none."""

    if not scoreable(cost):
        return None
    return max(0.0, min(100.0, unclipped_score(cost, anchors)))


def beyond_factor(cost: float, anchors: dict) -> float:
    """How far a cost lies outside the anchors, as a ratio (1.0 when inside)."""

    if cost < anchors["low"]:
        return anchors["low"] / cost
    if cost > anchors["high"]:
        return cost / anchors["high"]
    return 1.0


def clip_gate(costs: dict, anchors: dict) -> dict:
    """The single clip predicate for one basis: clipped rows, the allowance and whether the release holds."""

    known = {key: value for key, value in costs.items() if value is not None and value > 0}
    clipped = sorted(key for key, value in known.items() if beyond_factor(value, anchors) > 1.0)
    far = sorted(key for key, value in known.items() if beyond_factor(value, anchors) > BEYOND_FACTOR_LIMIT)
    allowance = max(1.0, CLIP_SHARE_LIMIT * len(known))
    return {
        "basis": anchors["basis"],
        "rows": len(known),
        "clipped": clipped,
        "allowance": allowance,
        "beyondFactorLimit": far,
        "hold": len(clipped) > allowance or bool(far),
    }


def exchange_rate(anchors: dict, beta: float) -> dict:
    """Value points lost per cost doubling, and the quality points that offset it (unclipped region)."""

    span = math.log(anchors["high"] / anchors["low"])
    value_points = 100.0 * beta * math.log(2.0) / span
    return {
        "valuePointsPerCostDoubling": value_points,
        "qualityPointsPerCostDoubling": value_points / (1.0 - beta),
        "anchorRatio": anchors["high"] / anchors["low"],
    }


def exchange_rate_curve(beta: float, ratios: list[float]) -> list[dict]:
    """The exchange rate as a function of the anchor ratio c_H / c_L (E60 sensitivity curve)."""

    return [
        {"anchorRatio": ratio, **{k: v for k, v in exchange_rate({"low": 1.0, "high": ratio}, beta).items() if k != "anchorRatio"}}
        for ratio in ratios
    ]


def cost_influence(cost_scores: list[float], quality_scores: list[float], beta: float) -> dict:
    """Within-cohort influence of cost: beta*SD(S_C) / (beta*SD(S_C) + (1-beta)*SD(S_Q)).

    Informational flags (E91, E126): ``flag`` below 10% (cost not discriminating) and
    ``qualityFlag`` above 90% (quality not discriminating); beta never changes.
    """

    if len(cost_scores) < 2 or len(quality_scores) < 2:
        return {"costShare": None, "flag": False, "qualityFlag": False, "varianceAllocation": None}
    cost_sd = statistics.pstdev(cost_scores)
    quality_sd = statistics.pstdev(quality_scores)
    denominator = beta * cost_sd + (1.0 - beta) * quality_sd
    share = beta * cost_sd / denominator if denominator else None
    return {
        "costSd": cost_sd,
        "qualitySd": quality_sd,
        "costShare": share,
        "flag": share is not None and share < LOW_INFLUENCE_FLAG,
        "qualityFlag": share is not None and share > HIGH_INFLUENCE_FLAG,
        "varianceAllocation": variance_allocation(cost_scores, quality_scores, beta),
    }


def variance_allocation(cost_scores: list[float], quality_scores: list[float], beta: float) -> dict | None:
    """E189: Cov(beta S_C, V) / Var(V) and Cov((1 - beta) Q, V) / Var(V), which sum to 1 (population moments).

    Cost and quality covary across a cohort, so the SD ratio above describes dispersion; this splits the value
    variance into what each term contributes. None when the value scores do not vary, and below three rows, where the
    two terms' deviations are tied by construction and the split carries no information (I38).
    """

    if len(cost_scores) < MIN_ALLOCATION_ROWS:
        return None
    values = [beta * cost + (1.0 - beta) * quality for cost, quality in zip(cost_scores, quality_scores)]
    centre, cost_mean, quality_mean = statistics.fmean(values), statistics.fmean(cost_scores), statistics.fmean(quality_scores)
    variance = statistics.fmean([(value - centre) ** 2 for value in values])
    if variance <= 0:
        return None
    cost_part = statistics.fmean([beta * (cost - cost_mean) * (value - centre) for cost, value in zip(cost_scores, values)])
    quality_part = statistics.fmean([(1.0 - beta) * (quality - quality_mean) * (value - centre) for quality, value in zip(quality_scores, values)])
    return {"cost": cost_part / variance, "quality": quality_part / variance}


ONE_CONFIGURATION = "undefined (one configuration)"


def _influence_status(rows: list[dict], result: dict) -> str:
    if len(rows) < 2:
        return "undefined (panel too small)"
    return "defined" if result["costShare"] is not None else "undefined — no composite dispersion"


def panel_cost_influence(rows: list[dict], beta: float, main_workload: str) -> dict:
    """E91: cost influence on the common-workload panel, per subset stratum, and over the displayed table.

    Each row is {"id", "workloadId", "costScore", "qualityScore"}. The headline
    statistic and its 10% flag use only the rows scored on the main workload with
    its anchor object (the same rows for both SDs); subset workloads get their own
    statistic; the whole-table value mixes anchor objects and is labelled
    "displayed-table dispersion".
    """

    scored = [row for row in rows if row["costScore"] is not None and row["qualityScore"] is not None]

    def summarise(panel: list[dict]) -> dict:
        # I54 L1: a Plan panel's rows are (configuration, plan) pairs; with one configuration the quality spread is zero
        # by construction, so the statistics are undefined rather than "quality not discriminating".
        configurations = {row.get("configurationId") or row["id"].split("@")[0] for row in panel}
        if len(panel) >= 2 and len(configurations) < 2:
            return {**cost_influence([], [], beta), "status": ONE_CONFIGURATION, "panel": sorted(row["id"] for row in panel)}
        result = cost_influence([row["costScore"] for row in panel], [row["qualityScore"] for row in panel], beta)
        return {**result, "status": _influence_status(panel, result), "panel": sorted(row["id"] for row in panel)}

    main = [row for row in scored if row["workloadId"] == main_workload]
    headline = summarise(main)
    headline["excluded"] = sorted(row["id"] for row in rows if row not in main)
    strata = {}
    for workload in sorted({row["workloadId"] for row in scored} - {main_workload}):
        strata[workload] = summarise([row for row in scored if row["workloadId"] == workload])
    return {
        "commonWorkload": headline,
        "subsetStrata": strata,
        "displayedTableDispersion": summarise(scored),
        "flag": headline["flag"],
        "qualityFlag": headline["qualityFlag"],
    }


def trimmed_anchor_object(reference_costs: dict, *, basis: str, workload: str | None, low_pct: float = 10.0, high_pct: float = 90.0) -> dict:
    """E126 diagnostic: anchors from the 10th and 90th percentile reference costs with the same padding (never primary)."""

    costs = sorted(float(value) for value in reference_costs.values() if scoreable(value))
    if len(costs) < 2:
        raise ValueError(f"the trimmed {basis} anchors need at least two reference costs")

    def percentile(pct: float) -> float:
        position = (len(costs) - 1) * pct / 100.0
        lower = int(position)
        upper = min(lower + 1, len(costs) - 1)
        return costs[lower] + (costs[upper] - costs[lower]) * (position - lower)

    return {
        "basis": basis,
        "workload": workload,
        "units": "USD per workload pass",
        "rule": f"P{low_pct:g} / {PADDING:g} and P{high_pct:g} x {PADDING:g} (diagnostic only)",
        "low": percentile(low_pct) / PADDING,
        "high": percentile(high_pct) * PADDING,
        "padding": PADDING,
    }


def value_score(cost_score_value: float | None, quality: float | None, beta: float) -> float | None:
    """V = beta * S_C + (1 - beta) * Q; a row needs both a cost score and a quality score (no cost, no value score)."""

    if cost_score_value is None or quality is None:
        return None
    return beta * cost_score_value + (1.0 - beta) * quality
