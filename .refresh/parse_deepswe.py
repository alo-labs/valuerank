#!/usr/bin/env python3
"""Parse DeepSWE leaderboard from HTML, hydrated body text, or live JSON API dump.

Static Next.js HTML often has zero __next_f chunks — prefer Playwright-hydrated
body text or artifacts/v1/leaderboard-live.json.
"""
import sys
import re
import json
from collections import defaultdict

path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    raw = f.read()

models = []
seen = set()


def add(name, org=None, rank=None, version=None, pass_rate=None, avg_cost=None, **extra):
    key = name
    if key in seen or pass_rate is None or avg_cost is None:
        return
    seen.add(key)
    row = {
        "name": name,
        "organization": org,
        "rank": rank,
        "version": version,
        "passRate": float(pass_rate),
        "avgCost": float(avg_cost),
    }
    row.update({k: v for k, v in extra.items() if v is not None})
    models.append(row)


# 1) Live JSON API
try:
    data = json.loads(raw)
except json.JSONDecodeError:
    data = None

if isinstance(data, dict) and any(
    k in data for k in ("configurations", "results", "leaderboard", "models", "rows")
):
    rows = (
        data.get("configurations")
        or data.get("results")
        or data.get("leaderboard")
        or data.get("models")
        or data.get("rows")
        or []
    )
    if isinstance(rows, dict):
        rows = list(rows.values())
    # Group by model family; pick Best = highest pass@1, tie → lower cost
    by_family = defaultdict(list)
    for row in rows:
        if not isinstance(row, dict):
            continue
        name = row.get("model") or row.get("name") or row.get("slug") or row.get("shortName")
        pr = row.get("passRate") or row.get("pass_rate") or row.get("pass_at_1")
        cost = (
            row.get("averageCostPerTask")
            or row.get("avgCost")
            or row.get("average_cost_per_task")
            or row.get("avg_cost")
        )
        if name is None or pr is None or cost is None:
            continue
        by_family[str(name)].append((float(pr), float(cost), row))
    for name, opts in by_family.items():
        opts.sort(key=lambda t: (-t[0], t[1]))
        pr, cost, row = opts[0]
        add(
            name,
            org=row.get("organization") or row.get("org"),
            version=row.get("version") or row.get("effort") or row.get("reasoning_effort"),
            pass_rate=pr if pr <= 1.0 else pr / 100.0,
            avg_cost=cost,
            effort=row.get("effort") or row.get("reasoning_effort"),
        )

# 2) Next.js flight chunks (legacy)
if not models:
    chunk_re = re.compile(
        r'self\.__next_f\.push\(\[\s*1\s*,\s*"((?:[^"\\]|\\.)*)"\s*\]\)', re.DOTALL
    )
    chunks = chunk_re.findall(raw)

    def unescape(s):
        out = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == "\\" and i + 1 < len(s):
                nxt = s[i + 1]
                mapping = {'"': '"', "\\": "\\", "n": "\n", "t": "\t", "r": "\r", "/": "/"}
                out.append(mapping.get(nxt, nxt))
                i += 2
            else:
                out.append(c)
                i += 1
        return "".join(out)

    unescaped = [unescape(c) for c in chunks]
    print(f"Total chunks: {len(chunks)}", file=sys.stderr)
    name_re = re.compile(r'"name"\s*:\s*"([^"]+)"\s*,\s*"organization"\s*:\s*"([^"]+)"')
    for chunk in unescaped:
        for m in name_re.finditer(chunk):
            name, org = m.group(1), m.group(2)
            if org.lower() == "organization":
                continue
            window = chunk[m.start() : m.start() + 5000]
            pass_m = re.search(r'"passRate"\s*:\s*([\d.]+)', window)
            cost_m = re.search(r'"averageCostPerTask"\s*:\s*([\d.]+)', window)
            ver_m = re.search(r'"version"\s*:\s*"([^"]+)"', window)
            rank_m = re.search(r'"rank"\s*:\s*(\d+)', window)
            if pass_m and cost_m:
                add(
                    name,
                    org=org,
                    rank=int(rank_m.group(1)) if rank_m else None,
                    version=ver_m.group(1) if ver_m else None,
                    pass_rate=float(pass_m.group(1)),
                    avg_cost=float(cost_m.group(1)),
                )

# 3) Hydrated Best table body text / cards
if not models:
    pattern = re.compile(
        r"(?m)^([a-z0-9][a-z0-9.\-]*)\n(?:\[([^\]]+)\]\n)?([\d.]+)%[^\n]*\n\$([\d.]+)",
        re.IGNORECASE,
    )
    skip = {
        "models",
        "best",
        "cost",
        "data",
        "blog",
        "run",
        "github",
        "leaderboard",
        "deepswe",
    }
    for m in pattern.finditer(raw):
        slug, effort, pct, cost = m.groups()
        if slug.lower() in skip:
            continue
        if slug in seen:
            continue  # first occurrence = Best table order
        add(
            slug,
            version=effort,
            pass_rate=float(pct) / 100.0,
            avg_cost=float(cost),
            effort=effort,
        )

print(json.dumps(models, indent=2))
print(f"# count={len(models)}", file=sys.stderr)
