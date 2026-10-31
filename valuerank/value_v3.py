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
import re
import statistics
import sys
from datetime import date, datetime, time, timezone
from pathlib import Path

from valuerank import anchors as anchor_math
from valuerank import basket
from valuerank import cost_diagnostics
from valuerank import diagnostics
from valuerank import exact_match
from valuerank import intervals
from valuerank import plan_admission
from valuerank import plan_routes
from valuerank import quality as q
from valuerank import scenarios
from valuerank.clock import utcnow
from valuerank.paths import DATA, ROOT
from valuerank.plan_costs import COST_WEIGHT_PCT

METHODOLOGY_VERSION = "3.0.0"
BASKET_VERSION = "SDLC basket v1"
BETA = COST_WEIGHT_PCT / 100.0
BASES = ("api", "plan")
TB4_HALF_WIDTH_PCT = 0.05  # tbench.ai resolution rates are published to 0.1 percentage point
BUG_HUNT_HALF_WIDTH = 0.05  # owner means of bugs fixed are published to 0.1 bug
# O136: the v5 successors' page fields (FrontierCode 2.0, HLE-Diamond, CritPt v2 hard subset, Terminal-Bench-Science).
FRACTION_LEAVES = {
    "frontierCode": "frontierCode20",
    "automationBench": "automationBenchPartialScore",
    "lcr": "lcr",
    "hle": "hleDiamond",
    "tbScience": "terminalBenchScience",
    "critpt": "critptAgenticHard",
}
CHART_SOURCES = {slug: f"AA {basket.COMPONENT_LABELS[slug]} total cost chart (labels rounded to USD 1)" for slug in basket.CHART_COMPONENTS}
DEFAULT_TB_HARNESS = "mini-SWE-agent"  # E125/O37: AA's Terminal-Bench harness; a leaf on any other agent is a gap fill
SCENARIO_COUNT = 10_000
SCENARIO_RUNS = (("S0", False), ("S1", False), ("S2", False), ("S1", True), ("S1M", False), ("S1T", False))
SAMPLING_STREAM = "S1T"  # O39: benchmark sampling noise, independent-task approximation (never a label)
# O39: each leaf's sampling unit, the published task count of the run the leaf reads (AA's evaluation pages and
# methodology; FrontierCode 1.1 Main's 100 tasks; Bug Hunt's 105 planted bugs).
LCR_TASKS = 100  # AA-LCR v1.1's documents; v5 runs it outside the Index, so it is no longer a basket component (O137)
SAMPLING_TASKS = {
    "frontierCode": basket.INDEX_SDLC_TASKS["frontiercode-2-0"], "terminalBench": basket.INDEX_SDLC_TASKS["terminalbench-4-0"],
    "bugHunt": 105, "automationBench": basket.INDEX_SDLC_TASKS["automationbench-aa"], "lcr": LCR_TASKS,
    "tbScience": basket.INDEX_SDLC_TASKS["terminal-bench-science"], "hle": basket.INDEX_RESIDUAL_TASKS["hle-diamond"],
    "critpt": basket.INDEX_RESIDUAL_TASKS["critpt-v2-hard"], "omniscience": basket.INDEX_RESIDUAL_TASKS["omniscience"],
    # O53-O55: AI Coding Daily's six graded projects (judged points read as a binomial share, an assumption). Vals
    # publishes a standard error per record, which the stream reads instead; LiveBench 2.0 Overall is read per category.
    "aiCodingDaily": 6,
}
# O61, E264, O67: LiveBench 2.0 Overall is the release's weighted mean of seven category means, so its noise is the
# weighted mean of seven binomial category draws. Counts are LiveBench's published task counts; Reasoning and Data Analysis publish only their parts (4
# and 3), each holding several short questions, so reading them as 4 and 3 trials overstates their noise (the wide reading).
LIVEBENCH_CATEGORY_TASKS = {"long_agentic": 18, "reasoning": 4, "coding": 29, "browser": 25, "data_analysis": 3, "research": 22, "design": 25}
# O39: GDPval-AA is a fitted Elo with no task-level outcome; AA's model page displays each configuration's rating interval
# without its level, so the stream reads the row's own interval as a 95% normal interval (I60 M2): an assumption,
# labelled. A row without a captured interval takes the -26/+26 width AA displayed for Claude Opus 5.5 on 2026-10-20.
GDPVAL_RATING_SD = 26.0 / 1.96
GDPVAL_SOURCE = "AA GDPval-AA v2.1 Elo as displayed on AA's model page at the capture (E90, O70)"
SAMPLING_ASSUMPTIONS = (
    "tasks are independent and each leaf's score is a mean over its published task count (plug-in binomial with the proportion (k + 1/2) / (n + 1), I28); attempts averaged within a task and tasks shared across models are ignored, so the noise is approximate",
    "GDPval-AA: each row's rating interval as AA's model page displays it, read as a 95% normal interval (AA states no level), SD = half-width / 1.96",
    "AA-Omniscience: each of 6,000 questions scores +1, 0 or -1, with the shares from AA's accuracy and hallucination rate",
    "Vals boards (Vibe Code Bench v1.1, Code Migration v1.1): Vals' published standard error per record, read as the leaf's SD",
    "AI Coding Daily: judged points over its six graded projects read as a binomial share of 60 points (an assumption; the board publishes no error)",
)
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


def track_file(name: str, track: str) -> str:
    """O53: each ranking keeps its own anchor object and scenario run; the default ranking keeps the original names."""

    return name if track == q.DEFAULT_TRACK else name.replace(".json", f"_{track}.json")


# --------------------------------------------------------------------------
# 1. Evidence
# --------------------------------------------------------------------------


# O36: a leaf the primary source lacks is taken, in this order, from another independent party that ran the same
# benchmark version on the exact configuration, else from the model provider's own published result (a provider claim).
SUPPLEMENT_ORDER = ("aa_recapture", "independent", "model_provider_claim")
LEAF_LABELS = {key: leaf.label for key, leaf in q.ALL_LEAVES.items()}
SUPPLEMENT_UNITS = {"percent": lambda value: q.percent_z(value), "fraction": lambda value: q.fraction_z(value),
                    "fixedOf105": lambda value: q.bug_hunt_z(value, BUG_HUNT_HALF_WIDTH)}
LEAF_SEARCH_MAX_AGE_DAYS = 7


# E237: the benchmark version a gap fill must state (O36: "the same benchmark version on the exact configuration").
SUPPLEMENT_VERSIONS = {"bugHunt": "Bug Hunt Bench", "frontierCode": "FrontierCode 1.1", "terminalBench": "Terminal-Bench 4.0"}


def check_comparability(entry: dict) -> None:
    """E237: a gap fill records the benchmark version (which must be the leaf's) and the metric it reports, or the build fails."""

    required = SUPPLEMENT_VERSIONS.get(entry["leaf"], LEAF_LABELS[entry["leaf"]])
    if entry.get("benchmarkVersion") != required or not entry.get("metric"):
        raise ValueError(f"{entry['modelId']}: the {entry['leaf']} gap fill must state benchmark version {required!r} and its metric (E237)")


def leaf_supplements(documents: dict) -> dict:
    """O36: the eligible supplementary observations per (model, leaf), best source first; Terminal-Bench provider claims
    recorded in the tbench.ai capture count as provider claims."""

    evidence = documents.get("leafEvidence") or {}
    entries = list(evidence.get("supplements", []))
    registry = evidence.get("sourceRegistry") or {}
    for entry in entries:
        check_comparability(entry)
        # E239: another party's or a newer AA result counts only from a source registered for that leaf; a provider claim
        # is the model provider's own document. A new source enters by a registry update, as E225 does for agents.
        if entry["sourceType"] != "model_provider_claim" and entry.get("publisher") not in registry.get(entry["leaf"], []):
            raise ValueError(f"{entry['modelId']}: {entry.get('publisher')!r} is not a registered {entry['leaf']} source (E239)")
    entries += [{"modelId": claim["cohortModelId"], "leaf": "terminalBench", "value": claim["valuePct"], "unit": "percent", "sourceType": "model_provider_claim",
                 "configuration": claim.get("evaluatedModel"), "url": claim.get("sourceUrl"), "publishedOn": claim.get("publishedOn"), "publisher": claim.get("publisher"),
                 "artifact": "tb4", "locator": f"providerClaims[claimId={claim.get('claimId')}].valuePct"}
                for claim in documents["tb4"].get("providerClaims", []) if claim.get("eligibleForRanking") is True]
    chosen = {}
    for entry in sorted(entries, key=lambda item: SUPPLEMENT_ORDER.index(item["sourceType"])):
        chosen.setdefault((entry["modelId"], entry["leaf"]), entry)
    return chosen


def track_records(documents: dict) -> dict:
    """O53-O55: the added software-engineering leaves' exact-configuration records, keyed (model, leaf)."""

    tracks = documents.get("sweTracks") or {"sources": {}, "records": []}
    # O122: the coding-specific share reads LiveBench's release weights, so a record on other weights stops the build.
    for record in tracks["records"]:
        if record["leaf"] == q.LIVEBENCH and record.get("weights") and record["weights"] != q.LIVEBENCH_CATEGORY_WEIGHTS:
            raise ValueError(f"{record['modelId']}: LiveBench category weights {record['weights']} differ from the release's (O67, O122)")
    return {(record["modelId"], record["leaf"]): {**record, "sourceMeta": tracks["sources"][record["leaf"]]} for record in tracks["records"]}


TRACK_UNITS = {"percent": q.percent_z, "points of 60": q.aicd_z}


def leaf_evidence(model_id: str, effort: str | None, page: dict, tb4_rows: list[dict], bug_hunt: dict | None,
                  supplements: dict | None = None, tracks: dict | None = None) -> dict:
    """Exact-configuration observations for the quality leaves, with provenance, evidence locators (E159) and the clipping audit (E110)."""

    observations, provenance, audit = {}, {}, []

    def add(key: str, raw, observation: q.Observation, source: dict, artifact: str, locator: str) -> None:
        check = q.clip_audit(key, raw)
        if not check["domainValid"]:
            raise ValueError(f"{model_id}: {key} value {raw!r} is outside its documented domain")
        observations[key] = observation
        provenance[key] = {**source, "evidence": {"artifact": f"data/{EVIDENCE_FILES[artifact][0]}", "locator": locator, "publishedValue": raw}}
        audit.append(check)

    page_path = f"pages[model.slug={page.get('slug')}].model"

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
        # E90, O70: the Elo AA's model page displays at the capture (AA refits it as models join; the Index total does not
        # move with it), with the page's displayed rating interval beside it (I60 M2; its level is not stated).
        add("gdpval", page["gdpval"], q.gdpval_z(page["gdpval"]),
            {"source": GDPVAL_SOURCE, "ratingInterval": page.get("gdpvalInterval"), "intervalLevel": "not stated by AA"}, "snapshot", f"{page_path}.gdpval")
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
        record = (tracks or {}).get((model_id, leaf.key))
        if record is not None:
            meta = record["sourceMeta"]
            add(leaf.key, record["value"], TRACK_UNITS[meta["unit"]](record["value"]),
                {"source": f"{meta['publisher']}: {meta['benchmark']}", "configuration": record.get("sourceLabel"), "effort": record.get("effort"),
                 "harness": record.get("harness") or meta["harness"], "url": meta["url"], "publishedOn": meta["updated"], "stderr": record.get("stderr"), "match": record.get("match"),
                 **({"categories": record["categories"]} if record.get("categories") else {}),
                 **({"weights": record["weights"]} if record.get("weights") else {}),
                 **({"note": record["note"]} if record.get("note") else {}),
                 # I50 M2: a board that lists the configuration more than once names its selection and the other rows.
                 **({"selection": record["selection"], "alternates": record["alternates"]} if record.get("alternates") else {}),
                 **({"cutoffDayRow": record["cutoffDayRow"]} if record.get("cutoffDayRow") else {})},
                "sweTracks", f"records[modelId={model_id}, leaf={leaf.key}].value")
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
    bug_hunt_by_id = {item["modelId"]: item for item in documents["bugHunt"]["models"]}
    supplements, tracks = leaf_supplements(documents), track_records(documents)
    entries = [incomplete_entry(configuration, leaf_evidence(configuration["id"], configuration.get("effort"), pages[configuration["aaSlug"]],
                                                             documents["tb4"]["rows"],
                                                             bug_hunt_by_id.get(configuration["id"]), supplements, tracks))
               for configuration in configurations]
    return [entry for entry in entries if entry is not None]


def check_leaf_searches(incomplete: list[dict], documents: dict, release_day: date, frontier: frozenset = frozenset()) -> None:
    """O36: every leaf a cohort configuration lacks has a logged exhaustive search at most 7 days before the cutoff;
    for a frontier or near-frontier family the log also holds an open-web discovery step whose every candidate is
    resolved (I28)."""

    evidence = documents.get("leafEvidence") or {}
    log = {(item["modelId"], item["leaf"]): item for item in evidence.get("searches", [])}
    for row in incomplete:
        for leaf in row["missing"]:
            entry = log.get((row["id"], leaf))
            if entry is None or (release_day - date.fromisoformat(entry["searchedOn"])).days > LEAF_SEARCH_MAX_AGE_DAYS:
                raise ValueError(f"{row['id']}: no exhaustive search for {leaf} logged within {LEAF_SEARCH_MAX_AGE_DAYS} days of the cutoff (O36)")
            if row["id"] in frontier:
                check_open_web(row["id"], leaf, entry.get("openWeb"), (evidence.get("sourceRegistry") or {}).get(leaf, []))


OPEN_WEB_RESOLUTIONS = ("register", "reject")


def check_open_web(model_id: str, leaf: str, step: dict | None, registry: list) -> None:
    """I28: the open-web discovery step of a listed frontier family's search; a candidate is either a dated registry
    addition (its publisher is now registered for the leaf) or a dated rejection with a reason."""

    if not step or not step.get("queries"):
        raise ValueError(f"{model_id}: the {leaf} search logs no open-web discovery step (I28)")
    for candidate in step.get("candidates", []):
        if candidate.get("resolution") not in OPEN_WEB_RESOLUTIONS or not candidate.get("reason"):
            raise ValueError(f"{model_id}: open-web candidate {candidate.get('url')} for {leaf} is unresolved (I28)")
        if candidate["resolution"] == "register" and candidate.get("publisher") not in registry:
            raise ValueError(f"{model_id}: open-web candidate {candidate.get('url')} for {leaf} awaits its registry addition (I28)")


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
        "leaf": "gdpval", "status": "captured, level unstated",
        "field": "model.gdpvalInterval {lower, upper} on every AA model page (captured since the 2026-10-23 re-capture, O47)",
        "method": "Crowd-BT maximum likelihood with sandwich-estimator confidence intervals (AA methodology, GDPval-AA v2.1)",
        "level": "not stated by the source (the 95% level on AA's methodology page belongs to AA-Briefcase)",
        "stream": "S1T: each row's half-width / 1.96 as its SD (read as a 95% interval, an analyst convention); published beside the leaf in each row's provenance (ratingInterval)",
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
    """E201/O33: same-family configurations AA plots at a lower total Index cost that are not ranked (not plotted on or
    near the frontier with every leaf, O51); ``ranked_efforts`` are the efforts of the family's ranked configurations."""

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


SOURCE_MAX_AGE_DAYS = 30  # O59: non-AA quality evidence, like the end-user report window


def source_clocks(documents: dict) -> list[dict]:
    """O59/O60: each non-AA quality source's capture instant and the source's own last update."""

    tracks = documents.get("sweTracks") or {}
    clocks = [{"source": f"{source['publisher']}: {source['benchmark']}", "artifact": "data/swe_tracks.json",
               "capturedAt": source.get("capturedAt") or tracks.get("capturedAt"), "sourceUpdated": source.get("updated")}
              for source in (tracks.get("sources") or {}).values()]
    scoreboard = documents.get("bugHuntScoreboard") or {}
    if scoreboard:
        clocks.append({"source": "Bug Hunt Bench scoreboard", "artifact": "data/bug_hunt_scoreboard.json", "capturedAt": scoreboard.get("capturedAt"),
                       "sourceUpdated": scoreboard.get("sourceUpdated")})
    tb4 = documents.get("tb4") or {}
    if tb4:
        # I58 M2: the leaderboard scrape's own instant, not the build stamp of the derived file.
        clocks.append({"source": "tbench.ai Terminal-Bench 4.0 leaderboard", "artifact": "data/tb4.json",
                       "capturedAt": (tb4.get("source") or {}).get("capturedAt") or tb4.get("observedAt"), "sourceUpdated": tb4.get("sourceUpdated")})
    cognition = (documents.get("leafEvidence") or {}).get("cognitionCapture")
    if cognition:
        clocks.append({"source": "Cognition: FrontierCode leaderboard", "artifact": cognition["file"], "capturedAt": cognition["capturedOn"],
                       "sourceUpdated": cognition.get("lastModified")})
    # I60 L6: an O68 re-read that found the board unchanged is printed beside the pinned capture's clock.
    rereads = {item["source"]: item for item in (documents.get("sourceRereads") or {}).get("rereads", [])}
    for clock in clocks:
        if clock["source"] in rereads:
            item = rereads[clock["source"]]
            clock["reRead"] = {"at": item["reReadAt"], "result": item["result"], "file": item["file"],
                               **({"lastModified": item["lastModified"]} if item.get("lastModified") else {})}
    return clocks


O71_STAGES = ("plain web search", "Claude's Deep Research", "Silver Bullet's Deep Research")
# I62 L6: the providers an O71 search must cover are derived from the cohort's developers (named as the plans' sellers).
PLAN_PROVIDER = {"Google DeepMind": "Google", "Moonshot AI": "Kimi"}
O71_FROM = "2026-10-25"


def cohort_providers(configurations: list[dict]) -> set[str]:
    return {PLAN_PROVIDER.get(item["developer"], item["developer"]) for item in configurations if item.get("developer")}


def check_o71_search(policy: dict, providers: set[str] = frozenset()) -> None:
    """O71, O75, I61 L3: from O71 on, the all-provider search that sets the cutoff ran all three stages over every cohort
    provider's plans, and records each stage."""

    entries = [entry for entry in policy.get("searchLog") or [] if entry.get("searchedOn") and not entry.get("singleProvider")]
    latest = max(entries, key=lambda entry: entry["searchedOn"], default=None)
    if latest is None or latest["searchedOn"] < O71_FROM:
        return
    stages = tuple(stage.get("stage") for stage in latest.get("stages") or [])
    if stages != O71_STAGES or not all(stage.get("record") and stage.get("outcome") for stage in latest["stages"]):
        raise ValueError(f"the all-provider search of {latest['searchedOn']} does not record the three O71 stages in order (O71, O75)")
    missing = sorted(set(providers) - set(latest.get("providers") or []))
    if missing:
        raise ValueError(f"the all-provider search of {latest['searchedOn']} omits {', '.join(missing)} (O71)")


# Reviewer 74 M1: each first-party plan's seller, by the plan's name in plan_reports.json's listed plans.
PLAN_SELLER = {"Claude": "Anthropic", "ChatGPT": "OpenAI", "Google AI": "Google", "MiMo": "Xiaomi", "Kimi": "Kimi", "MiniMax": "MiniMax"}


def plan_seller(plan: str) -> str | None:
    return next((seller for prefix, seller in PLAN_SELLER.items() if plan.startswith(prefix + " ")), None)


def o71_coverage(policy: dict, configurations: list[dict], listed_plans) -> dict:
    """O71, O75 (reviewer 74 M1): research coverage is keyed by model and plan, not provider. A cell (model, plan) is
    covered by an O71-era search log entry that ran all three stages, names the plan's seller and names the model (efforts
    pool, O87). Returns {"cells": n, "uncovered": [(model, plan)]} over every cohort model's sellers' current plans."""

    plans = [plan for plan in listed_plans if "(" not in plan]
    entries = [entry for entry in policy.get("searchLog") or [] if (entry.get("searchedOn") or "") >= O71_FROM
               and tuple(stage.get("stage") for stage in entry.get("stages") or []) == O71_STAGES]
    cells, uncovered = 0, []
    for model, provider in sorted({(configuration_family(item), PLAN_PROVIDER.get(item["developer"], item["developer"]))
                                   for item in configurations if item.get("developer")}):
        for plan in (plan for plan in plans if plan_seller(plan) == provider):
            cells += 1
            if not any(model in (entry.get("models") or []) and provider in (entry.get("providers") or [])
                       and plan in (entry.get("plans") or plans) for entry in entries):
                uncovered.append((model, plan))
    return {"cells": cells, "uncovered": uncovered}


def check_o71_coverage(policy: dict, configurations: list[dict], listed_plans) -> dict:
    coverage = o71_coverage(policy, configurations, listed_plans)
    if coverage["uncovered"]:
        cells = "; ".join(f"{model} on {plan}" for model, plan in coverage["uncovered"])
        raise ValueError(f"no three-stage O71 search names these cohort model and plan cells (O71, O75): {cells}")
    return coverage


def check_rereads(documents: dict) -> None:
    """I60 L6: an O68 re-read record must name, by hash, the pinned capture the build uses; a record left behind by a
    newer capture stops the build (the tests compare each 'unchanged' result with the re-read file, `reread_matches`)."""

    for item in (documents.get("sourceRereads") or {}).get("rereads", []):
        key, *path = item["pinnedKey"].split(".")
        pinned = documents.get(key) or {}
        for part in path:
            pinned = (pinned or {}).get(part)
        if pinned != item["pinnedSha256"]:
            raise ValueError(f"{item['source']}: the O68 re-read at {item['reReadAt']} was compared with a capture ({item['pinnedSha256'][:12]}) that is not the pinned one ({str(pinned)[:12]})")


def _compared_hash(document: dict, fields: list[str]) -> str:
    return hashlib.sha256(json.dumps({field: document.get(field) for field in fields}, sort_keys=True).encode()).hexdigest()


def reread_matches(item: dict, root: Path = ROOT) -> bool:
    """Whether a re-read file equals the pinned capture: the file hash, or for a scrape the hash of its compared fields
    (recorded from the pinned scrape, which is not committed; checked against it too where it is present)."""

    reread = (root / item["file"]).read_bytes()
    if item["compare"] == "sha256":
        return hashlib.sha256(reread).hexdigest() == item["pinnedSha256"]
    pinned = root / item["pinned"]
    if pinned.exists() and _compared_hash(json.loads(pinned.read_bytes()), item["compare"]) != item["comparedSha256"]:
        return False
    return _compared_hash(json.loads(reread), item["compare"]) == item["comparedSha256"]


def check_bug_hunt_dates(records: list[dict], release_day: date) -> str | None:
    """O69, I60 L3: a Bug Hunt record dated after the cutoff's day stops the build; one dated on the cutoff's day has no
    recorded instant, so it stops too. Returns the newest record date, printed beside the scoreboard's clock."""

    days = [record["reportedOn"] for record in records if record.get("reportedOn")]
    for record in records:
        day = record.get("reportedOn")
        if day and date.fromisoformat(day) >= release_day:
            raise ValueError(f"Bug Hunt record {record['modelId']} is dated {day}, not before the release cutoff's day {release_day} (O69)")
    return max(days) if days else None


def check_source_clocks(clocks: list[dict], release_day: date, cutoff: datetime) -> None:
    """O59: a non-AA source is captured at most 30 days before the cutoff; O60: a capture after the cutoff stands only
    when the source's own last update is dated before the cutoff's day, so the capture shows the board as of the cutoff."""

    for clock in clocks:
        stamp = clock["capturedAt"]
        if not stamp:
            raise ValueError(f"{clock['source']}: no capture instant recorded (O59)")
        if (release_day - date.fromisoformat(stamp[:10])).days > SOURCE_MAX_AGE_DAYS:
            raise ValueError(f"{clock['source']}: captured {stamp[:10]}, more than {SOURCE_MAX_AGE_DAYS} days before the release cutoff {release_day} (O59)")
        # A date-only stamp on the cutoff's day cannot be placed after it.
        after = _instant(stamp) > cutoff if "T" in stamp else date.fromisoformat(stamp) > release_day
        updated = clock["sourceUpdated"]
        if after and not (updated and date.fromisoformat(updated[:10]) < release_day):
            raise ValueError(f"{clock['source']}: captured {stamp} after the release cutoff, and the source's last update "
                             f"({updated or 'not recorded'}) does not predate the cutoff's day (O60)")


# E267: the effort names AA prints; any other parenthesis after a model name is not a recognised form. Since the
# 2026-10-30 capture AA capitalises them and writes the fallback inside the parenthesis ("(Max, Default Fallback)").
AGENT_EFFORTS = "minimal|low|medium|high|xhigh|max"
_KEYED_EFFORT = re.compile(rf" \(\{{'reasoning_effort': '(?P<effort>{AGENT_EFFORTS})'\}}\)\Z")
_PLAIN_EFFORT = re.compile(rf" \((?P<effort>{AGENT_EFFORTS})(?:, default fallback)?\)\Z", re.IGNORECASE)
# O54: the owner stated that AA's effort-less MiMo-V2.6-Pro configuration is high, so a record at high is exact too.
# O140: MiMo-V2.6-Flash has one documented reasoning mode, thinking on by default, which AI Coding Daily's "High" row is.
OWNER_STATED_EFFORT = {"mimo-v2-6-pro": "high", "kimi-k3-1-pro": "max", "mimo-v2-6-flash": "high"}  # O66: Kimi K3.1 Pro at max


def parse_agent_label(label: str) -> dict | None:
    """E267: "<agent> - <model>[ (<effort>)][ ({'reasoning_effort': '<effort>'})][ (with fallback)]", read whole; a label
    naming more than one model (" + ") is never an exact record and parses to None."""

    agent, separator, rest = label.partition(" - ")
    if not separator or " + " in rest:
        return None
    rest = rest.removesuffix(" (with fallback)")
    efforts = []
    for pattern in (_KEYED_EFFORT, _PLAIN_EFFORT):
        if match := pattern.search(rest):
            efforts.append(match["effort"].lower())
            rest = rest[:match.start()]
    if len(set(efforts)) > 1:
        return None
    return {"agent": agent, "model": rest, "effort": efforts[0] if efforts else None}


def exact_agent_records(configuration: dict, agent_records) -> list[str]:
    """E267: the Coding Agent Index records that are this configuration's exact record: one model, the configuration's
    model identity (with or without the "Claude " prefix and the fallback token) and its effort."""

    family = configuration.get("family") or configuration["name"]
    names = {family, family.removeprefix("Claude ")}
    efforts = {configuration.get("effort")}
    if configuration.get("effort") is None and configuration["id"] in OWNER_STATED_EFFORT:
        efforts.add(OWNER_STATED_EFFORT[configuration["id"]])
    found = []
    for label in agent_records:
        parsed = parse_agent_label(label)
        if parsed and parsed["model"] in names and parsed["effort"] in efforts:
            found.append(label)
    return sorted(found)


def agent_safety(record: dict | None) -> dict | None:
    """O63 (owner decision, 2026-10-25): blocked attempts (AA's hard stops) and attempts a fallback model finished, summed
    over the record's components, with the fallback models. Disclosed and flagged; never a cost or quality change."""

    if record is None:
        return None
    safeties = [component.get("safety") for component in record.get("components") or []]
    if any(safety is None for safety in safeties):
        return {"status": "not captured"}
    attempts = sum(component.get("attempts") or 0 for component in record["components"])
    blocked = sum(safety["blocked"] or 0 for safety in safeties)
    fallback = sum(safety["fallback"] or 0 for safety in safeties)
    return {"status": "flagged" if blocked or fallback else "none", "attempts": attempts, "blocked": blocked, "fallback": fallback,
            "fallbackModels": sorted({model for safety in safeties for model in safety["fallbackModels"]})}


def check_agent_manifest(captured: list[dict], manifest: dict) -> None:
    """O64 (I56 M1): a closed world. Every Coding Agent Index row AA lists is registered by its row id in the reviewed
    manifest; a new row, a changed label, a row AA no longer lists or two rows sharing a label stops the build."""

    rows = manifest["rows"]
    labels = [record["label"] for record in captured]
    if duplicates := sorted({label for label in labels if labels.count(label) > 1}):
        raise ValueError(f"AA lists more than one Coding Agent Index row under the label(s) {duplicates} (O64)")
    problems = [f"{record['label']!r} (id {record['id']}) is not in the manifest" for record in captured if record["id"] not in rows]
    problems += [f"id {record['id']} is registered as {rows[record['id']]['label']!r} but AA now labels it {record['label']!r}"
                 for record in captured if record["id"] in rows and rows[record["id"]]["label"] != record["label"]]
    problems += [f"{row['label']!r} (id {row_id}) is registered but AA no longer lists it" for row_id, row in rows.items()
                 if row_id not in {record["id"] for record in captured}]
    if problems:
        raise ValueError("review the Coding Agent Index manifest (O64): " + "; ".join(problems))


def agent_record_for(configuration: dict, mapping: dict, agent_records, manifest: dict | None = None) -> str | None:
    """E267 (I50 H1, I51 M1, I52 M1): the configuration's Coding Agent Index record is derived from the capture: its one
    exact record. A pin is only a recorded choice among several exact records; a pin that is not an exact record, or
    several exact records with no pin, stops the build. No pin can price a row from another configuration's record."""

    exact = exact_agent_records(configuration, agent_records)
    if manifest is not None:
        # O64: the reviewed manifest decides; the E267 grammar is a cross-check, and any disagreement stops the build.
        registered = sorted(row["label"] for row in manifest["rows"].values()
                            if row["classification"] == "exact" and row.get("configurationId") == configuration["id"])
        if registered != exact:
            raise ValueError(f"{configuration['id']}: the manifest registers {registered} as its Coding Agent Index record(s) "
                             f"but the E267 grammar reads {exact} (O64)")
    pin = (mapping.get(configuration["id"]) or {}).get(basket.CODING_AGENT_INDEX)
    if pin is not None and pin not in exact:
        raise ValueError(f"{configuration['id']}: its Coding Agent Index pin {pin!r} is not an exact record; exact: {exact} (E267)")
    if pin is None and len(exact) > 1:
        raise ValueError(f"{configuration['id']}: AA's Coding Agent Index has several exact records {exact}; pin the choice (E267)")
    return pin or (exact[0] if exact else None)


def assemble(configurations: list[dict], documents: dict, *, release_day: date, pinned: list[str] | None = None) -> dict:
    """Evidence, admission, basket costs and Plan routes for every ranked configuration (no anchors yet)."""

    pages = {page["model"]["slug"]: page["model"] for page in documents["snapshot"]["pages"]}
    bug_hunt_by_id = {item["modelId"]: item for item in documents["bugHunt"]["models"]}
    agent_records = {item["label"]: item for item in documents["codingAgents"]["configurations"]}
    chart_rows = {item["slug"]: {row["model"]: row for row in item["rows"]} for item in documents["costCharts"]["evaluations"]}
    mapping = documents["configurationMap"]["rows"]
    manifest = documents["codingAgentsManifest"]
    check_agent_manifest(documents["codingAgents"]["configurations"], manifest)
    agent_labels = {configuration["id"]: agent_record_for(configuration, mapping, agent_records, manifest) for configuration in configurations}
    # E208: a route inherits the token-category mix its source publishes for the measured workload.
    sources = documents["planRoutes"].get("sourceEvidence") or {}
    routes = [
        {**route, "workloadMix": sources[route["sourceEvidenceId"]]["workloadMix"]}
        if "workloadMix" not in route and (sources.get(route.get("sourceEvidenceId")) or {}).get("workloadMix") else route
        for route in documents["planRoutes"]["routes"]
    ]
    # O32: only end-user reports dated in the release's report window count toward admission.
    window = (documents["planRoutes"].get("evidencePolicy") or {}).get("reportingWindow")
    # O91: acknowledged accounting-fault windows apply to controlled measurements as well as to user reports.
    faults = ((documents["planRoutes"].get("evidencePolicy") or {}).get("reportEligibilityProfile") or {}).get("accountingFaultDays") or []
    # E213: one release cutoff; the report window is the 30 days ending on it (the evidence search cutoff is recorded apart).
    if window and window["end"] != release_day.isoformat():
        raise ValueError(f"the report window must end on the release cutoff {release_day} (E213), not {window['end']}")
    # E218: end-user reports are searched up to at most 7 days before the release cutoff, like the cohort capture (E211).
    policy = documents["planRoutes"].get("evidencePolicy") or {}
    searched = policy.get("searchCutoff")
    # I51 L6, I52 L1: the search cutoff is the date of the latest all-provider search in the log, never a free-standing date.
    all_provider = [entry["searchedOn"] for entry in policy.get("searchLog") or [] if not entry.get("singleProvider")]
    if searched and searched != max(all_provider, default=None):
        raise ValueError(f"the search cutoff {searched} is not the date of the latest all-provider search in the search log (E218)")
    # I77 L5: the registry's "as of" date is the evidence search cutoff it was last brought up to, never a stale stamp.
    if searched and documents["planRoutes"].get("asOf") and documents["planRoutes"]["asOf"] != searched:
        raise ValueError(f"the route registry is dated {documents['planRoutes']['asOf']}, not its search cutoff {searched} (E218)")
    check_o71_search(policy, cohort_providers(configurations))
    research_coverage = None
    if any((entry.get("searchedOn") or "") >= O71_FROM for entry in policy.get("searchLog") or []):
        research_coverage = check_o71_coverage(policy, configurations, (documents.get("planReports") or {}).get("listedPlans") or {})
    # O81: the build decides every O71 cell's admission from the report table, and refuses an unsupported report route.
    # O87: cells are keyed by the model (the configuration's AA family), so reports at any effort pool.
    families = {item["id"]: configuration_family(item) for item in configurations}
    allowance_cells = plan_admission.evaluate(documents.get("planReports") or {"reports": []}, policy.get("reportEligibilityProfile") or {}, release_day, families)
    plan_admission.check_routes(documents["planRoutes"]["routes"], allowance_cells, set(families), plan_routes.REPORT_KINDS, families)
    plan_routes.check_same_model_routes(documents["planRoutes"], families)
    change_records = plan_admission.profile_records(policy.get("reportEligibilityProfile") or {})
    plan_admission.check_change_flags(documents["planRoutes"]["routes"], change_records)
    plan_admission.check_change_records(documents["planRoutes"]["routes"], change_records, release_day)
    plan_routes.check_lower_of_routes(documents["planRoutes"])
    plan_routes.check_source_rereads(documents["planRoutes"], release_day)
    # I51 L7: an O46 ceiling is recomputed from its recorded credits, rate and fee, so the stored multiple cannot drift.
    for route in documents["planRoutes"]["routes"]:
        if route.get("evidenceClass") == "provider_quota_ceiling":
            ceiling = route["quotaCredits"] * route["usdPerBillionCredits"] / 1e9 / route["planPriceUsd"]
            if abs(ceiling - route["valueMultiple"]) > 0.0005:
                raise ValueError(f"{route['id']}: the stored multiple {route['valueMultiple']} is not the quota ceiling {ceiling:.4f} (O46)")
    if window and (not searched or (release_day - date.fromisoformat(searched)).days > REPORT_SEARCH_MAX_AGE_DAYS):
        raise ValueError(f"end-user reports were last searched on {searched}, more than {REPORT_SEARCH_MAX_AGE_DAYS} days before the release cutoff {release_day} (E218)")
    # E216: the AA model-page snapshot and the price records are at most 45 days old at the release cutoff (the chart
    # and catalog capture that defines the cohort has its own 7-day gate, E211).
    # The price records decide which tariff is in force at V (E170), so they share the cohort capture's 7-day gate.
    for name, stamp, limit in (("AA model-page snapshot", documents["snapshot"].get("capturedAt"), COST_EVIDENCE_MAX_AGE_DAYS),
                               ("price records", documents["priceRecords"].get("observedAt"), PRICE_RECORD_MAX_AGE_DAYS)):
        if stamp and (release_day - date.fromisoformat(stamp[:10])).days > limit:
            raise ValueError(f"the {name} ({stamp[:10]}) is more than {limit} days old at the release cutoff {release_day} (E216)")
    # O59/O60: the non-AA quality sources have their own capture clock. The cutoff instant is the pinned clock on the
    # release day, otherwise the end of that day.
    now = utcnow()
    clocks = source_clocks(documents)
    check_rereads(documents)
    newest = check_bug_hunt_dates(documents["bugHunt"]["models"], release_day)
    for clock in clocks:
        if clock["source"] == "Bug Hunt Bench scoreboard":
            clock["newestRowDate"] = newest
    check_source_clocks(clocks, release_day, now if now.date() == release_day else datetime.combine(release_day, time.max, tzinfo=timezone.utc))
    # E217: the model pages (costs and AA-run leaves) and the chart that defines the cohort describe one AA state.
    chart, pages_at = (documents.get("frontierCapture") or {}).get("captured_at"), documents["snapshot"].get("capturedAt")
    if chart and pages_at and abs(_instant(chart) - _instant(pages_at)).total_seconds() > CAPTURE_GAP_MAX_DAYS * 86400:
        raise ValueError(f"the AA chart capture ({chart}) and model-page snapshot ({pages_at}) are more than {CAPTURE_GAP_MAX_DAYS} days apart (E217)")
    # I57 M1: the Coding Agent Index and cost-chart captures price the basket, so they describe the same AA state too, and
    # none is taken after the release cutoff (O65: AA data read after the cutoff moves the cutoff and is re-captured).
    cutoff = now if now.date() == release_day else datetime.combine(release_day, time.max, tzinfo=timezone.utc)
    for name, stamp in (("Coding Agent Index capture", (documents.get("codingAgents") or {}).get("capturedAt")),
                        ("cost-chart capture", (documents.get("costCharts") or {}).get("capturedAt")),
                        *((("AA frontier chart capture", chart),) if chart else ())):
        if pages_at and not stamp:
            raise ValueError(f"the {name} carries no capture instant (E217)")
        if stamp and pages_at and abs(_instant(stamp) - _instant(pages_at)).total_seconds() > CAPTURE_GAP_MAX_DAYS * 86400:
            raise ValueError(f"the {name} ({stamp}) and model-page snapshot ({pages_at}) are more than {CAPTURE_GAP_MAX_DAYS} days apart (E217)")
        if stamp and _instant(stamp) > cutoff:
            raise ValueError(f"the {name} ({stamp}) was taken after the release cutoff (O65)")
    price_records = documents["priceRecords"]["records"]
    points = (documents.get("frontierCapture") or {}).get("points", [])
    rows, supplements, tracks = [], leaf_supplements(documents), track_records(documents)
    check_captured_footnotes(documents.get("frontierCapture"), documents.get("aaFootnotes"))
    check_capture_twins(documents.get("frontierCapture"))
    # I89 L4, I90 L6: the editorial roster (the cohort roster O51, the same in every command), not every configuration-map row.
    check_register_subjects(documents.get("aaFootnotes"), {item["id"] for item in documents.get("roster") or []} | {item["id"] for item in configurations})
    check_shared_labels(mapping)
    check_regime_bounds(documents["planRoutes"]["routes"], {item["id"]: pages.get(item["aaSlug"]) for item in configurations}, change_records)
    check_surface_notes(documents, documents.get("aaFootnotes"))
    for configuration in configurations:
        model_id, effort = configuration["id"], configuration.get("effort")
        page = pages.get(configuration["aaSlug"])
        if page is None:
            raise ValueError(f"{model_id}: AA model page {configuration['aaSlug']} is missing from the pinned snapshot")
        # E267: the agent record is derived from the capture; a row without a chart label in the map has no chart cost (flagged).
        labels = mapping.get(model_id) or {}
        evidence = leaf_evidence(model_id, effort, page, documents["tb4"]["rows"], bug_hunt_by_id.get(model_id), supplements, tracks)
        components, reconciliation = row_components(
            page,
            agent_records.get(agent_labels[model_id]),
            {slug: chart_rows.get(slug, {}).get(labels.get(slug)) for slug in basket.CHART_COMPONENTS},
        )
        gate = valuation_gate(page, [item for item in price_records if item["aaSlug"] == configuration["aaSlug"]], documents["snapshot"].get("capturedAt"))
        if gate["outcome"] == GATE_REVALUED:
            components = revalue(components, gate["factor"])
        candidates = plan_routes.route_candidates(model_id, effort, routes, release_day, window=window, faults=faults, families=families)
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
            # O63: AA's safety-refusal outcomes on the row's Coding Agent Index record, disclosed and flagged only.
            "agentSafety": agent_safety(agent_records.get(agent_labels[model_id])),
            "routeSelection": plan_routes.route_selection(candidates),
            # O100, O106: the registered class of every AA note on the row's chart point, model page, Coding Agent Index record
            # and cost-chart rows (and their charts), combined (the build stops on an unregistered note).
            # O109: the notes by surface; the class is combined after admission, from the admitted components only.
            "aaNoteSources": note_sources(configuration, page, agent_records.get(agent_labels[model_id]), documents, labels),
            "aaNote": chart_footnote(configuration, points),
            "admissionTable": plan_routes.admission_table(model_id, effort, routes, release_day, window, faults, families),
        })
    # O36: only configurations with every leaf are ranked; the rest stay listed with their missing leaves and searches.
    incomplete = [entry for entry in (incomplete_entry(row, row["evidence"]) for row in rows) if entry is not None]
    check_leaf_searches(incomplete, documents, release_day, frozenset(row["id"] for row in rows if row.get("frontierFamily")))
    # O41: a listed frontier or near-frontier family keeps its assembled evidence for the separated indicative value.
    listed = [row for row in rows if incomplete_entry(row, row["evidence"]) is not None and row.get("frontierFamily")]
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
    for row in rows + listed:
        row["aaNoteClass"] = admitted_note_class(row, admitted, documents.get("aaFootnotes"))
        row["aaUncountedNotes"] = uncounted_notes(row, admitted, documents.get("aaFootnotes"))
        row["cost"] = basket.row_cost(row["components"], admitted)
        selected = row["routeSelection"]["selected"]
        row["plan"] = plan_routes.plan_cost(row["cost"]["costUsd"], selected)
    return {
        "rows": rows, "admission": admission, "admitted": admitted, "deferred": [{"component": component, "reason": DEFERRED_MIGRATION} for component in deferred],
        "mainWorkload": main, "releaseDay": release_day.isoformat(), "tb4Rows": documents["tb4"]["rows"], "incomplete": incomplete, "listed": listed,
        "cognition": documents.get("cognitionFrontierCode") or {"v1_1": {"data": {}}},
        "sourceClocks": clocks,
        "planAllowanceCells": allowance_cells,
        "planResearchCoverage": research_coverage,
        "gdpvalPrevious": documents.get("aaPreviousCapture"),
        "codingAgents": documents.get("codingAgents"),
        "pages": documents["snapshot"]["pages"],
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
    if assembled["mainWorkload"] != frozen["mainWorkload"] and gained and len(anchor_population(assembled, assembled["admitted"], freezing=True)) < MIN_ANCHOR_REFERENCES:
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


PLAN_ROW_RULE = ("O48: the Plan basis ranks one row per configuration and plan: every plan on which the configuration has an eligible "
                 "(non-diagnostic) route, the route chosen by the official comparator among that plan's candidates (E85, E88); a "
                 "configuration with no eligible route keeps one API-cost fallback row (O13). Rows of one configuration share its quality "
                 "and its API cost, so they differ only by the plan's multiple")
API_FALLBACK_PLAN = "api"


def plan_slug(plan: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", plan.lower()).strip("-")


def plan_variants(assembled: dict) -> dict:
    """O48: the Plan-basis population, one row per configuration and plan (``<configuration>@<plan>``), each carrying the
    configuration's evidence and cost with the plan's selected route; ``configurationId`` names the configuration and
    ``representative`` marks the row on the configuration's own selected route."""

    rows = []
    for row in assembled["rows"]:
        by_plan: dict[str, list] = {}
        for candidate in row.get("routeCandidates", []):
            if candidate["grade"] != "diagnostic":
                # A route without a recorded plan name is its own plan.
                by_plan.setdefault(candidate["route"].get("plan") or candidate["route"]["id"], []).append(candidate)
        chosen = row["routeSelection"]["selected"]
        variants = [(plan, plan_routes.route_selection(candidates)) for plan, candidates in sorted(by_plan.items())] or [(None, row["routeSelection"])]
        for plan, selection in variants:
            selected = selection["selected"]
            rows.append({
                **row,
                "id": f"{row['id']}@{plan_slug(plan) if plan else API_FALLBACK_PLAN}",
                "configurationId": row["id"],
                "planName": plan,
                "routeSelection": selection,
                "plan": plan_routes.plan_cost(row["cost"]["costUsd"], selected),
                "representative": (selected is None and chosen is None) or (selected is not None and chosen is not None and selected["route"]["id"] == chosen["route"]["id"]),
            })
    return {**assembled, "rows": rows}


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
    # O94: a row whose AA cost omits a pricing term competes over [C, factor x C] and earns no label (like O29); O98: a
    # caveat without a stated factor competes over [C, infinity) (every label test reads a competitor's lower cost, C).
    if aa_cost_caveat(row):
        factor = caveat_factor(row)
        high, gate_provisional = (math.inf if factor is None else high * factor), True
    else:
        gate_provisional = False
    provisional = summary.provisional or gate["outcome"] == GATE_UNVERIFIED or gate_provisional
    if gate["outcome"] == GATE_NOT_IN_FORCE:
        ratio_low, ratio_high = blocker_domain(gate, basis)
        low, high, provisional = low * min(1.0, ratio_low), high * max(1.0, ratio_high), True
    return intervals.Box(row["id"], low, high, summary.lower, summary.upper, provisional)


FOOTNOTE_KINDS = ("pricing omission", "not a pricing omission")


def classify_footnote(note: str | None, register: dict | None) -> dict | None:
    """O100: an AA chart footnote's registered class, looked up by its exact text; the build stops on an unregistered or
    changed note (a closed-world register on the O64 pattern, never a keyword reading)."""

    if not note:
        return None
    entry = next((item for item in (register or {}).get("notes", []) if item.get("text") == note), None)
    if entry is None:
        raise ValueError(f"unregistered AA footnote: {note!r}; classify it in data/aa/aa_footnote_register.json (O100)")
    if entry.get("kind") not in FOOTNOTE_KINDS or (entry.get("factor") is not None and not entry["factor"] >= 1.0):
        raise ValueError(f"AA footnote register entry needs a kind in {FOOTNOTE_KINDS} and a factor of at least 1 or null (O100): {note!r}")
    return entry


def chart_footnote(configuration: dict, points: list[dict]) -> str | None:
    """I84 M1: the footnote the chart capture itself records for the configuration's point (family and effort), which the
    reconciliation inventory's note must equal; without a captured point the inventory's note stands."""

    notes = {point["footnote"] for point in points if point.get("footnote") and point.get("family") == configuration_family(configuration)
             and point.get("effort") == configuration.get("effort")}
    matched = any(point.get("family") == configuration_family(configuration) and point.get("effort") == configuration.get("effort") for point in points)
    if len(notes) > 1 or (matched and next(iter(notes), None) != configuration.get("aaNote")):
        raise ValueError(f"{configuration['id']}: AA footnote differs between the reconciliation inventory and the chart capture (O100)")
    return configuration.get("aaNote")


# I86 L4: O103 binds every AA capture later than the captures it was decided on (the 2026-10-25 release captures).
O103_AFTER = "2026-10-25T09:56:47Z"
NOTE_SURFACES = {
    "snapshot": lambda document: [page["model"] for page in document.get("pages", [])],
    "codingAgents": lambda document: [document, *document.get("configurations", [])],
    "costCharts": lambda document: [item for evaluation in document.get("evaluations", []) for item in (evaluation, *evaluation.get("rows", []))],
}


def check_surface_notes(documents: dict, register: dict | None) -> None:
    """O103, I85 L2, I86 L1: an AA capture taken after O103 must record the verbatim notes AA prints (``notes``, an empty
    list allowed) on every row, page and chart (the Coding Agent Index and each cost chart included), and every note must
    be registered (O100); the build stops otherwise."""

    for key, items_of in NOTE_SURFACES.items():
        document = documents.get(key) or {}
        if not document.get("capturedAt") or _instant(document["capturedAt"]) <= _instant(O103_AFTER):
            continue
        for item in items_of(document):
            if not isinstance(item.get("notes"), list):
                raise ValueError(f"{key}: a capture after O103 records no notes for a row or chart; capture AA's notes verbatim (O103)")
            for note in item["notes"]:
                classify_footnote(note, register)


# I86 L4: the fields only a frontier list carries (its position and the near-gap arithmetic) are not compared.
TWIN_LIST_FIELDS = {"order", "tier", "intelligence_gap", "cost_ratio"}


def check_shared_labels(mapping: dict) -> None:
    """I90 L5: no two configurations share one basket-chart label (a shared label prices both from one row)."""

    for slug in basket.CHART_COMPONENTS:
        seen: dict[str, str] = {}
        for model_id, labels in sorted(mapping.items()):
            label = (labels or {}).get(slug)
            if label is not None and seen.setdefault(label, model_id) != model_id:
                raise ValueError(f"{slug}: {seen[label]} and {model_id} share the label {label!r} (I90 L5)")


def check_regime_bounds(routes: list[dict], pages: dict, records: list[dict]) -> None:  # pages keyed by configuration ID
    """O110, I90 L1: a route's ``modelLaunchedOn`` equals AA's release date for its model, and its ``scheduleFrom`` is the
    date of a recorded change for its provider (the schedule's start); the build stops otherwise."""

    for route in routes:
        launched = route.get("modelLaunchedOn")
        model = (route.get("modelIds") or [None])[0]
        if launched is not None and model in pages:
            page = pages[model]
            if page is None or page.get("releaseDate") != launched:
                raise ValueError(f"route {route['id']}: modelLaunchedOn {launched} is not AA's release date {(page or {}).get('releaseDate')} (I90 L1)")
        schedule = route.get("scheduleFrom")
        if schedule is not None and not any(record["date"][:10] == schedule and record.get("provider") == route.get("provider") for record in records):
            raise ValueError(f"route {route['id']}: scheduleFrom {schedule} is no recorded change for its provider (I90 L1)")


def check_register_subjects(register: dict | None, known: set) -> None:
    """I88 L1: every configuration a chart-level note's ``appliesTo`` names is a known configuration (the build stops on a
    typo, a family name or any other ID that would silently match no row)."""

    for entry in (register or {}).get("notes", []):
        unknown = sorted(set(entry.get("appliesTo") or []) - known)
        if unknown:
            raise ValueError(f"AA note register entry {entry.get('text')!r} applies to unknown configurations {unknown} (I88 L1)")


def check_capture_twins(capture: dict | None) -> None:
    """I85 L3: each frontier and near-frontier entry equals its twin in ``points`` (same page URL and circle) on every shared
    field but its list position, the footnote included; the build stops otherwise."""

    points = {(point.get("url"), point.get("circle_id")): point for point in (capture or {}).get("points", [])}
    for entry in (capture or {}).get("frontier", []) + (capture or {}).get("near_frontier", []):
        twin = points.get((entry.get("url"), entry.get("circle_id")))
        if twin is None or any(entry.get(key) != twin.get(key) for key in (set(entry) | set(twin)) - TWIN_LIST_FIELDS
                               if not key.startswith("nearest_frontier")):
            raise ValueError(f"{entry.get('model_name')}: the chart capture's frontier list entry differs from its point (I85 L3)")


def check_captured_footnotes(capture: dict | None, register: dict | None) -> None:
    """O100, I84 M1: every footnote the chart capture records, on any point, is registered; the build stops otherwise."""

    for point in (capture or {}).get("points", []) + (capture or {}).get("frontier", []) + (capture or {}).get("near_frontier", []):
        classify_footnote(point.get("footnote"), register)


def page_notes(page: dict | None) -> list[str]:
    """O103, O106: the notes a post-O103 capture records on a model page."""

    return list((page or {}).get("notes") or [])


def basket_label(capture: dict | None, labels: dict, slug: str, configuration: dict | None = None, points: list[dict] | tuple = ()) -> str | None:
    """I87 L4: a row's mapped label on a basket cost chart, which must name a row the chart holds; I88 L3: a null label while
    the chart holds a row named as the configuration ("Name (effort)") would silently drop its cost and notes. The build
    stops on either. I89 L2: the configuration's name on AA's charts is its point's name in the chart capture (same family
    and effort), with "Name (effort)" as a fallback."""

    label = labels.get(slug)
    evaluation = next((item for item in (capture or {}).get("evaluations", []) if item.get("slug") == slug), None)
    models = {row.get("model") for row in (evaluation or {}).get("rows", [])}
    if label is not None and evaluation is not None and label not in models:
        raise ValueError(f"{slug}: the configuration map's label {label!r} names no row on the captured chart (I87 L4)")
    expected = {f"{configuration.get('name')} ({configuration.get('effort')})"} | {point.get("model_name") for point in points
                if point.get("family") == configuration_family(configuration) and point.get("effort") == configuration.get("effort")} if configuration else set()
    if label is None and configuration and expected & models:
        raise ValueError(f"{slug}: the chart holds a row for {configuration['id']} but the configuration map gives it no label (I88 L3)")
    # I90 L5: when the chart holds the configuration's own row, the label must name it, not another configuration's row.
    if label is not None and configuration and expected & models and label not in expected:
        raise ValueError(f"{slug}: {configuration['id']}'s label {label!r} names another row than its own ({sorted(expected & models)}) (I90 L5)")
    return label


def chart_notes(capture: dict | None, labels: dict, slug: str, configuration: dict | None = None, points: list[dict] | tuple = ()) -> list[str]:
    """O106: the notes on the row's own row of one basket cost chart."""

    label = basket_label(capture, labels, slug, configuration, points)
    evaluation = next((item for item in (capture or {}).get("evaluations", []) if item.get("slug") == slug), {})
    return [note for row in evaluation.get("rows", []) if label is not None and row.get("model") == label for note in row.get("notes") or []]


def chart_level_notes(capture: dict | None, labels: dict, slug: str) -> list[str]:
    """O106, I87 L3: the notes printed on one basket cost chart that holds the row (they name no row themselves)."""

    evaluation = next((item for item in (capture or {}).get("evaluations", []) if item.get("slug") == slug), {})
    # I90 L6: only on a chart that actually holds the row's label.
    holds = labels.get(slug) is not None and any(row.get("model") == labels[slug] for row in evaluation.get("rows", []))
    return list(evaluation.get("notes") or []) if holds else []


def note_sources(configuration: dict, page: dict | None, record: dict | None, documents: dict, labels: dict) -> dict:
    """O106, O108, O109: a row's AA notes by surface: always (the chart footnote and the model page), and per basket component
    its own row's notes and the notes printed for that whole chart or index."""

    charts = documents.get("costCharts") or {}
    agents = documents.get("codingAgents") or {}
    return {
        "always": [configuration.get("aaNote"), *page_notes(page)],
        "rows": {basket.CODING_AGENT_INDEX: list((record or {}).get("notes") or []), **{slug: chart_notes(charts, labels, slug, configuration, (documents.get("frontierCapture") or {}).get("points", [])) for slug in basket.CHART_COMPONENTS}},
        "shared": {basket.CODING_AGENT_INDEX: list(agents.get("notes") or []) if record else [], **{slug: chart_level_notes(charts, labels, slug) for slug in basket.CHART_COMPONENTS}},
        # O108, I89 L3: notes on charts outside the basket, disclosed only.
        "other": {evaluation["slug"]: [*(note for row in evaluation.get("rows", []) if row.get("model") == labels.get(evaluation["slug"]) for note in row.get("notes") or []),
                                      *chart_level_notes(charts, labels, evaluation["slug"])]
                  for evaluation in charts.get("evaluations", []) if evaluation.get("slug") not in basket.CHART_COMPONENTS and labels.get(evaluation.get("slug")) is not None},
    }


def uncounted_notes(row: dict, admitted: list[str], register: dict | None = None) -> list[dict]:
    """O108, O109, I89 L3: the row's notes that change nothing (a pending component's, or a chart outside the basket's),
    published as disclosures with their surface."""

    sources = row.get("aaNoteSources") or {}
    pending = [{"surface": slug, "note": note, "reason": "component not admitted to this ranking's cost workload (O109)"}
               for kind in ("rows", "shared") for slug, notes in (sources.get(kind) or {}).items() if slug not in admitted for note in notes]
    other = [{"surface": slug, "note": note, "reason": "chart outside the cost basket (O108)"} for slug, notes in (sources.get("other") or {}).items() for note in notes]
    # I90 L6: each disclosure carries its registered class and factor.
    return [{**item, **{key: entry.get(key) for key in ("kind", "factor")}} for item in pending + other
            if (entry := classify_footnote(item["note"], register)) is not None]


def admitted_note_class(row: dict, admitted: list[str], register: dict | None) -> dict | None:
    """O109 (2026-10-28): the row's note class from its chart footnote, its model page and the components admitted to this
    ranking's cost workload; a pending component's notes change nothing until it is admitted."""

    sources = row.get("aaNoteSources") or {"always": [row.get("aaNote")], "rows": {}, "shared": {}}
    return combined_note_class([*sources["always"], *(note for slug in admitted for note in sources["rows"].get(slug, []))],
                               [note for slug in admitted for note in sources["shared"].get(slug, [])], register, row["id"])


def combined_note_class(notes: list[str | None], shared: list[str], register: dict | None, model_id: str | None = None) -> dict | None:
    """O106: every registered note on the row's AA surfaces; a pricing omission anywhere makes the row an O94 row, with the
    largest stated factor, or none when any omission states none (O98). I87 L3: a note printed for a whole chart or index
    (``shared``) names no row, so as a pricing omission it applies only to the configurations its register entry lists in
    ``appliesTo``, and the build stops on one that lists none."""

    classes = [entry for note in dict.fromkeys(note for note in notes if note) if (entry := classify_footnote(note, register))]
    for note in dict.fromkeys(shared):
        entry = classify_footnote(note, register)
        if entry["kind"] == "pricing omission":
            if not entry.get("appliesTo"):
                raise ValueError(f"chart-level AA pricing note {note!r} must list the configurations it applies to (appliesTo, I87 L3)")
            if model_id in entry["appliesTo"]:
                classes.append(entry)
    omissions = [entry for entry in classes if entry["kind"] == "pricing omission"]
    if not omissions:
        return classes[0] if classes else None
    factors = [entry.get("factor") for entry in omissions]
    return {"kind": "pricing omission", "text": " ".join(entry["text"] for entry in omissions),
            "factor": None if None in factors else max(factors)}


def aa_cost_caveat(row: dict) -> str | None:
    """E141, O94, O100, O106: AA's own notes when their registered class is a pricing omission, else None."""

    entry = row.get("aaNoteClass") or {}
    return entry.get("text") if entry.get("kind") == "pricing omission" else None


def caveat_factor(row: dict) -> float | None:
    """O94, O100: the registered factor of the omitted pricing term (the largest the note states); None when the row has no
    caveat or the note states no factor (O98: the row then competes over [C, infinity))."""

    return (row.get("aaNoteClass") or {}).get("factor") if aa_cost_caveat(row) else None


def provider_claimed(row: dict) -> bool:
    """E233: a row with a leaf taken from the model provider's own published result (O36's last source)."""

    return any(source.get("sourceType") == "model_provider_claim" for source in row["evidence"]["provenance"].values())


def blocker_domain(gate: dict, basis: str) -> tuple[float, float] | None:
    """E183/E185: the current-tariff ratio range a blocker's box is widened by, or None when it cannot be constructed."""

    bounds = gate["bounds"]
    if bounds["status"] != "available":
        return None
    low, high = bounds["apiCost" if basis == "api" else "planCost"]
    return (low, high) if high is not None and low > 0 else None


def api_candidates(assembled: dict, components: list[str] | None = None) -> list[tuple[dict, float, float]]:
    """The rows (with their cost range) R_W admits on the API basis before the valuation gate: ranked rows with FullCost on
    the main workload (E37), or on the subset workload of ``components`` (E190)."""

    found = []
    for row in assembled["rows"]:
        cost = row["cost"] if components is None else basket.row_cost(row["components"], components)
        on_workload = components is not None or cost["workload"] == assembled["mainWorkload"]
        if cost["fullCost"] and on_workload and anchor_math.scoreable(cost["lowUsd"]):
            found.append((row, cost["lowUsd"], cost["highUsd"]))
    return found


def plan_candidates(assembled: dict) -> list[tuple[dict, float, float]]:
    """The rows R_W admits on the Plan basis before the valuation gate: FullCost on the main workload and an identified,
    finite M_W (E106 PlanIntervalEligible)."""

    found = []
    for row in assembled["rows"]:
        selected = row["routeSelection"]["selected"]
        cost = row["cost"]
        if selected is None or not cost["fullCost"] or cost["workload"] != assembled["mainWorkload"]:
            continue
        bounds = plan_routes.identified_bounds(selected)
        # E138: an unrecorded or different valuation basis is never interval-eligible.
        if bounds is None or not anchor_math.scoreable(bounds[1]) or selected["valuation"] not in {"release", "revalued"}:
            continue
        found.append((row, cost["lowUsd"] / bounds[1], cost["highUsd"] / bounds[0]))
    return found


def _boxes(candidates: list[tuple[dict, float, float]], basis: str) -> list[intervals.Box]:
    return [box for row, low, high in candidates if (box := _gated_box(row, low, high, basis)) is not None]


def api_boxes(assembled: dict, components: list[str] | None = None) -> list[intervals.Box]:
    """R_W on the API basis as admissible boxes."""

    return _boxes(api_candidates(assembled, components), "api")


def plan_boxes(assembled: dict) -> list[intervals.Box]:
    """R_W on the Plan basis as admissible boxes."""

    return _boxes(plan_candidates(assembled), "plan")


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
    "planRule": "the same configurations at their displayed Plan cost: measured routes, owner assumptions of every kind and API-cost fallbacks alike, since each is scored in the Plan table (O13, O16) and a narrower panel would clip them",
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
        # O94, I80 M1: a row whose AA cost omits a pricing term leaves the anchor population at the next re-freeze only; the
        # current anchors and the diagnostics that rebuild them by the same rule keep it, so their effects stay separable.
        table.append({"row": row["id"], "completeEvidence": complete, "valuationGate": outcome, "eligible": reason is None, "reason": reason,
                      "leavesAtNextFreeze": "AA cost omits a pricing term (O94)" if reason is None and aa_cost_caveat(row) else None})
    return table


def anchor_population(assembled: dict, components: list[str], *, freezing: bool = False) -> list[str]:
    """E160: ranked configurations with complete cost evidence on every component of a workload; a new freeze also leaves
    out rows whose AA cost omits a pricing term (O94)."""

    # E170/O29: a row whose AA cost is not on the price in force at V is never an anchor reference.
    return sorted(item["row"] for item in anchor_eligibility(assembled, components) if item["eligible"] and not (freezing and item["leavesAtNextFreeze"]))


def freeze(assembled: dict, *, frozen_at: str) -> dict:
    """Anchor objects per workload and basis from the registered anchor population (E160), and the bar reference."""

    workloads = {}
    by_id = {row["id"]: row for row in assembled["rows"]}
    for workload, entry in workload_catalog(assembled).items():
        components = entry["components"]
        population = anchor_population(assembled, components, freezing=True)
        if len(population) < MIN_ANCHOR_REFERENCES:
            if entry["role"] == "main":
                raise ValueError(f"the main workload has {len(population)} complete-evidence anchor references; at least {MIN_ANCHOR_REFERENCES} are required")
            workloads[workload] = {**entry, "anchors": {"api": None, "plan": None}, "anchorStatus": f"unavailable: fewer than {MIN_ANCHOR_REFERENCES} complete-evidence references"}
            continue
        api = {row_id: restricted_cost(by_id[row_id]["components"], components) for row_id in population}
        # O48: the Plan anchor references are the plan rows of the reference configurations.
        plan = {item["id"]: _plan_cost_on(item, components) for item in plan_variants(assembled)["rows"] if item["configurationId"] in population}
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
        "anchorVersion": f"v3-{frozen_at}" if q.TRACK == q.DEFAULT_TRACK else f"v3-{frozen_at}-{q.TRACK}",
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


def shared_uncertain_donors(candidates: list[tuple[dict, float, float]]) -> list[str]:
    """E273: donor routes whose set-identified (non-point) multiple is used by more than one interval candidate."""

    users: dict[str, set] = {}
    for row, _, _ in candidates:
        selected = row["routeSelection"]["selected"]
        bounds = plan_routes.identified_bounds(selected)
        if bounds is not None and bounds[0] != bounds[1]:
            users.setdefault(selected.get("donorRouteId") or selected["route"]["id"], set()).add(row.get("configurationId", row["id"]))
    return sorted(donor for donor, rows in users.items() if len(rows) > 1)


def interval_outputs(assembled: dict, frozen: dict, basis: str, components: list[str] | None = None) -> dict:
    """Frontier and bar results over R_W for one basis, with the universe and the unevaluable rows (E38).

    With ``components``, the outputs are for that subset workload (E190; API basis only: no Plan multiple is
    identified for a subset workload).
    """

    candidates = api_candidates(assembled, components) if basis == "api" else plan_candidates(assembled)
    # E273 (reviewer 71): E89's separability needs every row's cost to rest on its own primitives; two Plan rows sharing one
    # donor multiple known only as a range share an uncertain factor, so the outputs are unresolved, never computed by corners.
    shared = shared_uncertain_donors(candidates) if basis == "plan" else []
    if shared:
        return {"universe": sorted(row["id"] for row, _, _ in candidates), "unevaluable": [], "status": intervals.UNRESOLVED,
                "reason": "rows share an uncertain donor multiple, so the separability condition (E89) fails (E273): " + ", ".join(shared)}
    boxes = _boxes(candidates, basis)
    # E183: competitors range over U_W = R_W plus the O29 blockers B_W; labels go to R_W only.
    not_in_force = {row["id"] for row in assembled["rows"] if row["valuationGate"]["outcome"] == GATE_NOT_IN_FORCE}
    # E183: an O29 blocker without a constructible domain leaves the outputs unresolved, never silently computed without it;
    # I82 L3: only where the row would compete (the rows R_W would otherwise admit on this workload and basis). O98: an O94
    # row is always constructible (a factorless caveat competes over [C, infinity)).
    unconstructible = sorted(row["id"] for row, _, _ in candidates
                             if row["id"] in not_in_force and blocker_domain(row["valuationGate"], basis) is None)
    # E222/E228/E233: an unverified basis, a provider-claimed leaf, or (Plan) a route whose evidence a detected change may
    # have superseded, competes but earns no label, exactly like an O29 blocker; O118, O119: so does a hard-expired route
    # (in grace) and one measured inside an acknowledged accounting-fault window.
    blocked = not_in_force | {row["id"] for row in assembled["rows"] if row["valuationGate"]["outcome"] == GATE_UNVERIFIED or provider_claimed(row) or aa_cost_caveat(row)}
    if basis == "plan":
        blocked |= {row["id"] for row in assembled["rows"] if plan_routes.label_denied(row["routeSelection"]["selected"], date.fromisoformat(assembled["releaseDay"]) if assembled.get("releaseDay") else None)}
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
    # E170/O29: a blocker competes over its hull but earns no interval label of its own; I79: each says why.
    by_id = {row["id"]: row for row in assembled["rows"]}
    for row_id in blockers:
        status = withheld_label(by_id[row_id])
        frontier[row_id] = {"status": status}
        for bar in bars:
            if "rows" in bar:
                bar["rows"][row_id] = {"status": status}
                bar["possibleCheapest"] = [item for item in bar["possibleCheapest"] if item != row_id]
                bar["uncheckedCheaperSiblings"].pop(row_id, None)
    for bar in bars:
        if "rows" in bar:
            _comparison(bar)
    return {"universe": universe, "blockers": blockers, "unevaluable": unevaluable, "status": "evaluated", "frontier": frontier, "bars": bars}


WITHHELD_LABEL = "no interval label: AA cost on a price not in force at V (O29); competes over its current-tariff hull"
WITHHELD_CAVEAT = "no interval label: AA's cost omits a pricing term (O94); competes over its published cost up to the stated factor"
WITHHELD_OTHER = ("no interval label: unverified valuation basis (E222), a provider-claimed leaf (E233), or a change-flagged (E228),"
                  " hard-expired (O118) or fault-window (O119) Plan route; competes at its published record")


def withheld_label(row: dict) -> str:
    """Why a blocker earns no interval label of its own (O29, O94, E222, E233, E228, O118, O119)."""

    if row["valuationGate"]["outcome"] == GATE_NOT_IN_FORCE:
        return WITHHELD_LABEL
    return WITHHELD_CAVEAT if aa_cost_caveat(row) else WITHHELD_OTHER


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


def quality_margin(assembled: dict) -> float | None:
    """O44: the quality gap two typical rows need to separate under O39's task-sampling noise, 1.96 x sqrt(2) x the
    median row's quality SD (independent-task approximation, correlation 0)."""

    sds = [quality_sd(row) for row in assembled["rows"]]
    return 1.96 * math.sqrt(2.0) * statistics.median(sds) if sds else None


def displayed_cheapest(assembled: dict, frozen: dict, basis: str, margin: float | None = None) -> dict:
    """E203: per bar, the cheapest non-provisional scored main-workload rows whose displayed quality reaches the level (ties
    listed); O44: beside it, the cheapest whose displayed quality clears the level by at least the quality noise margin."""

    rows = [row for row in assembled["rows"] if row["cost"]["workload"] == assembled["mainWorkload"] and not row["summary"].provisional
            and row["summary"].displayed is not None and _basis_cost(row, basis) is not None]

    def cheapest(level: float) -> tuple[list[dict], float | None, list[str]]:
        qualifying = [row for row in rows if row["summary"].displayed >= level]
        low = min((_basis_cost(row, basis) for row in qualifying), default=None)
        return qualifying, low, sorted(row["id"] for row in qualifying if _basis_cost(row, basis) == low)

    bars = []
    for bar in frozen["barReferences"]:
        qualifying, low, rows_at = cheapest(bar["level"])
        entry = {"bar": bar["id"], "level": bar["level"], "qualifierN": len(qualifying), "costUsd": low, "cheapest": rows_at}
        if margin is not None:
            above, above_low, above_rows = cheapest(bar["level"] + margin)
            entry["margin"] = {"level": bar["level"] + margin, "qualifierN": len(above), "costUsd": above_low, "cheapest": above_rows}
        bars.append(entry)
    return {"label": DISPLAYED_CHEAPEST_LABEL, "margin": margin, "bars": bars}


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


# E258: the publisher of each independently run leaf; a publisher with two or more leaves in a ranking is a multi-leaf source.
LEAF_PUBLISHERS = {"vibeCode": "Vals AI", "codeMigration": "Vals AI", "livebench2Overall": "LiveBench"}


def source_leaves() -> dict:
    """The active ranking's multi-leaf sources: the AA-run leaves and every publisher of two or more independent leaves."""

    groups = {"Artificial Analysis": tuple(leaf.key for leaf in q.LEAVES if leaf.source == "aa")}
    for leaf in q.LEAVES:
        if leaf.key in LEAF_PUBLISHERS:
            groups.setdefault(LEAF_PUBLISHERS[leaf.key], ())
            groups[LEAF_PUBLISHERS[leaf.key]] += (leaf.key,)
    return {source: keys for source, keys in groups.items() if len(keys) >= 2}


# E178: the leaves whose benchmarks O15 excludes from the cost basket (basket.INDEX_RESIDUAL_TASKS), removed jointly.
BASKET_SCOPE_EXCLUDED = ("hle", "critpt", "omniscience")
BASKET_SCOPE_LABEL = "quality restricted to the cost basket's scope"


def deletion_branches() -> list[dict]:
    """Every registered branch: one per leaf (leave-one-benchmark-out) and one per multi-leaf source.

    A single-leaf source (Bug Hunt Bench, Terminal-Bench) coincides with its
    leaf's branch, which carries both labels; the Bug Hunt branch is the
    standing Bug Hunt removal.
    """

    multi = {key for keys in source_leaves().values() for key in keys}
    single = {leaf.key: leaf for leaf in q.LEAVES if leaf.source != "aa" and leaf.key not in multi}
    branches = []
    for leaf in q.LEAVES:
        labels = ["leave-one-benchmark-out"] + (["leave-one-source-out"] if leaf.key in single else [])
        branches.append({"id": f"leave-out:{leaf.key}", "labels": labels, "removed": [leaf.key]})
    for source, keys in source_leaves().items():
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


GAP_FILL_TYPES = ("independent", "model_provider_claim")


def gap_filled_leaves(row: dict) -> list[str]:
    """E234: the leaves a row takes from another party or the provider (O36), a tbench.ai Terminal-Bench fill included."""

    provenance = row["evidence"]["provenance"]
    return [key for key, source in provenance.items()
            if source.get("sourceType") in GAP_FILL_TYPES or (key == "terminalBench" and source.get("agent") not in (None, DEFAULT_TB_HARNESS))]


def gap_fill_sensitivity(rows: list[dict], per_row: dict) -> dict:
    """E234: rank changes when each row's gap-filled leaves are removed and its other leaves renormalised (no score changes)."""

    filled = {row["id"]: gap_filled_leaves(row) for row in rows if gap_filled_leaves(row)}
    bases = {}
    for basis in BASES:
        primary, branched = {}, {}
        for row in rows:
            scores = per_row[row["id"]][basis]
            if scores["value"] is None:
                continue
            primary[row["id"]] = scores["value"]
            quality = deletion_quality(row["evidence"]["observations"], set(filled.get(row["id"], [])))
            branched[row["id"]] = anchor_math.value_score(scores["costScore"], quality, BETA)
        bases[basis] = {"rankChanges": diagnostics.paired_rank_change(primary, branched)}
    return {"label": "gap-fill removal: each row's leaves from another party or the provider removed, the rest renormalised (E234; diagnostic)",
            "rows": filled, "bases": bases}


def gap_fill_bars(assembled: dict, frozen: dict, offset: float | None) -> dict:
    """E234 (as extended after I25): the displayed-record cheapest row at each frozen bar on both bases with the gap
    fills as published, removed (the rest renormalised), and with each third-party fill lowered by the measured mean
    offset; a sensitivity that changes no score and no label."""

    def variants(row: dict) -> dict:
        observations, filled = row["evidence"]["observations"], gap_filled_leaves(row)
        third_party = [key for key in filled if row["evidence"]["provenance"][key].get("sourceType") == "independent"]
        lowered = {**observations, **{key: q.Observation(max(0.0, observations[key].z - (offset or 0.0))) for key in third_party}}
        return {"published": row["summary"].displayed, "removed": deletion_quality(observations, set(filled)), "lowered": q.summarize(lowered).displayed}

    rows = [row for row in assembled["rows"] if row["cost"]["workload"] == assembled["mainWorkload"] and not row["summary"].provisional]
    quality = {row["id"]: variants(row) for row in rows}
    result = {"meanOffset": offset, "bases": {}}
    for basis in BASES:
        costs = {row["id"]: _basis_cost(row, basis) for row in rows if _basis_cost(row, basis) is not None}
        bars = []
        for bar in frozen["barReferences"]:
            entry = {"bar": bar["id"], "level": bar["level"]}
            for variant in ("published", "removed", "lowered"):
                qualifying = [row_id for row_id in costs if quality[row_id][variant] >= bar["level"]]
                low = min((costs[row_id] for row_id in qualifying), default=None)
                entry[variant] = sorted(row_id for row_id in qualifying if costs[row_id] == low)
            entry["survives"] = entry["published"] == entry["removed"] == entry["lowered"]
            bars.append(entry)
        result["bases"][basis] = bars
    return result


FRONTIERCODE_CROSS_SOURCE_RETIRED = ("retired (O136): the leaf is AA's FrontierCode 2.0 and Cognition's board publishes FrontierCode 1.1, "
                                     "so no fill or comparison is made across the two versions")


def frontiercode_cross_source(rows: list[dict], cognition: dict) -> dict:
    """E234: AA's FrontierCode against Cognition's main score for the same family and effort. Retired by O136 (the leaf is
    FrontierCode 2.0, Cognition's board 1.1); the object stays so the published diagnostic says why it is empty."""

    return {"label": "FrontierCode cross-source agreement (AA against Cognition; E234)", "panel": [], "excluded": [], "tau": None,
            "interval": None, "meanOffset": None, "maxAbsOffset": None, "status": FRONTIERCODE_CROSS_SOURCE_RETIRED, "scale": "not applicable"}


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


def costed_bar_ladder(assembled: dict, per_row: dict) -> dict:
    """I28: the bar population keeps full-benchmark rows without a cost by choice; this sensitivity recomputes the
    ladder over the scored rows alone (the frozen ladder is unchanged)."""

    scored = [row for row in assembled["rows"] if per_row[row["id"]]["api"]["value"] is not None]
    population, bars = bar_levels({**assembled, "rows": scored})
    return {"excluded": sorted(row["id"] for row in assembled["rows"] if row not in scored), "population": len(population),
            "levels": [bar["level"] for bar in bars]}


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


INDICATIVE_LABEL = "not ranked, not comparable: quality on the leaves the configuration has, renormalised, with no imputation (O41)"


def listed_indicative(assembled: dict, frozen: dict) -> list[dict]:
    """O41: for each frontier or near-frontier family listed under O38, an indicative value on its remaining leaves,
    published apart from the ranking with no rank and no label."""

    result = []
    for row in assembled.get("listed", []):
        entry = {"id": row["id"], "name": row["name"], "label": INDICATIVE_LABEL, "workload": row["cost"]["workload"],
                 "missing": [leaf.key for leaf in q.LEAVES if leaf.key not in row["evidence"]["observations"]],
                 "quality": row["summary"].displayed, "coverage": row["summary"].coverage}
        for basis in BASES:
            # A workload no ranked row uses has no frozen anchors, so the indicative row then has no cost score.
            anchors = (frozen["workloads"].get(row["cost"]["workload"]) or {}).get("anchors", {}).get(basis)
            cost = _basis_cost(row, basis)
            cost_score = anchor_math.cost_score(cost, anchors) if anchors and cost is not None else None
            entry[basis] = {"costUsd": cost, "costScore": cost_score, "value": anchor_math.value_score(cost_score, row["summary"].displayed, BETA)}
        result.append(entry)
    return result


def listed_beyond_anchors(listed: list[dict], frozen: dict) -> list[dict]:
    """O58: listed configurations whose cost lies outside a ranking's frozen anchors. The clip gate counts ranked rows
    only, so these never hold a release; they are disclosed with the factor, and a rendered-frontier point is marked."""

    result = []
    for row in listed:
        for basis in BASES:
            # As for the indicative value, a workload no ranked row uses has no frozen anchors to lie beyond.
            anchors = (frozen["workloads"].get(row["cost"]["workload"]) or {}).get("anchors", {}).get(basis)
            cost = _basis_cost(row, basis)
            if not anchors or cost is None or cost <= 0:
                continue
            factor = anchor_math.beyond_factor(cost, anchors)
            if factor > 1.0:
                result.append({"id": row["id"], "name": row["name"], "basis": basis, "workload": row["cost"]["workload"], "costUsd": cost,
                               "side": "below the low anchor" if cost < anchors["low"] else "above the high anchor", "factor": factor,
                               "beyondFactorLimit": factor > anchor_math.BEYOND_FACTOR_LIMIT, "renderedFrontier": row.get("aaTier") == "frontier"})
    return result


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
    # O48: the Plan basis is ranked over one row per configuration and plan; each configuration's own Plan figures are
    # those of its representative row (its selected route).
    plan_assembled = plan_variants(assembled)
    plan_rows = plan_assembled["rows"]
    per_plan = {}
    for row in plan_rows:
        anchors = _anchors_for(frozen, row["cost"]["workload"], "plan")
        cost = _basis_cost(row, "plan")
        cost_score = anchor_math.cost_score(cost, anchors) if anchors else None
        per_plan[row["id"]] = {"plan": {"costUsd": cost, "costScore": cost_score, "value": anchor_math.value_score(cost_score, row["summary"].displayed, BETA)}}
    plan_ranks = competition_ranks({row_id: entry["plan"]["value"] for row_id, entry in per_plan.items()})
    representative = {row["configurationId"]: row["id"] for row in plan_rows if row["representative"]}
    ranks = {"api": competition_ranks({row_id: entry["api"]["value"] for row_id, entry in per_row.items()}),
             "plan": {row_id: plan_ranks[plan_id] for row_id, plan_id in representative.items() if plan_id in plan_ranks}}
    gates, influence, exchange = {}, {}, {}
    for basis in BASES:
        basis_rows, scores_of = (rows, per_row) if basis == "api" else (plan_rows, per_plan)
        clip = []
        for workload in frozen["workloads"]:
            costs = {row["id"]: _basis_cost(row, basis) for row in basis_rows if row["cost"]["workload"] == workload}
            anchors = frozen["workloads"][workload]["anchors"][basis]
            if costs and anchors:
                clip.append({"workload": workload, **anchor_math.clip_gate(costs, anchors)})
        gates[basis] = clip
        influence[basis] = anchor_math.panel_cost_influence(
            [{"id": row["id"], "workloadId": row["cost"]["workload"], "costScore": scores_of[row["id"]][basis]["costScore"], "qualityScore": row["summary"].displayed} for row in basis_rows],
            BETA,
            main,
        )
        # E189: how closely the cost-only and quality-only orderings follow the value ordering on the same panel.
        panel_rows = [row for row in basis_rows if row["cost"]["workload"] == main and scores_of[row["id"]][basis]["value"] is not None]
        values = [scores_of[row["id"]][basis]["value"] for row in panel_rows]
        influence[basis]["orderingAgreement"] = {
            "costVsValue": diagnostics.kendall_tau_b([scores_of[row["id"]][basis]["costScore"] for row in panel_rows], values) if len(panel_rows) >= 2 else None,
            "qualityVsValue": diagnostics.kendall_tau_b([row["summary"].displayed for row in panel_rows], values) if len(panel_rows) >= 2 else None,
        }
        main_anchors = frozen["workloads"][main]["anchors"][basis]
        exchange[basis] = {**anchor_math.exchange_rate(main_anchors, BETA), "curve": anchor_math.exchange_rate_curve(BETA, [4.0, 16.0, 64.0, 256.0, 1024.0])}
    hold = any(item["hold"] for basis in BASES for item in gates[basis])
    yield_ = plan_routes.identification_yield({row["id"]: row["routeSelection"]["selected"] for row in plan_rows})
    agreement = _quality_agreement(rows)
    cohort_rows = rows + assembled.get("listed", [])
    measured = _measured_only_view(rows, frozen, per_row, plan_rows)
    readiness = cost_diagnostics.basket_readiness(rows, assembled["admission"], main)
    interval_rows = sorted(row["id"] for row in rows if (row["evidence"]["provenance"].get("terminalBench") or {}).get("ci95HalfWidthPct"))
    # I63 L5: the lifecycle entry counts plan rows, where the route flags sit.
    lifecycle_flagged = sorted(row["id"] for row in plan_rows if {"possibly-superseded", "expired"} & set((row.get("plan") or {}).get("flags", [])))
    fault_flagged = sorted(row["id"] for row in plan_rows if plan_routes.FAULT_FLAG in row["plan"].get("flags", []))
    caveated = sorted((row for row in rows if aa_cost_caveat(row)), key=lambda row: row["id"])
    manifest = [
        _rule("clip gate (E20)", "fired" if hold else "passed", f"release held; remedy: {anchor_math.CLIP_REMEDY}" if hold else "no basis exceeds the clipping allowance"),
        _rule("cost influence flag (E91)", "fired" if influence["api"]["flag"] or influence["plan"]["flag"] else "passed", "cost not discriminating (< 10%); informational only; beta never changes (O2)"),
        _rule("realised influence (E272)", "fired" if offsetting(influence) else "passed",
              "; ".join(offsetting(influence)) + "; informational only, beta never changes (O2)" if offsetting(influence)
              else "cost's value-variance allocation lies within 0-100% on both bases"),
        _rule("quality influence flag (E126)", "fired" if influence["api"]["qualityFlag"] or influence["plan"]["qualityFlag"] else "passed", "quality not discriminating (cost share > 90%); informational only"),
        _rule("subset scoring (O17)", "fired" if any(row["cost"]["subset"] for row in rows) else "vacuous", "subset rows scored on their own workload and anchors"),
        _rule("partial component flag (E37)", "fired" if any(row["cost"]["partialComponents"] for row in rows) else "vacuous", "AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209)"),
        _rule("route dominance filter (E88)", "fired" if any(row["routeSelection"]["dominated"] for row in rows) else "vacuous", "certifiably dearer routes set aside"),
        _rule("Plan exploratory label (E61)", "fired" if yield_["exploratory"] else "passed", "fewer than half of Plan rows have an identified M_W"),
        # I62 L7: the evidence lifecycle, valuation and clock gates are rules too.
        _rule("Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79)",
              "fired" if lifecycle_flagged else "passed",
              f"{len(lifecycle_flagged)} of {len(plan_rows)} plan rows carry a possibly-superseded or expired route: " + ", ".join(lifecycle_flagged)
              if lifecycle_flagged else "every selected route is fresh"),
        # I77 M1: O91/O92 fault windows, with the rows they flag.
        _rule("acknowledged accounting-fault windows (O91, O92, O93, O95, O96)", "fired" if fault_flagged else "passed",
              f"{len(fault_flagged)} of {len(plan_rows)} plan rows rest on a measurement inside an acknowledged fault window; they stay selected and "
              "yield to two concordant user reports for their own model and plan, and the transfers resting on them follow: " + ", ".join(fault_flagged)
              if fault_flagged else "no selected route rests on a measurement in a fault window"),
        # I80 L5: O94 rows, with the factor each competes over.
        _rule("AA cost omits a pricing term (O94, O98, O100, O106, O108, O109, O114)", "fired" if caveated else "passed",
              "ranked at the published cost; compete in interval outputs and the scenario labels' BlockerSafe test over [C, factor × C] ([C, ∞) without a stated factor, O98) without a label (scenario frequencies draw them at the published cost, O114), and leave the anchor "
              "population at the next freeze: " + ", ".join(f"{row['id']} (up to {caveat_factor(row):g}×)" if caveat_factor(row) else f"{row['id']} (no factor stated: [C, ∞), O98)" for row in caveated)
              if caveated else "no AA cost note names an omitted pricing term"),
        _rule("valuation-basis gate (E170)", "fired" if any(row["valuationGate"]["outcome"] not in GATE_SCORED for row in rows) else "passed",
              "rows outside the scored valuation outcomes: " + ", ".join(sorted(row["id"] for row in rows if row["valuationGate"]["outcome"] not in GATE_SCORED))
              if any(row["valuationGate"]["outcome"] not in GATE_SCORED for row in rows) else "every ranked row is compatible as captured or after evidenced revaluation"),
        _rule("source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218)", "passed",
              "every capture is within its age gate and none after the cutoff unless its source predates the cutoff's day; the build stops otherwise"),
        _rule("build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105-O111, E195, E204, E225)", "passed",
              "the Coding Agent Index manifest (O64), the Terminal-Bench agent list (E225), cutoff-day row dates (O69), the three-stage all-provider plan search (O71, O75), "
              "the typed change records behind every route flag and partition split, which also produce each route's label and blocking dates within its launch- and schedule-bounded span (O99, O101, O105, O107, O110, O111), the register of AA notes covering every captured one, with the chart's inventory and duplicate-entry checks, the post-O103 capture notes, the basket-chart labels and chart-level notes' named rows (O100, O103, O106, O108) "
              "and the frontier path checks (E195, E204) hold; the build stops otherwise"),
        _rule("score swing gate (E177)", "vacuous", "first v3 release: no previous v3 release to compare"),
        _rule("anchor migration (E184)", "fired" if assembled.get("deferred") else "vacuous",
              "deferred: " + ", ".join(item["component"] for item in assembled["deferred"]) if assembled.get("deferred") else "no main-workload migration deferred"),
        _rule("configuration map coverage", "fired" if not all(row["configurationMapped"] for row in rows) else "passed",
              "cohort rows without a configuration-map entry (chart labels; the agent record is derived, E267): " + ", ".join(sorted(row["id"] for row in rows if not row["configurationMapped"])) if not all(row["configurationMapped"] for row in rows) else "every cohort row has a configuration-map entry"),
        _rule("quality clipping audit (E110)", "fired" if any(item["anchorPosition"] != "inside" for row in rows for item in row["evidence"]["clipAudit"]) else "passed", "saturation disclosed; domain violations block the build"),
        _rule("full benchmark set (O36, O38)", "fired" if assembled.get("incomplete") else "passed",
              "listed, not ranked: " + ", ".join(item["id"] for item in assembled["incomplete"]) if assembled.get("incomplete") else "every cohort configuration has every leaf"),
        # E235: the missing-leaf rules stay defined but cannot fire on a ranked row while O36 holds.
        _rule("missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226)", "fired" if any(row["summary"].coverage < 1.0 - 1e-9 for row in rows) else "vacuous",
              "no ranked row has a missing leaf (O36)"),
        _rule("S1M interval stream (E145)", "fired" if interval_rows else "vacuous",
              "widens the published confidence intervals of: " + ", ".join(interval_rows) if interval_rows
              else "dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236)"),
        _rule("provider-claim label denial (E233)", "fired" if any(provider_claimed(row) for row in rows) else "vacuous",
              "competes, earns no label: " + ", ".join(sorted(row["id"] for row in rows if provider_claimed(row))) if any(provider_claimed(row) for row in rows) else "no row has a provider-claimed leaf"),
    ]
    return {
        "methodologyVersion": METHODOLOGY_VERSION,
        "basketVersion": BASKET_VERSION,
        "beta": BETA,
        "anchorVersion": frozen["anchorVersion"],
        "barPolicy": frozen["barPolicy"],
        # I73 L1: the frozen anchor policy with the current wording of its Plan panel rule (the rule itself is unchanged).
        "anchorPolicy": {**frozen["anchorPolicy"], "planRule": ANCHOR_POLICY["planRule"]},
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
        "sourceClocks": assembled.get("sourceClocks", []),
        "planAllowanceCells": assembled.get("planAllowanceCells", []),
        "planResearchCoverage": assembled.get("planResearchCoverage"),
        "costInfluence": influence,
        "gates": {"clip": gates, "hold": hold, "listedBeyondAnchors": listed_beyond_anchors(assembled.get("listed", []), frozen),
                  "population": "ranked rows only; listed rows beyond the anchors are disclosed and never hold a release (O58)"},
        "identificationYield": yield_,
        "rows": [{**_row_json(row, per_row[row["id"]], ranks, route_alternatives(row, _anchors_for(frozen, row["cost"]["workload"], "plan"))),
                  "planRowId": representative.get(row["id"])} for row in rows],
        "planRowRule": PLAN_ROW_RULE,
        "planRows": [_plan_row_json(row, per_plan[row["id"]]["plan"], plan_ranks.get(row["id"])) for row in plan_rows],
        "intervals": {"api": interval_outputs(assembled, frozen, "api"), "plan": interval_outputs(plan_assembled, frozen, "plan")},
        "incompleteEvidence": assembled.get("incomplete", []),
        "listedIndicative": listed_indicative(assembled, frozen),
        "displayedCheapest": {basis: displayed_cheapest(assembled if basis == "api" else plan_assembled, frozen, basis, quality_margin(assembled)) for basis in BASES},
        "barCurrency": bar_currency(assembled, frozen),
        "observedRangeBars": observed_range_bars(assembled, frozen),
        "requiredMissingScores": required_missing_scores(assembled, frozen),
        "subsetIntervals": subset_interval_outputs(assembled, frozen),
        "measuredOnlyPlanView": measured,
        "diagnostics": {
            "rankSeparability": rank_separability(assembled, per_row, exchange, plan_assembled, per_plan),
            "costedBarLadder": costed_bar_ladder(assembled, per_row),
            "terminalBenchSameHarness": _tb_same_harness(rows, assembled["tb4Rows"]),
            # E260: the AA-against-Cognition comparison ranges over every cohort configuration (ranked or listed in this
            # ranking), so both rankings estimate one offset from one panel.
            "frontierCodeCrossSource": frontiercode_cross_source(cohort_rows, assembled["cognition"]),
            "gapFillSensitivity": gap_fill_sensitivity(rows, per_row),
            "harnessCostStress": harness_cost_stress(assembled, frozen),
            "gapFillBars": gap_fill_bars(assembled, frozen, frontiercode_cross_source(cohort_rows, assembled["cognition"])["meanOffset"]),
            "anchorStability": _anchor_stability(rows, frozen, main, per_row),
            "omniscienceAbstentionSensitivity": _abstention_sensitivity(rows, per_row),
            "gdpvalLogisticSensitivity": _gdpval_logistic_sensitivity(rows, per_row),
            "gdpvalMovement": gdpval_movement(assembled, rows),
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
    "admission": "measurement candidates of grade controlled (exact effort, or the same model at another effort, O90) or concordant reports (no owner assumption of any kind, no diagnostics)",
    "selection": "the official selector (E111, E88, E85) rerun among the admitted candidates",
    "anchors": "the official Plan anchor object of the row's workload",
    "panel": "rows with an admitted measured candidate; others listed as 'no measured route' (no API fallback)",
}


def _measured_only_view(rows: list[dict], frozen: dict, per_row: dict, plan_rows: list[dict] = ()) -> dict:
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
        # I74 L2: a row measured on the same model at another effort (an O88 route, O90) says so.
        entries[row["id"]] = {"status": status, "routeId": selected["route"]["id"], "crossEffort": bool(selected["route"].get("sameModelAcrossEfforts")),
                              "faultWindow": selected.get("faultWindow"),
                              "costUsd": cost, "costScore": score_value, "value": value}
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
        "calibration": _measured_calibration(rows, frozen, entries, plan_rows),
    }


MEASURED_CALIBRATION_RULE = (
    "each workload's measured-only rows with complete cost evidence are the references: c_L = cheapest / 2, "
    "c_H = dearest x 2 (diagnostic only; the official anchors are unchanged)"
)


def _plan_evidence(row: dict | None) -> str:
    """How a row's displayed Plan cost is supported: measured route, an owner assumption (by kind) or API-cost fallback."""

    if row is None:
        return "not in the current table"
    if row["plan"]["fallback"]:
        return "API-cost fallback"
    if row["plan"]["grade"] == "assumption":
        return plan_routes.OWNER_ASSUMPTIONS[row["plan"].get("assumptionKind") or "transfer"][0]
    # I75 L3: an O88 route is a controlled measurement of the same model at another effort, named as such.
    if plan_routes.CROSS_EFFORT_FLAG in row["plan"].get("flags", []):
        return "same-model measurement from another effort"
    return {"controlled": "controlled measurement", "reports": "concordant reports"}[row["plan"]["grade"]]


def _reversals(baseline: dict, branch: dict) -> list[list[str]]:
    """Pairs ordered one way by ``baseline`` and the other way by ``branch`` (ties are not reversals)."""

    panel = sorted(row for row in set(baseline) & set(branch) if baseline[row] is not None and branch[row] is not None)
    return [
        [a, b]
        for index, a in enumerate(panel)
        for b in panel[index + 1:]
        if (baseline[a] - baseline[b]) * (branch[a] - branch[b]) < 0
    ]


def _measured_calibration(rows: list[dict], frozen: dict, entries: dict, plan_rows: list[dict] = ()) -> dict:
    """E164: the measured-only rows rescored on anchors built from measured evidence alone.

    The official Plan anchors include owner assumptions of every kind and API-cost fallbacks (E160), so an
    assumption can move measured-only ranks through the exchange rate even though no assumed route
    is in the view. Holding rows, routes, costs and quality fixed, this reports what calibration alone does.
    """

    by_id = {row["id"]: row for row in rows}
    # O48: the official Plan anchors are set over plan rows, so their provenance is read from those rows.
    anchor_rows = {**by_id, **{row["id"]: row for row in plan_rows}}
    measured = {row_id: entry for row_id, entry in entries.items() if "costUsd" in entry}
    workloads, official, calibrated = {}, {}, {}
    for workload, frozen_entry in frozen["workloads"].items():
        members = [row_id for row_id in measured if by_id[row_id]["cost"]["workload"] == workload]
        anchors_official = frozen_entry["anchors"]["plan"]
        provenance = None
        if anchors_official:
            references = anchors_official["referenceCosts"]
            low, high = min(references, key=references.get), max(references, key=references.get)
            provenance = {"low": {"row": low, "evidence": _plan_evidence(anchor_rows.get(low))}, "high": {"row": high, "evidence": _plan_evidence(anchor_rows.get(high))}}
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


def gdpval_movement(assembled: dict, rows: list[dict]) -> dict | None:
    """E90, O70, I60 M1: how far the displayed GDPval-AA Elo moved since the capture this one replaced, and whether the
    page's Intelligence Index total moved with it (it does not when AA keeps a rating frozen at addition in the Index)."""

    previous = assembled.get("gdpvalPrevious")
    if not previous:
        return None
    before = {page["id"]: page for page in previous["pages"]}
    common, moved, index_moved, frozen_index, deltas = 0, 0, 0, 0, {}
    for page in assembled["pages"]:
        old, model = before.get(page.get("id")), page["model"]
        if old is None or old.get("gdpval") is None or model.get("gdpval") is None:
            continue
        common += 1
        delta = model["gdpval"] - old["gdpval"]
        index_changed = model.get("intelligenceIndex") != old.get("intelligenceIndex")
        moved += delta != 0
        index_moved += index_changed
        frozen_index += delta != 0 and not index_changed
        deltas[page["id"]] = delta
    weight = q.LEAF_BY_KEY["gdpval"].weight / 100.0
    # A row's z moves by delta / 20 (E90) and its value by (1 - beta) x the leaf weight x that.
    ranked = [abs(deltas[row["id"]]) for row in rows if row["id"] in deltas]
    largest = max(ranked, default=0.0)
    return {"previousCapturedAt": previous["capturedAt"], "previousSha256": previous["sha256"], "commonPages": common,
            "eloMoved": moved, "indexMoved": index_moved, "eloMovedIndexUnchanged": frozen_index,
            "minDeltaElo": min(deltas.values(), default=0.0), "maxDeltaElo": max(deltas.values(), default=0.0),
            "rankedLargestAbsDeltaElo": largest, "rankedLargestAbsDeltaZ": largest / 20.0,
            "rankedLargestAbsDeltaValue": (1.0 - BETA) * weight * largest / 20.0}


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
        if all(leaf.key in values for leaf in independent_leaves()):
            independent[row["id"]] = sum(values[leaf.key].z for leaf in independent_leaves()) / len(independent_leaves())
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


def aa_leaves() -> tuple:
    return tuple(leaf for leaf in q.LEAVES if leaf.source == "aa")


def independent_leaves() -> tuple:
    return tuple(leaf for leaf in q.LEAVES if leaf.source == "independent")


def _disjoint_agreement(rows: list[dict]) -> dict:
    """E71 (c): tau-b between AA-executed-only quality and independently-executed-only quality on the matched panel."""

    independent = _independent_quality(rows)
    aa_only = {}
    for row in rows:
        values = row["evidence"]["observations"]
        observed = [leaf for leaf in aa_leaves() if leaf.key in values]
        if row["id"] in independent and observed:
            aa_only[row["id"]] = sum(leaf.weight * values[leaf.key].z for leaf in observed) / sum(leaf.weight for leaf in observed)
    result = diagnostics.agreement(aa_only, independent, label="disjoint-evidence agreement (restricted evidence comparison, not an eligible ranking)")
    result["retainedLeaves"] = {"aaExecuted": {leaf.key: leaf.weight for leaf in aa_leaves()}, "independent": {leaf.key: 100.0 / len(independent_leaves()) for leaf in independent_leaves()}}
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
    "ceiling": "provider quota ceiling: the full quota at API rates (O46; full use assumed)",
    "sameModel": "API-equivalent consumption measured on the same model at another effort (O88, O90)",
}
AMOUNT_TARGETS = {"ceiling": "full-quota consumption", "sameModel": "measured-workload consumption (another effort)", "transfer": "assumed consumption", "identified": "target-workload capacity", "capacity": "measured-workload capacity", "observed": "measured-workload consumption"}
NO_TARGET_LINEAGE = "not derivable: the target solution's cash lineage is not established"


def _amount_derivation(kind: str, route: dict, multiple: float, gross: float) -> tuple[float | None, str]:
    """E168: an amount and how it was derived; M x F reproduces an amount only within one object."""

    if kind == "ceiling":
        return (multiple * gross if math.isfinite(gross) else None), "quota ceiling: the tier's credits at the provider's API rate"
    if kind == "sameModel":
        return (multiple * gross if math.isfinite(gross) else None), "same-model measurement: the multiple measured at another effort times this route's cash (O88, O90)"
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
    if route.get("evidenceClass") == "provider_quota_ceiling":
        kind = "ceiling"
    elif route.get("sameModelAcrossEfforts"):
        kind = "sameModel"
    elif selected["grade"] == "assumption":
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


AGENT_EXECUTION = ("the Coding Agent Index runs the model in this vendor agent, while the FrontierCode and Terminal-Bench leaves come from"
                   " AA's own model runs, so the agent's token use is charged to the configuration but not measured on the quality side (O123)")


def coding_agent_execution(components: dict) -> dict | None:
    """O123: the agent behind a row's Coding Agent Index cost, with the execution-match flag."""

    component = components.get(basket.CODING_AGENT_INDEX)
    if component is None:
        return None
    return {"agent": component["detail"].get("agent"), "configuration": component["configuration"], "sameExecutionAsQuality": False, "reason": AGENT_EXECUTION}


def agent_effects(configurations: list[dict]) -> dict:
    """O123: per-agent cost effects h_a from log C(m, a) = alpha_m + h_a, fitted over AA's Coding Agent Index rows of the models
    it lists under two or more agents (centred within each connected group of agents); other agents are unidentified."""

    costs = [(item["model"], item["agent"], math.log(item["meanCostPerTaskUsd"])) for item in configurations if item.get("meanCostPerTaskUsd") and item.get("model") and item.get("agent")]
    agents_of: dict[str, set] = {}
    for model, agent, _ in costs:
        agents_of.setdefault(model, set()).add(agent)
    shared = {model for model, agents in agents_of.items() if len(agents) > 1}
    if not shared:
        return {}
    data = [item for item in costs if item[0] in shared]
    effects = {agent: 0.0 for _, agent, _ in data}
    for _ in range(500):  # backfitting converges for this two-way layout
        alpha = {model: statistics.fmean(cost - effects[agent] for m, agent, cost in data if m == model) for model in shared}
        effects = {agent: statistics.fmean(cost - alpha[model] for model, a, cost in data if a == agent) for agent in effects}
    groups, seen = [], set()
    for agent in sorted(effects):
        if agent in seen:
            continue
        group, frontier = set(), [agent]
        while frontier:
            current = frontier.pop()
            if current not in group:
                group.add(current)
                frontier.extend(a for model in shared if current in agents_of[model] for a in agents_of[model])
        seen |= group
        groups.append(group)
    return {agent: effects[agent] - statistics.fmean(effects[item] for item in group) for group in groups for agent in group}


HARNESS_UNEVALUABLE = "no model is listed under two or more agents in AA's Coding Agent Index capture, so no agent effect is identified (O123)"


def harness_cost_stress(assembled: dict, frozen: dict) -> dict:
    """O123: a named S2 stress: each row's Coding Agent Index cost with its agent's effect removed (C x exp(-h_a)), and the API
    ranks that follow; it never changes a score."""

    effects = agent_effects(((assembled.get("codingAgents") or {}).get("configurations")) or [])
    if not effects:
        return {"id": "harness cost (O123)", "stratum": "S2", "status": "unevaluable", "reason": HARNESS_UNEVALUABLE}
    anchors = frozen["workloads"][assembled["mainWorkload"]]["anchors"]["api"]
    values, adjusted = {}, {}
    for row in assembled["rows"]:
        cost = row["cost"]
        if cost["workload"] != assembled["mainWorkload"] or cost["costUsd"] is None or row["summary"].displayed is None:
            continue
        agent = (coding_agent_execution(row["components"]) or {}).get("agent")
        shift = 0.0
        if basket.CODING_AGENT_INDEX in cost["components"] and agent in effects:
            component = row["components"][basket.CODING_AGENT_INDEX]["costUsd"]
            shift = component * (math.exp(-effects[agent]) - 1.0)
        adjusted[row["id"]] = cost["costUsd"] + shift
        values[row["id"]] = anchor_math.value_score(anchor_math.cost_score(adjusted[row["id"]], anchors), row["summary"].displayed, BETA)
    ranks = competition_ranks(values)
    return {"id": "harness cost (O123)", "stratum": "S2", "status": "evaluated", "agentEffects": effects,
            "rows": {row_id: {"adjustedCostUsd": adjusted[row_id], "value": values[row_id], "rank": ranks.get(row_id)} for row_id in sorted(values)}}


def _row_json(row: dict, scores: dict, ranks: dict, alternatives: list[dict]) -> dict:
    selection = row["routeSelection"]
    selected = selection["selected"]
    caveat = aa_cost_caveat(row)
    return {
        "id": row["id"],
        "name": row["name"],
        "effort": row.get("effort"),
        "aaSlug": row["aaSlug"],
        "configurationMapped": row["configurationMapped"],
        "agentSafety": row.get("agentSafety"),
        # O123: the Coding Agent Index's agent, part of the costed configuration, and whether its run is the quality leaves' run.
        "codingAgent": coding_agent_execution(row["components"]),
        # E141: AA's own note on what its cost omits (e.g. a long-context surcharge), shown as a cost caveat.
        "aaCostCaveat": caveat,
        # O94, I80 L5: the most the omitted term multiplies the cost by, and the cost range the row competes over.
        "aaCostCaveatFactor": caveat_factor(row) if caveat else None,
        "aaUncountedNotes": row.get("aaUncountedNotes", []),
        "aaCostCaveatRangeUsd": [row["cost"]["costUsd"], row["cost"]["costUsd"] * caveat_factor(row)] if caveat and caveat_factor(row) and row["cost"]["costUsd"] is not None else None,
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
                    # I77 M1: the acknowledged fault window a measurement (or its donor) falls in (O91, O92).
                    "faultWindow": item.get("faultWindow"),
                    "contributingReportIds": item["route"].get("reportIds"), "excludedReportIds": item["route"].get("excludedReportIds"),
                }
                for item in row["admissionTable"]
            ],
        },
        "api": {**scores["api"], "rank": ranks["api"].get(row["id"])},
        "planScore": {**scores["plan"], "rank": ranks["plan"].get(row["id"])},
    }


def _plan_row_json(row: dict, scores: dict, rank: int | None) -> dict:
    """O48: one Plan-basis row: a configuration on one plan."""

    selected = row["routeSelection"]["selected"]
    return {
        "id": row["id"], "configurationId": row["configurationId"], "name": row["name"], "plan": row["planName"],
        "representative": row["representative"], "routeId": selected["route"]["id"] if selected else None,
        "planLabel": selected["route"].get("planLabel") if selected else None, "grade": row["plan"].get("grade"),
        "assumptionKind": row["plan"].get("assumptionKind"), "multiple": row["plan"].get("multiple"), "fallback": row["plan"].get("fallback"), "flags": row["plan"].get("flags", []),
        "selectionReason": row["routeSelection"]["reason"], "quality": row["summary"].displayed, **scores, "rank": rank,
    }


# --------------------------------------------------------------------------
# 4. Scenario shares (released as a data file)
# --------------------------------------------------------------------------


# E155: uncertainty outside every v1 stream, printed beside the scenario outputs.
NOT_QUANTIFIED = (
    "benchmark repeatability beyond S1T's independent-task approximation (correlated tasks, harness and attempt effects): not quantified in v1 scenario shares",
    "fitted-parameter uncertainty beyond S1T's assumed GDPval-AA rating interval: not quantified in v1 scenario shares",
)

# E147: the registered kernel-check object for v1 (multiples and price lists are fixed inputs, not drawn).
REGISTERED_DEPENDENCY = ("every row its own dependency component: no shared varying primitive in v1 streams; on the Plan basis the plan rows "
                         "of one configuration form one group sharing every draw (O48)")


def _binomial_variance(score: float, tasks: int) -> float:
    """I28: the Jeffreys-type plug-in proportion's binomial variance for one share scored 0-100."""

    p = (min(1.0, max(0.0, score / 100.0)) * tasks + 0.5) / (tasks + 1.0)
    return p * (1.0 - p) / tasks


def gdpval_row_sd(source: dict) -> float:
    """I60 M2: the row's displayed GDPval-AA interval read as a 95% normal interval, in Elo."""

    interval = source.get("ratingInterval")
    return (interval["upper"] - interval["lower"]) / 2.0 / 1.96 if interval else GDPVAL_RATING_SD


def sampling_sd(key: str, observation: q.Observation, source: dict, gdpval_sd: float | None = None, tasks_of: dict | None = None) -> float:
    """O39: the plug-in standard error of one leaf's z score under the independent-task approximation (binomial
    leaves with the Jeffreys-type proportion, I28)."""

    z = observation.z
    if key == "gdpval":
        return (gdpval_row_sd(source) if gdpval_sd is None else gdpval_sd) * 100.0 / 2000.0  # E90: z = (Elo - 500) / 20
    if source.get("stderr") is not None:
        return source["stderr"]  # Vals' published standard error, in percentage points (the leaf's z unit)
    if key == "livebench2Overall":
        # O67: LiveBench's Overall is the release's weighted mean, so the category draws carry the same weights.
        categories, weights = source["categories"], source.get("weights") or {name: 1.0 for name in LIVEBENCH_CATEGORY_TASKS}
        variance = sum(weights[name] ** 2 * _binomial_variance(categories[name], tasks) for name, tasks in LIVEBENCH_CATEGORY_TASKS.items())
        return 100.0 * math.sqrt(variance) / sum(weights[name] for name in LIVEBENCH_CATEGORY_TASKS)
    tasks = (tasks_of or SAMPLING_TASKS)[key]
    if key == "omniscience" and source.get("accuracy") is not None and source.get("hallucinationRate") is not None:
        correct = source["accuracy"]
        wrong = source["hallucinationRate"] * (1.0 - correct)
        index_sd = 100.0 * math.sqrt(max(0.0, correct + wrong - (correct - wrong) ** 2) / tasks)
        return index_sd / 2.0  # O28: z = (I + 100) / 2
    # I28: a Jeffreys-type plug-in, (k + 1/2) / (n + 1), keeps the SD positive at a 0% or 100% score.
    p = (min(1.0, max(0.0, z / 100.0)) * tasks + 0.5) / (tasks + 1.0)
    return 100.0 * math.sqrt(p * (1.0 - p) / tasks)


def sampling_kernel(key: str, observation: q.Observation, source: dict) -> scenarios.Kernel:
    """O39: the task-sampling kernel of one leaf, clipped to the 0-100 score domain."""

    derivation = scenarios.ANALYST_CONVENTION if key == "gdpval" else scenarios.PUBLISHED_PRECISION
    return scenarios.Kernel("normal", (observation.z, sampling_sd(key, observation, source), 0.0, 100.0), None, scenarios.TASK_SAMPLING, derivation)


def quality_sd(row: dict, gdpval_sd: float | None = None, tasks_of: dict | None = None) -> float:
    """O39: a row's analytic quality SD from its leaves' task-sampling SDs (cost is not drawn)."""

    observations, provenance = row["evidence"]["observations"], row["evidence"]["provenance"]
    return math.sqrt(sum((q.LEAF_BY_KEY[key].weight / 100.0 * sampling_sd(key, value, provenance.get(key) or {}, gdpval_sd, tasks_of)) ** 2
                         for key, value in observations.items()))


def rank_separability(assembled: dict, per_row: dict, exchange: dict | None = None, plan_assembled: dict | None = None,
                      per_plan: dict | None = None) -> dict:
    """O39: how far apart two values must be to separate under the task-sampling approximation, and how many
    adjacent ranks are separable, per basis (a diagnostic beside the ranks; scores and labels unchanged)."""

    sd = {row["id"]: (1.0 - BETA) * quality_sd(row) for row in assembled["rows"]}
    wide = {row["id"]: (1.0 - BETA) * quality_sd(row, GDPVAL_WIDE_SD) for row in assembled["rows"]}
    # E263: AI Coding Daily's noise reads its six graded projects as n = 6 trials of the points share (wide); the narrow
    # reading, n = 60 (one trial per point), is a named sensitivity in the ranking that has the leaf.
    narrow = {row["id"]: (1.0 - BETA) * quality_sd(row, tasks_of={**SAMPLING_TASKS, "aiCodingDaily": AICD_NARROW_TASKS}) for row in assembled["rows"]}
    # O48: the Plan basis is ranked over plan rows; a plan row carries its configuration's quality noise.
    plan_rows = (plan_assembled or assembled)["rows"]
    configuration_of = {row["id"]: row.get("configurationId", row["id"]) for row in plan_rows}
    configuration_of.update({row_id: row_id for row_id in sd})
    plan_scores = per_plan if per_plan is not None else per_row
    # I27: the Plan basis also carries owner-assumption error, which this noise does not include.
    assumed = sorted(row["id"] for row in plan_rows if transfer_dependent(row))
    result = {"assumptions": list(SAMPLING_ASSUMPTIONS), "bias": SEPARABILITY_BIAS, "bandRule": BAND_RULE, "valueSd": sd,
              "qualityMargin": quality_margin(assembled), "planAssumedRouteRows": assumed,
              # I71: rows per owner-assumption kind, so every published enumeration is generated.
              "planAssumedRouteKinds": {kind: sum(1 for row in plan_rows if transfer_dependent(row) and (row["plan"].get("assumptionKind") or "transfer") == kind)
                                        for kind in plan_routes.OWNER_ASSUMPTIONS}}
    for basis in BASES:
        ids, scores_of = (list(sd), per_row) if basis == "api" else ([row["id"] for row in plan_rows], plan_scores)
        ranked = sorted((scores_of[row_id][basis]["value"], row_id) for row_id in ids if scores_of[row_id][basis]["value"] is not None)
        ranked.reverse()

        # O48: two plan rows of one configuration share every quality draw, so only the plans' multiples order them; such
        # pairs are counted apart, and the threshold, its median and the separable count range over pairs of different
        # configurations (E258), so the median is not pulled to zero by a configuration's many plan rows.
        pairs = list(zip(ranked, ranked[1:]))
        # Reviewer 73 (O17, O117): a subset-workload row stays ranked, but its order against a row on another workload is not
        # identified, so such adjacent pairs are counted apart and never tested, and the row joins no noise band.
        workload_of = {row["id"]: row["cost"]["workload"] for row in assembled["rows"]}
        main = assembled.get("mainWorkload")
        off = {row_id for _, row_id in ranked if main is not None and workload_of.get(configuration_of[row_id], main) != main}
        across = [pair for pair in pairs if (pair[0][1] in off) != (pair[1][1] in off)]
        cross = [((high, first), (low, second)) for (high, first), (low, second) in pairs
                 if configuration_of[first] != configuration_of[second] and ((high, first), (low, second)) not in across]

        def adjacent(sds: dict, rho: float) -> tuple[int, float | None]:
            thresholds = [separation(sds[configuration_of[first]], sds[configuration_of[second]], rho) for (_, first), (_, second) in cross]
            separable = sum(high - low >= threshold and high > low for ((high, _), (low, _)), threshold in zip(cross, thresholds))
            return separable, statistics.median(thresholds) if thresholds else None

        separable, median = adjacent(sd, 0.0)
        result[basis] = {
            "adjacentPairs": len(cross), "separableAdjacentPairs": separable, "medianSeparation": median,
            "sameConfigurationAdjacentPairs": sum(1 for (_, first), (_, second) in pairs if configuration_of[first] == configuration_of[second]),
            "crossWorkloadAdjacentPairs": len(across),
            # I26: a shared task set correlates two rows' errors, which narrows the true threshold; the grid shows how far.
            "byCorrelation": {f"{rho:.1f}": adjacent(sd, rho)[0] for rho in SEPARABILITY_CORRELATIONS},
            "gdpvalWide": dict(zip(("separableAdjacentPairs", "medianSeparation"), adjacent(wide, 0.0))),
            **({"aicdNarrow": dict(zip(("separableAdjacentPairs", "medianSeparation"), adjacent(narrow, 0.0)))} if "aiCodingDaily" in q.LEAF_BY_KEY else {}),
            "bands": _bands_on_workload(ranked, off, sd, configuration_of),
        }
        doubling = ((exchange or {}).get(basis) or {}).get("valuePointsPerCostDoubling")
        # I28: the factor by which a cost (on the Plan basis, a transferred multiple) can be wrong before the value moves
        # by the median separation threshold; a tolerance, not an estimate of any transfer's error.
        result[basis]["costTolerance"] = None if median is None or not doubling else 2.0 ** (median / doubling)
        # E272: the tolerance uses the unclipped slope; an assumption row whose cost score is clipped at an anchor has slope 0
        # there, so its multiple can be wrong by any factor until the row re-enters the scale.
        result[basis]["toleranceUnbounded"] = sorted(row_id for row_id in (assumed if basis == "plan" else [])
                                                     if (plan_scores.get(row_id) or {}).get(basis, {}).get("costScore") in (0.0, 100.0))
    return result


SEPARABILITY_CORRELATIONS = (0.0, 0.3, 0.6)
AICD_NARROW_TASKS = 60  # E263: one trial per point of 60, the narrow reading of AI Coding Daily's noise
GDPVAL_WIDE_SD = 26.0  # I26, I60: AA's displayed +/-26 Elo for Claude Opus 5.5 read as one SD for every row, the wide reading of an interval whose level is unstated
SEPARABILITY_BIAS = ("net direction not established: treating two rows' errors as independent overstates the threshold, because every row "
                     "is scored on the same tasks and attempts are averaged within a task; sources it omits (run-to-run and harness "
                     "variance, AA's single cost run and, on the Plan basis, owner-assumption error) work the other way")
BAND_RULE = ("O42: rows in value order; a row joins the current band while its value is not separable from the band's first row at "
             "correlation 0 (1.96 x sqrt(SD_i^2 + SD_j^2), analytic quality-leaf SDs, cost not drawn), otherwise it starts a new band; "
             "every row is inseparable from its band's first row, and adjacent rows in different bands may also be inseparable. O48: on "
             "the Plan basis a plan row takes its configuration's SD; a row of the band's first configuration on another plan stays in "
             "the band, and adjacent plan rows of one configuration are counted apart from the separability pairs (E258)")


def _separable(gap: float, first: str, second: str, sd: dict) -> bool:
    """O42/O48: whether a row leaves the current band: its value gap to the band's first row separates them at correlation
    0. A row of the band's first configuration on another plan stays in the band: their order is certain, but the rows
    between them cannot be told apart from either."""

    return first != second and gap >= separation(sd[first], sd[second], 0.0)


def separation(first: float, second: float, rho: float) -> float:
    """O39: the 95% separation threshold for two value SDs whose errors correlate at rho."""

    return 1.96 * math.sqrt(max(0.0, first ** 2 + second ** 2 - 2.0 * rho * first * second))


def _bands_on_workload(ranked: list[tuple[float, str]], off: set, sd: dict, configuration_of: dict) -> dict:
    """Reviewer 73: the O42 bands over the main-workload rows only, with each band's positions read in the full value order."""

    kept = [item for item in ranked if item[1] not in off]
    position = {row_id: index for index, (_, row_id) in enumerate(ranked, 1)}
    at = [position[row_id] for _, row_id in kept]
    return {row_id: [at[first - 1], at[last - 1]] for row_id, (first, last) in rank_bands(kept, sd, configuration_of).items()}


def rank_bands(ranked: list[tuple[float, str]], sd: dict, configuration_of: dict | None = None) -> dict:
    """O42: each row's band, as the first and last positions of the rows it cannot be separated from by the band rule
    (O48: a plan row takes its configuration's SD; a row of the band's first configuration on another plan stays in the band)."""

    of = configuration_of or {}
    bands, current = [], []
    for value, row_id in ranked:
        if current and _separable(current[0][0] - value, of.get(current[0][1], current[0][1]), of.get(row_id, row_id), sd):
            bands.append(current)
            current = []
        current.append((value, row_id))
    if current:
        bands.append(current)
    result, position = {}, 0
    for band in bands:
        first, last = position + 1, position + len(band)
        result.update({row_id: [first, last] for _, row_id in band})
        position = last
    return result


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
def assumption_exclusion(row: dict) -> str:
    """E167, I72 L2: why a row is unevaluable with owner assumptions off, naming its assumption kind from the registry."""

    name = plan_routes.OWNER_ASSUMPTIONS[row["plan"].get("assumptionKind") or "transfer"][0]
    return f"{name}: unevaluable with owner assumptions off (never reselected or replaced by API cost)"


def transfers_on(stratum: str) -> bool:
    """E167: only S0, the displayed record's reporting precision, keeps owner-named transfers."""

    return stratum == "S0"


def transfer_dependent(row: dict) -> bool:
    """A row whose selected Plan route is an owner assumption of any kind (API-fallback rows carry no grade)."""

    return row["plan"].get("grade") == "assumption"


def scenario_panel(assembled: dict, basis: str, *, measurement: bool = False, transfers: bool = True, harness: float | None = None,
                   sampling: bool = False) -> list[scenarios.RowInputs]:
    """The declared panel for one basis (E96): rows with a cost on the main workload, in a fixed order.

    With ``measurement`` (the E162 stream), a leaf whose source documents a 95%
    confidence interval (Terminal-Bench's published half-width) is drawn inside that
    interval under a conventional kernel (E165): uniform with the arcsine
    alternative, never assumed normal, clipped to the leaf's domain. With
    ``harness`` (the E19 band width), Bug Hunt is drawn inside the harness-mismatch
    band centred on its observed score, a specification stress for S2 only.
    """

    panel = []
    # O48: the Plan panel is the plan rows; rows of one configuration share every draw (one dependency group).
    for row in (plan_variants(assembled)["rows"] if basis == "plan" else assembled["rows"]):
        cost = _basis_cost(row, basis)
        if row["cost"]["workload"] != assembled["mainWorkload"] or not anchor_math.scoreable(cost):
            continue
        if basis == "plan" and not transfers and transfer_dependent(row):
            continue
        observations = row["evidence"]["observations"]
        leaves = {key: _kernel(value.low, value.high, value.z) for key, value in observations.items()}
        if sampling:  # O39: the S1T stream redraws every leaf with its task-sampling noise
            leaves = {key: sampling_kernel(key, value, row["evidence"]["provenance"].get(key) or {}) for key, value in observations.items()}
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
        meta = {"group": row["configurationId"], "costRatio": cost / row["cost"]["costUsd"]} if basis == "plan" else {}
        panel.append(scenarios.RowInputs(row["id"], leaves, _cost_kernel(row, cost), row["summary"].provisional, meta))
    return panel


def scenario_hash(assembled: dict, frozen: dict, *, n: int, seed: int) -> str:
    """Identity of every scenario input: panels, kernels, anchors, beta, scenario count and seed, and (I83 L1) what decides
    the bar labels: the bar levels, the interval boxes and the blocker and non-candidate sets."""

    blocked, claimed = label_exclusions(assembled)
    finite = lambda value: value if math.isfinite(value) else None  # noqa: E731 - O98's unbounded box hashes as null
    payload = {
        "bars": [[reference["id"], reference["level"]] for reference in frozen.get("barReferences", [])],
        "boxes": [[box.row, box.c_low, finite(box.c_high), box.q_low, box.q_high, box.provisional] for box in api_boxes(assembled)],
        "blocked": sorted(blocked), "claimed": sorted(claimed),
        "beta": BETA,
        "n": n,
        "seed": seed,
        "anchors": {basis: frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis] for basis in BASES},
        "harnessBand": harness_band(assembled["tb4Rows"])["width"],
        "panels": {
            f"{basis}{'-measurement' if measurement else ''}{'-sampling' if sampling else ''}{'' if transfers else '-transfers-off'}": [
                {
                    "row": item.row, "provisional": item.provisional, "cost": [item.cost.family, list(item.cost.params)],
                    "leaves": {key: [kernel.family, list(kernel.params), kernel.target] for key, kernel in sorted(item.leaves.items())},
                }
                for item in scenario_panel(assembled, basis, measurement=measurement, transfers=transfers, sampling=sampling)
            ]
            for basis in BASES
            for measurement, sampling in ((False, False), (True, False), (False, True))
            for transfers in (True, False)
        },
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


# E19/E227: Bug Hunt runs each lab's model in that lab's own agent (and so does a tbench.ai Terminal-Bench gap
# fill; AA's own Terminal-Bench run uses one harness, O37), so a named S2 branch draws those leaves inside a harness-mismatch
# band whose width is the median spread of one configuration's Terminal-Bench score across agents on tbench.ai (pre-registered).
HARNESS_BAND_RULE = (
    "width = median over leaderboard configurations listed under two or more agents of (highest - lowest resolution rate, "
    "percentage points); each agent-run leaf (Bug Hunt, and Terminal-Bench when it is a tbench.ai gap fill rather "
    "than AA's single-harness run, O37) drawn uniformly within the band centred on its observed score (E227); S2 "
    "specification stress, never in Θ"
)


def agent_run_leaves(row: dict) -> list[str]:
    """E227/O37: the observed leaves scored in a lab's own agent, which the harness band stresses."""

    evidence = row["evidence"]
    agent_tb = (evidence["provenance"].get("terminalBench") or {}).get("agent") not in (None, DEFAULT_TB_HARNESS)
    return [key for key in ("bugHunt", "terminalBench") if key in evidence["observations"] and (key != "terminalBench" or agent_tb)]
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
    reasons = {
        row["id"]: assumption_exclusion(row) for row in plan_variants(assembled)["rows"]
        if row["cost"]["workload"] == assembled["mainWorkload"] and anchor_math.scoreable(_basis_cost(row, "plan")) and transfer_dependent(row)
    }
    excluded = sorted(reasons)
    for basis in BASES:
        anchors = frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis]
        results[basis] = []
        for index, (stratum, alternative) in enumerate(SCENARIO_RUNS):
            panel = scenario_panel(assembled, basis, measurement=stratum == MEASUREMENT_STREAM, transfers=transfers_on(stratum), sampling=stratum == SAMPLING_STREAM)
            run = scenarios.shares(panel, stratum, n, seed + index, anchors, BETA, alternative=alternative)
            if basis == "plan":
                run["transfers"] = "on (the displayed record)" if transfers_on(stratum) else "off"
                run["excluded"] = [] if transfers_on(stratum) else [{"row": row_id, "reason": reasons[row_id]} for row_id in excluded]
            results[basis].append(run)
    band = harness_band(assembled["tb4Rows"])
    if band["width"] is not None:
        band["results"] = {}
        for basis in BASES:
            anchors = frozen["workloads"][assembled["mainWorkload"]]["anchors"][basis]
            run = scenarios.shares(scenario_panel(assembled, basis, transfers=False, harness=band["width"]), "S2", n, seed + len(SCENARIO_RUNS), anchors, BETA)
            if basis == "plan":
                run["transfers"], run["excluded"] = "off", [{"row": row_id, "reason": reasons[row_id]} for row_id in excluded]
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


def label_exclusions(assembled: dict) -> tuple[set, set]:
    """The scenario labels' blockers and non-candidates (E186, E233, E222, O94)."""

    # O94: a row whose AA cost omits a pricing term is a blocker like an O29 row: scenario draws keep its published cost, so
    # a label also needs BlockerSafe against its widened box.
    blocked = {row["id"] for row in assembled["rows"] if row["valuationGate"]["outcome"] == GATE_NOT_IN_FORCE or aa_cost_caveat(row)}
    # E233: a provider-claimed row competes in every scenario but is never a candidate for a label; I76 L1, E92/E222: nor
    # is a row on an unverified valuation basis.
    claimed = {row["id"] for row in assembled["rows"] if provider_claimed(row) or row["valuationGate"]["outcome"] == GATE_UNVERIFIED or aa_cost_caveat(row)}
    return blocked, claimed


def bar_labels(assembled: dict, frozen: dict, *, seed: int, batch: int) -> list[dict]:
    """E100/E112: kernel-robust scenario-supported cheapest labels for each pinned bar on the API basis."""

    panel = scenario_panel(assembled, "api")
    boxes = api_boxes(assembled)
    # E147: the compiled dependency graph must be the registered kernel-check object, or the build fails.
    if any(len(component) > 1 for component in scenarios.dependency_components(panel)):
        raise ValueError(f"compiled dependency graph differs from the registered kernel-check object ({REGISTERED_DEPENDENCY})")
    blocked, claimed = label_exclusions(assembled)
    labels = []
    for reference in frozen["barReferences"]:
        bar = _bar_reference(reference)
        # E186: a blocker is never a candidate.
        candidates = [item for item in intervals.cheapest_above_bar(boxes, bar)["possibleCheapest"] if item not in blocked | claimed]
        results = {}
        for candidate in candidates:  # interval rows are main-workload rows with a cost, so all are panel members
            result = scenarios.kernel_robust_cheapest(panel, candidate, reference["level"], seed, batch=batch)
            if result["label"] and not blocker_safe(candidate, bar, boxes, blocked):
                result = {**result, "label": False, "reading": BLOCKER_UNRESOLVED}
            results[candidate] = result
        labels.append({"reference": reference["id"], "level": reference["level"], "status": "evaluated", "candidates": results})
    return labels


# I81 L4: an O29, E222, E228, E233 or O94 blocker alike.
BLOCKER_UNRESOLVED = "scenario frequency passes; blocker unresolved"

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
    "bugHunt": ("bug_hunt.json", "editorial capture of the owner's published results (source commit recorded)"),
    "tb4": ("tb4.json", "scripts/scrape-tb4.js, then valuerank.build_tb4"),
    "codingAgents": ("aa/coding_agents_capture.json", "valuerank.capture_coding_agents"),
    "costCharts": ("aa/cost_charts_capture.json", "scripts/capture-aa-cost-charts.js"),
    "configurationMap": ("v3_configuration_map.json", "editorial pinning from the research capture"),
    "codingAgentsManifest": ("aa/coding_agents_manifest.json", "editorial manifest of every AA Coding Agent Index row, reviewed at each capture (O64)"),
    "frontierCapture": ("aa_frontier_capture.json", "browser capture of AA's Intelligence Index vs cost chart from public tooltips (frontier membership, E195; unevaluated cheaper siblings, E201)"),
    "roster": ("aa_mapping.json", "editorial roster: every configuration AA plots on its rendered frontier or within 3 Index points of it (O51)"),
    "bugHuntScoreboard": ("bug_hunt_scoreboard.json", "the owner's combined scoreboard at the pinned commit (O31 roster check)"),
    "planRoutes": ("plan_cost_routes.json", "editorial Plan evidence registry"),
    "priceRecords": ("price_records.json", "editorial E141 price-record registry (superseded and promotional tariffs)"),
    "leafEvidence": ("leaf_evidence.json", "editorial supplementary leaf evidence and the exhaustive-search log (O36)"),
    "cognitionFrontierCode": ("cognition_frontiercode.json", "Cognition's FrontierCode leaderboard data (https://cognition.com/data/frontiercode-leaderboard/data.json), captured unchanged (O37)"),
    "sweTracks": ("swe_tracks.json", "research/2026-10-23-swe-benchmarks/build_swe_tracks.py from the verified coverage captures (O53-O55)"),
    "planReports": ("plan_reports.json", "editorial table of every O71 user report with the facts E270 needs; the build derives admission from it (O81)"),
    "aaPreviousCapture": ("aa/aa_previous_capture.json", "valuerank.capture_aa: digest of the model-page capture this one replaced (I60)"),
    "sourceRereads": ("source_rereads.json", "editorial record of the O68 re-reads, each 'unchanged' result verified against the re-read file"),
    "aaFootnotes": ("aa/aa_footnote_register.json", "editorial register of every AA note the captures record (the chart's footnotes, and from O103 the model pages, Coding Agent Index and cost charts), by exact text, each classified once (O100, O103)"),
}
CAPTURE_FIELDS = ("capturedAt", "observedAt", "snapshotDate", "asOf", "frozenAt")
SOURCE_INSTANTS = {
    # I84 L4: the register classifies the chart capture's footnotes, so it carries the capture's instant (I60 L6).
    "aaFootnotes": lambda document, documents: (documents.get("frontierCapture") or {}).get("captured_at"),
    "tb4": lambda document, documents: (document.get("source") or {}).get("capturedAt"),
    "bugHunt": lambda document, documents: max((record["observedAt"] for record in document.get("models", []) if record.get("observedAt")), default=None),
    "leafEvidence": lambda document, documents: max((day for search in document.get("searches", [])
                                                     for day in (search.get("searchedOn"), (search.get("openWeb") or {}).get("searchedOn")) if day), default=None),
    # I61 L2: every artifact carries an instant: editorial files take their review or search date, derived files the
    # instant of what they were derived from.
    "codingAgentsManifest": lambda document, documents: document.get("reviewedOn"),
    "frontierCapture": lambda document, documents: document.get("captured_at"),
    "roster": lambda document, documents: (documents.get("frontierCapture") or {}).get("captured_at"),
    "cognitionFrontierCode": lambda document, documents: ((documents.get("leafEvidence") or {}).get("cognitionCapture") or {}).get("capturedOn"),
    "sourceRereads": lambda document, documents: max((item["reReadAt"] for item in document.get("rereads", [])), default=document.get("recordedOn")),
    "planReports": lambda document, documents: max((report["windowEnd"][:10] for report in document.get("reports", [])), default=document.get("recordedOn")),
    "planRoutes": lambda document, documents: max((entry["searchedOn"] for entry in (document.get("evidencePolicy") or {}).get("searchLog") or []),
                                                  default=document.get("asOf")),
}


def load_documents(data: Path) -> dict:
    documents = {key: json.loads((data / relative).read_text()) for key, (relative, _extractor) in EVIDENCE_FILES.items()}
    plan_routes.check_report_window(documents["planRoutes"])
    plan_routes.check_allocation_regimes(documents["planRoutes"])
    plan_routes.check_report_independence(documents["planRoutes"])
    plan_routes.check_selected_analysis(documents["planRoutes"])
    return documents


def evidence_bundle(data: Path) -> dict:
    """E159: content hashes, capture times and extractors of the release's input artifacts (plus the anchor object)."""

    artifacts = []
    anchors = [(f"anchors:{track}" if track != q.DEFAULT_TRACK else "anchors", (track_file(FROZEN_FILE, track), "valuerank.value_v3 freeze"))
               for track in q.TRACKS if (data / track_file(FROZEN_FILE, track)).exists()]
    loaded = {key: json.loads((data / relative).read_bytes()) for key, (relative, _extractor) in EVIDENCE_FILES.items()}
    for key, (relative, extractor) in [*EVIDENCE_FILES.items(), *anchors]:
        content = (data / relative).read_bytes()
        document = json.loads(content)
        # The roster is a bare list with no capture time of its own.
        captured = next((document[field] for field in CAPTURE_FIELDS if isinstance(document.get(field), str)), None) if isinstance(document, dict) else None
        # I60 L6: a derived or editorial artifact carries its source's own latest instant, not its build stamp.
        captured = (SOURCE_INSTANTS[key](document, loaded) or captured) if key in SOURCE_INSTANTS else captured
        if not captured:
            raise ValueError(f"{key}: the evidence bundle has no capture instant for data/{relative} (I61 L2)")
        artifacts.append({"key": key, "artifact": f"data/{relative}", "sha256": hashlib.sha256(content).hexdigest(), "capturedAt": captured, "extractor": extractor})
    return {
        "artifacts": artifacts,
        "bundleHash": hashlib.sha256("".join(item["sha256"] for item in artifacts).encode()).hexdigest(),
        "rebuild": "every published output is rebuilt from these artifacts at the pinned publication clock (npm run verify:docs), never from live pages",
    }


RETAINED_REASON = "Plotted on or within the near gap of AA's rendered frontier (O51)"


def configuration(row: dict) -> dict:
    """A ranked score row's AA identity and whether it is ranked as a frontier or near-frontier family (E187)."""

    return {
        "id": row["id"], "name": row["name"], "family": row.get("family") or row["name"], "effort": row.get("aaVariant"), "aaSlug": row["aaSlug"],
        "aaNote": row.get("aaFrontierFootnote"),
        # O51: every cohort configuration is plotted on or near the frontier, so any inclusion reason makes it a frontier family row.
        "frontierFamily": bool(row.get("rankingInclusionReasons")),
        "familyPrimary": row.get("familyPrimary", True),
        # O58: whether AA plots the configuration on its rendered frontier or within the near gap.
        "aaTier": row.get("aaFrontierTier"),
        "developer": row.get("developer"),
    }


def configurations_from_scores(scores: dict) -> list[dict]:
    """The ranked cohort (fixed cohort policy: the ranking-eligible rows, in table order) with each AA identity."""

    return [configuration(row) for row in scores["models"] if row.get("rankingEligible") is True]


def scenario_seed(release_day: date) -> int:
    return int(release_day.strftime("%Y%m%d"))


def track_summary(track: str) -> dict:
    """O53: which ranking a v3 section is, with its leaves and weights."""

    return {"key": track, "label": q.TRACK_LABELS[track], "default": track == q.DEFAULT_TRACK, "diagnostic": track in q.DIAGNOSTIC_TRACKS,
            # O122: the software-engineering group's nominal share and its coding-specific part.
            "softwareEngineeringShare": sum(leaf.weight for leaf in q.TRACKS[track] if leaf.group == "swe"),
            "codingSpecificShare": q.coding_specific_share(q.TRACKS[track]),
            "leaves": [{"key": leaf.key, "label": leaf.label, "group": leaf.group, "weight": leaf.weight, "source": leaf.source} for leaf in q.TRACKS[track]]}


def build_tracks(configurations: list[dict], data: Path, *, release_day: date) -> dict:
    """O53: one v3 section per ranking, each scored on its own leaf set, anchors and bars."""

    sections = {}
    for track in q.TRACKS:
        with q.active_track(track):
            sections[track] = build(configurations, data, release_day=release_day)
    for track, comparison in leading_comparison(sections).items():
        sections[track]["leadingComparison"] = comparison
    sections[q.DEFAULT_TRACK]["rankingAgreement"] = ranking_agreement(*(sections[track] for track in q.LEADING_TRACKS))
    return sections


def ranking_agreement(first: dict, second: dict) -> dict:
    """E274 (reviewer 71): descriptive tau-b of the two leading rankings' API values on the configurations ranked in both;
    the values are not comparable across rankings, so only their order is compared."""

    values = [{row["id"]: row["api"]["value"] for row in section["rows"]} for section in (first, second)]
    return diagnostics.agreement(*values, label="API value order on configurations ranked in both leading rankings (descriptive)")


def build(configurations: list[dict], data: Path, *, release_day: date) -> dict:
    """The v3 section of scores.json for this release, for the active ranking (O53)."""

    track = q.TRACK
    frozen = json.loads((data / track_file(FROZEN_FILE, track)).read_text())
    assembled = assemble_for_release(configurations, load_documents(data), frozen, release_day=release_day)
    scored = score(assembled, frozen)
    scored["evidenceBundle"] = evidence_bundle(data)
    scored["track"] = track_summary(track)
    scenario_path = data / track_file(SCENARIO_FILE, track)
    document = json.loads(scenario_path.read_text()) if scenario_path.exists() else None
    seed = document["seed"] if document else scenario_seed(release_day)
    count = document["scenarios"] if document else SCENARIO_COUNT
    scored = attach_scenarios(scored, document, scenario_hash(assembled, frozen, n=count, seed=seed))
    return withhold_labels(scored) if track in q.DIAGNOSTIC_TRACKS else scored


DIAGNOSTIC_RANKING = ("diagnostic ranking (O121): computed like the leading rankings for comparison, but it earns no interval or"
                      " scenario label and its gates never hold the release")


def offsetting(influence: dict) -> list[str]:
    """E272: a basis whose cost value-variance allocation (E189) leaves [0, 1]: below 0 the cost term offsets quality
    differences, above 1 the quality term offsets cost differences. The E126 SD ratio cannot show either, as it lies in (0, 1)."""

    found = []
    for basis in BASES:
        share = (((influence.get(basis) or {}).get("commonWorkload") or {}).get("varianceAllocation") or {}).get("cost")
        if share is not None and share < 0.0:
            found.append(f"{basis.upper() if basis == 'api' else 'Plan'}: cost term offsetting ({share:.0%} of value variance)")
        elif share is not None and share > 1.0:
            found.append(f"{basis.upper() if basis == 'api' else 'Plan'}: quality term offsetting (cost {share:.0%} of value variance)")
    return found


def withhold_labels(scored: dict) -> dict:
    """O121: a diagnostic ranking keeps its outputs as comparisons; every label and the release hold are withheld."""

    scored["diagnosticRanking"] = {"rule": DIAGNOSTIC_RANKING, "gateWouldHold": scored["gates"]["hold"]}
    scored["gates"]["holdsRelease"] = False
    for basis in scored["intervals"].values():
        basis["labelsWithheld"] = DIAGNOSTIC_RANKING
    scenarios = scored.get("scenarios") or {}
    if scenarios.get("barLabels"):
        scenarios["barLabels"] = [{"reference": item["reference"], "level": item["level"], "status": "withheld", "reason": DIAGNOSTIC_RANKING}
                                  for item in scenarios["barLabels"]]
    scored["manifest"].append(_rule("diagnostic ranking (O121)", "fired", "no label is issued and the gates are disclosed without holding the release"))
    return scored


def leading_comparison(sections: dict) -> dict:
    """O121: per bar position and basis, the diagnostic ranking's displayed-record cheapest row beside each leading ranking's
    answer for the bar at the same ladder position (each ranking's bar levels are its own), and whether they differ."""

    comparison = {}
    for track in q.DIAGNOSTIC_TRACKS & set(sections):
        own = sections[track]["displayedCheapest"]
        comparison[track] = {
            basis: [
                {"bar": bar["bar"], "cheapest": bar["cheapest"],
                 "leading": {other: next((item["cheapest"] for item in sections[other]["displayedCheapest"][basis]["bars"] if item["bar"] == bar["bar"]), None)
                             for other in q.LEADING_TRACKS if other in sections},
                 "differs": {other: next((item["cheapest"] for item in sections[other]["displayedCheapest"][basis]["bars"] if item["bar"] == bar["bar"]), None) != bar["cheapest"]
                             for other in q.LEADING_TRACKS if other in sections}}
                for bar in own[basis]["bars"]
            ]
            for basis in own if basis in BASES
        }
    return comparison


def main(argv: list[str] | None = None, *, data: Path = DATA) -> int:
    parser = argparse.ArgumentParser(description="ValueRank v3: freeze anchors, run the scenario engine, or compare two anchor versions")
    parser.add_argument("command", choices=("freeze", "scenarios", "dual-run"))
    parser.add_argument("--scenarios", type=int, default=SCENARIO_COUNT)
    parser.add_argument("--previous", type=Path, help="dual-run: the previous anchor object (a v3_frozen.json)")
    parser.add_argument("--track", choices=tuple(q.TRACKS), help="one ranking only (default: every ranking, O53)")
    args = parser.parse_args(argv)
    if args.command == "dual-run" and args.previous is None:
        parser.error("dual-run needs --previous")
    scores = json.loads((data / "scores.json").read_text())
    release_day = utcnow().date()
    configurations, documents = configurations_from_scores(scores), load_documents(data)
    for track in [args.track] if args.track else list(q.TRACKS):
        with q.active_track(track):
            if args.command == "freeze":
                document = freeze(assemble(configurations, documents, release_day=release_day), frozen_at=release_day.isoformat())
                target = data / track_file(FROZEN_FILE, track)
            elif args.command == "dual-run":
                frozen = json.loads((data / track_file(FROZEN_FILE, track)).read_text())
                document = dual_run(assemble_for_release(configurations, documents, frozen, release_day=release_day), json.loads(args.previous.read_text()), frozen)
                target = data / track_file(DUAL_RUN_FILE, track)
            else:
                frozen = json.loads((data / track_file(FROZEN_FILE, track)).read_text())
                assembled = assemble_for_release(configurations, documents, frozen, release_day=release_day)
                document = run_scenarios(assembled, frozen, n=args.scenarios, seed=scenario_seed(release_day))
                target = data / track_file(SCENARIO_FILE, track)
        target.write_text(json.dumps(document, indent=2, ensure_ascii=False, default=_json_default) + "\n")
        print(json.dumps({"wrote": str(target.relative_to(data.parent)), "command": args.command, "track": track}))
    return 0


def _json_default(value):
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


if __name__ == "__main__":
    sys.exit(main())
