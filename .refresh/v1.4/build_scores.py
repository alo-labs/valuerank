#!/usr/bin/env python3
"""Build the reproducible ValueRank v1.4 ranking from current source data.

The ranked cohort is the complete current 21-model DeepSWE Best roster.  A
candidate dimension is retained only when every cohort member has a published
value; missing values are never neutral-filled.  Current AA v4.1.1 component
metrics are kept as fractions, while the score matrix is rank-normalized to a
0--100 scale.
    LiveBench Instruction Following and Terminal-Bench 4.0 are loaded as
    separately sourced coverage fields.  They are candidates for the score,
    but remain coverage-only when the pinned official snapshot does not cover
    every member of the complete cohort.
    """

from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
VERSION = "v1.4.0"
PUBLISH_DATE = "September 5, 2026"

DEVELOPER = {
    "GPT-6 Astra": "OpenAI",
    "Gemini 3.8 Flash": "Google DeepMind",
    "Claude Opus 5": "Anthropic",
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
}

SHORT = {
    "GPT-6 Astra": "GPT-6 Astra",
    "Gemini 3.8 Flash": "Gem 3.8 Flash",
    "Claude Opus 5": "Opus 5",
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
}

# The priority values are ValueRank's combined score priorities, not the
# Artificial Analysis component weights.  AA's official component weights are
# retained in aa_metrics.json and documented separately.
CANDIDATES = [
    ("costComposite", "Cost", False, 25),
    ("omniNonHallucination", "Non-Hallucination", True, 6),
    ("terminalBenchV4", "Terminal-Bench 4.0", True, 6),
    ("livebenchInstructionFollowing", "Instruction Following (LiveBench)", True, 5),
    ("deepswePassAt1", "DeepSWE", True, 7),
    ("gdpvalV2", "GDPval-AA v2", True, 6),
    ("tau3Banking", "τ³-Banking", True, 5),
    ("aaLcr", "AA-LCR", True, 4),
    ("omniAccuracy", "AA-Omniscience Accuracy", True, 4),
    ("hle", "HLE", True, 4),
    ("gpqaDiamond", "GPQA Diamond", True, 4),
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


def main() -> int:
    deepswe = json.loads((REFRESH / "deepswe.json").read_text())
    aa_document = json.loads((REFRESH / "aa_metrics.json").read_text())
    livebench_document = json.loads((REFRESH / "livebench.json").read_text())
    tb4_document = json.loads((REFRESH / "tb4.json").read_text())
    aa_models = aa_document["models"]
    livebench_models = livebench_document["models"]
    tb4_models = tb4_document["cohortRows"]
    coverage_document = json.loads((REFRESH / "coverage_matrix.json").read_text())
    if len(deepswe["models"]) != 21 or deepswe.get("n") != 21:
        raise ValueError("v1.4 requires the complete 21-model DeepSWE roster")
    cohort_ids = {item["slug"] for item in deepswe["models"]}
    if set(livebench_models) != cohort_ids:
        raise ValueError("LiveBench snapshot must contain exactly the current 21-model cohort")
    if livebench_document.get("matchedN") != 20 or tb4_document.get("matchedN") != 11:
        raise ValueError("unexpected external benchmark coverage; refresh snapshots before scoring")

    rows = []
    for deepswe_model in deepswe["models"]:
        model_id = deepswe_model["slug"]
        aa_model = aa_models.get(model_id)
        if not aa_model:
            raise ValueError(f"AA extraction missing DeepSWE model: {model_id}")
        aa_metrics = aa_model["metrics"]
        supplemental = aa_model.get("supplemental", {})
        livebench = livebench_models[model_id]
        tb4 = tb4_models.get(model_id)
        display_name = deepswe_model["displayName"]
        if display_name not in DEVELOPER or display_name not in SHORT:
            raise ValueError(f"identity mapping missing: {display_name}")
        row = {
            "id": model_id,
            "name": display_name,
            "shortName": SHORT[display_name],
            "developer": DEVELOPER[display_name],
            "rankDeepSWE": deepswe_model["rank"],
            "deepsweEffort": deepswe_model["effort"],
            "deepswePassAt1": require_number(deepswe_model["passRate"], f"{model_id}.passRate"),
            "deepswePassAt1Pct": require_number(deepswe_model["passAt1Pct"], f"{model_id}.passAt1Pct"),
            "deepsweUncertaintyPct": require_number(deepswe_model["uncertaintyPct"], f"{model_id}.uncertaintyPct"),
            "deepsweCost": require_number(deepswe_model["avgCost"], f"{model_id}.avgCost"),
            "deepsweOutputTokens": deepswe_model.get("outputTokens"),
            "deepsweOutputTokensLabel": deepswe_model.get("outputTokensLabel"),
            "deepsweAgentSteps": deepswe_model.get("agentSteps"),
            "aaSlug": aa_model["aaSlug"],
            "aaUrl": aa_model["aaUrl"],
            "aaVariant": aa_model.get("aaVariant"),
            "aaEvalCost": require_number(aa_metrics["aaEvalCost"], f"{model_id}.aaEvalCost"),
            "intelligenceIndex": aa_metrics.get("intelligenceIndex"),
            "gdpvalV2": aa_metrics.get("gdpvalV2"),
            "tau3Banking": aa_metrics.get("tau3Banking"),
            # Keep the AA v4.1.1 field under an explicit source namespace: the
            # current standalone Terminal-Bench field below is official TB4.
            "aaTerminalBenchV21": aa_metrics.get("terminalBenchV21"),
            "livebenchModel": livebench.get("livebenchModel"),
            "livebenchOverall": livebench.get("overallScore"),
            "livebenchInstructionFollowing": livebench.get("instructionFollowingScore"),
            "livebenchCostPerSuccessfulTask": livebench.get("costPerSuccessfulTaskUsd"),
            "livebenchCategoryScores": livebench.get("categoryScores", {}),
            "livebenchTaskScores": livebench.get("tasks", {}),
            "terminalBenchV4": tb4.get("resolutionRate") if tb4 else None,
            "terminalBenchV4Pct": tb4.get("resolutionRatePct") if tb4 else None,
            "terminalBenchV4UncertaintyPct": tb4.get("uncertaintyPct") if tb4 else None,
            "terminalBenchV4Cost": tb4.get("costUsd") if tb4 else None,
            "terminalBenchV4Agent": tb4.get("agent") if tb4 else None,
            "terminalBenchV4Effort": tb4.get("model") if tb4 else None,
            "terminalBenchV4ReleaseDate": tb4.get("releaseDate") if tb4 else None,
            "terminalBenchV4Model": tb4.get("baseModel") if tb4 else None,
            "scicode": aa_metrics.get("scicode"),
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

    max_aa_cost = max(require_number(row["aaEvalCost"], f"{row['id']}.aaEvalCost") for row in rows)
    max_deepswe_cost = max(require_number(row["deepsweCost"], f"{row['id']}.deepsweCost") for row in rows)
    if max_aa_cost <= 0 or max_deepswe_cost <= 0:
        raise ValueError("cost normalization requires positive maximum costs")
    for row in rows:
        row["aaCostNorm"] = round((row["aaEvalCost"] / max_aa_cost) * 100, 2)
        row["deepSweCostNorm"] = round((row["deepsweCost"] / max_deepswe_cost) * 100, 2)
        row["costComposite"] = round((row["aaCostNorm"] + row["deepSweCostNorm"]) / 2, 2)
        row["costMode"] = "aa+deepswe"

    coverage = {}
    for key, label, higher_better, priority in CANDIDATES:
        missing = [row["name"] for row in rows if row.get(key) is None]
        coverage[key] = {
            "label": label,
            "missing": missing,
            "nMissing": len(missing),
            "cohortN": len(rows),
            "higherBetter": higher_better,
            "priority": priority,
        }
    retained = [candidate for candidate in CANDIDATES if not coverage[candidate[0]]["missing"]]
    dropped = [
        {
            "key": key,
            "label": label,
            "missing": coverage[key]["missing"],
            "reason": "incomplete cohort coverage; values remain null and are not neutral-filled",
        }
        for key, label, _higher_better, _priority in CANDIDATES
        if coverage[key]["missing"]
    ]
    raw_priority_sum = sum(candidate[3] for candidate in retained)
    weights = [
        {
            "key": key,
            "label": label,
            "higherBetter": higher_better,
            "priority": priority,
            "weightPct": round(100.0 * priority / raw_priority_sum, 4),
        }
        for key, label, higher_better, priority in retained
    ]

    for row in rows:
        row["dims"] = {}
        row["missingFields"] = [key for key, _label, _higher, _priority in CANDIDATES if row.get(key) is None]
    for weight in weights:
        key = weight["key"]
        values = [require_number(row[key], f"{row['id']}.{key}") for row in rows]
        normalized = rank_normalize(values, weight["higherBetter"])
        for row, score in zip(rows, normalized):
            row["dims"][key] = score

    for row in rows:
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

    by_overall = sorted(rows, key=lambda row: (-row["overallScore"], row["costComposite"], row["name"]))
    for rank, row in enumerate(by_overall, 1):
        row["rank"] = rank
    by_quality = sorted(rows, key=lambda row: (-row["qualityScore"], row["costComposite"], row["name"]))
    quality_ranks = {row["id"]: rank for rank, row in enumerate(by_quality, 1)}
    for row in rows:
        row["qualityRank"] = quality_ranks[row["id"]]
        row["vRanks"] = {weight["key"]: row["dims"][weight["key"]] for weight in weights}

    pareto = []
    for row in rows:
        dominated = any(
            other["id"] != row["id"]
            and other["costComposite"] <= row["costComposite"]
            and other["qualityScore"] >= row["qualityScore"]
            and (
                other["costComposite"] < row["costComposite"]
                or other["qualityScore"] > row["qualityScore"]
            )
            for other in rows
        )
        row["pareto"] = not dominated
        if row["pareto"]:
            pareto.append(row["name"])

    # Keep source extraction coverage and add both the score-specific gate and
    # explicitly labelled external benchmark coverage.  Supplemental fields
    # are never rank-normalized unless the zero-gap candidate gate retains them.
    score_coverage = {
        key: {
            "label": item["label"],
            "availableN": item["cohortN"] - item["nMissing"],
            "cohortN": item["cohortN"],
            "missingModels": item["missing"],
            "includedInPrimaryScore": key in {weight["key"] for weight in weights},
        }
        for key, item in coverage.items()
    }
    external_coverage = {
        "livebenchOverall": {
            "group": "supplemental",
            "label": "LiveBench Overall Score",
            "availableN": livebench_document["matchedN"],
            "cohortN": len(rows),
            "coveragePct": round(100 * livebench_document["matchedN"] / len(rows), 2),
            "missingModels": livebench_document["missingModels"],
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
            "group": "supplemental",
            "label": "Instruction Following (LiveBench)",
            "availableN": livebench_document["matchedN"],
            "cohortN": len(rows),
            "coveragePct": round(100 * livebench_document["matchedN"] / len(rows), 2),
            "missingModels": livebench_document["missingModels"],
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
        "livebenchCostPerSuccessfulTask": {
            "group": "supplemental",
            "label": "LiveBench Cost Per Successful Task",
            "availableN": livebench_document["matchedN"],
            "cohortN": len(rows),
            "coveragePct": round(100 * livebench_document["matchedN"] / len(rows), 2),
            "missingModels": livebench_document["missingModels"],
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
            "availableN": tb4_document["matchedN"],
            "cohortN": len(rows),
            "coveragePct": round(100 * tb4_document["matchedN"] / len(rows), 2),
            "missingModels": tb4_document["missingModels"],
            "includedInPrimaryScore": False,
            "sourceRelease": tb4_document["version"],
        },
    }
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
            "cohortN": tb4_document["cohortN"],
        },
    }
    coverage_document["scoring"] = {
        "version": VERSION,
        "cohortN": len(rows),
        "costMode": "aa+deepswe",
        "retainedDimensions": [weight["key"] for weight in weights],
        "droppedDimensions": dropped,
        "zeroGap": not any(item["missingModels"] for item in score_coverage.values() if item["includedInPrimaryScore"]),
        "noNeutralFills": True,
        "fields": score_coverage,
    }

    observed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    ranking_summary = {
        "version": VERSION,
        "publishDate": PUBLISH_DATE,
        "observedAt": observed_at,
        "cohortN": len(rows),
        "deepsweSourceUpdatedOn": deepswe.get("sourceUpdatedOn"),
        "aaBenchmarkVersion": aa_document.get("benchmarkVersion"),
        "retainedDimensionN": len(weights),
        "retainedDimensions": [weight["label"] for weight in weights],
        "droppedDimensions": dropped,
        "zeroGap": coverage_document["scoring"]["zeroGap"],
        "costMode": "aa+deepswe",
        "pareto": pareto,
        "topFive": [
            {"rank": row["rank"], "name": row["name"], "overallScore": row["overallScore"], "qualityScore": row["qualityScore"]}
            for row in by_overall[:5]
        ],
        "externalCoverage": {
            "livebench": f"{livebench_document['matchedN']}/{livebench_document['cohortN']}",
            "livebenchPublishedN": livebench_document.get("publishedN", livebench_document["matchedN"]),
            "livebenchSupplementalModels": list(livebench_document.get("supplementalModels", {})),
            "terminalBenchV4": f"{tb4_document['matchedN']}/{tb4_document['cohortN']}",
        },
    }
    manifest_path = ROOT / "research" / "2026-09-04-valuerank-refresh" / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["scoring"] = ranking_summary
    manifest["scoring"]["weights"] = weights
    manifest["scoring"]["primaryMissingFields"] = {
        key: data["missing"] for key, data in coverage.items() if data["missing"]
    }

    (REFRESH / "scores.json").write_text(
        json.dumps(
            {
                "version": VERSION,
                "publishDate": PUBLISH_DATE,
                "observedAt": observed_at,
                "benchmarkVersion": aa_document.get("benchmarkVersion"),
                "cohort": {"n": len(rows), "source": deepswe["source"], "sourceUpdatedOn": deepswe.get("sourceUpdatedOn")},
                "weights": weights,
                "models": by_overall,
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
                        "cohortN": tb4_document["cohortN"],
                    },
                },
                "appendixNonRanked": [],
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
        "n": len(rows),
        "retainedDimensions": len(weights),
        "dropped": dropped,
        "zeroGap": ranking_summary["zeroGap"],
        "topFive": ranking_summary["topFive"],
        "outputs": [
            ".refresh/v1.4/scores.json",
            ".refresh/v1.4/coverage_matrix.json",
            ".refresh/v1.4/ranking_summary.json",
        ],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
