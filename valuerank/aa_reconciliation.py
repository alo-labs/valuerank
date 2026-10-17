#!/usr/bin/env python3
"""Reconcile a dated AA intelligence/total-cost inventory with exact source IDs.

The inventory may capture the complete displayed AA frontier directly, with
catalog/plotted-point counts, or the full numeric chart universe. Neither mode
uses the selected ValueRank roster as evidence of AA-wide completeness.

An observed-frontier inventory also carries the near-frontier policy: a plotted
configuration is near the rendered frontier when its public Intelligence Index
is within ``nearFrontierPolicy.maxIntelligenceGap`` points of the frontier's
intelligence at its cost (the highest intelligence among frontier points costing
no more).  Cost ratio is informational only.  Each near-frontier family must be
in the primary ranking (its selected configuration may differ from the near
one) or be explicitly deferred by a dated roster decision, like frontier families.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html import escape
import json
import math
from pathlib import Path

from valuerank.clock import utcnow
import re
from urllib.parse import urlparse

from valuerank.paths import DATA, ROOT
INVENTORY = DATA / "aa_reconciliation_inventory.json"
REPORT = DATA / "aa_reconciliation_report.json"
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


def check_row_identity(row, index, near, seen, issues):
    """Shared exact-identity checks for frontier and near-frontier rows.

    Returns the exact evaluated-variant key, or None when the row is rejected
    (the reason is appended to ``issues``).  Accepted keys join ``seen``.
    """
    kind, prefix = ("Near-frontier", "Near-frontier ") if near else ("Inventory", "")
    if not isinstance(row, dict):
        issues.append(f"{kind} row {index} is not an object.")
        return None
    identity = row.get("aaId")
    if not isinstance(identity, str) or not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", identity):
        issues.append(f"{kind} row {index} lacks an exact AA model URL slug.")
        return None
    if not isinstance(row.get("name"), str) or not row["name"] or row.get("sourceUrl") != f"https://artificialanalysis.ai/models/{identity}":
        issues.append(f"{prefix}{identity}: name and matching exact model source URL required.")
        return None
    if row.get("evaluatedVariant") is not None and (not isinstance(row["evaluatedVariant"], str) or not row["evaluatedVariant"]):
        issues.append(f"{prefix}{identity}: evaluatedVariant must be a nonempty string when supplied.")
        return None
    if row.get("isReasoning") is not None and not isinstance(row["isReasoning"], bool):
        issues.append(f"{prefix}{identity}: isReasoning must be boolean when supplied.")
        return None
    if combined_variant(row.get("evaluatedVariant"), row["name"], row.get("isReasoning")) is None:
        issues.append(f"{prefix}{identity}: declared variant contradicts its displayed label or has unsupported/ambiguous metadata.")
        return None
    identity_variant = variant_key(row)
    if identity_variant in seen:
        issues.append(f"Duplicate exact AA evaluated variant: {identity_variant}.")
        return None
    seen.add(identity_variant)
    footnote = row.get("sourceFootnote")
    if footnote is not None and (not isinstance(footnote, str) or not footnote.strip()):
        issues.append(f"{row['name']}: sourceFootnote must be a nonempty string or null.")
        return None
    return identity_variant


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


def reconcile(now=None, data=None):
    """Reconcile the frontier inventory under ``data`` (default: the module DATA dir) as of ``now``."""

    now = now or utcnow()
    data = DATA if data is None else data
    inventory = data / "aa_reconciliation_inventory.json"
    report = {"schemaVersion": 1, "checkedAt": now.isoformat(), "inventoryPath": str(inventory.relative_to(data.parent)),
              "maxAgeDays": MAX_AGE_DAYS, "issues": [], "frontier": [], "comparisonCandidates": [],
              "frontierDefinition": "Higher AA intelligence index and lower AA total evaluation cost; at least one strict improvement dominates.",
              "scope": "unknown", "completeness": {"status": "missing"},
              "nearFrontierPolicy": None, "nearFrontier": [], "nearFrontierFamilies": [],
              "missingNearFrontierIds": [], "unresolvedNearFrontierIds": [], "deferredNearFrontierIds": []}
    issues = report["issues"]
    try:
        doc = read_json(inventory)
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
    max_gap, near_rows = None, []
    if observed_frontier:
        universe = doc.get("sourceUniverse") or {}
        if not isinstance(universe, dict) or any(not isinstance(universe.get(key), int) or isinstance(universe.get(key), bool) or universe[key] <= 0
               for key in ("selectedModelN", "plottedPointN", "observedFrontierPointN")):
            issues.append("Observed frontier requires positive selectedModelN, plottedPointN, and observedFrontierPointN source counts.")
        elif not (len(rows) == universe["observedFrontierPointN"] <= universe["plottedPointN"] <= universe["selectedModelN"]):
            issues.append("Frontier capture row count does not reconcile with displayed frontier/plotted/catalog counts.")
        policy = doc.get("nearFrontierPolicy")
        if (isinstance(policy, dict) and number(policy.get("maxIntelligenceGap")) and policy["maxIntelligenceGap"] > 0
                and all(isinstance(policy.get(key), str) and policy[key].strip() for key in ("basis", "text"))):
            max_gap = policy["maxIntelligenceGap"]
            report["nearFrontierPolicy"] = policy
        else:
            issues.append("Observed frontier requires nearFrontierPolicy with a positive maxIntelligenceGap and nonempty basis and text.")
        near_rows_ok = isinstance(doc.get("nearFrontierRows"), list)
        if near_rows_ok:
            near_rows = doc["nearFrontierRows"]
        else:
            issues.append("Observed frontier requires a nearFrontierRows array.")
        near_n = universe.get("nearFrontierPointN") if isinstance(universe, dict) else None
        if not isinstance(near_n, int) or isinstance(near_n, bool) or near_n < 0:
            issues.append("Observed frontier requires a non-negative integer sourceUniverse.nearFrontierPointN.")
        elif near_rows_ok and near_n != len(near_rows):
            issues.append(f"Near-frontier row count {len(near_rows)} does not match sourceUniverse.nearFrontierPointN {near_n}.")
    try:
        metrics = read_json(data / "aa_metrics.json")
        roster = list(metrics["models"].items())
        if doc.get("benchmarkVersion") != metrics.get("benchmarkVersion"):
            issues.append("Inventory benchmark version differs from aa_metrics.json; recapture or migrate the exact version before publishing.")
        scores = read_json(data / "scores.json")
        ranked = {item["id"] for item in scores["models"] if item.get("rankingEligible") is True}
        primary_gaps = {item["id"]: item.get("rankingExclusionReasons", []) for item in scores["models"]}
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
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
    seen = set()
    roster_ids = {model_id for model_id, _ in roster}

    def resolved(row, identity_variant):
        model_id = exact_roster_match(row, roster)
        deferred = decisions.get(identity_variant) if model_id is None else None
        return {**row, "valueRankModelId": model_id,
                "intelligenceIndexPrecision": row.get("intelligenceIndexPrecision") or doc.get("intelligenceIndexPrecision"),
                "rosterDecision": deferred,
                "primaryRankingGaps": primary_gaps.get(model_id, ["Exact evaluated variant absent from source roster"]),
                "metricGap": "Numeric intelligence/cost values not fully available in the public chart capture"
                if not number(row.get("intelligenceIndex")) or not number(row.get("totalCostUsd")) else None,
                "rankStatus": "Primary ranked" if model_id in ranked else "Unranked source candidate" if model_id else "Deferred comparison candidate" if deferred else "Missing from source roster"}

    valid = []
    for index, row in enumerate(rows):
        identity_variant = check_row_identity(row, index, False, seen, issues)
        if identity_variant is None:
            continue
        identity = row["aaId"]
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
        valid.append(resolved(row, identity_variant))
    frontier = valid if observed_frontier else [row for row in valid if not any(
        other["intelligenceIndex"] >= row["intelligenceIndex"] and other["totalCostUsd"] <= row["totalCostUsd"]
        and (other["intelligenceIndex"] > row["intelligenceIndex"] or other["totalCostUsd"] < row["totalCostUsd"])
        for other in valid)]
    report["frontier"] = sorted(frontier, key=lambda row: (row.get("totalCostUsd") if number(row.get("totalCostUsd")) else math.inf, row["aaId"], row["name"]))
    # Near-frontier rows are plotted configurations within the policy gap of the rendered frontier.
    frontier_aa_ids = {row["aaId"] for row in report["frontier"]}
    gap_limit = math.inf if max_gap is None else max_gap
    gap_text = "the policy maximum" if max_gap is None else f"{max_gap:g}"
    near_valid = []
    for index, row in enumerate(near_rows):
        identity_variant = check_row_identity(row, index, True, seen, issues)
        if identity_variant is None:
            continue
        name = row["name"]
        if row.get("directlyObservedFrontier") is not False:
            issues.append(f"{name}: near-frontier rows must not claim direct frontier observation.")
            continue
        intelligence, cost, gap, ratio = (row.get(key) for key in ("intelligenceIndex", "totalCostUsd", "intelligenceGap", "costRatio"))
        if not number(intelligence) or not number(cost) or cost < 0:
            issues.append(f"{name}: near-frontier intelligenceIndex and totalCostUsd must be numeric.")
            continue
        if not number(gap) or not 0 <= gap <= gap_limit:
            issues.append(f"{name}: intelligenceGap must be a number between 0 and {gap_text}.")
            continue
        if ratio is not None and (not number(ratio) or ratio < 0):
            issues.append(f"{name}: costRatio must be null or a nonnegative number.")
            continue
        if not isinstance(row.get("nearestFrontierAaId"), str) or row["nearestFrontierAaId"] not in frontier_aa_ids:
            issues.append(f"{name}: nearestFrontierAaId must name a frontier row.")
            continue
        near_valid.append(resolved(row, identity_variant))
    report["nearFrontier"] = sorted(near_valid, key=lambda row: (row["totalCostUsd"], row["aaId"], row["name"]))
    near_groups = {}
    for row in report["nearFrontier"]:
        family, required_id = row.get("family"), row.get("requiredFamilyModelId")
        if not isinstance(family, str) or not family:
            issues.append(f"{row['name']}: near-frontier family is required.")
            continue
        if "requiredFamilyModelId" not in row or (required_id is not None and (not isinstance(required_id, str) or not required_id)):
            issues.append(f"{row['name']}: near-frontier requiredFamilyModelId must be a model ID string or null.")
            continue
        group = near_groups.setdefault(family, {"modelIds": set(), "rows": []})
        group["modelIds"].add(required_id)
        group["rows"].append(row)
    for family, group in near_groups.items():
        if len(group["modelIds"]) != 1:
            issues.append(f"Near-frontier AA family {family}: conflicting requiredFamilyModelId values.")
            continue
        required_id = next(iter(group["modelIds"]))
        in_roster, primary_ranked = required_id in roster_ids, required_id in ranked
        report["nearFrontierFamilies"].append({"family": family, "modelId": required_id, "configurationN": len(group["rows"]),
                                               "inRoster": in_roster, "primaryRanked": primary_ranked, "deferred": required_id is None})
        if required_id is not None and not (in_roster and primary_ranked):
            issues.append(f"Near-frontier AA family {family} ({required_id}) must appear in the primary ranking using its selected roster configuration; the near configuration itself need not be selected.")
        undecided = [row["name"] for row in group["rows"] if required_id is None and not row["rosterDecision"]]
        if undecided:
            issues.append(f"Near-frontier AA family {family} is deferred without a dated roster decision for: " + ", ".join(undecided) + ".")
    near_label = lambda row: row["aaId"] + " :: " + row["name"]
    report["missingNearFrontierIds"] = [near_label(row) for row in report["nearFrontier"] if not row["valueRankModelId"]]
    report["unresolvedNearFrontierIds"] = [near_label(row) for row in report["nearFrontier"] if not row["valueRankModelId"] and not row["rosterDecision"]]
    report["deferredNearFrontierIds"] = [near_label(row) for row in report["nearFrontier"] if row["rosterDecision"]]
    # Alternate effort decisions cannot waive a model family's required inclusion.
    families = {}
    for row in report["frontier"]:
        family, required_id = row.get("family"), row.get("requiredFamilyModelId")
        if not isinstance(family, str) or not family or not isinstance(required_id, str) or not required_id:
            issues.append(f"{row['name']}: frontier family and requiredFamilyModelId are required.")
            continue
        group = families.setdefault(family, {"modelIds": set(), "rows": []})
        group["modelIds"].add(required_id)
        group["rows"].append(row)
    report["requiredFamilies"] = []
    for family, group in families.items():
        if len(group["modelIds"]) != 1:
            issues.append(f"{family}: conflicting required family model IDs.")
            continue
        required_id = next(iter(group["modelIds"]))
        matches = [row for row in group["rows"] if row.get("valueRankModelId") == required_id]
        included = len(matches) == 1 and required_id in ranked
        report["requiredFamilies"].append({"family": family, "modelId": required_id,
                                          "selectedFrontierConfigurationN": len(matches),
                                          "primaryRanked": included})
        if not included:
            issues.append(f"Required AA frontier family {family} ({required_id}) must resolve to one exact selected frontier configuration and appear in the primary ranking.")
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


def near_gap_label(policy):
    """Render the policy's maximum Index-point gap, e.g. ``3`` or ``2.5``."""
    gap = policy.get("maxIntelligenceGap") if isinstance(policy, dict) else None
    return f"{gap:g}" if number(gap) else "unknown"


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
        required = report.get("requiredFamilies", [])
        summary += f" All {len(required)} distinct frontier model families are required in the main ranking using exact selected configurations; {sum(item.get('primaryRanked') is True for item in required)} are included. Other effort configurations remain separate comparison entries."
        policy = report.get("nearFrontierPolicy") if isinstance(report.get("nearFrontierPolicy"), dict) else {}
        near_families = report.get("nearFrontierFamilies", [])
        summary += (f" {len(report.get('nearFrontier', []))} plotted configurations from {len(near_families)} families lie within "
                    f"{near_gap_label(policy)} Index points of the rendered frontier; "
                    f"{sum(item.get('primaryRanked') is True for item in near_families)} of those families are in the main ranking, "
                    f"{sum(item.get('deferred') is True for item in near_families)} are deferred.")
    near = report.get("nearFrontier", [])
    selected = {variant_key(row): row for row in report["frontier"] + near + report["comparisonCandidates"]}
    frontier_ids = {variant_key(row) for row in report["frontier"]}
    near_ids = {variant_key(row) for row in near}
    near_flag = f"Near AA frontier (within {near_gap_label(report.get('nearFrontierPolicy'))} Index points)"
    md_rows, html_rows = [], []
    for row in selected.values():
        flag = ("Observed AA frontier" if variant_key(row) in frontier_ids
                else near_flag if variant_key(row) in near_ids else "Comparison candidate")
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
