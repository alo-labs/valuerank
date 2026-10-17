#!/usr/bin/env python3
"""Parse DeepSWE models from previously extracted next_f unescaped text."""
import json
import re
import sys

path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Prefer full model objects when present
obj_re = re.compile(
    r'\{\s*"id"\s*:\s*"[^"]+"\s*,\s*"slug"\s*:\s*"([^"]+)"\s*,\s*"name"\s*:\s*"([^"]+)"'
    r'(?:.*?"organization"\s*:\s*"([^"]*)")?'
    r'(?:.*?"version"\s*:\s*"([^"]*)")?'
    r'(?:.*?"rank"\s*:\s*(\d+))?'
    r'(?:.*?"passRate"\s*:\s*([\d.]+))?'
    r'(?:.*?"averageCostPerTask"\s*:\s*([\d.]+))?',
    re.DOTALL,
)

models = []
seen = set()

# Sliding windows around name+org
name_re = re.compile(r'"name"\s*:\s*"([^"]+)"\s*,\s*"organization"\s*:\s*"([^"]+)"')
for m in name_re.finditer(text):
    name, org = m.group(1), m.group(2)
    if org.lower() in ("organization",) or name in seen:
        continue
    window = text[m.start() : m.start() + 8000]
    pass_m = re.search(r'"passRate"\s*:\s*([\d.]+)', window)
    cost_m = re.search(r'"averageCostPerTask"\s*:\s*([\d.]+)', window)
    ver_m = re.search(r'"version"\s*:\s*"([^"]+)"', window)
    rank_m = re.search(r'"rank"\s*:\s*(\d+)', window)
    slug_m = re.search(r'"slug"\s*:\s*"([^"]+)"', window)
    short_m = re.search(r'"shortName"\s*:\s*"([^"]+)"', window)
    if not (pass_m and cost_m):
        continue
    seen.add(name)
    models.append(
        {
            "name": name,
            "shortName": short_m.group(1) if short_m else None,
            "slug": slug_m.group(1) if slug_m else None,
            "organization": org,
            "rank": int(rank_m.group(1)) if rank_m else None,
            "version": ver_m.group(1) if ver_m else None,
            "passRate": float(pass_m.group(1)),
            "avgCost": float(cost_m.group(1)),
        }
    )

# Also try alternate key order: shortName first
if not models:
    alt = re.compile(
        r'"shortName"\s*:\s*"([^"]+)".{0,2000}?"name"\s*:\s*"([^"]+)".{0,2000}?"passRate"\s*:\s*([\d.]+).{0,500}?"averageCostPerTask"\s*:\s*([\d.]+)',
        re.DOTALL,
    )
    for m in alt.finditer(text):
        short, name, pr, cost = m.groups()
        if name in seen:
            continue
        seen.add(name)
        models.append(
            {
                "name": name,
                "shortName": short,
                "passRate": float(pr),
                "avgCost": float(cost),
            }
        )

print(json.dumps(models, indent=2))
print(f"# count={len(models)}", file=sys.stderr)
