#!/usr/bin/env python3
"""Parse DeepSWE Best roster from Playwright body text or cards."""
import json
import re
import sys
from datetime import datetime, timezone

src = sys.argv[1]
out = sys.argv[2]

with open(src, "r", encoding="utf-8") as f:
    raw = f.read()

# If JSON with textSample/cards, prefer that
models = []
try:
    data = json.loads(raw)
    text = data.get("textSample") or ""
    cards = data.get("cards") or []
    # Prefer cards that look like leaderboard rows
    for c in cards:
        lines = [ln.strip() for ln in c.splitlines() if ln.strip()]
        if len(lines) >= 3 and re.match(r"^[\w.+\-]+$", lines[0].replace("[", "").split()[0] if False else lines[0].split("\n")[0]):
            # format: name\n[effort]\npass%\n$cost\n...
            name = lines[0]
            effort = None
            idx = 1
            if lines[1].startswith("[") and lines[1].endswith("]"):
                effort = lines[1].strip("[]")
                idx = 2
            if idx >= len(lines):
                continue
            pass_m = re.match(r"([\d.]+)%", lines[idx])
            cost_m = re.match(r"\$([\d.]+)", lines[idx + 1]) if idx + 1 < len(lines) else None
            if pass_m and cost_m:
                models.append(
                    {
                        "slug": name,
                        "name": name,
                        "effort": effort,
                        "passRate": float(pass_m.group(1)) / 100.0,
                        "passAt1Pct": float(pass_m.group(1)),
                        "avgCost": float(cost_m.group(1)),
                        "source": "card",
                    }
                )
    if not models:
        text = data.get("textSample") or json.dumps(data)
except json.JSONDecodeError:
    text = raw

if not models:
    # Parse block after "Best" / MODEL PASS@1
    # Patterns like:
    # claude-opus-5
    # [max]
    # 74%±4%
    # $11.84
    pattern = re.compile(
        r"(?m)^([a-z0-9][a-z0-9.\-]*)\n(?:\[([^\]]+)\]\n)?([\d.]+)%[^\n]*\n\$([\d.]+)",
        re.IGNORECASE,
    )
    for m in pattern.finditer(text):
        slug, effort, pct, cost = m.groups()
        # skip UI chrome
        if slug.lower() in {"models", "best", "cost", "data", "blog", "run", "github", "leaderboard"}:
            continue
        models.append(
            {
                "slug": slug,
                "name": slug,
                "effort": effort,
                "passRate": float(pct) / 100.0,
                "passAt1Pct": float(pct),
                "avgCost": float(cost),
                "source": "body",
            }
        )

# Dedupe by slug keeping first (Best table order)
seen = set()
unique = []
for m in models:
    if m["slug"] in seen:
        continue
    seen.add(m["slug"])
    unique.append(m)

# Assign ranks
for i, m in enumerate(unique, 1):
    m["rank"] = i

# Human-friendly display names
DISPLAY = {
    "claude-opus-5": "Claude Opus 5",
    "gpt-5.6-sol": "GPT-5.6 Sol",
    "claude-fable-5": "Claude Fable 5",
    "gpt-5.6-terra": "GPT-5.6 Terra",
    "kimi-k3": "Kimi K3",
    "gpt-5.6-luna": "GPT-5.6 Luna",
    "gpt-5.5": "GPT-5.5",
    "claude-opus-4.8": "Claude Opus 4.8",
    "claude-sonnet-5": "Claude Sonnet 5",
    "grok-4.5": "Grok 4.5",
    "muse-spark-1.1": "Muse Spark 1.1",
    "gpt-5.4": "GPT-5.4",
    "gemini-3.6-flash": "Gemini 3.6 Flash",
    "glm-5.2": "GLM-5.2",
    "gemini-3.5-flash": "Gemini 3.5 Flash",
    "kimi-k2.7-code": "Kimi K2.7 Code",
    "claude-sonnet-4.6": "Claude Sonnet 4.6",
    "gemini-3.1-pro": "Gemini 3.1 Pro",
}
for m in unique:
    m["displayName"] = DISPLAY.get(m["slug"], m["slug"])

# Methodology exclusions that still apply (not on DeepSWE Best)
EXCLUSIONS = ["Grok-Build-0.1", "Gemini 3 Flash", "Claude Opus 4.6"]

payload = {
    "version": "v1.3",
    "scrapedAt": datetime.now(timezone.utc).isoformat(),
    "source": "https://deepswe.datacurve.ai/",
    "leaderboard": "Best",
    "updatedOnSource": "July 25, 2026",
    "cohortRule": "Full current DeepSWE Best roster; no invented scores",
    "historicalExclusionsNotOnRoster": EXCLUSIONS,
    "n": len(unique),
    "models": unique,
}

with open(out, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)
    f.write("\n")

print(json.dumps({"n": len(unique), "models": [(m["rank"], m["displayName"], m["passAt1Pct"], m["avgCost"], m.get("effort")) for m in unique]}, indent=2))
