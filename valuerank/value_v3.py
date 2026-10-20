"""ValueRank v3: the SDLC cost basket, the twelve-leaf quality vector, value scores and their checks.

This module assembles the engine modules (quality, basket, anchors, plan_routes,
intervals, scenarios, diagnostics) into the published v3 ranking:

1. ``assemble`` gathers exact-configuration evidence for every ranked
   configuration: quality observations (no transfer between efforts or
   versions; missing stays missing), basket cost components, the admitted
   workload (E26/E95/E101), each row's basket cost (O17 subset rows) and its
   Plan route (E85/E88/E93/E106).
2. ``freeze`` writes the frozen anchor objects per workload and basis (E20,
   E10) and the pinned bar references; a refresh never re-anchors silently.
3. ``score`` computes cost and value scores, ranks, gates, the cost-weight
   disclosures (E60, E91), the interval outputs (frontier and bar, E37/E38/E45)
   and the diagnostics.
4. ``run_scenarios`` draws the scenario shares with a published seed; they are
   released as a data file and attached to the scores only when their input
   hash matches the scored inputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import date
from pathlib import Path

from valuerank import anchors as anchor_math
from valuerank import basket
from valuerank import diagnostics
from valuerank import exact_match
from valuerank import intervals
from valuerank import plan_routes
from valuerank import quality as q
from valuerank import scenarios
from valuerank.clock import utcnow
from valuerank.paths import DATA
from valuerank.plan_costs import COST_WEIGHT_PCT

METHODOLOGY_VERSION = "3.0.0"
BASKET_VERSION = "SDLC basket v1"
BETA = COST_WEIGHT_PCT / 100.0
BASES = ("api", "plan")
TB4_HALF_WIDTH_PCT = 0.05  # tbench.ai resolution rates are published to 0.1 percentage point
BUG_HUNT_HALF_WIDTH = 0.05  # owner means of bugs fixed are published to 0.1 bug
FRACTION_LEAVES = {
    "frontierCode": "frontierCode",
    "automationBench": "automationBenchPartialScore",
    "lcr": "lcr",
    "hle": "hle",
    "scicode": "scicode",
    "critpt": "critpt",
}
CHART_SOURCES = {slug: f"AA {basket.COMPONENT_LABELS[slug]} total cost chart (labels rounded to USD 1)" for slug in basket.CHART_COMPONENTS}
DEFAULT_TB_HARNESS = "Terminus 2"  # E125: the named default harness of the same-harness diagnostic
SCENARIO_COUNT = 10_000
SCENARIO_RUNS = (("S0", False), ("S1", False), ("S2", False), ("S1", True), ("S1M", False))
MEASUREMENT_STREAM = "S1M"  # E162/E165: S1 plus conventional range sensitivity inside published 95% intervals (Terminal-Bench today)
# E165: Terminal-Bench documents a 95% confidence interval (its leaderboard whiskers; accuracy_ci95_half_width with
# n_trials) but not its estimand, method or sampling unit, so S1M's draws inside it are a conventional sensitivity.
TB_INTERVAL_CONTRACT = {
    "leaf": "terminalBench",
    "source": "https://www.tbench.ai/leaderboard/terminal-bench/4.0",
    "sourceStatement": "The whiskers span the 95% confidence interval",
    "confidenceLevel": 0.95,
    "sourceFields": ["accuracy_ci95_half_width", "n_trials"],
    "sourceEstimand": scenarios.NOT_ESTABLISHED,
    "sourceIntervalMethod": scenarios.NOT_ESTABLISHED,
    "samplingUnit": scenarios.NOT_ESTABLISHED,
    "repeatedTaskTreatment": scenarios.NOT_ESTABLISHED,
    "kernelStatus": "conventional-within-CI",
    "kernel": "uniform on [z - h, z + h] clipped to [0, 100] (arcsine alternative), h the published half-width",
    "tailTreatment": "values outside the interval are not explored; no tail mass is invented",
}
FROZEN_FILE = "v3_frozen.json"
SCENARIO_FILE = "v3_scenarios.json"


# --------------------------------------------------------------------------
# 1. Evidence
# --------------------------------------------------------------------------


def leaf_evidence(model_id: str, effort: str | None, page: dict, deepswe: dict | None, tb4_rows: list[dict], bug_hunt: dict | None) -> dict:
    """Exact-configuration observations for the eleven leaves, with provenance, evidence locators (E159) and the clipping audit (E110)."""

    observations, provenance, audit = {}, {}, []

    def add(key: str, raw, observation: q.Observation, source: dict, artifact: str, locator: str) -> None:
        check = q.clip_audit(key, raw)
        if not check["domainValid"]:
            raise ValueError(f"{model_id}: {key} value {raw!r} is outside its documented domain")
        observations[key] = observation
        provenance[key] = {**source, "evidence": {"artifact": f"data/{EVIDENCE_FILES[artifact][0]}", "locator": locator, "publishedValue": raw}}
        audit.append(check)

    page_path = f"pages[model.slug={page.get('slug')}].model"

    if deepswe is not None and exact_match.efforts_match(model_id, effort, deepswe.get("effort")):
        precision = deepswe.get("scorePrecision")
        half = precision / 2.0 if isinstance(precision, (int, float)) else 0.0
        add("deepswe", deepswe["scorePct"], q.percent_z(deepswe["scorePct"], half),
            {"source": "AA Coding Agent Index, DeepSWE v1.1", "configuration": deepswe.get("displayLabel"), "agent": deepswe.get("agent")},
            "deepswe", f"configurations[valueRankModelId={model_id}].scorePct")
    if exact_match.bug_hunt_matches(model_id, effort, bug_hunt):
        add("bugHunt", bug_hunt["fixedOf105"], q.bug_hunt_z(bug_hunt["fixedOf105"], BUG_HUNT_HALF_WIDTH),
            {"source": "Bug Hunt Bench owner-published runs", "configuration": bug_hunt.get("evaluatedModel"), "harness": bug_hunt.get("harness"), "runs": bug_hunt.get("sampleN")},
            "bugHunt", f"models[modelId={model_id}].fixedOf105")
    tb4 = exact_match.select_tb4_row(model_id, effort, tb4_rows)
    if tb4 is not None:
        add("terminalBench", tb4["resolutionRatePct"], q.percent_z(tb4["resolutionRatePct"], TB4_HALF_WIDTH_PCT),
            {"source": "tbench.ai Terminal-Bench 4.0 leaderboard", "configuration": tb4["model"], "agent": tb4.get("agent"),
             "ci95HalfWidthPct": tb4.get("uncertaintyPct")},
            "tb4", f"rows[model={tb4['model']}, agent={tb4.get('agent')}].resolutionRatePct")
    if page.get("gdpval") is not None:
        add("gdpval", page["gdpval"], q.gdpval_z(page["gdpval"]), {"source": "AA GDPval-AA v2.1 Elo as integrated in the pinned Index (E90)"}, "snapshot", f"{page_path}.gdpval")
    for key, field in FRACTION_LEAVES.items():
        if page.get(field) is not None:
            add(key, page[field], q.fraction_z(page[field]), {"source": f"AA field {field}"}, "snapshot", f"{page_path}.{field}")
    if page.get("omniscience") is not None:
        accuracy, hallucination = page.get("omniscienceAccuracy"), page.get("omniscienceHallucinationRate")
        rebuilt = q.omniscience_index_from_rates(accuracy, hallucination) if accuracy is not None and hallucination is not None else None
        unanswered = (1.0 - accuracy) * (1.0 - hallucination) if rebuilt is not None else None
        add("omniscience", page["omniscience"], q.omniscience_index_z(page["omniscience"]),
            {"source": "AA Omniscience Index (O28)", "accuracy": accuracy, "hallucinationRate": hallucination, "indexFromRates": rebuilt,
             "unansweredOrPartialShare": unanswered, "abstentionPenalisedZ": max(0.0, page["omniscience"])},
            "snapshot", f"{page_path}.omniscience")
    return {"observations": observations, "provenance": provenance, "clipAudit": audit}


def row_components(page: dict, cai_record: dict | None, chart_rows: dict) -> tuple[dict, dict]:
    """Basket components for one configuration: seven Index evaluations, the Coding Agent Index and chart totals."""

    components, reconciliation = basket.index_components(page.get("intelligenceIndexEvaluations") or [], (page.get("intelligenceIndexCost") or {}).get("total"))
    agent_index = basket.coding_agent_component(cai_record)
    if agent_index is not None:
        components[basket.CODING_AGENT_INDEX] = agent_index
    for slug, row in chart_rows.items():
        chart = basket.chart_component(row, source=CHART_SOURCES[slug])
        if chart is not None:
            components[slug] = chart
    return components, reconciliation


# E131: each source token field's mapping onto the exclusive canonical coordinates.
TOKEN_ONTOLOGY = {
    "intelligenceIndexEvaluations[].outputTokensPerTask": {"canonical": ["reasoning", "answer"], "mapping": "inclusive"},
    "canonicalIntelligenceIndexTokenCount.output": {"canonical": ["reasoning", "answer"], "mapping": "inclusive"},
    "canonicalIntelligenceIndexTokenCount.reasoning": {"canonical": ["reasoning"], "mapping": "exclusive"},
    "canonicalIntelligenceIndexTokenCount.answer": {"canonical": ["answer"], "mapping": "exclusive"},
    "canonicalIntelligenceIndexTokenCount.input": {"canonical": ["uncached input", "cache read", "cache write"], "mapping": "inclusive"},
}
INDEX_COMPONENTS = {**basket.INDEX_SDLC_TASKS, **basket.INDEX_RESIDUAL_TASKS}


def demand_registry(page: dict, admitted: list[str]) -> dict:
    """E124/E130/E131: set-identified demand populations from AA's public telemetry (never rescaled).

    The ten Intelligence Index executions are one population, conserved against
    AA's Index-wide token totals, with the excluded evaluations kept as residual
    demand; the Coding Agent Index is its own population (AA publishes no category
    telemetry for it). Output token fields are inclusive of reasoning and answer.
    """

    evaluations = {item.get("slug"): item for item in page.get("intelligenceIndexEvaluations") or []}
    outputs = {
        slug: evaluations[slug]["outputTokensPerTask"] * tasks
        for slug, tasks in INDEX_COMPONENTS.items()
        if (evaluations.get(slug) or {}).get("outputTokensPerTask") is not None
    }
    totals = page.get("canonicalIntelligenceIndexTokenCount") or {}
    inclusive = totals.get("output") is not None and totals.get("reasoning") is not None and totals.get("answer") is not None
    populations = {
        "intelligence-index": {
            "conservationTotalId": "canonicalIntelligenceIndexTokenCount",
            "conservationTotal": totals or None,
            "scoredComponents": [slug for slug in basket.INDEX_SDLC_TASKS if slug in admitted],
            "residualComponents": list(basket.INDEX_RESIDUAL_TASKS),
            "componentOutputTokens": outputs,
            "outputEqualsReasoningPlusAnswer": (totals["output"] == totals["reasoning"] + totals["answer"]) if inclusive else None,
        },
    }
    if basket.CODING_AGENT_INDEX in admitted:
        populations[basket.CODING_AGENT_INDEX] = {"conservationTotalId": None, "status": "no public category telemetry; demand unconstrained beyond its cost identity"}
    return {
        "status": "set-identified feasible region; M_W not identified",
        "populations": populations,
        "scoredVector": "d_iW = sum of the admitted Index components' d_ie + d_iA (Coding Agent Index)",
        "tokenOntology": TOKEN_ONTOLOGY,
        "identities": "p . d_ie = C_ie for each component under AA's category-linear valuation (E157: a banded provider tariff needs band-allocated demand, unavailable, so tariff-corrected valuation and transport stay unidentified); the Index totals bound the sum over all ten Index executions only",
        "missingForIdentification": ["category-specific burn coefficients for each plan meter", "or a controlled measurement on a workload compatible with W"],
    }


# E158: what each component's published cost covers. AA prices the contestant model's provider-reported tokens; for
# GDP.pdf it states that judge calls, PDF preparation and OCR are excluded. Nothing else is stated, so it stays unknown.
COST_LABEL = "contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost)"
COST_BOUNDARY_SOURCE = "https://artificialanalysis.ai/methodology/intelligence-benchmarking (fetched 2026-10-19)"
CHARGE_CLASSES = ("contestantModelTokens", "otherModelCalls", "externalTools", "executionEnvironment", "preparation", "grading")
COMPONENT_BOUNDARY = {"gdp-pdf": {"otherModelCalls": "excluded", "preparation": "excluded", "grading": "excluded"}}


def cost_boundary(component: str) -> dict:
    """One component's charge classes: included / excluded / not applicable / unknown (unknown unless documented)."""

    return {charge: "included" if charge == "contestantModelTokens" else COMPONENT_BOUNDARY.get(component, {}).get(charge, "unknown") for charge in CHARGE_CLASSES}


def valuation_contract(caveat: str | None) -> dict:
    """E157: AA's valuation is linear in token categories, so category totals suffice to reconcile it; a provider tariff
    banded by request (e.g. context length) needs band-allocated demand or a request ledger, which no source publishes."""

    return {
        "costSourceRule": "AA: provider-reported token counts priced per token category at AA's recorded prices, cache pricing included",
        "valuationSufficiency": "category totals sufficient for AA's published valuation",
        "providerBillingRule": "banded tariff not reflected in AA's cost (AA cost caveat)" if caveat else "not recorded",
        "tariffCorrectedValuation": "unidentified: billing-band allocation unavailable" if caveat else "not assessed: provider billing rule not recorded",
        "tariffAllocationSupport": "unavailable",
    }


def restricted_cost(components: dict, workload_components: list[str]) -> float | None:
    """A configuration's cost on a workload's components, or None unless it has every one of them."""

    if any(components.get(component) is None for component in workload_components):
        return None
    return sum(components[component]["costUsd"] for component in workload_components)


def _observation_json(observation: q.Observation) -> dict:
    return {"z": observation.z, "halfWidth": observation.half_width, "low": observation.low, "high": observation.high}


def _summary_json(summary: q.QualitySummary) -> dict:
    return {
        "displayed": summary.displayed,
        "lower": summary.lower,
        "upper": summary.upper,
        "coverage": summary.coverage,
        "provisional": summary.provisional,
        "provisionalReasons": list(summary.provisional_reasons),
        "sweLeaves": summary.swe_leaves,
        "sweWeight": summary.swe_weight,
    }


def assemble(configurations: list[dict], documents: dict, *, release_day: date) -> dict:
    """Evidence, admission, basket costs and Plan routes for every ranked configuration (no anchors yet)."""

    pages = {page["model"]["slug"]: page["model"] for page in documents["snapshot"]["pages"]}
    deepswe_by_id = {item["valueRankModelId"]: item for item in documents["deepswe"]["configurations"] if item.get("valueRankModelId")}
    bug_hunt_by_id = {item["modelId"]: item for item in documents["bugHunt"]["models"]}
    agent_records = {item["label"]: item for item in documents["codingAgents"]["configurations"]}
    chart_rows = {item["slug"]: {row["model"]: row for row in item["rows"]} for item in documents["costCharts"]["evaluations"]}
    mapping = documents["configurationMap"]["rows"]
    routes = documents["planRoutes"]["routes"]
    rows = []
    for configuration in configurations:
        model_id, effort = configuration["id"], configuration.get("effort")
        page = pages.get(configuration["aaSlug"])
        if page is None:
            raise ValueError(f"{model_id}: AA model page {configuration['aaSlug']} is missing from the pinned snapshot")
        # A cohort row without a pinned map entry keeps its Index evidence; its agent and chart costs are missing (flagged).
        labels = mapping.get(model_id) or {}
        evidence = leaf_evidence(model_id, effort, page, deepswe_by_id.get(model_id), documents["tb4"]["rows"], bug_hunt_by_id.get(model_id))
        components, reconciliation = row_components(
            page,
            agent_records.get(labels.get(basket.CODING_AGENT_INDEX)),
            {slug: chart_rows[slug].get(labels.get(slug)) for slug in basket.CHART_COMPONENTS},
        )
        candidates = plan_routes.route_candidates(model_id, effort, routes, release_day)
        rows.append({
            "page": page,
            "routeCandidates": candidates,
            **configuration,
            "evidence": evidence,
            "summary": q.summarize(evidence["observations"]),
            "components": components,
            "indexReconciliation": reconciliation,
            "configurationMapped": model_id in mapping,
            "routeSelection": plan_routes.route_selection(candidates),
            "admissionTable": plan_routes.admission_table(model_id, effort, routes, release_day),
        })
    ids = [row["id"] for row in rows]
    admission = basket.admission_panel({row["id"]: row["components"] for row in rows}, ids)
    admitted = admission["admitted"]
    main = basket.workload_hash(admitted)
    for row in rows:
        row["cost"] = basket.row_cost(row["components"], admitted)
        selected = row["routeSelection"]["selected"]
        row["plan"] = plan_routes.plan_cost(row["cost"]["costUsd"], selected)
    return {"rows": rows, "admission": admission, "admitted": admitted, "mainWorkload": main, "releaseDay": release_day.isoformat(), "tb4Rows": documents["tb4"]["rows"]}


def workload_catalog(assembled: dict) -> dict:
    """Every workload a ranked row is scored on: the main workload and any O17 subset workloads."""

    catalog = {assembled["mainWorkload"]: {"components": list(assembled["admitted"]), "role": "main"}}
    for row in assembled["rows"]:
        workload = row["cost"]["workload"]
        if workload is not None and workload not in catalog:
            catalog[workload] = {"components": list(row["cost"]["components"]), "role": "subset"}
    return catalog


def basis_cost_on(row: dict, workload_components: list[str], basis: str) -> float | None:
    """E152: a row's cost on a workload, typed by basis: the API sum A, or P = A / m with the row's selected
    displayed multiple m (an API-fallback row's Plan cost is A, as on the primary workload)."""

    return restricted_cost(row["components"], workload_components) if basis == "api" else _plan_cost_on(row, workload_components)


def _plan_cost_on(row: dict, workload_components: list[str]) -> float | None:
    cost = restricted_cost(row["components"], workload_components)
    if cost is None:
        return None
    selected = row["routeSelection"]["selected"]
    return cost if selected is None else cost / plan_routes.comparison_multiple(selected["route"])


# --------------------------------------------------------------------------
# 2. Frozen anchors and bar references
# --------------------------------------------------------------------------


def api_boxes(assembled: dict) -> list[intervals.Box]:
    """R_W on the API basis: ranked rows with FullCost on the main workload (E37), as admissible boxes."""

    boxes = []
    for row in assembled["rows"]:
        cost = row["cost"]
        if cost["fullCost"] and cost["workload"] == assembled["mainWorkload"] and anchor_math.scoreable(cost["lowUsd"]):
            summary = row["summary"]
            boxes.append(intervals.Box(row["id"], cost["lowUsd"], cost["highUsd"], summary.lower, summary.upper, summary.provisional))
    return boxes


def plan_boxes(assembled: dict) -> list[intervals.Box]:
    """R_W on the Plan basis: FullCost on the main workload and an identified, finite M_W (E106 PlanIntervalEligible)."""

    boxes = []
    for row in assembled["rows"]:
        selected = row["routeSelection"]["selected"]
        cost = row["cost"]
        if selected is None or not cost["fullCost"] or cost["workload"] != assembled["mainWorkload"]:
            continue
        bounds = plan_routes.identified_bounds(selected)
        # E138: an unrecorded or different valuation basis is never interval-eligible.
        if bounds is None or not anchor_math.scoreable(bounds[1]) or selected["valuation"] not in {"release", "revalued"}:
            continue
        summary = row["summary"]
        boxes.append(intervals.Box(row["id"], cost["lowUsd"] / bounds[1], cost["highUsd"] / bounds[0], summary.lower, summary.upper, summary.provisional))
    return boxes


BAR_POLICY = {
    "policyId": "median-definite-frontier",
    "version": 1,
    "selectionMode": "deterministic at anchor freeze, before any bar outcome is computed",
    "populationRule": "non-provisional configurations on the API main-workload definite frontier of the interval outputs",
    "order": "displayed quality ascending, then configuration ID",
    "position": "lower median",
    "emptyPopulation": "no bar pinned; the bar is published as unavailable",
    "lifetime": "fixed for the anchor version; replaced only by a versioned re-freeze that publishes old- and new-bar results on the common evaluable panel",
}


# E160: the registered rule that selects each workload's anchor references (separate from workload admission).
ANCHOR_POLICY = {
    "policyId": "complete-evidence-panel",
    "version": 1,
    "populationRule": "ranked configurations with complete cost evidence (exact cost, no AA missing- or declined-task marker) on every component of the workload at the freeze cutoff; on the main workload this is the admission reference panel",
    "planRule": "the same configurations at their displayed Plan cost: measured routes, owner-named transfers and API-cost fallbacks alike, since each is scored in the Plan table (O13, O16) and a narrower panel would clip them",
    "minimumReferences": 2,
    "belowMinimum": "anchors unavailable: configurations on that workload get no cost score (the main workload must meet the minimum)",
    "lifetime": "reference IDs and costs are frozen; a population or rule change is a new anchor version with an old/new bridge, and evidence lost after freezing never rebuilds an anchor",
}
MIN_ANCHOR_REFERENCES = 2


def anchor_population(assembled: dict, components: list[str]) -> list[str]:
    """E160: ranked configurations with complete cost evidence on every component of a workload."""

    return sorted(
        row["id"] for row in assembled["rows"]
        if all((row["components"].get(component) or {}).get("completeness") == basket.COMPLETE for component in components)
    )


def freeze(assembled: dict, *, frozen_at: str) -> dict:
    """Anchor objects per workload and basis from the registered anchor population (E160), and the bar reference."""

    workloads = {}
    by_id = {row["id"]: row for row in assembled["rows"]}
    for workload, entry in workload_catalog(assembled).items():
        components = entry["components"]
        population = anchor_population(assembled, components)
        if len(population) < MIN_ANCHOR_REFERENCES:
            if entry["role"] == "main":
                raise ValueError(f"the main workload has {len(population)} complete-evidence anchor references; at least {MIN_ANCHOR_REFERENCES} are required")
            workloads[workload] = {**entry, "anchors": {"api": None, "plan": None}, "anchorStatus": f"unavailable: fewer than {MIN_ANCHOR_REFERENCES} complete-evidence references"}
            continue
        api = {row_id: restricted_cost(by_id[row_id]["components"], components) for row_id in population}
        plan = {row_id: _plan_cost_on(by_id[row_id], components) for row_id in population}
        workloads[workload] = {
            **entry,
            "anchors": {
                "api": anchor_math.anchor_object(api, basis="api", workload=workload),
                "plan": anchor_math.anchor_object(plan, basis="plan", workload=workload),
            },
            "anchorStatus": "frozen",
        }
    frontier = intervals.frontier(api_boxes(assembled))
    by_id = {row["id"]: row for row in assembled["rows"]}
    # E156: the bar reference comes from the registered policy, at freeze, before any bar outcome is computed.
    population = [row_id for row_id, result in frontier.items() if result["definite"] == intervals.CERTIFIED and not by_id[row_id]["summary"].provisional]
    definite = sorted(population, key=lambda row_id: (by_id[row_id]["summary"].displayed, row_id))
    references = []
    if definite:
        references.append({
            "id": definite[(len(definite) - 1) // 2],
            "rule": "median definite-frontier configuration on the API basis at freeze, by displayed quality (lower median)",
        })
    return {
        "schemaVersion": 1,
        "methodologyVersion": METHODOLOGY_VERSION,
        "anchorVersion": f"v3-{frozen_at}",
        "frozenAt": frozen_at,
        "basketVersion": BASKET_VERSION,
        "mainWorkload": assembled["mainWorkload"],
        "workloads": workloads,
        "barReferences": references,
        "anchorPolicy": ANCHOR_POLICY,
        "barPolicy": {**BAR_POLICY, "selectionCutoff": frozen_at, "population": sorted(population), "referenceIds": [item["id"] for item in references]},
    }


# --------------------------------------------------------------------------
# 3. Scores, gates, interval outputs and diagnostics
# --------------------------------------------------------------------------


def competition_ranks(values: dict) -> dict:
    """1 = highest value; equal values share the better rank (E96)."""

    scored = {key: value for key, value in values.items() if value is not None}
    return {key: 1 + sum(1 for other in scored.values() if other > value) for key, value in scored.items()}


def _basis_cost(row: dict, basis: str) -> float | None:
    return row["cost"]["costUsd"] if basis == "api" else row["plan"]["costUsd"]


def _anchors_for(frozen: dict, workload: str | None, basis: str) -> dict | None:
    if workload is None:
        return None
    entry = frozen["workloads"].get(workload)
    if entry is None:
        raise ValueError(f"workload {workload} has no frozen anchors; anchoring a new workload is a versioned migration (run `freeze`)")
    return entry["anchors"][basis]


def interval_outputs(assembled: dict, frozen: dict, basis: str) -> dict:
    """Frontier and bar results over R_W for one basis, with the universe and the unevaluable rows (E38)."""

    boxes = api_boxes(assembled) if basis == "api" else plan_boxes(assembled)
    universe = sorted(box.row for box in boxes)
    unevaluable = sorted(row["id"] for row in assembled["rows"] if row["id"] not in universe)
    if not boxes:
        reason = "no row has FullCost and an identified M_W (E61/E67)" if basis == "plan" else "no row has FullCost on the main workload"
        return {"universe": [], "unevaluable": unevaluable, "status": intervals.UNEVALUABLE, "reason": reason}
    return {"universe": universe, "unevaluable": unevaluable, "status": "evaluated", "frontier": intervals.frontier(boxes), "bars": _bar_results(boxes, assembled, frozen)}


def _bar_results(boxes: list[intervals.Box], assembled: dict, frozen: dict) -> list[dict]:
    by_id = {row["id"]: row for row in assembled["rows"]}
    results = []
    for reference in frozen["barReferences"]:
        row = by_id.get(reference["id"])
        if row is None or row["summary"].displayed is None:
            results.append({"reference": reference, "status": intervals.UNEVALUABLE, "reason": "reference quality is not evaluable"})
            continue
        summary = row["summary"]
        outcome = intervals.cheapest_above_bar(boxes, intervals.Reference(row["id"], summary.lower, summary.upper))
        results.append({"reference": reference, "referenceQuality": {"lower": summary.lower, "upper": summary.upper}, **outcome})
    return results


# E146: registered deletion branches. Displayed-score sensitivity removes the leaf set R globally and
# renormalises the remaining observed weights: Q(-R) = sum_{b in O\R} w_b z_b / sum_{b in O\R} w_b (a zero
# denominator leaves the row unevaluable); cost, workload, route and anchors stay primary.
LEAVE_OUT_MIN_WEIGHT = 0.40
SOURCE_LEAVES = {"Artificial Analysis": tuple(leaf.key for leaf in q.LEAVES if leaf.source == "aa")}


def deletion_branches() -> list[dict]:
    """Every registered branch: one per leaf (leave-one-benchmark-out) and one per multi-leaf source.

    A single-leaf source (Bug Hunt Bench, Terminal-Bench) coincides with its
    leaf's branch, which carries both labels; the Bug Hunt branch is the
    standing Bug Hunt removal.
    """

    single = {leaf.key: leaf for leaf in q.LEAVES if leaf.source != "aa"}
    branches = []
    for leaf in q.LEAVES:
        labels = ["leave-one-benchmark-out"] + (["leave-one-source-out"] if leaf.key in single else [])
        branches.append({"id": f"leave-out:{leaf.key}", "labels": labels, "removed": [leaf.key]})
    for source, keys in SOURCE_LEAVES.items():
        branches.append({"id": f"leave-source-out:{source}", "labels": ["leave-one-source-out"], "removed": list(keys)})
    return branches


def deletion_quality(observations: dict, removed: set) -> float | None:
    """Q(-R) for one row: the observed leaves outside R, renormalised (None when none remain)."""

    return q.summarize({key: value for key, value in observations.items() if key not in removed}).displayed


def _deletion_sensitivity(rows: list[dict], per_row: dict) -> list[dict]:
    """E146: each registered deletion branch's rank changes on the common panel (E65), per basis."""

    results = []
    for branch in deletion_branches():
        removed = set(branch["removed"])
        retained = sum(leaf.weight for leaf in q.LEAVES if leaf.key not in removed) / 100.0
        entry = {**branch, "retainedNominalWeight": retained}
        if retained < LEAVE_OUT_MIN_WEIGHT:
            results.append({**entry, "status": "not identifiable under the coverage rule"})
            continue
        unevaluable = sorted(row["id"] for row in rows if deletion_quality(row["evidence"]["observations"], removed) is None)
        bases = {}
        for basis in BASES:
            primary, branched = {}, {}
            for row in rows:
                quality = deletion_quality(row["evidence"]["observations"], removed)
                scores = per_row[row["id"]][basis]
                if scores["value"] is None or quality is None:
                    continue
                primary[row["id"]] = scores["value"]
                branched[row["id"]] = anchor_math.value_score(scores["costScore"], quality, BETA)
            panel = sorted(primary)
            bases[basis] = {
                "rankChanges": diagnostics.paired_rank_change(primary, branched),
                "kendallTauB": diagnostics.kendall_tau_b([primary[key] for key in panel], [branched[key] for key in panel]),
            }
        results.append({**entry, "status": "evaluated", "unevaluableRows": unevaluable, "bases": bases})
    return results


# E64/E149: the standing cost-component removal. The Coding Agent Index runs Terminal-Bench v4 too, so the
# column removes AA's Index-run Terminal-Bench 4.0 cost; quality stays primary (E146 governs quality deletion).
STANDING_COST_REMOVAL = "terminalbench-4-0"
FIXED_ANCHOR_LABEL = "cost-component removal, original anchors"
RECALIBRATED_LABEL = "alternative workload, recalibrated anchors"
FIXED_MULTIPLE_LABEL = "fixed-multiple arithmetic stress (not identified Plan economics for the altered workload)"


def cost_removal(assembled: dict, frozen: dict, per_row: dict, component: str = STANDING_COST_REMOVAL) -> dict:
    """The cost-deletion branch object D_cost = (R_C, W - R_C, anchor, route, multiple and panel policies).

    Two calculations on the main-workload panel, each compared with the primary
    ranks on the common panel (E65): the removed component's cost subtracted and
    scored on the original anchor object, and the alternative workload scored on
    anchors rebuilt by the freeze rule (its exchange rate published). The Plan
    basis keeps each row's selected route and displayed multiple, labelled as a
    fixed-multiple arithmetic stress.
    """

    main = assembled["mainWorkload"]
    if component not in assembled["admitted"]:
        return {"component": component, "status": "not in the admitted basket"}
    remaining = [item for item in assembled["admitted"] if item != component]
    workload = basket.workload_hash(remaining)
    rows = [row for row in assembled["rows"] if row["cost"]["workload"] == main]
    bases = {}
    for basis in BASES:
        costs = {row["id"]: basis_cost_on(row, remaining, basis) for row in assembled["rows"]}
        original = frozen["workloads"][main]["anchors"][basis]
        rebuilt = anchor_math.anchor_object(costs, basis=basis, workload=workload)
        primary = {row["id"]: per_row[row["id"]][basis]["value"] for row in rows}
        fixed = {row["id"]: anchor_math.value_score(anchor_math.cost_score(costs[row["id"]], original), row["summary"].displayed, BETA) for row in rows}
        recalibrated = {row["id"]: anchor_math.value_score(anchor_math.cost_score(costs[row["id"]], rebuilt), row["summary"].displayed, BETA) for row in rows}
        bases[basis] = {
            "multiplePolicy": FIXED_MULTIPLE_LABEL if basis == "plan" else None,
            "fixedAnchors": {"label": FIXED_ANCHOR_LABEL, "rankChanges": diagnostics.paired_rank_change(primary, fixed)},
            "recalibrated": {
                "label": RECALIBRATED_LABEL,
                "anchors": {key: rebuilt[key] for key in ("low", "high", "referenceIds")},
                "exchangeRate": anchor_math.exchange_rate(rebuilt, BETA),
                "rankChanges": diagnostics.paired_rank_change(primary, recalibrated),
            },
        }
    return {
        "component": component,
        "status": "evaluated",
        "alternativeWorkload": {"id": workload, "components": remaining},
        "routePolicy": "each row's selected route on the primary workload",
        "panelRule": "main-workload rows with a value in both runs (E65)",
        "bases": bases,
    }


def _rule(rule: str, status: str, detail: str) -> dict:
    return {"rule": rule, "status": status, "detail": detail}


def score(assembled: dict, frozen: dict) -> dict:
    """Scores per basis, ranks, gates, disclosures, interval outputs, diagnostics and the active-rules manifest."""

    main = assembled["mainWorkload"]
    if frozen["mainWorkload"] != main:
        raise ValueError("the admitted main workload changed since the anchors were frozen; this is a workload migration (run `freeze`)")
    rows = assembled["rows"]
    per_row = {}
    for row in rows:
        entry = {}
        for basis in BASES:
            anchors = _anchors_for(frozen, row["cost"]["workload"], basis)
            cost = _basis_cost(row, basis)
            cost_score = anchor_math.cost_score(cost, anchors) if anchors else None
            entry[basis] = {"costUsd": cost, "costScore": cost_score, "value": anchor_math.value_score(cost_score, row["summary"].displayed, BETA)}
        per_row[row["id"]] = entry
    ranks = {basis: competition_ranks({row_id: entry[basis]["value"] for row_id, entry in per_row.items()}) for basis in BASES}
    gates, influence, exchange = {}, {}, {}
    for basis in BASES:
        clip = []
        for workload in frozen["workloads"]:
            costs = {row["id"]: _basis_cost(row, basis) for row in rows if row["cost"]["workload"] == workload}
            anchors = frozen["workloads"][workload]["anchors"][basis]
            if costs and anchors:
                clip.append({"workload": workload, **anchor_math.clip_gate(costs, anchors)})
        gates[basis] = clip
        influence[basis] = anchor_math.panel_cost_influence(
            [{"id": row["id"], "workloadId": row["cost"]["workload"], "costScore": per_row[row["id"]][basis]["costScore"], "qualityScore": row["summary"].displayed} for row in rows],
            BETA,
            main,
        )
        main_anchors = frozen["workloads"][main]["anchors"][basis]
        exchange[basis] = {**anchor_math.exchange_rate(main_anchors, BETA), "curve": anchor_math.exchange_rate_curve(BETA, [4.0, 16.0, 64.0, 256.0, 1024.0])}
    hold = any(item["hold"] for basis in BASES for item in gates[basis])
    yield_ = plan_routes.identification_yield({row["id"]: row["routeSelection"]["selected"] for row in rows})
    agreement = _quality_agreement(rows)
    measured = _measured_only_view(rows, frozen, per_row)
    manifest = [
        _rule("clip gate (E20)", "fired" if hold else "passed", "release held" if hold else "no basis exceeds the clipping allowance"),
        _rule("cost influence flag (E91)", "fired" if influence["api"]["flag"] or influence["plan"]["flag"] else "passed", "cost not discriminating (< 10%); informational only; beta never changes (O2)"),
        _rule("quality influence flag (E126)", "fired" if influence["api"]["qualityFlag"] or influence["plan"]["qualityFlag"] else "passed", "quality not discriminating (cost share > 90%); informational only"),
        _rule("subset scoring (O17)", "fired" if any(row["cost"]["subset"] for row in rows) else "vacuous", "subset rows scored on their own workload and anchors"),
        _rule("partial component flag (E37)", "fired" if any(row["cost"]["partialComponents"] for row in rows) else "vacuous", "AA declined- or missing-task markers"),
        _rule("route dominance filter (E88)", "fired" if any(row["routeSelection"]["dominated"] for row in rows) else "vacuous", "certifiably dearer routes set aside"),
        _rule("Plan exploratory label (E61)", "fired" if yield_["exploratory"] else "passed", "fewer than half of Plan rows have an identified M_W"),
        _rule("score swing gate (> 5 points without cause)", "vacuous", "first v3 release: no previous v3 release to compare"),
        _rule("configuration map coverage", "fired" if not all(row["configurationMapped"] for row in rows) else "passed",
              "cohort rows without a pinned agent/chart configuration identity: " + ", ".join(sorted(row["id"] for row in rows if not row["configurationMapped"])) if not all(row["configurationMapped"] for row in rows) else "every cohort row has a pinned identity"),
        _rule("quality clipping audit (E110)", "fired" if any(item["anchorPosition"] != "inside" for row in rows for item in row["evidence"]["clipAudit"]) else "passed", "saturation disclosed; domain violations block the build"),
    ]
    return {
        "methodologyVersion": METHODOLOGY_VERSION,
        "basketVersion": BASKET_VERSION,
        "beta": BETA,
        "anchorVersion": frozen["anchorVersion"],
        "barPolicy": frozen["barPolicy"],
        "anchorPolicy": frozen["anchorPolicy"],
        "costBoundary": {
            "label": COST_LABEL,
            "source": COST_BOUNDARY_SOURCE,
            "chargeClasses": list(CHARGE_CLASSES),
            "components": {component: cost_boundary(component) for component in assembled["admitted"]},
        },
        "mainWorkload": main,
        "admission": {key: value for key, value in assembled["admission"].items() if key != "matrices"},
        "admissionMatrices": assembled["admission"]["matrices"],
        "workloads": {
            workload: {"components": entry["components"], "role": entry["role"], "anchors": entry["anchors"], "anchorStatus": entry["anchorStatus"]}
            for workload, entry in frozen["workloads"].items()
        },
        "exchangeRate": exchange,
        "costInfluence": influence,
        "gates": {"clip": gates, "hold": hold},
        "identificationYield": yield_,
        "rows": [_row_json(row, per_row[row["id"]], ranks) for row in rows],
        "intervals": {basis: interval_outputs(assembled, frozen, basis) for basis in BASES},
        "measuredOnlyPlanView": measured,
        "diagnostics": {
            "terminalBenchSameHarness": _tb_same_harness(rows, assembled["tb4Rows"]),
            "anchorStability": _anchor_stability(rows, frozen, main, per_row),
            "omniscienceAbstentionSensitivity": _abstention_sensitivity(rows, per_row),
            "qualitySourceShares": q.source_shares(),
            "qualityAgreement": agreement,
            "nonDiscriminatingLeaves": diagnostics.non_discriminating(_z_by_leaf(rows)),
            "groupDrift": _group_drift(rows),
            "qualityDispersion": _panel_dispersion(rows),
            "deletionSensitivity": _deletion_sensitivity(rows, per_row),
            "costRemoval": cost_removal(assembled, frozen, per_row),
        },
        "manifest": manifest,
    }


MEASURED_VIEW_SPEC = {
    "admission": "exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics)",
    "selection": "the official selector (E111, E88, E85) rerun among the admitted candidates",
    "anchors": "the official Plan anchor object of the row's workload",
    "panel": "rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback)",
}


def _measured_only_view(rows: list[dict], frozen: dict, per_row: dict) -> dict:
    """E113: the measured-only Plan view D_measured, compared with the official Plan ranks on the common panel."""

    entries, values = {}, {}
    for row in rows:
        selection = plan_routes.measured_only_selection(row["routeCandidates"])
        selected = selection["selected"]
        if selected is None or row["cost"]["costUsd"] is None:
            entries[row["id"]] = {"status": "no measured route"}
            continue
        cost = row["cost"]["costUsd"] / plan_routes.comparison_multiple(selected["route"])
        anchors = _anchors_for(frozen, row["cost"]["workload"], "plan")
        score_value = anchor_math.cost_score(cost, anchors) if anchors else None
        value = anchor_math.value_score(score_value, row["summary"].displayed, BETA)
        status = "measured, target-workload identified" if selected["identification"] in plan_routes.IDENTIFIED else "measured, target-workload unmatched"
        entries[row["id"]] = {"status": status, "routeId": selected["route"]["id"], "costUsd": cost, "costScore": score_value, "value": value}
        values[row["id"]] = value
    ranks = competition_ranks(values)
    for row_id, rank in ranks.items():
        entries[row_id]["rank"] = rank
    official = {row_id: entry["plan"]["value"] for row_id, entry in per_row.items() if entry["plan"]["value"] is not None}
    specification = dict(MEASURED_VIEW_SPEC)
    specification["id"] = hashlib.sha256(json.dumps(specification, sort_keys=True).encode()).hexdigest()[:16]
    return {
        "specification": specification,
        "rows": entries,
        "rankChangeVsOfficial": diagnostics.paired_rank_change(official, values),
        "calibration": _measured_calibration(rows, frozen, entries),
    }


MEASURED_CALIBRATION_RULE = (
    "each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, "
    "c_H = dearest x 2 (diagnostic only; the official anchors are unchanged)"
)


def _plan_evidence(row: dict | None) -> str:
    """How a row's displayed Plan cost is supported: measured route, owner-named transfer or API-cost fallback."""

    if row is None:
        return "not in the current table"
    if row["plan"]["fallback"]:
        return "API-cost fallback"
    return {"controlled": "controlled measurement", "reports": "concordant reports"}.get(row["plan"]["grade"], "owner-named transfer")


def _reversals(baseline: dict, branch: dict) -> list[list[str]]:
    """Pairs ordered one way by ``baseline`` and the other way by ``branch`` (ties are not reversals)."""

    panel = sorted(row for row in set(baseline) & set(branch) if baseline[row] is not None and branch[row] is not None)
    return [
        [a, b]
        for index, a in enumerate(panel)
        for b in panel[index + 1:]
        if (baseline[a] - baseline[b]) * (branch[a] - branch[b]) < 0
    ]


def _measured_calibration(rows: list[dict], frozen: dict, entries: dict) -> dict:
    """E164: the measured-only rows rescored on anchors built from measured evidence alone.

    The official Plan anchors include owner-named transfers and API-cost fallbacks (E160), so an
    assumption can move measured-only ranks through the exchange rate even though no assumed route
    is in the view. Holding rows, routes, costs and quality fixed, this reports what calibration alone does.
    """

    by_id = {row["id"]: row for row in rows}
    measured = {row_id: entry for row_id, entry in entries.items() if "costUsd" in entry}
    workloads, official, calibrated = {}, {}, {}
    for workload, frozen_entry in frozen["workloads"].items():
        members = [row_id for row_id in measured if by_id[row_id]["cost"]["workload"] == workload]
        anchors_official = frozen_entry["anchors"]["plan"]
        provenance = None
        if anchors_official:
            references = anchors_official["referenceCosts"]
            low, high = min(references, key=references.get), max(references, key=references.get)
            provenance = {"low": {"row": low, "evidence": _plan_evidence(by_id.get(low))}, "high": {"row": high, "evidence": _plan_evidence(by_id.get(high))}}
        references = {row_id: measured[row_id]["costUsd"] for row_id in members if not by_id[row_id]["cost"]["partialComponents"]}
        entry = {"rows": sorted(members), "references": sorted(references), "officialAnchorProvenance": provenance}
        if len(references) < MIN_ANCHOR_REFERENCES:
            workloads[workload] = {**entry, "status": "measured-evidence calibration unavailable (fewer than two measured references)"}
            continue
        anchors = anchor_math.anchor_object(references, basis="plan", workload=workload)
        workloads[workload] = {
            **entry,
            "status": "evaluated",
            "anchors": anchors,
            "exchangeRate": anchor_math.exchange_rate(anchors, BETA),
            "officialExchangeRate": anchor_math.exchange_rate(anchors_official, BETA) if anchors_official else None,
        }
        for row_id in members:
            official[row_id] = measured[row_id]["value"]
            calibrated[row_id] = anchor_math.value_score(anchor_math.cost_score(measured[row_id]["costUsd"], anchors), by_id[row_id]["summary"].displayed, BETA)
    return {
        "rule": MEASURED_CALIBRATION_RULE,
        "status": "evaluated" if calibrated else "measured-evidence calibration unavailable",
        "workloads": workloads,
        "values": calibrated,
        "rankChange": diagnostics.paired_rank_change(official, calibrated),
        "reversals": _reversals(official, calibrated),
        "maxAbsValueChange": max(
            (abs(calibrated[row_id] - official[row_id]) for row_id in calibrated if calibrated[row_id] is not None and official[row_id] is not None), default=None
        ),
    }


def _complete_panel(rows: list[dict]) -> tuple[list[str], dict, dict]:
    """The declared common complete panel (rows with every leaf observed), its z values and nominal weights."""

    complete = [row for row in rows if len(row["evidence"]["observations"]) == len(q.LEAVES)]
    z = {leaf.key: [row["evidence"]["observations"][leaf.key].z for row in complete] for leaf in q.LEAVES}
    return sorted(row["id"] for row in complete), z, {leaf.key: leaf.weight for leaf in q.LEAVES}


def _group_drift(rows: list[dict]) -> dict:
    """E114 on the common complete panel."""

    panel, z, weights = _complete_panel(rows)
    return {**diagnostics.group_drift(z, weights, {leaf.key: leaf.group for leaf in q.LEAVES}), "panel": panel}


def _panel_dispersion(rows: list[dict]) -> dict:
    """E153/E81: the normalised weighted spread and the signed covariance allocation on the common complete panel."""

    panel, z, weights = _complete_panel(rows)
    return {"panel": panel, "weightedSpread": diagnostics.dispersion_shares(z, weights), "covarianceAllocation": diagnostics.covariance_allocation(z, weights)}


def _tb_same_harness(rows: list[dict], tb4_rows: list[dict]) -> dict:
    """E125: the restricted single-harness Terminal-Bench variant, its agreement with the primary leaf, harness-mixed rows."""

    same = [item for item in tb4_rows if item.get("agent") == DEFAULT_TB_HARNESS]
    primary, restricted, mixed = {}, {}, []
    for row in rows:
        source = row["evidence"]["provenance"].get("terminalBench")
        if source is not None:
            primary[row["id"]] = row["evidence"]["observations"]["terminalBench"].z
            if source.get("agent") != DEFAULT_TB_HARNESS:
                mixed.append(row["id"])
        selected = exact_match.select_tb4_row(row["id"], row.get("effort"), same)
        if selected is not None:
            restricted[row["id"]] = selected["resolutionRatePct"]
    return {
        "defaultHarness": DEFAULT_TB_HARNESS,
        "restricted": restricted,
        "harnessMixed": sorted(mixed),
        "agreement": diagnostics.agreement(primary, restricted, label="Terminal-Bench same-harness diagnostic"),
    }


def _anchor_stability(rows: list[dict], frozen: dict, main: str, per_row: dict) -> dict:
    """E126: the exchange-rate series across anchor versions and the trimmed-anchor rank-shift diagnostic (API basis)."""

    anchors = frozen["workloads"][main]["anchors"]["api"]
    trimmed = anchor_math.trimmed_anchor_object(anchors["referenceCosts"], basis="api", workload=main)
    primary, shifted = {}, {}
    for row in rows:
        if row["cost"]["workload"] == main and per_row[row["id"]]["api"]["value"] is not None:
            primary[row["id"]] = per_row[row["id"]]["api"]["value"]
            shifted[row["id"]] = anchor_math.value_score(anchor_math.cost_score(row["cost"]["costUsd"], trimmed), row["summary"].displayed, BETA)
    return {
        "exchangeRateSeries": [{"anchorVersion": frozen["anchorVersion"], **anchor_math.exchange_rate(anchors, BETA)}],
        "trimmedAnchors": trimmed,
        "trimmedRankShifts": diagnostics.paired_rank_change(primary, shifted),
    }


def _abstention_sensitivity(rows: list[dict], per_row: dict) -> dict:
    """E128: API ranks with the Omniscience leaf at z_pen = max(0, I) (total abstention scores 0); O28 is unchanged."""

    primary, penalised = {}, {}
    for row in rows:
        observations = dict(row["evidence"]["observations"])
        source = row["evidence"]["provenance"].get("omniscience")
        value = per_row[row["id"]]["api"]["value"]
        if value is None:
            continue
        if source is not None:
            observations["omniscience"] = q.Observation(source["abstentionPenalisedZ"])
        primary[row["id"]] = value
        penalised[row["id"]] = anchor_math.value_score(per_row[row["id"]]["api"]["costScore"], q.summarize(observations).displayed, BETA)
    return {"rule": "z_pen = max(0, I)", "rankChanges": diagnostics.paired_rank_change(primary, penalised)}


def _z_by_leaf(rows: list[dict]) -> dict:
    return {leaf.key: [row["evidence"]["observations"][leaf.key].z for row in rows if leaf.key in row["evidence"]["observations"]] for leaf in q.LEAVES}


def _quality_agreement(rows: list[dict]) -> dict:
    """E62 (a): Kendall tau-b between observed quality and the independent-only quality on the matched panel."""

    observed, independent = {}, {}
    for row in rows:
        values = row["evidence"]["observations"]
        if "bugHunt" in values and "terminalBench" in values:
            observed[row["id"]] = row["summary"].displayed
            independent[row["id"]] = (values["bugHunt"].z + values["terminalBench"].z) / 2.0
    return diagnostics.agreement(observed, independent, label="quality agreement (matched-panel sensitivity)")


# E166: what the selected measurement's API-priced amount M x F_gross measures, so a displayed amount never reads
# as capacity it does not establish. API-fallback rows publish no Plan amount.
AMOUNT_KINDS = {
    "transfer": "assumed API-equivalent consumption (owner-named transfer)",
    "identified": "identified target-workload capacity",
    "capacity": "measured-workload capacity",
    "observed": "observed eligible consumption (capacity not established)",
}


def plan_amount(selected: dict | None) -> dict | None:
    """E166: the selected measurement's amount M x F_gross with its kind, cash components and statuses."""

    if selected is None:
        return None
    route = selected["route"]
    if selected["grade"] == "assumption":
        kind = "transfer"
    elif selected["identification"] in plan_routes.IDENTIFIED:
        kind = "identified"
    elif selected.get("measurementCapacityStatus") == "capacity established on the measurement workload":
        kind = "capacity"
    else:
        kind = "observed"
    gross = plan_routes.gross_cash(route)
    period = route.get("feePeriod", "month")
    return {
        "amountKind": AMOUNT_KINDS[kind],
        "amountUsd": plan_routes.comparison_multiple(route) * gross if math.isfinite(gross) else None,
        "feePeriod": period,
        "subscriptionCashUsd": route.get("planPriceUsd"),
        "additionalCashUsd": float(route.get("additionalCashUsd") or 0.0),
        "grossCashUsd": gross if math.isfinite(gross) else None,
        "workload": "the scored workload W" if kind == "identified" else "the route's measurement workload",
        "capacityStatus": selected.get("measurementCapacityStatus"),
        "valuationStatus": selected.get("valuation"),
        "donorRouteId": selected.get("donorRouteId"),
        "interpretationLabel": f"{AMOUNT_KINDS[kind]}, API-priced USD per {period}",
    }


def _row_json(row: dict, scores: dict, ranks: dict) -> dict:
    selection = row["routeSelection"]
    selected = selection["selected"]
    caveat = row.get("aaNote") if row.get("aaNote") and any(word in row["aaNote"].lower() for word in ("pricing", "cost", "price")) else None
    return {
        "id": row["id"],
        "name": row["name"],
        "effort": row.get("effort"),
        "aaSlug": row["aaSlug"],
        "configurationMapped": row["configurationMapped"],
        # E141: AA's own note on what its cost omits (e.g. a long-context surcharge), shown as a cost caveat.
        "aaCostCaveat": caveat,
        "valuation": valuation_contract(caveat),
        "tariffStatus": "as published by AA (effective dates not recorded)",
        "demandRegistry": demand_registry(row["page"], row["cost"]["components"]),
        "quality": {
            **_summary_json(row["summary"]),
            "status": "scored" if row["summary"].displayed is not None else "quality not scoreable — no observed leaves",
            "leaves": {key: {**_observation_json(value), **row["evidence"]["provenance"][key]} for key, value in row["evidence"]["observations"].items()},
            "clipAudit": row["evidence"]["clipAudit"],
        },
        "cost": {
            **row["cost"],
            "componentsDetail": row["components"],
            "indexReconciliation": row["indexReconciliation"],
        },
        "plan": {
            **row["plan"],
            "selectionReason": selection["reason"],
            "dominatedRoutes": selection["dominated"],
            # Strict JSON: an unknown fee (infinite gross cash) is written as null.
            "comparisonTuples": {key: [item if math.isfinite(item) else None for item in value] for key, value in selection["tuples"].items()},
            "selectedIdentification": selected["identification"] if selected else None,
            "amount": plan_amount(selected),
            "admission": [
                {
                    "routeId": item["route"]["id"], "case": item["case"], "officialDisplayEligible": item["officialDisplayEligible"],
                    "planIntervalEligible": item["planIntervalEligible"],
                    # E144/E151: the evidence clock behind the classification.
                    "expiry": item.get("expiry"), "evidenceDate": item.get("evidenceDate"), "donorRouteId": item.get("donorRouteId"),
                    "contributingReportIds": item["route"].get("reportIds"), "excludedReportIds": item["route"].get("excludedReportIds"),
                }
                for item in row["admissionTable"]
            ],
        },
        "api": {**scores["api"], "rank": ranks["api"].get(row["id"])},
        "planScore": {**scores["plan"], "rank": ranks["plan"].get(row["id"])},
    }


# --------------------------------------------------------------------------
# 4. Scenario shares (released as a data file)
# --------------------------------------------------------------------------


# E155: uncertainty outside every v1 stream, printed beside the scenario outputs.
NOT_QUANTIFIED = (
    "benchmark repeatability beyond the conventional Terminal-Bench interval-range sensitivity in S1M (other published intervals, run-to-run ranges): not quantified in v1 scenario shares",
    "fitted-parameter uncertainty (e.g. Elo rating intervals): not quantified in v1 scenario shares",
)

# E147: the registered kernel-check object for v1 (multiples and price lists are fixed inputs, not drawn).
REGISTERED_DEPENDENCY = "every row its own dependency component: no shared varying primitive in v1 streams"


def _kernel(low: float, high: float, point: float) -> scenarios.Kernel:
    return scenarios.Kernel("uniform", (low, high), "endpoint-heavy") if high > low else scenarios.Kernel("fixed", (point,))


# E154: rounded published records linked by an accounting identity that is used as a sampling constraint form one
# compiled component, which needs a registered joint law. v1 uses no identity as a sampling constraint (AA's Index
# total and the Coding Agent Index published sum are validation identities), so every rounded record is a singleton.
SAMPLING_IDENTITIES: tuple = ()
JOINT_LAWS = {"singleton": "independent uniform within the reporting interval (arcsine alternative)"}


def rounding_components(records: list[str], identities: tuple = SAMPLING_IDENTITIES) -> list[list[str]]:
    """E154: connected components of rounded records under the sampling identities; only singletons have a registered law."""

    components = [{record} for record in records]
    for identity in identities:
        members = set(identity)
        linked = [component for component in components if component & members]
        if linked:
            components = [component for component in components if not component & members] + [set().union(*linked)]
    unregistered = sorted(sorted(component) for component in components if len(component) > 1)
    if unregistered:
        raise ValueError(f"no registered joint rounding law (E154) for the rounded-record components {unregistered}")
    return sorted(sorted(component) for component in components)


def _cost_kernel(row: dict, cost: float) -> scenarios.Kernel:
    """E154: the basis cost derived from its components' draws, never one uniform on the summed interval.

    Each rounded component record is a primitive with its own uniform kernel (arcsine
    alternative); exact components are a fixed offset; a single rounded component is
    a plain uniform. Plan costs scale every term by the row's API-to-Plan ratio.
    """

    ratio = cost / row["cost"]["costUsd"]
    detail = row["components"]
    rounding_components([key for key in row["cost"]["components"] if detail[key]["halfWidthUsd"] > 0])
    rounded = [detail[key] for key in row["cost"]["components"] if detail[key]["halfWidthUsd"] > 0]
    if len(rounded) <= 1:
        return _kernel(row["cost"]["lowUsd"] * ratio, row["cost"]["highUsd"] * ratio, cost)
    exact = sum(detail[key]["costUsd"] for key in row["cost"]["components"] if detail[key]["halfWidthUsd"] <= 0)
    terms = tuple(((item["costUsd"] - item["halfWidthUsd"]) * ratio, (item["costUsd"] + item["halfWidthUsd"]) * ratio) for item in rounded)
    return scenarios.Kernel("uniform-sum", (exact * ratio, *terms), "endpoint-heavy")


# E167: the core scenario branches run with owner-named transfers off. On the Plan basis a row whose selected route is
# a transfer is unevaluable there (selected-evidence removal: never reselected, never replaced by API cost; the
# measured-only view answers reselection). S0 describes the displayed record, transfers included.
TRANSFER_EXCLUSION = "owner-named transfer: unevaluable with transfers off (never reselected or replaced by API cost)"


def transfers_on(stratum: str) -> bool:
    """E167: only S0, the displayed record's reporting precision, keeps owner-named transfers."""

    return stratum == "S0"


def transfer_dependent(row: dict) -> bool:
    """A row whose selected Plan route is an owner-named transfer (API-fallback rows carry no grade)."""

    return row["plan"].get("grade") == "assumption"


def scenario_panel(assembled: dict, basis: str, *, measurement: bool = False, transfers: bool = True) -> list[scenarios.RowInputs]:
    """The declared panel for one basis (E96): rows with a cost on the main workload, in a fixed order.

    With ``measurement`` (the E162 stream), a leaf whose source documents a 95%
    confidence interval (Terminal-Bench's published half-width) is drawn inside that
    interval under a conventional kernel (E165): uniform with the arcsine
    alternative, never assumed normal, clipped to the leaf's domain.
    """

    panel = []
    for row in assembled["rows"]:
        cost = _basis_cost(row, basis)
        if row["cost"]["workload"] != assembled["mainWorkload"] or not anchor_math.scoreable(cost):
            continue
        if basis == "plan" and not transfers and transfer_dependent(row):
            continue
        observations = row["evidence"]["observations"]
        leaves = {key: _kernel(value.low, value.high, value.z) for key, value in observations.items()}
        half = (row["evidence"]["provenance"].get("terminalBench") or {}).get("ci95HalfWidthPct")
        if measurement and half:
            z = observations["terminalBench"].z
            leaves["terminalBench"] = scenarios.Kernel("uniform", (max(0.0, z - half), min(100.0, z + half)), "endpoint-heavy", scenarios.INTERVAL_RANGE)
        panel.append(scenarios.RowInputs(row["id"], leaves, _cost_kernel(row, cost), row["summary"].provisional))
    return panel


def scenario_hash(assembled: dict, frozen: dict, *, n: int, seed: int) -> str:
    """Identity of every scenario input: panels, kernels, anchors, beta, scenario count and seed."""

    payload = {
        "beta": BETA,
        "n": n,
        "seed": seed,
        "anchors": {basis: frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis] for basis in BASES},
        "panels": {
            f"{basis}{'-measurement' if measurement else ''}{'' if transfers else '-transfers-off'}": [
                {
                    "row": item.row, "provisional": item.provisional, "cost": [item.cost.family, list(item.cost.params)],
                    "leaves": {key: [kernel.family, list(kernel.params), kernel.target] for key, kernel in sorted(item.leaves.items())},
                }
                for item in scenario_panel(assembled, basis, measurement=measurement, transfers=transfers)
            ]
            for basis in BASES
            for measurement in (False, True)
            for transfers in (True, False)
        },
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def run_scenarios(assembled: dict, frozen: dict, *, n: int = SCENARIO_COUNT, seed: int) -> dict:
    """Per-basis, per-stratum scenario shares with the published seed and the input hash."""

    results = {}
    excluded = sorted(
        row["id"] for row in assembled["rows"]
        if row["cost"]["workload"] == assembled["mainWorkload"] and anchor_math.scoreable(_basis_cost(row, "plan")) and transfer_dependent(row)
    )
    for basis in BASES:
        anchors = frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis]
        results[basis] = []
        for index, (stratum, alternative) in enumerate(SCENARIO_RUNS):
            panel = scenario_panel(assembled, basis, measurement=stratum == MEASUREMENT_STREAM, transfers=transfers_on(stratum))
            run = scenarios.shares(panel, stratum, n, seed + index, anchors, BETA, alternative=alternative)
            if basis == "plan":
                run["transfers"] = "on (the displayed record)" if transfers_on(stratum) else "off"
                run["excluded"] = [] if transfers_on(stratum) else [{"row": row_id, "reason": TRANSFER_EXCLUSION} for row_id in excluded]
            results[basis].append(run)
    return {
        "schemaVersion": 1,
        "inputHash": scenario_hash(assembled, frozen, n=n, seed=seed),
        "seed": seed,
        "scenarios": n,
        # E155: uncertainty descriptions come from the stream manifests, including what v1 does not quantify.
        "streamDescriptions": dict(scenarios.TARGET_PROFILES),
        "notQuantified": list(NOT_QUANTIFIED),
        "intervalInterpretation": {MEASUREMENT_STREAM: [scenarios.interval_interpretation(TB_INTERVAL_CONTRACT)]},
        "jointRoundingLaw": {"samplingIdentities": list(SAMPLING_IDENTITIES), "registeredLaws": JOINT_LAWS, "components": "every rounded record is a singleton"},
        "results": results,
        "barLabels": bar_labels(assembled, frozen, seed=seed, batch=n),
    }


def bar_labels(assembled: dict, frozen: dict, *, seed: int, batch: int) -> list[dict]:
    """E100/E112: kernel-robust scenario-supported cheapest labels for each pinned bar on the API basis."""

    panel = scenario_panel(assembled, "api")
    members = {item.row for item in panel}
    boxes = api_boxes(assembled)
    by_id = {row["id"]: row for row in assembled["rows"]}
    # E147: the compiled dependency graph must be the registered kernel-check object, or the build fails.
    if any(len(component) > 1 for component in scenarios.dependency_components(panel)):
        raise ValueError(f"compiled dependency graph differs from the registered kernel-check object ({REGISTERED_DEPENDENCY})")
    labels = []
    for reference in frozen["barReferences"]:
        if reference["id"] not in members:
            labels.append({"reference": reference["id"], "status": "unevaluable", "reason": "reference outside the declared scenario panel"})
            continue
        summary = by_id[reference["id"]]["summary"]
        candidates = intervals.cheapest_above_bar(boxes, intervals.Reference(reference["id"], summary.lower, summary.upper))["possibleCheapest"]
        results = {candidate: scenarios.kernel_robust_cheapest(panel, candidate, reference["id"], seed, batch=batch) for candidate in candidates if candidate in members}
        labels.append({"reference": reference["id"], "status": "evaluated", "candidates": results})
    return labels


def attach_scenarios(scored: dict, document: dict | None, expected_hash: str) -> dict:
    """Scenario shares join the scores only when computed from exactly these inputs; otherwise a held release."""

    if document is None or document.get("inputHash") != expected_hash:
        status = "missing" if document is None else "stale (inputs changed since the scenario run)"
        scored["scenarios"] = {"status": status}
        scored["gates"]["hold"] = True
        scored["manifest"].append(_rule("scenario outputs current (E72)", "fired", f"scenario outputs {status}; release held"))
        return scored
    scored["scenarios"] = {"status": "current", **document}
    scored["manifest"].append(_rule("scenario outputs current (E72)", "passed", "scenario input hash matches the scored inputs"))
    return scored


# --------------------------------------------------------------------------
# 5. Loading and the command line
# --------------------------------------------------------------------------


# E159: every captured artifact the v3 build reads, with the code or procedure that produced it. The build never
# consults live pages, so the committed artifacts are the release's evidence bundle.
EVIDENCE_FILES = {
    "snapshot": ("aa/aa_v432_snapshot.json", "valuerank.capture_aa"),
    "deepswe": ("aa_deepswe.json", "valuerank.fetch_deepswe"),
    "bugHunt": ("bug_hunt.json", "editorial capture of the owner's published results (source commit recorded)"),
    "tb4": ("tb4.json", "scripts/scrape-tb4.js, then valuerank.build_tb4"),
    "codingAgents": ("aa/coding_agents_capture.json", "valuerank.capture_coding_agents"),
    "costCharts": ("aa/cost_charts_capture.json", "scripts/capture-aa-cost-charts.js"),
    "configurationMap": ("v3_configuration_map.json", "editorial pinning from the research capture"),
    "planRoutes": ("plan_cost_routes.json", "editorial Plan evidence registry"),
}
CAPTURE_FIELDS = ("capturedAt", "observedAt", "snapshotDate", "asOf", "frozenAt")


def load_documents(data: Path) -> dict:
    return {key: json.loads((data / relative).read_text()) for key, (relative, _extractor) in EVIDENCE_FILES.items()}


def evidence_bundle(data: Path) -> dict:
    """E159: content hashes, capture times and extractors of the release's input artifacts (plus the anchor object)."""

    artifacts = []
    for key, (relative, extractor) in [*EVIDENCE_FILES.items(), ("anchors", (FROZEN_FILE, "valuerank.value_v3 freeze"))]:
        content = (data / relative).read_bytes()
        document = json.loads(content)
        captured = next((document[field] for field in CAPTURE_FIELDS if isinstance(document.get(field), str)), None)
        artifacts.append({"key": key, "artifact": f"data/{relative}", "sha256": hashlib.sha256(content).hexdigest(), "capturedAt": captured, "extractor": extractor})
    return {
        "artifacts": artifacts,
        "bundleHash": hashlib.sha256("".join(item["sha256"] for item in artifacts).encode()).hexdigest(),
        "rebuild": "every published output is rebuilt from these artifacts at the pinned publication clock (npm run verify:docs), never from live pages",
    }


def configurations_from_scores(scores: dict) -> list[dict]:
    """The ranked cohort (fixed cohort policy: the ranking-eligible rows, in table order) with each AA identity."""

    return [
        {"id": row["id"], "name": row["name"], "effort": row.get("aaVariant"), "aaSlug": row["aaSlug"], "aaNote": row.get("aaFrontierFootnote")}
        for row in scores["models"]
        if row.get("rankingEligible") is True
    ]


def scenario_seed(release_day: date) -> int:
    return int(release_day.strftime("%Y%m%d"))


def build(configurations: list[dict], data: Path, *, release_day: date) -> dict:
    """The v3 section of scores.json for this release."""

    assembled = assemble(configurations, load_documents(data), release_day=release_day)
    frozen = json.loads((data / FROZEN_FILE).read_text())
    scored = score(assembled, frozen)
    scored["evidenceBundle"] = evidence_bundle(data)
    scenario_path = data / SCENARIO_FILE
    document = json.loads(scenario_path.read_text()) if scenario_path.exists() else None
    seed = document["seed"] if document else scenario_seed(release_day)
    count = document["scenarios"] if document else SCENARIO_COUNT
    return attach_scenarios(scored, document, scenario_hash(assembled, frozen, n=count, seed=seed))


def main(argv: list[str] | None = None, *, data: Path = DATA) -> int:
    parser = argparse.ArgumentParser(description="ValueRank v3: freeze anchors or run the scenario engine")
    parser.add_argument("command", choices=("freeze", "scenarios"))
    parser.add_argument("--scenarios", type=int, default=SCENARIO_COUNT)
    args = parser.parse_args(argv)
    scores = json.loads((data / "scores.json").read_text())
    release_day = utcnow().date()
    assembled = assemble(configurations_from_scores(scores), load_documents(data), release_day=release_day)
    if args.command == "freeze":
        document = freeze(assembled, frozen_at=release_day.isoformat())
        target = data / FROZEN_FILE
    else:
        frozen = json.loads((data / FROZEN_FILE).read_text())
        document = run_scenarios(assembled, frozen, n=args.scenarios, seed=scenario_seed(release_day))
        target = data / SCENARIO_FILE
    target.write_text(json.dumps(document, indent=2, ensure_ascii=False, default=_json_default) + "\n")
    print(json.dumps({"wrote": str(target.relative_to(data.parent)), "command": args.command}))
    return 0


def _json_default(value):
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


if __name__ == "__main__":
    sys.exit(main())
