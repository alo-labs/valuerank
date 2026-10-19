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


def anchor_object(reference_costs: dict, *, basis: str, workload: str | None) -> dict:
    """The versioned anchor object: reference ids and costs, padded anchors, basis and workload."""

    costs = {key: float(value) for key, value in reference_costs.items() if value is not None}
    if not costs:
        raise ValueError(f"no reference costs for the {basis} anchors")
    if any(value <= 0 for value in costs.values()):
        raise ValueError("anchor reference costs must be positive")
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

    if cost is None or cost <= 0:
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
    """Within-cohort influence of cost: beta*SD(S_C) / (beta*SD(S_C) + (1-beta)*SD(S_Q)); informational flag below 10%."""

    if len(cost_scores) < 2 or len(quality_scores) < 2:
        return {"costShare": None, "flag": False}
    cost_sd = statistics.pstdev(cost_scores)
    quality_sd = statistics.pstdev(quality_scores)
    denominator = beta * cost_sd + (1.0 - beta) * quality_sd
    share = beta * cost_sd / denominator if denominator else None
    return {
        "costSd": cost_sd,
        "qualitySd": quality_sd,
        "costShare": share,
        "flag": share is not None and share < LOW_INFLUENCE_FLAG,
    }


def value_score(cost_score_value: float | None, quality: float | None, beta: float) -> float | None:
    """V = beta * S_C + (1 - beta) * Q; a row needs both a cost score and a quality score (no cost, no value score)."""

    if cost_score_value is None or quality is None:
        return None
    return beta * cost_score_value + (1.0 - beta) * quality
