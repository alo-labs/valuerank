#!/usr/bin/env python3
"""Normalize the rendered official Terminal-Bench 4.0 leaderboard capture."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
TARGET_URL = "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
HOMEPAGE_URL = "https://www.tbench.ai/"

COHORT_ALIAS = {
    "GPT-6 Astra": "gpt-6-astra",
    "Opus 5": "claude-opus-5",
    "Fable 5": "claude-fable-5",
    "GLM-5.3": "glm-5.3",
    "GPT-5.6 Sol": "gpt-5.6-sol",
    "Opus 4.8": "claude-opus-4.8",
    "Grok 4.6": "grok-4.6",
    "Gemini 3.8 Flash": "gemini-3.8-flash",
    "GPT-5.6 Luna": "gpt-5.6-luna",
    "Sonnet 5": "claude-sonnet-5",
    "Gemini 3.7 Flash": "gemini-3.7-flash",
}


def parse_rate(value: str) -> tuple[float, float]:
    match = re.fullmatch(r"\s*([0-9.]+)%\s*±\s*([0-9.]+)%\s*", value)
    if not match:
        raise ValueError(f"unexpected Terminal-Bench resolution rate: {value!r}")
    return float(match.group(1)) / 100, float(match.group(2))


def parse_cost(value: str) -> float:
    match = re.fullmatch(r"\s*\$([0-9.]+)([kKmM]?)\s*", value)
    if not match:
        raise ValueError(f"unexpected Terminal-Bench cost: {value!r}")
    multiplier = {"": 1, "k": 1_000, "K": 1_000, "m": 1_000_000, "M": 1_000_000}[match.group(2)]
    return round(float(match.group(1)) * multiplier, 2)


def main() -> int:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else REFRESH / "tb4-scrape.json"
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else REFRESH / "tb4.json"
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
            "cohortModelId": COHORT_ALIAS.get(base_model),
        })
    if len(entries) != 14:
        raise ValueError(f"expected 14 current Terminal-Bench 4.0 rows, found {len(entries)}")
    cohort = json.loads((REFRESH / "deepswe.json").read_text())["models"]
    cohort_ids = [item["slug"] for item in cohort]
    matches = {entry["cohortModelId"]: entry for entry in entries if entry["cohortModelId"]}
    if len(matches) != 11:
        raise ValueError(f"expected 11 Terminal-Bench cohort matches, found {len(matches)}")
    missing = [item["displayName"] for item in cohort if item["slug"] not in matches]
    document = {
        "schemaVersion": "valuerank-terminal-bench-v1",
        "version": "4.0",
        "observedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": {
            "publisher": "Terminal-Bench / Harbor",
            "targetUrl": TARGET_URL,
            "renderedUrl": raw.get("finalUrl"),
            "homepage": HOMEPAGE_URL,
            "tasksUrl": "https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4?tab=tasks",
            "captureSha256": hashlib.sha256(raw_bytes).hexdigest(),
            "capturePath": ".refresh/v1.4/tb4-scrape.json",
            "capturedAt": raw.get("scrapedAt"),
        },
        "rowN": len(entries),
        "cohortN": len(cohort_ids),
        "matchedN": len(matches),
        "missingModels": missing,
        "rows": entries,
        "cohortRows": {model_id: matches[model_id] for model_id in cohort_ids if model_id in matches},
    }
    output_path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "version": document["version"],
        "rows": document["rowN"],
        "cohortN": document["cohortN"],
        "matchedN": document["matchedN"],
        "missingModels": document["missingModels"],
        "output": str(output_path if output_path.is_absolute() else output_path),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
