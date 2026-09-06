"""Resolve model-specific subscription routes into effective task costs.

The route file deliberately keeps evidence and eligibility next to the
arithmetic.  A missing route is not treated as free usage: callers receive an
explicit API fallback marker and can explain it in the UI.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROUTE_PATH = ROOT / ".refresh" / "v1.4" / "plan_cost_routes.json"
CONFIDENCE_ORDER = {"high": 4, "medium-high": 3, "medium": 2, "low-medium": 1, "low": 0}


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


def select_best_route(model_id: str, route_document: dict) -> dict | None:
    """Select the highest-multiple eligible route with deterministic tie-breaks."""

    candidates = _routes_for_model(model_id, route_document)
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


def rank_cost_scores(costs: list[float | int | None]) -> list[float | None]:
    """Convert lower-is-better costs to 0-100 scores with average ties."""

    numeric = [(index, float(value)) for index, value in enumerate(costs) if value is not None]
    if not numeric:
        return [None] * len(costs)
    ordered = sorted(value for _index, value in numeric)
    n = len(ordered)
    scores: list[float | None] = [None] * len(costs)
    for index, value in numeric:
        first = ordered.index(value) + 1
        last = n - ordered[::-1].index(value)
        average_rank = (first + last) / 2
        scores[index] = round(((n - average_rank) / (n - 1)) * 100, 6) if n > 1 else 50.0
    return scores


def build_cost_fields(models: list[dict], route_document: dict) -> list[dict]:
    """Return API and plan cost values plus normalized scores for each model."""

    api_costs = [model.get("deepsweCost", model.get("apiCost")) for model in models]
    routes = [select_best_route(model["id"], route_document) for model in models]
    plan_costs = [effective_cost(api_cost, route) for api_cost, route in zip(api_costs, routes)]
    comparable_plan_costs = [
        plan_cost if plan_cost is not None else api_cost
        for plan_cost, api_cost in zip(plan_costs, api_costs)
    ]
    api_scores = rank_cost_scores(api_costs)
    plan_scores = rank_cost_scores(comparable_plan_costs)
    result = []
    for api_cost, plan_cost, comparable, api_score, plan_score, route in zip(
        api_costs, plan_costs, comparable_plan_costs, api_scores, plan_scores, routes
    ):
        result.append(
            {
                "apiCost": api_cost,
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
