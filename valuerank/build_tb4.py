#!/usr/bin/env python3
"""Normalize the rendered official Terminal-Bench 4.0 leaderboard capture."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from valuerank.clock import iso_z


from valuerank.paths import DATA, ROOT
TARGET_URL = "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
HOMEPAGE_URL = "https://www.tbench.ai/"

# O132 (2026-10-30): the AA Intelligence Index v5 cohort. tbench.ai shows one row per model (its best effort), so every
# cohort configuration is aliased by the exact displayed model and effort (O33), never by base name.
COHORT_ALIAS: dict[str, str] = {}

EXACT_ALIAS = {
    "Opus 5.5 (max)": "claude-opus-5-5",
    "Sonnet 5.5 (max)": "claude-sonnet-5-5",
    "GPT-6 Astra (max)": "gpt-6-astra",
    "GPT-6.1 Sol (max)": "gpt-6.1-sol",
    "GPT-6 Luna (max)": "gpt-6-luna",
}


def parse_rate(value: str) -> tuple[float, float]:
    match = re.fullmatch(r"\s*([0-9.]+)%\s*±\s*([0-9.]+)%\s*", value)
    if not match:
        raise ValueError(f"unexpected Terminal-Bench resolution rate: {value!r}")
    return float(match.group(1)) / 100, float(match.group(2))


NO_COST = {"", "—", "–", "-", "n/a"}


def parse_cost(value: str) -> float | None:
    if value.strip().lower() in NO_COST:
        return None
    match = re.fullmatch(r"\s*\$([0-9.]+)([kKmM]?)\s*", value)
    if not match:
        raise ValueError(f"unexpected Terminal-Bench cost: {value!r}")
    multiplier = {"": 1, "k": 1_000, "K": 1_000, "m": 1_000_000, "M": 1_000_000}[match.group(2)]
    return round(float(match.group(1)) * multiplier, 2)


def main(argv: list[str] | None = None, *, data: Path = DATA) -> int:
    args = sys.argv[1:] if argv is None else argv
    input_path = Path(args[0]) if len(args) >= 1 else data / "tb4-scrape.json"
    output_path = Path(args[1]) if len(args) >= 2 else data / "tb4.json"
    raw_bytes = input_path.read_bytes()
    raw = json.loads(raw_bytes)
    rows = raw.get("rows", [])
    if not rows or rows[0] != ["RANK", "MODEL", "AGENT", "RESOLUTION RATE", "RELEASE DATE", "TOKENS", "COST"]:
        raise ValueError("Terminal-Bench capture does not contain the expected 4.0 table header")
    entries = []
    for index, values in enumerate(rows[1:], 1):
        if len(values) != 7:
            raise ValueError(f"Terminal-Bench row {index} has {len(values)} cells, expected 7")
        rank, model, agent, rate, release_date, tokens, cost = values
        resolution_rate, uncertainty_pct = parse_rate(rate)
        base_model = re.sub(r"\s+\([^)]*\)$", "", model)
        entries.append({
            "rank": int(rank),
            "rankLabel": rank,
            "model": model,
            "baseModel": base_model,
            "agent": agent,
            "resolutionRate": round(resolution_rate, 4),
            "resolutionRatePct": round(resolution_rate * 100, 1),
            "uncertaintyPct": uncertainty_pct,
            "releaseDate": release_date,
            "tokens": tokens,
            "costUsd": parse_cost(cost),
            "cohortModelId": EXACT_ALIAS.get(model) or COHORT_ALIAS.get(base_model),
        })
    aa_models = json.loads((data / "aa_metrics.json").read_text())["models"]
    cohort = [{"slug": model_id, "displayName": item["displayName"]} for model_id, item in aa_models.items()]
    cohort_ids = [item["slug"] for item in cohort]
    aliased = [entry["cohortModelId"] for entry in entries if entry["cohortModelId"]]
    duplicates = sorted({model_id for model_id in aliased if aliased.count(model_id) > 1})
    if duplicates:
        raise ValueError(f"Terminal-Bench cohort aliases are not unique: {', '.join(duplicates)}")
    matches = {entry["cohortModelId"]: entry for entry in entries if entry["cohortModelId"]}
    missing = [item["displayName"] for item in cohort if item["slug"] not in matches]
    claim_document = json.loads((data / "provider_claims.json").read_text())
    provider_claims = [
        claim for claim in claim_document.get("claims", [])
        if claim.get("benchmark") == "Terminal-Bench"
        and claim.get("benchmarkVersion") == "4.0"
        and claim.get("eligibleForRanking") is True
        and claim.get("cohortModelId") not in matches
    ]
    claim_model_ids = {claim["cohortModelId"] for claim in provider_claims}
    ranking_missing = [
        item["displayName"] for item in cohort
        if item["slug"] not in matches and item["slug"] not in claim_model_ids
    ]
    document = {
        "schemaVersion": "valuerank-terminal-bench-v1",
        "version": "4.0",
        "observedAt": iso_z(),
        "source": {
            "publisher": "Terminal-Bench / Harbor",
            "targetUrl": TARGET_URL,
            "renderedUrl": raw.get("finalUrl"),
            "homepage": HOMEPAGE_URL,
            "tasksUrl": "https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4?tab=tasks",
            "captureSha256": hashlib.sha256(raw_bytes).hexdigest(),
            "capturePath": str(input_path),
            "captureMethod": raw.get("captureMethod", "rendered leaderboard snapshot"),
            "capturedAt": raw.get("scrapedAt"),
        },
        "rowN": len(entries),
        "rowsWithoutCostN": sum(entry["costUsd"] is None for entry in entries),
        "cohortN": len(cohort_ids),
        "matchedN": len(matches),
        "missingModels": missing,
        "rankingAvailableN": len(matches) + len(claim_model_ids),
        "rankingMissingModels": ranking_missing,
        "providerClaimN": len(provider_claims),
        "providerClaims": provider_claims,
        "providerClaimPolicy": "Use exact-version provider claims only while the benchmark owner has no result; preserve claim type and evaluated model/alias details.",
        "rows": entries,
        "cohortRows": {model_id: matches[model_id] for model_id in cohort_ids if model_id in matches},
    }
    output_path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "version": document["version"],
        "rows": document["rowN"],
        "rowsWithoutCostN": document["rowsWithoutCostN"],
        "cohortN": document["cohortN"],
        "matchedN": document["matchedN"],
        "rankingAvailableN": document["rankingAvailableN"],
        "providerClaimN": document["providerClaimN"],
        "missingModels": document["missingModels"],
        "rankingMissingModels": document["rankingMissingModels"],
        "output": str(output_path if output_path.is_absolute() else output_path),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
