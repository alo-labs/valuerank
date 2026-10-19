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
SCENARIO_RUNS = (("S0", False), ("S1", False), ("S2", False), ("S1", True))
FROZEN_FILE = "v3_frozen.json"
SCENARIO_FILE = "v3_scenarios.json"


# --------------------------------------------------------------------------
# 1. Evidence
# --------------------------------------------------------------------------


def leaf_evidence(model_id: str, effort: str | None, page: dict, deepswe: dict | None, tb4_rows: list[dict], bug_hunt: dict | None) -> dict:
    """Exact-configuration observations for the twelve leaves, with provenance and the clipping audit (E110)."""

    observations, provenance, audit = {}, {}, []

    def add(key: str, raw, observation: q.Observation, source: dict) -> None:
        check = q.clip_audit(key, raw)
        if not check["domainValid"]:
            raise ValueError(f"{model_id}: {key} value {raw!r} is outside its documented domain")
        observations[key] = observation
        provenance[key] = source
        audit.append(check)

    if deepswe is not None and exact_match.efforts_match(model_id, effort, deepswe.get("effort")):
        precision = deepswe.get("scorePrecision")
        half = precision / 2.0 if isinstance(precision, (int, float)) else 0.0
        add("deepswe", deepswe["scorePct"], q.percent_z(deepswe["scorePct"], half),
            {"source": "AA Coding Agent Index, DeepSWE v1.1", "configuration": deepswe.get("displayLabel"), "agent": deepswe.get("agent")})
    if exact_match.bug_hunt_matches(model_id, effort, bug_hunt):
        add("bugHunt", bug_hunt["fixedOf105"], q.bug_hunt_z(bug_hunt["fixedOf105"], BUG_HUNT_HALF_WIDTH),
            {"source": "Bug Hunt Bench owner-published runs", "configuration": bug_hunt.get("evaluatedModel"), "harness": bug_hunt.get("harness"), "runs": bug_hunt.get("sampleN")})
    tb4 = exact_match.select_tb4_row(model_id, effort, tb4_rows)
    if tb4 is not None:
        add("terminalBench", tb4["resolutionRatePct"], q.percent_z(tb4["resolutionRatePct"], TB4_HALF_WIDTH_PCT),
            {"source": "tbench.ai Terminal-Bench 4.0 leaderboard", "configuration": tb4["model"], "agent": tb4.get("agent")})
    if page.get("gdpval") is not None:
        add("gdpval", page["gdpval"], q.gdpval_z(page["gdpval"]), {"source": "AA GDPval-AA v2.1 Elo as integrated in the pinned Index (E90)"})
    for key, field in FRACTION_LEAVES.items():
        if page.get(field) is not None:
            add(key, page[field], q.fraction_z(page[field]), {"source": f"AA field {field}"})
    if page.get("omniscience") is not None:
        accuracy, hallucination = page.get("omniscienceAccuracy"), page.get("omniscienceHallucinationRate")
        rebuilt = q.omniscience_index_from_rates(accuracy, hallucination) if accuracy is not None and hallucination is not None else None
        unanswered = (1.0 - accuracy) * (1.0 - hallucination) if rebuilt is not None else None
        add("omniscience", page["omniscience"], q.omniscience_index_z(page["omniscience"]),
            {"source": "AA Omniscience Index (O28)", "accuracy": accuracy, "hallucinationRate": hallucination, "indexFromRates": rebuilt,
             "unansweredOrPartialShare": unanswered, "abstentionPenalisedZ": max(0.0, page["omniscience"])})
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
        "identities": "p . d_ie = C_ie for each component; the Index totals bound the sum over all ten Index executions only",
        "missingForIdentification": ["category-specific burn coefficients for each plan meter", "or a controlled measurement on a workload compatible with W"],
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
        if bounds is None or not anchor_math.scoreable(bounds[1]):
            continue
        summary = row["summary"]
        boxes.append(intervals.Box(row["id"], cost["lowUsd"] / bounds[1], cost["highUsd"] / bounds[0], summary.lower, summary.upper, summary.provisional))
    return boxes


def freeze(assembled: dict, *, frozen_at: str) -> dict:
    """Anchor objects per workload and basis from the evidenced reference configurations, and the bar reference."""

    workloads = {}
    for workload, entry in workload_catalog(assembled).items():
        components = entry["components"]
        api = {row["id"]: restricted_cost(row["components"], components) for row in assembled["rows"]}
        plan = {row["id"]: _plan_cost_on(row, components) for row in assembled["rows"]}
        workloads[workload] = {
            **entry,
            "anchors": {
                "api": anchor_math.anchor_object(api, basis="api", workload=workload),
                "plan": anchor_math.anchor_object(plan, basis="plan", workload=workload),
            },
        }
    frontier = intervals.frontier(api_boxes(assembled))
    by_id = {row["id"]: row for row in assembled["rows"]}
    definite = sorted((row_id for row_id, result in frontier.items() if result["definite"] == intervals.CERTIFIED), key=lambda row_id: (by_id[row_id]["summary"].displayed, row_id))
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
            if costs:
                clip.append({"workload": workload, **anchor_math.clip_gate(costs, frozen["workloads"][workload]["anchors"][basis])})
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
        "mainWorkload": main,
        "admission": {key: value for key, value in assembled["admission"].items() if key != "matrices"},
        "admissionMatrices": assembled["admission"]["matrices"],
        "workloads": {workload: {"components": entry["components"], "role": entry["role"], "anchors": entry["anchors"]} for workload, entry in frozen["workloads"].items()},
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
        score_value = anchor_math.cost_score(cost, _anchors_for(frozen, row["cost"]["workload"], "plan"))
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
    return {"specification": specification, "rows": entries, "rankChangeVsOfficial": diagnostics.paired_rank_change(official, values)}


def _group_drift(rows: list[dict]) -> dict:
    """E114 on the common complete panel: rows with every leaf observed."""

    complete = [row for row in rows if len(row["evidence"]["observations"]) == len(q.LEAVES)]
    z = {leaf.key: [row["evidence"]["observations"][leaf.key].z for row in complete] for leaf in q.LEAVES}
    result = diagnostics.group_drift(z, {leaf.key: leaf.weight for leaf in q.LEAVES}, {leaf.key: leaf.group for leaf in q.LEAVES})
    return {**result, "panel": sorted(row["id"] for row in complete)}


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


def _row_json(row: dict, scores: dict, ranks: dict) -> dict:
    selection = row["routeSelection"]
    selected = selection["selected"]
    return {
        "id": row["id"],
        "name": row["name"],
        "effort": row.get("effort"),
        "aaSlug": row["aaSlug"],
        "configurationMapped": row["configurationMapped"],
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
            "comparisonTuples": {key: list(value) for key, value in selection["tuples"].items()},
            "selectedIdentification": selected["identification"] if selected else None,
            "admission": [{"routeId": item["route"]["id"], "case": item["case"], "officialDisplayEligible": item["officialDisplayEligible"], "planIntervalEligible": item["planIntervalEligible"]} for item in row["admissionTable"]],
        },
        "api": {**scores["api"], "rank": ranks["api"].get(row["id"])},
        "planScore": {**scores["plan"], "rank": ranks["plan"].get(row["id"])},
    }


# --------------------------------------------------------------------------
# 4. Scenario shares (released as a data file)
# --------------------------------------------------------------------------


def _kernel(low: float, high: float, point: float) -> scenarios.Kernel:
    return scenarios.Kernel("uniform", (low, high), "endpoint-heavy") if high > low else scenarios.Kernel("fixed", (point,))


def scenario_panel(assembled: dict, basis: str) -> list[scenarios.RowInputs]:
    """The declared panel for one basis (E96): rows with a cost on the main workload, in a fixed order."""

    panel = []
    for row in assembled["rows"]:
        cost = _basis_cost(row, basis)
        if row["cost"]["workload"] != assembled["mainWorkload"] or not anchor_math.scoreable(cost):
            continue
        ratio = cost / row["cost"]["costUsd"]
        leaves = {key: _kernel(value.low, value.high, value.z) for key, value in row["evidence"]["observations"].items()}
        panel.append(scenarios.RowInputs(row["id"], leaves, _kernel(row["cost"]["lowUsd"] * ratio, row["cost"]["highUsd"] * ratio, cost), row["summary"].provisional))
    return panel


def scenario_hash(assembled: dict, frozen: dict, *, n: int, seed: int) -> str:
    """Identity of every scenario input: panels, kernels, anchors, beta, scenario count and seed."""

    payload = {
        "beta": BETA,
        "n": n,
        "seed": seed,
        "anchors": {basis: frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis] for basis in BASES},
        "panels": {
            basis: [
                {"row": item.row, "provisional": item.provisional, "cost": [item.cost.family, list(item.cost.params)], "leaves": {key: [kernel.family, list(kernel.params)] for key, kernel in sorted(item.leaves.items())}}
                for item in scenario_panel(assembled, basis)
            ]
            for basis in BASES
        },
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def run_scenarios(assembled: dict, frozen: dict, *, n: int = SCENARIO_COUNT, seed: int) -> dict:
    """Per-basis, per-stratum scenario shares with the published seed and the input hash."""

    results = {}
    for basis in BASES:
        panel = scenario_panel(assembled, basis)
        anchors = frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis]
        results[basis] = [
            scenarios.shares(panel, stratum, n, seed + index, anchors, BETA, alternative=alternative)
            for index, (stratum, alternative) in enumerate(SCENARIO_RUNS)
        ]
    return {
        "schemaVersion": 1,
        "inputHash": scenario_hash(assembled, frozen, n=n, seed=seed),
        "seed": seed,
        "scenarios": n,
        "results": results,
        "barLabels": bar_labels(assembled, frozen, seed=seed, batch=n),
    }


def bar_labels(assembled: dict, frozen: dict, *, seed: int, batch: int) -> list[dict]:
    """E100/E112: kernel-robust scenario-supported cheapest labels for each pinned bar on the API basis."""

    panel = scenario_panel(assembled, "api")
    members = {item.row for item in panel}
    boxes = api_boxes(assembled)
    by_id = {row["id"]: row for row in assembled["rows"]}
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


def load_documents(data: Path) -> dict:
    def read(relative: str) -> dict:
        return json.loads((data / relative).read_text())

    return {
        "snapshot": read("aa/aa_v432_snapshot.json"),
        "deepswe": read("aa_deepswe.json"),
        "bugHunt": read("bug_hunt.json"),
        "tb4": read("tb4.json"),
        "codingAgents": read("aa/coding_agents_capture.json"),
        "costCharts": read("aa/cost_charts_capture.json"),
        "configurationMap": read("v3_configuration_map.json"),
        "planRoutes": read("plan_cost_routes.json"),
    }


def configurations_from_scores(scores: dict) -> list[dict]:
    """The ranked cohort (fixed cohort policy: the ranking-eligible rows, in table order) with each AA identity."""

    return [
        {"id": row["id"], "name": row["name"], "effort": row.get("aaVariant"), "aaSlug": row["aaSlug"]}
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
