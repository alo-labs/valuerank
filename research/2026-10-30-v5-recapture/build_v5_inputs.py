"""Build the cohort inputs for the AA Intelligence Index v5 release (owner decisions O132, O51) from the v5 chart capture.

    python3 research/2026-10-30-v5-recapture/build_v5_inputs.py

Writes, in the schemas the 2026-10-25 refresh used: data/aa_frontier_capture.json (every plotted point, its tier, the
rendered Pareto path), data/aa_reconciliation_inventory.json (frontier and near-frontier rows), data/aa/aa_extract.json and
data/aa_mapping.json (the cohort's 27 configurations and their AA identities). Frontier membership is the rendered path's
vertices; the near gap is O51's: the public rounded Index within 3 points of the highest rendered-frontier Index at equal or
lower cost. Each family's required configuration is its highest rendered-frontier point (E193), or, for a family with near
points only, its highest near point.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
DATA = ROOT / "data"
CAPTURE = HERE / "v5-chart-capture.json"
COHORT = HERE / "cohort.json"
CATALOG_PAGE = HERE / "catalog-source.html"
GAP = 3
EFFORT_ORDER = ("low", "medium", "high", "xhigh", "max")
BENCHMARK = "Artificial Analysis Intelligence Index v5.0"


def parse_tooltip(text: str) -> dict:
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    head = lines[0]
    starred = head.endswith("*")
    name = head.rstrip("*").strip()
    cost = float(re.search(r"\$([\d,]+(?:\.\d+)?)", text).group(1).replace(",", ""))
    index = int(lines[lines.index("Artificial Analysis Intelligence Index") + 1])
    footnote = next((line[2:].strip() for line in lines if line.startswith("* ")), None) if starred else None
    match = re.fullmatch(r"(.+?) \((.+)\)", name)
    family, variant = (match.group(1), match.group(2)) if match else (name, None)
    fallback = "with fallback" if variant and variant.endswith("with fallback") else None
    effort = variant.replace("with fallback", "").strip() if variant else None
    return {"model_name": name, "family": family, "effort": effort or None, "fallback": fallback, "intelligence_index_display": index,
            "total_cost_usd": cost, "footnote": footnote}


def catalog() -> dict:
    """AA's own model catalog ({slug, name}) embedded in a model page, keyed by lower-case name."""

    html = CATALOG_PAGE.read_text()
    return {name.lower(): slug for slug, name in re.findall(r'\\"slug\\":\\"([a-z0-9.\-]+)\\",\\"name\\":\\"([^"\\]+)\\",\\"releaseSlug\\"', html)}


def catalog_url(point: dict, names: dict) -> str | None:
    effort, family = point["effort"], point["family"]
    candidates = [point["model_name"].lower()]
    if effort and point["fallback"]:
        candidates.append(f"{family} ({effort}, default fallback)".lower())
    if not effort and point["fallback"]:
        candidates.append(f"{family} (default fallback)".lower())
    slug = next((names[name] for name in candidates if name in names), None)
    return f"https://artificialanalysis.ai/models/{slug}" if slug else None


def main() -> None:
    capture = json.loads(CAPTURE.read_text())
    cohort = json.loads(COHORT.read_text())["configurations"]
    by_url = {item["url"]: item for item in cohort}
    names = catalog()
    path = capture["paretoPaths"][0]["d"]
    vertices = [tuple(map(float, pair)) for pair in re.findall(r"([\d.]+)[ ,]([\d.]+)", path)]
    points = []
    for hover in capture["hovers"]:
        point = {**parse_tooltip(hover["tooltip"]), "circle_id": hover["id"], "svg_x": hover["cx"], "svg_y": hover["cy"]}
        point["url"] = catalog_url(point, names)
        points.append(point)
    frontier = []
    for x, y in vertices:
        match = [point for point in points if abs(point["svg_x"] - x) < 1e-6 and abs(point["svg_y"] - y) < 1e-6]
        if len(match) != 1:
            raise ValueError(f"Pareto vertex ({x}, {y}) matches {len(match)} circles")
        frontier.append(match[0])
    frontier_ids = {id(point) for point in frontier}
    for point in points:
        reach = [item for item in frontier if item["total_cost_usd"] <= point["total_cost_usd"]]
        best = max(reach, key=lambda item: item["intelligence_index_display"]) if reach else None
        point["intelligence_gap"] = best["intelligence_index_display"] - point["intelligence_index_display"] if best else None
        point["nearest_frontier"] = best
        point["cost_ratio"] = round(point["total_cost_usd"] / min(item["total_cost_usd"] for item in frontier
                                                                  if item["intelligence_index_display"] >= point["intelligence_index_display"]), 4) \
            if any(item["intelligence_index_display"] >= point["intelligence_index_display"] for item in frontier) else None
        point["tier"] = "frontier" if id(point) in frontier_ids else ("near" if point["intelligence_gap"] is not None and point["intelligence_gap"] <= GAP else "dominated")
    near = sorted((point for point in points if point["tier"] == "near"), key=lambda item: item["total_cost_usd"])
    cohort_points = frontier + near
    missing = [point["model_name"] for point in cohort_points if point["url"] not in by_url]
    if missing or len(cohort_points) != len(cohort):
        raise ValueError(f"cohort.json does not match the chart's frontier and near points: {missing}")

    def required(point: dict) -> str:
        """E193: the family's highest rendered-frontier point, else (near-only family) its highest near point."""

        family = [item for item in frontier if item["family"] == point["family"]] or [item for item in near if item["family"] == point["family"]]
        top = max(family, key=lambda item: (item["intelligence_index_display"], item["total_cost_usd"]))  # build_scores.frontier_order
        return by_url[top["url"]]["id"]

    def strip(point: dict) -> dict:
        return {key: value for key, value in point.items() if key not in ("nearest_frontier",)}

    ordered = [{"order": index, **strip(point)} for index, point in enumerate(sorted(points, key=lambda item: -item["intelligence_index_display"]))]
    capture_doc = {
        "captured_at": capture["capturedAt"], "local_capture_date": capture["capturedAt"][:10], "local_timezone": "UTC",
        "source_url": capture["sourceUrl"], "source_owner": "Artificial Analysis", "index_version": "5.0", "chart_title": capture["chartTitle"],
        "x_axis": "Cost to Run Intelligence Index (USD, Log Scale)", "y_axis": "Artificial Analysis Intelligence Index",
        "cost_unit": "USD to run all Intelligence Index evaluations",
        "universe": {"catalog_models": int(capture["selectorAfter"].split(" of ")[1].split()[0]), "selected_models": int(capture["selectorAfter"].split(" of ")[0]),
                     "plotted_models_with_both_coordinates": len(points), "rendered_pareto_vertices": len(frontier), "near_frontier_points": len(near),
                     "model_families": len({point["family"] for point in cohort_points}),
                     "selection_evidence": f"The chart's model selector displayed '{capture['selectorAfter']}' after Select all (it showed '{capture['selectorBefore']}' before). "
                                           f"The chart SVG held {len(points)} circles and one dotted Pareto path (stroke-dasharray '{capture['paretoPaths'][0]['dash']}') with "
                                           f"{len(frontier)} M/L coordinate pairs, each matching a circle centre exactly."},
        "method": "research/2026-10-30-v5-recapture/capture_chart.mjs: Playwright (headless Chromium 1600 x 1200; no sign-in; optional cookies declined). The chart's "
                  "model selector set to Select all; every circle centre and the dotted Pareto path read from the chart SVG; each circle hovered at its on-screen "
                  "centre from a neutral point and its public tooltip recorded verbatim. No embedded payload, API, export or paid data was used for the chart values; "
                  "owner URLs come from AA's own catalog ({slug, name}) embedded in a model page.",
        "precision": {"intelligence_index": "Rounded integer displayed by public tooltip; raw precision is not recovered from SVG coordinates.",
                      "total_cost_usd": "Two decimal places displayed by public tooltip."},
        "duplicate_resolution": f"None needed: every circle-centre hover returned a distinct tooltip ({len(points)} distinct for {len(points)} circles).",
        "comparison_to_previous_capture": {"previous_inventory": "data/aa_frontier_capture.json captured 2026-10-25T09:53:28Z (Intelligence Index v4.3.2)",
                                           "basis": "AA replaced Intelligence Index v4.3.2 with v5.0 (owner decision O132): the Index, its evaluations and the chart's "
                                                    "universe changed, so the frontier is re-read rather than compared vertex by vertex."},
        "family_groups": [{"family": family, "efforts": [point["effort"] or "none" for point in frontier if point["family"] == family],
                           "frontier_configurations": sum(1 for point in frontier if point["family"] == family),
                           **({"fallback": "with fallback"} if any(point["fallback"] for point in frontier if point["family"] == family) else {})}
                          for family in dict.fromkeys(point["family"] for point in frontier)],
        "near_frontier_policy": {"rule": "intelligence_gap_at_cost", "max_intelligence_gap": GAP,
                                 "basis": "Public rounded integer Intelligence Index and two-decimal USD total cost from the chart tooltips. The frontier's intelligence at a "
                                          "point's cost is the highest intelligence among rendered-frontier points whose cost is at or below that cost; a point cheaper than "
                                          "every frontier point has no gap.", "cost_ratio": "reported only"},
        "frontier": [{"order": index + 1, **strip(point)} for index, point in enumerate(frontier)],
        "near_frontier": [{"order": index + 1, **strip(point), "nearest_frontier_model_name": point["nearest_frontier"]["model_name"],
                           "nearest_frontier_url": point["nearest_frontier"]["url"]} for index, point in enumerate(near)],
        "points": ordered,
        "rendered_pareto_svg_path": path,
    }
    (DATA / "aa_frontier_capture.json").write_text(json.dumps(capture_doc, indent=2, ensure_ascii=False) + "\n")

    previous = json.loads((DATA / "aa_reconciliation_inventory.json").read_text())

    def variant(point: dict) -> str:
        return (point["effort"] + (" with fallback" if point["fallback"] else "")) if point["effort"] else ("reasoning" if not point["fallback"] else "with fallback")

    def inventory_row(point: dict, near_row: bool) -> dict:
        row = {"aaId": point["url"].rsplit("/", 1)[1], "name": point["model_name"], "evaluatedVariant": variant(point),
               "intelligenceIndex": point["intelligence_index_display"], "totalCostUsd": point["total_cost_usd"]}
        if near_row:
            row.update({"intelligenceGap": point["intelligence_gap"], "costRatio": point["cost_ratio"],
                        "nearestFrontierAaId": point["nearest_frontier"]["url"].rsplit("/", 1)[1]})
        return {**row, "directlyObservedFrontier": not near_row, "sourceUrl": point["url"], "family": point["family"],
                "requiredFamilyModelId": required(point), "sourceFootnote": point["footnote"]}

    inventory = {
        **{key: previous[key] for key in ("mode", "intelligenceIndexPrecision", "nearFrontierPolicy", "requiredFamilyPolicy", "nearFrontierFamilyPolicy")},
        "observedAt": capture["capturedAt"], "benchmarkVersion": BENCHMARK, "sourceUrl": capture["sourceUrl"],
        "scope": f"Complete displayed intelligence versus total evaluation cost Pareto line with all {capture_doc['universe']['catalog_models']} catalog models "
                 f"selected; {len(points)} eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.",
        "sourceUniverse": {"selectedModelN": capture_doc["universe"]["selected_models"], "plottedPointN": len(points), "observedFrontierPointN": len(frontier),
                           "nearFrontierPointN": len(near)},
        "completeness": {"status": "complete", "note": f"All {capture_doc['universe']['catalog_models']} catalog models selected; all {len(points)} plotted points and all "
                                                       f"{len(frontier)} Pareto path vertices captured from public tooltips (rounded integer Intelligence Index, two-decimal "
                                                       f"USD total cost) with Playwright on {capture['capturedAt'][:10]}. Every hover returned a distinct tooltip, so no "
                                                       "overlapped-circle resolution was needed. No hidden state or paid export used."},
        "rosterDecisions": [],
        "rows": [inventory_row(point, False) for point in frontier],
        "nearFrontierRows": [inventory_row(point, True) for point in near],
        "captureArtifact": "data/aa_frontier_capture.json",
    }
    (DATA / "aa_reconciliation_inventory.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n")

    point_by_url = {point["url"]: point for point in cohort_points}
    extract = [{"id": item["id"], "displayName": item["displayName"], "url": item["url"], "variant": item["url"].rsplit("/", 1)[1],
                "note": f"AA Intelligence Index v5 cohort (O51, O132): {item['chartTier']} point on the 2026-10-30 chart."} for item in cohort]
    (DATA / "aa" / "aa_extract.json").write_text(json.dumps(extract, indent=2, ensure_ascii=False) + "\n")
    mapping = []
    primaries = {required(point) for point in cohort_points}
    for item in cohort:
        point = point_by_url[item["url"]]
        # A family's required configuration carries the family's name (the score build checks it); other efforts their own.
        name = point["family"] if item["id"] in primaries else item["displayName"]
        mapping.append({"id": item["id"], "displayName": name, "urls": [item["url"]], "aaSlug": item["url"].rsplit("/", 1)[1],
                        "aaVariant": point["effort"], "family": point["family"]})
    (DATA / "aa_mapping.json").write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"plotted": len(points), "frontier": len(frontier), "near": len(near), "cohort": len(cohort),
                      "required": sorted({required(point) for point in cohort_points})}, indent=1))


if __name__ == "__main__":
    main()
