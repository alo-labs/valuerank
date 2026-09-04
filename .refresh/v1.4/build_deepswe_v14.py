#!/usr/bin/env python3
"""Build a source-backed DeepSWE v1.1 Best-roster snapshot from Playwright output."""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


source_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
payload = json.loads(source_path.read_text(encoding="utf-8"))

DISPLAY = {
    "gpt-6-astra": "GPT-6 Astra",
    "gemini-3.8-flash": "Gemini 3.8 Flash",
    "claude-opus-5": "Claude Opus 5",
    "gpt-5.6-sol": "GPT-5.6 Sol",
    "claude-fable-5": "Claude Fable 5",
    "glm-5.3": "GLM-5.3",
    "kimi-k3": "Kimi K3",
    "grok-4.6": "Grok 4.6",
    "gpt-5.6-luna": "GPT-5.6 Luna",
    "gpt-5.5": "GPT-5.5",
    "gemini-3.7-flash": "Gemini 3.7 Flash",
    "glm-5.3-flash": "GLM-5.3 Flash",
    "deepseek-v4-pro": "DeepSeek V4 Pro",
    "claude-opus-4.8": "Claude Opus 4.8",
    "qwen3.8-max": "Qwen3.8 Max",
    "muse-spark-1.2": "Muse Spark 1.2",
    "claude-sonnet-5": "Claude Sonnet 5",
    "deepseek-v4-flash": "DeepSeek V4 Flash",
    "gemini-3.6-flash": "Gemini 3.6 Flash",
    "glm-5.2": "GLM-5.2",
    "gemini-3.5-flash": "Gemini 3.5 Flash",
}


def parse_percent(value: str) -> tuple[float, str | None]:
    match = re.match(r"([\d.]+)%", value)
    if not match:
        raise ValueError(f"invalid DeepSWE percentage: {value!r}")
    uncertainty = re.search(r"±([\d.]+)%", value)
    return float(match.group(1)), uncertainty.group(1) if uncertainty else None


def parse_tokens(value: str) -> int | None:
    match = re.fullmatch(r"([\d.]+)([kKmM]?)", value.strip())
    if not match:
        return None
    number = float(match.group(1))
    multiplier = {"": 1, "k": 1_000, "K": 1_000, "m": 1_000_000, "M": 1_000_000}[match.group(2)]
    return int(number * multiplier)


def parse_card(card: str) -> dict | None:
    lines = [line.strip() for line in card.splitlines() if line.strip()]
    if len(lines) < 6 or lines[0] not in DISPLAY:
        return None
    if not (lines[1].startswith("[") and lines[1].endswith("]")):
        return None
    pass_at_1, uncertainty = parse_percent(lines[2])
    cost = re.fullmatch(r"\$([\d.]+)", lines[3])
    steps = re.fullmatch(r"\d+", lines[5])
    if not cost or not steps:
        return None
    return {
        "slug": lines[0],
        "name": lines[0],
        "displayName": DISPLAY[lines[0]],
        "effort": lines[1].strip("[]").lower(),
        "passRate": pass_at_1 / 100,
        "passAt1Pct": pass_at_1,
        "uncertaintyPct": float(uncertainty) if uncertainty else None,
        "avgCost": float(cost.group(1)),
        "outputTokens": parse_tokens(lines[4]),
        "outputTokensLabel": lines[4],
        "agentSteps": int(steps.group(0)),
        "source": "DeepSWE Best page card",
    }


models = []
for card in payload.get("cards") or []:
    model = parse_card(card)
    if model:
        models.append(model)

if len(models) != 21:
    raise SystemExit(f"expected 21 current Best cards, parsed {len(models)}")

seen: set[str] = set()
unique = []
for model in models:
    if model["slug"] not in seen:
        seen.add(model["slug"])
        unique.append(model)
for rank, model in enumerate(unique, start=1):
    model["rank"] = rank

text = payload.get("textSample") or ""
source_update = re.search(r"updated\s+([A-Z][a-z]+\s+\d{1,2},\s+\d{4})", text)
tasks = re.search(r"(\d+)\s+tasks", text)
repositories = re.search(r"(\d+)\s+repos", text)
languages = re.search(r"(\d+)\s+languages", text)
models_total = re.search(r"models\s+(\d+)", text)
configs = re.search(r"Configs\s*\(([^)]+)\)", text)

output = {
    "version": "v1.1",
    "observedAt": payload.get("scrapedAt") or datetime.now(timezone.utc).isoformat(),
    "source": "https://deepswe.datacurve.ai/",
    "sourceSnapshot": str(source_path),
    "leaderboard": "Best",
    "sourceUpdatedOn": source_update.group(1) if source_update else None,
    "tasks": int(tasks.group(1)) if tasks else None,
    "repositories": int(repositories.group(1)) if repositories else None,
    "languages": int(languages.group(1)) if languages else None,
    "modelCatalog": int(models_total.group(1)) if models_total else None,
    "configsShown": configs.group(1) if configs else None,
    "selectionRule": "Current rows in the DeepSWE Best tab, preserving the source table order and effort level; no family collapse or score imputation.",
    "methodology": {
        "harness": "mini-swe-agent",
        "taskDesign": "Original contamination-free engineering tasks",
        "verification": "Hand-written behavioral verifiers",
    },
    "historicalExclusionsNotOnRoster": [
        "Grok-Build-0.1",
        "Gemini 3 Flash",
        "Claude Opus 4.6",
    ],
    "n": len(unique),
    "models": unique,
}

output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"n": len(unique), "sourceUpdatedOn": output["sourceUpdatedOn"], "models": [(m["rank"], m["displayName"], m["passAt1Pct"], m["avgCost"], m["effort"]) for m in unique]}, indent=2))
