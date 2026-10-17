"""Plain-language picks (best value, best quality, best budget) for a ranking basis.

``build_picks(models, basis, bases)`` takes the ``rankings.json`` model entries and returns
``{"value": {...}|None, "quality": {...}|None, "budget": {...}|None}`` where each pick is
``{"slug", "reason"}``. ``value`` is rank 1 on the basis, ``quality`` is quality rank 1, and ``budget``
is the best-ranked model among the cheapest third by that basis' cost score. Reasons are built from
the data and stay under 25 words.
"""

from __future__ import annotations

import math


def _cost_text(model: dict, basis: str) -> str:
    cost = model["cost"]
    if basis == "api":
        value = cost["apiUsd"]
        return "with no cost data" if value is None else f"${value:,.2f} per Index run"
    value = cost["planComparableUsdPerPoint"]
    if value is None:
        return "with no cost data"
    suffix = " (API fallback)" if cost["fallback"] else ""
    return f"${value:,.2f} per Index point{suffix}"


def _pick(model: dict, reason: str) -> dict:
    return {"slug": model["slug"], "reason": reason}


def build_picks(models: list[dict], basis: str, bases: dict) -> dict:
    ranked = [model for model in models if model["rank"][basis] is not None]
    if not ranked:
        return {"value": None, "quality": None, "budget": None}
    label = bases[basis]["label"]
    value = min(ranked, key=lambda model: model["rank"][basis])
    quality = min(ranked, key=lambda model: (model["qualityRank"], model["rank"][basis]))
    priced = sorted(
        (model for model in ranked if model["costDims"][basis] is not None),
        key=lambda model: (-model["costDims"][basis], model["name"]),
    )
    cheapest_third = priced[: math.ceil(len(priced) / 3)]
    budget = min(cheapest_third, key=lambda model: model["rank"][basis]) if cheapest_third else None
    return {
        "value": _pick(
            value,
            f"{value['name']} has the highest overall score in the {label} at {value['overall'][basis]:.1f}, costing {_cost_text(value, basis)}.",
        ),
        "quality": _pick(
            quality,
            f"{quality['name']} has the best quality score ({quality['quality']:.1f}) before cost; it ranks #{quality['rank'][basis]} in the {label}.",
        ),
        "budget": None
        if budget is None
        else _pick(
            budget,
            f"{budget['name']} scores best overall ({budget['overall'][basis]:.1f}) among the cheapest third, at {_cost_text(budget, basis)}.",
        ),
    }
