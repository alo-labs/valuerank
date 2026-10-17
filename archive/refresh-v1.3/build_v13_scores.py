#!/usr/bin/env python3
"""Build ValueRank v1.3.1 zero-gap matrix, scores, and evidence ledger.

v1.3.1 methodology correction: exclude Kimi K2.7 Code from the ranked cohort
(no published AA Intelligence Index total eval cost) so Cost can restore the
v1.2-style AA+DeepSWE composite. DeepSWE row preserved as non-ranked appendix.
"""
from __future__ import annotations

import json
import math
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path("/Users/shafqat/valuerank")
R = ROOT / ".refresh" / "v1.3"
PUBLISH_DATE = "July 28, 2026"
VERSION = "v1.3.1"

# Ranked-cohort exclusions (still on DeepSWE; preserved in appendix / raw-data)
RANKED_EXCLUSIONS = {
    "kimi-k2.7-code": {
        "reason": (
            "No published AA Intelligence Index total eval cost on "
            "https://artificialanalysis.ai/models/kimi-k2-7-code "
            "(see .refresh/v1.3/aa-kimi-k27-cost-search.md). Excluded from "
            "ranked cohort so Cost can use AA+DeepSWE composite for remaining models."
        ),
        "preserveInAppendix": True,
    },
}

deepswe = json.loads((R / "deepswe.json").read_text())
aa = json.loads((R / "aa_metrics.json").read_text())["models"]
catalog = json.loads((R / "aa" / "aa_catalog.json").read_text())

# Preferred AA slugs (most complete for retained dims)
PREFERRED_SLUG = {
    "claude-opus-5": "claude-opus-5",
    "gpt-5.6-sol": "gpt-5-6-sol",
    "gpt-5.6-terra": "gpt-5-6-terra",
    "claude-fable-5": "claude-fable-5",
    "kimi-k3": "kimi-k3",
    "gpt-5.6-luna": "gpt-5-6-luna",
    "gpt-5.5": "gpt-5-5",  # page redirects to xhigh default
    "claude-opus-4.8": "claude-opus-4-8",
    "grok-4.5": "grok-4-5",
    "claude-sonnet-5": "claude-sonnet-5",
    "muse-spark-1.1": "muse-spark-1-1",  # has evalCost+speed; muse-spark lacks cost
    "gpt-5.4": "gpt-5-4",
    "gemini-3.6-flash": "gemini-3-6-flash",
    "glm-5.2": "glm-5-2",
    "gemini-3.5-flash": "gemini-3-5-flash",  # (high) default on page — fuller than medium
    "kimi-k2.7-code": "kimi-k2-7-code",
    "claude-sonnet-4.6": "claude-sonnet-4-6-adaptive",
    "gemini-3.1-pro": "gemini-3-1-pro-preview",
}

DEVELOPER = {
    "Claude Opus 5": "Anthropic",
    "GPT-5.6 Sol": "OpenAI",
    "GPT-5.6 Terra": "OpenAI",
    "Claude Fable 5": "Anthropic",
    "Kimi K3": "Moonshot AI",
    "GPT-5.6 Luna": "OpenAI",
    "GPT-5.5": "OpenAI",
    "Claude Opus 4.8": "Anthropic",
    "Grok 4.5": "SpaceXAI",
    "Claude Sonnet 5": "Anthropic",
    "Muse Spark 1.1": "Meta",
    "GPT-5.4": "OpenAI",
    "Gemini 3.6 Flash": "Google DeepMind",
    "GLM-5.2": "Z AI",
    "Gemini 3.5 Flash": "Google DeepMind",
    "Kimi K2.7 Code": "Moonshot AI",
    "Claude Sonnet 4.6": "Anthropic",
    "Gemini 3.1 Pro": "Google DeepMind",
}

SHORT = {
    "Claude Opus 5": "Opus 5",
    "GPT-5.6 Sol": "GPT-5.6 Sol",
    "GPT-5.6 Terra": "GPT-5.6 Terra",
    "Claude Fable 5": "Fable 5",
    "Kimi K3": "Kimi K3",
    "GPT-5.6 Luna": "GPT-5.6 Luna",
    "GPT-5.5": "GPT-5.5",
    "Claude Opus 4.8": "Opus 4.8",
    "Grok 4.5": "Grok 4.5",
    "Claude Sonnet 5": "Sonnet 5",
    "Muse Spark 1.1": "Muse Spark",
    "GPT-5.4": "GPT-5.4",
    "Gemini 3.6 Flash": "Gem 3.6 Flash",
    "GLM-5.2": "GLM-5.2",
    "Gemini 3.5 Flash": "Gem 3.5 Flash",
    "Kimi K2.7 Code": "Kimi K2.7",
    "Claude Sonnet 4.6": "Sonnet 4.6",
    "Gemini 3.1 Pro": "Gem 3.1 Pro",
}


def pct(x):
    if x is None:
        return None
    return round(x * 100, 2) if x <= 1.5 else round(float(x), 2)


def from_catalog(slug: str) -> dict:
    o = catalog.get(slug) or {}
    speed = o.get("speed")
    # timescale often only on page text / separate; filled later
    return {
        "slug": slug,
        "name": o.get("name"),
        "intelligenceIndex": o.get("intelligenceIndex"),
        "ifbench": pct(o.get("ifbench")),
        "hle": pct(o.get("hle")),
        "gpqa": pct(o.get("gpqa")),
        "critpt": pct(o.get("critpt")),
        "scicode": pct(o.get("scicode")),
        "lcr": pct(o.get("lcr")),
        "terminalBenchHard": pct(o.get("terminalbenchHard")),
        "gdpvalNormalized": pct(o.get("gdpvalNormalized")),
        "omniAcc": pct(o.get("omniAcc")),
        "omniHalluc": pct(o.get("omniHalluc")),
        "tau2": pct(o.get("tau2")),
        "evalCost": o.get("evalCost"),
        "speed": speed,
    }


rows = []
for m in deepswe["models"]:
    mid = m["slug"]
    display = m["displayName"]
    slug = PREFERRED_SLUG[mid]
    metrics = from_catalog(slug)
    # Merge page extract (speed/evalCost/index often better)
    page = aa.get(mid, {}).get("metrics") or {}
    page_sum = aa.get(mid, {}).get("summary") or {}
    for k in (
        "intelligenceIndex",
        "evalCost",
        "speed",
        "ifbench",
        "hle",
        "gpqa",
        "critpt",
        "scicode",
        "lcr",
        "terminalBenchHard",
        "gdpvalNormalized",
        "omniAcc",
        "omniHalluc",
        "tau2",
    ):
        if metrics.get(k) is None and page.get(k) is not None:
            metrics[k] = page[k]
    for k in ("intelligenceIndex", "evalCost", "speed"):
        if metrics.get(k) is None and page_sum.get(k) is not None:
            metrics[k] = page_sum[k]
    # muse-spark-1-1 specific: page text has speed/cost
    if mid == "muse-spark-1.1":
        m1 = from_catalog("muse-spark-1-1")
        for k, v in m1.items():
            if v is not None:
                metrics[k] = v
        # fill omni etc from muse-spark if missing on 1-1
        ms = from_catalog("muse-spark")
        for k in ("omniAcc", "omniHalluc", "lcr", "hle", "gpqa", "scicode", "critpt"):
            if metrics.get(k) is None:
                metrics[k] = ms.get(k)
        # speed/cost from page summary of muse-spark-1-1
        for e in aa.values():
            if e.get("pageVariant") == "muse-spark-1-1" or (
                e.get("metrics") or {}
            ).get("slug") == "muse-spark-1-1":
                for k in ("speed", "evalCost", "intelligenceIndex"):
                    if e.get("summary", {}).get(k) is not None:
                        metrics[k] = e["summary"][k]
                    if e.get("metrics", {}).get(k) is not None:
                        metrics[k] = e["metrics"][k]
        # hardcode from scraped text if still missing
        if metrics.get("speed") is None:
            metrics["speed"] = 129.0
        if metrics.get("evalCost") is None:
            metrics["evalCost"] = 548.07
        if metrics.get("intelligenceIndex") is None:
            metrics["intelligenceIndex"] = 51.0

    # sonnet 4.6 adaptive
    if mid == "claude-sonnet-4.6":
        metrics = from_catalog("claude-sonnet-4-6-adaptive")
        page = aa.get(mid, {}).get("metrics") or {}
        for k, v in page.items():
            if k in metrics and metrics[k] is None and v is not None:
                metrics[k] = v
        sm = aa.get(mid, {}).get("summary") or {}
        for k in ("speed", "evalCost", "intelligenceIndex"):
            if metrics.get(k) is None and sm.get(k) is not None:
                metrics[k] = sm[k]

    # Fill speed from aa_metrics for all if still missing
    if metrics.get("speed") is None:
        metrics["speed"] = (aa.get(mid, {}).get("summary") or {}).get("speed") or (
            aa.get(mid, {}).get("metrics") or {}
        ).get("speed")

    # Do not let AA payload fields overwrite display identity
    metrics.pop("name", None)
    metrics.pop("shortName", None)
    rows.append(
        {
            **metrics,
            "id": mid,
            "name": display,
            "shortName": SHORT[display],
            "developer": DEVELOPER[display],
            "deepswePassAt1": m["passAt1Pct"],
            "deepsweCost": m["avgCost"],
            "deepsweEffort": m.get("effort"),
            "aaSlug": metrics.get("slug") or slug,
            "aaUrl": f"https://artificialanalysis.ai/models/{slug}",
        }
    )

# Candidate dimensions (raw key, display, higher_better, v12_weight)
CANDIDATES = [
    ("costComposite", "Cost", False, 25),  # built below
    ("ifbench", "IFBench", True, 12),
    ("omniHalluc", "Hallucination", False, 6),
    ("terminalBenchHard", "Terminal-Bench Hard", True, 6),
    ("deepswePassAt1", "DeepSWE", True, 7),
    ("gdpvalNormalized", "GDPval-AA", True, 6),
    ("tau2", "τ²-Bench Telecom", True, 5),
    ("lcr", "AA-LCR", True, 4),
    ("omniAcc", "Omni Acc", True, 4),
    ("hle", "HLE", True, 4),
    ("gpqa", "GPQA", True, 4),
    ("scicode", "SciCode", True, 4),
    ("critpt", "CritPt", True, 3),
    ("intelligenceIndex", "AA Intelligence Index", True, 6),
    ("speed", "Speed", True, 5),
]

# Split ranked cohort vs non-ranked appendix (e.g. Kimi K2.7 Code)
all_rows = rows
appendix = []
ranked = []
for r in all_rows:
    excl = RANKED_EXCLUSIONS.get(r["id"])
    if excl:
        r["ranked"] = False
        r["exclusionReason"] = excl["reason"]
        appendix.append(r)
    else:
        r["ranked"] = True
        ranked.append(r)
rows = ranked  # subsequent scoring uses ranked cohort only

# Build AA+DeepSWE composite cost where possible (ranked cohort)
aa_costs = [r.get("evalCost") for r in rows]
aa_cost_complete = all(c is not None for c in aa_costs)
max_aa = max(c for c in aa_costs if c is not None) if any(aa_costs) else None
max_ds = max(r["deepsweCost"] for r in rows)
for r in rows:
    ds_pen = (r["deepsweCost"] / max_ds) * 100
    if aa_cost_complete:
        aa_pen = (r["evalCost"] / max_aa) * 100
        r["aaCostNorm"] = round(aa_pen, 2)
        r["deepSweCostNorm"] = round(ds_pen, 2)
        r["costComposite"] = round((aa_pen + ds_pen) / 2, 2)
        r["costMode"] = "aa+deepswe"
    else:
        r["aaCostNorm"] = None if r.get("evalCost") is None else round((r["evalCost"] / max_aa) * 100, 2)
        r["deepSweCostNorm"] = round(ds_pen, 2)
        # Zero-gap: AA eval cost incomplete → Cost = DeepSWE-only (documented)
        r["costComposite"] = round(ds_pen, 2)
        r["costMode"] = "deepswe-only"
        r["evalCost"] = r.get("evalCost")

# Appendix: DeepSWE-only cost scale for reference (not ranked)
if appendix and max_ds:
    for r in appendix:
        ds_pen = (r["deepsweCost"] / max_ds) * 100
        r["aaCostNorm"] = None
        r["deepSweCostNorm"] = round(ds_pen, 2)
        r["costComposite"] = round(ds_pen, 2)
        r["costMode"] = "appendix-deepswe-only-not-ranked"

cost_note = (
    "Composite AA+DeepSWE (Kimi K2.7 Code excluded from ranked cohort — no AA Index total eval cost; see aa-kimi-k27-cost-search.md)"
    if aa_cost_complete
    else "DeepSWE-only (AA Intelligence Index total eval cost incomplete for ranked cohort)"
)

# Coverage matrix
coverage = {}
for key, label, higher, w in CANDIDATES:
    missing = [r["name"] for r in rows if r.get(key) is None]
    coverage[key] = {"label": label, "missing": missing, "n_missing": len(missing), "weight": w}

retained = [
    (key, label, higher, w)
    for key, label, higher, w in CANDIDATES
    if coverage[key]["n_missing"] == 0
]
dropped = [
    {
        "key": key,
        "label": label,
        "missing": coverage[key]["missing"],
        "reason": "incomplete cohort coverage",
    }
    for key, label, higher, w in CANDIDATES
    if coverage[key]["n_missing"] > 0
]

# Renormalize weights to sum ~100 preserving relative priorities
raw_sum = sum(w for _, _, _, w in retained)
weights = []
for key, label, higher, w in retained:
    weights.append(
        {
            "key": key,
            "label": label,
            "higherBetter": higher,
            "v12Weight": w,
            "weight": round(100.0 * w / raw_sum, 4),
        }
    )


def rank_normalize(values, higher_better=True):
    n = len(values)
    # ties: average rank
    indexed = list(enumerate(values))
    indexed.sort(key=lambda t: t[1], reverse=higher_better)
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and indexed[j + 1][1] == indexed[i][1]:
            j += 1
        # ranks i..j (1-based)
        avg_rank = sum(range(i + 1, j + 2)) / (j - i + 1)
        for k in range(i, j + 1):
            ranks[indexed[k][0]] = avg_rank
        i = j + 1
    if n == 1:
        return [100.0]
    return [round(((n - r) / (n - 1)) * 100, 1) for r in ranks]


# Normalized matrix
norm = {r["name"]: [] for r in rows}
dim_order = []
for w in weights:
    key = w["key"]
    dim_order.append(w["label"])
    vals = [r[key] for r in rows]
    norms = rank_normalize(vals, higher_better=w["higherBetter"])
    for r, nv in zip(rows, norms):
        norm[r["name"]].append(nv)
        r.setdefault("dims", {})
        r["dims"][key] = nv

# Overall / quality
for r in rows:
    overall = 0.0
    for w, nv in zip(weights, norm[r["name"]]):
        overall += nv * (w["weight"] / 100.0)
    r["overallScore"] = round(overall, 1)
    # Quality: exclude Cost
    q_weights = [w for w in weights if w["key"] != "costComposite"]
    q_sum = sum(w["weight"] for w in q_weights)
    quality = 0.0
    for w in q_weights:
        quality += r["dims"][w["key"]] * (w["weight"] / q_sum)
    r["qualityScore"] = round(quality, 1)

# Ranks
by_overall = sorted(rows, key=lambda r: (-r["overallScore"], r["costComposite"]))
for i, r in enumerate(by_overall, 1):
    r["rank"] = i
by_quality = sorted(rows, key=lambda r: (-r["qualityScore"], r["costComposite"]))
qmap = {r["name"]: i for i, r in enumerate(by_quality, 1)}
for r in rows:
    r["qualityRank"] = qmap[r["name"]]

# Pareto: undominated on costComposite (lower better) vs quality (higher better)
pareto = []
for r in rows:
    dominated = False
    for o in rows:
        if o["name"] == r["name"]:
            continue
        if o["costComposite"] <= r["costComposite"] and o["qualityScore"] >= r["qualityScore"]:
            if o["costComposite"] < r["costComposite"] or o["qualityScore"] > r["qualityScore"]:
                dominated = True
                break
    r["pareto"] = not dominated
    if r["pareto"]:
        pareto.append(r["name"])

# Evidence ledger
sources = []
evidence = []
claims = []
now = datetime.now(timezone.utc).isoformat()
sources.append(
    {
        "id": "deepswe",
        "url": "https://deepswe.datacurve.ai/",
        "asOf": deepswe.get("updatedOnSource"),
        "retrievedAt": deepswe.get("scrapedAt"),
    }
)
for r in rows:
    sources.append({"id": f"aa:{r['aaSlug']}", "url": r["aaUrl"], "retrievedAt": now})
    evidence.append(
        {
            "model": r["name"],
            "deepswePassAt1": r["deepswePassAt1"],
            "deepsweCost": r["deepsweCost"],
            "aaSlug": r["aaSlug"],
            "metrics": {
                k: r.get(k)
                for k in (
                    "intelligenceIndex",
                    "ifbench",
                    "omniHalluc",
                    "omniAcc",
                    "terminalBenchHard",
                    "gdpvalNormalized",
                    "tau2",
                    "lcr",
                    "hle",
                    "gpqa",
                    "scicode",
                    "critpt",
                    "evalCost",
                    "speed",
                )
            },
        }
    )
    claims.append(
        {
            "claim": f"{r['name']} overall={r['overallScore']} rank={r['rank']}",
            "support": ["deepswe", f"aa:{r['aaSlug']}"],
        }
    )

manifest = {
    "version": VERSION,
    "publishDate": PUBLISH_DATE,
    "cohortN": len(rows),
    "deepsweRosterN": len(all_rows),
    "rankedExclusions": [
        {
            "id": r["id"],
            "name": r["name"],
            "reason": r.get("exclusionReason"),
        }
        for r in appendix
    ],
    "retainedDimensions": [w["label"] for w in weights],
    "retainedCount": len(weights),
    "droppedDimensions": dropped,
    "costMode": rows[0]["costMode"],
    "costNote": cost_note,
    "weights": weights,
    "pareto": pareto,
    "changelog": (
        "v1.3.1: Exclude Kimi K2.7 Code from ranked cohort (no AA Index total "
        "eval cost); restore AA+DeepSWE composite Cost for n=17."
    ),
}

(R / "coverage_matrix.json").write_text(
    json.dumps({"coverage": coverage, "retained": [w["key"] for w in weights], "dropped": dropped}, indent=2)
    + "\n"
)
(R / "scores.json").write_text(
    json.dumps(
        {
            "version": VERSION,
            "models": by_overall,
            "weights": weights,
            "pareto": pareto,
            "appendixNonRanked": appendix,
        },
        indent=2,
    )
    + "\n"
)
(R / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

with (R / "sources.jsonl").open("w") as f:
    for s in sources:
        f.write(json.dumps(s) + "\n")
with (R / "evidence.jsonl").open("w") as f:
    for e in evidence:
        f.write(json.dumps(e) + "\n")
with (R / "claims.jsonl").open("w") as f:
    for c in claims:
        f.write(json.dumps(c) + "\n")

# Print summary
print(f"version={VERSION} n={len(rows)} appendix={len(appendix)} retained_dims={len(weights)} costMode={rows[0]['costMode']}")
print("EXCLUDED:", [f"{r['name']}: {r['exclusionReason'][:80]}..." for r in appendix])
print("RETAINED:", [w["label"] + f"({w['weight']}%)" for w in weights])
print("DROPPED:", [d["label"] + f" missing={d['missing']}" for d in dropped])
print("\nRANKING:")
for r in by_overall:
    print(
        f"{r['rank']:2d} {r['name']:22s} overall={r['overallScore']:5.1f} quality={r['qualityScore']:5.1f} qrank={r['qualityRank']:2d} cost={r['costComposite']:6.2f} pareto={r['pareto']}"
    )
print("\nPARETO:", pareto)

