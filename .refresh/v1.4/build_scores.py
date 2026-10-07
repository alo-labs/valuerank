#!/usr/bin/env python3
"""Build ValueRank's primary composite on the exact AA DeepSWE and Bug Hunt overlap.

The current comparison roster comes from the mapped AA model data, not the retired
DeepSWE Best leaderboard. Only exact model-variant chart rows with an eligible
Bug Hunt result enter the main rank; missing values are never neutral-filled.
    """

from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
VERSION = "v1.9.4"
PUBLISH_DATE = "October 8, 2026"
BUG_HUNT_PRIORITY = 20
BUG_HUNT_EMPHASIS_PRIORITY = 30
DEEPSWE_PRIORITY = 25

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


def require_number(value, label):
    if value is None or isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"missing/non-numeric required value: {label}")
    if not math.isfinite(float(value)):
        raise ValueError(f"non-finite required value: {label}")
    return float(value)


def optional_number(value, label):
    return None if value is None else require_number(value, label)


def build_bug_hunt_emphasis(rows, weights, base_priority_sum, document):
    matched_rows = [row for row in rows if row.get("rankingEligible") is True]
    if len(matched_rows) < 2:
        raise ValueError("Bug Hunt emphasis ranking requires at least two matched models")
    total_priority = base_priority_sum + BUG_HUNT_EMPHASIS_PRIORITY
    emphasis_weights = [
        {
            "key": weight["key"],
            "label": weight["label"],
            "higherBetter": weight["higherBetter"],
            "priority": weight["priority"],
            "weightPct": round(100.0 * weight["priority"] / total_priority, 4),
        }
        for weight in weights
    ]
    emphasis_weights.append({
        "key": "bugHuntFixedOf105",
        "label": "Bug Hunt Bench",
        "higherBetter": True,
        "priority": BUG_HUNT_EMPHASIS_PRIORITY,
        "weightPct": round(100.0 * BUG_HUNT_EMPHASIS_PRIORITY / total_priority, 4),
    })
    for weight in weights:
        key = weight["key"]
        values = [require_number(row[key], f"{row['id']}.{key}") for row in matched_rows]
        normalized = rank_normalize(values, weight["higherBetter"])
        for row, score in zip(matched_rows, normalized):
            row.setdefault("bugHuntEmphasisDims", {})[key] = score
    bug_hunt_values = [
        require_number(row["bugHunt"]["fixedOf105"], f"{row['id']}.bugHunt.fixedOf105")
        for row in matched_rows
    ]
    bug_hunt_normalized = rank_normalize(bug_hunt_values, True)
    for row, score in zip(matched_rows, bug_hunt_normalized):
        row.setdefault("bugHuntEmphasisDims", {})["bugHuntFixedOf105"] = score
        row["bugHuntEmphasisScore"] = round(
            sum(
                row["bugHuntEmphasisDims"][weight["key"]] * weight["weightPct"] / 100
                for weight in emphasis_weights
            ),
            1,
        )
    ranked_rows = sorted(
        matched_rows,
        key=lambda row: (-row["bugHuntEmphasisScore"], row["costComposite"], row["name"]),
    )
    for rank, row in enumerate(ranked_rows, 1):
        row["bugHuntEmphasisRank"] = rank
    missing_models = [row["name"] for row in rows if row.get("rankingEligible") is not True]
    ranking = {
        "benchmark": document["benchmark"],
        "benchmarkVersion": document["benchmarkVersion"],
        "sourceCommit": document["sourceCommit"],
        "sources": document["sources"],
        "matchedN": len(ranked_rows),
        "cohortN": len(rows),
        "coveragePct": round(100.0 * len(ranked_rows) / len(rows), 2),
        "basePrioritySum": base_priority_sum,
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
    if len(deepswe_chart.get("configurations", [])) != 25 or deepswe_chart.get("benchmarkTasks") != 113:
        raise ValueError("AA Coding Agent Index DeepSWE chart must contain the observed 25 configurations and 113 tasks")
    deepswe_by_id = {}
    for config in deepswe_chart["configurations"]:
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

    primary_rows = [
        row for row in rows
        if row["bugHunt"].get("matched") is True and row.get("deepswePassAt1Pct") is not None
    ]
    primary_ids = {row["id"] for row in primary_rows}
    unranked_rows = [row for row in rows if row["id"] not in primary_ids]
    if len(primary_rows) < 2:
        raise ValueError("Primary cohort requires at least two exact AA DeepSWE and Bug Hunt matches")

    aa_cost_rows = [row for row in primary_rows if row["aaEvalCost"] is not None]
    aa_cost_complete = len(aa_cost_rows) == len(primary_rows)
    max_aa_cost = (
        max(require_number(row["aaEvalCost"], f"{row['id']}.aaEvalCost") for row in aa_cost_rows)
        if aa_cost_rows
        else None
    )
    if max_aa_cost is not None and max_aa_cost <= 0:
        raise ValueError("AA evaluation cost normalization requires a positive maximum")
    cost_mode = "aa-only" if aa_cost_complete else "unavailable (AA evaluation cost incomplete)"
    for row in primary_rows:
        row["deepSweCostNorm"] = None
        row["aaCostNorm"] = round((row["aaEvalCost"] / max_aa_cost) * 100, 2) if aa_cost_complete else None
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
            "cohortN": len(primary_rows),
            "sourceMissing": source_missing,
            "sourceCohortN": len(rows),
            "sourceAvailableN": len(rows) - len(source_missing),
            "higherBetter": higher_better,
            "priority": priority,
        }
    retained = [candidate for candidate in CANDIDATES if not coverage[candidate[0]]["missing"]]
    dropped = [
        {
            "key": key,
            "label": label,
            "missing": coverage[key]["missing"],
            "sourceMissing": coverage[key]["sourceMissing"],
            "reason": "incomplete coverage within the exact Bug Hunt matched cohort; values remain null and are not neutral-filled",
        }
        for key, label, _higher_better, _priority in CANDIDATES
        if coverage[key]["missing"]
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
    ]
    primary_total_priority = raw_priority_sum + BUG_HUNT_PRIORITY
    weights = [
        {
            **weight,
            "weightPct": round(100.0 * weight["priority"] / primary_total_priority, 4),
        }
        for weight in base_weights
    ]
    weights.append({
        "key": "bugHuntFixedOf105",
        "label": "Bug Hunt Bench",
        "higherBetter": True,
        "priority": BUG_HUNT_PRIORITY,
        "weightPct": round(100.0 * BUG_HUNT_PRIORITY / primary_total_priority, 4),
    })

    for row in rows:
        row["dims"] = {}
        row["rankingEligible"] = row["id"] in primary_ids
        row["missingFields"] = [key for key, _label, _higher, _priority in CANDIDATES if row.get(key) is None]
        row["rankingExclusionReasons"] = []
        if row["bugHunt"].get("matched") is not True:
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
        if row.get("deepswePassAt1Pct") is None:
            row["rankingExclusionReasons"].append("No exact-variant AA DeepSWE result in the selected source snapshot")
        if not row["rankingEligible"]:
            row["rank"] = None
            row["qualityRank"] = None
            row["overallScore"] = None
            row["qualityScore"] = None
            row["vRanks"] = {}
            row["pareto"] = None
            row["isMissing"] = True
    for weight in weights:
        key = weight["key"]
        values = [
            require_number(
                row["bugHunt"]["fixedOf105"] if key == "bugHuntFixedOf105" else row[key],
                f"{row['id']}.{key}",
            )
            for row in primary_rows
        ]
        normalized = rank_normalize(values, weight["higherBetter"])
        for row, score in zip(primary_rows, normalized):
            row["dims"][key] = score

    for row in primary_rows:
        row["overallScore"] = round(
            sum(row["dims"][weight["key"]] * weight["weightPct"] / 100 for weight in weights),
            1,
        )
        quality_weights = [weight for weight in weights if weight["key"] != "costComposite"]
        quality_weight_sum = sum(weight["weightPct"] for weight in quality_weights)
        row["qualityScore"] = round(
            sum(row["dims"][weight["key"]] * weight["weightPct"] / quality_weight_sum for weight in quality_weights),
            1,
        )
        row["isMissing"] = bool(row["missingFields"])

    by_overall = sorted(primary_rows, key=lambda row: (-row["overallScore"], row["costComposite"], row["name"]))
    for rank, row in enumerate(by_overall, 1):
        row["rank"] = rank
    by_quality = sorted(primary_rows, key=lambda row: (-row["qualityScore"], row["costComposite"], row["name"]))
    quality_ranks = {row["id"]: rank for rank, row in enumerate(by_quality, 1)}
    for row in primary_rows:
        row["qualityRank"] = quality_ranks[row["id"]]
        row["vRanks"] = {weight["key"]: row["dims"][weight["key"]] for weight in weights}

    pareto = []
    for row in primary_rows:
        dominated = any(
            other["id"] != row["id"]
            and other["costComposite"] <= row["costComposite"]
            and other["qualityScore"] >= row["qualityScore"]
            and (
                other["costComposite"] < row["costComposite"]
                or other["qualityScore"] > row["qualityScore"]
            )
            for other in primary_rows
        )
        row["pareto"] = not dominated
        if row["pareto"]:
            pareto.append(row["name"])

    # Retain a stronger Bug Hunt emphasis view as an optional companion to the primary rank.
    bug_hunt_emphasis, bug_hunt_ranked_rows, bug_hunt_weights = build_bug_hunt_emphasis(
        rows, base_weights, raw_priority_sum, bug_hunt_document
    )
    bug_hunt_missing_models = bug_hunt_emphasis["missingModels"]

    # Keep source extraction coverage and add both the score-specific gate and
    # explicitly labelled external benchmark coverage.  Supplemental fields
    # are never rank-normalized unless the zero-gap candidate gate retains them.
    score_coverage = {
        key: {
            "label": item["label"],
            "availableN": item["cohortN"] - item["nMissing"],
            "cohortN": item["cohortN"],
            "missingModels": item["missing"],
            "sourceAvailableN": item["sourceAvailableN"],
            "sourceCohortN": item["sourceCohortN"],
            "sourceMissingModels": item["sourceMissing"],
            "includedInPrimaryScore": key in {weight["key"] for weight in weights},
        }
        for key, item in coverage.items()
    }
    score_coverage["bugHuntFixedOf105"] = {
        "label": "Bug Hunt Bench bugs fixed out of 105",
        "availableN": len(primary_rows),
        "cohortN": len(primary_rows),
        "missingModels": [],
        "sourceAvailableN": len(bug_hunt_owner_matches),
        "sourceCohortN": len(rows),
        "sourceMissingModels": bug_hunt_owner_missing_names,
        "rankableOverlapN": len(primary_rows),
        "includedInPrimaryScore": True,
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
            "group": "primary",
            "label": "Instruction Following (LiveBench)",
            "availableN": sum(row["livebenchInstructionFollowing"] is not None for row in primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": round(100 * sum(row["livebenchInstructionFollowing"] is not None for row in primary_rows) / len(primary_rows), 2),
            "missingModels": [row["name"] for row in primary_rows if row["livebenchInstructionFollowing"] is None],
            "sourceAvailableN": livebench_document["matchedN"],
            "sourceCohortN": len(rows),
            "sourceMissingModels": livebench_document["missingModels"],
            "includedInPrimaryScore": "livebenchInstructionFollowing" in {weight["key"] for weight in weights},
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
            "group": "supplemental",
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
            "includedInPrimaryScore": False,
            "sourceRelease": tb4_document["version"],
        },
        "bugHuntFixedOf105": {
            "group": "primary",
            "label": "Bug Hunt Bench bugs fixed out of 105",
            "availableN": len(primary_rows),
            "cohortN": len(primary_rows),
            "coveragePct": 100.0,
            "sourceAvailableN": len(primary_rows),
            "sourceCohortN": len(rows),
            "sourceCoveragePct": bug_hunt_emphasis["coveragePct"],
            "missingModels": [],
            "sourceMissingModels": bug_hunt_missing_models,
            "includedInPrimaryScore": True,
            "includedInBugHuntEmphasisRanking": True,
            "sourceRelease": bug_hunt_document["benchmarkVersion"],
            "sourceCommit": bug_hunt_document["sourceCommit"],
        },
    }
    coverage_document["cohort"] = f"Artificial Analysis v4.3.2 mapped {len(rows)}-model ValueRank comparison roster"
    coverage_document["cohortN"] = len(rows)
    coverage_document["deepSweSource"] = deepswe_chart["source"]
    coverage_document["deepSweConfigurationsN"] = len(deepswe_chart["configurations"])
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
            "rankableOverlapN": len(primary_rows),
            "sourceCohortN": len(rows),
            "primaryCohortN": len(primary_rows),
            "sourceCoveragePct": round(100 * len(bug_hunt_owner_matches) / len(rows), 2),
            "primaryCoveragePct": round(100 * len(primary_rows) / len(rows), 2),
            "primaryWeightPct": next(weight["weightPct"] for weight in weights if weight["key"] == "bugHuntFixedOf105"),
            "emphasisWeightPct": bug_hunt_emphasis["benchmarkWeightPct"],
        },
    }
    coverage_document["scoring"] = {
        "version": VERSION,
        "cohortN": len(primary_rows),
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
        "zeroGap": not any(item["missingModels"] for item in score_coverage.values() if item["includedInPrimaryScore"]),
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
            "bugHunt": f"{len(bug_hunt_owner_matches)}/{len(rows)} owner matches; {len(primary_rows)} exact AA DeepSWE plus Bug Hunt overlaps rank in the primary composite",
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
                "cohort": {
                    "n": len(primary_rows),
                    "sourceN": len(rows),
                    "source": "Artificial Analysis Coding Agent Index v1.5 DeepSWE v1.1 chart",
                    "sourceUpdatedOn": deepswe_chart["observedAt"],
                },
                "weights": weights,
                "bugHuntEmphasisRanking": bug_hunt_emphasis,
                "costMode": cost_mode,
                "costCoverage": coverage_document["scoring"]["costCoverage"],
                "models": by_overall + sorted(unranked_rows, key=lambda row: row["name"]),
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
                        "rankableOverlapN": len(primary_rows),
                        "cohortN": len(rows),
                        "primaryCohortN": len(primary_rows),
                        "primaryWeightPct": next(weight["weightPct"] for weight in weights if weight["key"] == "bugHuntFixedOf105"),
                        "sourceCommit": bug_hunt_document["sourceCommit"],
                    },
                },
                "appendixNonRanked": [
                    {
                        "id": row["id"],
                        "name": row["name"],
                        "reason": (
                            "No exact AA DeepSWE v1.1 chart variant or eligible Bug Hunt result"
                            if row.get("deepswePassAt1Pct") is None and row["bugHunt"].get("matched") is not True
                            else "No exact AA DeepSWE v1.1 chart variant"
                            if row.get("deepswePassAt1Pct") is None
                            else "No exact eligible Bug Hunt result"
                        ),
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
