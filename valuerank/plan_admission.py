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

import hashlib
import math
from datetime import date, datetime, time, timedelta, timezone

CONCORDANCE = 1.20  # O11 / E98
WEEKS_PER_MONTH = 52 / 12  # E270: 52 weeks over 12 months, exact (reviewer 77; was the rounded 4.33)
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
# O112 (2026-10-29): a provider's global meter reset flags nothing and splits nothing. O156 (2026-11-01, superseding O112's
# exclusion and O131): a documented periodic reset is part of the regime every user of the plan experiences, so a reading
# spanning registered reset records counts (O11, O85 and O86 as usual) and its cell and route carry ACROSS_RESETS_FLAG.
RESET_TYPES = {"reset"}
ACROSS_RESETS_FLAG = "measured across documented meter resets (O156)"


def splitting(records: list[dict]) -> list[dict]:
    """O83, O99: the recorded changes that split the report partition."""

    for record in records:
        if record.get("type") not in FLAGGING_TYPES | LOGGED_TYPES | RESET_TYPES:
            raise ValueError(f"partition record {record.get('provider')} {record.get('date')} needs a type: one of {sorted(FLAGGING_TYPES | LOGGED_TYPES | RESET_TYPES)} (O99, O105, O111, O112)")
    return [record for record in records if record["type"] in SPLIT_TYPES]


def profile_records(profile: dict) -> list[dict]:
    """O113 (2026-10-29): the profile's typed change records, each record naming a meter family (``meterFamily``) applying
    to every plan on that meter (``meterFamilies``), listed, tier-unstated and redacted plans alike; the build stops on an
    unknown family."""

    families = profile.get("meterFamilies") or {}
    records = []
    for record in profile.get("partitionSplits", []):
        family = record.get("meterFamily")
        if family is not None:
            if family not in families:
                raise ValueError(f"change record {record.get('provider')} {record.get('date')} names an unknown meter family {family!r} (O113)")
            record = {**record, "plans": list(families[family])}
        records.append(record)
    return records


def canonical_plans(document: dict, aliases: dict | None) -> dict:
    """E244 (reviewer 75): a report filed under a provider's renamed plan (evidencePolicy.planAliases, e.g. Anthropic's
    "Claude Ultra" for Max 20x from 2026-10-30) counts under the plan's canonical key, never as an unlisted plan (O85)."""

    names = {alias["name"]: plan for plan, alias in (aliases or {}).items()}
    if not names:
        return document
    reports = [{**report, "plan": names[report["plan"]], "planAsFiled": report["plan"]} if report.get("plan") in names else report
               for report in document.get("reports", [])]
    return {**document, "reports": reports}


def spans_reset(report: dict, records: list[dict]) -> bool:
    """O112, O156: whether a reading's window touches a registered day on which its provider reset every meter."""

    start, end = window(report)
    return any(record.get("type") in RESET_TYPES and applies(record, report)
               and start <= _end(record["date"][:10]) and end >= _start(record["date"][:10]) for record in records)


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


# O177 (2026-11-03, on reviewer 96, amending the outright exclusion of split-spanning reports): a report that states its
# readings per period ("periods": windowStart, windowEnd, valueLower, valueUpper each) and spans a split counts only through
# its periods in the latest partition they reach, each wholly on one side of every split; they enter as one range for the
# observer (E270) and the report is flagged. A report without isolable periods stays excluded; nothing pools across a split.
ACROSS_SPLIT_FLAG = "measured across a split: only its readings wholly after the split count (O177)"


def isolate_periods(report: dict, splits: list[dict]) -> dict | None:
    """O177: the report reduced to its isolable periods in the latest partition they reach, or None."""

    periods = report.get("periods") or []
    if not periods or partition(report, splits) is not None:
        return None
    placed = [(partition({**report, "windowStart": item["windowStart"], "windowEnd": item["windowEnd"]}, splits), item) for item in periods]
    indices = [index for index, _ in placed if index is not None]
    if not indices:
        return None
    kept = [item for index, item in placed if index == max(indices)]
    return {**report, "windowStart": min(item["windowStart"] for item in kept), "windowEnd": max(item["windowEnd"] for item in kept),
            "valueLower": min(item["valueLower"] for item in kept), "valueUpper": max(item["valueUpper"] for item in kept), "acrossSplit": True}


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


def test_bounds(report: dict, multipliers: dict) -> tuple[float, float]:
    """O192 (2026-11-05, on reviewer 123, amending O174): the bounds the O86 test reads for an observer. Without recorded readings
    they are the report's range; with several readings they are the tightest (the largest lower bound and the smallest upper
    bound over the readings, which may cross), so an observer's spread cannot create agreement its readings never had."""

    low, high = converted(report, multipliers)
    readings = report.get("readings") or []
    if len(readings) < 2:
        return low, high
    scale = low / report["valueLower"] if report["valueLower"] else 1.0
    return max(lower for lower, _ in readings) * scale, min(upper for _, upper in readings) * scale


FORM_STAGE = "form"  # E244: a report submitted through the GitHub intake form, not found by the staged O71 search


# O165 (2026-11-01): from the release after the 2026-11-01 cutoff, a report the staged search found counts only with an archived
# copy of its page (URL or mirror URL, fetch instant, SHA-256 of the fetched bytes, the quoted allowance span) in the evidence
# bundle, as O124 already asks of form submissions. O168 (2026-11-01, on reviewer 90): only the report records present at the
# 2026-11-01 release are grandfathered, frozen by id in plan_reports.json `o165Grandfathered` (hash-checked); a report first
# added later needs a copy whatever its date.
ARCHIVE_FROM = date(2026, 11, 1)
NOT_ARCHIVED = "not archived: recorded before O165 without a hashed copy"


def archived(report: dict) -> bool:
    return bool((report.get("archive") or {}).get("sha256"))


def grandfathered_ids(document: dict) -> frozenset:
    """O168: the frozen id list of report records grandfathered by O165, checked against its recorded hash."""

    record = document.get("o165Grandfathered")
    if not record:
        return frozenset()
    ids = sorted(record["ids"])
    if hashlib.sha256("\n".join(ids).encode()).hexdigest() != record["sha256"]:
        raise ValueError("the O165 grandfathered report list does not match its recorded hash (O168)")
    return frozenset(ids)


READINGS_DISAGREE = "the observer's own readings disagree beyond the O86 tolerance (O189)"


def exclusion(report: dict, profile: dict, release_day: date, grandfathered: frozenset = frozenset()) -> str | None:
    """Why a report does not count (E270), or None."""

    if report.get("stage") != FORM_STAGE and not archived(report) and release_day > ARCHIVE_FROM and report["id"] not in grandfathered:
        return "staged-search report without an archived hashed copy, first recorded after the 2026-11-01 release (O165, O168)"

    # O124 (2026-10-30): a report submitted through the intake form counts only with an evidence artifact (a meter screenshot
    # or usage-ledger excerpt) hashed into the evidence bundle.
    if report.get("stage") == FORM_STAGE and not report.get("evidenceArtifactSha256"):
        return "form submission without an evidence artifact (O124)"
    # E336 (reviewer 93): the O86 concordance ratio divides by the smallest upper bound, so a report with a non-positive
    # figure is excluded before any test reads it.
    if report["valueUpper"] <= 0 or report["valueLower"] < 0:
        return "non-positive allowance figure: no concordance test can read it (E336)"
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
    # O189 (2026-11-05, on reviewer 111, amending O174): an observer's several readings in one partition stand in for the observer
    # as their enclosing range only when they concord with one another (O86's 1.20x test over the observer's own readings), so
    # an observer whose readings disagree cannot manufacture agreement with another observer.
    readings = report.get("readings") or []
    if len(readings) >= 2 and max(low for low, _ in readings) > CONCORDANCE * min(high for _, high in readings):
        return READINGS_DISAGREE
    start, end = window(report)
    if end.date() < release_day - timedelta(days=30) or start.date() > release_day:
        return "measured outside the report window"
    if on_fault_day(report, profile.get("accountingFaultDays", [])):
        return "measured on a provider-acknowledged accounting-fault day"
    records = profile_records(profile)
    # I86 M1: only the records that split (O99, O105) can exclude a report as spanning a split.
    if partition(report, splitting(records)) is None:
        return "spans a partition split"
    return None


EMPTY_WINDOW = "empty: the cell's latest staged search predates the report envelope, so it admits no new report (E320)"


def new_report_window(release_day: date, searched: str | None) -> dict:
    """E308, E320 (reviewer 86): a cell's new-report window is the release envelope [V − 30 days, V] ended at its latest staged
    search; under O167's 31-day monthly clock that search can predate the envelope, and the window is then empty, published
    as such, never as an inverted date range. A freshness check never moves it."""

    start = release_day - timedelta(days=30)
    end = date.fromisoformat(searched) if searched else release_day
    end = min(end, release_day)
    if end < start:
        return {"start": start.isoformat(), "end": None, "status": EMPTY_WINDOW}
    return {"start": start.isoformat(), "end": end.isoformat(), "status": "nonempty"}


def cell_key(report: dict, families: dict | None = None) -> tuple:
    return report["provider"], report["plan"], model_of(report["modelId"], families), report["unit"], report.get("region", "global")


def evaluate(document: dict, profile: dict, release_day: date, families: dict | None = None, search_dates: dict | None = None) -> list[dict]:
    """Every model × plan × unit cell's admission, with each report's role (E270, O11, O81, O82)."""

    records = profile_records(profile)
    grandfathered = grandfathered_ids(document)
    multipliers, splits = document.get("speedModeMultipliers", {}), splitting(records)
    cells: dict[tuple, list[dict]] = {}
    for report in document["reports"]:
        cells.setdefault(cell_key(report, families), []).append(report)
    results = []
    for key, reports in sorted(cells.items(), key=lambda item: tuple(str(part) for part in item[0])):
        provider, plan, model, unit, region = key
        rows, eligible, discordant = [], [], []
        for report in reports:
            report = isolate_periods(report, splits) or report
            reason = exclusion(report, profile, release_day, grandfathered)
            # O161: a cell's window ends at its latest staged search; a report dated after it was never searched for.
            searched = (search_dates or {}).get((model, plan))
            if reason is None and searched and window(report)[1].date() > date.fromisoformat(searched):
                reason = f"dated after the cell's latest staged search, {searched} (O161)"
            low, high = converted(report, multipliers)
            part = partition(report, splits) if reason is None else None
            # O191: an observer withheld for discordant readings is not pooled but still blocks its partition's admission.
            # E348 (reviewer 116): every observer O159 lets contest the range test blocks, a re-checked provisional one included.
            discordant_part = (partition(report, splits) if reason == READINGS_DISAGREE
                               and (not report.get("provisional") or report.get("inferenceRechecked")) else None)
            test_low, test_high = test_bounds(report, multipliers)
            rows.append({"id": report["id"], "observer": report["observer"], "valueLower": low, "valueUpper": high, "testLower": test_low, "testUpper": test_high, "partition": part,
                         "provisional": bool(report.get("provisional")), "speedMode": report.get("speedMode"), "stage": report.get("stage"), "excluded": reason,
                         "acrossResets": spans_reset(report, records), "acrossSplit": bool(report.get("acrossSplit")), "inferenceRechecked": report.get("inferenceRechecked"),
                         "archive": None if report.get("stage") == FORM_STAGE or archived(report) else NOT_ARCHIVED})
            if reason is None:
                eligible.append(rows[-1])
            elif discordant_part is not None:
                discordant.append({**rows[-1], "partition": discordant_part})
        latest_split = sum(applies(item, reports[0]) for item in splits)
        pool = [row for row in eligible if row["partition"] == latest_split]
        observers = [row["observer"] for row in pool]
        lowest = min((row["valueLower"] for row in pool), default=None)
        highest = max((row["valueUpper"] for row in pool), default=None)
        # O86: the reports concord when the largest lower bound is at most 1.20x the smallest upper bound, so a coarse meter
        # reading is not mistaken for disagreement. O159 (2026-11-01, amending O74/O81/O115): the test and the clip band read
        # the non-provisional reports, plus a provisional report whose inference has been re-checked against them (logged as
        # inferenceRechecked); the band over every report is published beside it.
        firm = [row for row in pool if not row["provisional"]]
        tested = [row for row in pool if not row["provisional"] or row["inferenceRechecked"]]
        largest_lower = max((row["testLower"] for row in tested), default=None)
        smallest_upper = min((row["testUpper"] for row in tested), default=None)
        all_lower = max((row["testLower"] for row in pool), default=None)
        all_upper = min((row["testUpper"] for row in pool), default=None)
        # O85: every cell is tested; a cell on a plan the Plan ranking does not list is published as evidence only.
        listed = plan in document.get("listedPlans", {}) and region == "global"
        if unit not in UNIT_TO_MONTH:
            status = "fails: a 5-hour figure never converts to a billing period (O82)"
        elif len(set(observers)) < len(observers):
            raise ValueError(f"{key}: one observer reports twice in one partition; record it once with its range (E270)")
        elif len(firm) < 2:
            status = f"fails: {len(firm)} non-provisional report(s) in the current partition"
        elif any(row["partition"] == latest_split for row in discordant):
            # O191 (2026-11-05, on reviewer 115, amending O189): withholding a discordant observer must never create a pass.
            status = "fails: an observer's own readings disagree, which blocks admission while it stays unresolved (O189, O191)"
        elif all(row["stage"] == FORM_STAGE for row in firm):
            # O124: an admitted pair needs at least one report the staged search found, so submissions alone never admit.
            status = "fails: every counting report was submitted through the intake form; one must be found by the staged search (O124)"
        elif largest_lower > CONCORDANCE * smallest_upper:
            status = f"fails: largest lower bound {largest_lower / smallest_upper:.2f}× the smallest upper bound (O86 allows 1.20×) in the current partition"
        else:
            status = "passes"
        # I64 L3: the split comes first, then the range test over every eligible report of the current partition (provisional
        # ones included); the value is the geometric mean of the non-provisional reports' midpoints, the E33 pool the
        # route's own multiple uses (I65 L3).
        # O115 (2026-10-29), E271: each midpoint is first clipped to the concordance band [largest lower bound / 1.20, 1.20x
        # the smallest upper bound], so a wide report cannot pull the pool beyond what the concordance test admitted, while
        # concordant point reports keep their own values (the symmetric band adds no upward pull); every report still counts.
        # O176 (2026-11-03, on reviewer 96, amending O159): the band that clips the value reads only the admitting
        # (non-provisional) reports, so a re-checked provisional report can fail a cell but never move its value.
        feasible = ([max(row["testLower"] for row in firm) / CONCORDANCE, CONCORDANCE * min(row["testUpper"] for row in firm)]
                    if status == "passes" else None)
        value = (math.exp(sum(math.log(min(max((row["valueLower"] + row["valueUpper"]) / 2, feasible[0]), feasible[1])) for row in firm) / len(firm))
                 if status == "passes" else None)
        monthly = value * UNIT_TO_MONTH[unit] if value is not None else None
        fee = document.get("listedPlans", {}).get(plan) if listed else None
        results.append({"provider": provider, "plan": plan, "modelId": model, "unit": unit, "region": region, "status": status, "listed": listed,
                        "currentPartition": latest_split, "partitionsWithReports": sorted({row["partition"] for row in eligible}),
                        "configurations": sorted({str(report["modelId"]) for report in reports}), "efforts": sorted({str(report.get("effort") or "unstated") for report in reports}), "value": value, "monthlyUsd": monthly, "multiple": monthly / fee if monthly is not None and fee else None,
                        "range": None if lowest is None else [lowest, highest], "feasibleRange": feasible, "reports": rows,
                        "allReportsBand": None if all_lower is None else [all_lower / CONCORDANCE, CONCORDANCE * all_upper],
                        "admittingObservers": sorted(row["observer"] for row in firm) if status == "passes" else [],
                        "discordantObservers": sorted(row["observer"] for row in discordant if row["partition"] == latest_split),
                        "searchedThrough": (search_dates or {}).get((model, plan)),
                        "newReportWindow": new_report_window(release_day, (search_dates or {}).get((model, plan))),
                        # Reviewer 95: the reports whose midpoint the O115 band moved, so a band-dominated value is visible.
                        "bandMoved": sorted(row["observer"] for row in firm if not feasible[0] <= (row["valueLower"] + row["valueUpper"]) / 2 <= feasible[1]) if status == "passes" else [],
                        "notArchivedAdmitting": sorted(row["observer"] for row in firm if row["archive"]) if status == "passes" else [],
                        "flags": ([ACROSS_RESETS_FLAG] if status == "passes" and any(row["acrossResets"] for row in firm) else [])
                                 + ([ACROSS_SPLIT_FLAG] if status == "passes" and any(row["acrossSplit"] for row in firm) else [])})
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
            reports = route.get("independentReports") or []
            # O127: a pair admitted at an earlier release ages like a measurement once its reports leave the window, so it
            # needs no passing cell now; a passing cell with other reports still forces the route to be revised.
            if not supporting and reports and all(report.get("admittedOn") for report in reports):
                continue
            if not supporting:
                raise ValueError(f"{route['id']}: no passing O71 cell supports a report route for {model} on {route.get('plan')} (O81)")
            # I66 L2: a plan and model can pass in more than one unit; the route's observers must be one cell's admitting set.
            observers = sorted(str(report.get("observer") or "") for report in route.get("independentReports") or [])
            if all(observers != cell["admittingObservers"] for cell in supporting):
                raise ValueError(f"{route['id']}: its reports ({', '.join(observers)}) are not a passing cell's admitting reports "
                                 f"({'; '.join(', '.join(cell['admittingObservers']) for cell in supporting)}) (O81)")
            # O156: a route resting on a cell admitted across documented meter resets carries the flag, and only then.
            matched = [cell for cell in supporting if cell["admittingObservers"] == observers]
            if any(ACROSS_RESETS_FLAG in cell.get("flags", []) for cell in matched) != bool(route.get("acrossResets")):
                raise ValueError(f"{route['id']}: acrossResets must be set exactly when its admitting reports span documented meter resets (O156)")
