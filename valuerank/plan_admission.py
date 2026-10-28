"""Owner decision O81 (2026-10-26): the build decides O71 plan admission from the report table.

Every user report the O71 research found is a row of ``data/plan_reports.json``. This module applies the report
eligibility profile E270 (held in ``plan_cost_routes.json`` ``evidencePolicy.reportEligibilityProfile``) and O11's
concordance test to every model × plan cell, and the build refuses a report route the result does not support:

- a report counts only with a meter fraction (no lower bounds), one model, an observer (not an aggregator), a stated
  model (a challenged report is excluded), measured at least partly inside the report window, clear of a
  provider-acknowledged accounting-fault day, and inside one partition (a report spanning a split is excluded);
- a speed-mode value is converted at the provider's published multiplier and flagged (O76);
- a partition splits at each recorded change (E18 or provider-documented, O83); the partition current at the cutoff decides;
- the cell passes when it has at least two non-provisional reports, every report's whole range lies within 1.20× of the
  smallest lower bound (E98, E107: every eligible report together), the unit converts to a month (O82: a 5-hour figure
  never does), and the plan is one ValueRank lists; the value is the geometric mean of the firm reports' midpoints.
"""

from __future__ import annotations

import math
from datetime import date, datetime, time, timedelta, timezone

CONCORDANCE = 1.20  # O11 / E98
WEEKS_PER_MONTH = 4.33  # E270
UNIT_TO_MONTH = {"month": 1.0, "week": WEEKS_PER_MONTH}  # O82: a 5-hour figure never converts and never admits a route


def _start(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")) if "T" in stamp else datetime.combine(date.fromisoformat(stamp), time.min, timezone.utc)


def _end(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")) if "T" in stamp else datetime.combine(date.fromisoformat(stamp), time.max, timezone.utc)


def window(report: dict) -> tuple[datetime, datetime]:
    start = report.get("windowStart") or report["windowEnd"]
    return _start(start), _end(report["windowEnd"])


def split_span(split: dict) -> tuple[datetime, datetime]:
    """A split given as an instant is a point; a split given as a date covers that whole day (its hour is unknown)."""

    return _start(split["date"]), _end(split["date"])


def applies(entry: dict, report: dict) -> bool:
    return entry["provider"] == report["provider"] and (not entry.get("plans") or report["plan"] in entry["plans"])


def partition(report: dict, splits: list[dict]) -> int | None:
    """The index of the report's partition (how many of its provider's splits precede it), or None when it spans one."""

    start, end = window(report)
    index = 0
    for split in sorted((item for item in splits if applies(item, report)), key=lambda item: split_span(item)[0]):
        low, high = split_span(split)
        instant = "T" in split["date"]
        if end < low or (instant and end <= low):
            break
        if start > high or (instant and start >= high):
            index += 1
            continue
        return None
    return index


def on_fault_day(report: dict, faults: list[dict]) -> bool:
    start, end = window(report)
    for fault in faults:
        if not applies(fault, report):
            continue
        for day in fault["days"]:
            first, _, last = day.partition("..")
            if start <= _end(last or first) and end >= _start(first):
                return True
    return False


def converted(report: dict, multipliers: dict) -> tuple[float, float]:
    factor = multipliers.get(report["provider"], {}).get(report["speedMode"], 1.0) if report.get("speedMode") else 1.0
    return report["valueLower"] * factor, report["valueUpper"] * factor


def exclusion(report: dict, profile: dict, release_day: date) -> str | None:
    """Why a report does not count (E270), or None."""

    if report.get("lowerBound"):
        return "lower bound: no meter fraction"
    if report.get("mixedModel"):
        return "mixed-model usage"
    if report.get("aggregator"):
        return "aggregator or derived figure (cross-check only)"
    if report.get("modelUnstated") or not report.get("modelId"):
        return "model not stated"
    if report.get("tierUnstated"):
        return "tier not stated"
    if report.get("derived"):
        return "the research's own arithmetic, not a figure the observer reported"
    if report.get("anomaly"):
        return "an anomaly or legacy-account report"
    if report.get("challenged"):
        return "challenged: does not reproduce from its own figures"
    start, end = window(report)
    if end.date() < release_day - timedelta(days=30) or start.date() > release_day:
        return "measured outside the report window"
    if on_fault_day(report, profile.get("accountingFaultDays", [])):
        return "measured on a provider-acknowledged accounting-fault day"
    if partition(report, profile.get("partitionSplits", [])) is None:
        return "spans a partition split"
    return None


def cell_key(report: dict) -> tuple:
    return report["provider"], report["plan"], report["modelId"], report["unit"], report.get("region", "global")


def evaluate(document: dict, profile: dict, release_day: date) -> list[dict]:
    """Every model × plan × unit cell's admission, with each report's role (E270, O11, O81, O82)."""

    multipliers, splits = document.get("speedModeMultipliers", {}), profile.get("partitionSplits", [])
    cells: dict[tuple, list[dict]] = {}
    for report in document["reports"]:
        cells.setdefault(cell_key(report), []).append(report)
    results = []
    for key, reports in sorted(cells.items(), key=lambda item: tuple(str(part) for part in item[0])):
        provider, plan, model, unit, region = key
        rows, eligible = [], []
        for report in reports:
            reason = exclusion(report, profile, release_day)
            low, high = converted(report, multipliers)
            part = partition(report, splits) if reason is None else None
            rows.append({"id": report["id"], "observer": report["observer"], "valueLower": low, "valueUpper": high, "partition": part,
                         "provisional": bool(report.get("provisional")), "speedMode": report.get("speedMode"), "excluded": reason})
            if reason is None:
                eligible.append(rows[-1])
        latest_split = sum(applies(item, reports[0]) for item in splits)
        pool = [row for row in eligible if row["partition"] == latest_split]
        observers = [row["observer"] for row in pool]
        lowest = min((row["valueLower"] for row in pool), default=None)
        highest = max((row["valueUpper"] for row in pool), default=None)
        firm = [row for row in pool if not row["provisional"]]
        if plan not in document.get("listedPlans", {}) or region != "global":
            status = "not a listed plan"
        elif unit not in UNIT_TO_MONTH:
            status = "fails: a 5-hour figure never converts to a billing period (O82)"
        elif len(set(observers)) < len(observers):
            raise ValueError(f"{key}: one observer reports twice in one partition; record it once with its range (E270)")
        elif len(firm) < 2:
            status = f"fails: {len(firm)} non-provisional report(s) in the current partition"
        elif highest > CONCORDANCE * lowest:
            status = f"fails: range {highest / lowest:.2f}× over the current partition"
        else:
            status = "passes"
        # I64 L3: the split comes first, then the range test over every eligible report of the current partition (provisional
        # ones included); the value is the geometric mean of the non-provisional reports' midpoints, the E33 pool the
        # route's own multiple uses (I65 L3).
        value = (math.exp(sum(math.log((row["valueLower"] + row["valueUpper"]) / 2) for row in firm) / len(firm))
                 if status == "passes" else None)
        monthly = value * UNIT_TO_MONTH[unit] if value is not None else None
        fee = document.get("listedPlans", {}).get(plan)
        results.append({"provider": provider, "plan": plan, "modelId": model, "unit": unit, "region": region, "status": status,
                        "currentPartition": latest_split, "partitionsWithReports": sorted({row["partition"] for row in eligible}),
                        "value": value, "monthlyUsd": monthly, "multiple": monthly / fee if monthly is not None and fee else None,
                        "range": None if lowest is None else [lowest, highest], "reports": rows,
                        "admittingObservers": sorted(row["observer"] for row in firm) if status == "passes" else []})
    return results


def check_routes(routes: list[dict], cells: list[dict], cohort: set[str], report_kinds: set[str]) -> None:
    """O81, I65 L3: a report-based route for a cohort model must rest on a passing cell for its plan and model, and its
    pooled reports must be that cell's admitting reports (the same observers), so the two paths cannot disagree."""

    passing: dict[tuple, list[dict]] = {}
    for cell in cells:
        if cell["status"] == "passes":
            passing.setdefault((cell["plan"], cell["modelId"]), []).append(cell)
    for route in routes:
        if route.get("valueMultipleKind") not in report_kinds:
            continue
        for model in set(route.get("modelIds") or []) & cohort:
            supporting = passing.get((route.get("plan"), model), [])
            if not supporting:
                raise ValueError(f"{route['id']}: no passing O71 cell supports a report route for {model} on {route.get('plan')} (O81)")
            # I66 L2: a plan and model can pass in more than one unit; the route's observers must be one cell's admitting set.
            observers = sorted(str(report.get("observer") or "") for report in route.get("independentReports") or [])
            if all(observers != cell["admittingObservers"] for cell in supporting):
                raise ValueError(f"{route['id']}: its reports ({', '.join(observers)}) are not a passing cell's admitting reports "
                                 f"({'; '.join(', '.join(cell['admittingObservers']) for cell in supporting)}) (O81)")
