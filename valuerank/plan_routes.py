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
from datetime import date

SOFT_EXPIRY_DAYS = 30
HARD_EXPIRY_DAYS = 90
GRACE_DAYS = 30
CONCORDANCE_RATIO = 1.2
CONTROLLED_KINDS = {"controlled_account_workload_projection", "controlled_measurement"}
ASSUMPTION_KINDS = {"user_assumption"}
REPORT_KINDS = {"user_reported_projection", "end_user_report", "community_observed"}
GRADE = {"controlled": 3, "reports": 2, "assumption": 1, "diagnostic": 0}
# O78: a controlled route flagged by a detected change ranks just below a report pair measured after that change.
POST_CHANGE_SUPERSEDED = 1.5


def grade_rank(candidate: dict) -> float:
    """The grade key of the comparator (O73, O78)."""

    return POST_CHANGE_SUPERSEDED if candidate.get("postChangeSuperseded") else GRADE[candidate["grade"]]


def post_change_ranks(candidates: list[dict]) -> list[dict]:
    """O78: when a controlled route carries a detected change (E18) and a report-pair route for the same plan has every
    report dated after that change, the controlled route loses its precedence (O73) to it; the candidates are returned,
    marked, as copies."""

    def earliest_report(route: dict) -> date | None:
        # I63 L2: the pair's own report dates (E194), not the route record's date.
        # I64 L1: a pooled report route carries its reports as independentReports.
        days = [report_date(report) for report in route.get("independentReports") or route.get("reports") or [route]]
        return None if None in days else min(days)

    marked = []
    for candidate in candidates:
        route, changed = candidate["route"], candidate["route"].get("changeDetectedOn")
        superseded = (candidate["grade"] == "controlled" and changed and candidate.get("expiry") in {"possibly-superseded", "expired"}
                      and any(other["grade"] == "reports" and other["route"].get("plan") == route.get("plan")
                              and (earliest_report(other["route"]) or date.min) > date.fromisoformat(changed) for other in candidates))
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
        # The donor model's own route is its measurement; other models carry the owner-named transfer.
        return "controlled" if same_model and source_kind in CONTROLLED_KINDS else "assumption"
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
    age = age_days(source, release_day)
    if age is None:
        return "fresh"
    if age > HARD_EXPIRY_DAYS + GRACE_DAYS:
        return "demoted"
    if age > HARD_EXPIRY_DAYS:
        return "expired"
    changed = source.get("changeDetectedOn")
    if age > SOFT_EXPIRY_DAYS or (changed and evidence_date(source) <= date.fromisoformat(changed) <= release_day):
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

    A report admitted at an earlier release records ``admittedOn``; it stays published as a
    diagnostic until it expires (E151/O13) but no longer counts once it leaves the window (O32).
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


def change_flagged(candidate: dict | None) -> bool:
    """E228: a selected route whose evidence a scoped change (or two reports of a limit change) may have superseded."""

    return bool(candidate and candidate["route"].get("changeDetectedOn") and candidate.get("expiry") in {"possibly-superseded", "expired"})



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
    counted = {report["id"] for report in reports if stages[report["id"]] != "demoted" and in_window(report, window)}
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


def route_candidates(model_id: str, configuration_effort: str | None, routes: list[dict], release_day: date, *, registry: list[dict] | None = None, window: dict | None = None) -> list[dict]:
    """Every route-measurement pair for this model, classified; variant-restricted routes need an exact effort match.

    ``registry`` is the full route list donors are resolved in (default: ``routes``); ``window`` is the
    release's report window (O32).
    """

    by_id = {item["id"]: item for item in (registry if registry is not None else routes)}
    candidates = []
    for route in [item for base in routes for item in measurement_objects(base, release_day, window)]:
        if model_id not in route.get("modelIds", []):
            continue
        required = route.get("requiredVariant")
        if required is not None and (configuration_effort or "").casefold() != required.casefold():
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
                "donorRouteId": source["id"] if source is not None else None,
                # E144: valuation compatibility and capacity status are the donor measurement's for a transfer.
                "valuation": "different" if "different" in {valuation_status(item) for item in checks} else valuation_status(provenance),
                "measurementCapacityStatus": measurement_capacity_status(provenance),
                "mixCheck": mix_check(provenance),
            }
        )
    return candidates


IDENTIFIED = {"point-identified", "set-identified"}


def admission_table(model_id: str, configuration_effort: str | None, routes: list[dict], release_day: date, window: dict | None = None) -> list[dict]:
    """E106/E123: every route-measurement pair naming the model, classified once by case and the three predicates.

    1 execution-identity incompatibility (excluded); 2 owner-named transfer
    (display only, never identifies M_W); 3 exact-route measurement with
    unidentified transport (displayed, interval-ineligible); 4 exact-route
    measurement on an unreconciled price basis (unmatched under O7: diagnostic
    only); 5 evidence failing admission (diagnostic only); and "identified" for
    exact-route measurements with an identified M_W.
    """

    table = []
    for route in routes:
        if model_id not in route.get("modelIds", []):
            continue
        candidates = route_candidates(model_id, configuration_effort, [route], release_day, registry=routes, window=window)
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
                **candidate, "case": case, "officialDisplayEligible": case not in (4, 5),
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
    if deciding == DECIDING_KEYS[2] and ordered[0]["identification"] == "unidentified":
        deciding = "larger observed multiple (observed-workload multiple — target-workload ordering not identified)"
    return {"selected": ordered[0], "reason": deciding, "dominated": dominated, "tuples": tuples}


MEASURED_GRADES = {"controlled", "reports"}


def measured_only_selection(candidates: list[dict]) -> dict:
    """E113: the measured-only view reruns the same selector among exact-route measurements (no transfers)."""

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
    if selected["grade"] == "assumption" and route.get("evidenceClass") != "provider_quota_ceiling":
        flags.append("owner-named transfer (assumption)")
    if selected["expiry"] in {"possibly-superseded", "expired"}:
        flags.append(selected["expiry"])
    # E144: a candidate carries its provenance's (the donor's, for a transfer) valuation and capacity status.
    valuation = selected.get("valuation", valuation_status(route))
    capacity = selected.get("measurementCapacityStatus", measurement_capacity_status(route))
    if valuation == "unverified":
        flags.append("valuation basis unverified")
    if capacity == CAPACITY_CEILING:
        flags.append("provider quota ceiling; full use assumed (O46)")
    elif capacity != CAPACITY_ESTABLISHED:
        flags.append("observed-usage multiple; full utilisation not established")
    return {
        "costUsd": api_cost / comparison_multiple(route),
        "fallback": None,
        "routeId": route["id"],
        "multiple": comparison_multiple(route),
        "grade": selected["grade"],
        "identification": selected["identification"],
        "measurementCapacityStatus": capacity,
        "mixCheck": selected.get("mixCheck", mix_check(route)),
        "evidenceDate": selected.get("evidenceDate"),
        "donorRouteId": selected.get("donorRouteId"),
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
