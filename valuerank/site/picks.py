"""Plain-language picks for a ranking basis: three cards that show three different angles.

``build_picks(models, basis, bases)`` takes the ``rankings.json`` model entries and returns
``{"value": {...}|None, "other": {...}|None, "budget": {...}|None}``. Each pick is
``{"slug", "label", "reason", "score", "unit"}``.

* ``value`` is rank 1 on the active basis ("Best overall value").
* ``other`` is rank 1 on the other basis, labelled from ``bases[other]["pickLabel"]``. When that is
  the same model as ``value`` it becomes the quality leader and, if that is also ``value``, the
  runner-up overall, so the cards differ whenever the cohort allows.
* ``budget`` is the best overall model in the cheapest third by the basis' cost score. When that
  third holds several models, models already picked are skipped (unless that would empty it).

Reasons are built from the data and stay under 25 words; a subset-cost pick (O17) says its cross-workload
ordering is not identified. ``assets/js/scoring.js`` applies the same rule when the cost weight moves.
"""

from __future__ import annotations

import math


def _cost_text(model: dict, basis: str) -> str:
    """The basis' cost of one run of the SDLC basket (methodology v3); the Plan basis notes an API fallback."""

    cost = model["cost"]
    value = cost["apiUsd"] if basis == "api" else cost["planUsd"]
    if value is None:
        return "with no cost data"
    suffix = " (API fallback)" if basis == "plan" and cost["fallback"] else ""
    return f"${value:,.2f} per basket run{suffix}"


def _pick(model: dict, label: str, reason: str, score: float, unit: str) -> dict:
    # O17: a subset-cost row is scored on its own workload; its ordering against full-basket rows is not identified.
    if model["cost"]["subset"]:
        reason += " Subset cost: cross-workload ordering not identified."
    return {"slug": model["slug"], "label": label, "reason": reason, "score": score, "unit": unit}


def _other_pick(value: dict, ranked: list[dict], basis: str, other: str, bases: dict) -> dict | None:
    label = bases[basis]["label"]
    leader = min(
        (model for model in ranked if model["rank"][other] is not None),
        key=lambda model: model["rank"][other],
        default=None,
    )
    if leader is not None and leader is not value:
        phrase = bases[other]["pickPhrase"]
        return _pick(
            leader,
            bases[other]["pickLabel"],
            f"{leader['name']} ranks #1 {phrase} and #{leader['rank'][basis]} in the {label}.",
            leader["overall"][other],
            f"overall {phrase}",
        )
    quality = min(ranked, key=lambda model: (model["qualityRank"], model["rank"][basis]))
    if quality is not value:
        return _pick(
            quality,
            "Best quality, any cost",
            f"{quality['name']} has the best quality score ({quality['quality']:.1f}) before cost; it ranks #{quality['rank'][basis]} in the {label}.",
            quality["quality"],
            "quality",
        )
    runner_up = min((model for model in ranked if model is not value), key=lambda model: model["rank"][basis], default=None)
    if runner_up is None:
        return None
    return _pick(
        runner_up,
        "Runner-up overall",
        f"{runner_up['name']} is the runner-up in the {label} at {runner_up['overall'][basis]:.1f}.",
        runner_up["overall"][basis],
        "overall",
    )


def build_picks(models: list[dict], basis: str, bases: dict) -> dict:
    ranked = [model for model in models if model["rank"][basis] is not None]
    if not ranked:
        return {"value": None, "other": None, "budget": None}
    other_basis = next(key for key in bases if key != basis)
    label = bases[basis]["label"]
    value = min(ranked, key=lambda model: model["rank"][basis])
    other = _other_pick(value, ranked, basis, other_basis, bases)
    picked = {value["slug"], other["slug"] if other else None}
    priced = sorted(
        (model for model in ranked if model["costDims"][basis] is not None),
        key=lambda model: (-model["costDims"][basis], model["name"]),
    )
    cheapest_third = priced[: math.ceil(len(priced) / 3)]
    if len(cheapest_third) > 1:
        cheapest_third = [m for m in cheapest_third if m["slug"] not in picked] or cheapest_third
    budget = min(cheapest_third, key=lambda model: model["rank"][basis]) if cheapest_third else None
    return {
        "value": _pick(
            value,
            "Best overall value",
            f"{value['name']} has the highest overall score in the {label} at {value['overall'][basis]:.1f}, costing {_cost_text(value, basis)}.",
            value["overall"][basis],
            "overall",
        ),
        "other": other,
        "budget": None
        if budget is None
        else _pick(
            budget,
            "Best on a budget",
            f"{budget['name']} scores best overall ({budget['overall'][basis]:.1f}) among the cheapest third, at {_cost_text(budget, basis)}.",
            budget["overall"][basis],
            "overall",
        ),
    }
