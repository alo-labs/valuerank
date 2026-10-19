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
"cross-estimand ordering not identified". Routes certifiably dearer than another
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


def age_days(route: dict, release_day: date) -> int | None:
    stamp = route.get("checkedOn") or route.get("validFrom")
    if not stamp:
        return None
    return (release_day - date.fromisoformat(stamp)).days


def expiry_status(route: dict, release_day: date) -> str:
    """fresh / possibly-superseded (soft expiry) / expired (hard expiry, in grace) / demoted (past grace)."""

    age = age_days(route, release_day)
    if age is None:
        return "fresh"
    if age > HARD_EXPIRY_DAYS + GRACE_DAYS:
        return "demoted"
    if age > HARD_EXPIRY_DAYS:
        return "expired"
    if age > SOFT_EXPIRY_DAYS:
        return "possibly-superseded"
    return "fresh"


def valuation_status(route: dict) -> str:
    """E138: release / revalued / different (O7 price-basis mismatch) / unverified (basis not recorded)."""

    if route.get("valuationBasisReconciled") is False:
        return "different"
    return route.get("valuationBasis") if route.get("valuationBasis") in {"release", "revalued", "different"} else "unverified"


def _divisor_eligible(route: dict) -> bool:
    """E109: every multiple a route can divide by is finite and strictly positive."""

    values = [route.get("valueMultiple")] + [route[key] for key in ("valueMultipleLower", "valueMultipleUpper") if key in route]
    return all(isinstance(value, (int, float)) and not isinstance(value, bool) and 0 < value < math.inf for value in values)


def measurement_objects(route: dict) -> list[dict]:
    """E111: a route's measurement objects — its own measurement, or one per concordant comparable report partition."""

    reports = route.get("independentReports")
    if route.get("valueMultipleKind") not in REPORT_KINDS or not reports:
        return [route]
    groups, _separate = comparable_groups(reports)
    objects = []
    for index, group in enumerate(groups, start=1):
        pooled = concordant_pool([report.get("multiple") for report in group])
        if pooled is not None:
            objects.append({**route, "id": f"{route['id']}#m{index}", "routeId": route["id"], "valueMultiple": pooled, "reportIds": sorted(report["id"] for report in group)})
    return objects or [route]


def route_candidates(model_id: str, configuration_effort: str | None, routes: list[dict], release_day: date) -> list[dict]:
    """Every route-measurement pair for this model, classified; variant-restricted routes need an exact effort match."""

    candidates = []
    for route in [item for base in routes for item in measurement_objects(base)]:
        if model_id not in route.get("modelIds", []):
            continue
        required = route.get("requiredVariant")
        if required is not None and (configuration_effort or "").casefold() != required.casefold():
            continue
        grade = evidence_grade(route, model_id)
        expiry = expiry_status(route, release_day)
        # O7/E123: a measurement on an unreconciled price basis is unmatched; E109: divisors must be positive.
        if expiry == "demoted" or not _divisor_eligible(route) or valuation_status(route) == "different":
            grade = "diagnostic"
        candidates.append(
            {
                "route": route,
                "grade": grade,
                "expiry": expiry,
                "identification": route.get("identification", "unidentified"),
            }
        )
    return candidates


IDENTIFIED = {"point-identified", "set-identified"}


def admission_table(model_id: str, configuration_effort: str | None, routes: list[dict], release_day: date) -> list[dict]:
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
        candidates = route_candidates(model_id, configuration_effort, [route], release_day)
        if not candidates:
            table.append({"route": route, "case": 1, "officialDisplayEligible": False, "targetTransportIdentified": False, "planIntervalEligible": False})
            continue
        for candidate in candidates:
            identified = candidate["identification"] in IDENTIFIED
            if valuation_status(candidate["route"]) == "different":
                case = 4
            elif candidate["grade"] == "diagnostic":
                case = 5
            elif candidate["grade"] == "assumption":
                case = 2
            else:
                case = "identified" if identified else 3
            transport = case == "identified"
            valued = valuation_status(candidate["route"]) in {"release", "revalued"}
            table.append({
                **candidate, "case": case, "valuation": valuation_status(candidate["route"]), "officialDisplayEligible": case not in (4, 5),
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
        GRADE[candidate["grade"]],
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
            if GRADE[winner["grade"]] >= GRADE[loser["grade"]] and winner_bounds[0] > loser_bounds[1]:
                dominated[loser["route"]["id"]] = winner["route"]["id"]
                break
    return [candidate for candidate in candidates if candidate["route"]["id"] not in dominated], dominated


DECIDING_KEYS = ("higher identification class", "higher evidence grade", "larger comparison multiple", "lower gross cash")


def _order(candidate: dict) -> tuple:
    """E85/E116: the comparator keys, then route ID, then the measurement-object ID (a total order)."""

    route = candidate["route"]
    return tuple(-value for value in comparison_tuple(candidate)), route.get("routeId", route["id"]), route["id"]


def route_selection(candidates: list[dict]) -> dict:
    """The official route with its published selection reason, dominated routes and comparison tuples (E85, E88, E93)."""

    eligible = [candidate for candidate in candidates if candidate["grade"] != "diagnostic"]
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
    if selected["grade"] == "assumption":
        flags.append("owner-named transfer (assumption)")
    if selected["expiry"] in {"possibly-superseded", "expired"}:
        flags.append(selected["expiry"])
    if valuation_status(route) == "unverified":
        flags.append("valuation basis unverified")
    return {
        "costUsd": api_cost / comparison_multiple(route),
        "fallback": None,
        "routeId": route["id"],
        "multiple": comparison_multiple(route),
        "grade": selected["grade"],
        "identification": selected["identification"],
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
