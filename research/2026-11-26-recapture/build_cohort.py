"""Derive the 2026-11-26 cohort (O51, O145) from the chart capture: rendered frontier, O51 near gap, and the previous cohort's
rows that left (retained one release, O145). Resolves AA model-page URLs from the family pages' embedded variant lists.

    python3 research/2026-11-26-recapture/build_cohort.py
"""
from __future__ import annotations

import importlib.util
import json
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location("bi", HERE / "build_inputs.py")
bi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bi)

GAP = 3


def fetch(url: str) -> str:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as response:
        return response.read().decode("utf-8", "replace").replace('\\"', '"')


def family_catalog(seed: str) -> dict:
    page = fetch("https://artificialanalysis.ai/models/" + seed)
    return {name.lower(): slug for slug, name in re.findall(r'"slug":"([a-z0-9.\-]+)","name":"([^"]+)","releaseDate"', page)}


def variants(family_slug: str) -> dict:
    page = fetch("https://artificialanalysis.ai/models/" + family_slug)
    pairs = re.findall(r'"slug":"([a-z0-9.\-]+)","name":"([^"]+)","shortName":"([^"]+)"', page)
    plain = lambda text: re.sub(r", default fallback", "", text.lower())
    return {plain(short): slug for slug, name, short in pairs} | {plain(name): slug for slug, name, short in pairs}


def main() -> None:
    capture = json.loads((HERE / "chart-capture.json").read_text())
    path = capture["paretoPaths"][0]["d"]
    vertices = [tuple(map(float, pair)) for pair in re.findall(r"([\d.]+)[ ,]([\d.]+)", path)]
    points = [{**bi.parse_tooltip(h["tooltip"]), "cx": h["cx"], "cy": h["cy"]} for h in capture["hovers"]]
    frontier, seen = [], set()
    for x, y in vertices:
        match = [p for p in points if abs(p["cx"] - x) < 1e-6 and abs(p["cy"] - y) < 1e-6]
        if len(match) != 1:
            raise ValueError(f"vertex ({x}, {y}) matches {len(match)} circles")
        if match[0]["model_name"] not in seen:
            seen.add(match[0]["model_name"])
            frontier.append(match[0])
    ids = {p["model_name"] for p in frontier}
    near = []
    for p in points:
        if p["model_name"] in ids:
            continue
        reach = [f for f in frontier if f["total_cost_usd"] <= p["total_cost_usd"]]
        best = max(reach, key=lambda f: f["intelligence_index_display"]) if reach else None
        if best and best["intelligence_index_display"] - p["intelligence_index_display"] <= GAP:
            near.append(p)
    previous = json.loads((ROOT / "data" / "aa_frontier_capture.json").read_text())
    # AA's chart dropped the " with fallback" wording on the Claude labels (page names still say "Default Fallback"); same slugs and costs.
    previous_names = [re.sub(r" with fallback\)$", ")", re.sub(r" with fallback$", "", p["model_name"])).replace(" with fallback)", ")")
                      for p in previous["frontier"] + previous["near_frontier"]]
    names_now = {p["model_name"] for p in frontier + near}
    by_name = {p["model_name"]: p for p in points}
    retained = [by_name[n] for n in dict.fromkeys(previous_names) if n not in names_now and n in by_name]
    gone = [n for n in dict.fromkeys(previous_names) if n not in names_now and n not in by_name]
    families = {}
    catalog = family_catalog("gemini-4-carbon")

    def resolve(p: dict) -> str | None:
        fam = p["family"]
        if fam not in families:
            slug = catalog.get(fam.lower()) or re.sub(r"[^a-z0-9]+", "-", fam.lower()).strip("-")
            try:
                families[fam] = variants(slug)
                families[fam]["__slug"] = slug
            except Exception:
                families[fam] = {}
        vmap = families[fam]
        label = re.sub(r" with fallback\)$", ")", p["model_name"].lower())
        slug = vmap.get(label)
        if slug is None and p["effort"] is None:
            slug = vmap.get("__slug")
        return slug

    urls = {p["model_name"]: (f"https://artificialanalysis.ai/models/{resolve(p)}" if resolve(p) else None) for p in points}
    (HERE / "urls.json").write_text(json.dumps(urls, indent=2) + "\n")
    out = []
    for tier, group in (("frontier", frontier), ("near", near), ("retained", retained)):
        for p in group:
            slug = resolve(p)
            out.append({"id": slug, "displayName": p["model_name"], "url": urls[p["model_name"]],
                        "chartTier": tier, "intelligenceIndex": p["intelligence_index_display"], "totalCostUsd": p["total_cost_usd"]})
    (HERE / "cohort.json").write_text(json.dumps({"capturedFrom": "chart-capture.json", "configurations": out}, indent=2) + "\n")
    print(json.dumps({"frontier": len(frontier), "near": len(near), "retained": len(retained), "left_chart_entirely": gone,
                      "unresolved": [o["displayName"] for o in out if not o["url"]], "unresolved_points": [n for n, u in urls.items() if not u]}, indent=1))


if __name__ == "__main__":
    main()
