"""Owner decision O81 (2026-10-26): the build decides O71 plan admission from the report table.

Every user report the O71 research found is a row of ``data/plan_reports.json``. This module applies the report
eligibility profile E270 (held in ``plan_cost_routes.json`` ``evidencePolicy.reportEligibilityProfile``) and O11's
concordance test to every model × plan cell, and the build refuses a report route the result does not support:

- a report counts only with a meter fraction (no lower bounds), one model, an observer (not an aggregator), a stated
  model (a challenged report is excluded), measured at least partly inside the report window, clear of a
  provider-acknowledged accounting-fault day, and inside one partition (a report spanning a split is excluded);
- a speed-mode value is converted at the provider's published multiplier and flagged (O76);
- a partition splits at each recorded change (E18 or provider-documented, O83) to the plan's limits or price (O99: a record
  typed "metering", which changes neither, is logged and does not split); the partition current at the cutoff decides;
- the cell passes when it has at least two non-provisional reports, the largest lower bound is at most 1.20× the smallest
  upper bound (O86; E98, E107: every eligible report together),
  reports at any effort pool for the model (O87), the unit converts to a month (O82: a 5-hour figure
  never does), and every cell is tested (O85: a cell on a plan the Plan ranking does not list is published as evidence
  only and supports no route); the value is the geometric mean of the firm reports' midpoints.
"""

from __future__ import annotations

import math
from datetime import date, datetime, time, timedelta, timezone

CONCORDANCE = 1.20  # O11 / E98
WEEKS_PER_MONTH = 4.33  # E270
UNIT_TO_MONTH = {"month": 1.0, "week": WEEKS_PER_MONTH}


def model_of(configuration_id: str | None, families: dict | None = None) -> str | None:
    """O87, I69 L2: a plan allowance is effort-invariant, so a cell is keyed by the model (the configuration's AA family,
    for example "GPT-6 Astra" for both its max and high rows), never by parsing the ID; an unknown ID keys itself."""

    return (families or {}).get(configuration_id, configuration_id)


def _start(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")) if "T" in stamp else datetime.combine(date.fromisoformat(stamp), time.min, timezone.utc)


def _end(stamp: str) -> datetime:
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")) if "T" in stamp else datetime.combine(date.fromisoformat(stamp), time.max, timezone.utc)


METER_DAYS = {"week": 7, "month": 30}  # I79 L2: the period a meter reading of each unit covers


def window(report: dict) -> tuple[datetime, datetime]:
    """The report's measurement window; an unstated window is the meter's own period ending on the report date (a weekly
    reading covers 7 days, a monthly one 30, a 5-hour one its day), so a reading never counts wholly after a split it spans."""

    if report.get("windowStart"):
        return _start(report["windowStart"]), _end(report["windowEnd"])
    end = _end(report["windowEnd"])
    days = METER_DAYS.get(report.get("unit"), 1)
    return _start(report["windowEnd"]) - timedelta(days=days - 1), end


def split_span(split: dict) -> tuple[datetime, datetime]:
    """A split given as an instant is a point; a split given as a date covers that whole day (its hour is unknown)."""

    return _start(split["date"]), _end(split["date"])


# O99 (2026-10-28): only a change to a plan's limits or price splits the report partition; a metering-only announcement is
# logged. Every record is typed, and the build refuses an untyped or unknown one.
SPLIT_TYPES = {"limit", "price"}
# O105 (2026-10-28): a documented change to which models a plan offers flags the plan's routes but splits nothing, as the
# allowance itself did not change.
FLAG_ONLY_TYPES = {"availability"}
# O111 (2026-10-29): a bundled credit grant (e.g. API credits added to a plan) flags and blocks like a limit change but
# leaves the meter-reading partitions whole, as the meter users read did not change.
CREDIT_TYPES = {"credit"}
BLOCKING_TYPES = SPLIT_TYPES | CREDIT_TYPES
FLAGGING_TYPES = BLOCKING_TYPES | FLAG_ONLY_TYPES
LOGGED_TYPES = {"metering"}


def splitting(records: list[dict]) -> list[dict]:
    """O83, O99: the recorded changes that split the report partition."""

    for record in records:
        if record.get("type") not in FLAGGING_TYPES | LOGGED_TYPES:
            raise ValueError(f"partition record {record.get('provider')} {record.get('date')} needs a type: one of {sorted(FLAGGING_TYPES | LOGGED_TYPES)} (O99, O105, O111)")
    return [record for record in records if record["type"] in SPLIT_TYPES]


def check_change_flags(routes: list[dict], records: list[dict]) -> None:
    """O77 as amended by O101, I84 L2, O105: a route's detected-change flag rests on a typed limit, price or model-availability
    change record for its provider and plan on that date; a flag no such record supports stops the build."""

    splitting(records)
    supporting = [record for record in records if record["type"] in FLAGGING_TYPES]
    for route in routes:
        changed = route.get("changeDetectedOn")
        if changed and not any(item["date"][:10] == changed and applies(item, route) for item in supporting):
            raise ValueError(f"route {route['id']}: change flag {changed} has no typed limit, price, credit or availability change record for its provider and plan (O101, O105, O111)")


def check_change_records(routes: list[dict], records: list[dict], release_day: date) -> None:
    """I86 L3, O107, I87 M1 and L1: the typed records produce every route's two change dates. A controlled measurement on a
    plan a record covers carries ``changeDetectedOn``, the earliest limit, price or availability record dated on or after the
    earliest day it can have been taken and by the cutoff (the label); every flagged route (an O46 ceiling or a report route
    flagged by hand included) carries ``blockingChangeOn`` exactly when the earliest limit or price record from its label
    date on differs from the label date (null when none: an availability-only flag blocks nothing). The build stops
    otherwise."""

    from valuerank import plan_routes  # local: plan_routes does not depend on this module

    splitting(records)
    dated = [(date.fromisoformat(record["date"][:10]), record) for record in records if record["type"] in FLAGGING_TYPES]
    for route in routes:
        applicable = sorted((day, record["type"]) for day, record in dated if applies(record, route) and day <= release_day)
        if route.get("valueMultipleKind") in plan_routes.CONTROLLED_KINDS:
            earliest = plan_routes.change_floor(route)
            derived = next((day for day, _ in applicable if earliest is None or day >= earliest), None)
            if (derived.isoformat() if derived else None) != route.get("changeDetectedOn"):
                raise ValueError(f"route {route['id']}: its change flag must be {derived} from the typed change records (I86 L3)")
        label = route.get("changeDetectedOn")
        if label is None:
            if "blockingChangeOn" in route:
                raise ValueError(f"route {route['id']}: blockingChangeOn without a change flag (I87 M1)")
            continue
        blocking = next((day.isoformat() for day, kind in applicable if kind in BLOCKING_TYPES and day.isoformat() >= label), None)
        if blocking == label:
            if "blockingChangeOn" in route:
                raise ValueError(f"route {route['id']}: blockingChangeOn must be omitted when it equals the change flag (I87 M1)")
        elif route.get("blockingChangeOn", "absent") != blocking:
            raise ValueError(f"route {route['id']}: blockingChangeOn must be {blocking} from the typed change records (O107, I87 M1)")


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
    # I86 M1: only the records that split (O99, O105) can exclude a report as spanning a split.
    if partition(report, splitting(profile.get("partitionSplits", []))) is None:
        return "spans a partition split"
    return None


def cell_key(report: dict, families: dict | None = None) -> tuple:
    return report["provider"], report["plan"], model_of(report["modelId"], families), report["unit"], report.get("region", "global")


def evaluate(document: dict, profile: dict, release_day: date, families: dict | None = None) -> list[dict]:
    """Every model × plan × unit cell's admission, with each report's role (E270, O11, O81, O82)."""

    multipliers, splits = document.get("speedModeMultipliers", {}), splitting(profile.get("partitionSplits", []))
    cells: dict[tuple, list[dict]] = {}
    for report in document["reports"]:
        cells.setdefault(cell_key(report, families), []).append(report)
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
        # O86: the reports concord when the largest lower bound is at most 1.20x the smallest upper bound, so a coarse meter
        # reading is not mistaken for disagreement.
        largest_lower = max((row["valueLower"] for row in pool), default=None)
        smallest_upper = min((row["valueUpper"] for row in pool), default=None)
        firm = [row for row in pool if not row["provisional"]]
        # O85: every cell is tested; a cell on a plan the Plan ranking does not list is published as evidence only.
        listed = plan in document.get("listedPlans", {}) and region == "global"
        if unit not in UNIT_TO_MONTH:
            status = "fails: a 5-hour figure never converts to a billing period (O82)"
        elif len(set(observers)) < len(observers):
            raise ValueError(f"{key}: one observer reports twice in one partition; record it once with its range (E270)")
        elif len(firm) < 2:
            status = f"fails: {len(firm)} non-provisional report(s) in the current partition"
        elif largest_lower > CONCORDANCE * smallest_upper:
            status = f"fails: largest lower bound {largest_lower / smallest_upper:.2f}× the smallest upper bound (O86 allows 1.20×) in the current partition"
        else:
            status = "passes"
        # I64 L3: the split comes first, then the range test over every eligible report of the current partition (provisional
        # ones included); the value is the geometric mean of the non-provisional reports' midpoints, the E33 pool the
        # route's own multiple uses (I65 L3).
        value = (math.exp(sum(math.log((row["valueLower"] + row["valueUpper"]) / 2) for row in firm) / len(firm))
                 if status == "passes" else None)
        monthly = value * UNIT_TO_MONTH[unit] if value is not None else None
        fee = document.get("listedPlans", {}).get(plan) if listed else None
        results.append({"provider": provider, "plan": plan, "modelId": model, "unit": unit, "region": region, "status": status, "listed": listed,
                        "currentPartition": latest_split, "partitionsWithReports": sorted({row["partition"] for row in eligible}),
                        "configurations": sorted({str(report["modelId"]) for report in reports}), "efforts": sorted({str(report.get("effort") or "unstated") for report in reports}), "value": value, "monthlyUsd": monthly, "multiple": monthly / fee if monthly is not None and fee else None,
                        "range": None if lowest is None else [lowest, highest], "reports": rows,
                        "admittingObservers": sorted(row["observer"] for row in firm) if status == "passes" else []})
    return results


def check_routes(routes: list[dict], cells: list[dict], cohort: set[str], report_kinds: set[str], families: dict | None = None) -> None:
    """O81, I65 L3: a report-based route for a cohort model must rest on a passing cell for its plan and model, and its
    pooled reports must be that cell's admitting reports (the same observers), so the two paths cannot disagree."""

    passing: dict[tuple, list[dict]] = {}
    for cell in cells:
        if cell["status"] == "passes" and cell.get("listed", True):
            passing.setdefault((cell["plan"], cell["modelId"]), []).append(cell)
    for route in routes:
        if route.get("valueMultipleKind") not in report_kinds:
            continue
        for model in set(route.get("modelIds") or []) & cohort:
            supporting = passing.get((route.get("plan"), model_of(model, families)), [])
            if not supporting:
                raise ValueError(f"{route['id']}: no passing O71 cell supports a report route for {model} on {route.get('plan')} (O81)")
            # I66 L2: a plan and model can pass in more than one unit; the route's observers must be one cell's admitting set.
            observers = sorted(str(report.get("observer") or "") for report in route.get("independentReports") or [])
            if all(observers != cell["admittingObservers"] for cell in supporting):
                raise ValueError(f"{route['id']}: its reports ({', '.join(observers)}) are not a passing cell's admitting reports "
                                 f"({'; '.join(', '.join(cell['admittingObservers']) for cell in supporting)}) (O81)")
