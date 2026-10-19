"""Resolve model-specific subscription routes into effective AA evaluation costs.

The route file deliberately keeps evidence and eligibility next to the
arithmetic. A missing route is not treated as free usage: callers receive an
explicit API fallback marker and can explain it in the UI.

This module also owns the value rule shared by ``build_scores``, the site view
models and the site JavaScript: both bases compare cost per AA Intelligence
Index point, scored on a log scale, and cost carries a fixed ``COST_WEIGHT_PCT``
share of every overall score.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path


from valuerank.paths import DATA, ROOT
DEFAULT_ROUTE_PATH = DATA / "plan_cost_routes.json"
CONFIDENCE_ORDER = {"high": 4, "medium-high": 3, "medium": 2, "low-medium": 1, "low": 0}
# Cost's fixed share of the overall score on both bases; the quality dimensions share the rest.
COST_WEIGHT_PCT = 25.0


def load_plan_routes(path: str | Path = DEFAULT_ROUTE_PATH) -> dict:
    document = json.loads(Path(path).read_text())
    if not isinstance(document.get("routes"), list):
        raise ValueError("plan route document must contain a routes list")
    for route in document["routes"]:
        multiple = route.get("valueMultiple")
        if not route.get("id") or not route.get("modelIds") or not isinstance(multiple, (int, float)) or multiple <= 0:
            raise ValueError(f"invalid plan route: {route.get('id', '<missing id>')}")
    return document


def _routes_for_model(model_id: str, route_document: dict) -> list[dict]:
    return [route for route in route_document["routes"] if model_id in route.get("modelIds", [])]


def select_best_route(
    model_id: str, route_document: dict, evaluated_variant: str | None = None
) -> dict | None:
    """Select an eligible route; variant-restricted evidence requires an exact match."""

    candidates = [
        route
        for route in _routes_for_model(model_id, route_document)
        if route.get("requiredVariant") is None or route["requiredVariant"] == evaluated_variant
    ]
    if not candidates:
        return None
    return max(
        candidates,
        key=lambda route: (
            float(route["valueMultiple"]),
            CONFIDENCE_ORDER.get(route.get("confidence", "low"), -1),
            route.get("id", ""),
        ),
    )


def opencode_go_tiers(route_document: dict) -> list[dict]:
    return sorted(
        (
            route
            for route in route_document["routes"]
            if route.get("provider") == "OpenCode" and route.get("plan") == "Go"
        ),
        key=lambda route: route["usageUsd"],
    )


def effective_cost(api_cost: float | int | None, route: dict | None) -> float | None:
    if api_cost is None or route is None:
        return None
    multiple = route.get("valueMultiple")
    if not isinstance(multiple, (int, float)) or multiple <= 0:
        return None
    return float(api_cost) / float(multiple)


def cost_per_index_point(cost: float | int | None, intelligence_index) -> float | None:
    """Express a cost in USD per AA Intelligence Index point.

    Dividing by the achieved intelligence credits token-efficient models: a
    plan allowance buys more work from a model that reaches a given score
    with fewer dollars. Without a positive numeric index there is no rate.
    """

    if cost is None or isinstance(intelligence_index, bool) or not isinstance(intelligence_index, (int, float)):
        return None
    if intelligence_index <= 0:
        return None
    return float(cost) / float(intelligence_index)


def cost_scores(costs: list[float | int | None]) -> list[float | None]:
    """Convert lower-is-better costs to 0-100 scores on a log scale.

    The cheapest known cost scores 100 and the dearest 0; in between, equal cost
    ratios move the score by equal amounts, so a model ten times dearer than
    another is penalised by the same distance wherever it sits on the scale.
    When every known cost is equal there is no spread to compare and each scores 50.
    """

    numeric = [(index, float(value)) for index, value in enumerate(costs) if value is not None]
    for _index, value in numeric:
        if value <= 0:
            raise ValueError("cost scores need positive costs")
    scores: list[float | None] = [None] * len(costs)
    if not numeric:
        return scores
    low = math.log(min(value for _index, value in numeric))
    high = math.log(max(value for _index, value in numeric))
    for index, value in numeric:
        # One decimal, the precision of every dimension stored in scores.json, so a composite
        # recomputed from the public data reproduces the committed score exactly.
        scores[index] = round(100 * (high - math.log(value)) / (high - low), 1) if high > low else 50.0
    return scores


def blend(cost_score: float | None, quality_score: float | None, cost_weight_pct: float = COST_WEIGHT_PCT) -> float | None:
    """Overall score: cost carries ``cost_weight_pct`` and quality the rest.

    A model without a quality score has no overall score; a model without a cost
    score is scored on quality alone. Neither gap is filled in.
    """

    if quality_score is None:
        return None
    if cost_score is None:
        return round(quality_score, 1)
    share = cost_weight_pct / 100
    return round(share * cost_score + (1 - share) * quality_score, 1)


def build_cost_fields(models: list[dict], route_document: dict) -> list[dict]:
    """Return API and plan cost values plus normalized scores for each model.

    ``apiCost`` is the AA total evaluation cost (USD per Index run) and
    ``apiCostPerPoint`` divides it by the model's AA Intelligence Index (USD
    per Index point), which is what the API-basis rank compares.
    ``planCostPerRun`` divides the run cost by the selected route's Value
    Multiple, and ``planCost`` divides that by the Index, which is what the
    Plan-basis rank compares. A model without an eligible route is not
    treated as free usage: it is compared on API cost per Index point and
    carries an explicit fallback marker. Both scores come from ``cost_scores``.
    """

    api_costs = [model.get("aaEvalCost") for model in models]
    indices = [model.get("intelligenceIndex") for model in models]
    routes = [select_best_route(model["id"], route_document, model.get("aaVariant")) for model in models]
    api_point_costs = [cost_per_index_point(api_cost, index) for api_cost, index in zip(api_costs, indices)]
    plan_run_costs = [effective_cost(api_cost, route) for api_cost, route in zip(api_costs, routes)]
    plan_costs = [cost_per_index_point(run_cost, index) for run_cost, index in zip(plan_run_costs, indices)]
    comparable_plan_costs = [
        plan_cost if plan_cost is not None else api_point_cost
        for plan_cost, api_point_cost in zip(plan_costs, api_point_costs)
    ]
    api_scores = cost_scores(api_point_costs)
    plan_scores = cost_scores(comparable_plan_costs)
    result = []
    for api_cost, api_point_cost, index, run_cost, plan_cost, comparable, api_score, plan_score, route in zip(
        api_costs, api_point_costs, indices, plan_run_costs, plan_costs, comparable_plan_costs, api_scores, plan_scores, routes
    ):
        result.append(
            {
                "apiCost": api_cost,
                "apiCostPerPoint": api_point_cost,
                "intelligenceIndex": index,
                "planCostPerRun": run_cost,
                "planCost": plan_cost,
                "planComparableCost": comparable,
                "apiCostScore": api_score,
                "planCostScore": plan_score,
                "planRoute": route,
                "planCostFallback": "api" if route is None else None,
            }
        )
    return result


def route_summary(route_document: dict, fields: list[dict]) -> dict:
    supported = sum(1 for field in fields if field["planRoute"] is not None)
    return {
        "asOf": route_document.get("asOf"),
        "routeCount": len(route_document["routes"]),
        "supportedModelCount": supported,
        "fallbackModelCount": len(fields) - supported,
        "mixId": route_document.get("costMix", {}).get("id"),
    }
