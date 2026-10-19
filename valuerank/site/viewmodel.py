"""Server-side view models for the multi-page site (docs/site-data-contract.md).

Entry point: ``build_bundle(data: Path = DATA) -> Bundle`` computes every public JSON document once:

* ``bundle.rankings``   -> ``site/data/rankings.json``
* ``bundle.models``     -> ``site/data/models/<slug>.json`` (dict slug -> document)
* ``bundle.plans``      -> ``site/data/plans.json``
* ``bundle.benchmarks`` -> ``site/data/benchmarks.json``
* ``bundle.tb4``        -> ``site/data/benchmarks/terminal-bench-4.json``
* ``bundle.changelog``  -> ``site/data/changelog.json``
* ``bundle.livebench``  -> ``site/data/livebench.json``

Page view-model helpers take the bundle and return the ``page`` mapping for one template:
``index_page``, ``rankings_page``, ``model_page(bundle, slug)``, ``plans_page``, ``benchmarks_page``,
``tb4_page``, ``methodology_page``, ``changelog_page``, ``data_page`` and ``models_page`` (the ``/models/`` index).

Scoring rules
-------------
* ``slug`` is the model id with dots replaced by hyphens (``gpt-6.1-sol`` -> ``gpt-6-1-sol``).
* Cost arithmetic is delegated to ``valuerank.plan_costs``. Both bases compare cost per AA Intelligence
  Index point; cost *scores* are log-scaled within the ranked cohort (as ``emit_docs`` does), and cost
  *numbers* (USD) are computed for every roster model.
* The overall score on a basis gives that basis' cost score a fixed ``COST_WEIGHT_PCT`` share and the
  priority-weighted quality score (renormalised over the available quality dimensions) the rest: the rule
  of ``build_scores`` and the site JavaScript. Models rank by score descending, then lower cost on that basis, then name. The API-basis
  result reproduces ``data/scores.json``.
* Historic ranks predate the plan basis; see ``valuerank.site.changelog``.
"""

from __future__ import annotations

import datetime as dt
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from valuerank.emit_docs import AA_METHODOLOGY_URL, BENCHMARK_URLS, model_inclusion, plan_evidence_label
from valuerank.paths import DATA
from valuerank.plan_costs import (
    COST_WEIGHT_PCT,
    blend,
    build_cost_fields,
    cost_per_index_point,
    effective_cost,
    load_plan_routes,
    route_summary,
)
from valuerank.release import DATE, VERSION
from valuerank.site import evidence
from valuerank.site.changelog import build_changelog, model_history
from valuerank.site.picks import build_picks

BASES = {
    "api": {
        "label": "API ranking",
        "costLabel": "API cost",
        "costUnit": "USD per Index point",
        "description": "AA total evaluation cost at API rates ÷ AA Intelligence Index.",
        "pickLabel": "Best at API rates",
        "pickPhrase": "at API rates",
    },
    "plan": {
        "label": "Plan ranking",
        "costLabel": "Plan cost",
        "costUnit": "USD per Index point",
        "description": "AA total evaluation cost ÷ highest eligible Value Multiple ÷ AA Intelligence Index.",
        "pickLabel": "Best on a subscription",
        "pickPhrase": "on a subscription",
    },
}
CATEGORIES = {
    "cost": "Cost",
    "rely": "Reliability",
    "code": "Code/Agentic",
    "prod": "Production",
    "intel": "Intelligence",
    "language": "Language",
}
COST_KEY = "costComposite"
TIERS = ((15, "Budget"), (22, "Near-Budget"), (35, "Mid-Range"), (55, "Premium"))
AA_ONLY_EXCLUDED = {"deepswePassAt1", "bugHuntFixedOf105", "livebenchInstructionFollowing", "terminalBenchV4"}


@dataclass
class Bundle:
    """Every public document, computed once from one ``data`` directory."""

    data: Path
    rankings: dict
    models: dict[str, dict]
    plans: dict
    benchmarks: dict
    tb4: dict
    changelog: dict
    livebench: dict
    extras: dict = field(default_factory=dict)


# --- scoring ---------------------------------------------------------------------------------


def slugify(model_id: str) -> str:
    return model_id.replace(".", "-")


def composite_score(dims: dict, cost_score: float | None, weights: list[dict]) -> float | None:
    """Cost's fixed share of ``cost_score`` plus the rest of the available quality mean (``plan_costs.blend``)."""

    total = priority = 0.0
    for weight in weights:
        value = dims.get(weight["key"]) if weight["key"] != COST_KEY else None
        if value is not None:
            total += value * weight["priority"]
            priority += weight["priority"]
    return blend(cost_score, total / priority if priority else None)


def coverage_pct(has_cost: bool, available_priority: float, total_priority: float) -> float:
    """Share of the scoring weight with an eligible value: cost's fixed share plus the quality share."""

    quality = (100.0 - COST_WEIGHT_PCT) * available_priority / total_priority if total_priority else 0.0
    return round((COST_WEIGHT_PCT if has_cost else 0.0) + quality, 2)


def rank_scores(scores: dict, names: dict, costs: dict | None = None) -> dict:
    """1-based ranks by score descending, then lower cost (unknown last), then name; entries without a score are skipped."""

    costs = costs or {}
    scored = [key for key, score in scores.items() if score is not None]
    ordered = sorted(
        scored,
        key=lambda key: (-scores[key], costs[key] if costs.get(key) is not None else float("inf"), names[key]),
    )
    return {key: position for position, key in enumerate(ordered, 1)}


def _tier(cost_score: float | None) -> str | None:
    if cost_score is None:
        return None
    penalty = 100 - cost_score
    return next((name for limit, name in TIERS if penalty <= limit), "Expensive")


def _pareto(entries: dict[str, tuple[float | None, float | None]]) -> dict[str, bool]:
    """Non-dominated models on (cost score, quality score), both higher-is-better."""

    scored = {key: pair for key, pair in entries.items() if pair[0] is not None and pair[1] is not None}
    return {
        key: not any(
            other != key
            and scored[other][0] >= cost
            and scored[other][1] >= quality
            and (scored[other][0] > cost or scored[other][1] > quality)
            for other in scored
        )
        for key, (cost, quality) in scored.items()
    }


# --- loading ---------------------------------------------------------------------------------


def _load(data: Path) -> dict[str, Any]:
    def read(name: str):
        return json.loads((data / name).read_text())

    return {
        "scores": read("scores.json"),
        "aa": read("aa_metrics.json"),
        "history": read("ranking_history_v1.5.json"),
        "report": read("aa_reconciliation_report.json"),
        "coverage": read("coverage_matrix.json"),
        "tb4": read("tb4.json"),
        "livebench": read("livebench.json"),
        "claims": read("provider_claims.json"),
        "deepswe": read("aa_deepswe.json"),
        "bugHunt": read("bug_hunt.json"),
        "routes": load_plan_routes(data / "plan_cost_routes.json"),
    }


def _route_view(route: dict | None) -> dict | None:
    if route is None:
        return None
    return {
        "id": route["id"],
        "planLabel": route.get("planLabel"),
        "planFeeUsd": route.get("planPriceUsd"),
        "valueMultiple": route["valueMultiple"],
        "grade": evidence.route_grade(route.get("evidenceClass")),
        "evidenceLabel": plan_evidence_label(route),
        "sourceModel": route.get("sourceModel"),
        "sourceUrl": route.get("sourceUrl"),
        "sourceDate": route.get("sourcePublicationDate"),
    }


def _cost_view(fields: dict) -> dict:
    return {
        "apiUsd": fields["apiCost"],
        "apiUsdPerPoint": fields["apiCostPerPoint"],
        "planUsdPerRun": fields["planCostPerRun"],
        "planUsdPerPoint": fields["planCost"],
        "planComparableUsdPerPoint": fields["planComparableCost"],
        "fallback": fields["planCostFallback"],
        "route": _route_view(fields["planRoute"]),
    }


def _dimension_docs(source: dict, slug: str, weights: list[dict], normalized: dict, cost_dims: dict, inputs: dict) -> list[dict]:
    """Every retained dimension in weight order for one model, including missing ones."""

    context = {
        "scores": inputs["scores"],
        "aaSources": inputs["aa"]["models"].get(source["id"], {}).get("metricSources", {}),
        "livebench": inputs["livebench"],
        "tb4": inputs["tb4"],
    }
    docs = []
    for weight in sorted(weights, key=lambda item: -item["weightPct"]):
        key = weight["key"]
        meta = evidence.DIMENSION_META[key]
        value = evidence.raw_value(key, source)
        proof = (
            evidence.dimension_evidence(key, source, context)
            if value is not None
            else {"source": None, "observedAt": None, "evaluatedVariant": None, "note": None, "grade": "missing"}
        )
        doc = {
            "key": key,
            "label": weight["label"],
            "category": meta["category"],
            "weightPct": weight["weightPct"],
            "value": value,
            "unit": meta["unit"],
            "normalized": cost_dims["api"] if key == COST_KEY else normalized.get(key),
            **proof,
        }
        if key == COST_KEY:
            doc["normalizedByBasis"] = dict(cost_dims)
        docs.append(doc)
    return docs


# --- bundle ----------------------------------------------------------------------------------


FRONTIER_TIER_KEYS = ("aaFrontierTier", "aaFrontierConfiguration", "aaFrontierIntelligenceGap", "aaFrontierFootnote")


def build_bundle(data: Path = DATA) -> Bundle:
    inputs = _load(data)
    scores = inputs["scores"]
    weights = scores["weights"]
    roster = scores["models"]
    slugs = [slugify(source["id"]) for source in roster]
    if len(set(slugs)) != len(slugs):
        raise ValueError("duplicate model slug in data/scores.json")
    ranked = [source for source in roster if source.get("rankingEligible") is True]
    if not ranked:
        raise ValueError("no ranked models in data/scores.json")

    all_fields = dict(zip((s["id"] for s in roster), build_cost_fields(roster, inputs["routes"])))
    cohort_fields = dict(zip((s["id"] for s in ranked), build_cost_fields(ranked, inputs["routes"])))
    names = {source["id"]: source["name"] for source in roster}
    non_cost = [w["key"] for w in weights if w["key"] != COST_KEY]

    overall: dict[str, dict] = {"api": {}, "plan": {}}
    for basis, score_key in (("api", "apiCostScore"), ("plan", "planCostScore")):
        overall[basis] = {
            source["id"]: composite_score(source["dims"], cohort_fields[source["id"]][score_key], weights) for source in ranked
        }
    tie_costs = {
        basis: {source["id"]: cohort_fields[source["id"]][cost_key] for source in ranked}
        for basis, cost_key in (("api", "apiCostPerPoint"), ("plan", "planComparableCost"))
    }
    ranks = {basis: rank_scores(overall[basis], names, tie_costs[basis]) for basis in overall}
    pareto = {
        basis: _pareto(
            {
                source["id"]: (cohort_fields[source["id"]][score_key], source.get("qualityScore"))
                for source in ranked
            }
        )
        for basis, score_key in (("api", "apiCostScore"), ("plan", "planCostScore"))
    }

    entries, docs = {}, {}
    total_priority = sum(w["priority"] for w in weights if w["key"] != COST_KEY)
    for source in roster:
        model_id, slug = source["id"], slugify(source["id"])
        is_ranked = source in ranked
        cohort = cohort_fields.get(model_id, {})
        cost_dims = {"api": cohort.get("apiCostScore"), "plan": cohort.get("planCostScore")}
        normalized = source["dims"] if is_ranked else {}
        dimension_docs = _dimension_docs(source, slug, weights, normalized, cost_dims, inputs)
        present = [doc for doc in dimension_docs if doc["value"] is not None]
        present_keys = {d["key"] for d in present}
        available = sum(w["priority"] for w in weights if w["key"] != COST_KEY and w["key"] in present_keys)
        coverage = {
            "pct": coverage_pct(COST_KEY in present_keys, available, total_priority),
            "costAvailable": COST_KEY in present_keys,
            "availablePriority": available,
            "totalPriority": total_priority,
            "missing": [w["label"] for w in weights if not any(d["key"] == w["key"] for d in present)],
        }
        entries[slug] = {
            "slug": slug,
            "name": source["name"],
            "shortName": source["shortName"],
            "developer": source["developer"],
            "aaUrl": source["aaUrl"],
            "aaVariant": source.get("aaVariant"),
            "rankingEligible": is_ranked,
            "exclusionReasons": list(source.get("rankingExclusionReasons") or []),
            "rank": {basis: ranks[basis].get(model_id) for basis in BASES},
            "overall": {basis: overall[basis].get(model_id) for basis in BASES},
            "quality": source.get("qualityScore"),
            "qualityRank": source.get("qualityRank"),
            "dims": {key: (normalized.get(key) if is_ranked else None) for key in [COST_KEY, *non_cost]} | {COST_KEY: None},
            "costDims": cost_dims,
            "raw": {key: evidence.raw_value(key, source) for key in non_cost},
            "coverage": coverage,
            "cost": _cost_view(all_fields[model_id]),
            "intelligenceIndex": {"value": source.get("intelligenceIndex"), "status": source.get("intelligenceIndexStatus")},
            "speed": source.get("speed"),
            "grade": evidence.worst_grade(doc["grade"] for doc in dimension_docs),
            "pareto": {basis: pareto[basis].get(model_id, False) for basis in BASES},
            "tier": _tier(cost_dims["plan"]),
            **{key: source.get(key) for key in FRONTIER_TIER_KEYS},
        }
        docs[slug] = dimension_docs

    ordered = sorted(
        entries.values(),
        key=lambda entry: (entry["rank"]["plan"] is None, entry["rank"]["plan"] or 0, entry["name"]),
    )
    cost_weight = next(w["weightPct"] for w in weights if w["key"] == COST_KEY)
    rankings = {
        "version": VERSION,
        "publishDate": DATE,
        "observedAt": scores["observedAt"],
        "bases": BASES,
        "defaultBasis": "plan",
        "costWeightPct": cost_weight,
        "modelInclusion": model_inclusion(scores.get("frontierSelection"), roster),
        "dimensions": [
            {
                "key": w["key"],
                "label": w["label"],
                "fullLabel": "Cost (selected basis)" if w["key"] == COST_KEY else w["label"],
                "category": evidence.DIMENSION_META[w["key"]]["category"],
                "weightPct": w["weightPct"],
                "priority": w["priority"],
                "higherBetter": w["higherBetter"],
                "sourceUrl": evidence.dimension_url(w["key"]),
            }
            for w in weights
        ],
        "categories": CATEGORIES,
        "models": ordered,
        "picks": {basis: build_picks(ordered, basis, BASES) for basis in BASES},
        "planMeta": {
            **{k: v for k, v in route_summary(inputs["routes"], list(cohort_fields.values())).items() if k != "mixId"},
            "totalModelCount": len(ranked),
        },
    }

    current = {
        "version": VERSION,
        "dateIso": dt.datetime.strptime(DATE, "%B %d, %Y").date().isoformat(),
        "dateHuman": DATE,
        "modelCount": len(ranked),
        "dimensionCount": len(weights),
        "ranks": {
            source["id"]: {basis: ranks[basis][source["id"]] for basis in BASES} for source in ranked
        },
    }
    bundle = Bundle(
        data=data,
        rankings=rankings,
        models={},
        plans=_plans(inputs, entries, slugs),
        benchmarks=_benchmarks(inputs, rankings),
        tb4=_tb4(inputs, roster),
        changelog=build_changelog(inputs["history"], current, names),
        livebench=_livebench(inputs),
    )
    bundle.models = {
        slugify(source["id"]): _model_doc(source, entries[slugify(source["id"])], docs[slugify(source["id"])], inputs, current)
        for source in roster
    }
    return bundle


# --- per-model documents --------------------------------------------------------------------


def _model_doc(source: dict, entry: dict, dimension_docs: list[dict], inputs: dict, current: dict) -> dict:
    model_id = source["id"]
    index = source.get("intelligenceIndex")
    selected = entry["cost"]["route"]["id"] if entry["cost"]["route"] else None
    plans = []
    for route in inputs["routes"]["routes"]:
        if model_id not in route["modelIds"] or route.get("requiredVariant") not in (None, source.get("aaVariant")):
            continue
        per_run = effective_cost(entry["cost"]["apiUsd"], route)
        plans.append(
            {
                **{k: v for k, v in _route_view(route).items() if k != "sourceModel"},
                "usdPerRun": per_run,
                "usdPerPoint": cost_per_index_point(per_run, index),
                "selected": route["id"] == selected,
            }
        )
    plans.sort(key=lambda plan: (plan["usdPerPoint"] is None, plan["usdPerPoint"] or 0, plan["id"]))
    rows = [row for row in inputs["report"]["frontier"] if row.get("valueRankModelId") == model_id]
    on_frontier = bool(rows)
    return {
        "slug": entry["slug"],
        "name": entry["name"],
        "developer": entry["developer"],
        "aaUrl": entry["aaUrl"],
        "aaVariant": entry["aaVariant"],
        "selectedPage": entry["aaUrl"],
        "summary": {
            "rank": entry["rank"],
            "overall": entry["overall"],
            "quality": entry["quality"],
            "qualityRank": entry["qualityRank"],
            "coverage": entry["coverage"],
            "grade": entry["grade"],
            "rankingEligible": entry["rankingEligible"],
            "exclusionReasons": entry["exclusionReasons"],
        },
        "dimensions": dimension_docs,
        "cost": entry["cost"],
        "plans": plans,
        "history": model_history(inputs["history"], current, model_id),
        "frontier": {
            "onAaFrontier": on_frontier,
            "aaFrontierNote": (
                f"On the observed Artificial Analysis Intelligence Index versus total cost frontier as {rows[0]['name']}."
                if on_frontier
                else "Not on the observed Artificial Analysis Intelligence Index versus total cost frontier."
            ),
            "tier": entry["aaFrontierTier"],
            "configuration": entry["aaFrontierConfiguration"],
            "intelligenceGap": entry["aaFrontierIntelligenceGap"],
            "footnote": entry["aaFrontierFootnote"],
        },
    }


# --- plans, benchmarks, TB4 -------------------------------------------------------------------


def _plans(inputs: dict, entries: dict, slugs: list[str]) -> dict:
    routes = inputs["routes"]
    return {
        "asOf": routes.get("asOf"),
        "policy": routes["evidencePolicy"],
        "routes": [
            {
                "id": route["id"],
                "provider": route.get("provider"),
                "planLabel": route.get("planLabel"),
                "planFeeUsd": route.get("planPriceUsd"),
                "valueMultiple": route["valueMultiple"],
                "apiEquivalentUsd": route.get("apiEquivalentUsd"),
                "grade": evidence.route_grade(route.get("evidenceClass")),
                "evidenceLabel": plan_evidence_label(route),
                "sourceModel": route.get("sourceModel"),
                "sourceUrl": route.get("sourceUrl"),
                "sourceDate": route.get("sourcePublicationDate"),
                "modelSlugs": [slugify(model_id) for model_id in route["modelIds"]],
                "notes": route.get("notes"),
            }
            for route in routes["routes"]
        ],
        "candidates": [
            {
                "slug": slug,
                "name": entry["name"],
                "rank": entry["rank"],
                "intelligenceIndex": entry["intelligenceIndex"],
                "apiUsd": entry["cost"]["apiUsd"],
                "planUsdPerRun": entry["cost"]["planUsdPerRun"],
                "planUsdPerPoint": entry["cost"]["planUsdPerPoint"],
                "fallback": entry["cost"]["fallback"],
                "routeId": entry["cost"]["route"]["id"] if entry["cost"]["route"] else None,
            }
            for slug, entry in sorted(entries.items())
        ],
        "workedExample": {"slugs": ["claude-opus-5-5", "gpt-6-1-sol"]},
    }


def _benchmarks(inputs: dict, rankings: dict) -> dict:
    scores, deepswe, bug_hunt = inputs["scores"], inputs["deepswe"], inputs["bugHunt"]
    livebench, tb4, claims = inputs["livebench"], inputs["tb4"], inputs["claims"]["claims"]
    dimension = {d["key"]: d for d in rankings["dimensions"]}
    ranked = [m for m in rankings["models"] if m["rankingEligible"]]

    def coverage(key: str) -> dict:
        return {"available": sum(1 for m in ranked if m["raw"].get(key) is not None), "cohort": len(ranked)}

    aa_keys = [key for key in dimension if key not in AA_ONLY_EXCLUDED]
    sources = [
        {
            "id": "aa-intelligence-index",
            "name": "Artificial Analysis Intelligence Index",
            "owner": "Artificial Analysis",
            "version": scores["benchmarkVersion"],
            "url": BENCHMARK_URLS["AA Intelligence Index"],
            "observedAt": scores["observedAt"][:10],
            "role": "primary dimensions",
            "weightPct": round(sum(dimension[key]["weightPct"] for key in aa_keys), 4),
            "coverage": coverage("intelligenceIndex"),
            "unit": "Index points and component scores",
            "notes": f"Cost, speed, Intelligence Index and its components for the selected variants. {inputs['aa']['providerClaimPolicy']}",
        },
        {
            "id": "deepswe",
            "name": scores["deepsweBenchmarkVersion"],
            "owner": deepswe["source"]["publisher"],
            "version": f"Coding Agent Index {deepswe['source']['indexVersion']}",
            "url": deepswe["source"]["url"],
            "observedAt": deepswe["observedAt"],
            "role": "primary dimension",
            "weightPct": dimension["deepswePassAt1"]["weightPct"],
            "coverage": coverage("deepswePassAt1"),
            "unit": "% pass@1",
            "notes": deepswe["source"]["methodology"],
        },
        {
            "id": "bug-hunt",
            "name": "Bug Hunt Bench",
            "owner": "Bug Hunt Bench benchmark owner",
            "version": bug_hunt["benchmarkVersion"],
            "url": bug_hunt["sources"]["homepage"],
            "observedAt": bug_hunt["snapshotDate"],
            "role": "primary dimension",
            "weightPct": dimension["bugHuntFixedOf105"]["weightPct"],
            "coverage": coverage("bugHuntFixedOf105"),
            "unit": bug_hunt["scoreUnit"],
            "notes": bug_hunt["matchingPolicy"],
        },
        {
            "id": "livebench",
            "name": "LiveBench",
            "owner": livebench["source"]["publisher"],
            "version": f"release {livebench['release']}",
            "url": livebench["source"]["homepage"],
            "observedAt": livebench["observedAt"][:10],
            "role": "primary dimension",
            "weightPct": dimension["livebenchInstructionFollowing"]["weightPct"],
            "coverage": coverage("livebenchInstructionFollowing"),
            "unit": "Instruction Following score",
            "notes": f"Release data pinned to commit {livebench['source']['releaseDataCommit']}.",
        },
        {
            "id": "terminal-bench-4",
            "name": "Terminal-Bench 4.0",
            "owner": tb4["source"]["publisher"],
            "version": tb4["version"],
            "url": tb4["source"]["targetUrl"],
            "observedAt": tb4["observedAt"][:10],
            "role": "primary dimension",
            "weightPct": dimension["terminalBenchV4"]["weightPct"],
            "coverage": coverage("terminalBenchV4"),
            "unit": "% resolved",
            "notes": tb4["providerClaimPolicy"],
        },
        {
            "id": "provider-claims",
            "name": "Provider claims",
            "owner": "Model providers",
            "version": inputs["claims"]["schemaVersion"],
            "url": None,
            "observedAt": max(claim["publishedOn"] for claim in claims),
            "role": "fallback evidence",
            "weightPct": None,
            "coverage": {"available": sum(1 for c in claims if c["eligibleForRanking"] is True), "cohort": len(claims)},
            "unit": "claimed value",
            "notes": inputs["claims"]["policy"],
        },
    ]
    report = inputs["report"]
    return {
        "sources": sources,
        "aaComponents": [
            {"name": item["label"], "weightPct": item["weightPct"], "url": BENCHMARK_URLS.get(item["label"], AA_METHODOLOGY_URL)}
            for item in inputs["aa"]["primaryEvaluations"]
        ],
        "coverageMatrix": {
            "cohort": inputs["coverage"]["cohort"],
            "cohortN": inputs["coverage"]["cohortN"],
            "observedAt": inputs["coverage"]["observedAt"],
            "note": inputs["coverage"]["note"],
            "fields": inputs["coverage"]["fields"],
        },
        "frontier": {
            "status": report["completeness"]["status"],
            "checkedAt": report["checkedAt"],
            "observedAt": report["observedAt"],
            "sourceUrl": report["sourceUrl"],
            "benchmarkVersion": report["benchmarkVersion"],
            "definition": report["frontierDefinition"],
            "note": report["completeness"]["note"],
            "rows": [
                {
                    "aaId": row["aaId"],
                    "name": row["name"],
                    "evaluatedVariant": row["evaluatedVariant"],
                    "intelligenceIndex": row["intelligenceIndex"],
                    "totalCostUsd": row["totalCostUsd"],
                    "family": row["family"],
                    "slug": slugify(row["valueRankModelId"]) if row["valueRankModelId"] else None,
                    "sourceUrl": row["sourceUrl"],
                }
                for row in report["frontier"]
            ],
        },
    }


def _livebench(inputs: dict) -> dict:
    """Matched LiveBench rows (roster and supplemental) for the cost-versus-score chart, cheapest first."""

    document = inputs["livebench"]
    frontier = set(document.get("pareto", []))
    sources = {**document["models"], **document.get("supplementalModels", {})}
    rows = [
        {
            "id": slugify(model_id),
            "name": item["name"],
            "livebenchModel": item.get("livebenchModel"),
            "overallScore": item["overallScore"],
            "instructionFollowingScore": item.get("instructionFollowingScore"),
            "costPerSuccessfulTaskUsd": item.get("costPerSuccessfulTaskUsd"),
            "pareto": model_id in frontier,
        }
        for model_id, item in sources.items()
        if item.get("overallScore") is not None
    ]
    rows.sort(key=lambda row: (row["costPerSuccessfulTaskUsd"] is None, row["costPerSuccessfulTaskUsd"] or 0, row["id"]))
    return {"release": document["release"], "observedAt": document["observedAt"], "rows": rows}


def _tb4(inputs: dict, roster: list[dict]) -> dict:
    document = inputs["tb4"]
    claims = {claim["cohortModelId"]: claim for claim in document["providerClaims"]}
    best, frontier = -float("inf"), 0
    for row in sorted(document["rows"], key=lambda item: (item["costUsd"] is None, item["costUsd"] or 0, -item["resolutionRate"])):
        if row["costUsd"] is not None and row["resolutionRate"] > best:
            best, frontier = row["resolutionRate"], frontier + 1
    mapping = {}
    for source in roster:
        model_id = source["id"]
        official, claim = document["cohortRows"].get(model_id), claims.get(model_id)
        if official:
            entry = {"status": "official", "rank": official["rank"], "resolutionRatePct": official["resolutionRatePct"], "evaluatedModel": official["model"]}
        elif claim:
            entry = {"status": "provider_claim", "rank": None, "resolutionRatePct": claim["valuePct"], "evaluatedModel": claim["evaluatedModel"]}
        else:
            entry = {"status": "missing", "rank": None, "resolutionRatePct": None, "evaluatedModel": None}
        mapping[slugify(model_id)] = entry
    return {**document, "frontierCount": frontier, "cohortMapping": mapping}


# --- page view models ------------------------------------------------------------------------


def _cost_label(entry: dict, basis: str) -> str:
    cost = entry["cost"]
    if basis == "api":
        return f"${cost['apiUsd']:,.2f} per Index run"
    return f"${cost['planComparableUsdPerPoint']:,.2f} per Index point"


def index_page(bundle: Bundle) -> dict:
    rankings = bundle.rankings
    ranked = [m for m in rankings["models"] if m["rankingEligible"]]
    by_slug = {m["slug"]: m for m in rankings["models"]}
    quality = min(ranked, key=lambda m: m["qualityRank"])
    headline = {}
    for basis, picks in rankings["picks"].items():
        value = by_slug[picks["value"]["slug"]]
        lead = f"{value['name']} leads the {rankings['bases'][basis]['label']} at {value['overall'][basis]:.1f}"
        headline[basis] = (
            f"{lead} and also leads on quality."
            if value is quality
            else f"{lead}; {quality['name']} leads on quality."
        )
    return {
        "headline": headline,
        "picks": rankings["picks"],
        "models": [
            {
                "slug": m["slug"],
                "name": m["name"],
                "developer": m["developer"],
                "rank": m["rank"],
                "overall": m["overall"],
                "quality": m["quality"],
                "qualityRank": m["qualityRank"],
                "grade": m["grade"],
                "costDims": m["costDims"],
                "cost": m["cost"],
                "coveragePct": m["coverage"]["pct"],
                "coverage": m["coverage"],
                "tier": m["tier"],
            }
            for m in ranked
        ],
        "dimensions": rankings["dimensions"],
        "chart": {
            basis: [
                {
                    "slug": m["slug"],
                    "name": m["name"],
                    "x": m["cost"]["apiUsd"] if basis == "api" else m["cost"]["planComparableUsdPerPoint"],
                    "y": m["quality"],
                    "pareto": m["pareto"][basis],
                    "costLabel": _cost_label(m, basis),
                }
                for m in ranked
            ]
            for basis in rankings["bases"]
        },
        "rankingsJson": rankings,
    }


COLUMN_ORDER = (
    ("rank", "Rank"), ("name", "Model"), ("overall", "Overall"), ("quality", "Quality"), ("cost", "Cost"),
    ("grade", "Evidence"), ("coverage", "Coverage"), ("developer", "Developer"), ("qualityRank", "Quality rank"),
    ("speed", "Speed"), ("ii", "Intelligence Index"),
)
DEFAULT_COLUMNS = tuple(key for key, _label in COLUMN_ORDER[:7])


def rankings_page(bundle: Bundle) -> dict:
    """Column keys match ``assets/js/filters.js`` (``name`` is the model column)."""

    rankings = bundle.rankings
    columns = [{"key": key, "label": label} for key, label in COLUMN_ORDER]
    columns += [{"key": d["key"], "label": d["label"]} for d in rankings["dimensions"] if d["key"] != COST_KEY]
    return {
        "rankingsJson": rankings,
        "nearFrontierGap": rankings["modelInclusion"]["nearFrontierGap"],
        "providers": sorted({m["developer"] for m in rankings["models"]}),
        "grades": list(evidence.GRADES),
        "columns": [{**column, "sortable": True, "default": column["key"] in DEFAULT_COLUMNS} for column in columns],
    }


def models_page(bundle: Bundle) -> dict:
    """The ``/models/`` index: every roster model, ranked first, with both ranks and the evidence grade."""

    models = [
        {
            "slug": m["slug"], "name": m["name"], "developer": m["developer"], "rank": m["rank"], "overall": m["overall"],
            "grade": m["grade"], "rankingEligible": m["rankingEligible"], "coveragePct": m["coverage"]["pct"],
        }
        for m in bundle.rankings["models"]
    ]
    ranked = sum(1 for m in models if m["rankingEligible"])
    return {"models": models, "rankedCount": ranked, "unrankedCount": len(models) - ranked}


def model_page(bundle: Bundle, slug: str) -> dict:
    document = bundle.models[slug]
    related = [
        {"slug": m["slug"], "name": m["name"], "developer": m["developer"], "rank": m["rank"], "overall": m["overall"]}
        for m in bundle.rankings["models"]
        if m["developer"] == document["developer"] and m["slug"] != slug
    ]
    return {**document, "related": related}


def plans_page(bundle: Bundle) -> dict:
    by_slug = {m["slug"]: m for m in bundle.rankings["models"]}
    example = []
    for slug in bundle.plans["workedExample"]["slugs"]:
        entry = by_slug[slug]
        route = entry["cost"]["route"]
        if route is None:
            raise ValueError(f"worked example model {slug} has no plan route")
        example.append(
            {
                "slug": slug,
                "name": entry["name"],
                "routeLabel": route["planLabel"],
                "planFeeUsd": route["planFeeUsd"],
                "valueMultiple": route["valueMultiple"],
                "grade": route["grade"],
                "evidenceLabel": route["evidenceLabel"],
                "indexValue": entry["intelligenceIndex"]["value"],
                "apiUsd": entry["cost"]["apiUsd"],
                "planUsdPerRun": entry["cost"]["planUsdPerRun"],
                "planUsdPerPoint": entry["cost"]["planUsdPerPoint"],
            }
        )
    providers: dict[str, list] = {}
    for route in sorted(bundle.plans["routes"], key=lambda item: item["id"]):
        providers.setdefault(route["provider"], []).append(route)
    return {"plansJson": bundle.plans, "workedExample": {"models": example}, "routesByProvider": dict(sorted(providers.items()))}


def benchmarks_page(bundle: Bundle) -> dict:
    return {"benchmarksJson": bundle.benchmarks}


def tb4_page(bundle: Bundle) -> dict:
    return {"tb4Json": bundle.tb4}


def changelog_page(bundle: Bundle) -> dict:
    return {"changelogJson": bundle.changelog}


FAQ_TEMPLATE = (
    ("How is the overall score calculated?", "Cost carries a fixed {cost:.0f}% of the score and quality the rest. The cost score compares USD per Intelligence Index point on a log scale, so the cheapest model scores 100, the dearest 0, and equal cost ratios count equally. Each quality dimension is rank-normalised to 0-100 across the ranked cohort, multiplied by its weight and divided by the quality weights that are available for that model."),
    ("What happens when a benchmark has no result for a model?", "The dimension is dropped for that model and the remaining quality weights are renormalised; cost keeps its fixed share. Nothing is filled in, and the gap is shown on the model page."),
    ("What is the difference between the API ranking and the Plan ranking?", "Both rank on token efficiency: what it costs to run the Artificial Analysis Intelligence Index, per Index point. The API ranking prices the run at API rates. The Plan ranking also divides by the best eligible subscription Value Multiple, the API-priced usage a plan delivers per dollar of fee."),
    ("What do the evidence grades mean?", "Measured values come from the benchmark owner or a controlled account measurement. Claims come from the model provider, estimates are owner estimates or user-reported projections, and assumptions are explicitly authorised stand-ins."),
    ("Why is a model not ranked?", "Ranked models need an exact-variant DeepSWE and Bug Hunt result or a required place on the Artificial Analysis frontier. Unranked models still have pages with every value we hold."),
)

LIMITATIONS = (
    "Rank and cost scores are relative to the ranked cohort and change when the cohort changes.",
    "Public benchmark displays are rounded, so small differences between models are not meaningful.",
    "Subscription value multiples are projections or assumptions, not guarantees of what a plan delivers.",
    "Results are never transferred between model versions or reasoning efforts; missing coverage lowers confidence.",
    "Cost per Index point assumes the Artificial Analysis token mix, not your own workload.",
)


def methodology_page(bundle: Bundle) -> dict:
    rankings = bundle.rankings
    ranked = sorted((m for m in rankings["models"] if m["rank"]["plan"] is not None), key=lambda m: m["rank"]["plan"])
    chosen = next((m for m in ranked if m["coverage"]["pct"] < 100), ranked[0])
    dimensions = rankings["dimensions"]
    normalized = {d["key"]: (chosen["costDims"]["plan"] if d["key"] == COST_KEY else chosen["dims"][d["key"]]) for d in dimensions}
    available = sum(d["weightPct"] for d in dimensions if normalized[d["key"]] is not None)
    quality_available = sum(d["weightPct"] for d in dimensions if d["key"] != COST_KEY and normalized[d["key"]] is not None)
    available_priority = sum(d["priority"] for d in dimensions if d["key"] != COST_KEY and normalized[d["key"]] is not None)
    cost_share = rankings["costWeightPct"] if normalized.get(COST_KEY) is not None else 0.0
    rows = []
    for d in dimensions:
        value = normalized[d["key"]]
        included = value is not None
        if not included:
            effective = 0.0
        elif d["key"] == COST_KEY:
            effective = cost_share
        else:
            effective = round((100 - cost_share) * d["weightPct"] / quality_available, 4)
        rows.append(
            {
                "key": d["key"],
                "label": d["label"],
                "weightPct": d["weightPct"],
                "normalized": value,
                "included": included,
                "effectiveWeightPct": effective,
                "contribution": round((value or 0.0) * effective / 100, 3),
            }
        )
    return {
        "dimensions": dimensions,
        "costWeightPct": rankings["costWeightPct"],
        "modelInclusion": rankings["modelInclusion"],
        "weights": {d["key"]: d["weightPct"] for d in dimensions},
        "workedExample": {
            "slug": chosen["slug"],
            "name": chosen["name"],
            "basis": "plan",
            "overall": chosen["overall"]["plan"],
            "availableWeightPct": round(available, 4),
            "availablePriority": available_priority,
            "totalPriority": sum(d["priority"] for d in dimensions if d["key"] != COST_KEY),
            "steps": rows,
            "missing": [row["label"] for row in rows if not row["included"]],
        },
        "faq": [{"q": q, "a": a.format(cost=rankings["costWeightPct"])} for q, a in FAQ_TEMPLATE],
        "limitations": list(LIMITATIONS),
    }


def data_page(bundle: Bundle) -> dict:
    def schema(document: dict) -> str:
        return "{" + ", ".join(document) + "}"

    sample = next(iter(bundle.models.values()))
    files = [
        ("/data/rankings.json", "Every roster model with scores, ranks, cost and evidence on both bases.", schema(bundle.rankings)),
        ("/data/models/<slug>.json", "One document per roster model with every dimension, source, plan route and history.", schema(sample)),
        ("/data/plans.json", "Subscription routes, their evidence and the full candidate cost comparison.", schema(bundle.plans)),
        ("/data/benchmarks.json", "Benchmark source registry, coverage matrix and the Artificial Analysis frontier.", schema(bundle.benchmarks)),
        ("/data/benchmarks/terminal-bench-4.json", "Terminal-Bench 4.0 official rows, provider claims and cohort mapping.", schema(bundle.tb4)),
        ("/data/changelog.json", "Versions, newest first, with recorded ranks and rank changes between consecutive releases.", schema(bundle.changelog)),
        ("/data/livebench.json", "Matched LiveBench rows with overall score, instruction following and cost per successful task.", schema(bundle.livebench)),
    ]
    return {"files": [{"path": path, "description": description, "schema": shape} for path, description, shape in files]}
