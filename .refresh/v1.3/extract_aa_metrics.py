#!/usr/bin/env python3
"""Extract AA model metric objects from scraped HTML (escaped JSON in RSC payloads)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

aa_dir = Path(sys.argv[1] if len(sys.argv) > 1 else ".refresh/v1.3/aa")
out_path = Path(sys.argv[2] if len(sys.argv) > 2 else ".refresh/v1.3/aa_metrics.json")

# Match escaped or raw model objects keyed by slug + intelligenceIndex + ifbench
OBJ_RE = re.compile(
    r'\\?"slug\\?"\s*:\s*\\?"([^"\\]+)\\?"\s*,\s*'
    r'\\?"name\\?"\s*:\s*\\?"((?:[^"\\]|\\.)*)\\?"'
    r'[\s\S]{0,2500}?'
    r'\\?"intelligenceIndex\\?"\s*:\s*(null|[\d.]+)'
    r'[\s\S]{0,4000}?'
    r'\\?"ifbench\\?"\s*:\s*(null|[\d.]+)',
    re.I,
)


def unescape(s: str) -> str:
    return (
        s.replace(r"\"", '"')
        .replace(r"\\", "\\")
        .replace(r"\/", "/")
        .replace(r"\n", "\n")
    )


def parse_float(v):
    if v is None or v == "null":
        return None
    try:
        return float(v)
    except Exception:
        return None


def extract_field(window: str, *keys):
    for key in keys:
        m = re.search(rf'\\?"{key}\\?"\s*:\s*(null|-?[\d.]+|true|false)', window, re.I)
        if m:
            raw = m.group(1)
            if raw in ("true", "false"):
                return raw == "true"
            return parse_float(raw)
    return None


def extract_nested(window: str, parent: str, child: str):
    m = re.search(
        rf'\\?"{parent}\\?"\s*:\s*\{{[\s\S]{{0,400}}?\\?"{child}\\?"\s*:\s*(null|-?[\d.]+)',
        window,
        re.I,
    )
    if m:
        return parse_float(m.group(1))
    return None


def extract_objects(html: str):
    objs = []
    for m in re.finditer(r'\\?"slug\\?"\s*:\s*\\?"([^"\\]+)\\?"', html):
        slug = m.group(1)
        start = m.start()
        # Expand window backward a bit for id, forward for metrics
        window = html[max(0, start - 200) : start + 7000]
        if "ifbench" not in window and "intelligenceIndex" not in window:
            continue
        name_m = re.search(r'\\?"name\\?"\s*:\s*\\?"((?:[^"\\]|\\.)*)\\?"', window)
        short_m = re.search(r'\\?"shortName\\?"\s*:\s*\\?"((?:[^"\\]|\\.)*)\\?"', window)
        name = unescape(name_m.group(1)) if name_m else None
        short = unescape(short_m.group(1)) if short_m else None
        omni_acc = extract_nested(window, "omniscienceBreakdown", "accuracy")
        omni_hall = extract_nested(window, "omniscienceBreakdown", "hallucinationRate")
        eval_cost = extract_nested(window, "intelligenceIndexCost", "total")
        obj = {
            "slug": slug,
            "name": name,
            "shortName": short,
            "intelligenceIndex": extract_field(window, "intelligenceIndex"),
            "codingIndex": extract_field(window, "codingIndex"),
            "agenticIndex": extract_field(window, "agenticIndex"),
            "omniscience": extract_field(window, "omniscience"),
            "omniAcc": omni_acc,
            "omniHalluc": omni_hall,
            "gdpval": extract_field(window, "gdpval"),
            "gdpvalNormalized": extract_field(window, "gdpvalNormalized"),
            "tau2": extract_field(window, "tau2"),
            "tauBanking": extract_field(window, "tauBanking"),
            "terminalbenchHard": extract_field(window, "terminalbenchHard"),
            "terminalbenchV21": extract_field(window, "terminalbenchV21"),
            "scicode": extract_field(window, "scicode"),
            "lcr": extract_field(window, "lcr"),
            "ifbench": extract_field(window, "ifbench"),
            "hle": extract_field(window, "hle"),
            "gpqa": extract_field(window, "gpqa"),
            "critpt": extract_field(window, "critpt"),
            "evalCost": eval_cost,
            "price1mInputTokens": extract_field(window, "price1mInputTokens"),
            "price1mOutputTokens": extract_field(window, "price1mOutputTokens"),
            "deprecated": extract_field(window, "deprecated"),
        }
        # speed often separate; try common keys
        obj["speed"] = extract_field(
            window, "outputSpeed", "outputTokensPerSecond", "medianOutputTokensPerSecond"
        )
        covered = sum(
            1
            for k in (
                "ifbench",
                "hle",
                "gpqa",
                "critpt",
                "scicode",
                "lcr",
                "terminalbenchHard",
                "gdpvalNormalized",
                "omniAcc",
                "omniHalluc",
                "tau2",
                "intelligenceIndex",
                "evalCost",
            )
            if obj.get(k) is not None
        )
        obj["_coverage"] = covered
        if covered >= 3:
            objs.append(obj)
    # Dedupe by slug keeping highest coverage
    best = {}
    for o in objs:
        prev = best.get(o["slug"])
        if not prev or o["_coverage"] > prev["_coverage"]:
            best[o["slug"]] = o
    return list(best.values())


def parse_summary_speed_cost(text: str):
    out = {}
    m = re.search(
        r"scores ([\d.]+) on the Artificial Analysis Intelligence Index", text
    )
    if m:
        out["intelligenceIndex"] = float(m.group(1))
    m = re.search(r"it cost \$([\d,]+(?:\.\d+)?) to evaluate", text)
    if m:
        out["evalCost"] = float(m.group(1).replace(",", ""))
    m = re.search(r"At ([\d.]+) tokens per second", text)
    if m:
        out["speed"] = float(m.group(1))
    m = re.search(
        r"Intelligence\n#\d+\s*/\s*\d+\n([\d.]+)\nArtificial Analysis Intelligence Index",
        text,
    )
    if m:
        out["intelligenceIndex"] = float(m.group(1))
    m = re.search(r"Speed\n#\d+\s*/\s*\d+\n([\d.]+)\nOutput tokens per second", text)
    if m:
        out["speed"] = float(m.group(1))
    return out


by_model = {}
catalog = {}  # slug -> object across all pages

for html_path in sorted(aa_dir.glob("*.html")):
    stem = html_path.stem
    if "__" not in stem:
        continue
    mid, variant = stem.split("__", 1)
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    if len(html) < 5000 or "Page not found" in html[:300]:
        continue
    text_path = html_path.with_suffix(".txt")
    text = text_path.read_text(encoding="utf-8", errors="ignore") if text_path.exists() else ""
    summary = parse_summary_speed_cost(text)
    objs = extract_objects(html)
    for o in objs:
        catalog[o["slug"]] = o

    # Prefer exact variant match, else closest family match
    chosen = None
    for o in objs:
        if o["slug"] == variant or o["slug"].startswith(variant) or variant.startswith(o["slug"]):
            chosen = o
            break
    if not chosen and objs:
        # pick object whose name appears in page title line
        title = text.split("\n", 40)[0:30]
        title_s = "\n".join(title)
        for o in sorted(objs, key=lambda x: -x["_coverage"]):
            if o.get("shortName") and o["shortName"].split("(")[0].strip() in title_s:
                chosen = o
                break
            if o.get("name") and o["name"].split("(")[0].strip() in title_s:
                chosen = o
                break
    if not chosen:
        # fallback: highest coverage object whose slug shares family token
        fam = mid.split("-")[0]
        cands = [o for o in objs if fam in o["slug"]]
        chosen = max(cands or objs, key=lambda x: x["_coverage"]) if objs else None

    metrics = {}
    if chosen:
        metrics = {
            "slug": chosen["slug"],
            "name": chosen["name"],
            "intelligenceIndex": chosen.get("intelligenceIndex"),
            "ifbench": None if chosen.get("ifbench") is None else round(chosen["ifbench"] * 100, 2),
            "hle": None if chosen.get("hle") is None else round(chosen["hle"] * 100, 2),
            "gpqa": None if chosen.get("gpqa") is None else round(chosen["gpqa"] * 100, 2),
            "critpt": None if chosen.get("critpt") is None else round(chosen["critpt"] * 100, 2),
            "scicode": None if chosen.get("scicode") is None else round(chosen["scicode"] * 100, 2),
            "lcr": None if chosen.get("lcr") is None else round(chosen["lcr"] * 100, 2),
            "terminalBenchHard": None
            if chosen.get("terminalbenchHard") is None
            else round(chosen["terminalbenchHard"] * 100, 2),
            "terminalBenchV21": None
            if chosen.get("terminalbenchV21") is None
            else round(chosen["terminalbenchV21"] * 100, 2),
            "gdpvalNormalized": None
            if chosen.get("gdpvalNormalized") is None
            else round(chosen["gdpvalNormalized"] * 100, 2),
            "gdpval": chosen.get("gdpval"),
            "omniAcc": None if chosen.get("omniAcc") is None else round(chosen["omniAcc"] * 100, 2),
            "omniHalluc": None
            if chosen.get("omniHalluc") is None
            else round(chosen["omniHalluc"] * 100, 2),
            "tau2": None if chosen.get("tau2") is None else round(chosen["tau2"] * 100, 2),
            "tauBanking": None
            if chosen.get("tauBanking") is None
            else round(chosen["tauBanking"] * 100, 2),
            "evalCost": chosen.get("evalCost"),
            "speed": chosen.get("speed"),
        }
    # Fill summary speed/cost/index when missing
    for k, v in summary.items():
        if metrics.get(k) is None and v is not None:
            metrics[k] = v

    entry = {
        "id": mid,
        "pageVariant": variant,
        "url": f"https://artificialanalysis.ai/models/{variant}",
        "chosenSlug": metrics.get("slug"),
        "aaName": metrics.get("name"),
        "metrics": metrics,
        "summary": summary,
        "objectsFound": len(objs),
        "coverage": sum(
            1
            for k in (
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
                "intelligenceIndex",
                "evalCost",
                "speed",
            )
            if metrics.get(k) is not None
        ),
    }
    prev = by_model.get(mid)
    if not prev or entry["coverage"] > prev["coverage"]:
        by_model[mid] = entry

# Also dump catalog for cross-page fill / variant selection
catalog_out = {
    slug: {k: v for k, v in obj.items() if not k.startswith("_")}
    for slug, obj in catalog.items()
}

payload = {
    "n": len(by_model),
    "models": by_model,
    "catalogSize": len(catalog_out),
}
out_path.write_text(json.dumps(payload, indent=2) + "\n")
(aa_dir / "aa_catalog.json").write_text(json.dumps(catalog_out, indent=2) + "\n")

# Print coverage matrix
print(f"models={len(by_model)} catalog={len(catalog_out)}")
dims = [
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
]
print("id".ljust(22), "cov", *[d[:6] for d in dims])
for mid, e in by_model.items():
    m = e["metrics"]
    cells = []
    for d in dims:
        v = m.get(d)
        cells.append("---" if v is None else f"{v:.1f}"[:6])
    print(mid.ljust(22), f"{e['coverage']:2d}", *cells)
