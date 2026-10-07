#!/usr/bin/env python3
"""Build ValueRank's primary composite from eligible overlap and AA frontier models.

The comparison roster comes from the mapped AA model data, not the retired
DeepSWE Best leaderboard. Exact DeepSWE and Bug Hunt overlaps remain eligible;
the selected AA Intelligence Index versus total-cost frontier models are also
included with per-row coverage when benchmark results are missing.
"""

from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
VERSION = "v1.9.6"
PUBLISH_DATE = "October 8, 2026"
BUG_HUNT_PRIORITY = 20
BUG_HUNT_EMPHASIS_PRIORITY = 30
DEEPSWE_PRIORITY = 25
FRONTIER_INVENTORY = REFRESH / "aa_reconciliation_inventory.json"

DEVELOPER = {
    "GPT-6 Astra": "OpenAI",
    "Gemini 3.8 Flash": "Google DeepMind",
    "Claude Opus 5": "Anthropic",
    "Claude Opus 5.5": "Anthropic",
    "GPT-5.6 Sol": "OpenAI",
    "Claude Fable 5": "Anthropic",
    "GLM-5.3": "Z AI",
    "Kimi K3": "Moonshot AI",
    "Grok 4.6": "xAI",
    "GPT-5.6 Luna": "OpenAI",
    "GPT-5.5": "OpenAI",
    "Gemini 3.7 Flash": "Google DeepMind",
    "GLM-5.3 Flash": "Z AI",
    "DeepSeek V4 Pro": "DeepSeek",
    "Claude Opus 4.8": "Anthropic",
    "Qwen3.8 Max": "Alibaba",
    "Muse Spark 1.2": "Meta",
    "Claude Sonnet 5": "Anthropic",
    "DeepSeek V4 Flash": "DeepSeek",
    "Gemini 3.6 Flash": "Google DeepMind",
    "GLM-5.2": "Z AI",
    "Gemini 3.5 Flash": "Google DeepMind",
    "GPT-6 Sol": "OpenAI",
    "GPT-6.1 Sol": "OpenAI",
    "GPT-6 Luna": "OpenAI",
    "Grok 4.7": "xAI",
    "MiMo-V2.6-Pro": "Xiaomi",
    "MiMo-V2.6-Flash": "Xiaomi",
}

SHORT = {
    "GPT-6 Astra": "GPT-6 Astra",
    "Gemini 3.8 Flash": "Gem 3.8 Flash",
    "Claude Opus 5": "Opus 5",
    "Claude Opus 5.5": "Opus 5.5",
    "GPT-5.6 Sol": "GPT-5.6 Sol",
    "Claude Fable 5": "Fable 5",
    "GLM-5.3": "GLM-5.3",
    "Kimi K3": "Kimi K3",
    "Grok 4.6": "Grok 4.6",
    "GPT-5.6 Luna": "GPT-5.6 Luna",
    "GPT-5.5": "GPT-5.5",
    "Gemini 3.7 Flash": "Gem 3.7 Flash",
    "GLM-5.3 Flash": "GLM-5.3 Flash",
    "DeepSeek V4 Pro": "DeepSeek V4 Pro",
    "Claude Opus 4.8": "Opus 4.8",
    "Qwen3.8 Max": "Qwen3.8 Max",
    "Muse Spark 1.2": "Muse Spark",
    "Claude Sonnet 5": "Sonnet 5",
    "DeepSeek V4 Flash": "DeepSeek V4 Flash",
    "Gemini 3.6 Flash": "Gem 3.6 Flash",
    "GLM-5.2": "GLM-5.2",
    "Gemini 3.5 Flash": "Gem 3.5 Flash",
    "GPT-6 Sol": "GPT-6 Sol",
    "GPT-6.1 Sol": "GPT-6.1 Sol",
    "GPT-6 Luna": "GPT-6 Luna",
    "Grok 4.7": "Grok 4.7",
    "MiMo-V2.6-Pro": "MiMo V2.6 Pro",
    "MiMo-V2.6-Flash": "MiMo V2.6 Flash",
}

# The priority values are ValueRank's combined score priorities, not the
# Artificial Analysis component weights.  AA's official component weights are
# retained in aa_metrics.json and documented separately.
CANDIDATES = [
    ("costComposite", "Cost", False, 25),
    ("omniNonHallucination", "Non-Hallucination", True, 6),
    ("terminalBenchV4", "Terminal-Bench 4.0", True, 6),
    ("livebenchInstructionFollowing", "Instruction Following (LiveBench)", True, 5),
    ("deepswePassAt1", "DeepSWE v1.1", True, DEEPSWE_PRIORITY),
    ("gdpvalV21", "GDPval-AA v2.1", True, 6),
    ("automationBenchAA", "AutomationBench-AA", True, 5),
    ("aaLcr", "AA-LCR v1.1", True, 4),
    ("omniAccuracy", "AA-Omniscience Accuracy", True, 4),
    ("hle", "HLE", True, 4),
    ("gpqaDiamond", "GPQA Diamond (legacy)", True, 4),
    ("scicode", "SciCode", True, 4),
    ("critpt", "CritPt", True, 3),
    ("intelligenceIndex", "AA Intelligence Index", True, 6),
    ("speed", "Speed", True, 5),
]


def rank_normalize(values, higher_better=True):
    """Convert values to a 0--100 rank score, averaging exact ties."""

    if not values:
        return []
    indexed = sorted(enumerate(values), key=lambda pair: pair[1], reverse=higher_better)
    ranks = [0.0] * len(values)
    cursor = 0
    while cursor < len(indexed):
        end = cursor
        while end + 1 < len(indexed) and indexed[end + 1][1] == indexed[cursor][1]:
            end += 1
        average_rank = sum(range(cursor + 1, end + 2)) / (end - cursor + 1)
        for position in range(cursor, end + 1):
            ranks[indexed[position][0]] = average_rank
        cursor = end + 1
    if len(values) == 1:
        return [100.0]
    return [round(((len(values) - rank) / (len(values) - 1)) * 100, 1) for rank in ranks]


def frontier_effort(variant):
    effort = str(variant or "").casefold().strip()
    if "fallback" in effort:
        effort = effort.split(" with ", 1)[0].split(" (", 1)[0].strip()
    return effort


def require_number(value, label):
    if value is None or isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"missing/non-numeric required value: {label}")
    if not math.isfinite(float(value)):
        raise ValueError(f"non-finite required value: {label}")
    return float(value)


def optional_number(value, label):
    return None if value is None else require_number(value, label)


def comparison_number(value, key, label):
    value = require_number(value, label)
    # New public captures expose whole-point II labels. Compare at that shared
    # precision so older full-precision inputs do not create spurious ordering.
    return round(value) if key == "intelligenceIndex" else value


def build_bug_hunt_emphasis(rows, weights, document):
    matched_rows = [
        row for row in rows
        if row.get("bugHunt", {}).get("matched") is True
        and row.get("deepswePassAt1Pct") is not None
    ]
    if len(matched_rows) < 2:
        emphasis_weights = [{
            "key": "bugHuntFixedOf105",
            "label": "Bug Hunt Bench",
            "higherBetter": True,
            "priority": BUG_HUNT_EMPHASIS_PRIORITY,
            "weightPct": 100.0,
        }]
        matched_ids = {row["id"] for row in matched_rows}
        return {
            "benchmark": document["benchmark"],
            "benchmarkVersion": document["benchmarkVersion"],
            "sourceCommit": document["sourceCommit"],
            "sources": document["sources"],
            "matchedN": 0,
            "availableMeasuredN": len(matched_rows),
            "cohortN": len(rows),
            "coveragePct": 0.0,
            "basePrioritySum": 0,
            "benchmarkPriority": BUG_HUNT_EMPHASIS_PRIORITY,
            "totalPriority": BUG_HUNT_EMPHASIS_PRIORITY,
            "benchmarkWeightPct": 100.0,
            "weights": emphasis_weights,
            "missingModels": [row["name"] for row in rows if row["id"] not in matched_ids],
            "unscoredMeasuredModels": [row["name"] for row in matched_rows],
            "excludedResults": document.get("excludedResults", []),
            "providerClaimAudit": document.get("providerClaimAudit", {}),
            "ranking": [],
        }, [], emphasis_weights

    emphasis_base_weights = []
    for weight in weights:
        key = weight["key"]
        available_rows = [row for row in matched_rows if row.get(key) is not None]
        if len(available_rows) < 2:
            continue
        normalized = rank_normalize(
            [comparison_number(row[key], key, f"{row['id']}.{key}") for row in available_rows],
            weight["higherBetter"],
        )
        for row, score in zip(available_rows, normalized):
            row.setdefault("bugHuntEmphasisDims", {})[key] = score
        emphasis_base_weights.append(weight)

    emphasis_base_priority = sum(weight["priority"] for weight in emphasis_base_weights)
    total_priority = emphasis_base_priority + BUG_HUNT_EMPHASIS_PRIORITY
    emphasis_weights = [
        {
            "key": weight["key"],
            "label": weight["label"],
            "higherBetter": weight["higherBetter"],
            "priority": weight["priority"],
            "weightPct": round(100.0 * weight["priority"] / total_priority, 4),
        }
        for weight in emphasis_base_weights
    ]
    emphasis_weights.append({
        "key": "bugHuntFixedOf105",
        "label": "Bug Hunt Bench",
        "higherBetter": True,
        "priority": BUG_HUNT_EMPHASIS_PRIORITY,
        "weightPct": round(100.0 * BUG_HUNT_EMPHASIS_PRIORITY / total_priority, 4),
    })
    bug_hunt_values = [
        require_number(row["bugHunt"]["fixedOf105"], f"{row['id']}.bugHunt.fixedOf105")
        for row in matched_rows
    ]
    bug_hunt_normalized = rank_normalize(bug_hunt_values, True)
    for row, score in zip(matched_rows, bug_hunt_normalized):
        row.setdefault("bugHuntEmphasisDims", {})["bugHuntFixedOf105"] = score
        available_weights = [
            weight for weight in emphasis_weights
            if weight["key"] in row["bugHuntEmphasisDims"]
        ]
        available_priority = sum(weight["priority"] for weight in available_weights)
        row["bugHuntEmphasisScore"] = round(
            sum(
                row["bugHuntEmphasisDims"][weight["key"]] * weight["priority"]
                for weight in available_weights
            ) / available_priority,
            1,
        )
    ranked_rows = sorted(
        matched_rows,
        key=lambda row: (
            -row["bugHuntEmphasisScore"],
            row["costComposite"] if row["costComposite"] is not None else math.inf,
            row["name"],
        ),
    )
    for rank, row in enumerate(ranked_rows, 1):
        row["bugHuntEmphasisRank"] = rank
    matched_ids = {row["id"] for row in matched_rows}
    missing_models = [row["name"] for row in rows if row["id"] not in matched_ids]
    ranking = {
        "benchmark": document["benchmark"],
        "benchmarkVersion": document["benchmarkVersion"],
        "sourceCommit": document["sourceCommit"],
        "sources": document["sources"],
        "matchedN": len(ranked_rows),
        "cohortN": len(rows),
        "coveragePct": round(100.0 * len(ranked_rows) / len(rows), 2),
        "basePrioritySum": emphasis_base_priority,
        "benchmarkPriority": BUG_HUNT_EMPHASIS_PRIORITY,
        "totalPriority": total_priority,
        "benchmarkWeightPct": round(100.0 * BUG_HUNT_EMPHASIS_PRIORITY / total_priority, 4),
        "weights": emphasis_weights,
        "missingModels": missing_models,
        "excludedResults": document.get("excludedResults", []),
        "providerClaimAudit": document.get("providerClaimAudit", {}),
        "ranking": [
            {
                "rank": row["bugHuntEmphasisRank"],
                "modelId": row["id"],
                "name": row["name"],
                "fixedOf105": row["bugHunt"]["fixedOf105"],
                "emphasisScore": row["bugHuntEmphasisScore"],
                "primaryRank": row["rank"],
            }
            for row in ranked_rows
        ],
    }
    return ranking, ranked_rows, emphasis_weights


def main() -> int:
    deepswe_chart = json.loads((REFRESH / "aa_deepswe.json").read_text())
    aa_document = json.loads((REFRESH / "aa_metrics.json").read_text())
    frontier_inventory = json.loads(FRONTIER_INVENTORY.read_text())
    livebench_document = json.loads((REFRESH / "livebench.json").read_text())
    tb4_document = json.loads((REFRESH / "tb4.json").read_text())
    bug_hunt_document = json.loads((REFRESH / "bug_hunt.json").read_text())
    aa_models = aa_document["models"]
    livebench_models = livebench_document["models"]
    tb4_models = tb4_document["cohortRows"]
    tb4_provider_claims = {
        item["cohortModelId"]: item
        for item in tb4_document.get("providerClaims", [])
        if item.get("eligibleForRanking") is True
    }
    coverage_document = json.loads((REFRESH / "coverage_matrix.json").read_text())
    if not aa_models:
        raise ValueError("AA metrics snapshot must contain a non-empty comparison roster")
    observed_configuration_n = deepswe_chart.get("observedConfigurationN")
    configurations = deepswe_chart.get("configurations", [])
    if (
        isinstance(observed_configuration_n, bool)
        or not isinstance(observed_configuration_n, int)
        or observed_configuration_n < 1
        or len(configurations) != observed_configuration_n
        or deepswe_chart.get("benchmarkTasks") != 113
    ):
        raise ValueError(
            "AA Coding Agent Index DeepSWE chart must match its capture-backed configuration count and 113-task source"
        )
    deepswe_by_id = {}
    for config in configurations:
        model_id = config.get("valueRankModelId")
        if model_id is None:
            continue
        if config.get("matchStatus") != "exact_variant" or model_id in deepswe_by_id:
            raise ValueError(f"invalid or duplicate exact AA DeepSWE mapping for {model_id}")
        score_pct = require_number(config.get("scorePct"), f"{model_id}.DeepSWE scorePct")
        if not 0 <= score_pct <= 100:
            raise ValueError(f"invalid AA DeepSWE score for {model_id}")
        deepswe_by_id[model_id] = config
    if not set(deepswe_by_id).issubset(aa_models):
        raise ValueError("AA DeepSWE mapped model IDs must belong to the current ValueRank roster")

    frontier_rows = frontier_inventory.get("rows", [])
    frontier_universe = frontier_inventory.get("sourceUniverse", {})
    if (
        frontier_inventory.get("completeness", {}).get("status") != "complete"
        or not frontier_rows
        or len(frontier_rows) != frontier_universe.get("observedFrontierPointN")
    ):
        raise ValueError("AA reconciliation inventory must contain the complete observed frontier point set")
    capture_artifact = frontier_inventory.get("captureArtifact")
    if not capture_artifact:
        raise ValueError("AA reconciliation inventory must identify its current frontier capture artifact")
    frontier_capture = json.loads((ROOT / capture_artifact).read_text())
    capture_rows = frontier_capture.get("frontier", [])
    capture_by_url = {item.get("url"): item for item in capture_rows if item.get("url")}
    capture_universe = frontier_capture.get("universe", {})
    if (
        len(capture_rows) != len(frontier_rows)
        or len(capture_by_url) != len(capture_rows)
        or frontier_capture.get("source_url") != frontier_inventory.get("sourceUrl")
        or capture_universe.get("rendered_pareto_vertices") != frontier_universe.get("observedFrontierPointN")
        or capture_universe.get("catalog_models") != frontier_universe.get("selectedModelN")
        or capture_universe.get("plotted_models_with_both_coordinates") != frontier_universe.get("plottedPointN")
    ):
        raise ValueError("AA reconciliation inventory no longer matches its complete direct-observation capture")
    frontier_families = {}
    frontier_urls = set()
    for item in frontier_rows:
        family = item.get("family")
        required_id = item.get("requiredFamilyModelId")
        url = item.get("sourceUrl")
        if not family or not required_id or not url or item.get("directlyObservedFrontier") is not True:
            raise ValueError("Every AA frontier inventory row must carry its observed family, owner URL, and required model ID")
        if url in frontier_urls:
            raise ValueError(f"AA frontier inventory has a duplicate owner URL: {url}")
        frontier_urls.add(url)
        capture_item = capture_by_url.get(url)
        inventory_effort = str(item.get("evaluatedVariant") or "").casefold()
        captured_effort = capture_item.get("effort") if capture_item else None
        expected_capture_effort = (
            None if inventory_effort == "reasoning"
            else frontier_effort(inventory_effort)
        )
        expected_fallback = "fallback" in inventory_effort
        capture_fallback = capture_item.get("fallback") if capture_item else None
        captured_has_fallback = (
            capture_fallback is True
            or "fallback" in str(capture_fallback or "").casefold()
        )
        if (
            capture_item is None
            or capture_item.get("model_name") != item.get("name")
            or capture_item.get("family") != family
            or captured_effort != expected_capture_effort
            or captured_has_fallback != expected_fallback
            or capture_item.get("intelligence_index_display") != item.get("intelligenceIndex")
            or round(require_number(capture_item.get("total_cost_usd"), f"{url}.total_cost_usd"), 2)
            != round(require_number(item.get("totalCostUsd"), f"{url}.totalCostUsd"), 2)
        ):
            raise ValueError(f"AA reconciliation row is inconsistent with its current frontier capture: {url}")
        frontier_families.setdefault(family, []).append(item)

    frontier_selection_by_id = {}
    for family, family_rows in frontier_families.items():
        required_ids = {item["requiredFamilyModelId"] for item in family_rows}
        if len(required_ids) != 1:
            raise ValueError(f"AA frontier family has inconsistent required model IDs: {family}")
        model_id = next(iter(required_ids))
        aa_model = aa_models.get(model_id)
        if aa_model is None:
            raise ValueError(f"AA frontier family model is absent from the selected AA metrics roster: {model_id}")
        selected_rows = [
            item for item in family_rows
            if item.get("sourceUrl") == aa_model.get("aaUrl")
        ]
        if len(selected_rows) != 1:
            raise ValueError(f"AA frontier family must identify one exact selected source URL: {family}")
        frontier_item = selected_rows[0]
        if aa_model.get("aaSlug") != frontier_item.get("aaId"):
            raise ValueError(f"AA frontier source slug does not match selected catalog identity for {model_id}")
        if aa_model.get("displayName") != family:
            raise ValueError(f"AA frontier family does not match selected catalog identity for {model_id}")
        if aa_model.get("aaUrl") != frontier_item["sourceUrl"]:
            raise ValueError(f"AA frontier owner URL does not match selected catalog identity for {model_id}")
        inventory_effort = str(frontier_item.get("evaluatedVariant") or "").casefold()
        selected_effort = aa_model.get("aaVariant")
        if inventory_effort == "reasoning":
            if selected_effort is not None:
                raise ValueError(f"AA reasoning-only frontier identity has an unexpected selected effort for {model_id}")
        else:
            normalized_effort = frontier_effort(inventory_effort)
            if selected_effort != normalized_effort:
                raise ValueError(f"AA frontier effort does not match selected catalog variant for {model_id}")
        fallback = "with fallback" if "fallback" in inventory_effort else None
        aa_labels = " ".join(
            str(aa_model.get(key) or "") for key in ("aaName", "aaShortName")
        ).casefold()
        if fallback and "fallback" not in aa_labels:
            raise ValueError(f"AA frontier fallback does not match selected catalog identity for {model_id}")
        frontier_selection_by_id[model_id] = {
            "family": family,
            "modelName": frontier_item["name"],
            "effort": frontier_item.get("evaluatedVariant"),
            "fallback": fallback,
            "url": frontier_item["sourceUrl"],
            "intelligenceIndexDisplay": frontier_item["intelligenceIndex"],
            "totalCostUsd": frontier_item["totalCostUsd"],
        }

    frontier_selection = {
        "sourceUrl": frontier_inventory["sourceUrl"],
        "captureArtifact": frontier_inventory["captureArtifact"],
        "capturedAt": frontier_capture.get("captured_at"),
        "indexVersion": frontier_capture.get("index_version"),
        "chartTitle": frontier_capture.get("chart_title"),
        "costUnit": frontier_capture.get("cost_unit"),
        "completeness": frontier_inventory["completeness"],
        "sourceUniverse": frontier_universe,
        "configurationN": len(frontier_rows),
        "familyN": len(frontier_families),
        "selectedFamilyModelIds": [
            {
                "modelId": model_id,
                **selection,
            }
            for model_id, selection in sorted(
                frontier_selection_by_id.items(),
                key=lambda item: item[1]["family"],
            )
        ],
    }
    cohort_ids = set(aa_models)
    if set(livebench_models) != cohort_ids:
        raise ValueError("LiveBench snapshot must contain exactly the current AA model cohort")
    bug_hunt_by_id = {item["modelId"]: item for item in bug_hunt_document["models"]}
    if set(bug_hunt_by_id) != cohort_ids:
        raise ValueError("Bug Hunt snapshot must declare exactly the current AA model cohort")
    for model_id, item in bug_hunt_by_id.items():
        if item.get("matched") is True:
            require_number(item.get("fixedOf105"), f"{model_id}.bugHunt.fixedOf105")
            if not 0 <= item["fixedOf105"] <= 105 or item.get("sampleN", 0) < 1:
                raise ValueError(f"invalid Bug Hunt score/sample for {model_id}")

    bug_hunt_owner_matches = [item for item in bug_hunt_by_id.values() if item.get("matched") is True]
    bug_hunt_owner_missing_names = [
        aa_models[model_id]["displayName"]
        for model_id, item in bug_hunt_by_id.items()
        if item.get("matched") is not True
    ]

    rows = []
    for model_id, aa_model in aa_models.items():
        deepswe_model = deepswe_by_id.get(model_id)
        aa_metrics = aa_model["metrics"]
        supplemental = aa_model.get("supplemental", {})
        livebench = livebench_models[model_id]
        tb4 = tb4_models.get(model_id)
        tb4_claim = tb4_provider_claims.get(model_id) if not tb4 else None
        display_name = aa_model["displayName"]
        if display_name not in DEVELOPER or display_name not in SHORT:
            raise ValueError(f"identity mapping missing: {display_name}")
        row = {
            "id": model_id,
            "name": display_name,
            "shortName": SHORT[display_name],
            "developer": DEVELOPER[display_name],
            "frontierSelection": frontier_selection_by_id.get(model_id),
            "bugHunt": bug_hunt_by_id[model_id],
            "rankDeepSWE": deepswe_model.get("sourceOrder") if deepswe_model else None,
            "deepsweEffort": deepswe_model.get("effort") if deepswe_model else None,
            "deepswePassAt1": (require_number(deepswe_model["scorePct"], f"{model_id}.DeepSWE scorePct") / 100) if deepswe_model else None,
            "deepswePassAt1Pct": require_number(deepswe_model["scorePct"], f"{model_id}.DeepSWE scorePct") if deepswe_model else None,
            "deepsweUncertaintyPct": None,
            "deepsweCost": None,
            "deepsweOutputTokens": None,
            "deepsweOutputTokensLabel": None,
            "deepsweAgent": deepswe_model.get("agent") if deepswe_model else None,
            "deepsweScoreConfig": deepswe_model,
            "deepsweAgentSteps": None,
            "aaSlug": aa_model["aaSlug"],
            "aaUrl": aa_model["aaUrl"],
            "aaVariant": aa_model.get("aaVariant"),
            "aaEvalCost": aa_metrics.get("aaEvalCost"),
            "briefcaseElo": aa_metrics.get("briefcaseElo"),
            "briefcaseNormalized": aa_metrics.get("briefcaseNormalized"),
            "intelligenceIndex": aa_metrics.get("intelligenceIndex"),
            "intelligenceIndexStatus": aa_model.get("intelligenceIndexStatus", "measured"),
            "gdpvalV21": aa_metrics.get("gdpvalV21"),
            "gdpvalV21Normalized": aa_metrics.get("gdpvalV21Normalized"),
            "automationBenchAA": aa_metrics.get("automationBenchAA"),
            "aaTerminalBenchV40": aa_metrics.get("terminalBenchV40"),
            "aaTerminalBenchV21": supplemental.get("terminalBenchV21"),
            "legacyTau3Banking": supplemental.get("tauBanking"),
            "livebenchModel": livebench.get("livebenchModel"),
            "livebenchOverall": livebench.get("overallScore"),
            "livebenchInstructionFollowing": livebench.get("instructionFollowingScore"),
            "livebenchCostPerSuccessfulTask": livebench.get("costPerSuccessfulTaskUsd"),
            "livebenchCategoryScores": livebench.get("categoryScores", {}),
            "livebenchTaskScores": livebench.get("tasks", {}),
            "terminalBenchV4": tb4.get("resolutionRate") if tb4 else (tb4_claim.get("value") if tb4_claim else None),
            "terminalBenchV4Pct": tb4.get("resolutionRatePct") if tb4 else (tb4_claim.get("valuePct") if tb4_claim else None),
            "terminalBenchV4UncertaintyPct": tb4.get("uncertaintyPct") if tb4 else None,
            "terminalBenchV4SourceType": "benchmark_owner" if tb4 else ("model_provider_claim" if tb4_claim else None),
            "terminalBenchV4Claim": tb4_claim,
            "terminalBenchV4Cost": tb4.get("costUsd") if tb4 else None,
            "terminalBenchV4Agent": tb4.get("agent") if tb4 else None,
            "terminalBenchV4Effort": tb4.get("model") if tb4 else (tb4_claim.get("evaluatedModel") if tb4_claim else None),
            "terminalBenchV4ReleaseDate": tb4.get("releaseDate") if tb4 else (tb4_claim.get("publishedOn") if tb4_claim else None),
            "terminalBenchV4Model": tb4.get("baseModel") if tb4 else (tb4_claim.get("evaluatedModel") if tb4_claim else None),
            "scicode": aa_metrics.get("scicode"),
            "gdpPdfAllPass": aa_metrics.get("gdpPdfAllPass"),
            "aaLcr": aa_metrics.get("aaLcr"),
            "hle": aa_metrics.get("hle"),
            "gpqaDiamond": aa_metrics.get("gpqaDiamond"),
            "critpt": aa_metrics.get("critpt"),
            "omniAccuracy": aa_metrics.get("omniAccuracy"),
            "omniNonHallucination": aa_metrics.get("omniNonHallucination"),
            "speed": aa_metrics.get("speed"),
            "supplemental": supplemental,
            "extraction": aa_model.get("extraction"),
        }
        rows.append(row)

    overlap_primary_ids = {
        row["id"] for row in rows
        if row["bugHunt"].get("matched") is True
        and row.get("deepswePassAt1Pct") is not None
    }
    frontier_primary_ids = set(frontier_selection_by_id)
    primary_ids = overlap_primary_ids | frontier_primary_ids
    primary_rows = [row for row in rows if row["id"] in primary_ids]
    unranked_rows = [row for row in rows if row["id"] not in primary_ids]
    if not primary_rows:
        raise ValueError("Primary cohort requires an exact AA overlap or a mapped AA frontier model")

    aa_cost_rows = [row for row in primary_rows if row["aaEvalCost"] is not None]
    max_aa_cost = (
        max(require_number(row["aaEvalCost"], f"{row['id']}.aaEvalCost") for row in aa_cost_rows)
        if aa_cost_rows
        else None
    )
    if max_aa_cost is not None and max_aa_cost <= 0:
        raise ValueError("AA evaluation cost normalization requires a positive maximum")
    cost_mode = "aa-only" if aa_cost_rows else "unavailable (AA evaluation cost has no primary coverage)"
    for row in primary_rows:
        row["deepSweCostNorm"] = None
        row["aaCostNorm"] = (
            round((require_number(row["aaEvalCost"], f"{row['id']}.aaEvalCost") / max_aa_cost) * 100, 2)
            if row["aaEvalCost"] is not None and max_aa_cost is not None
            else None
        )
        row["costComposite"] = row["aaCostNorm"]
        row["costMode"] = cost_mode
    for row in unranked_rows:
        row["deepSweCostNorm"] = None
        row["aaCostNorm"] = None
        row["costComposite"] = None
        row["costMode"] = cost_mode

    coverage = {}
    for key, label, higher_better, priority in CANDIDATES:
        missing = [row["name"] for row in primary_rows if row.get(key) is None]
        source_missing = [row["name"] for row in rows if row.get(key) is None]
        coverage[key] = {
            "label": label,
            "missing": missing,
            "nMissing": len(missing),
            "availableN": len(primary_rows) - len(missing),
            "cohortN": len(primary_rows),
            "sourceMissing": source_missing,
            "sourceCohortN": len(rows),
            "sourceAvailableN": len(rows) - len(source_missing),
            "higherBetter": higher_better,
            "priority": priority,
        }
    retained = [candidate for candidate in CANDIDATES if coverage[candidate[0]]["availableN"] >= 2]
    dropped = [
        {
            "key": key,
            "label": label,
            "missing": coverage[key]["missing"],
            "sourceMissing": coverage[key]["sourceMissing"],
            "availableN": coverage[key]["availableN"],
            "reason": (
                "fewer than two primary models have observed values; no comparative percentile is assigned"
            ),
        }
        for key, label, _higher_better, _priority in CANDIDATES
        if coverage[key]["availableN"] < 2
    ]
    raw_priority_sum = sum(candidate[3] for candidate in retained)
    base_weights = [
        {
            "key": key,
            "label": label,
            "higherBetter": higher_better,
            "priority": priority,
            "weightPct": round(100.0 * priority / raw_priority_sum, 4),
        }
        for key, label, higher_better, priority in retained
    ] if raw_priority_sum else []
    primary_bug_hunt_value_n = sum(
        row["bugHunt"].get("matched") is True for row in primary_rows
    )
    primary_has_bug_hunt_dimension = primary_bug_hunt_value_n >= 2
    primary_total_priority = raw_priority_sum + (
        BUG_HUNT_PRIORITY if primary_has_bug_hunt_dimension else 0
    )
    weights = [
        {
            **weight,
            "weightPct": round(100.0 * weight["priority"] / primary_total_priority, 4),
        }
        for weight in base_weights
    ]
    if primary_has_bug_hunt_dimension:
        weights.append({
            "key": "bugHuntFixedOf105",
            "label": "Bug Hunt Bench",
            "higherBetter": True,
            "priority": BUG_HUNT_PRIORITY,
            "weightPct": round(100.0 * BUG_HUNT_PRIORITY / primary_total_priority, 4),
        })
    bug_hunt_primary_weight_pct = next(
        (weight["weightPct"] for weight in weights if weight["key"] == "bugHuntFixedOf105"),
        0.0,
    )

    for row in rows:
        row["dims"] = {}
        row["rankingEligible"] = row["id"] in primary_ids
        row["rankingInclusionReasons"] = []
        if row["id"] in overlap_primary_ids:
            row["rankingInclusionReasons"].append("Exact AA DeepSWE and eligible Bug Hunt overlap")
        if row["id"] in frontier_primary_ids:
            row["rankingInclusionReasons"].append(
                "Required AA Intelligence Index versus total-evaluation-cost frontier family"
            )
        row["missingFields"] = [key for key, _label, _higher, _priority in CANDIDATES if row.get(key) is None]
        row["rankingExclusionReasons"] = []
        if row["bugHunt"].get("matched") is not True and row["rankingEligible"]:
            row["missingFields"].append("bugHuntFixedOf105")
        if not row["rankingEligible"] and row["bugHunt"].get("matched") is not True:
            row["missingFields"].append("bugHuntFixedOf105")
            if row["bugHunt"].get("matchStatus") == "reasoning_variant_unverified":
                owner_configurations = row["bugHunt"].get("availableOwnerConfigurations", [])
                available_scores = [
                    f"{config['fixedOf105']:g}/105"
                    for config in owner_configurations
                    if isinstance(config.get("fixedOf105"), (int, float))
                    and not isinstance(config.get("fixedOf105"), bool)
                ]
                owner_result_note = (
                    f"owner default result {', '.join(available_scores)} available"
                    if available_scores else "owner default result available"
                )
                row["rankingExclusionReasons"].append(
                    "No eligible exact-variant Bug Hunt match; " + owner_result_note
                    + "; selected reasoning equivalence is unverified"
                )
            else:
                row["rankingExclusionReasons"].append("No eligible exact-model Bug Hunt result in the selected source snapshot")
        if not row["rankingEligible"] and row.get("deepswePassAt1Pct") is None:
            row["rankingExclusionReasons"].append("No exact-variant AA DeepSWE result in the selected source snapshot")
        if not row["rankingEligible"]:
            row["rankingExclusionReasons"].append("Not a required selected AA frontier family model")
            row["rank"] = None
            row["qualityRank"] = None
            row["overallScore"] = None
            row["qualityScore"] = None
            row["vRanks"] = {}
            row["pareto"] = None
            row["isMissing"] = True
            row["rankingStatus"] = "excluded_from_primary_cohort"
    for weight in weights:
        key = weight["key"]
        available_rows = []
        values = []
        for row in primary_rows:
            if key == "bugHuntFixedOf105":
                value = row["bugHunt"].get("fixedOf105") if row["bugHunt"].get("matched") is True else None
            else:
                value = row.get(key)
            if value is None:
                continue
            available_rows.append(row)
            values.append(comparison_number(value, key, f"{row['id']}.{key}"))
        if len(available_rows) < 2:
            continue
        normalized = rank_normalize(values, weight["higherBetter"])
        for row, score in zip(available_rows, normalized):
            row["dims"][key] = score

    effective_keys = [weight["key"] for weight in weights]
    for row in rows:
        available_weights = [weight for weight in weights if weight["key"] in row["dims"]]
        available_priority = sum(weight["priority"] for weight in available_weights)
        row["metricCoverage"] = {
            "availablePriority": available_priority,
            "totalPriority": primary_total_priority,
            "coveragePct": round(100.0 * available_priority / primary_total_priority, 2)
            if primary_total_priority
            else 0.0,
            "missingKeys": [key for key in effective_keys if key not in row["dims"]],
        }

    for row in primary_rows:
        available_weights = [weight for weight in weights if weight["key"] in row["dims"]]
        available_priority = sum(weight["priority"] for weight in available_weights)
        quality_weights = [
            weight for weight in available_weights if weight["key"] != "costComposite"
        ]
        quality_priority = sum(weight["priority"] for weight in quality_weights)
        row["overallScore"] = (
            round(
                sum(row["dims"][weight["key"]] * weight["priority"] for weight in available_weights)
                / available_priority,
                1,
            )
            if available_priority and quality_priority
            else None
        )
        row["qualityScore"] = (
            round(
                sum(row["dims"][weight["key"]] * weight["priority"] for weight in quality_weights)
                / quality_priority,
                1,
            )
            if quality_priority
            else None
        )
        row["isMissing"] = bool(row["missingFields"] or row["metricCoverage"]["missingKeys"])
        row["rank"] = None
        row["qualityRank"] = None
        row["pareto"] = None
        row["rankingStatus"] = (
            "rankable" if row["qualityScore"] is not None
            else "unranked_no_quality_dimension"
        )
        row["vRanks"] = {
            weight["key"]: row["dims"][weight["key"]]
            for weight in weights
            if weight["key"] in row["dims"]
        }

    by_overall = sorted(
        [
            row for row in primary_rows
            if row["overallScore"] is not None and row["qualityScore"] is not None
        ],
        key=lambda row: (
            -row["overallScore"],
            row["costComposite"] if row["costComposite"] is not None else math.inf,
            row["name"],
        ),
    )
    for rank, row in enumerate(by_overall, 1):
        row["rank"] = rank
        row["rankingStatus"] = "ranked"
    unscored_primary_rows = sorted(
        [row for row in primary_rows if row["overallScore"] is None],
        key=lambda row: row["name"],
    )
    by_quality = sorted(
        [row for row in primary_rows if row["qualityScore"] is not None],
        key=lambda row: (
            -row["qualityScore"],
            row["costComposite"] if row["costComposite"] is not None else math.inf,
            row["name"],
        ),
    )
    for rank, row in enumerate(by_quality, 1):
        row["qualityRank"] = rank

    pareto_candidates = [
        row for row in primary_rows
        if row["costComposite"] is not None and row["qualityScore"] is not None
    ]
    pareto = []
    for row in pareto_candidates:
        dominated = any(
            other["id"] != row["id"]
            and other["costComposite"] <= row["costComposite"]
            and other["qualityScore"] >= row["qualityScore"]
            and (
                other["costComposite"] < row["costComposite"]
                or other["qualityScore"] > row["qualityScore"]
            )
            for other in pareto_candidates
        )
        row["pareto"] = not dominated
        if row["pareto"]:
            pareto.append(row["name"])

    frontier_rows_without_quality = [
        row["id"]
        for row in primary_rows
        if row["id"] in frontier_primary_ids
        and (
            row["qualityScore"] is None
            or not math.isfinite(row["qualityScore"])
        )
    ]
    if frontier_rows_without_quality:
        raise ValueError(
            "Every required AA frontier model must have a finite non-cost quality score: "
            f"{frontier_rows_without_quality}"
        )

    # Retain a stronger Bug Hunt emphasis view as an optional companion to the primary rank.
    bug_hunt_emphasis, bug_hunt_ranked_rows, bug_hunt_weights = build_bug_hunt_emphasis(
        rows, base_weights, bug_hunt_document
    )
    primary_bug_hunt_matches = [
        row for row in primary_rows if row["bugHunt"].get("matched") is True
    ]
    primary_bug_hunt_missing_names = [
        row["name"] for row in primary_rows if row["bugHunt"].get("matched") is not True
    ]
    if len(primary_bug_hunt_matches) < 2:
        dropped.append({
            "key": "bugHuntFixedOf105",
            "label": "Bug Hunt Bench bugs fixed out of 105",
            "missing": primary_bug_hunt_missing_names,
            "sourceMissing": bug_hunt_owner_missing_names,
            "availableN": len(primary_bug_hunt_matches),
            "reason": "fewer than two primary models have eligible results; no comparative percentile is assigned",
        })

    # Keep source extraction coverage and add score-specific and explicitly
    # labelled external benchmark coverage.
    primary_dimension_keys = {weight["key"] for weight in weights}
    score_coverage = {
        key: {
            "label": item["label"],
            "availableN": item["cohortN"] - item["nMissing"],
            "cohortN": item["cohortN"],
            "coveragePct": round(100.0 * (item["cohortN"] - item["nMissing"]) / item["cohortN"], 2),
            "normalizableN": item["availableN"] if item["availableN"] >= 2 else 0,
            "missingModels": item["missing"],
            "sourceAvailableN": item["sourceAvailableN"],
            "sourceCohortN": item["sourceCohortN"],
            "sourceMissingModels": item["sourceMissing"],
            "includedInPrimaryScore": key in primary_dimension_keys,
        }
        for key, item in coverage.items()
    }
    score_coverage["bugHuntFixedOf105"] = {
        "label": "Bug Hunt Bench bugs fixed out of 105",
        "availableN": len(primary_bug_hunt_matches),
        "cohortN": len(primary_rows),
        "coveragePct": round(100.0 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
        "normalizableN": len(primary_bug_hunt_matches) if len(primary_bug_hunt_matches) >= 2 else 0,
        "missingModels": primary_bug_hunt_missing_names,
        "sourceAvailableN": len(bug_hunt_owner_matches),
        "sourceCohortN": len(rows),
        "sourceMissingModels": bug_hunt_owner_missing_names,
        "rankableOverlapN": len(overlap_primary_ids),
        "includedInPrimaryScore": "bugHuntFixedOf105" in primary_dimension_keys,
    }
    external_coverage = {
        "livebenchOverall": {
            "group": "supplemental",
            "label": "LiveBench Overall Score",
            "availableN": sum(row["livebenchOverall"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["livebenchOverall"] is not None for row in primary_rows) / len(primary_rows), 2),
            "missingModels": [row["name"] for row in primary_rows if row["livebenchOverall"] is None],
            "sourceAvailableN": livebench_document["matchedN"],
            "sourceCohortN": len(rows),
            "sourceMissingModels": livebench_document["missingModels"],
            "includedInPrimaryScore": False,
            "sourceRelease": livebench_document["release"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": [
                record["name"]
                for record in livebench_document.get("supplementalModels", {}).values()
                if record.get("matched")
            ],
        },
        "livebenchInstructionFollowing": {
            "group": "primary" if "livebenchInstructionFollowing" in primary_dimension_keys else "supplemental",
            "label": "Instruction Following (LiveBench)",
            "availableN": sum(row["livebenchInstructionFollowing"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["livebenchInstructionFollowing"] is not None for row in primary_rows) / len(primary_rows), 2),
            "missingModels": [row["name"] for row in primary_rows if row["livebenchInstructionFollowing"] is None],
            "sourceAvailableN": livebench_document["matchedN"],
            "sourceCohortN": len(rows),
            "sourceMissingModels": livebench_document["missingModels"],
            "includedInPrimaryScore": "livebenchInstructionFollowing" in primary_dimension_keys,
            "sourceRelease": livebench_document["release"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": [
                record["name"]
                for record in livebench_document.get("supplementalModels", {}).values()
                if record.get("matched")
            ],
        },
        "livebenchCostPerSuccessfulTask": {
            "group": "supplemental",
            "label": "LiveBench Cost Per Successful Task",
            "availableN": sum(row["livebenchCostPerSuccessfulTask"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["livebenchCostPerSuccessfulTask"] is not None for row in primary_rows) / len(primary_rows), 2),
            "missingModels": [row["name"] for row in primary_rows if row["livebenchCostPerSuccessfulTask"] is None],
            "sourceAvailableN": livebench_document["matchedN"],
            "sourceCohortN": len(rows),
            "sourceMissingModels": livebench_document["missingModels"],
            "includedInPrimaryScore": False,
            "sourceRelease": livebench_document["release"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": [
                record["name"]
                for record in livebench_document.get("supplementalModels", {}).values()
                if record.get("matched")
            ],
        },
        "terminalBenchV4": {
            "group": "primary" if "terminalBenchV4" in primary_dimension_keys else "supplemental",
            "label": "Terminal-Bench 4.0",
            "availableN": sum(row["terminalBenchV4"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["terminalBenchV4"] is not None for row in primary_rows) / len(primary_rows), 2),
            "sourceAvailableN": tb4_document.get("rankingAvailableN", tb4_document["matchedN"]),
            "sourceCohortN": len(rows),
            "officialMatchedN": tb4_document["matchedN"],
            "providerClaimMatchedN": tb4_document.get("providerClaimN", 0),
            "missingModels": [row["name"] for row in primary_rows if row["terminalBenchV4"] is None],
            "sourceMissingModels": tb4_document.get("rankingMissingModels", tb4_document["missingModels"]),
            "includedInPrimaryScore": "terminalBenchV4" in primary_dimension_keys,
            "sourceRelease": tb4_document["version"],
        },
        "bugHuntFixedOf105": {
            "group": "primary" if "bugHuntFixedOf105" in primary_dimension_keys else "supplemental",
            "label": "Bug Hunt Bench bugs fixed out of 105",
            "availableN": len(primary_bug_hunt_matches),
            "cohortN": len(primary_rows),
            "coveragePct": round(100.0 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
            "missingModels": primary_bug_hunt_missing_names,
            "sourceAvailableN": len(bug_hunt_owner_matches),
            "sourceCohortN": len(rows),
            "sourceCoveragePct": round(100.0 * len(bug_hunt_owner_matches) / len(rows), 2),
            "sourceMissingModels": bug_hunt_owner_missing_names,
            "includedInPrimaryScore": "bugHuntFixedOf105" in primary_dimension_keys,
            "includedInBugHuntEmphasisRanking": bug_hunt_emphasis["matchedN"] >= 2,
            "sourceRelease": bug_hunt_document["benchmarkVersion"],
            "sourceCommit": bug_hunt_document["sourceCommit"],
        },
    }
    coverage_document["cohort"] = f"Artificial Analysis v4.3.2 mapped {len(rows)}-model ValueRank comparison roster"
    coverage_document["cohortN"] = len(rows)
    coverage_document["deepSweSource"] = deepswe_chart["source"]
    coverage_document["deepSweConfigurationsN"] = len(deepswe_chart["configurations"])
    coverage_document["deepSweObservedConfigurationN"] = observed_configuration_n
    coverage_document["frontierSelection"] = frontier_selection
    source_fields = dict(coverage_document.get("fields", {}))
    source_fields.update(external_coverage)
    coverage_document["fields"] = source_fields
    coverage_document["externalBenchmarks"] = {
        "livebench": {
            "release": livebench_document["release"],
            "matchedN": livebench_document["matchedN"],
            "cohortN": livebench_document["cohortN"],
            "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
            "supplementalModels": list(livebench_document.get("supplementalModels", {})),
            "pareto": livebench_document["pareto"],
        },
        "terminalBenchV4": {
            "version": tb4_document["version"],
            "matchedN": tb4_document["matchedN"],
            "providerClaimN": tb4_document.get("providerClaimN", 0),
            "rankingAvailableN": tb4_document.get("rankingAvailableN", tb4_document["matchedN"]),
            "cohortN": tb4_document["cohortN"],
        },
        "bugHunt": {
            "version": bug_hunt_document["benchmarkVersion"],
            "sourceCommit": bug_hunt_document["sourceCommit"],
            "matchedN": len(bug_hunt_owner_matches),
            "rankableOverlapN": len(overlap_primary_ids),
            "sourceCohortN": len(rows),
            "primaryCohortN": len(primary_rows),
            "sourceCoveragePct": round(100 * len(bug_hunt_owner_matches) / len(rows), 2),
            "primaryCoveragePct": round(100 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
            "primaryWeightPct": bug_hunt_primary_weight_pct,
            "emphasisWeightPct": bug_hunt_emphasis["benchmarkWeightPct"],
        },
    }
    coverage_document["scoring"] = {
        "version": VERSION,
        "cohortN": len(primary_rows),
        "scoredN": len(by_overall),
        "exactBenchmarkOverlapN": len(overlap_primary_ids),
        "frontierRequiredModelN": len(frontier_primary_ids),
        "frontierRequiredModelIds": sorted(frontier_primary_ids),
        "frontierSelection": frontier_selection,
        "sourceCohortN": len(rows),
        "rankingExcludedModels": [row["name"] for row in unranked_rows],
        "rankingExclusions": [
            {"modelId": row["id"], "name": row["name"], "reasons": row["rankingExclusionReasons"]}
            for row in unranked_rows
        ],
        "costMode": cost_mode,
        "costCoverage": {
            "availableN": len(aa_cost_rows),
            "cohortN": len(primary_rows),
            "sourceAvailableN": sum(row["aaEvalCost"] is not None for row in rows),
            "sourceCohortN": len(rows),
            "missingModels": [row["name"] for row in primary_rows if row["aaEvalCost"] is None],
            "sourceMissingModels": [row["name"] for row in rows if row["aaEvalCost"] is None],
            "selectiveSubstitution": False,
        },
        "retainedDimensions": [weight["key"] for weight in weights],
        "droppedDimensions": dropped,
        "zeroGap": (
            not dropped
            and not any(
                item["missingModels"]
                for item in score_coverage.values()
                if item["includedInPrimaryScore"]
            )
        ),
        "noNeutralFills": True,
        "fields": score_coverage,
        "alternateRankings": {
            "bugHuntEmphasis": {
                "matchedN": bug_hunt_emphasis["matchedN"],
                "cohortN": bug_hunt_emphasis["cohortN"],
                "benchmarkWeightPct": bug_hunt_emphasis["benchmarkWeightPct"],
                "sourceCommit": bug_hunt_emphasis["sourceCommit"],
                "ranking": [
                    {"rank": item["rank"], "modelId": item["modelId"], "score": item["emphasisScore"]}
                    for item in bug_hunt_emphasis["ranking"]
                ],
            }
        },
    }

    observed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    ranking_summary = {
        "version": VERSION,
        "publishDate": PUBLISH_DATE,
        "observedAt": observed_at,
        "cohortN": len(primary_rows),
        "scoredN": len(by_overall),
        "exactBenchmarkOverlapN": len(overlap_primary_ids),
        "frontierRequiredModelN": len(frontier_primary_ids),
        "frontierSelection": frontier_selection,
        "sourceCohortN": len(rows),
        "rankingExcludedModels": [row["name"] for row in unranked_rows],
        "rankingExclusions": coverage_document["scoring"]["rankingExclusions"],
        "deepsweSource": deepswe_chart["source"],
        "deepsweObservedAt": deepswe_chart["observedAt"],
        "deepsweBenchmarkVersion": deepswe_chart["benchmark"],
        "deepsweConfigurationsN": len(deepswe_chart["configurations"]),
        "aaBenchmarkVersion": aa_document.get("benchmarkVersion"),
        "retainedDimensionN": len(weights),
        "retainedDimensions": [weight["label"] for weight in weights],
        "droppedDimensions": dropped,
        "zeroGap": coverage_document["scoring"]["zeroGap"],
        "costMode": cost_mode,
        "costCoverage": coverage_document["scoring"]["costCoverage"],
        "pareto": pareto,
        "topFive": [
            {"rank": row["rank"], "name": row["name"], "overallScore": row["overallScore"], "qualityScore": row["qualityScore"]}
            for row in by_overall[:5]
        ],
        "bugHuntEmphasis": {
            "matchedN": bug_hunt_emphasis["matchedN"],
            "cohortN": bug_hunt_emphasis["cohortN"],
            "benchmarkWeightPct": bug_hunt_emphasis["benchmarkWeightPct"],
            "sourceCommit": bug_hunt_emphasis["sourceCommit"],
            "topFive": [
                {"rank": item["rank"], "name": item["name"], "score": item["emphasisScore"], "fixedOf105": item["fixedOf105"]}
                for item in bug_hunt_emphasis["ranking"][:5]
            ],
        },
        "externalCoverage": {
            "livebench": f"{livebench_document['matchedN']}/{livebench_document['cohortN']}",
            "livebenchPublishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "livebenchSupplementalModels": list(livebench_document.get("supplementalModels", {})),
            "bugHunt": (
                f"{len(bug_hunt_owner_matches)}/{len(rows)} owner matches; "
                f"{len(overlap_primary_ids)} exact DeepSWE and Bug Hunt overlaps plus "
                f"{len(frontier_primary_ids)} selected AA frontier family models enter the primary cohort"
            ),
            "terminalBenchV4": f"{tb4_document.get('rankingAvailableN', tb4_document['matchedN'])}/{tb4_document['cohortN']} including {tb4_document.get('providerClaimN', 0)} provider claim",
        },
    }
    manifest_path = ROOT / "research" / "2026-09-29-valuerank-refresh-v4-3-2" / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["scoring"] = ranking_summary
    manifest["scoring"]["weights"] = weights
    manifest["scoring"]["bugHuntEmphasisRanking"] = bug_hunt_emphasis
    manifest["scoring"]["primaryMissingFields"] = {
        key: data["missing"] for key, data in coverage.items() if data["missing"]
    }
    manifest["scoring"]["providerClaimsUsed"] = [
        {"model": row["name"], "benchmark": "Terminal-Bench 4.0", "sourceUrl": row["terminalBenchV4Claim"]["sourceUrl"]}
        for row in primary_rows if row.get("terminalBenchV4Claim")
    ]

    (REFRESH / "scores.json").write_text(
        json.dumps(
            {
                "version": VERSION,
                "publishDate": PUBLISH_DATE,
                "observedAt": observed_at,
                "benchmarkVersion": aa_document.get("benchmarkVersion"),
                "deepsweBenchmarkVersion": deepswe_chart["benchmark"],
                "deepsweSource": deepswe_chart["source"],
                "deepsweConfigurationsN": len(deepswe_chart["configurations"]),
                "deepsweObservedConfigurationN": observed_configuration_n,
                "cohort": {
                    "n": len(primary_rows),
                    "scoredN": len(by_overall),
                    "sourceN": len(rows),
                    "exactBenchmarkOverlapN": len(overlap_primary_ids),
                    "frontierRequiredModelN": len(frontier_primary_ids),
                    "source": "Artificial Analysis Coding Agent Index v1.5 DeepSWE v1.1 chart",
                    "sourceUpdatedOn": deepswe_chart["observedAt"],
                },
                "frontierSelection": frontier_selection,
                "weights": weights,
                "bugHuntEmphasisRanking": bug_hunt_emphasis,
                "costMode": cost_mode,
                "costCoverage": coverage_document["scoring"]["costCoverage"],
                "models": by_overall + unscored_primary_rows + sorted(unranked_rows, key=lambda row: row["name"]),
                "rankedModelIds": [row["id"] for row in by_overall],
                "pareto": pareto,
                "externalBenchmarks": {
                    "livebench": {
                        "release": livebench_document["release"],
                        "matchedN": livebench_document["matchedN"],
                        "cohortN": livebench_document["cohortN"],
                        "publishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
                        "supplementalMatchedN": livebench_document.get("supplementalMatchedN", 0),
                        "supplementalModels": list(livebench_document.get("supplementalModels", {})),
                        "pareto": livebench_document["pareto"],
                    },
                    "terminalBenchV4": {
                        "version": tb4_document["version"],
                        "matchedN": tb4_document["matchedN"],
                        "providerClaimN": tb4_document.get("providerClaimN", 0),
                        "rankingAvailableN": tb4_document.get("rankingAvailableN", tb4_document["matchedN"]),
                        "cohortN": tb4_document["cohortN"],
                    },
                    "bugHunt": {
                        "version": bug_hunt_document["benchmarkVersion"],
                        "matchedN": len(bug_hunt_owner_matches),
                        "rankableOverlapN": len(overlap_primary_ids),
                        "cohortN": len(rows),
                        "primaryCohortN": len(primary_rows),
                        "primaryCoveragePct": round(100.0 * len(primary_bug_hunt_matches) / len(primary_rows), 2),
                        "primaryWeightPct": bug_hunt_primary_weight_pct,
                        "sourceCommit": bug_hunt_document["sourceCommit"],
                    },
                },
                "appendixNonRanked": [
                    {
                        "id": row["id"],
                        "name": row["name"],
                        "reason": "; ".join(row["rankingExclusionReasons"]),
                    }
                    for row in unranked_rows
                ],
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )
    (REFRESH / "coverage_matrix.json").write_text(json.dumps(coverage_document, indent=2, ensure_ascii=False) + "\n")
    (REFRESH / "ranking_summary.json").write_text(json.dumps(ranking_summary, indent=2, ensure_ascii=False) + "\n")
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    print(json.dumps({
        "version": VERSION,
        "n": len(primary_rows),
        "sourceN": len(rows),
        "retainedDimensions": len(weights),
        "dropped": dropped,
        "zeroGap": ranking_summary["zeroGap"],
        "topFive": ranking_summary["topFive"],
        "bugHuntEmphasisTopFive": ranking_summary["bugHuntEmphasis"]["topFive"],
        "outputs": [
            ".refresh/v1.4/scores.json",
            ".refresh/v1.4/coverage_matrix.json",
            ".refresh/v1.4/ranking_summary.json",
        ],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
