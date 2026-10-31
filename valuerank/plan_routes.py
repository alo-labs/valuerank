"""v3 Plan routes: evidence admission, expiry, lexicographic route choice and Plan cost (O3, O4/O7, O11, O13, O16).

A route gives a Value Multiple M for a model on a plan tier. For each model the
route's evidence is classified:

- ``controlled``: a controlled saturation measurement of this exact model
  (e.g. SemiAnalysis);
- ``reports``: at least two independent, comparable end-user reports concordant
  within 20% (E102 comparability record first, then max/min <= 1.2 on the
  unpooled reports, then a geometric mean);
- ``assumption``: an owner-named model-to-model transfer (labelled; it never
  identifies the scored-workload multiple M_W).
- ``diagnostic``: single-source reports and anything else the admission rule
  does not admit; shown, never in the official Plan ranking.

Routes past the 90-day hard expiry plus a 30-day grace are demoted to
diagnostic; the model then falls back to API cost, flagged and labelled
"cross-estimand ordering not identified". Age runs from the evidence's own
observation date, never from a record's check or edit date, and an owner-named
transfer that names its donor measurement inherits that donor's date, expiry
stage, change flags and diagnostic status (E144). Routes certifiably dearer than another
identified route of at least equal grade are first set aside (E88). The official
route is then chosen by the E85 comparator: identification class (point > set >
unidentified), evidence grade (controlled > reports > assumption), the
comparison multiple, lower gross cash under the declared purchase policy, then
route ID. Plan cost is the API basket cost divided by the comparison multiple
(the lower bound of a multiple range; E74).
"""

from __future__ import annotations

import math
from datetime import date, timedelta

SOFT_EXPIRY_DAYS = 30
HARD_EXPIRY_DAYS = 90
GRACE_DAYS = 30
CONCORDANCE_RATIO = 1.2
CONTROLLED_KINDS = {"controlled_account_workload_projection", "controlled_measurement"}
ASSUMPTION_KINDS = {"user_assumption"}
REPORT_KINDS = {"user_reported_projection", "end_user_report", "community_observed"}
GRADE = {"controlled": 3, "reports": 2, "assumption": 1, "diagnostic": 0}
# O89, O90: a measurement of the same model at another effort (an O88 route) is measured evidence that ranks below an
# exact-effort measurement and above concordant reports, so it keeps its donor's precedence against reports only.
CROSS_EFFORT = 2.75
CROSS_EFFORT_FLAG = "same-model measurement from another effort (O88, O90)"
REPORT_PAIR_FLAG = "same-model route following its donor's replacing report pair (O96, O97)"
FAULT_FLAG = "measured inside an acknowledged accounting-fault window (O91, O92)"
# O78: a controlled route flagged by a detected change ranks just below a report pair measured after that change.
POST_CHANGE_SUPERSEDED = 1.5


def blocking_change(route: dict) -> str | None:
    """O107 (2026-10-28), I87 M1: the detected limit or price change that can block labels (E228) and let a later report pair
    outrank the measurement (O78). A route keeps two dates: ``changeDetectedOn``, the earliest change of any flagging type,
    which prints the "possibly superseded" label, and, when it differs, ``blockingChangeOn``, the earliest limit or price
    change (null when only a model-availability change, O105, flags it)."""

    return route["blockingChangeOn"] if "blockingChangeOn" in route else route.get("changeDetectedOn")


def grade_rank(candidate: dict) -> float:
    """The grade key of the comparator (O73, O78)."""

    if candidate.get("postChangeSuperseded"):
        return POST_CHANGE_SUPERSEDED
    # O89, O90, I73 L3: an O88 same-model route is a measurement of another effort; it outranks reports (one multiple per
    # model) but never an exact-effort measurement.
    if candidate["grade"] == "controlled" and candidate["route"].get("sameModelAcrossEfforts"):
        return CROSS_EFFORT
    return GRADE[candidate["grade"]]


def post_change_ranks(candidates: list[dict]) -> list[dict]:
    """O78: when a controlled route carries a detected change (E18) and a report-pair route for the same plan has every
    report dated after that change, the controlled route loses its precedence (O73) to it; the candidates are returned,
    marked, as copies."""

    marked = []
    for candidate in candidates:
        route = candidate["route"]
        # O89: an O88 route follows its donor's detected change, as it shares the donor's precedence.
        shares_donor = candidate["grade"] == "controlled" and route.get("sameModelAcrossEfforts")
        changed = blocking_change(route) or (candidate.get("donorChangeDetectedOn") if shares_donor else None)
        earliest = candidate.get("earliestEvidenceDate") or candidate.get("evidenceDate")
        # O78: only a flagged change supersedes; O92, O93: a controlled measurement in an acknowledged fault window (and every
        # route resting on it) yields to a concordant report pair for the same plan (whose reports E270 keeps off fault
        # days); an assumption already ranks below reports (I78 L1). I81 L1: the test is the one donor-following routes use.
        flagged = candidate.get("expiry") in {"possibly-superseded", "expired"}
        superseded = candidate["grade"] == "controlled" and any(
            other["grade"] == "reports" and other["route"].get("plan") == route.get("plan")
            and pair_replaces(other["route"], changed=changed if flagged else None, earliest=date.fromisoformat(earliest) if earliest else None,
                              faulted=bool(candidate.get("faultWindow")))
            for other in candidates)
        marked.append({**candidate, "postChangeSuperseded": True} if superseded else candidate)
    return marked


# E102: reports are pooled only when their public comparability records agree on all of these.
COMPARABILITY_FIELDS = ("feePeriod", "grossCashAccounting", "limitSchema", "eligibleConsumption", "valuationBasis", "measurementWorkload")
IDENTIFICATION = {"point-identified": 2, "set-identified": 1, "unidentified": 0}
# Route source-model labels mapped to ValueRank model ids (the donor of a measured multiple).
SOURCE_MODEL_IDS = {
    "Opus 5.5": "claude-opus-5-5",
    "GPT-6 Astra": "gpt-6-astra",
    "GPT-6.1 Sol": "gpt-6.1-sol",
    "Grok 4.7 XHigh": "grok-4.7",
}


def concordant_pool(reports: list[float]) -> float | None:
    """Geometric-mean pool of at least two independent reports that agree within 20% (checked unpooled)."""

    values = [float(value) for value in reports if value and value > 0]
    if len(values) < 2 or max(values) / min(values) > CONCORDANCE_RATIO:
        return None
    return math.exp(sum(math.log(value) for value in values) / len(values))


def comparable_groups(reports: list[dict]) -> tuple[list[list[dict]], list[dict]]:
    """E102: reports sharing a complete comparability record; reports without one stay separate objects."""

    groups: dict[tuple, list[dict]] = {}
    separate = []
    for report in reports:
        record = report.get("comparability") or {}
        if any(not record.get(field) for field in COMPARABILITY_FIELDS):
            separate.append(report)
            continue
        groups.setdefault(tuple(record[field] for field in COMPARABILITY_FIELDS), []).append(report)
    return list(groups.values()), separate


def pooled_reports(reports: list[dict]) -> dict | None:
    """The concordant comparable group with the highest pooled multiple (the owner's highest-eligible rule), or None."""

    groups, _separate = comparable_groups(reports)
    pooled = []
    for group in groups:
        value = concordant_pool([report.get("multiple") for report in group])
        if value is not None:
            pooled.append({"multiple": value, "reportIds": sorted(report["id"] for report in group)})
    return max(pooled, key=lambda item: (item["multiple"], item["reportIds"]), default=None)


def evidence_grade(route: dict, model_id: str) -> str:
    """Classify a route's evidence for one model (see the module docstring)."""

    kind = route.get("valueMultipleKind")
    source_kind = route.get("sourceEvidenceClass")
    same_model = SOURCE_MODEL_IDS.get(route.get("sourceModel")) == model_id
    if kind in CONTROLLED_KINDS:
        return "controlled" if same_model or len(route.get("modelIds", [])) == 1 else "assumption"
    if kind in ASSUMPTION_KINDS:
        # The donor model's own route is its measurement; other models carry the owner-named transfer. O90: an O88 route
        # (the same model's measurement at another effort) is measured evidence too.
        cross_effort = route.get("sameModelAcrossEfforts") and source_kind in CONTROLLED_KINDS
        return "controlled" if (same_model or cross_effort) and source_kind in CONTROLLED_KINDS else "assumption"
    if kind in REPORT_KINDS and pooled_reports(route.get("independentReports") or []) is not None:
        return "reports"
    return "diagnostic"


def donor(route: dict, registry: dict | None) -> dict | None:
    """E144: the donor measurement an owner-named transfer names (``donorRouteId``), resolved in the route registry."""

    donor_id = route.get("donorRouteId")
    if donor_id is None:
        return None
    seen = {route["id"]}
    while True:
        if registry is None or donor_id not in registry:
            raise ValueError(f"route {route['id']} names an unknown donor measurement: {donor_id}")
        if donor_id in seen:
            raise ValueError(f"donor chain of route {route['id']} is circular")
        seen.add(donor_id)
        found = registry[donor_id]
        donor_id = found.get("donorRouteId")
        if donor_id is None:
            return found


def evidence_date(route: dict, registry: dict | None = None) -> date | None:
    """E144: when the evidence was observed — the donor's date for a transfer, else the measurement window's end,
    the source publication date, or (for an owner assumption without a donor measurement) its authorisation date.

    A record's check or edit date (``checkedOn``) is an editorial event and never restarts the clock. An O46 quota
    ceiling is a function of Xiaomi's pages, so it ages from the read of those pages (``capturedOn``, E261, I50 M1).
    """

    source = donor(route, registry) or route
    ceiling = source.get("evidenceClass") == "provider_quota_ceiling" and source.get("capturedOn")
    stamp = ceiling or (source.get("measurementWindow") or {}).get("end") or source.get("sourcePublicationDate") or source.get("validFrom")
    return date.fromisoformat(stamp) if stamp else None


def age_days(route: dict, release_day: date, registry: dict | None = None) -> int | None:
    stamp = evidence_date(route, registry)
    return None if stamp is None else (release_day - stamp).days


def expiry_status(route: dict, release_day: date, registry: dict | None = None) -> str:
    """fresh / possibly-superseded (soft expiry or a scoped change detected since observation) / expired (hard
    expiry, in grace) / demoted (past grace); a transfer takes its donor's stage (E144)."""

    source = donor(route, registry) or route
    if source is not route and source.get("valueMultipleKind") in REPORT_KINDS:
        # E151, E144, I82 L1: a transfer resting on a report pair ages with the pair's contributors.
        stage = measurement_objects(source, release_day)[0].get("partitionStage")
        if stage:
            return stage
    age = age_days(source, release_day)
    if age is None:
        return "fresh"
    if age > HARD_EXPIRY_DAYS + GRACE_DAYS:
        return "demoted"
    if age > HARD_EXPIRY_DAYS:
        return "expired"
    changed = source.get("changeDetectedOn")
    # I79 L1, I80 L3: a change can have superseded the measurement unless it predates the earliest date the measurement can
    # have been taken (its window start, else 30 dates before publication).
    earliest = change_floor(source) or evidence_date(source)
    if age > SOFT_EXPIRY_DAYS or (changed and earliest is not None and earliest <= date.fromisoformat(changed) <= release_day):
        return "possibly-superseded"
    return "fresh"


CAPACITY_ESTABLISHED = "capacity established on the measurement workload"
CAPACITY_OBSERVED = "observed usage; capacity not established"
CAPACITY_UNVERIFIED = "saturation unverified"
CAPACITY_CEILING = "provider quota ceiling: full use of the quota assumed (O46)"
CAPACITY_STATUSES = (CAPACITY_ESTABLISHED, CAPACITY_OBSERVED, CAPACITY_UNVERIFIED, CAPACITY_CEILING)


def measurement_capacity_status(route: dict) -> str:
    """E139: whether the measurement established capacity on its own workload (separate from transport to W).

    A recorded status wins; otherwise a controlled saturation measurement (the donor's,
    for an owner-named transfer) establishes capacity, and anything else is unverified.
    """

    recorded = route.get("measurementCapacityStatus")
    if recorded in CAPACITY_STATUSES:
        return recorded
    if route.get("evidenceClass") == "provider_quota_ceiling":
        # I68 L2: an O46 ceiling observes nothing; it is the whole quota by construction.
        return CAPACITY_CEILING
    kind, source_kind = route.get("valueMultipleKind"), route.get("sourceEvidenceClass")
    if kind in CONTROLLED_KINDS or (kind in ASSUMPTION_KINDS and source_kind in CONTROLLED_KINDS):
        return CAPACITY_ESTABLISHED
    return CAPACITY_UNVERIFIED


def valuation_status(route: dict) -> str:
    """E138: release / revalued / different (O7 price-basis mismatch) / unverified (basis not recorded)."""

    if route.get("valuationBasisReconciled") is False:
        return "different"
    return route.get("valuationBasis") if route.get("valuationBasis") in {"release", "revalued", "different"} else "unverified"


def _divisor_eligible(route: dict) -> bool:
    """E109: every multiple a route can divide by is finite and strictly positive."""

    values = [route.get("valueMultiple")] + [route[key] for key in ("valueMultipleLower", "valueMultipleUpper") if key in route]
    return all(isinstance(value, (int, float)) and not isinstance(value, bool) and 0 < value < math.inf for value in values)


STAGES = ("fresh", "possibly-superseded", "expired", "demoted")

# E194: AGENTS.md's "reports from the preceding month" is the 30 days ending on the release cutoff (E213).
REPORT_WINDOW_DAYS = 30


def report_date(report: dict) -> date | None:
    """E194: a report's date is its measurement window's end, else its report date, else its publication date."""

    stamp = (report.get("measurementWindow") or {}).get("end") or report.get("reportDate") or report.get("sourcePublicationDate")
    return date.fromisoformat(stamp) if stamp else None


def in_window(report: dict, window: dict | None) -> bool:
    """O32: a report counts toward source count and concordance only while dated inside the current report window."""

    if window is None:
        return True
    stamp = report_date(report)
    return stamp is not None and date.fromisoformat(window["start"]) <= stamp <= date.fromisoformat(window["end"])


def straddles(report: dict, window: dict | None) -> bool:
    """E201: a counted report whose measurement window starts before the report window is flagged window-straddling."""

    start = (report.get("measurementWindow") or {}).get("start")
    return window is not None and start is not None and date.fromisoformat(start) < date.fromisoformat(window["start"])


def check_report_window(document: dict) -> None:
    """E194: every newly admitted end-user report is dated inside the release's report window.

    A report admitted at an earlier release records ``admittedOn``; under O127 it keeps counting after it leaves
    the window, ageing on its own clock (E151/O13) until demotion.
    """

    window = document["evidencePolicy"]["reportingWindow"]
    start, end = date.fromisoformat(window["start"]), date.fromisoformat(window["end"])
    if (end - start).days != REPORT_WINDOW_DAYS:
        raise ValueError(f"the report window must span {REPORT_WINDOW_DAYS} days ending at the release cutoff (E194, E213)")
    for route in document["routes"]:
        if route.get("valueMultipleKind") not in REPORT_KINDS:
            continue
        for report in route.get("independentReports") or [route]:
            if not report.get("admittedOn") and not in_window(report, window):
                raise ValueError(f"{report['id']}: end-user report dated outside the report window {start} to {end} (E194)")


def check_report_independence(document: dict) -> None:
    """E223: reports pooled for one route are independent: each names its observer, observers are distinct, and no two
    share an upstream source (a post, thread or derivation). Calendar spacing is not required (O11)."""

    for route in document["routes"]:
        reports = route.get("independentReports") or []
        observers = [str(report.get("observer") or "").strip() for report in reports]
        sources = [report.get("upstreamSource") for report in reports if report.get("upstreamSource")]
        if reports and (not all(observers) or len(set(observers)) < len(observers) or len(set(sources)) < len(sources)):
            raise ValueError(f"{route['id']}: pooled reports must name distinct observers and share no upstream source (E223)")


def change_flagged(candidate: dict | None, release_day: date | None = None) -> bool:
    """E228: a selected route whose evidence a scoped change (or two reports of a limit change) may have superseded."""

    # I76 L2: a transfer or O88 route inherits its donor's detected change (E144, O89). I77 L2: a change dated after the
    # release cutoff does not count (age alone never makes a blocker).
    changed = candidate and (blocking_change(candidate["route"]) or candidate.get("donorChangeDetectedOn"))
    if changed and release_day is not None and date.fromisoformat(changed) > release_day:
        return False
    # I78 L2, I79 L1: a change dated before the earliest date the measurement can have been taken cannot have superseded it.
    earliest = candidate.get("earliestEvidenceDate") or candidate.get("evidenceDate") if candidate else None
    if changed and earliest and date.fromisoformat(changed) < date.fromisoformat(earliest):
        return False
    return bool(changed and candidate.get("expiry") in {"possibly-superseded", "expired"})


def label_denied(candidate: dict | None, release_day: date | None = None) -> bool:
    """E228, O118, O119: a selected Plan route that competes but earns no label: change-flagged, hard-expired (in grace) or
    measured inside an acknowledged accounting-fault window."""

    if candidate is None:
        return False
    return change_flagged(candidate, release_day) or candidate.get("expiry") == "expired" or bool(candidate.get("faultWindow"))



# O126 (2026-10-30): an allowance is effort-invariant only on a meter that counts tokens or credits; on a meter that
# counts messages, requests or time, a higher effort spends more tokens per unit, so the multiple differs by effort.
EFFORT_INVARIANT_METERS = {"tokens", "credits"}
METER_DENOMINATIONS = EFFORT_INVARIANT_METERS | {"messages", "requests", "time window", "not documented"}


def check_same_model_routes(document: dict, families: dict | None = None) -> None:
    """I74 L3: a route flagged ``sameModelAcrossEfforts`` (which O90 grades as measured) must name a controlled donor
    measurement of the same model on the same plan, at another configuration of that model. O126: its plan's recorded
    meter must count tokens or credits; any other meter needs the route recorded as a donor assumption instead."""

    by_id = {route["id"]: route for route in document["routes"]}
    meters = (document.get("evidencePolicy") or {}).get("meterDenominations")
    for route in document["routes"]:
        if not route.get("sameModelAcrossEfforts"):
            continue
        if meters is not None:
            meter = (meters.get(route.get("plan")) or {}).get("denomination")
            if meter not in METER_DENOMINATIONS:
                raise ValueError(f"{route['id']}: plan {route.get('plan')!r} has no recorded meter denomination (O126)")
            if meter not in EFFORT_INVARIANT_METERS:
                raise ValueError(f"{route['id']}: plan {route.get('plan')!r} meters {meter}, so a cross-effort figure is a donor assumption, not measured (O126)")
        source = by_id.get(route.get("donorRouteId") or "")
        if source is None or source.get("valueMultipleKind") not in CONTROLLED_KINDS:
            raise ValueError(f"{route['id']}: a same-model route needs a controlled donor measurement (O88, O90)")
        mine, theirs = (route.get("modelIds") or [None])[0], (source.get("modelIds") or [None])[0]
        same_model = (families or {}).get(mine, mine) == (families or {}).get(theirs, theirs) if mine in (families or {}) and theirs in (families or {}) \
            else str(mine).startswith(f"{theirs}-")
        if source.get("plan") != route.get("plan") or mine == theirs or not same_model or source.get("sourceModel") != route.get("sourceModel"):
            raise ValueError(f"{route['id']}: its donor {source['id']} is not the same model's measurement on {route.get('plan')} at another configuration (O88, O90)")
        # I75 L2: the route carries its donor's multiple and allocation regime unchanged (E220).
        if (route.get("valueMultiple"), route.get("allocationRegime"), route.get("planPriceUsd")) != (source.get("valueMultiple"), source.get("allocationRegime"), source.get("planPriceUsd")):
            raise ValueError(f"{route['id']}: a same-model route must carry its donor {source['id']}'s multiple and allocation regime (O88, E220)")


REREAD_MAX_AGE_DAYS = 30


def check_source_rereads(document: dict, release_day: date) -> str | None:
    """O130: a paywalled selected article is not captured, so each release re-reads its figure table against the transcription
    made at selection; the latest read (``rereads``) must be dated on or before the release day and at most 30 days before
    it. Returns the latest read's date (None when no source is paywalled)."""

    latest = None
    for key, source in (document.get("sourceEvidence") or {}).items():
        if not source.get("paywalled"):
            continue
        reads = sorted(item["readOn"] for item in source.get("rereads") or [] if date.fromisoformat(item["readOn"]) <= release_day)
        if not reads or (release_day - date.fromisoformat(reads[-1])).days > REREAD_MAX_AGE_DAYS:
            raise ValueError(f"{key}: the selected article has no re-read of its figure table within {REREAD_MAX_AGE_DAYS} days of the release (O130)")
        latest = max(latest or reads[-1], reads[-1])
    return latest


def check_lower_of_routes(document: dict) -> None:
    """O45, O95: a stored lower-of transfer names the lower of its plan's measured figures and carries that multiple."""

    by_id = {route["id"]: route for route in document["routes"]}
    for route in document["routes"]:
        if route.get("donorRule") != "lower-of":
            continue
        measured = [item for item in by_id.values() if item.get("valueMultipleKind") in CONTROLLED_KINDS and item.get("provider") == route.get("provider")
                    and item.get("plan") == route.get("plan") and item.get("sourceEvidenceId") == route.get("sourceEvidenceId")]
        lowest = min(measured, key=lambda item: (comparison_multiple(item), item["id"]), default=None)
        if lowest is None or lowest["id"] != route.get("donorRouteId") or lowest["valueMultiple"] != route.get("valueMultiple"):
            raise ValueError(f"{route['id']}: a lower-of transfer must name and carry the lowest measured figure on {route.get('plan')} (O45, O95)")


def check_allocation_regimes(document: dict) -> None:
    """E220: a controlled subscription-account measurement keeps the allocation regime it was measured under (AGENTS.md),
    so measurements under different regimes are never compared or pooled as one."""

    for route in document["routes"]:
        if route.get("valueMultipleKind") in CONTROLLED_KINDS and not str(route.get("allocationRegime") or "").strip():
            raise ValueError(f"{route['id']}: a controlled measurement must record its allocation regime (E220)")


def check_selected_analysis(document: dict) -> None:
    """E238: for the providers whose comparison the owner tied to one selected analysis (AGENTS.md), every controlled
    measurement and every transfer of one cites that analysis. A newer analysis enters only when the owner selects it;
    the selection then replaces the old one outright (its routes become diagnostics), whatever their multiples."""

    selected = document["evidencePolicy"].get("selectedSourceException")
    if not selected:
        return
    for route in document["routes"]:
        cites_series = route.get("sourceEvidenceId") == "semianalysis" or route.get("valueMultipleKind") in CONTROLLED_KINDS
        if route.get("provider") in selected["providers"] and cites_series and route.get("sourceUrl") != selected["sourceUrl"]:
            raise ValueError(f"{route['id']}: cites {route.get('sourceUrl')}, not the owner-selected analysis {selected['sourceUrl']} (E238)")


def report_stage(report: dict, route: dict, release_day: date) -> str:
    """E151: one report's own expiry stage, by its E194 date (window end, report date, publication date); else the route's."""

    stamp = report_date(report)
    source = {"id": report["id"], "sourcePublicationDate": stamp.isoformat(), "changeDetectedOn": route.get("changeDetectedOn")} if stamp else route
    return expiry_status(source, release_day)


def measurement_objects(route: dict, release_day: date | None = None, window: dict | None = None) -> list[dict]:
    """E111/E151: a route's measurement objects — its own measurement, or one per concordant comparable report partition.

    With a release day, each report is first classified by its own clock; reports
    past expiry and grace leave their partition, and the complete surviving
    partition is pooled and re-tested for source count and concordance (never a
    searched-for passing subset). The object carries its contributors, the
    excluded reports and its partition stage (the most advanced contributor stage).
    With a report window, only reports dated inside it count (O32); older ones are excluded.
    """

    reports = route.get("independentReports")
    if route.get("valueMultipleKind") not in REPORT_KINDS or not reports:
        return [route]
    stages = {report["id"]: report_stage(report, route, release_day) if release_day else "fresh" for report in reports}
    # O127 (2026-10-30): a report admitted at an earlier release (``admittedOn``) keeps counting after it leaves the window,
    # ageing on its own clock like a measurement until demotion; only newly admitted reports must be in the window (O32).
    counted = {report["id"] for report in reports if stages[report["id"]] != "demoted" and (in_window(report, window) or report.get("admittedOn"))}
    excluded = sorted(report["id"] for report in reports if report["id"] not in counted)
    groups, _separate = comparable_groups(reports)
    objects = []
    for index, group in enumerate(groups, start=1):
        surviving = [report for report in group if report["id"] in counted]
        pooled = concordant_pool([report.get("multiple") for report in surviving])
        if pooled is not None:
            objects.append({
                **route, "id": f"{route['id']}#m{index}", "routeId": route["id"], "valueMultiple": pooled, "independentReports": surviving,
                "reportIds": sorted(report["id"] for report in surviving), "excludedReportIds": excluded,
                "windowStraddlingReportIds": sorted(report["id"] for report in surviving if straddles(report, window)),
                "partitionStage": max((stages[report["id"]] for report in surviving), key=STAGES.index),
            })
    # No surviving partition: the route keeps only its unexpired reports, so it cannot grade as pooled evidence.
    return objects or [{**route, "independentReports": [report for report in reports if report["id"] in counted], "excludedReportIds": excluded}]


# E208: the token-mix comparison is against the basket's own demand region (E124), never AA's Index-wide shares. AA
# publishes that region only as set-identified totals, so no route's category shares can be compared with it today.
MIX_NOT_REPORTED = "mix not reported: the measurement publishes no token-category shares"
MIX_UNIDENTIFIED = "mix unidentified: the basket's token-category shares are set-identified only (E124), so the L1 test (above 0.30 flags mix-unmatched) is not computed"


def mix_check(measurement: dict) -> str:
    """E208: the token-mix status of a measurement against the basket's demand region."""

    return MIX_UNIDENTIFIED if measurement.get("workloadMix") else MIX_NOT_REPORTED


FAULT_LOOKBACK_DAYS = 30  # I77 L1: an undated measurement window is taken as the 30 days ending on publication


def _regime_start(route: dict) -> date | None:
    """O110: the later of the measured model's launch on the plan and the start of the plan schedule the measurement says it
    ran under, when recorded."""

    bounds = [date.fromisoformat(route[key]) for key in ("modelLaunchedOn", "scheduleFrom") if route.get(key)]
    return max(bounds) if bounds else None


def measurement_span(route: dict) -> tuple[date | None, date | None]:
    """I77 L1, I79 L1, O110: the earliest and latest dates a controlled measurement can have been taken: its stated window,
    else the 30 dates ending on its publication date, never before its model's launch or its stated schedule's start."""

    window = route.get("measurementWindow") or {}
    published = route.get("sourcePublicationDate")
    first = date.fromisoformat(window["start"]) if window.get("start") else (date.fromisoformat(published) - timedelta(days=FAULT_LOOKBACK_DAYS - 1) if published else None)
    last = date.fromisoformat(window["end"]) if window.get("end") else (date.fromisoformat(published) if published else None)
    regime = _regime_start(route)
    if regime is not None and (first is None or regime > first):
        first = regime
    return first, last


def change_floor(route: dict) -> date | None:
    """O110: the earliest date a change can postdate the measurement. A change dated on the launch or schedule start that
    bounds the span is part of the measured regime (for example a limit raised at the model's launch), so it must be later."""

    first = measurement_span(route)[0]
    regime = _regime_start(route)
    return first + timedelta(days=1) if first is not None and regime is not None and first == regime else first


def in_fault_window(route: dict, faults: list[dict] | None) -> dict | None:
    """O91, O92: the acknowledged accounting-fault entry a controlled measurement may fall in. The measurement is dated by its
    window, else conservatively by the 30 days ending on its publication date; an undated measurement on a plan with a fault
    is treated as inside it (fail closed)."""

    if not faults or route.get("valueMultipleKind") not in CONTROLLED_KINDS:
        return None
    # I78 L2: 30 dates ending on the publication date (inclusive), the same end date the age and change clocks use (E144).
    first, last = measurement_span(route)
    for fault in faults:
        if fault.get("provider") != route.get("provider") or (fault.get("plans") and route.get("plan") not in fault["plans"]):
            continue
        if first is None or last is None:
            return fault
        for day in fault["days"]:
            low, _, high = day.partition("..")
            if first <= date.fromisoformat(high or low) and last >= date.fromisoformat(low):
                return fault
    return None


def report_covers(route: dict, model_id: str, families: dict | None = None) -> str | None:
    """O87 (allowance is effort-invariant), I81 L1, I82 L1: the configuration ID through which a route covers a
    configuration: its own; for a report route, also any configuration of the same AA family (keyed by the families map,
    never by parsing the ID, I69 L2)."""

    listed = route.get("modelIds") or []
    if model_id in listed:
        return model_id
    if route.get("valueMultipleKind") in REPORT_KINDS and families and model_id in families:
        return next((item for item in listed if families.get(item) == families[model_id]), None)
    return None


def pair_replaces(report_route: dict, *, changed: str | None, earliest: date | None, faulted: bool, release_day: date | None = None) -> bool:
    """O78, O92 (I81 L1: the one replacement test the comparator and every donor-following route share): an admitted report
    pair replaces a controlled measurement on the same plan when the measurement is in an acknowledged fault window, or a
    detected change (on or after the earliest day the measurement can have been taken, and by the release cutoff) predates
    every report of the pair."""

    if faulted:
        return True
    if not changed:
        return False
    change = date.fromisoformat(changed)
    if (release_day is not None and change > release_day) or (earliest is not None and change < earliest):
        return False
    dates = [report_date(report) for report in report_route.get("independentReports") or report_route.get("reports") or [report_route]]
    return None not in dates and min(dates) > change


def effective_measurement(route: dict, registry: dict, release_day: date, window: dict | None, faults: list[dict] | None,
                          families: dict | None = None) -> dict:
    """O92, O93, O78, O96, I82 L1: the measurement that stands for a controlled route's model on its plan is whatever the
    comparator selects for that model from the measurement and the report routes covering the model on that plan (O87):
    the replacing report pair, else the measurement itself (also when no route remains eligible)."""

    model = (route.get("modelIds") or [None])[0]
    reports = [other for other in registry.values() if other.get("valueMultipleKind") in REPORT_KINDS and other.get("plan") == route.get("plan")
               and model is not None and report_covers(other, model, families) is not None]
    if not reports:
        return route
    candidates = route_candidates(model, route.get("requiredVariant"), [route, *reports], release_day, registry=list(registry.values()),
                                  window=window, faults=faults, families=families)
    selected = route_selection(candidates)["selected"]
    if selected is None or selected["grade"] != "reports":
        return route
    # I80 L4: the replacing object names its base route, the id a transfer can name as its donor.
    return {**selected["route"], "baseRouteId": selected["route"].get("routeId", selected["route"]["id"])}


def measurement_eligible(route: dict, release_day: date, registry: dict | None) -> bool:
    """The comparator's own exclusions for a controlled measurement (route_candidates): demoted, an invalid divisor (E109) or
    an unreconcilable valuation basis (O7, E123)."""

    return expiry_status(route, release_day, registry) != "demoted" and _divisor_eligible(route) and valuation_status(route) != "different"


def rebase_lower_of(route: dict, registry: dict, release_day: date, window: dict | None, faults: list[dict] | None,
                    families: dict | None = None) -> dict:
    """O95: a lower-of transfer (O45) takes, per plan, the lower of its plan's measured figures, each model's figure being
    its effective measurement (a replacing report pair or the controlled route); the result names its donor."""

    measured = [item for item in registry.values() if item.get("valueMultipleKind") in CONTROLLED_KINDS and item.get("provider") == route.get("provider")
                and item.get("plan") == route.get("plan") and item.get("sourceEvidenceId") == route.get("sourceEvidenceId")]
    if not measured:
        return route
    effective = [effective_measurement(item, registry, release_day, window, faults, families) for item in measured]
    # O104, I86 L2: a measurement the comparator would grade diagnostic (demoted, an invalid divisor or an unreconcilable
    # valuation basis) and no report pair replaced has left the selection (E142), so it drops out of the minimum; with no
    # eligible figure left the transfer keeps its stored donor and is diagnostic with it (E144).
    eligible = [item for item in effective if item.get("valueMultipleKind") in REPORT_KINDS or measurement_eligible(item, release_day, registry)]
    if not eligible:
        return route
    lowest = min(eligible, key=lambda item: (comparison_multiple(item), item["id"]))
    return _rebased(route, lowest)


# I82 L2: the fields that identify a following route; everything else is the measurement it now rests on.
FOLLOWER_IDENTITY = ("id", "modelIds", "requiredVariant", "donorRule")


def _rebased(route: dict, donor_object: dict) -> dict:
    donor_id = donor_object.get("baseRouteId", donor_object["id"])
    if donor_id == route.get("donorRouteId"):
        return route
    if route.get("sameModelAcrossEfforts") and donor_object.get("valueMultipleKind") in REPORT_KINDS:
        # O97, I82 L2: an O88 route that follows its donor to a replacing report pair is no longer a measurement of another
        # effort: it takes the pair's whole measurement object (grade, amount, workload, window, dates, statuses).
        # I83 L2: the pair's own variant restriction never carries over to the follower.
        pair = {key: value for key, value in donor_object.items() if key not in {"baseRouteId", "routeId", "requiredVariant"}}
        return {**pair, **{key: route[key] for key in FOLLOWER_IDENTITY if key in route}, "donorRouteId": donor_id,
                "rebasedFrom": route.get("donorRouteId"), "followsReportPair": donor_id, "sameModelAcrossEfforts": False}
    return {**route, "donorRouteId": donor_id, "valueMultiple": comparison_multiple(donor_object), "rebasedFrom": route.get("donorRouteId"),
            "sourceModel": donor_object.get("sourceModel", route.get("sourceModel"))}


def rebase_transfer(route: dict, registry: dict, release_day: date, window: dict | None, faults: list[dict] | None,
                    families: dict | None = None) -> dict:
    """O95, O96: every route resting on a donor measurement takes its donor's effective figure: a lower-of transfer the lower
    of its plan's effective figures, any other transfer (or O88 route) its own donor's replacing report pair, if any."""

    if route.get("donorRule") == "lower-of":
        return rebase_lower_of(route, registry, release_day, window, faults, families)
    source = registry.get(route.get("donorRouteId") or "")
    if source is None or source.get("valueMultipleKind") not in CONTROLLED_KINDS:
        return route
    return _rebased(route, effective_measurement(source, registry, release_day, window, faults, families))


def route_candidates(model_id: str, configuration_effort: str | None, routes: list[dict], release_day: date, *, registry: list[dict] | None = None,
                     window: dict | None = None, faults: list[dict] | None = None, families: dict | None = None) -> list[dict]:
    """Every route-measurement pair for this model, classified; variant-restricted routes need an exact effort match,
    except report routes, whose allowance evidence covers every configuration of the model (O87, I82 L1).

    ``registry`` is the full route list donors are resolved in (default: ``routes``); ``window`` is the
    release's report window (O32); ``faults`` are the acknowledged accounting-fault windows (O91); ``families`` maps
    configuration IDs to AA families (O87).
    """

    by_id = {item["id"]: item for item in (registry if registry is not None else routes)}
    candidates = []
    for route in [item for base in routes for item in measurement_objects(base, release_day, window)]:
        if report_covers(route, model_id, families) is None:
            continue
        reported = route.get("valueMultipleKind") in REPORT_KINDS
        route = rebase_transfer(route, by_id, release_day, window, faults, families)
        required = route.get("requiredVariant")
        if required is not None and not reported and (configuration_effort or "").casefold() != required.casefold():
            continue
        grade = evidence_grade(route, model_id)
        # E151: a pooled partition ages with its contributors; any other object with its own (or its donor's) clock.
        expiry = route.get("partitionStage") or expiry_status(route, release_day, by_id)
        source = donor(route, by_id)
        # O7/E123: a measurement on an unreconciled price basis is unmatched; E109: divisors must be positive;
        # E144: a transfer is diagnostic whenever its donor measurement is.
        checks = [route] + ([source] if source is not None else [])
        # O32: a transfer whose donor is an end-user report partition follows the donor's window status.
        lapsed_donor = source is not None and source.get("valueMultipleKind") in REPORT_KINDS and evidence_grade(measurement_objects(source, release_day, window)[0], model_id) == "diagnostic"
        # O91 as amended by O92: a controlled measurement taken in an acknowledged fault window (or a transfer or O88 route
        # resting on one) stays selected and flagged until two concordant user reports for the plan replace it.
        faulted = next((fault for item in checks if (fault := in_fault_window(item, faults))), None)
        if lapsed_donor or expiry == "demoted" or any(not _divisor_eligible(item) or valuation_status(item) == "different" for item in checks):
            grade = "diagnostic"
        stamp = evidence_date(route, by_id)
        provenance = source if source is not None else route
        candidates.append(
            {
                "route": route,
                "grade": grade,
                "expiry": expiry,
                "identification": route.get("identification", "unidentified"),
                "evidenceDate": stamp.isoformat() if stamp else None,
                # I79 L1: the earliest date the (donor's) measurement can have been taken.
                "earliestEvidenceDate": (lambda first: first.isoformat() if first else None)(change_floor(provenance)),
                "donorRouteId": source["id"] if source is not None else None,
                "donorChangeDetectedOn": blocking_change(source) if source is not None else None,
                "faultWindow": faulted["evidence"] if faulted else None,
                # E144: valuation compatibility and capacity status are the donor measurement's for a transfer.
                "valuation": "different" if "different" in {valuation_status(item) for item in checks} else valuation_status(provenance),
                "measurementCapacityStatus": measurement_capacity_status(provenance),
                "mixCheck": mix_check(provenance),
            }
        )
    # I83 L2: an O88 follower of a report pair that is itself a candidate here is the same evidence twice; the pair stands.
    present = {item["route"].get("routeId") for item in candidates if item["route"].get("valueMultipleKind") in REPORT_KINDS}
    return [item for item in candidates if item["route"].get("followsReportPair") not in present or not item["route"].get("followsReportPair")]


IDENTIFIED = {"point-identified", "set-identified"}


def admission_table(model_id: str, configuration_effort: str | None, routes: list[dict], release_day: date, window: dict | None = None,
                    faults: list[dict] | None = None, families: dict | None = None) -> list[dict]:
    """E106/E123: every route-measurement pair naming the model, classified once by case and the three predicates.

    1 execution-identity incompatibility (excluded); 2 owner assumption: an
    owner-named transfer or an O46 ceiling (display only, never identifies
    M_W); 3 measurement with unidentified transport, exact-route or, under
    O90, an O88 route measured on the same model at another effort
    (displayed, interval-ineligible); 4 any route (or its donor) on an
    unreconciled price basis (unmatched under O7: diagnostic only); 5 evidence failing admission (diagnostic only); and "identified" for
    measurements (exact-route or O88) with an identified M_W. A measurement in an acknowledged fault window keeps its case
    and is flagged (O91, O92).
    """

    table = []
    for route in routes:
        if report_covers(route, model_id, families) is None:
            continue
        candidates = route_candidates(model_id, configuration_effort, [route], release_day, registry=routes, window=window, faults=faults, families=families)
        if not candidates:
            table.append({"route": route, "case": 1, "officialDisplayEligible": False, "targetTransportIdentified": False, "planIntervalEligible": False})
            continue
        for candidate in candidates:
            identified = candidate["identification"] in IDENTIFIED
            if candidate["valuation"] == "different":
                case = 4
            elif candidate["grade"] == "diagnostic":
                case = 5
            elif candidate["grade"] == "assumption":
                case = 2
            else:
                case = "identified" if identified else 3
            transport = case == "identified"
            valued = candidate["valuation"] in {"release", "revalued"}
            table.append({
                # I82 L2: crossEffort reads the (possibly rebased) candidate route.
                **candidate, "case": case, "crossEffort": bool(candidate["route"].get("sameModelAcrossEfforts")), "officialDisplayEligible": case not in (4, 5),
                "targetTransportIdentified": transport, "planIntervalEligible": transport and valued,
            })
    return table


def gross_cash(route: dict) -> float:
    """Cash paid for the fee period under the declared purchase policy (subscription fee + declared additional cash)."""

    fee = route.get("planPriceUsd")
    if not isinstance(fee, (int, float)):
        return math.inf
    return float(fee) + float(route.get("additionalCashUsd") or 0.0)


def comparison_multiple(route: dict) -> float:
    """The multiple a route is compared and scored at: its lower bound when a range is recorded (E74)."""

    return float(route.get("valueMultipleLower", route["valueMultiple"]))


def comparison_tuple(candidate: dict) -> tuple:
    """The E85 comparator key (higher is preferred); published with every route."""

    route = candidate["route"]
    return (
        IDENTIFICATION.get(candidate["identification"], 0),
        grade_rank(candidate),
        comparison_multiple(route),
        -gross_cash(route),
    )


def identified_bounds(candidate: dict) -> tuple[float, float] | None:
    """[L, U] of an identified M_W: a point twice, or a set's bounds (no recorded upper bound = unbounded)."""

    route = candidate["route"]
    if candidate["identification"] == "point-identified":
        return float(route["valueMultiple"]), float(route["valueMultiple"])
    if candidate["identification"] == "set-identified":
        return comparison_multiple(route), float(route.get("valueMultipleUpper", math.inf))
    return None


def dominance_filter(candidates: list[dict]) -> tuple[list[dict], dict]:
    """E88: set aside each route b for which an identified route a of at least b's grade has L_a > U_b.

    L_a > U_b makes a cheaper on the workload in every admissible state, whatever
    the joint constraints. Unidentified routes neither filter nor are filtered.
    Returns the remaining routes and {dominated route ID: dominating route ID}.
    """

    dominated = {}
    for loser in candidates:
        loser_bounds = identified_bounds(loser)
        for winner in candidates:
            winner_bounds = identified_bounds(winner)
            if winner is loser or loser_bounds is None or winner_bounds is None:
                continue
            if grade_rank(winner) >= grade_rank(loser) and winner_bounds[0] > loser_bounds[1]:
                dominated[loser["route"]["id"]] = winner["route"]["id"]
                break
    return [candidate for candidate in candidates if candidate["route"]["id"] not in dominated], dominated


DECIDING_KEYS = ("higher identification class", "higher evidence grade", "larger comparison multiple", "lower gross cash")


def _order(candidate: dict) -> tuple:
    """E85/E116: the comparator keys, then route ID, then the measurement-object ID (a total order)."""

    route = candidate["route"]
    return tuple(-value for value in comparison_tuple(candidate)), route.get("routeId", route["id"]), route["id"]


def comparator_key(candidate: dict) -> tuple:
    """The total comparator order (E85/E116); sorting ascending puts the official choice first."""

    return _order(candidate)


def route_selection(candidates: list[dict]) -> dict:
    """The official route with its published selection reason, dominated routes and comparison tuples (E85, E88, E93)."""

    eligible = post_change_ranks([candidate for candidate in candidates if candidate["grade"] != "diagnostic"])
    remaining, dominated = dominance_filter(eligible)
    ordered = sorted(remaining, key=_order)
    tuples = {candidate["route"]["id"]: comparison_tuple(candidate) for candidate in eligible}
    if not ordered:
        return {"selected": None, "reason": "no eligible route", "dominated": dominated, "tuples": tuples}
    if len(ordered) == 1:
        return {"selected": ordered[0], "reason": "only remaining eligible route", "dominated": dominated, "tuples": tuples}
    best, runner_up = (comparison_tuple(candidate) for candidate in ordered[:2])
    deciding = next((DECIDING_KEYS[index] for index, (a, b) in enumerate(zip(best, runner_up)) if a != b), "route ID tie-break")
    if deciding == DECIDING_KEYS[2] and ordered[0]["route"].get("evidenceClass") == "provider_quota_ceiling":
        deciding = "larger quota-ceiling multiple (O46: provider-derived, not observed)"
    elif deciding == DECIDING_KEYS[2] and ordered[0]["identification"] == "unidentified":
        deciding = "larger observed multiple (observed-workload multiple — target-workload ordering not identified)"
    return {"selected": ordered[0], "reason": deciding, "dominated": dominated, "tuples": tuples}


# I71: the one registry of owner-assumption kinds; every flag, amount type, count and enumeration is generated from it.
OWNER_ASSUMPTIONS = {
    "transfer": ("owner-named transfer", "owner-named transfers"),
    "ceiling": ("O46 provider quota ceiling", "O46 provider quota ceilings"),
}


def assumption_kind(route: dict) -> str:
    """Which owner assumption an assumption-graded route is (O45/2026-10-18 transfer or O46 ceiling; an O88 route is
    measured evidence under O90, not an assumption)."""

    return "ceiling" if route.get("evidenceClass") == "provider_quota_ceiling" else "transfer"


def assumption_kinds_text(conjunction: str = "or", plural: bool = False) -> str:
    """Every assumption kind, named once from the registry ("an owner-named transfer, ... or an O46 ...")."""

    names = [plural_name if plural else (f"an {singular}" if singular[0] in "aeiouAEIOU" else f"a {singular}")
             for singular, plural_name in OWNER_ASSUMPTIONS.values()]
    return ", ".join(names[:-1]) + f" {conjunction} " + names[-1]


def assumption_counts_text(counts: dict) -> str:
    """Rows per assumption kind, in registry order ("26 owner-named transfers, 18 O88 ... and 4 O46 ...")."""

    parts = [f"{counts[kind]} {plural if counts[kind] != 1 else singular}" for kind, (singular, plural) in OWNER_ASSUMPTIONS.items() if counts.get(kind)]
    return ", ".join(parts[:-1]) + (" and " if len(parts) > 1 else "") + parts[-1] if parts else "none"


MEASURED_GRADES = {"controlled", "reports"}


def measured_only_selection(candidates: list[dict]) -> dict:
    """E113: the measured-only view reruns the same selector among measurements (no owner assumption of any kind)."""

    return route_selection([candidate for candidate in candidates if candidate["grade"] in MEASURED_GRADES])


def select_route(candidates: list[dict]) -> dict | None:
    """The official route: after the E88 filter, the greatest comparator tuple; on a complete tie, the first route ID."""

    return route_selection(candidates)["selected"]


def plan_cost(api_cost: float | None, selected: dict | None) -> dict:
    """Plan cost for one row: API basket cost / M, or an API fallback with its flags."""

    if api_cost is None:
        return {"costUsd": None, "fallback": None, "flags": []}
    if selected is None:
        return {
            "costUsd": api_cost,
            "fallback": "api",
            "flags": ["API-cost fallback: no admitted Plan route", "cross-estimand ordering not identified"],
        }
    route = selected["route"]
    flags = []
    if selected["identification"] not in {"point-identified", "set-identified"}:
        flags.append("workload-unmatched")
    kind = assumption_kind(route) if selected["grade"] == "assumption" else None
    if route.get("sameModelAcrossEfforts"):
        flags.append(CROSS_EFFORT_FLAG)
    elif route.get("followsReportPair"):
        flags.append(REPORT_PAIR_FLAG)
    elif kind == "transfer":
        flags.append("owner-named transfer (assumption)")
    if selected["expiry"] in {"possibly-superseded", "expired"}:
        flags.append(selected["expiry"])
    if selected.get("faultWindow"):
        flags.append(FAULT_FLAG)
    # E144: a candidate carries its provenance's (the donor's, for a transfer) valuation and capacity status.
    valuation = selected.get("valuation", valuation_status(route))
    capacity = selected.get("measurementCapacityStatus", measurement_capacity_status(route))
    if valuation == "unverified":
        flags.append("valuation basis unverified")
    if capacity == CAPACITY_CEILING:
        flags.append("provider quota ceiling; full use assumed, the optimistic end on use; credits valued at the recorded API rate, not the highest (O46, O125)")
    elif capacity != CAPACITY_ESTABLISHED:
        flags.append("observed-usage multiple; full utilisation not established")
    return {
        "costUsd": api_cost / comparison_multiple(route),
        "fallback": None,
        "routeId": route["id"],
        "multiple": comparison_multiple(route),
        "grade": selected["grade"],
        "assumptionKind": kind,
        "identification": selected["identification"],
        "measurementCapacityStatus": capacity,
        "mixCheck": selected.get("mixCheck", mix_check(route)),
        "evidenceDate": selected.get("evidenceDate"),
        "donorRouteId": selected.get("donorRouteId"),
        # E144, I82 L2: the donor a release rebased the route from (O95, O96), published only when it was rebased.
        **({"rebasedFrom": route["rebasedFrom"]} if route.get("rebasedFrom") else {}),
        "flags": flags,
    }


def identification_yield(selected_by_row: dict) -> dict:
    """E61/E67: counts of point- and set-identified official routes, and the exploratory label rule."""

    rows = len(selected_by_row)
    point = sum(1 for item in selected_by_row.values() if item and item["identification"] == "point-identified")
    set_identified = sum(1 for item in selected_by_row.values() if item and item["identification"] == "set-identified")
    return {
        "rows": rows,
        "pointIdentified": point,
        "setIdentified": set_identified,
        "unidentified": rows - point - set_identified,
        "exploratory": rows > 0 and 2 * (point + set_identified) < rows,
    }
