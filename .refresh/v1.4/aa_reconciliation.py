#!/usr/bin/env python3
"""Reconcile a dated AA intelligence/total-cost inventory with exact source IDs.

The inventory may capture the complete displayed AA frontier directly, with
catalog/plotted-point counts, or the full numeric chart universe. Neither mode
uses the selected ValueRank roster as evidence of AA-wide completeness.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html import escape
import json
import math
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
INVENTORY = REFRESH / "aa_reconciliation_inventory.json"
REPORT = REFRESH / "aa_reconciliation_report.json"
MAX_AGE_DAYS = 7


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def aa_url(value):
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and parsed.netloc == "artificialanalysis.ai"


def read_json(path):
    return json.loads(path.read_text())


def variant_key(row):
    return (row["aaId"], row.get("evaluatedVariant") or row["name"])


def canonical_variant(value):
    """Separate effort, reasoning mode, and fallback instead of comparing phrases."""
    text = str(value or "").lower().replace("_", "-")
    efforts = set(re.findall(r"\b(xhigh|high|medium|low|max|mini)\b", text))
    nonreasoning = "non-reasoning" in text or "non reasoning" in text
    return {"effort": next(iter(efforts)) if len(efforts) == 1 else None,
            "ambiguous": len(efforts) > 1,
            "reasoning": False if nonreasoning else True if "reasoning" in text else None,
            "fallback": "fallback" in text}


def combined_variant(declared, label, reasoning=None):
    explicit, displayed = canonical_variant(declared), canonical_variant(label)
    if declared and not explicit["effort"] and explicit["reasoning"] is None and not explicit["fallback"]:
        return None
    if explicit["ambiguous"] or displayed["ambiguous"]:
        return None
    if explicit["effort"] and displayed["effort"] and explicit["effort"] != displayed["effort"]:
        return None
    modes = [value for value in (explicit["reasoning"], displayed["reasoning"], reasoning) if value is not None]
    if modes and any(value != modes[0] for value in modes):
        return None
    return {"effort": explicit["effort"] or displayed["effort"],
            "reasoning": modes[0] if modes else None,
            "fallback": explicit["fallback"] or displayed["fallback"]}


def exact_roster_match(row, roster):
    captured = combined_variant(row.get("evaluatedVariant"), row["name"], row.get("isReasoning"))
    if captured is None:
        return None
    matches = []
    for model_id, item in roster:
        if item.get("aaSlug") != row["aaId"]:
            continue
        selected = combined_variant(item.get("aaVariant"), " ".join(str(item.get(key) or "") for key in ("aaName", "aaShortName")), item.get("isReasoning"))
        if selected is None or captured["effort"] != selected["effort"] or captured["fallback"] != selected["fallback"]:
            continue
        if captured["reasoning"] is not None and captured["reasoning"] != selected["reasoning"]:
            continue
        # Validate declared effort/mode before an identical display name can match.
        if row["name"] in (item.get("aaName"), item.get("aaShortName")) or row.get("evaluatedVariant"):
            matches.append(model_id)
    return matches[0] if len(matches) == 1 else None


def reconcile(now=None):
    now = now or datetime.now(timezone.utc)
    report = {"schemaVersion": 1, "checkedAt": now.isoformat(), "inventoryPath": str(INVENTORY.relative_to(ROOT)),
              "maxAgeDays": MAX_AGE_DAYS, "issues": [], "frontier": [], "comparisonCandidates": [],
              "frontierDefinition": "Higher AA intelligence index and lower AA total evaluation cost; at least one strict improvement dominates.",
              "scope": "unknown", "completeness": {"status": "missing"}}
    issues = report["issues"]
    try:
        doc = read_json(INVENTORY)
        if not isinstance(doc, dict):
            raise ValueError("inventory root must be an object")
    except (OSError, ValueError) as exc:
        issues.append(f"Missing or invalid inventory: {exc}. Capture the AA intelligence-versus-total-cost chart universe with exact model IDs and dated source evidence.")
        report["status"] = "blocked"
        return report
    report.update({key: doc.get(key) for key in ("observedAt", "benchmarkVersion", "sourceUrl", "scope", "completeness", "mode", "sourceUniverse")})
    observed_frontier = doc.get("mode") == "observedFrontier"
    if doc.get("mode") not in ("observedFrontier", "fullNumericUniverse"):
        issues.append("Inventory mode must be observedFrontier or fullNumericUniverse.")
    if observed_frontier:
        report["frontierDefinition"] = "Directly observed AA displayed intelligence-versus-total-cost frontier; not recomputed from a subset."
    try:
        observed = datetime.fromisoformat(doc["observedAt"].replace("Z", "+00:00"))
        if observed.tzinfo is None:
            raise ValueError("timezone required")
        age = (now - observed).total_seconds() / 86400
        report["ageDays"] = round(age, 3)
        if age < -1 / 24 or age > MAX_AGE_DAYS:
            issues.append(f"Inventory is stale or future-dated ({age:.2f} days); recapture within {MAX_AGE_DAYS} days.")
    except (KeyError, TypeError, ValueError, AttributeError):
        issues.append("Inventory observedAt must be a timezone-qualified ISO 8601 timestamp.")
    completeness = doc.get("completeness") or {}
    if not isinstance(completeness, dict) or completeness.get("status") != "complete":
        issues.append("Inventory is partial or completeness is unknown; its frontier is only among observed rows, not all AA models.")
    if not doc.get("scope") or not isinstance(completeness, dict) or not completeness.get("note"):
        issues.append("Document the chart universe/filter scope and capture-completeness evidence.")
    if not aa_url(doc.get("sourceUrl")) or not doc.get("benchmarkVersion"):
        issues.append("Inventory requires a first-party AA source URL and exact benchmark version.")
    rows = doc.get("rows")
    if not isinstance(rows, list) or not rows:
        issues.append("Inventory rows must be a nonempty array.")
        rows = []
    if observed_frontier:
        universe = doc.get("sourceUniverse") or {}
        if not isinstance(universe, dict) or any(not isinstance(universe.get(key), int) or isinstance(universe.get(key), bool) or universe[key] <= 0
               for key in ("selectedModelN", "plottedPointN", "observedFrontierPointN")):
            issues.append("Observed frontier requires positive selectedModelN, plottedPointN, and observedFrontierPointN source counts.")
        elif not (len(rows) == universe["observedFrontierPointN"] <= universe["plottedPointN"] <= universe["selectedModelN"]):
            issues.append("Frontier capture row count does not reconcile with displayed frontier/plotted/catalog counts.")
    try:
        metrics = read_json(REFRESH / "aa_metrics.json")
        roster = list(metrics["models"].items())
        if doc.get("benchmarkVersion") != metrics.get("benchmarkVersion"):
            issues.append("Inventory benchmark version differs from aa_metrics.json; recapture or migrate the exact version before publishing.")
        scores = read_json(REFRESH / "scores.json")
        ranked = {item["id"] for item in scores["models"] if item.get("rankingEligible") is True}
        primary_gaps = {item["id"]: item.get("rankingExclusionReasons", []) for item in scores["models"]}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        issues.append(f"Source roster or ranking unavailable: {exc}")
        roster, ranked, primary_gaps = [], set(), {}
    decisions = {}
    decision_rows = doc.get("rosterDecisions", [])
    if not isinstance(decision_rows, list):
        issues.append("rosterDecisions must be an array.")
        decision_rows = []
    for decision in decision_rows:
        try:
            reviewed = datetime.fromisoformat(decision["reviewedAt"].replace("Z", "+00:00"))
            captured = datetime.fromisoformat(doc["observedAt"].replace("Z", "+00:00"))
            if reviewed.tzinfo is None or reviewed < captured or (reviewed - now).total_seconds() > 3600:
                raise ValueError("review date must follow capture and not be future-dated")
            if decision.get("decision") != "defer" or not isinstance(decision.get("reason"), str) or not decision["reason"].strip():
                raise ValueError("explicit defer decision and reason required")
            key = variant_key(decision)
            if key in decisions:
                raise ValueError("duplicate decision")
            decisions[key] = decision
        except (KeyError, TypeError, AttributeError, ValueError) as exc:
            issues.append(f"Invalid exact-variant roster decision: {exc}")
    valid, seen = [], set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            issues.append(f"Inventory row {index} is not an object.")
            continue
        identity = row.get("aaId")
        if not isinstance(identity, str) or not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", identity):
            issues.append(f"Inventory row {index} lacks an exact AA model URL slug.")
            continue
        if not isinstance(row.get("name"), str) or not row["name"] or row.get("sourceUrl") != f"https://artificialanalysis.ai/models/{identity}":
            issues.append(f"{identity}: name and matching exact model source URL required.")
            continue
        if row.get("evaluatedVariant") is not None and (not isinstance(row["evaluatedVariant"], str) or not row["evaluatedVariant"]):
            issues.append(f"{identity}: evaluatedVariant must be a nonempty string when supplied.")
            continue
        if row.get("isReasoning") is not None and not isinstance(row["isReasoning"], bool):
            issues.append(f"{identity}: isReasoning must be boolean when supplied.")
            continue
        if combined_variant(row.get("evaluatedVariant"), row["name"], row.get("isReasoning")) is None:
            issues.append(f"{identity}: declared variant contradicts its displayed label or has unsupported/ambiguous metadata.")
            continue
        identity_variant = variant_key(row)
        if identity_variant in seen:
            issues.append(f"Duplicate exact AA evaluated variant: {identity_variant}.")
            continue
        seen.add(identity_variant)
        intelligence, cost = row.get("intelligenceIndex"), row.get("totalCostUsd")
        if observed_frontier and row.get("directlyObservedFrontier") is not True:
            issues.append(f"{row['name']}: direct observation of displayed AA frontier membership required.")
            continue
        if observed_frontier and ((intelligence is not None and not number(intelligence)) or (cost is not None and (not number(cost) or cost < 0))):
            issues.append(f"{row['name']}: invalid optional numeric metric.")
            continue
        if not observed_frontier and (not number(intelligence) or not number(cost) or cost < 0):
            issues.append(f"{identity}: intelligence index or total evaluation cost missing/invalid; dominance cannot be established.")
            continue
        model_id = exact_roster_match(row, roster)
        deferred = decisions.get(identity_variant) if model_id is None else None
        valid.append({**row, "valueRankModelId": model_id,
                      "intelligenceIndexPrecision": row.get("intelligenceIndexPrecision") or doc.get("intelligenceIndexPrecision"),
                      "rosterDecision": deferred,
                      "primaryRankingGaps": primary_gaps.get(model_id, ["Exact evaluated variant absent from source roster"]),
                      "metricGap": "Numeric intelligence/cost values not fully available in the public chart capture" if not number(intelligence) or not number(cost) else None,
                      "rankStatus": "Primary ranked" if model_id in ranked else "Unranked source candidate" if model_id else "Deferred comparison candidate" if deferred else "Missing from source roster"})
    frontier = valid if observed_frontier else [row for row in valid if not any(
        other["intelligenceIndex"] >= row["intelligenceIndex"] and other["totalCostUsd"] <= row["totalCostUsd"]
        and (other["intelligenceIndex"] > row["intelligenceIndex"] or other["totalCostUsd"] < row["totalCostUsd"])
        for other in valid)]
    report["frontier"] = sorted(frontier, key=lambda row: (row.get("totalCostUsd") if number(row.get("totalCostUsd")) else math.inf, row["aaId"], row["name"]))
    report["comparisonCandidates"] = [row for row in valid if not row["valueRankModelId"]]
    report["metricGaps"] = [{"aaId": row["aaId"], "name": row["name"], "gap": row["metricGap"]} for row in valid if row["metricGap"]]
    report["observedRowN"] = len(rows)
    report["validRowN"] = len(valid)
    report["missingFrontierIds"] = [row["aaId"] + " :: " + row["name"] for row in report["frontier"] if not row["valueRankModelId"]]
    report["unresolvedFrontierIds"] = [row["aaId"] + " :: " + row["name"] for row in report["frontier"] if not row["valueRankModelId"] and not row["rosterDecision"]]
    report["deferredFrontierIds"] = [row["aaId"] + " :: " + row["name"] for row in report["frontier"] if row["rosterDecision"]]
    for key in decisions:
        if key not in seen:
            issues.append(f"Roster decision does not match an observed evaluated variant: {key}.")
    if report["unresolvedFrontierIds"]:
        issues.append("Frontier entrants missing from exact source roster without a dated review decision: " + ", ".join(report["unresolvedFrontierIds"]) + ". Add exact evidence with gaps or explicitly defer each evaluated variant; never transfer a lower-effort result to the selected variant.")
    report["status"] = "blocked" if issues else "reconciled"
    return report


def publication(report):
    """Return escaped Markdown and HTML comparison views, including blocked scope."""
    summary = (f"Observed {report.get('observedAt') or 'unknown date'}; {report.get('benchmarkVersion') or 'unknown version'}. "
               f"Scope: {report.get('scope') or 'unknown'}. Reconciliation: {report['status']}. "
               "This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately.")
    if report["issues"]:
        summary += " Gaps: " + " ".join(report["issues"])
    if report.get("mode") == "observedFrontier":
        summary += " Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. "
        universe = report.get("sourceUniverse") if isinstance(report.get("sourceUniverse"), dict) else {}
        summary += f"Source selected {universe.get('selectedModelN', 'unknown')} models, plotted {universe.get('plottedPointN', 'unknown')} eligible points, and displayed {universe.get('observedFrontierPointN', 'unknown')} frontier points. Public metric/export gaps are shown explicitly."
    selected = {variant_key(row): row for row in report["frontier"] + report["comparisonCandidates"]}
    frontier_ids = {variant_key(row) for row in report["frontier"]}
    md_rows, html_rows = [], []
    for row in selected.values():
        flag = "Observed AA frontier" if variant_key(row) in frontier_ids else "Comparison candidate"
        intelligence = "Not publicly captured"
        if number(row.get("intelligenceIndex")):
            precision = row.get("intelligenceIndexPrecision")
            intelligence = (f"{row['intelligenceIndex']:.0f} (rounded)" if precision == "rounded_whole_public_label"
                            else str(row['intelligenceIndex']) if report.get("mode") == "observedFrontier"
                            else f"{row['intelligenceIndex']:.2f}")
        cost = f"${row['totalCostUsd']:,.2f}" if number(row.get("totalCostUsd")) else "Not publicly captured"
        gap_text = "; ".join(row.get("primaryRankingGaps", [])) or "None"
        if row.get("rosterDecision"):
            decision = row["rosterDecision"]
            gap_text += f"; Reviewed {decision['reviewedAt']}: {decision['reason']}"
        cells = [row["name"], row["aaId"], intelligence, cost, flag, row["rankStatus"], gap_text]
        md_cells = [str(cell).replace("|", "\\|").replace("\n", " ") for cell in cells]
        md_cells[0] = f"[{md_cells[0].replace('[', '&#91;').replace(']', '&#93;')}]({row['sourceUrl']})"
        md_rows.append("| " + " | ".join(md_cells) + " |")
        html_cells = [escape(str(cell)) for cell in cells]
        html_cells[0] = f'<a href="{escape(row["sourceUrl"], quote=True)}" target="_blank" rel="noopener">{html_cells[0]}</a>'
        html_rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in html_cells) + "</tr>")
    headers = ["Exact AA model", "AA ID", "Intelligence index", "Total evaluation cost (USD)", "Observed comparison", "Primary rank status", "Primary evidence gaps"]
    markdown = "\n\n## AA intelligence and total-cost comparison\n\n" + summary + "\n\n| " + " | ".join(headers) + " |\n|" + "---|" * len(headers) + "\n" + "\n".join(md_rows) + "\n"
    html = ('<!-- aa-reconciliation:start --><section class="card mb-6" id="aa-frontier-comparison" aria-labelledby="aa-frontier-heading">'
            '<h2 id="aa-frontier-heading">AA intelligence and total-cost comparison</h2><p class="method-text">' + escape(summary)
            + '</p><div style="overflow-x:auto"><table><thead><tr>' + "".join(f"<th scope=\"col\">{escape(header)}</th>" for header in headers)
            + "</tr></thead><tbody>" + "".join(html_rows) + "</tbody></table></div></section><!-- aa-reconciliation:end -->")
    return markdown, html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-only", action="store_true", help="Write an honest blocked report without passing the refresh gate")
    args = parser.parse_args()
    report = reconcile()
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"AA reconciliation {report['status']}: {REPORT.relative_to(ROOT)}")
    for issue in report["issues"]:
        print("- " + issue)
    return 0 if args.report_only or report["status"] == "reconciled" else 1


if __name__ == "__main__":
    raise SystemExit(main())
