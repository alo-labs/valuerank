"""Server-side view models for the multi-page site (docs/site-data-contract.md), methodology v3.

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

Scoring rules (methodology v3; every number comes from the ``v3`` section of ``data/scores.json``)
--------------------------------------------------------------------------------------------------
* ``slug`` is the model id with dots replaced by hyphens (``gpt-6.1-sol`` -> ``gpt-6-1-sol``).
* Value on a basis = ``COST_WEIGHT_PCT``% of the cost score + the rest of the quality score. The cost
  score is log-scaled against frozen anchors; cost is the SDLC basket (AA's published cost to run seven
  Intelligence Index SDLC evaluations and the Coding Agent Index once, USD per basket run), divided on
  the Plan basis by a subscription route's Value Multiple (one row per configuration and plan). Quality is the weighted mean of
  the ranking's benchmark leaves on fixed 0-100 anchors over the leaves observed for the exact configuration; two rankings
  (``quality.TRACKS``, O53) each rank the configurations with their complete leaf set.
* A configuration without a cost score has no value score; ranks are competition ranks (ties share the
  better rank). The site's JavaScript recomputes the same rule when the cost weight moves.
* Historic ranks predate the plan basis; see ``valuerank.site.changelog``.
"""

from __future__ import annotations

import datetime as dt
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from valuerank import basket
from valuerank import plan_routes
from valuerank import quality as q
from valuerank import value_v3
from valuerank.paths import DATA
from valuerank.plan_costs import COST_WEIGHT_PCT
from valuerank.publication import AA_METHODOLOGY_URL, BENCHMARK_URLS, model_inclusion, plan_evidence_label
from valuerank.release import DATE, VERSION
from valuerank.site import evidence
from valuerank.site.changelog import build_changelog, model_history
from valuerank.site.picks import build_picks

BASES = {
    "api": {
        "label": "API ranking",
        "costLabel": "API cost",
        "costUnit": "USD per basket run",
        "description": "AA's published cost to run the SDLC basket once at API rates: seven Intelligence Index SDLC evaluations and the Coding Agent Index.",
        "pickLabel": "Best at API rates",
        "pickPhrase": "at API rates",
    },
    "plan": {
        "label": "Plan ranking",
        "costLabel": "Plan cost",
        "costUnit": "USD per basket run",
        "description": "The basket's API cost divided by a subscription route's Value Multiple at full utilisation, one row per configuration and plan (O48); API cost when no route is admitted.",
        "pickLabel": "Best on a subscription",
        "pickPhrase": "on a subscription",
    },
}
# Quality groups (valuerank.quality) shown under the site's category keys, which the chart palette uses.
GROUP_CATEGORY = {"swe": "code", "professional": "prod", "reliability": "rely", "knowledge": "intel"}
CATEGORIES = {
    "cost": "Cost",
    "code": "Software engineering",
    "prod": "Professional work",
    "rely": "Reliability",
    "intel": "Knowledge and science",
}
COST_KEY = "costComposite"
TIERS = ((15, "Budget"), (22, "Near-Budget"), (35, "Mid-Range"), (55, "Premium"))
FRONTIERCODE_URL = "https://artificialanalysis.ai/evaluations/frontiercode"
LEAF_INFO = {
    "deepswe": {"unit": "% pass@1", "url": BENCHMARK_URLS["DeepSWE pass@1"]},
    "bugHunt": {"unit": "bugs fixed of 105", "url": BENCHMARK_URLS["Bug Hunt Bench"]},
    "frontierCode": {"unit": "AA score (0-1)", "url": FRONTIERCODE_URL},
    "terminalBench": {"unit": "% resolved", "url": BENCHMARK_URLS["Terminal-Bench 4.0"]},
    "gdpval": {"unit": "Elo", "url": BENCHMARK_URLS["GDPval-AA v2.1"]},
    "automationBench": {"unit": "AA score (0-1)", "url": BENCHMARK_URLS["AutomationBench-AA"]},
    "omniscience": {"unit": "AA Omniscience Index (-100 to 100)", "url": BENCHMARK_URLS["AA-Omniscience Accuracy"]},
    "lcr": {"unit": "accuracy (0-1)", "url": BENCHMARK_URLS["AA-LCR v1.1"]},
    "hle": {"unit": "accuracy (0-1)", "url": BENCHMARK_URLS["HLE"]},
    "scicode": {"unit": "score (0-1)", "url": BENCHMARK_URLS["SciCode"]},
    "critpt": {"unit": "score (0-1)", "url": BENCHMARK_URLS["CritPt"]},
    # O53-O55: the leaves the two rankings add.
    "vibeCode": {"unit": "% of test workflows passed", "url": "https://www.vals.ai/benchmarks/vibe-code"},
    "codeMigration": {"unit": "% of hidden tests passed", "url": "https://www.vals.ai/benchmarks/code-migration-v1-1"},
    "livebench2Overall": {"unit": "mean of seven category scores (0-100)", "url": "https://livebench.ai/"},
    "aiCodingDaily": {"unit": "points of 60", "url": "https://aicodingdaily.com/leaderboard"},
}
# Public source names (the engine's provenance strings are internal and stay in scores.json).
AA_SOURCE = "Artificial Analysis model page (Intelligence Index v4.3.2)"
SOURCE_NAMES = {
    "deepswe": "AA Coding Agent Index (DeepSWE v1.1)",
    "bugHunt": "Bug Hunt Bench published runs",
    "terminalBench": "Artificial Analysis Terminal-Bench 4.0 run (mini-SWE-agent)",
}
TB_GAP_SOURCE = "tbench.ai Terminal-Bench 4.0 leaderboard (gap fill, O37)"
LEAF_NOTES = {
    "gdpval": "Scored with AA's integration transform, (Elo - 500) / 2000, on the rating as integrated in the pinned Index.",
    "omniscience": "Scored as AA's Omniscience Index I (correct minus incorrect over all questions), z = (I + 100) / 2 (owner decision O28).",
    "bugHunt": "Mean bugs fixed over the owner's published runs for the exact model, effort and harness.",
    "terminalBench": "AA's own run on one harness (mini-SWE-agent) since O37; tbench.ai rows fill a gap and are compared with it as a diagnostic.",
    "vibeCode": "Vals AI's run on one harness (OpenHands) at each vendor's top effort; Vals' published standard error is the sampling noise.",
    "codeMigration": "Vals AI's run on one harness (Pi) at each vendor's top effort; Vals' published standard error is the sampling noise.",
    "livebench2Overall": "LiveBench 2.0's own run at each model's top effort (release 2026-10-14); Overall is the mean of its seven categories, as LiveBench computes it.",
    "aiCodingDaily": "Laravel quality, React-TS quality and edge-case testing (max 60); the bug-finding column is left out because it overlaps Bug Hunt. The harness is chosen per model by AI Coding Daily.",
}
# v3 Plan evidence grades shown with the site's grade vocabulary (controlled measurements are measured).
ROUTE_GRADES = {"controlled": "measured", "reports": "estimate", "assumption": "assumption", "diagnostic": "assumption"}
SCENARIO_STRATUM = "S1"  # the full-composite stream that authorises scenario labels (E100)


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


# --- helpers ---------------------------------------------------------------------------------


def slugify(model_id: str) -> str:
    return model_id.replace(".", "-")


def competition_ranks(values: dict) -> dict:
    """1 = highest; equal values share the better rank; entries without a value are skipped."""

    scored = {key: value for key, value in values.items() if value is not None}
    return {key: 1 + sum(1 for other in scored.values() if other > value) for key, value in scored.items()}


def _tier(cost_score: float | None) -> str | None:
    if cost_score is None:
        return None
    penalty = 100 - cost_score
    return next((name for limit, name in TIERS if penalty <= limit), "Expensive")


def _load(data: Path) -> dict[str, Any]:
    def read(name: str):
        return json.loads((data / name).read_text())

    return {
        "scores": read("scores.json"),
        "history": read("ranking_history_v1.5.json"),
        "report": read("aa_reconciliation_report.json"),
        "tb4": read("tb4.json"),
        "livebench": read("livebench.json"),
        "deepswe": read("aa_deepswe.json"),
        "bugHunt": read("bug_hunt.json"),
        "routes": read("plan_cost_routes.json"),
    }


def dimensions() -> list[dict]:
    """The value's dimensions: the cost score (fixed share) and the ten quality leaves."""

    quality_share = (100.0 - COST_WEIGHT_PCT) / 100.0
    rows = [{
        "key": COST_KEY, "label": "Cost", "fullLabel": "Cost (selected basis)", "category": "cost",
        "weightPct": COST_WEIGHT_PCT, "priority": None, "higherBetter": True, "sourceUrl": None,
    }]
    for leaf in q.LEAVES:
        rows.append({
            "key": leaf.key, "label": leaf.label, "fullLabel": leaf.label, "category": GROUP_CATEGORY[leaf.group],
            "weightPct": round(quality_share * leaf.weight, 4), "priority": leaf.weight, "higherBetter": True,
            "sourceUrl": LEAF_INFO[leaf.key]["url"],
        })
    return rows


def _route_view(route: dict | None, grade: str | None = None) -> dict | None:
    if route is None:
        return None
    return {
        "id": route["id"],
        "planLabel": route.get("planLabel"),
        "planFeeUsd": route.get("planPriceUsd"),
        "valueMultiple": route["valueMultiple"],
        "grade": ROUTE_GRADES[grade] if grade else evidence.route_grade(route.get("evidenceClass")),
        "evidenceLabel": plan_evidence_label(route),
        "sourceModel": route.get("sourceModel"),
        "sourceUrl": route.get("sourceUrl"),
        "sourceDate": route.get("sourcePublicationDate"),
    }


def _row_flags(row: dict) -> list[str]:
    """Plain-language flags for one v3 row, in a fixed order."""

    flags = []
    if row["api"]["costUsd"] is None:
        flags.append("No cost: AA publishes no cost for this configuration, so it has no value score and no rank")
    elif row["cost"]["subset"]:
        flags.append("Subset cost: scored on its own workload; cross-workload ordering not identified")
    claimed = [q.LEAF_BY_KEY[key].label for key, leaf in row["quality"].get("leaves", {}).items() if leaf.get("sourceType") == "model_provider_claim"]
    if claimed:
        flags.append("Provider-claimed leaf: " + ", ".join(claimed) + " is the model provider's own result; competes but earns no interval label")
    if row["quality"]["provisional"]:
        flags.append("Provisional quality: " + "; ".join(row["quality"]["provisionalReasons"]))
    if row["cost"]["partialComponents"]:
        flags.append("Partial cost component: AA marks tasks missing or declined")
    if row.get("aaCostCaveat"):
        flags.append("AA cost caveat: " + row["aaCostCaveat"])
    return flags


def pareto_set(rows: list[dict], workload: str, basis: str) -> set:
    """Point-estimate Pareto set on one basis: main-workload rows no other row beats on both cost and quality.

    Subset-cost rows sit on another workload, so their ordering against these rows is not identified (O17).
    """

    key = "api" if basis == "api" else "planScore"
    points = {
        row["id"]: (row[key]["costUsd"], row["quality"]["displayed"])
        for row in rows
        if row["cost"]["workload"] == workload and row[key]["costUsd"] is not None and row["quality"]["displayed"] is not None
    }
    return {
        row_id for row_id, (cost, quality) in points.items()
        if not any(c <= cost and qv >= quality and (c < cost or qv > quality) for other, (c, qv) in points.items() if other != row_id)
    }


def _scenario_view(v3: dict) -> dict:
    """S1 core shares per basis and row (rank 1, top 3, frontier), when the scenario outputs are current."""

    scenarios = v3.get("scenarios") or {}
    result = {"api": {}, "plan": {}}
    if scenarios.get("status") != "current":
        return result
    for basis in result:
        for run in scenarios["results"][basis]:
            if run["stratum"] == SCENARIO_STRATUM and not run["alternative"]:
                result[basis] = {row_id: {key: shares[key]["share"] for key in ("top1", "top3", "frontier")} for row_id, shares in run["rows"].items()}
    return result


# --- bundle ----------------------------------------------------------------------------------


FRONTIER_TIER_KEYS = ("aaFrontierTier", "aaFrontierConfiguration", "aaFrontierIntelligenceGap", "aaFrontierFootnote")


def _entry(source: dict, row: dict | None, quality_ranks: dict, frontier: dict, shares: dict, routes: dict, pareto: dict) -> dict:
    """One ``rankings.json`` model entry (v3 values for ranked rows; nulls for unranked roster rows)."""

    model_id = source["id"]
    base = {
        "slug": slugify(model_id),
        "name": source["name"],
        "shortName": source["shortName"],
        "developer": source["developer"],
        "aaUrl": source["aaUrl"],
        "aaVariant": source.get("aaVariant"),
        "rankingEligible": row is not None,
        "exclusionReasons": list(source.get("rankingExclusionReasons") or []),
        "intelligenceIndex": {"value": source.get("intelligenceIndex"), "status": source.get("intelligenceIndexStatus")},
        "speed": source.get("speed"),
        **{key: source.get(key) for key in FRONTIER_TIER_KEYS},
    }
    if row is None:
        return {
            **base,
            "rank": {"api": None, "plan": None},
            "overall": {"api": None, "plan": None},
            "quality": None,
            "qualityRank": None,
            "dims": {COST_KEY: None, **{leaf.key: None for leaf in q.LEAVES}},
            "costDims": {"api": None, "plan": None},
            "raw": {leaf.key: None for leaf in q.LEAVES},
            "coverage": {"pct": 0.0, "costAvailable": False, "missing": [leaf.label for leaf in q.LEAVES], "provisional": None, "provisionalReasons": []},
            "cost": {"apiUsd": None, "planUsd": None, "fallback": None, "route": None, "subset": None, "partialComponents": [], "workload": None, "planFlags": []},
            "grade": "missing",
            "pareto": {"api": False, "plan": False},
            "frontierStatus": {"api": None, "plan": None},
            "scenario": {"api": None, "plan": None},
            "flags": [],
            "tier": None,
        }
    leaves = row["quality"]["leaves"]
    audit = {item["leaf"]: item for item in row["quality"]["clipAudit"]}
    plan = row["plan"]
    route = routes.get((plan.get("routeId") or "").split("#")[0])
    cost_available = row["api"]["costScore"] is not None
    api_frontier = frontier.get(model_id)
    return {
        **base,
        "rank": {"api": row["api"]["rank"], "plan": row["planScore"]["rank"]},
        "overall": {"api": row["api"]["value"], "plan": row["planScore"]["value"]},
        "quality": row["quality"]["displayed"],
        "qualityRank": quality_ranks.get(model_id),
        "dims": {COST_KEY: None, **{leaf.key: (leaves[leaf.key]["z"] if leaf.key in leaves else None) for leaf in q.LEAVES}},
        "costDims": {"api": row["api"]["costScore"], "plan": row["planScore"]["costScore"]},
        "raw": {leaf.key: (audit[leaf.key]["raw"] if leaf.key in audit else None) for leaf in q.LEAVES},
        "coverage": {
            "pct": round(100.0 * row["quality"]["coverage"], 2),
            "costAvailable": cost_available,
            "missing": [leaf.label for leaf in q.LEAVES if leaf.key not in leaves],
            "provisional": row["quality"]["provisional"],
            "provisionalReasons": row["quality"]["provisionalReasons"],
        },
        "cost": {
            "apiUsd": row["api"]["costUsd"],
            "planUsd": row["planScore"]["costUsd"],
            "fallback": plan.get("fallback"),
            "route": _route_view(route, plan.get("grade")),
            "subset": row["cost"]["subset"],
            "partialComponents": row["cost"]["partialComponents"],
            "workload": row["cost"]["workload"],
            "planFlags": plan["flags"],
        },
        # Every scored value is an owner or AA measurement (provider claims never enter); Plan routes grade separately.
        "grade": "measured" if leaves else "missing",
        "pareto": {basis: model_id in pareto[basis] for basis in BASES},
        "frontierStatus": {"api": {"definite": api_frontier["definite"], "possible": api_frontier["possible"]} if api_frontier else None, "plan": None},
        # O48: the Plan shares are those of the configuration's own plan row (its selected route).
        "scenario": {"api": shares["api"].get(model_id), "plan": shares["plan"].get(row.get("planRowId"))},
        "flags": _row_flags(row),
        "tier": _tier(row["planScore"]["costScore"]),
    }


# O53/O54: the site path of each ranking; the max-effort ranking leads at /rankings/.
TRACK_PATHS = {"max": "/rankings/", "aicd": "/rankings/ai-coding-daily/"}
TRACK_LEADS = {
    "max": "One configuration per model family at its top effort, scored on the AA leaves plus LiveBench 2.0 Overall and two Vals AI boards.",
    "aicd": "The configurations AI Coding Daily has tested, mostly at high and medium effort, scored on the AA leaves plus AI Coding Daily.",
}


def build_bundle(data: Path = DATA, track: str | None = None) -> Bundle:
    """The site bundle. With no track, the leading ranking's bundle, carrying every other ranking in ``extras["tracks"]``;
    a configuration ranked only in another ranking takes its model page from that ranking (O53)."""

    if track is not None:
        with q.active_track(track):
            return _track_bundle(data, track)
    primary = build_bundle(data, q.DEFAULT_TRACK)
    others = {other: build_bundle(data, other) for other in q.TRACKS if other != q.DEFAULT_TRACK}
    primary.extras["tracks"] = others
    for slug, doc in primary.models.items():
        home = q.DEFAULT_TRACK
        if not doc["summary"]["rankingEligible"]:
            home = next((other for other, bundle in others.items() if bundle.models[slug]["summary"]["rankingEligible"]), q.DEFAULT_TRACK)
        if home != q.DEFAULT_TRACK:
            primary.models[slug] = others[home].models[slug]
        bundles = {q.DEFAULT_TRACK: primary, **others}
        primary.models[slug]["rankings"] = [
            {"track": key, "label": q.TRACK_LABELS[key], "href": TRACK_PATHS[key], "shown": key == home,
             "rankingEligible": entry["rankingEligible"], "rank": entry["rank"], "overall": entry["overall"]}
            for key, bundle in bundles.items() for entry in bundle.rankings["models"] if entry["slug"] == slug
        ]
    return primary


def _track_bundle(data: Path, track: str) -> Bundle:
    inputs = _load(data)
    scores = inputs["scores"]
    v3 = scores["v3"] if track == q.DEFAULT_TRACK else scores["v3Tracks"][track]
    roster = scores["models"]
    slugs = [slugify(source["id"]) for source in roster]
    if len(set(slugs)) != len(slugs):
        raise ValueError("duplicate model slug in data/scores.json")
    rows = {row["id"]: row for row in v3["rows"]}
    if not rows:
        raise ValueError("no ranked models in the v3 section of data/scores.json")
    names = {source["id"]: source["name"] for source in roster}
    quality_ranks = competition_ranks({row_id: row["quality"]["displayed"] for row_id, row in rows.items()})
    api_intervals = v3["intervals"]["api"]
    frontier = api_intervals.get("frontier") or {}
    shares = _scenario_view(v3)
    routes = {route["id"]: route for route in inputs["routes"]["routes"]}
    ranks = {basis: {row_id: row[key]["rank"] for row_id, row in rows.items()} for basis, key in (("api", "api"), ("plan", "planScore"))}

    pareto = {basis: pareto_set(v3["rows"], v3["mainWorkload"], basis) for basis in BASES}
    entries = {slugify(source["id"]): _entry(source, rows.get(source["id"]), quality_ranks, frontier, shares, routes, pareto) for source in roster}
    # O53: a configuration ranked only in another ranking says which leaves this ranking lacks and where it is ranked.
    missing = {item["id"]: item["missing"] for item in v3.get("incompleteEvidence", [])}
    for source in roster:
        entry = entries[slugify(source["id"])]
        if not entry["rankingEligible"] and source.get("rankingEligible") and source["id"] in missing:
            elsewhere = [q.TRACK_NAMES[key] for key, ranked in (source.get("rankings") or {}).items() if ranked and key != track]
            entry["exclusionReasons"] = [f"Not in the {q.TRACK_NAMES[track]}: no " + ", ".join(q.ALL_LEAVES[key].label for key in missing[source["id"]])
                                         + (f"; ranked in the {', '.join(elsewhere)}" if elsewhere else "")]
    # O42: the band of rank positions each ranked row cannot be separated from under benchmark sampling noise.
    bands = {basis: v3["diagnostics"]["rankSeparability"][basis]["bands"] for basis in BASES}
    transferred = set(v3["diagnostics"]["rankSeparability"]["planAssumedRouteRows"])
    for source in roster:
        plan_row = (rows.get(source["id"]) or {}).get("planRowId")
        entries[slugify(source["id"])]["band"] = {"api": bands["api"].get(source["id"]), "plan": bands["plan"].get(plan_row)}
        # I28: a Plan band on an owner-named transfer excludes the transfer's error.
        entries[slugify(source["id"])]["bandExcludesTransfer"] = plan_row in transferred
    ordered = sorted(entries.values(), key=lambda entry: (entry["rank"]["plan"] is None, entry["rank"]["plan"] or 0, entry["name"]))
    plan_models = _plan_models(v3, entries, routes, shares, bands, transferred)
    rankings = {
        "track": {"key": track, "label": q.TRACK_LABELS[track], "href": TRACK_PATHS[track]},
        "version": VERSION,
        "publishDate": DATE,
        "observedAt": scores["observedAt"],
        "methodologyVersion": v3["methodologyVersion"],
        "basketVersion": v3["basketVersion"],
        "bases": BASES,
        "defaultBasis": "plan",
        "costWeightPct": COST_WEIGHT_PCT,
        "exchangeRate": {basis: {k: v3["exchangeRate"][basis][k] for k in ("valuePointsPerCostDoubling", "qualityPointsPerCostDoubling", "anchorRatio")} for basis in BASES},
        "planExploratory": v3["identificationYield"]["exploratory"],
        "modelInclusion": model_inclusion(scores.get("frontierSelection"), roster),
        "dimensions": dimensions(),
        "categories": CATEGORIES,
        "models": ordered,
        "planModels": plan_models,
        "picks": {basis: build_picks(ordered, basis, BASES) for basis in BASES},
    }
    current = {
        "version": VERSION,
        "dateIso": dt.datetime.strptime(DATE, "%B %d, %Y").date().isoformat(),
        "dateHuman": DATE,
        "modelCount": len(rows),
        "dimensionCount": len(rankings["dimensions"]),
        "ranks": {row_id: {basis: ranks[basis][row_id] for basis in BASES} for row_id in rows},
    }
    bundle = Bundle(
        data=data,
        extras={"method": _method_summary(v3, names)},
        rankings=rankings,
        models={},
        plans=_plans(inputs, entries, v3),
        benchmarks=_benchmarks(inputs, v3),
        tb4=_tb4(inputs, roster),
        changelog=build_changelog(inputs["history"], current, names),
        livebench=_livebench(inputs),
    )
    bundle.models = {
        slugify(source["id"]): _model_doc(source, entries[slugify(source["id"])], rows.get(source["id"]), inputs, current, v3)
        for source in roster
    }
    return bundle


def _plan_models(v3: dict, entries: dict, routes: dict, shares: dict, bands: dict, transferred: set) -> list[dict]:
    """O48: the Plan-basis table, one entry per configuration and plan (``key`` is unique; ``slug`` still links the
    model page), followed by the roster rows that have no ranked configuration."""

    result = []
    for item in v3["planRows"]:
        entry = entries[slugify(item["configurationId"])]
        result.append({
            **entry,
            # A DOM id and CSS selector token: the plan row id's "@" becomes "--".
            "key": slugify(item["id"]).replace("@", "--"),
            "name": f"{entry['name']} · {item['plan'] or 'API-cost fallback'}",
            "planRow": {"plan": item["plan"], "routeId": item["routeId"], "multiple": item["multiple"], "representative": item["representative"]},
            "rank": {**entry["rank"], "plan": item["rank"]},
            "overall": {**entry["overall"], "plan": item["value"]},
            "costDims": {**entry["costDims"], "plan": item["costScore"]},
            "cost": {**entry["cost"], "planUsd": item["costUsd"], "fallback": item["fallback"], "route": _route_view(routes.get(item["routeId"] or ""), item["grade"]),
                     "planFlags": item["flags"]},
            "band": {**entry["band"], "plan": bands["plan"].get(item["id"])},
            "bandExcludesTransfer": item["id"] in transferred,
            "scenario": {**entry["scenario"], "plan": shares["plan"].get(item["id"])},
            "tier": _tier(item["costScore"]),
        })
    ranked = {item["configurationId"] for item in v3["planRows"]}
    result += [entry for entry in entries.values() if entry["slug"] not in {slugify(row_id) for row_id in ranked}]
    return sorted(result, key=lambda entry: (entry["rank"]["plan"] is None, entry["rank"]["plan"] or 0, entry["name"]))


def _method_summary(v3: dict, names: dict) -> dict:
    """The methodology facts the pages quote: cost label, basket, anchors, exchange rate, streams and the bar."""

    main = v3["mainWorkload"]
    admission = v3["admission"]
    scenarios = v3.get("scenarios") or {}
    bar = (v3["barPolicy"]["bars"] or [None])[0]
    return {
        "methodologyVersion": v3["methodologyVersion"],
        "costLabel": v3["costBoundary"]["label"],
        "basket": {
            "version": v3["basketVersion"],
            "admitted": [{"key": key, "label": basket.COMPONENT_LABELS.get(key, key)} for key in admission["admitted"]],
            "pending": [{"key": key, "label": basket.COMPONENT_LABELS.get(key, key)} for key, item in admission["components"].items() if not item["admitted"]],
        },
        "anchorVersion": v3["anchorVersion"],
        "anchors": {basis: {key: v3["workloads"][main]["anchors"][basis][key] for key in ("low", "high")} for basis in BASES},
        "exchangeRate": v3["exchangeRate"],
        "planExploratory": v3["identificationYield"]["exploratory"],
        # E196: the nominal 25% next to cost's share of the variance in value on the common panel (E189).
        "costVarianceShare": {basis: (v3["costInfluence"][basis]["commonWorkload"]["varianceAllocation"] or {}).get("cost") for basis in BASES},
        "streamDescriptions": scenarios.get("streamDescriptions", {}),
        "notQuantified": scenarios.get("notQuantified", []),
        # E192: the bar is a frozen quality level; the configuration at the median is named for audit only.
        "barLevel": f"quality {bar['level']:.1f} (the displayed quality of {names.get(bar['levelConfiguration'], bar['levelConfiguration'])} at freeze)" if bar else None,
        "barPolicy": f"lower median of {v3['barPolicy']['populationRule']}",
        # O34: the other ladder levels (lower and upper quartile), each a frozen quality level.
        "barLadder": [f"quality {item['level']:.1f}" for item in v3["barPolicy"]["bars"][1:]],
    }


# --- per-model documents --------------------------------------------------------------------


def _leaf_docs(row: dict | None, inputs: dict) -> list[dict]:
    """Every quality leaf for one model in weight order, with its source and evidence (missing ones included)."""

    leaves = row["quality"]["leaves"] if row else {}
    audit = {item["leaf"]: item for item in row["quality"]["clipAudit"]} if row else {}
    observed = {
        "deepswe": inputs["deepswe"].get("observedAt"),
        "bugHunt": inputs["bugHunt"].get("snapshotDate"),
        "terminalBench": (inputs["tb4"].get("observedAt") or "")[:10] or None,
    }
    docs = []
    for leaf in sorted(q.LEAVES, key=lambda item: -item.weight):
        present = leaf.key in leaves
        detail = leaves.get(leaf.key, {})
        variant = " / ".join(str(part) for part in (detail.get("configuration"), detail.get("agent") or detail.get("harness")) if part) or None
        docs.append({
            "key": leaf.key,
            "label": leaf.label,
            "category": CATEGORIES[GROUP_CATEGORY[leaf.group]],
            "weightPct": round((100.0 - COST_WEIGHT_PCT) * leaf.weight / 100.0, 4),
            "value": audit[leaf.key]["raw"] if present else None,
            "decimals": 3 if "(0-1)" in LEAF_INFO[leaf.key]["unit"] else 1,
            "unit": LEAF_INFO[leaf.key]["unit"],
            "normalized": detail.get("z"),
            "source": _leaf_source(leaf.key, detail) if present else None,
            "observedAt": (observed.get(leaf.key) or (inputs["scores"]["observedAt"] or "")[:10]) if present else None,
            "evaluatedVariant": variant,
            "note": f"Saturates the scoring anchor ({audit[leaf.key]['anchorPosition']})." if present and audit[leaf.key]["anchorPosition"] != "inside" else None,
            "grade": ("claim" if detail.get("sourceType") == "model_provider_claim" else "measured") if present else "missing",
        })
    return docs


def _leaf_source(key: str, detail: dict) -> dict:
    """The public source of one leaf: an O36/O37 gap fill names its publisher; a Terminal-Bench gap fill is tbench.ai's."""

    if detail.get("sourceType"):
        return {"name": detail["source"], "url": detail.get("url") or LEAF_INFO[key]["url"]}
    if key == "terminalBench" and detail.get("agent") != value_v3.DEFAULT_TB_HARNESS:
        return {"name": TB_GAP_SOURCE, "url": LEAF_INFO[key]["url"]}
    return {"name": SOURCE_NAMES.get(key, AA_SOURCE), "url": LEAF_INFO[key]["url"]}


def _component_docs(row: dict | None) -> list[dict]:
    if row is None:
        return []
    detail = row["cost"]["componentsDetail"]
    return [
        {
            "key": key,
            "label": basket.COMPONENT_LABELS.get(key, key),
            "costUsd": detail[key]["costUsd"],
            "completeness": detail[key]["completeness"],
            "source": detail[key]["source"],
            "admitted": key in row["cost"]["components"],
        }
        for key in basket.TARGET_COMPONENTS
        if key in detail
    ]


def _plan_rows(row: dict | None, routes: dict, plan_rows: list | None = None) -> list[dict]:
    """Every route-measurement pair naming the model, classified (E106), with its cost on this model's basket and, for
    the route its plan row ranks on (O48), that row's Plan rank and value."""

    if row is None:
        return []
    ranked = {item["routeId"]: item for item in plan_rows or [] if item["configurationId"] == row["id"] and item["routeId"]}
    selected = row["plan"].get("routeId")
    api = row["api"]["costUsd"]
    result = []
    for item in row["plan"]["admission"]:
        route = routes[item["routeId"].split("#")[0]]
        multiple = plan_routes.comparison_multiple(route)
        result.append({
            **{k: v for k, v in _route_view(route).items() if k != "sourceModel"},
            "case": item["case"],
            "officialDisplayEligible": item["officialDisplayEligible"],
            "planIntervalEligible": item["planIntervalEligible"],
            "usdPerRun": api / multiple if api is not None and multiple > 0 else None,
            "selected": item["routeId"] == selected,
            "planRank": (ranked.get(item["routeId"]) or {}).get("rank"),
            "planValue": (ranked.get(item["routeId"]) or {}).get("value"),
        })
    result.sort(key=lambda plan: (not plan["selected"], plan["usdPerRun"] is None, plan["usdPerRun"] or 0, plan["id"]))
    return result


def _scenario_doc(v3: dict, model_id: str, plan_row: str | None = None) -> dict:
    scenarios = v3.get("scenarios") or {}
    if scenarios.get("status") != "current":
        return {"status": scenarios.get("status"), "api": [], "plan": []}
    result = {"status": "current"}
    for basis in ("api", "plan"):
        result[basis] = []
        # O48: the Plan streams rank plan rows; a model page shows its own plan row (its selected route).
        key = plan_row if basis == "plan" else model_id
        for run in scenarios["results"][basis]:
            base = {"stratum": run["stratum"], "kernel": "endpoint-heavy" if run["alternative"] else "primary", "targetProfile": run.get("targetProfile")}
            # E167: a transfer-dependent row is declared unevaluable in the transfers-off Plan streams.
            reason = next((item["reason"] for item in run.get("excluded", []) if item["row"] == key), None)
            if key in run["rows"]:
                result[basis].append({**base, "unevaluable": None, **{event: run["rows"][key][event]["share"] for event in ("top1", "top3", "frontier")}})
            elif reason:
                result[basis].append({**base, "unevaluable": reason, "top1": None, "top3": None, "frontier": None})
    return result


def _model_doc(source: dict, entry: dict, row: dict | None, inputs: dict, current: dict, v3: dict) -> dict:
    model_id = source["id"]
    routes = {route["id"]: route for route in inputs["routes"]["routes"]}
    frontier_rows = [item for item in inputs["report"]["frontier"] if item.get("valueRankModelId") == model_id]
    on_frontier = bool(frontier_rows)
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
            "flags": entry["flags"],
        },
        "dimensions": _leaf_docs(row, inputs),
        "cost": {
            **entry["cost"],
            "costScore": entry["costDims"],
            "components": _component_docs(row),
            "aaCostCaveat": row.get("aaCostCaveat") if row else None,
            "selectionReason": row["plan"]["selectionReason"] if row else None,
            "planAmount": row["plan"]["amount"] if row else None,
        },
        "plans": _plan_rows(row, routes, v3.get("planRows", [])),
        "scenarios": _scenario_doc(v3, model_id, (row or {}).get("planRowId")),
        "intervals": {"api": entry["frontierStatus"]["api"], "plan": None},
        "history": model_history(inputs["history"], current, model_id),
        "frontier": {
            "onAaFrontier": on_frontier,
            "aaFrontierNote": (
                f"On the observed Artificial Analysis Intelligence Index versus total cost frontier as {frontier_rows[0]['name']}."
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


def _plans(inputs: dict, entries: dict, v3: dict) -> dict:
    routes = inputs["routes"]
    measured = {slugify(model_id): row for model_id, row in v3["measuredOnlyPlanView"]["rows"].items()}
    return {
        "asOf": routes.get("asOf"),
        "policy": routes["evidencePolicy"],
        "identificationYield": v3["identificationYield"],
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
                "apiUsd": entry["cost"]["apiUsd"],
                "planUsd": entry["cost"]["planUsd"],
                "fallback": entry["cost"]["fallback"],
                "routeId": entry["cost"]["route"]["id"] if entry["cost"]["route"] else None,
                "flags": entry["cost"]["planFlags"],
                "measuredOnly": measured.get(slug),
            }
            for slug, entry in sorted(entries.items())
            if entry["rankingEligible"]
        ],
        "workedExample": {"slugs": ["claude-opus-5-5", "gpt-6-1-sol"]},
    }


def _benchmarks(inputs: dict, v3: dict) -> dict:
    deepswe, bug_hunt = inputs["deepswe"], inputs["bugHunt"]
    rows = v3["rows"]

    def coverage(key: str) -> dict:
        return {"available": sum(1 for row in rows if key in row["quality"]["leaves"]), "cohort": len(rows)}

    owners = {
        "deepswe": ("Artificial Analysis Coding Agent Index", deepswe.get("observedAt")),
        "bugHunt": ("Bug Hunt Bench benchmark owner", bug_hunt.get("snapshotDate")),
    }
    sources = []
    for leaf in q.LEAVES:
        owner, observed = owners.get(leaf.key, ("Artificial Analysis", (inputs["scores"]["observedAt"] or "")[:10]))
        sources.append({
            "id": leaf.key,
            "name": leaf.label,
            "owner": owner,
            "url": LEAF_INFO[leaf.key]["url"],
            "observedAt": observed,
            "role": f"quality leaf ({CATEGORIES[GROUP_CATEGORY[leaf.group]]})",
            "weightPct": round((100.0 - COST_WEIGHT_PCT) * leaf.weight / 100.0, 4),
            "coverage": coverage(leaf.key),
            "unit": LEAF_INFO[leaf.key]["unit"],
            "execution": "AA-run" if leaf.source == "aa" else "independent",
            "notes": LEAF_NOTES.get(leaf.key),
        })
    admission = v3["admission"]
    report = inputs["report"]
    return {
        "sources": sources,
        "basket": {
            "version": v3["basketVersion"],
            "admitted": [{"key": key, "label": basket.COMPONENT_LABELS.get(key, key)} for key in admission["admitted"]],
            "pending": [
                {"key": key, "label": basket.COMPONENT_LABELS.get(key, key), "covered": item["covered"], "ranked": item["ranked"]}
                for key, item in admission["components"].items()
                if not item["admitted"]
            ],
            "referencePanelSize": admission["jointCovered"],
            "requiredPanelSize": admission["requiredPanelSize"],
        },
        "qualitySourceShares": v3["diagnostics"]["qualitySourceShares"],
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
    """Matched LiveBench rows (retired as a quality leaf, owner decision O26), cheapest first."""

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
    value = entry["cost"]["apiUsd"] if basis == "api" else entry["cost"]["planUsd"]
    return "no cost data" if value is None else f"${value:,.2f} per basket run"


def index_page(bundle: Bundle) -> dict:
    rankings = bundle.rankings
    ranked = [m for m in rankings["models"] if m["rankingEligible"]]
    by_slug = {m["slug"]: m for m in rankings["models"]}
    quality = min((m for m in ranked if m["qualityRank"] is not None), key=lambda m: (m["qualityRank"], m["name"]))
    headline = {}
    for basis, picks in rankings["picks"].items():
        value = by_slug[picks["value"]["slug"]]
        # O17, the provisional rule and E167: a leader scored on a subset workload, with provisional quality or, on the
        # Plan basis, through an owner-named transfer says so.
        transfer = basis == "plan" and (value["cost"]["route"] or {}).get("grade") == "assumption"
        caveats = [label for flag, label in ((value["cost"]["subset"], "subset cost"), (value["coverage"]["provisional"], "provisional quality"), (transfer, "owner-named transfer")) if flag]
        lead = f"{value['name']} leads the {rankings['bases'][basis]['label']} at {value['overall'][basis]:.1f}" + (f" ({', '.join(caveats)})" if caveats else "")
        headline[basis] = f"{lead} and also leads on quality." if value is quality else f"{lead}; {quality['name']} leads on quality."
    return {
        "headline": headline,
        # ValueRank's scope: the software-engineering share of quality and its leaves, stated on the home page.
        "focus": {"swePct": q.GROUPS["swe"], "sweLeaves": [leaf.label for leaf in q.LEAVES if leaf.group == "swe"]},
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
                "flags": m["flags"],
            }
            for m in ranked
        ],
        "dimensions": rankings["dimensions"],
        "chart": {
            basis: [
                {
                    "slug": m["slug"],
                    "name": m["name"],
                    "x": m["cost"]["apiUsd"] if basis == "api" else m["cost"]["planUsd"],
                    "y": m["quality"],
                    "pareto": m["pareto"][basis],
                    "costLabel": _cost_label(m, basis),
                }
                for m in ranked
                if (m["cost"]["apiUsd"] if basis == "api" else m["cost"]["planUsd"]) is not None
            ]
            for basis in rankings["bases"]
        },
        "rankingsJson": rankings,
    }


COLUMN_ORDER = (
    ("rank", "Rank"), ("name", "Model"), ("overall", "Value"), ("quality", "Quality"), ("cost", "Cost"),
    ("grade", "Evidence"), ("coverage", "Coverage"), ("developer", "Developer"), ("qualityRank", "Quality rank"),
    ("speed", "Speed"), ("ii", "Intelligence Index"), ("band", "Noise band"),
)
DEFAULT_COLUMNS = tuple(key for key, _label in COLUMN_ORDER[:7])


def rankings_page(bundle: Bundle) -> dict:
    """Column keys match ``assets/js/filters.js`` (``name`` is the model column)."""

    rankings = bundle.rankings
    columns = [{"key": key, "label": label} for key, label in COLUMN_ORDER]
    columns += [{"key": d["key"], "label": d["label"]} for d in rankings["dimensions"] if d["key"] != COST_KEY]
    track = rankings["track"]["key"]
    return {
        # O53/O54: each ranking has its own page; the heading names it and links the others.
        "heading": "Rankings" if track == q.DEFAULT_TRACK else q.TRACK_LABELS[track],
        "trackLead": TRACK_LEADS[track],
        "action": TRACK_PATHS[track],
        "trackLinks": [{"label": q.TRACK_LABELS[key], "href": TRACK_PATHS[key], "current": key == track} for key in q.TRACKS],
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
                "apiUsd": entry["cost"]["apiUsd"],
                "planUsd": entry["cost"]["planUsd"],
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
    ("How is the value score calculated?", "Cost carries a fixed {cost:.0f}% of the value score and quality the rest. The cost score compares what each configuration costs to run the SDLC cost basket once, on a log scale against frozen anchors, so equal cost ratios count equally. Quality is the weighted mean of the ranking's benchmark leaves ({leaves} in the max-effort ranking) on fixed 0-100 anchors."),
    ("What happens when a benchmark has no result for a model?", "ValueRank publishes two rankings, each over the configurations with its full benchmark set: the max-effort ranking (one configuration per family at its top effort, adding LiveBench 2.0 and two Vals AI boards) and the AI Coding Daily ranking (mostly high and medium efforts, adding AI Coding Daily). Within a ranking every model is scored on the same benchmarks. A result Artificial Analysis has not run comes from another party's run of the same benchmark on the exact configuration, then from the model provider's published result. A configuration still missing one after a logged exhaustive search is listed with the gap, not ranked. A configuration without a cost gets no value score."),
    ("What is the difference between the API ranking and the Plan ranking?", "Both price the same SDLC basket. The API ranking uses Artificial Analysis' cost at API rates. The Plan ranking divides it by a subscription route's Value Multiple, the API-priced usage a plan delivers per dollar of fee at full utilisation, and lists one row per configuration and plan; a model without an admitted route falls back to API cost, flagged."),
    ("What do the evidence grades mean?", "Measured values come from the benchmark owner or a controlled account measurement. Estimates are concordant end-user reports, and assumptions are owner-authorised transfers of one model's measured multiple to another."),
    ("Why is a model not ranked?", "The ranked cohort is fixed policy: every configuration Artificial Analysis plots on its Intelligence-versus-cost frontier or within 3 Index points of it, each effort as its own row. A cohort configuration missing a benchmark of both rankings after an exhaustive search is listed with the gap, not ranked; one ranked in only one ranking appears there. Other models still have pages with what we hold."),
)

LIMITATIONS = (
    "Cost is the contestant-model API token cost of AA's runs, not total agent or workflow operating cost.",
    "Cost scores use frozen anchors; a new anchor version is a published migration, never a silent change.",
    "The basket is AA's SDLC-relevant evaluations at AA's token mix, not your own workload.",
    "Results are never transferred between model versions or reasoning efforts; missing evidence stays missing.",
    "Published values are rounded; interval outputs and scenario shares show which differences the evidence supports. Benchmark sampling noise is approximated in one scenario stream (S1T) that treats tasks as independent, so adjacent ranks often lie within that noise.",
)
EXPLORATORY_LIMITATION = "Subscription Value Multiples are measured on their own workloads; none is yet identified on the basket, so the Plan ranking is exploratory."


def methodology_page(bundle: Bundle) -> dict:
    rankings = bundle.rankings
    ranked = sorted((m for m in rankings["models"] if m["rank"]["plan"] is not None), key=lambda m: (m["rank"]["plan"], m["name"]))
    chosen = next((m for m in ranked if m["coverage"]["pct"] < 100), ranked[0])
    quality_share = 100.0 - rankings["costWeightPct"]
    observed = [d for d in rankings["dimensions"] if d["key"] != COST_KEY and chosen["dims"][d["key"]] is not None]
    observed_priority = sum(d["priority"] for d in observed)
    rows = []
    for d in rankings["dimensions"]:
        value = chosen["costDims"]["plan"] if d["key"] == COST_KEY else chosen["dims"][d["key"]]
        included = value is not None
        if not included:
            effective = 0.0
        elif d["key"] == COST_KEY:
            effective = rankings["costWeightPct"]
        else:
            effective = round(quality_share * d["priority"] / observed_priority, 4)
        rows.append({
            "key": d["key"],
            "label": d["label"],
            "weightPct": d["weightPct"],
            "normalized": value,
            "included": included,
            "effectiveWeightPct": effective,
            "contribution": round((value or 0.0) * effective / 100, 3),
        })
    return {
        "method": bundle.extras["method"],
        "dimensions": rankings["dimensions"],
        "costWeightPct": rankings["costWeightPct"],
        "exchangeRate": rankings["exchangeRate"],
        "basketVersion": rankings["basketVersion"],
        "modelInclusion": rankings["modelInclusion"],
        "weights": {d["key"]: d["weightPct"] for d in rankings["dimensions"]},
        "workedExample": {
            "slug": chosen["slug"],
            "name": chosen["name"],
            "basis": "plan",
            "overall": chosen["overall"]["plan"],
            "qualityCoveragePct": chosen["coverage"]["pct"],
            "steps": rows,
            "missing": [row["label"] for row in rows if not row["included"]],
        },
        "faq": [{"q": question, "a": answer.format(cost=rankings["costWeightPct"], leaves=len(rankings["dimensions"]) - 1)} for question, answer in FAQ_TEMPLATE],
        "limitations": [*LIMITATIONS, *([EXPLORATORY_LIMITATION] if rankings["planExploratory"] else [])],
        "methodologyUrl": AA_METHODOLOGY_URL,
    }


def data_page(bundle: Bundle) -> dict:
    def schema(document: dict) -> str:
        return "{" + ", ".join(document) + "}"

    sample = next(iter(bundle.models.values()))
    files = [
        ("/data/rankings.json", "Every roster model with v3 value scores, ranks, basket cost and evidence on both bases, in the max-effort ranking.", schema(bundle.rankings)),
        *((f"/data/rankings-{track}.json", f"The same document for the {q.TRACK_NAMES[track]} (O53).", schema(other.rankings))
          for track, other in bundle.extras.get("tracks", {}).items()),
        ("/data/models/<slug>.json", "One document per roster model with every quality leaf, its source, the cost basket, plan routes, scenario shares and history.", schema(sample)),
        ("/data/plans.json", "Subscription routes, their evidence and every candidate's API and Plan basket cost.", schema(bundle.plans)),
        ("/data/benchmarks.json", "Quality-leaf sources and coverage, the admitted cost basket and the Artificial Analysis frontier.", schema(bundle.benchmarks)),
        ("/data/benchmarks/terminal-bench-4.json", "Terminal-Bench 4.0 official rows, provider claims and cohort mapping.", schema(bundle.tb4)),
        ("/data/changelog.json", "Versions, newest first, with recorded ranks and rank changes between consecutive releases.", schema(bundle.changelog)),
        ("/data/livebench.json", "Matched LiveBench rows (no longer scored; owner decision O26), with cost per successful task.", schema(bundle.livebench)),
    ]
    return {"files": [{"path": path, "description": description, "schema": shape} for path, description, shape in files]}
