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
import dataclasses
import hashlib
import json
import math
import statistics
import sys
from datetime import date, datetime
from pathlib import Path

from valuerank import anchors as anchor_math
from valuerank import basket
from valuerank import cost_diagnostics
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
DEFAULT_TB_HARNESS = "mini-SWE-agent"  # E125/O37: AA's Terminal-Bench harness; a leaf on any other agent is a gap fill
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


# O36: a leaf the primary source lacks is taken, in this order, from another independent party that ran the same
# benchmark version on the exact configuration, else from the model provider's own published result (a provider claim).
SUPPLEMENT_ORDER = ("aa_recapture", "independent", "model_provider_claim")
LEAF_LABELS = {leaf.key: leaf.label for leaf in q.LEAVES}
SUPPLEMENT_UNITS = {"percent": lambda value: q.percent_z(value), "fraction": lambda value: q.fraction_z(value),
                    "fixedOf105": lambda value: q.bug_hunt_z(value, BUG_HUNT_HALF_WIDTH)}
LEAF_SEARCH_MAX_AGE_DAYS = 7


def leaf_supplements(documents: dict) -> dict:
    """O36: the eligible supplementary observations per (model, leaf), best source first; Terminal-Bench provider claims
    recorded in the tbench.ai capture count as provider claims."""

    entries = list((documents.get("leafEvidence") or {}).get("supplements", []))
    entries += [{"modelId": claim["cohortModelId"], "leaf": "terminalBench", "value": claim["valuePct"], "unit": "percent", "sourceType": "model_provider_claim",
                 "configuration": claim.get("evaluatedModel"), "url": claim.get("sourceUrl"), "publishedOn": claim.get("publishedOn"), "publisher": claim.get("publisher"),
                 "artifact": "tb4", "locator": f"providerClaims[claimId={claim.get('claimId')}].valuePct"}
                for claim in documents["tb4"].get("providerClaims", []) if claim.get("eligibleForRanking") is True]
    chosen = {}
    for entry in sorted(entries, key=lambda item: SUPPLEMENT_ORDER.index(item["sourceType"])):
        chosen.setdefault((entry["modelId"], entry["leaf"]), entry)
    return chosen


def leaf_evidence(model_id: str, effort: str | None, page: dict, deepswe: dict | None, tb4_rows: list[dict], bug_hunt: dict | None,
                  supplements: dict | None = None) -> dict:
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
    # O37: AA's own Terminal-Bench 4.0 run (one harness, every configuration) is the leaf; tbench.ai fills a gap.
    if page.get("terminalBench40") is not None:
        add("terminalBench", 100.0 * page["terminalBench40"], q.percent_z(100.0 * page["terminalBench40"]),
            {"source": "AA Terminal-Bench 4.0 run (Intelligence Index, mini-SWE-agent harness)", "agent": "mini-SWE-agent"},
            "snapshot", f"{page_path}.terminalBench40")
    tb4 = None if "terminalBench" in observations else exact_match.select_tb4_row(model_id, effort, tb4_rows)
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
        # E128: with every question correct the conditional hallucination rate is undefined and nothing is unanswered.
        unanswered = 0.0 if accuracy == 1.0 else (1.0 - accuracy) * (1.0 - hallucination) if rebuilt is not None else None
        add("omniscience", page["omniscience"], q.omniscience_index_z(page["omniscience"]),
            {"source": "AA Omniscience Index (O28)", "accuracy": accuracy, "hallucinationRate": hallucination, "indexFromRates": rebuilt,
             "unansweredOrPartialShare": unanswered, "abstentionPenalisedZ": max(0.0, page["omniscience"])},
            "snapshot", f"{page_path}.omniscience")
    for leaf in q.LEAVES:
        entry = (supplements or {}).get((model_id, leaf.key))
        if leaf.key not in observations and entry is not None:
            add(leaf.key, entry["value"], SUPPLEMENT_UNITS[entry["unit"]](entry["value"]),
                {"source": entry.get("publisher") or entry["sourceType"], "sourceType": entry["sourceType"], "configuration": entry.get("configuration"),
                 "url": entry.get("url"), "publishedOn": entry.get("publishedOn")},
                entry.get("artifact", "leafEvidence"), entry.get("locator", f"supplements[modelId={model_id}, leaf={leaf.key}].value"))
    return {"observations": observations, "provenance": provenance, "clipAudit": audit}


def incomplete_entry(configuration: dict, evidence: dict) -> dict | None:
    """O36: a configuration's missing leaves, or None when it has the full benchmark set."""

    missing = [leaf.key for leaf in q.LEAVES if leaf.key not in evidence["observations"]]
    return {"id": configuration["id"], "name": configuration["name"], "effort": configuration.get("effort"), "missing": missing} if missing else None


def incomplete_configurations(configurations: list[dict], documents: dict) -> list[dict]:
    """O36: the configurations the ranking must list but not rank, each with the leaves it lacks after every source."""

    pages = {page["model"]["slug"]: page["model"] for page in documents["snapshot"]["pages"]}
    deepswe_by_id = {item["valueRankModelId"]: item for item in documents["deepswe"]["configurations"] if item.get("valueRankModelId")}
    bug_hunt_by_id = {item["modelId"]: item for item in documents["bugHunt"]["models"]}
    supplements = leaf_supplements(documents)
    entries = [incomplete_entry(configuration, leaf_evidence(configuration["id"], configuration.get("effort"), pages[configuration["aaSlug"]],
                                                             deepswe_by_id.get(configuration["id"]), documents["tb4"]["rows"],
                                                             bug_hunt_by_id.get(configuration["id"]), supplements))
               for configuration in configurations]
    return [entry for entry in entries if entry is not None]


def check_leaf_searches(incomplete: list[dict], documents: dict, release_day: date) -> None:
    """O36: every leaf a cohort configuration lacks has a logged exhaustive search at most 7 days before the cutoff."""

    log = {(item["modelId"], item["leaf"]): item for item in (documents.get("leafEvidence") or {}).get("searches", [])}
    for row in incomplete:
        for leaf in row["missing"]:
            entry = log.get((row["id"], leaf))
            if entry is None or (release_day - date.fromisoformat(entry["searchedOn"])).days > LEAF_SEARCH_MAX_AGE_DAYS:
                raise ValueError(f"{row['id']}: no exhaustive search for {leaf} logged within {LEAF_SEARCH_MAX_AGE_DAYS} days of the cutoff (O36)")


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


# E176: AA's documented metering and cache rules (methodology page, 2026-10-20).
TOKEN_METERING_UNPUBLISHED = "not published per configuration (AA: provider-reported token counts where available, a canonical-tokenizer fallback otherwise)"
CACHE_RATE_PROVENANCE = "AA's live measurement of the model's typical cache-hit rate, not the run's one-off rate (measurement window not published)"
METERING_BASES = ("provider-reported", "canonical-tokenizer fallback", "not published per configuration")
# E174/E175: source facts the registry pins (each source's own displayed dates and documented interval levels).
SOURCE_INTERVALS = [
    {"leaf": "terminalBench", "status": "captured", "level": "95% (tbench.ai: \"The whiskers span the 95% confidence interval\")", "stream": "S1M"},
    {
        "leaf": "gdpval", "status": "published, not captured",
        "method": "Crowd-BT maximum likelihood with sandwich-estimator confidence intervals (AA methodology, GDPval-AA v2.1)",
        "level": "not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase)",
        "stream": "none until captured with a documented level; otherwise published beside the leaf outside every stream",
        "captureTask": "capture the GDPval-AA leaderboard CI column for the exact configurations",
    },
]
SOURCE_DATES = {"LiveBench 2.0": {"release": "2026-10-14", "lastUpdated": "2026-10-18", "observedOn": "2026-10-20", "role": "retired quality source (O26)"}}


def valuation_contract(caveat: str | None) -> dict:
    """E157: AA's valuation is linear in token categories, so category totals suffice to reconcile it; a provider tariff
    banded by request (e.g. context length) needs band-allocated demand or a request ledger, which no source publishes."""

    return {
        "costSourceRule": "AA: provider-reported token counts priced per token category at AA's recorded prices, cache pricing included",
        "valuationSufficiency": "category totals sufficient for AA's published valuation",
        "providerBillingRule": "banded tariff not reflected in AA's cost (AA cost caveat)" if caveat else "not recorded",
        "tariffCorrectedValuation": "unidentified: billing-band allocation unavailable" if caveat else "not assessed: provider billing rule not recorded",
        "tariffAllocationSupport": "unavailable",
        # E176: how AA metered the tokens and valued cached input (AA does not say per configuration which basis applies).
        "tokenMeteringBasis": TOKEN_METERING_UNPUBLISHED,
        "cacheRateProvenance": CACHE_RATE_PROVENANCE,
    }


# E170: the valuation-basis gate. AA's Index cost reconciles exactly with the prices AA displays for the configuration
# at capture (cache writes at the input rate where AA lists no cache-write price; exact to 1e-15 for every ranked row of
# the 2026-10-17 snapshot), which identifies the prices AA applied. Price records registered beyond AA's displayed
# prices (E141) name superseded or promotional tariffs; when AA's cost reconciles with one of them instead, the join
# decides between exact revaluation and owner decision O29.
VALUATION_TOLERANCE = 1e-9
INPUT_CATEGORIES = {"input": "nonCacheInput", "cacheRead": "cacheRead", "cacheWrite": "cacheWrite"}
GATE_COMPATIBLE = "compatible as captured"
GATE_REVALUED = "compatible after evidenced revaluation"
GATE_NOT_IN_FORCE = "AA's applied price not in force at V (O29)"
GATE_UNVERIFIED = "valuation basis unverified"
GATE_SCORED = (GATE_COMPATIBLE, GATE_REVALUED)
BOUND_UNAVAILABLE = "unavailable: a category priced at zero when AA valued the cost is priced at V (E185)"
NOT_IN_FORCE_FLAGS = {"superseded": "AA cost at superseded price", "promotional": "AA cost at standard price during a promotion"}


def displayed_prices(page: dict) -> dict | None:
    """AA's displayed per-category prices (USD per 1M tokens); cache writes at the input rate where none is listed."""

    prices = {"input": page.get("price1mInputTokens"), "cacheRead": page.get("cacheHitPrice"), "output": page.get("price1mOutputTokens")}
    prices["cacheWrite"] = page.get("cacheWritePrice") if page.get("cacheWritePrice") is not None else prices["input"]
    # A cache category may be free (E185); uncached input and output must carry a price.
    valid = all(isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value >= 0 for value in prices.values())
    return prices if valid and prices["input"] > 0 and prices["output"] > 0 else None


def reconciles(page: dict, prices: dict) -> bool | None:
    """p . d = C on AA's Index categories, or None when the category costs or token totals are not published.

    The output cost over the output price gives the output tokens; the input categories' costs over their prices
    give implied tokens that must sum to the input total.
    """

    cost, tokens = page.get("intelligenceIndexCost") or {}, page.get("canonicalIntelligenceIndexTokenCount") or {}
    if any(cost.get(field) is None for field in (*INPUT_CATEGORIES.values(), "output")) or not tokens.get("input") or not tokens.get("output"):
        return None
    if prices["output"] <= 0:
        return False  # a priced output cost cannot come from a free output tariff
    if any(prices[key] == 0 and cost[field] > 0 for key, field in INPUT_CATEGORIES.items()):
        return False
    output = cost["output"] / prices["output"] * 1e6
    inputs = sum(cost[field] / prices[key] for key, field in INPUT_CATEGORIES.items() if prices[key] > 0) * 1e6
    # E185: a free input category hides its tokens, so the priced ones may only fall short of the input total.
    free = any(prices[key] == 0 for key in INPUT_CATEGORIES)
    input_ok = inputs <= tokens["input"] * (1 + VALUATION_TOLERANCE) if free else abs(inputs - tokens["input"]) <= VALUATION_TOLERANCE * tokens["input"]
    return abs(output - tokens["output"]) <= VALUATION_TOLERANCE * tokens["output"] and input_ok


def valuation_gate(page: dict, records: list[dict], captured_at: str | None) -> dict:
    """E170: the one outcome of joining the prices AA applied with the price records in force at the release cutoff V.

    v1's records in force at V are AA's displayed prices at capture. A component without published category costs
    (the Coding Agent Index, the chart components) is valued by AA at the configuration's listed prices, so it shares
    the Index outcome. Ratios r = in-force price / applied price run over categories with a positive Index cost.
    """

    in_force = displayed_prices(page)
    gate = {"inForce": {"source": "AA's displayed prices at capture", "observedAt": captured_at, "prices": in_force}, "factor": None, "bounds": None, "flag": None, "appliedRecord": None}
    if in_force is None:
        return {**gate, "outcome": GATE_UNVERIFIED, "flag": GATE_UNVERIFIED, "reason": "AA displays no complete price vector for the configuration"}
    check = reconciles(page, in_force)
    if check is not False:
        reason = "AA's Index category costs reconcile exactly with its displayed prices" if check else "category costs not published: AA's documented rule (listed prices) names the basis"
        return {**gate, "outcome": GATE_COMPATIBLE, "reason": reason}
    cost = page["intelligenceIndexCost"]
    active = [key for key in in_force if cost[INPUT_CATEGORIES.get(key, key)] > 0]
    for record in records:
        if not reconciles(page, record["prices"]):
            continue
        applied = {key: record[key] for key in ("id", "tariffStatus", "effectiveFrom", "effectiveUntil") if key in record}
        flagged = {**gate, "outcome": GATE_NOT_IN_FORCE, "appliedRecord": applied, "flag": NOT_IN_FORCE_FLAGS[record.get("tariffStatus", "superseded")],
                   "reason": "AA's cost reconciles with a registered price record that is not in force at V"}
        # E185: a free category that is now priced may carry demand no published total bounds.
        if any(record["prices"][key] == 0 and in_force[key] > 0 for key in in_force):
            return {**flagged, "bounds": {"status": BOUND_UNAVAILABLE}}
        ratios = {key: in_force[key] / record["prices"][key] for key in active}
        low, high = min(ratios.values()), max(ratios.values())
        if high - low <= VALUATION_TOLERANCE * high:
            return {**gate, "outcome": GATE_REVALUED, "factor": high, "appliedRecord": applied, "reason": "every priced category moved by one common factor; C' = k C for any demand mix"}
        # C'/C and M'/M are demand- and consumption-weighted means of the same ratios; a zero price in force has no finite Plan upper end.
        return {**flagged, "bounds": {"status": "available", "ratios": ratios, "apiCost": [low, high], "planCost": [low / high, high / low if low > 0 else None]}}
    return {**gate, "outcome": GATE_UNVERIFIED, "flag": GATE_UNVERIFIED, "reason": "AA's cost reconciles with neither its displayed prices nor a registered price record"}


def revalue(components: dict, factor: float) -> dict:
    """E170 outcome 2: every component's cost and reporting half-width scaled by the common price factor."""

    return {key: {**value, "costUsd": value["costUsd"] * factor, "halfWidthUsd": value["halfWidthUsd"] * factor} if value.get("costUsd") is not None else value for key, value in components.items()}


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


def configuration_family(configuration: dict) -> str:
    """The AA family of a ranked configuration (its chart points' family); the name for a record without one."""

    return configuration.get("family") or configuration["name"]


def cheaper_siblings(configuration: dict, page: dict, points: list[dict], ranked_efforts: set | frozenset = frozenset()) -> list[str]:
    """E201/O33: same-family configurations AA plots at a lower total Index cost that are not ranked (they lack an exact
    DeepSWE or Bug Hunt result); ``ranked_efforts`` are the efforts of the family's ranked configurations."""

    total = (page.get("intelligenceIndexCost") or {}).get("total")
    if total is None:
        return []
    family = configuration_family(configuration)
    return [point["model_name"] for point in points
            if point.get("family") == family and point["total_cost_usd"] < total
            and point.get("effort") != configuration.get("effort") and point.get("effort") not in ranked_efforts]


COST_EVIDENCE_MAX_AGE_DAYS = 45
PRICE_RECORD_MAX_AGE_DAYS = 7
REPORT_SEARCH_MAX_AGE_DAYS = 7
CAPTURE_GAP_MAX_DAYS = 7


def _instant(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def assemble(configurations: list[dict], documents: dict, *, release_day: date, pinned: list[str] | None = None) -> dict:
    """Evidence, admission, basket costs and Plan routes for every ranked configuration (no anchors yet)."""

    pages = {page["model"]["slug"]: page["model"] for page in documents["snapshot"]["pages"]}
    deepswe_by_id = {item["valueRankModelId"]: item for item in documents["deepswe"]["configurations"] if item.get("valueRankModelId")}
    bug_hunt_by_id = {item["modelId"]: item for item in documents["bugHunt"]["models"]}
    agent_records = {item["label"]: item for item in documents["codingAgents"]["configurations"]}
    chart_rows = {item["slug"]: {row["model"]: row for row in item["rows"]} for item in documents["costCharts"]["evaluations"]}
    mapping = documents["configurationMap"]["rows"]
    # E208: a route inherits the token-category mix its source publishes for the measured workload.
    sources = documents["planRoutes"].get("sourceEvidence") or {}
    routes = [
        {**route, "workloadMix": sources[route["sourceEvidenceId"]]["workloadMix"]}
        if "workloadMix" not in route and (sources.get(route.get("sourceEvidenceId")) or {}).get("workloadMix") else route
        for route in documents["planRoutes"]["routes"]
    ]
    # O32: only end-user reports dated in the release's report window count toward admission.
    window = (documents["planRoutes"].get("evidencePolicy") or {}).get("reportingWindow")
    # E213: one release cutoff; the report window is the 30 days ending on it (the evidence search cutoff is recorded apart).
    if window and window["end"] != release_day.isoformat():
        raise ValueError(f"the report window must end on the release cutoff {release_day} (E213), not {window['end']}")
    # E218: end-user reports are searched up to at most 7 days before the release cutoff, like the cohort capture (E211).
    searched = (documents["planRoutes"].get("evidencePolicy") or {}).get("searchCutoff")
    if window and (not searched or (release_day - date.fromisoformat(searched)).days > REPORT_SEARCH_MAX_AGE_DAYS):
        raise ValueError(f"end-user reports were last searched on {searched}, more than {REPORT_SEARCH_MAX_AGE_DAYS} days before the release cutoff {release_day} (E218)")
    # E216: the AA model-page snapshot and the price records are at most 45 days old at the release cutoff (the chart
    # and catalog capture that defines the cohort has its own 7-day gate, E211).
    # The price records decide which tariff is in force at V (E170), so they share the cohort capture's 7-day gate.
    for name, stamp, limit in (("AA model-page snapshot", documents["snapshot"].get("capturedAt"), COST_EVIDENCE_MAX_AGE_DAYS),
                               ("price records", documents["priceRecords"].get("observedAt"), PRICE_RECORD_MAX_AGE_DAYS)):
        if stamp and (release_day - date.fromisoformat(stamp[:10])).days > limit:
            raise ValueError(f"the {name} ({stamp[:10]}) is more than {limit} days old at the release cutoff {release_day} (E216)")
    # E217: the model pages (costs and AA-run leaves) and the chart that defines the cohort describe one AA state.
    chart, pages_at = (documents.get("frontierCapture") or {}).get("captured_at"), documents["snapshot"].get("capturedAt")
    if chart and pages_at and abs(_instant(chart) - _instant(pages_at)).total_seconds() > CAPTURE_GAP_MAX_DAYS * 86400:
        raise ValueError(f"the AA chart capture ({chart}) and model-page snapshot ({pages_at}) are more than {CAPTURE_GAP_MAX_DAYS} days apart (E217)")
    price_records = documents["priceRecords"]["records"]
    points = (documents.get("frontierCapture") or {}).get("points", [])
    rows, supplements = [], leaf_supplements(documents)
    for configuration in configurations:
        model_id, effort = configuration["id"], configuration.get("effort")
        page = pages.get(configuration["aaSlug"])
        if page is None:
            raise ValueError(f"{model_id}: AA model page {configuration['aaSlug']} is missing from the pinned snapshot")
        # A cohort row without a pinned map entry keeps its Index evidence; its agent and chart costs are missing (flagged).
        labels = mapping.get(model_id) or {}
        evidence = leaf_evidence(model_id, effort, page, deepswe_by_id.get(model_id), documents["tb4"]["rows"], bug_hunt_by_id.get(model_id), supplements)
        components, reconciliation = row_components(
            page,
            agent_records.get(labels.get(basket.CODING_AGENT_INDEX)),
            {slug: chart_rows[slug].get(labels.get(slug)) for slug in basket.CHART_COMPONENTS},
        )
        gate = valuation_gate(page, [item for item in price_records if item["aaSlug"] == configuration["aaSlug"]], documents["snapshot"].get("capturedAt"))
        if gate["outcome"] == GATE_REVALUED:
            components = revalue(components, gate["factor"])
        candidates = plan_routes.route_candidates(model_id, effort, routes, release_day, window=window)
        if gate["outcome"] == GATE_NOT_IN_FORCE:
            # O29: the Plan cost divides only by a multiple valued on the row's own (superseded) price record.
            for candidate in candidates:
                if candidate["route"].get("valuationPriceRecord") != gate["appliedRecord"].get("id"):
                    candidate.update(grade="diagnostic", valuation="different")
        rows.append({
            "valuationGate": gate,
            "page": page,
            "routeCandidates": candidates,
            **configuration,
            "evidence": evidence,
            "summary": q.summarize(evidence["observations"]),
            "components": components,
            "indexReconciliation": reconciliation,
            "configurationMapped": model_id in mapping,
            "routeSelection": plan_routes.route_selection(candidates),
            "admissionTable": plan_routes.admission_table(model_id, effort, routes, release_day, window),
        })
    # O36: only configurations with every leaf are ranked; the rest stay listed with their missing leaves and searches.
    incomplete = [entry for entry in (incomplete_entry(row, row["evidence"]) for row in rows) if entry is not None]
    check_leaf_searches(incomplete, documents, release_day)
    rows = [row for row in rows if incomplete_entry(row, row["evidence"]) is None]
    # O33: several efforts of one family can be ranked; only unranked cheaper configurations (an O36-incomplete one
    # included) are listed as unchecked.
    ranked_efforts: dict[str, set] = {}
    for row in rows:
        ranked_efforts.setdefault(configuration_family(row), set()).add(row.get("effort"))
    for row in rows:
        row["cheaperSiblings"] = cheaper_siblings(row, row["page"], points, ranked_efforts[configuration_family(row)])
    ids = [row["id"] for row in rows]
    admission = basket.admission_panel({row["id"]: row["components"] for row in rows}, ids)
    admitted = admission["admitted"]
    # E184: a deferred migration keeps the frozen admitted set; the newly admissible components stay pending.
    deferred = [component for component in admitted if pinned is not None and component not in pinned]
    admitted = [component for component in admitted if component not in deferred]
    main = basket.workload_hash(admitted)
    for row in rows:
        row["cost"] = basket.row_cost(row["components"], admitted)
        selected = row["routeSelection"]["selected"]
        row["plan"] = plan_routes.plan_cost(row["cost"]["costUsd"], selected)
    return {
        "rows": rows, "admission": admission, "admitted": admitted, "deferred": [{"component": component, "reason": DEFERRED_MIGRATION} for component in deferred],
        "mainWorkload": main, "releaseDay": release_day.isoformat(), "tb4Rows": documents["tb4"]["rows"], "incomplete": incomplete,
    }


DEFERRED_MIGRATION = "anchor migration unavailable — insufficient valuation-eligible references (E184)"


def assemble_for_release(configurations: list[dict], documents: dict, frozen: dict, *, release_day: date) -> dict:
    """E184: assemble, deferring a main-workload migration whose new workload could not be anchored.

    A component that gained admission since the anchors were frozen stays pending, and the release publishes on
    the frozen workload, when the new workload has fewer than two valuation-eligible anchor references; any other
    workload change is an ordinary migration (run `freeze`).
    """

    assembled = assemble(configurations, documents, release_day=release_day)
    frozen_components = frozen["workloads"][frozen["mainWorkload"]]["components"]
    gained = set(assembled["admitted"]) > set(frozen_components)
    if assembled["mainWorkload"] != frozen["mainWorkload"] and gained and len(anchor_population(assembled, assembled["admitted"])) < MIN_ANCHOR_REFERENCES:
        return assemble(configurations, documents, release_day=release_day, pinned=frozen_components)
    return assembled


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


def _gated_box(row: dict, low: float, high: float, basis: str) -> intervals.Box | None:
    """E170: a row's admissible box after the valuation-basis gate, or None when it is not interval-eligible.

    A row on an unverified basis competes at its published record, flagged provisional so it never earns a label but
    can still deny one (E222: O25 protects the published record). A row on a price not in force at V (O29) competes
    over the hull of its published record and its current-tariff bound, flagged provisional likewise.
    """

    gate, summary = row["valuationGate"], row["summary"]
    if gate["outcome"] == GATE_NOT_IN_FORCE and blocker_domain(gate, basis) is None:
        return None
    provisional = summary.provisional or gate["outcome"] == GATE_UNVERIFIED
    if gate["outcome"] == GATE_NOT_IN_FORCE:
        ratio_low, ratio_high = blocker_domain(gate, basis)
        low, high, provisional = low * min(1.0, ratio_low), high * max(1.0, ratio_high), True
    return intervals.Box(row["id"], low, high, summary.lower, summary.upper, provisional)


def blocker_domain(gate: dict, basis: str) -> tuple[float, float] | None:
    """E183/E185: the current-tariff ratio range a blocker's box is widened by, or None when it cannot be constructed."""

    bounds = gate["bounds"]
    if bounds["status"] != "available":
        return None
    low, high = bounds["apiCost" if basis == "api" else "planCost"]
    return (low, high) if high is not None and low > 0 else None


def api_boxes(assembled: dict, components: list[str] | None = None) -> list[intervals.Box]:
    """R_W on the API basis: ranked rows with FullCost on the main workload (E37), or on the subset workload of
    ``components`` (E190), as admissible boxes."""

    boxes = []
    for row in assembled["rows"]:
        cost = row["cost"] if components is None else basket.row_cost(row["components"], components)
        on_workload = components is not None or cost["workload"] == assembled["mainWorkload"]
        if cost["fullCost"] and on_workload and anchor_math.scoreable(cost["lowUsd"]):
            box = _gated_box(row, cost["lowUsd"], cost["highUsd"], "api")
            if box is not None:
                boxes.append(box)
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
        box = _gated_box(row, cost["lowUsd"] / bounds[1], cost["highUsd"] / bounds[0], "plan")
        if box is not None:
            boxes.append(box)
    return boxes


# E192: the bar is a quality level. A configuration on the frontier it tests can never be beaten there, so a
# configuration reference made the cheapest-above-the-bar output its own answer (version 1, superseded before release).
BAR_POLICY = {
    "policyId": "quality-quartile-ladder",
    "version": 3,
    "selectionMode": "deterministic at anchor freeze, before any bar outcome is computed",
    "populationRule": "non-provisional ranked configurations with a displayed quality",
    "order": "displayed quality ascending, then configuration ID",
    "position": "lower quartile, lower median (the headline bar) and upper quartile, each the displayed quality at zero-based position floor((n - 1) * k / 4), k = 1, 2, 3 (O34)",
    "reference": "the displayed quality at each ladder position, frozen as a level; the configuration at that position is recorded for audit and competes like any other",
    "minimumPopulation": 2,
    "emptyPopulation": "fewer than two population configurations: no bar pinned; the bar is published as unavailable",
    "ladderPopulation": "fewer than four population configurations: only the headline bar is pinned, because the quartile positions would coincide with it (E215)",
    "nonTautology": "a frozen level is never a configuration, so no bar can return its setter by construction; whether a result compares alternatives is published per result (possibleQualifierN, E198)",
    "lifetime": "fixed for the anchor version; replaced only by a versioned re-freeze that publishes old- and new-bar results on the common evaluable panel",
}
BAR_ID = "bar:median-quality"
MIN_BAR_POPULATION = 2
# E215: below four configurations the quartile positions coincide with the headline's, so only the headline is pinned.
MIN_LADDER_POPULATION = 4


# O34: the ladder of frozen levels, the median first (it is the headline bar). Each level is the displayed quality at
# zero-based position floor((n - 1) * k / 4) of the ascending population, so k = 2 is the lower median.
BAR_LADDER = (
    (BAR_ID, 2, "lower-median displayed quality of the non-provisional cohort configurations at freeze (E192; headline bar)"),
    ("bar:lower-quartile-quality", 1, "lower-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)"),
    ("bar:upper-quartile-quality", 3, "upper-quartile displayed quality of the non-provisional cohort configurations at freeze (O34)"),
)


def bar_levels(assembled: dict) -> tuple[list[str], list[dict]]:
    """E156/E192/O34: the bar population and the frozen quality ladder, chosen before any bar outcome is computed."""

    rows = [row for row in assembled["rows"] if row["summary"].displayed is not None and not row["summary"].provisional]
    ordered = sorted(rows, key=lambda row: (row["summary"].displayed, row["id"]))
    if len(ordered) < MIN_BAR_POPULATION:
        return [row["id"] for row in ordered], []
    bars = []
    for bar_id, quarter, rule in BAR_LADDER:
        if quarter != 2 and len(ordered) < MIN_LADDER_POPULATION:
            continue
        row = ordered[(len(ordered) - 1) * quarter // 4]
        bars.append({"id": bar_id, "level": row["summary"].displayed, "levelConfiguration": row["id"], "rule": rule})
    return [row["id"] for row in ordered], bars


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


def anchor_eligibility(assembled: dict, components: list[str]) -> list[dict]:
    """E184: each row's anchor-reference eligibility on a workload, with the reason it is excluded."""

    table = []
    for row in assembled["rows"]:
        complete = all((row["components"].get(component) or {}).get("completeness") == basket.COMPLETE for component in components)
        outcome = row["valuationGate"]["outcome"]
        reason = None if complete and outcome in GATE_SCORED else "incomplete cost evidence" if not complete else f"valuation gate: {outcome}"
        table.append({"row": row["id"], "completeEvidence": complete, "valuationGate": outcome, "eligible": reason is None, "reason": reason})
    return table


def anchor_population(assembled: dict, components: list[str]) -> list[str]:
    """E160: ranked configurations with complete cost evidence on every component of a workload."""

    # E170/O29: a row whose AA cost is not on the price in force at V is never an anchor reference.
    return sorted(item["row"] for item in anchor_eligibility(assembled, components) if item["eligible"])


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
    # E156/E192: the bar comes from the registered policy, at freeze, before any bar outcome is computed.
    population, references = bar_levels(assembled)
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
        "barPolicy": {**BAR_POLICY, "selectionCutoff": frozen_at, "population": sorted(population), "bars": [{key: item[key] for key in ("id", "level", "levelConfiguration")} for item in references]},
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


def interval_outputs(assembled: dict, frozen: dict, basis: str, components: list[str] | None = None) -> dict:
    """Frontier and bar results over R_W for one basis, with the universe and the unevaluable rows (E38).

    With ``components``, the outputs are for that subset workload (E190; API basis only: no Plan multiple is
    identified for a subset workload).
    """

    boxes = api_boxes(assembled, components) if basis == "api" else plan_boxes(assembled)
    # E183: competitors range over U_W = R_W plus the O29 blockers B_W; labels go to R_W only.
    not_in_force = {row["id"] for row in assembled["rows"] if row["valuationGate"]["outcome"] == GATE_NOT_IN_FORCE}
    unconstructible = sorted(row["id"] for row in assembled["rows"] if row["id"] in not_in_force and blocker_domain(row["valuationGate"], basis) is None)
    # E222/E228: an unverified basis, or (Plan) a route whose evidence a detected change may have superseded, competes but
    # earns no label, exactly like an O29 blocker.
    blocked = not_in_force | {row["id"] for row in assembled["rows"] if row["valuationGate"]["outcome"] == GATE_UNVERIFIED}
    if basis == "plan":
        blocked |= {row["id"] for row in assembled["rows"] if plan_routes.change_flagged(row["routeSelection"]["selected"])}
    universe = sorted(box.row for box in boxes if box.row not in blocked)
    blockers = sorted(box.row for box in boxes if box.row in blocked)
    unevaluable = sorted(row["id"] for row in assembled["rows"] if row["id"] not in universe and row["id"] not in blockers)
    if not boxes:
        reason = "no row has FullCost and an identified M_W (E61/E67)" if basis == "plan" else "no row has FullCost on the main workload"
        return {"universe": [], "unevaluable": unevaluable, "status": intervals.UNEVALUABLE, "reason": reason}
    if unconstructible:
        unevaluable = [row_id for row_id in unevaluable if row_id not in unconstructible]
        return {"universe": universe, "blockers": sorted(set(blockers) | set(unconstructible)), "unevaluable": unevaluable, "status": intervals.UNRESOLVED,
                "reason": "a blocker's current-tariff domain cannot be constructed (E183, E185): " + ", ".join(unconstructible)}
    frontier, bars = intervals.frontier(boxes), _bar_results(boxes, assembled, frozen)
    # E170/O29: a blocker competes over its hull but earns no interval label of its own.
    for row_id in blockers:
        frontier[row_id] = {"status": WITHHELD_LABEL}
        for bar in bars:
            if "rows" in bar:
                bar["rows"][row_id] = {"status": WITHHELD_LABEL}
                bar["possibleCheapest"] = [item for item in bar["possibleCheapest"] if item != row_id]
                bar["uncheckedCheaperSiblings"].pop(row_id, None)
    for bar in bars:
        if "rows" in bar:
            _comparison(bar)
    return {"universe": universe, "blockers": blockers, "unevaluable": unevaluable, "status": "evaluated", "frontier": frontier, "bars": bars}


WITHHELD_LABEL = "no interval label: AA cost on a price not in force at V (O29); competes over its current-tariff hull"


SUBSET_PLAN_INTERVALS = "unevaluable: no Plan multiple is identified for a subset workload (E149, E190)"


def subset_interval_outputs(assembled: dict, frozen: dict) -> dict:
    """E190: frontier and bar outputs on each subset workload over every row with FullCost there."""

    return {
        workload: {"components": entry["components"], "api": interval_outputs(assembled, frozen, "api", entry["components"]),
                   "plan": {"status": intervals.UNEVALUABLE, "reason": SUBSET_PLAN_INTERVALS}}
        for workload, entry in sorted(frozen["workloads"].items())
        if entry.get("role") == "subset"
    }


def _bar_reference(bar: dict) -> intervals.Reference:
    """E192: a frozen quality level is a reference with no uncertainty of its own."""

    return intervals.Reference(bar["id"], bar["level"], bar["level"])


def _bar_results(boxes: list[intervals.Box], assembled: dict, frozen: dict) -> list[dict]:
    """Each bar's interval outcome; every row also gets its displayed-quality margin to the level (E198)."""

    by_id = {row["id"]: row for row in assembled["rows"]}
    results = []
    for bar in frozen["barReferences"]:
        outcome = intervals.cheapest_above_bar(boxes, _bar_reference(bar))
        for row_id, item in outcome.get("rows", {}).items():
            displayed = by_id[row_id]["summary"].displayed
            item["displayedMargin"] = None if displayed is None else displayed - bar["level"]
        if "possibleCheapest" in outcome:
            # E201/O33: cheaper plotted configurations of each candidate's family that are not ranked were not evaluated.
            outcome["uncheckedCheaperSiblings"] = {row_id: by_id[row_id].get("cheaperSiblings", []) for row_id in outcome["possibleCheapest"]}
        results.append({"reference": bar, **outcome})
    return results


VACUOUS_COMPARISON = "vacuous: fewer than two evaluable configurations can qualify"

DISPLAYED_CHEAPEST_LABEL = "displayed record on the headline scale, not a claim: the lowest-cost scored main-workload row whose displayed quality reaches each bar (E203)"


def displayed_cheapest(assembled: dict, frozen: dict, basis: str) -> dict:
    """E203: per bar, the cheapest non-provisional scored main-workload rows whose displayed quality reaches the level (ties listed)."""

    rows = [row for row in assembled["rows"] if row["cost"]["workload"] == assembled["mainWorkload"] and not row["summary"].provisional
            and row["summary"].displayed is not None and _basis_cost(row, basis) is not None]
    bars = []
    for bar in frozen["barReferences"]:
        qualifying = [row for row in rows if row["summary"].displayed >= bar["level"]]
        low = min((_basis_cost(row, basis) for row in qualifying), default=None)
        bars.append({"bar": bar["id"], "level": bar["level"], "qualifierN": len(qualifying), "costUsd": low,
                     "cheapest": sorted(row["id"] for row in qualifying if _basis_cost(row, basis) == low)})
    return {"label": DISPLAYED_CHEAPEST_LABEL, "bars": bars}


def _comparison(bar: dict) -> None:
    """E198: how many configurations of R_W can possibly qualify, so a one-candidate result is never read as a comparison."""

    count = sum(1 for item in bar["rows"].values() if item.get("possible") == intervals.CERTIFIED)
    bar["possibleQualifierN"] = count
    # E201: confirmed qualification needs a row's full-composite lower bound (missing leaves at 0, O25) to clear the level.
    bar["confirmedQualifierN"] = sum(1 for item in bar["rows"].values() if item.get("confirmed") == intervals.CERTIFIED)
    bar["comparison"] = VACUOUS_COMPARISON if count < 2 else f"compares {count} configurations that can qualify"


# E146: registered deletion branches. Displayed-score sensitivity removes the leaf set R globally and
# renormalises the remaining observed weights: Q(-R) = sum_{b in O\R} w_b z_b / sum_{b in O\R} w_b (a zero
# denominator leaves the row unevaluable); cost, workload, route and anchors stay primary.
LEAVE_OUT_MIN_WEIGHT = 0.40
SOURCE_LEAVES = {"Artificial Analysis": tuple(leaf.key for leaf in q.LEAVES if leaf.source == "aa")}


# E178: the leaves whose benchmarks O15 excludes from the cost basket (basket.INDEX_RESIDUAL_TASKS), removed jointly.
BASKET_SCOPE_EXCLUDED = ("hle", "critpt", "omniscience")
BASKET_SCOPE_LABEL = "quality restricted to the cost basket's scope"


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
    branches.append({"id": "basket-scope", "labels": [BASKET_SCOPE_LABEL], "removed": list(BASKET_SCOPE_EXCLUDED)})
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


# E226: renormalising over each row's own leaves is not neutral when the sparse leaves are the hard ones. The common-leaf
# branch drops, for every row, the leaves fewer than 90% of cohort rows observe, and publishes each row's effect
# (displayed minus common-leaf quality, also in cost-doubling equivalents), the rank changes and the bar reach. It is a
# deletion diagnostic like E146: nothing is imputed and no score changes (O8).
COMMON_LEAF_SHARE = 0.90
COMMON_LEAF_LABEL = "common leaf set: leaves observed by fewer than 90% of cohort rows removed for every row (E226; diagnostic)"


def common_leaf_diagnostic(rows: list[dict], per_row: dict, frozen: dict, quality_per_doubling: float) -> dict:
    """E226: each row's leaf-availability effect, the value-rank changes and the frozen bars' reach on the common leaves."""

    counts = {leaf.key: sum(1 for row in rows if leaf.key in row["evidence"]["observations"]) for leaf in q.LEAVES}
    sparse = sorted(key for key, count in counts.items() if count < COMMON_LEAF_SHARE * len(rows))
    common = {row["id"]: deletion_quality(row["evidence"]["observations"], set(sparse)) for row in rows}
    effects = {}
    for row in rows:
        displayed = row["summary"].displayed
        if displayed is not None and common[row["id"]] is not None:
            effect = displayed - common[row["id"]]
            effects[row["id"]] = {"effect": effect, "costDoublings": effect / quality_per_doubling}
    bases = {}
    for basis in BASES:
        primary = {row_id: per_row[row_id][basis]["value"] for row_id in effects if per_row[row_id][basis]["value"] is not None}
        branched = {row_id: anchor_math.value_score(per_row[row_id][basis]["costScore"], common[row_id], BETA) for row_id in primary}
        panel = sorted(primary)
        bases[basis] = {"rankChanges": diagnostics.paired_rank_change(primary, branched),
                        "kendallTauB": diagnostics.kendall_tau_b([primary[key] for key in panel], [branched[key] for key in panel])}
    population = [row for row in rows if row["summary"].displayed is not None and not row["summary"].provisional and common[row["id"]] is not None]
    reach = [{"bar": bar["id"], "level": bar["level"], "displayedReachN": sum(1 for row in population if row["summary"].displayed >= bar["level"]),
              "commonLeafReachN": sum(1 for row in population if common[row["id"]] >= bar["level"])} for bar in frozen["barReferences"]]
    flagged = sorted(row_id for row_id, item in effects.items() if abs(item["costDoublings"]) > 1.0)
    return {"label": COMMON_LEAF_LABEL, "sparseLeaves": sparse, "coverage": counts, "rows": effects, "flagged": flagged, "bases": bases, "barReach": reach}


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


# E171: every admissible route-measurement pair beside the selected one. No separate "best" route ranking exists: the
# owner's highest-eligible Value Multiple rule is comparator key 3, and a larger displayed score here is arithmetic.
ALTERNATIVE_IDENTIFIED = "identified on the scored workload"
ALTERNATIVE_ARITHMETIC = "observed-workload arithmetic only (target-workload ordering not identified)"


def route_alternatives(row: dict, anchors: dict | None) -> dict:
    """E171/E179: the route-alternative table for one row, in comparator order, with its selection summary."""

    selection = row["routeSelection"]
    selected = selection["selected"]
    api_cost = row["cost"]["costUsd"]
    table = []
    for candidate in sorted((item for item in row["routeCandidates"] if item["grade"] != "diagnostic"), key=plan_routes.comparator_key):
        route = candidate["route"]
        multiple = plan_routes.comparison_multiple(route)
        cost = api_cost / multiple if anchor_math.scoreable(api_cost) else None
        score = anchor_math.cost_score(cost, anchors) if anchors and cost is not None else None
        dominated_by = selection["dominated"].get(route["id"])
        tuple_ = plan_routes.comparison_tuple(candidate)
        table.append({
            "routeId": route["id"],
            "identification": candidate["identification"],
            "grade": candidate["grade"],
            "measurementWorkload": route.get("measurementWorkload", "the route's measurement workload"),
            "valuationStatus": candidate["valuation"],
            "displayedMultiple": multiple,
            "displayedPlanValue": anchor_math.value_score(score, row["summary"].displayed, BETA),
            "comparisonTuple": [item if math.isfinite(item) else None for item in tuple_],
            "status": "selected" if selected is candidate else f"dominated by {dominated_by} (E88)" if dominated_by else "not selected by the comparator",
            "comparisonWithSelected": ALTERNATIVE_IDENTIFIED if candidate["identification"] in plan_routes.IDENTIFIED else ALTERNATIVE_ARITHMETIC,
        })
    # E179: the comparator's pick with the selected pair removed shows what choosing the largest observed multiple gained.
    fallback = plan_routes.route_selection([item for item in row["routeCandidates"] if item is not selected])["selected"] if selected else None
    by_route = {item["routeId"]: item for item in table}
    return {
        "pairs": table,
        "admissiblePairs": len(table),
        "unidentifiedPairs": sum(1 for item in table if item["identification"] not in plan_routes.IDENTIFIED),
        "leaveSelectedOut": None if fallback is None else {key: by_route[fallback["route"]["id"]][key] for key in ("routeId", "displayedMultiple", "displayedPlanValue")},
    }


FRONTIER_ANCHOR_LABEL = "anchors from frontier and near-frontier configurations only (diagnostic; the frozen anchors stay primary)"


POLICY_BAR_ID = "bar:policy-cohort-median"


def policy_cohort_bar(assembled: dict, frozen: dict) -> dict:
    """E199: the bar recomputed over the frontier and near-frontier configurations alone, with its API result (a sensitivity)."""

    population, bars = bar_levels({**assembled, "rows": [row for row in assembled["rows"] if row.get("frontierFamily", True)]})
    if not bars:
        return {"status": f"unavailable: fewer than {MIN_BAR_POPULATION} non-provisional frontier-family configurations", "population": population}
    bar = {**bars[0], "id": POLICY_BAR_ID, "rule": "lower-median displayed quality of the non-provisional frontier and near-frontier configurations (E199)"}
    result = interval_outputs(assembled, {**frozen, "barReferences": [bar]}, "api")
    return {"status": "evaluated", "population": population, "bar": bar, "api": result["bars"][0] if result["status"] == "evaluated" else {"status": result["status"]}}


def frontier_anchor_diagnostic(assembled: dict, frozen: dict, per_row: dict) -> dict:
    """E187: each basis rescored on anchors built from the frontier and near-frontier references alone (and E199's bar)."""

    by_id = {row["id"]: row for row in assembled["rows"]}
    references = [row_id for row_id in anchor_population(assembled, assembled["admitted"]) if by_id[row_id].get("frontierFamily", True)]
    policy_bar = policy_cohort_bar(assembled, frozen)
    if len(references) < MIN_ANCHOR_REFERENCES:
        return {"label": FRONTIER_ANCHOR_LABEL, "status": f"unavailable: fewer than {MIN_ANCHOR_REFERENCES} frontier-family references", "references": references, "bar": policy_bar}
    return {"label": FRONTIER_ANCHOR_LABEL, "status": "evaluated", "references": references, "bases": _rebuilt_anchor_bases(assembled, frozen, per_row, references), "bar": policy_bar}


def _rebuilt_anchor_bases(assembled: dict, frozen: dict, per_row: dict, references: list[str]) -> dict:
    """Each basis rescored on anchors rebuilt from ``references`` by the freeze rule, against the frozen anchors."""

    main = assembled["mainWorkload"]
    by_id = {row["id"]: row for row in assembled["rows"]}
    rows = [row for row in assembled["rows"] if row["cost"]["workload"] == main]
    bases = {}
    for basis in BASES:
        costs = {row_id: basis_cost_on(by_id[row_id], assembled["admitted"], basis) for row_id in references}
        rebuilt = anchor_math.anchor_object(costs, basis=basis, workload=main)
        primary = {row["id"]: per_row[row["id"]][basis]["value"] for row in rows}
        rescored = {row["id"]: anchor_math.value_score(anchor_math.cost_score(_basis_cost(row, basis), rebuilt), row["summary"].displayed, BETA) for row in rows}
        bases[basis] = {
            "anchors": {key: rebuilt[key] for key in ("low", "high", "referenceIds")},
            "exchangeRate": anchor_math.exchange_rate(rebuilt, BETA),
            "frozenExchangeRate": anchor_math.exchange_rate(frozen["workloads"][main]["anchors"][basis], BETA),
            "rankChanges": diagnostics.paired_rank_change(primary, rescored),
        }
    return bases


FAMILY_PRIMARY_LABEL = "one row per family, each family's primary configuration (diagnostic, E205); the frozen ladder and anchors stay primary"


def family_primary_diagnostic(assembled: dict, frozen: dict, per_row: dict) -> dict:
    """E205: the bar ladder and the anchors recomputed with one row per family, so the effect of how many efforts a family
    has evidenced is separable from E199's narrowing to frontier families (same rules, primary rows only)."""

    keep = {row["id"] for row in assembled["rows"] if row.get("familyPrimary", True)}
    population, bars = bar_levels({**assembled, "rows": [row for row in assembled["rows"] if row["id"] in keep]})
    references = [row_id for row_id in anchor_population(assembled, assembled["admitted"]) if row_id in keep]
    result = {
        "label": FAMILY_PRIMARY_LABEL, "population": population, "references": references,
        "ladder": [{key: bar[key] for key in ("id", "level", "levelConfiguration")} for bar in bars],
        "frozenLadder": [{key: bar[key] for key in ("id", "level")} for bar in frozen["barReferences"]],
    }
    if len(references) < MIN_ANCHOR_REFERENCES:
        return {**result, "status": f"unavailable: fewer than {MIN_ANCHOR_REFERENCES} family-primary references"}
    return {**result, "status": "evaluated", "bases": _rebuilt_anchor_bases(assembled, frozen, per_row, references)}


def cost_component_family(assembled: dict, frozen: dict, per_row: dict) -> list[dict]:
    """E172: the E149 cost-deletion object registered once per admitted basket unit (the Coding Agent Index is one unit)."""

    return [cost_removal(assembled, frozen, per_row, component) for component in assembled["admitted"]]


def _spread(values: list[float]) -> dict:
    """Median and range of a list, or nulls when it is empty."""

    if not values:
        return {"median": None, "min": None, "max": None, "n": 0}
    return {"median": statistics.median(values), "min": min(values), "max": max(values), "n": len(values)}


def subset_bridges(assembled: dict, frozen: dict, per_row: dict, expenditure: dict) -> list[dict]:
    """E10/E173: each subset workload's paired full/subset results and the missing components' expenditure shares.

    The rows evidenced on both the main workload W and the subset W_S are the
    main-workload rows (W_S is a subset of W). Each is scored on both workloads
    against that workload's own frozen anchors; missing costs are never filled.
    The missing components' shares come from the E22 expenditure object, so a
    subset row's readers see how large the omitted spend is among full rows.
    """

    main = assembled["mainWorkload"]
    main_components = frozen["workloads"][main]["components"]
    paired = [row for row in assembled["rows"] if row["cost"]["workload"] == main]
    bridges = []
    for workload, entry in sorted(frozen["workloads"].items()):
        if entry.get("role") != "subset":
            continue
        components = entry["components"]
        members = sorted(row["id"] for row in assembled["rows"] if row["cost"]["workload"] == workload)
        missing = [component for component in main_components if component not in components]
        shares = {component: _spread([item["shares"][component] for item in expenditure.values() if component in item["shares"]]) for component in missing}
        bases = {}
        for basis in BASES:
            anchors = entry["anchors"][basis]
            if anchors is None:
                bases[basis] = {"status": entry.get("anchorStatus", "unavailable")}
                continue
            full = {row["id"]: per_row[row["id"]][basis]["value"] for row in paired}
            restricted = {
                row["id"]: anchor_math.value_score(anchor_math.cost_score(basis_cost_on(row, components, basis), anchors), row["summary"].displayed, BETA)
                for row in paired
            }
            changes = diagnostics.paired_rank_change(full, restricted)
            differences = [restricted[key] - full[key] for key in full if full[key] is not None and restricted[key] is not None]
            bases[basis] = {
                "status": "evaluated",
                "exchangeRates": {"main": anchor_math.exchange_rate(frozen["workloads"][main]["anchors"][basis], BETA), "subset": anchor_math.exchange_rate(anchors, BETA)},
                "valueDifference": _spread(differences),
                "rows": {key: {"fullValue": full[key], "subsetValue": restricted[key]} for key in sorted(full)},
                "rankChanges": changes,
            }
        bridges.append({
            "workload": workload, "components": components, "subsetRows": members, "missingComponents": missing,
            "missingExpenditureShare": shares, "pairedRows": sorted(row["id"] for row in paired),
            "label": "paired full/subset bridge on rows evidenced on both workloads (E10); missing costs are never filled",
            "direction": "not known: a subset row's effect depends on its unobserved share of the missing components relative to the reference configurations",
            "bases": bases,
        })
    return bridges


# E219: the quality section's sensitivity band applied to the bar outputs. Each missing leaf is bounded by the cohort's
# observed range for that leaf instead of 0-100, which shows how much of the possible/confirmed gap is missing-leaf
# ignorance. It is a sensitivity, never evidence: it enters no label, no Θ and no published claim (O19, O25).
BAND_LABEL = "observed-range sensitivity, not evidence: missing leaves bounded by the cohort's observed range for that leaf (E219)"


def leaf_ranges(assembled: dict) -> dict:
    """The cohort's observed z range for each leaf (a leaf no row observes keeps its 0-100 domain)."""

    ranges = {}
    for leaf in q.LEAVES:
        values = [row["summary"].observations[leaf.key].z for row in assembled["rows"] if leaf.key in row["summary"].observations]
        ranges[leaf.key] = (min(values), max(values)) if values else (0.0, 100.0)
    return ranges


def band_summary(summary, ranges: dict):
    """A row's quality bounds with each missing leaf inside the cohort's observed range (E219)."""

    lower = upper = 0.0
    for leaf in q.LEAVES:
        observation = summary.observations.get(leaf.key)
        low, high = (observation.low, observation.high) if observation else ranges[leaf.key]
        lower, upper = lower + leaf.weight * low, upper + leaf.weight * high
    return dataclasses.replace(summary, lower=lower / 100.0, upper=upper / 100.0)


def observed_range_bars(assembled: dict, frozen: dict) -> dict:
    """E219: the API bar results recomputed on the band bounds, beside the published ones."""

    ranges = leaf_ranges(assembled)
    banded = {**assembled, "rows": [{**row, "summary": band_summary(row["summary"], ranges)} for row in assembled["rows"]]}
    result = interval_outputs(banded, frozen, "api")
    bars = [{key: bar.get(key) for key in ("status", "possibleQualifierN", "confirmedQualifierN", "confirmedCheapest", "possibleCheapest")} | {"bar": bar["reference"]["id"]}
            for bar in result.get("bars", [])]
    return {"label": BAND_LABEL, "status": result["status"], "ranges": ranges, "bars": bars}


# E221: for each row that can but need not reach a bar, the mean score its missing leaves would need (at the observed
# leaves' point values) for its full composite to reach the bar. It says what evidence would settle the row; it is a
# deterministic reading of published values, never a claim and never a label.
REQUIRED_LABEL = "required mean score on the missing leaves for the full composite to reach the bar (E221; not a claim)"


def required_missing_score(summary, level: float) -> float | None:
    """u* = (100 H - sum of observed w z) / sum of missing w; None when no leaf is missing."""

    missing = sum(leaf.weight for leaf in q.LEAVES if leaf.key not in summary.observations)
    if not missing:
        return None
    observed = sum(leaf.weight * summary.observations[leaf.key].z for leaf in q.LEAVES if leaf.key in summary.observations)
    return (100.0 * level - observed) / missing


def required_missing_scores(assembled: dict, frozen: dict) -> dict:
    """E221: the API rows that can possibly but not certainly reach each bar, with u* and their missing leaves."""

    by_id = {row["id"]: row for row in assembled["rows"]}
    result = interval_outputs(assembled, frozen, "api")
    bars = []
    for bar in result.get("bars", []):
        level = bar["reference"]["level"]
        open_rows = [row_id for row_id, status in bar["rows"].items() if status.get("possible") == "certified" and status.get("confirmed") != "certified"]
        rows = [{"row": row_id, "required": required_missing_score(by_id[row_id]["summary"], level),
                 "missing": [leaf.key for leaf in q.LEAVES if leaf.key not in by_id[row_id]["summary"].observations]} for row_id in open_rows]
        bars.append({"bar": bar["reference"]["id"], "level": level, "rows": sorted(rows, key=lambda item: (item["required"] is None, item["required"] or 0.0, item["row"]))})
    return {"label": REQUIRED_LABEL, "status": result["status"], "bars": bars}


# E207: the frozen ladder's standing in the current population, so a bar most rows have outgrown is flagged, not silent.
BAR_LIFETIME = "until the next anchor re-freeze or methodology version, whichever comes first"
BAR_STALE_LOW = "headline bar below the current population's lower quartile: re-freeze the ladder at the next anchor version (informational; no score changes)"
BAR_STALE_HIGH = "headline bar above the current population's upper quartile: re-freeze the ladder at the next anchor version (informational; no score changes)"


def bar_currency(assembled: dict, frozen: dict) -> dict:
    """E207: each frozen bar's reach in the current bar population, the ladder this population would freeze, and a flag
    when the headline bar has left the current interquartile range."""

    population, current = bar_levels(assembled)
    displayed = [row["summary"].displayed for row in assembled["rows"] if row["id"] in set(population)]
    bars = [{"bar": bar["id"], "level": bar["level"], "reachN": sum(1 for value in displayed if value >= bar["level"]), "populationN": len(displayed)}
            for bar in frozen["barReferences"]]
    levels = {bar["id"]: bar["level"] for bar in current}
    headline = next((bar["level"] for bar in frozen["barReferences"] if bar["id"] == BAR_ID), None)
    flag = None
    if headline is not None and len(levels) == len(BAR_LADDER):
        flag = BAR_STALE_LOW if headline < levels[BAR_LADDER[1][0]] else BAR_STALE_HIGH if headline > levels[BAR_LADDER[2][0]] else None
    return {"lifetime": BAR_LIFETIME, "bars": bars, "currentLadder": [{key: bar[key] for key in ("id", "level")} for bar in current], "flag": flag}


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
        # E189: how closely the cost-only and quality-only orderings follow the value ordering on the same panel.
        panel_rows = [row for row in rows if row["cost"]["workload"] == main and per_row[row["id"]][basis]["value"] is not None]
        values = [per_row[row["id"]][basis]["value"] for row in panel_rows]
        influence[basis]["orderingAgreement"] = {
            "costVsValue": diagnostics.kendall_tau_b([per_row[row["id"]][basis]["costScore"] for row in panel_rows], values) if len(panel_rows) >= 2 else None,
            "qualityVsValue": diagnostics.kendall_tau_b([row["summary"].displayed for row in panel_rows], values) if len(panel_rows) >= 2 else None,
        }
        main_anchors = frozen["workloads"][main]["anchors"][basis]
        exchange[basis] = {**anchor_math.exchange_rate(main_anchors, BETA), "curve": anchor_math.exchange_rate_curve(BETA, [4.0, 16.0, 64.0, 256.0, 1024.0])}
    hold = any(item["hold"] for basis in BASES for item in gates[basis])
    yield_ = plan_routes.identification_yield({row["id"]: row["routeSelection"]["selected"] for row in rows})
    agreement = _quality_agreement(rows)
    measured = _measured_only_view(rows, frozen, per_row)
    readiness = cost_diagnostics.basket_readiness(rows, assembled["admission"], main)
    manifest = [
        _rule("clip gate (E20)", "fired" if hold else "passed", "release held" if hold else "no basis exceeds the clipping allowance"),
        _rule("cost influence flag (E91)", "fired" if influence["api"]["flag"] or influence["plan"]["flag"] else "passed", "cost not discriminating (< 10%); informational only; beta never changes (O2)"),
        _rule("quality influence flag (E126)", "fired" if influence["api"]["qualityFlag"] or influence["plan"]["qualityFlag"] else "passed", "quality not discriminating (cost share > 90%); informational only"),
        _rule("subset scoring (O17)", "fired" if any(row["cost"]["subset"] for row in rows) else "vacuous", "subset rows scored on their own workload and anchors"),
        _rule("partial component flag (E37)", "fired" if any(row["cost"]["partialComponents"] for row in rows) else "vacuous", "AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209)"),
        _rule("route dominance filter (E88)", "fired" if any(row["routeSelection"]["dominated"] for row in rows) else "vacuous", "certifiably dearer routes set aside"),
        _rule("Plan exploratory label (E61)", "fired" if yield_["exploratory"] else "passed", "fewer than half of Plan rows have an identified M_W"),
        _rule("score swing gate (E177)", "vacuous", "first v3 release: no previous v3 release to compare"),
        _rule("anchor migration (E184)", "fired" if assembled.get("deferred") else "vacuous",
              "deferred: " + ", ".join(item["component"] for item in assembled["deferred"]) if assembled.get("deferred") else "no main-workload migration deferred"),
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
        "deferredComponents": assembled.get("deferred", []),
        "admissionMatrices": assembled["admission"]["matrices"],
        "workloads": {
            workload: {"components": entry["components"], "role": entry["role"], "anchors": entry["anchors"], "anchorStatus": entry["anchorStatus"]}
            for workload, entry in frozen["workloads"].items()
        },
        "exchangeRate": exchange,
        # E176: rows by token metering basis; AA does not publish the basis per configuration today.
        "meteringMix": {basis_name: (len(rows) if basis_name == METERING_BASES[-1] else 0) for basis_name in METERING_BASES},
        "sourceIntervals": SOURCE_INTERVALS,
        "sourceDates": SOURCE_DATES,
        "costInfluence": influence,
        "gates": {"clip": gates, "hold": hold},
        "identificationYield": yield_,
        "rows": [_row_json(row, per_row[row["id"]], ranks, route_alternatives(row, _anchors_for(frozen, row["cost"]["workload"], "plan"))) for row in rows],
        "intervals": {basis: interval_outputs(assembled, frozen, basis) for basis in BASES},
        "incompleteEvidence": assembled.get("incomplete", []),
        "displayedCheapest": {basis: displayed_cheapest(assembled, frozen, basis) for basis in BASES},
        "barCurrency": bar_currency(assembled, frozen),
        "observedRangeBars": observed_range_bars(assembled, frozen),
        "requiredMissingScores": required_missing_scores(assembled, frozen),
        "subsetIntervals": subset_interval_outputs(assembled, frozen),
        "measuredOnlyPlanView": measured,
        "diagnostics": {
            "terminalBenchSameHarness": _tb_same_harness(rows, assembled["tb4Rows"]),
            "anchorStability": _anchor_stability(rows, frozen, main, per_row),
            "omniscienceAbstentionSensitivity": _abstention_sensitivity(rows, per_row),
            "gdpvalLogisticSensitivity": _gdpval_logistic_sensitivity(rows, per_row),
            "qualitySourceShares": q.source_shares(),
            "qualityAgreement": agreement,
            "qualitySubstitutionAgreement": _substitution_agreement(rows, per_row),
            "disjointEvidenceAgreement": _disjoint_agreement(rows),
            "nonDiscriminatingLeaves": diagnostics.non_discriminating(_z_by_leaf(rows)),
            "groupDrift": _group_drift(rows),
            "qualityDispersion": _panel_dispersion(rows),
            "deletionSensitivity": _deletion_sensitivity(rows, per_row),
            "commonLeaf": common_leaf_diagnostic(rows, per_row, frozen, exchange["api"]["qualityPointsPerCostDoubling"]),
            "costRemoval": cost_removal(assembled, frozen, per_row),
            "costComponentFamily": cost_component_family(assembled, frozen, per_row),
            "frontierAnchors": frontier_anchor_diagnostic(assembled, frozen, per_row),
            "familyPrimary": family_primary_diagnostic(assembled, frozen, per_row),
            "subsetBridges": subset_bridges(assembled, frozen, per_row, readiness["expenditure"]),
            "basketReadiness": readiness,
            "anchorEligibility": anchor_eligibility(assembled, assembled["admitted"]),
            "sweCompanion": cost_diagnostics.swe_companion(rows, main),
            "matchedCost": cost_diagnostics.matched_cost(rows, main),
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
        # E170/O29: a row whose AA cost is not on the price in force at V is never a measured reference.
        references = {
            row_id: measured[row_id]["costUsd"] for row_id in members
            if not by_id[row_id]["cost"]["partialComponents"] and by_id[row_id]["valuationGate"]["outcome"] in GATE_SCORED
        }
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
    """E125 (as amended by O37): the leaf is AA's own run on one harness; rows whose leaf came from another agent are
    harness-mixed, and the leaf's agreement with tbench.ai's vendor-agent results is published on their common panel."""

    primary, restricted, mixed = {}, {}, []
    for row in rows:
        source = row["evidence"]["provenance"].get("terminalBench")
        if source is not None and "terminalBench" in row["evidence"]["observations"]:
            primary[row["id"]] = row["evidence"]["observations"]["terminalBench"].z
            if source.get("agent") != DEFAULT_TB_HARNESS:
                mixed.append(row["id"])
        selected = exact_match.select_tb4_row(row["id"], row.get("effort"), tb4_rows)
        if selected is not None:
            restricted[row["id"]] = selected["resolutionRatePct"]
    return {
        "defaultHarness": DEFAULT_TB_HARNESS,
        "restricted": restricted,
        "harnessMixed": sorted(mixed),
        "agreement": diagnostics.agreement(primary, restricted, label="Terminal-Bench cross-source agreement (AA's run against tbench.ai)"),
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
        value = per_row[row["id"]]["api"]["value"]
        if value is None:
            continue
        # O36: every scored row has the Omniscience leaf.
        observations = {**row["evidence"]["observations"], "omniscience": q.Observation(row["evidence"]["provenance"]["omniscience"]["abstentionPenalisedZ"])}
        primary[row["id"]] = value
        penalised[row["id"]] = anchor_math.value_score(per_row[row["id"]]["api"]["costScore"], q.summarize(observations).displayed, BETA)
    return {"rule": "z_pen = max(0, I)", "rankChanges": diagnostics.paired_rank_change(primary, penalised)}


def _gdpval_logistic_sensitivity(rows: list[dict], per_row: dict) -> dict:
    """E181: ranks per basis with the GDPval-AA leaf mapped by the logistic win probability against AA's anchor."""

    result = {"rule": "z = 100 / (1 + 10^((1600 - E) / 400)) against AA's pinned anchor; every other input fixed"}
    for basis in BASES:
        primary, logistic = {}, {}
        for row in rows:
            value = per_row[row["id"]][basis]["value"]
            if value is None:
                continue
            # O36: every scored row has the GDPval-AA leaf.
            published = row["evidence"]["provenance"]["gdpval"]["evidence"]["publishedValue"]
            observations = {**row["evidence"]["observations"], "gdpval": q.Observation(q.gdpval_logistic_z(published))}
            primary[row["id"]] = value
            logistic[row["id"]] = anchor_math.value_score(per_row[row["id"]][basis]["costScore"], q.summarize(observations).displayed, BETA)
        result[basis] = {"rankChanges": diagnostics.paired_rank_change(primary, logistic)}
    return result


def _z_by_leaf(rows: list[dict]) -> dict:
    return {leaf.key: [row["evidence"]["observations"][leaf.key].z for row in rows if leaf.key in row["evidence"]["observations"]] for leaf in q.LEAVES}


def _independent_quality(rows: list[dict]) -> dict:
    """Q_ind = the mean z of the independently executed leaves (Bug Hunt alone since O37 moved Terminal-Bench to AA's
    run) on the matched panel: rows with every such leaf."""

    independent = {}
    for row in rows:
        values = row["evidence"]["observations"]
        if all(leaf.key in values for leaf in INDEPENDENT_LEAVES):
            independent[row["id"]] = sum(values[leaf.key].z for leaf in INDEPENDENT_LEAVES) / len(INDEPENDENT_LEAVES)
    return independent


def _quality_agreement(rows: list[dict]) -> dict:
    """E62 (a): Kendall tau-b between observed quality and the independent-only quality on the matched panel."""

    independent = _independent_quality(rows)
    observed = {row["id"]: row["summary"].displayed for row in rows if row["id"] in independent}
    return diagnostics.agreement(observed, independent, label="quality agreement (matched-panel sensitivity)")


def _substitution_agreement(rows: list[dict], per_row: dict) -> dict:
    """E62 (b): tau-b between displayed value and value with Q_ind in place of quality (cost, anchors, basis, route fixed)."""

    independent = _independent_quality(rows)
    result = {}
    for basis in BASES:
        displayed = {row_id: per_row[row_id][basis]["value"] for row_id in independent}
        substituted = {row_id: anchor_math.value_score(per_row[row_id][basis]["costScore"], independent[row_id], BETA) for row_id in independent}
        result[basis] = diagnostics.agreement(displayed, substituted, label=f"quality-substitution value agreement, {basis} basis (matched-panel sensitivity)")
    return result


AA_LEAVES = tuple(leaf for leaf in q.LEAVES if leaf.source == "aa")
INDEPENDENT_LEAVES = tuple(leaf for leaf in q.LEAVES if leaf.source == "independent")


def _disjoint_agreement(rows: list[dict]) -> dict:
    """E71 (c): tau-b between AA-executed-only quality and independently-executed-only quality on the matched panel."""

    independent = _independent_quality(rows)
    aa_only = {}
    for row in rows:
        values = row["evidence"]["observations"]
        observed = [leaf for leaf in AA_LEAVES if leaf.key in values]
        if row["id"] in independent and observed:
            aa_only[row["id"]] = sum(leaf.weight * values[leaf.key].z for leaf in observed) / sum(leaf.weight for leaf in observed)
    result = diagnostics.agreement(aa_only, independent, label="disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking)")
    result["retainedLeaves"] = {"aaExecuted": {leaf.key: leaf.weight for leaf in AA_LEAVES}, "independent": {leaf.key: 100.0 / len(INDEPENDENT_LEAVES) for leaf in INDEPENDENT_LEAVES}}
    return result


# E15: the workday-feasible multiple re-solves the route's capacity program with consumption only in a pre-registered
# 40-hour week. No route records an evidenced quota schema, so there is no program to re-solve; a route that records one
# fails the build until the capacity program (E70, E117) exists, rather than being skipped silently.
WORKDAY_RULE = "capacity program re-solved with consumption allowed only in a 40-hour week (8 h x 5 days, versioned calendar, E117); diagnostic, never scored"


def workday_status(selected: dict | None) -> dict:
    """E15: the workday-feasible Plan multiple's status for the selected route."""

    if selected is None:
        return {"status": "not applicable: no Plan route selected", "rule": WORKDAY_RULE}
    route = selected["route"]
    if route.get("quotaSchema"):
        raise ValueError(f"{route['id']}: a recorded quota schema needs the E70 capacity program and the E15 workday solve")
    return {"status": "not evaluated: no evidenced quota schema for this route", "rule": WORKDAY_RULE}


# E166: what the selected measurement's API-priced amount measures, so a displayed amount never reads as capacity it
# does not establish. API-fallback rows publish no Plan amount.
AMOUNT_KINDS = {
    "transfer": "assumed API-equivalent consumption (owner-named transfer)",
    "identified": "identified target-workload capacity",
    "capacity": "measured-workload capacity",
    "observed": "observed eligible consumption (capacity not established)",
}
AMOUNT_TARGETS = {"transfer": "assumed consumption", "identified": "target-workload capacity", "capacity": "measured-workload capacity", "observed": "measured-workload consumption"}
NO_TARGET_LINEAGE = "not derivable: the target solution's cash lineage is not established"


def _amount_derivation(kind: str, route: dict, multiple: float, gross: float) -> tuple[float | None, str]:
    """E168: an amount and how it was derived; M x F reproduces an amount only within one object."""

    if kind == "transfer":
        return (multiple * gross if math.isfinite(gross) else None), "authorised assumption: the donor's multiple times this route's cash"
    if kind == "identified":
        if route.get("targetCapacityUsd") is not None:
            return float(route["targetCapacityUsd"]), "capacity solver projection (U_W*)"
        if route.get("paymentRule") == "fixed" and math.isfinite(gross):
            return multiple * gross, "valid multiplication: fixed cash, U_W* = M_W x F_0"
        return None, NO_TARGET_LINEAGE
    if route.get("apiEquivalentUsd") is not None:
        kind_of_numerator = str(route.get("numeratorKind", "kind not recorded")).replace("_", " ")
        return float(route["apiEquivalentUsd"]), f"measurement record: its recorded numerator U_obs = M_obs x F_obs ({kind_of_numerator})"
    return (multiple * gross if math.isfinite(gross) else None), "measurement identity: U_obs = M_obs x F_obs"


def plan_amount(selected: dict | None, workload: str | None = None) -> dict | None:
    """E166/E168: the selected measurement's amount with its kind, cash, statuses and lineage."""

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
    amount, derivation = _amount_derivation(kind, route, plan_routes.comparison_multiple(route), gross)
    return {
        "amountKind": AMOUNT_KINDS[kind],
        "amountTarget": AMOUNT_TARGETS[kind],
        "amountUsd": amount,
        "derivation": derivation,
        "feePeriod": period,
        "subscriptionCashUsd": route.get("planPriceUsd"),
        "additionalCashUsd": float(route.get("additionalCashUsd") or 0.0),
        "grossCashUsd": gross if math.isfinite(gross) else None,
        "workload": f"scored workload {workload}" if kind == "identified" else route.get("measurementWorkload", "the route's measurement workload"),
        "measurementObjectId": selected.get("measurementObjectId", route["id"]),
        "capacitySolutionId": route.get("capacitySolutionId") if kind == "identified" else None,
        "cashObjectId": f"{route['id']}:{period} cash",
        "purchasePolicyId": route.get("purchasePolicy", "subscription fee for the fee period, no additional cash declared"),
        "capacityStatus": selected.get("measurementCapacityStatus"),
        "valuationStatus": selected.get("valuation"),
        "donorRouteId": selected.get("donorRouteId"),
        "interpretationLabel": f"{AMOUNT_KINDS[kind]}, API-priced USD per {period}",
    }


def _row_json(row: dict, scores: dict, ranks: dict, alternatives: list[dict]) -> dict:
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
        # E170: the valuation-basis gate's outcome for this row's AA cost (O29 governs a price not in force at V).
        "valuationGate": row["valuationGate"],
        "tariffStatus": row["valuationGate"]["outcome"],
        # Outputs item 4: AA's Index figures for the exact configuration (diagnostics only, never scored).
        "indexDiagnostics": cost_diagnostics.index_diagnostics(row["page"]),
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
            "amount": plan_amount(selected, row["cost"]["workload"]),
            "workday": workday_status(selected),
            "routeAlternatives": alternatives,
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


def scenario_panel(assembled: dict, basis: str, *, measurement: bool = False, transfers: bool = True, harness: float | None = None) -> list[scenarios.RowInputs]:
    """The declared panel for one basis (E96): rows with a cost on the main workload, in a fixed order.

    With ``measurement`` (the E162 stream), a leaf whose source documents a 95%
    confidence interval (Terminal-Bench's published half-width) is drawn inside that
    interval under a conventional kernel (E165): uniform with the arcsine
    alternative, never assumed normal, clipped to the leaf's domain. With
    ``harness`` (the E19 band width), Bug Hunt is drawn inside the harness-mismatch
    band centred on its observed score, a specification stress for S2 only.
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
            low, high = max(0.0, z - half), min(100.0, z + half)
            # E182: an interval clipped off-centre keeps the published point as its median.
            family, params = ("uniform", (low, high)) if math.isclose(z - low, high - z) else ("split-uniform", (low, z, high))
            leaves["terminalBench"] = scenarios.Kernel(family, params, "endpoint-heavy", scenarios.INTERVAL_RANGE)
        if harness is not None:
            for key in agent_run_leaves(row):
                z = observations[key].z
                leaves[key] = scenarios.Kernel("uniform", (max(0.0, z - harness / 2.0), min(100.0, z + harness / 2.0)), "endpoint-heavy", scenarios.SPECIFICATION_STRESS)
        panel.append(scenarios.RowInputs(row["id"], leaves, _cost_kernel(row, cost), row["summary"].provisional))
    return panel


def scenario_hash(assembled: dict, frozen: dict, *, n: int, seed: int) -> str:
    """Identity of every scenario input: panels, kernels, anchors, beta, scenario count and seed."""

    payload = {
        "beta": BETA,
        "n": n,
        "seed": seed,
        "anchors": {basis: frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis] for basis in BASES},
        "harnessBand": harness_band(assembled["tb4Rows"])["width"],
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


# E19/E227: Bug Hunt and DeepSWE run each lab's model in that lab's own agent (and so does a tbench.ai Terminal-Bench gap
# fill; AA's own Terminal-Bench run uses one harness, O37), so a named S2 branch draws those leaves inside a harness-mismatch
# band whose width is the median spread of one configuration's Terminal-Bench score across agents on tbench.ai (pre-registered).
HARNESS_BAND_RULE = (
    "width = median over leaderboard configurations listed under two or more agents of (highest - lowest resolution rate, "
    "percentage points); each agent-run leaf (Bug Hunt, DeepSWE, and Terminal-Bench when it is a tbench.ai gap fill rather "
    "than AA's single-harness run, O37) drawn uniformly within the band centred on its observed score (E227); S2 "
    "specification stress, never in Θ"
)


def agent_run_leaves(row: dict) -> list[str]:
    """E227/O37: the observed leaves scored in a lab's own agent, which the harness band stresses."""

    evidence = row["evidence"]
    agent_tb = (evidence["provenance"].get("terminalBench") or {}).get("agent") not in (None, DEFAULT_TB_HARNESS)
    return [key for key in ("deepswe", "bugHunt", "terminalBench") if key in evidence["observations"] and (key != "terminalBench" or agent_tb)]
# E34 and E122: the other named S2 branches, unevaluable from the captured evidence (stated, never silently skipped).
CACHE_BRANCH = {
    "id": "cache-hit variation (E34)", "stratum": "S2", "status": "unevaluable",
    "reason": "AA's published cost embeds its cache-pricing protocol; varying the cache-hit rate needs each basket component's cache-read and uncached-input demand, which AA publishes only for the whole Index (E157)",
}
PRICE_RULE_BRANCH = {
    "id": "first-party list versus cross-provider median price rule (E122)", "stratum": "S2", "status": "unevaluable",
    "reason": "AA publishes one price per configuration under its own rule; the alternative rule's prices are not captured",
}


def harness_band(tb4_rows: list[dict]) -> dict:
    """E19: the pre-registered harness-mismatch band from same-configuration cross-agent spreads, or why it is unevaluable."""

    by_configuration = {}
    for item in tb4_rows:
        if item.get("resolutionRatePct") is not None:
            by_configuration.setdefault(item["model"], {})[item.get("agent")] = item["resolutionRatePct"]
    spreads = {model: max(rates.values()) - min(rates.values()) for model, rates in sorted(by_configuration.items()) if len(rates) >= 2}
    if not spreads:
        return {
            "id": "Bug Hunt harness band (E19)", "stratum": "S2", "rule": HARNESS_BAND_RULE, "status": "unevaluable", "spreads": {}, "width": None,
            "reason": "the captured tbench.ai leaderboard lists no configuration under two or more agents, so no cross-agent spread exists",
        }
    return {"id": "Bug Hunt harness band (E19)", "stratum": "S2", "rule": HARNESS_BAND_RULE, "status": "evaluated", "spreads": spreads, "width": statistics.median(spreads.values())}


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
    band = harness_band(assembled["tb4Rows"])
    if band["width"] is not None:
        band["results"] = {}
        for basis in BASES:
            anchors = frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis]
            run = scenarios.shares(scenario_panel(assembled, basis, transfers=False, harness=band["width"]), "S2", n, seed + len(SCENARIO_RUNS), anchors, BETA)
            if basis == "plan":
                run["transfers"], run["excluded"] = "off", [{"row": row_id, "reason": TRANSFER_EXCLUSION} for row_id in excluded]
            band["results"][basis] = run
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
        "namedBranches": [band, CACHE_BRANCH, PRICE_RULE_BRANCH],
        "barLabels": bar_labels(assembled, frozen, seed=seed, batch=n),
    }


def bar_labels(assembled: dict, frozen: dict, *, seed: int, batch: int) -> list[dict]:
    """E100/E112: kernel-robust scenario-supported cheapest labels for each pinned bar on the API basis."""

    panel = scenario_panel(assembled, "api")
    boxes = api_boxes(assembled)
    # E147: the compiled dependency graph must be the registered kernel-check object, or the build fails.
    if any(len(component) > 1 for component in scenarios.dependency_components(panel)):
        raise ValueError(f"compiled dependency graph differs from the registered kernel-check object ({REGISTERED_DEPENDENCY})")
    blocked = {row["id"] for row in assembled["rows"] if row["valuationGate"]["outcome"] == GATE_NOT_IN_FORCE}
    labels = []
    for reference in frozen["barReferences"]:
        bar = _bar_reference(reference)
        # E186: a blocker is never a candidate.
        candidates = [item for item in intervals.cheapest_above_bar(boxes, bar)["possibleCheapest"] if item not in blocked]
        results = {}
        for candidate in candidates:  # interval rows are main-workload rows with a cost, so all are panel members
            result = scenarios.kernel_robust_cheapest(panel, candidate, reference["level"], seed, batch=batch)
            if result["label"] and not blocker_safe(candidate, bar, boxes, blocked):
                result = {**result, "label": False, "reading": BLOCKER_UNRESOLVED}
            results[candidate] = result
        labels.append({"reference": reference["id"], "level": reference["level"], "status": "evaluated", "candidates": results})
    return labels


BLOCKER_UNRESOLVED = "scenario frequency passes; superseded-price blocker unresolved"

DUAL_RUN_FILE = "v3_dual_run.json"


def dual_run(assembled: dict, previous: dict, current: dict) -> dict:
    """O12/E197: a re-anchoring scores the same evidence on the previous and the new anchor objects, side by side.

    Each row's cost score, value and rank are published under both anchor versions, and each bar's result under
    both bar objects (a reference-policy transition, E156), so the migration's effect is separated from any change
    in evidence.
    """

    old, new = score(assembled, previous), score(assembled, current)
    fields = ("costScore", "value", "rank")
    rows = [
        {"row": before["id"], **{basis: {"previous": {field: before[key][field] for field in fields}, "current": {field: after[key][field] for field in fields}}
                                 for basis, key in (("api", "api"), ("plan", "planScore"))}}
        for before, after in zip(old["rows"], new["rows"])
    ]
    bars = {basis: {"previous": old["intervals"][basis].get("bars", []), "current": new["intervals"][basis].get("bars", [])} for basis in ("api", "plan")}
    return {"previousAnchorVersion": previous["anchorVersion"], "anchorVersion": current["anchorVersion"], "rows": rows, "bars": bars}


def blocker_safe(candidate: str, bar: intervals.Reference, boxes: list[intervals.Box], blocked: set) -> bool:
    """E186: no superseded-price blocker can qualify at the bar and be no dearer than the candidate in any state.

    Over independent boxes, some state has Q_b >= the bar and C_b <= C_i exactly when b's best quality reaches the bar
    level (E192) and b's lowest cost reaches the candidate's highest; a blocker without a constructible box is never safe.
    """

    by_row = {box.row: box for box in boxes}
    if any(row_id not in by_row for row_id in blocked):
        return False
    own = by_row[candidate]
    for row_id in blocked:
        box = by_row[row_id]
        if box.q_high >= bar.q_low and box.c_low <= own.c_high:
            return False
    return True


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
    "frontierCapture": ("aa_frontier_capture.json", "browser capture of AA's Intelligence Index vs cost chart from public tooltips (frontier membership, E195; unevaluated cheaper siblings, E201)"),
    "roster": ("aa_mapping.json", "editorial roster: AA frontier and near-frontier families plus every configuration with exact DeepSWE and Bug Hunt results (O31)"),
    "bugHuntScoreboard": ("bug_hunt_scoreboard.json", "the owner's combined scoreboard at the pinned commit (O31 roster check)"),
    "planRoutes": ("plan_cost_routes.json", "editorial Plan evidence registry"),
    "priceRecords": ("price_records.json", "editorial E141 price-record registry (superseded and promotional tariffs)"),
    "leafEvidence": ("leaf_evidence.json", "editorial supplementary leaf evidence and the exhaustive-search log (O36)"),
    "cognitionFrontierCode": ("cognition_frontiercode.json", "Cognition's FrontierCode leaderboard data (https://cognition.com/data/frontiercode-leaderboard/data.json), captured unchanged (O37)"),
}
CAPTURE_FIELDS = ("capturedAt", "observedAt", "snapshotDate", "asOf", "frozenAt")


def load_documents(data: Path) -> dict:
    documents = {key: json.loads((data / relative).read_text()) for key, (relative, _extractor) in EVIDENCE_FILES.items()}
    plan_routes.check_report_window(documents["planRoutes"])
    plan_routes.check_allocation_regimes(documents["planRoutes"])
    plan_routes.check_report_independence(documents["planRoutes"])
    return documents


def evidence_bundle(data: Path) -> dict:
    """E159: content hashes, capture times and extractors of the release's input artifacts (plus the anchor object)."""

    artifacts = []
    for key, (relative, extractor) in [*EVIDENCE_FILES.items(), ("anchors", (FROZEN_FILE, "valuerank.value_v3 freeze"))]:
        content = (data / relative).read_bytes()
        document = json.loads(content)
        # The roster is a bare list with no capture time of its own.
        captured = next((document[field] for field in CAPTURE_FIELDS if isinstance(document.get(field), str)), None) if isinstance(document, dict) else None
        artifacts.append({"key": key, "artifact": f"data/{relative}", "sha256": hashlib.sha256(content).hexdigest(), "capturedAt": captured, "extractor": extractor})
    return {
        "artifacts": artifacts,
        "bundleHash": hashlib.sha256("".join(item["sha256"] for item in artifacts).encode()).hexdigest(),
        "rebuild": "every published output is rebuilt from these artifacts at the pinned publication clock (npm run verify:docs), never from live pages",
    }


RETAINED_REASON = "Exact AA DeepSWE and eligible Bug Hunt overlap"


def configuration(row: dict) -> dict:
    """A ranked score row's AA identity and whether it is ranked as a frontier or near-frontier family (E187)."""

    return {
        "id": row["id"], "name": row["name"], "family": row.get("family") or row["name"], "effort": row.get("aaVariant"), "aaSlug": row["aaSlug"],
        "aaNote": row.get("aaFrontierFootnote"),
        "frontierFamily": any(reason != RETAINED_REASON for reason in row.get("rankingInclusionReasons") or []),
        "familyPrimary": row.get("familyPrimary", True),
    }


def configurations_from_scores(scores: dict) -> list[dict]:
    """The ranked cohort (fixed cohort policy: the ranking-eligible rows, in table order) with each AA identity."""

    return [configuration(row) for row in scores["models"] if row.get("rankingEligible") is True]


def scenario_seed(release_day: date) -> int:
    return int(release_day.strftime("%Y%m%d"))


def build(configurations: list[dict], data: Path, *, release_day: date) -> dict:
    """The v3 section of scores.json for this release."""

    frozen = json.loads((data / FROZEN_FILE).read_text())
    assembled = assemble_for_release(configurations, load_documents(data), frozen, release_day=release_day)
    scored = score(assembled, frozen)
    scored["evidenceBundle"] = evidence_bundle(data)
    scenario_path = data / SCENARIO_FILE
    document = json.loads(scenario_path.read_text()) if scenario_path.exists() else None
    seed = document["seed"] if document else scenario_seed(release_day)
    count = document["scenarios"] if document else SCENARIO_COUNT
    return attach_scenarios(scored, document, scenario_hash(assembled, frozen, n=count, seed=seed))


def main(argv: list[str] | None = None, *, data: Path = DATA) -> int:
    parser = argparse.ArgumentParser(description="ValueRank v3: freeze anchors, run the scenario engine, or compare two anchor versions")
    parser.add_argument("command", choices=("freeze", "scenarios", "dual-run"))
    parser.add_argument("--scenarios", type=int, default=SCENARIO_COUNT)
    parser.add_argument("--previous", type=Path, help="dual-run: the previous anchor object (a v3_frozen.json)")
    args = parser.parse_args(argv)
    scores = json.loads((data / "scores.json").read_text())
    release_day = utcnow().date()
    configurations, documents = configurations_from_scores(scores), load_documents(data)
    if args.command == "freeze":
        document = freeze(assemble(configurations, documents, release_day=release_day), frozen_at=release_day.isoformat())
        target = data / FROZEN_FILE
    elif args.command == "dual-run":
        if args.previous is None:
            parser.error("dual-run needs --previous")
        frozen = json.loads((data / FROZEN_FILE).read_text())
        document = dual_run(assemble_for_release(configurations, documents, frozen, release_day=release_day), json.loads(args.previous.read_text()), frozen)
        target = data / DUAL_RUN_FILE
    else:
        frozen = json.loads((data / FROZEN_FILE).read_text())
        assembled = assemble_for_release(configurations, documents, frozen, release_day=release_day)
        document = run_scenarios(assembled, frozen, n=args.scenarios, seed=scenario_seed(release_day))
        target = data / SCENARIO_FILE
    target.write_text(json.dumps(document, indent=2, ensure_ascii=False, default=_json_default) + "\n")
    print(json.dumps({"wrote": str(target.relative_to(data.parent)), "command": args.command}))
    return 0


def _json_default(value):
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


if __name__ == "__main__":
    sys.exit(main())
