"""Tests for v3 Plan route admission, expiry, route choice and Plan cost."""

from __future__ import annotations

import math
from datetime import date, timedelta

import pytest

from valuerank import plan_routes as pr

TODAY = date(2026, 10, 19)


def route(identifier, multiple, *, kind="controlled_account_workload_projection", models=("m",), fee=20, source=None, source_kind=None, checked="2026-10-10", **extra):
    document = {
        "id": identifier,
        "valueMultiple": multiple,
        "valueMultipleKind": kind,
        "modelIds": list(models),
        "planPriceUsd": fee,
        "checkedOn": checked,
        "sourcePublicationDate": checked,
    }
    if source:
        document["sourceModel"] = source
    if source_kind:
        document["sourceEvidenceClass"] = source_kind
    document.update(extra)
    return document


def test_concordant_pool_checks_unpooled_reports_then_takes_the_geometric_mean():
    assert pr.concordant_pool([10.0, 11.0]) == pytest.approx((10 * 11) ** 0.5)
    assert pr.concordant_pool([10.0, 12.5]) is None  # 1.25 > 1.2
    assert pr.concordant_pool([10.0]) is None
    # E98 boundary: the largest report may be at most 20% above the smallest.
    assert pr.concordant_pool([100.0, 120.0]) is not None and pr.concordant_pool([100.0, 120.001]) is None
    assert pr.concordant_pool([80.0, 120.0]) is None  # within +-20% of 100, but 50% apart
    assert pr.concordant_pool([10.0, 0, None]) is None


def comparable_report(identifier, multiple, **overrides):
    record = {field: "same" for field in pr.COMPARABILITY_FIELDS}
    record.update(overrides)
    return {"id": identifier, "multiple": multiple, "comparability": record}


def test_comparable_groups_and_pooling():
    reports = [
        comparable_report("a", 10.0),
        comparable_report("b", 11.0),
        comparable_report("c", 30.0, measurementWorkload="chat"),
        comparable_report("d", 31.0, measurementWorkload="chat"),
        comparable_report("e", 50.0, valuationBasis=None),
        {"id": "f", "multiple": 12.0},
    ]
    groups, separate = pr.comparable_groups(reports)
    assert [[item["id"] for item in group] for group in groups] == [["a", "b"], ["c", "d"]]
    assert [item["id"] for item in separate] == ["e", "f"]
    pooled = pr.pooled_reports(reports)
    assert pooled["reportIds"] == ["c", "d"] and pooled["multiple"] == pytest.approx((30 * 31) ** 0.5)
    assert pr.pooled_reports([comparable_report("a", 10.0), comparable_report("b", 13.0)]) is None
    assert pr.pooled_reports([]) is None


def test_evidence_grades():
    measured = route("a", 50, models=("claude-opus-5-5",), source="Opus 5.5")
    assert pr.evidence_grade(measured, "claude-opus-5-5") == "controlled"
    shared_controlled = route("b", 50, models=("x", "y"))
    assert pr.evidence_grade(shared_controlled, "x") == "assumption"
    transfer = route("c", 10, kind="user_assumption", models=("gpt-6.1-sol", "gpt-6-sol"), source="GPT-6.1 Sol", source_kind="controlled_account_workload_projection")
    assert pr.evidence_grade(transfer, "gpt-6.1-sol") == "controlled"  # the donor's own measurement
    assert pr.evidence_grade(transfer, "gpt-6-sol") == "assumption"
    report = route("d", 5, kind="user_reported_projection", models=("grok-4.7",), source="Grok 4.7 XHigh")
    assert pr.evidence_grade(report, "grok-4.7") == "diagnostic"
    concordant = dict(report, independentReports=[comparable_report("r1", 5.0), comparable_report("r2", 5.5)])
    assert pr.evidence_grade(concordant, "grok-4.7") == "reports"
    # E102: numerically concordant reports on different measurement workloads are never pooled.
    mixed = dict(report, independentReports=[comparable_report("r1", 5.0), comparable_report("r2", 5.5, measurementWorkload="chat")])
    assert pr.evidence_grade(mixed, "grok-4.7") == "diagnostic"
    assert pr.evidence_grade(route("e", 1, kind="press_claim"), "m") == "diagnostic"


def test_expiry_states():
    assert pr.expiry_status(route("a", 1, checked="2026-10-01"), TODAY) == "fresh"
    assert pr.expiry_status(route("a", 1, checked="2026-09-01"), TODAY) == "possibly-superseded"
    assert pr.expiry_status(route("a", 1, checked="2026-07-01"), TODAY) == "expired"
    assert pr.expiry_status(route("a", 1, checked="2026-05-01"), TODAY) == "demoted"
    undated = route("a", 1)
    del undated["checkedOn"], undated["sourcePublicationDate"]
    assert pr.age_days(undated, TODAY) is None and pr.expiry_status(undated, TODAY) == "fresh"
    assert pr.age_days(dict(undated, validFrom="2026-10-09"), TODAY) == 10


def test_evidence_clock_runs_from_the_observation_never_from_a_record_edit():
    """E144: the measurement window's end, else the publication date, else the authorisation date; checkedOn is editorial."""

    rechecked = route("a", 1, checked="2026-05-01", checkedOn="2026-10-18")
    assert pr.age_days(rechecked, TODAY) == 171 and pr.expiry_status(rechecked, TODAY) == "demoted"
    windowed = route("b", 1, checked="2026-10-15", measurementWindow={"start": "2026-10-01", "end": "2026-10-09"})
    assert pr.evidence_date(windowed) == date(2026, 10, 9) and pr.age_days(windowed, TODAY) == 10
    # I50 M1: an O46 ceiling ages from the read of Xiaomi's pages; re-read unchanged, the clock renews; not re-read, it ages.
    ceiling = route("c", 1, checked="2026-05-01", evidenceClass="provider_quota_ceiling", capturedOn="2026-10-18")
    assert pr.evidence_date(ceiling) == date(2026, 10, 18) and pr.expiry_status(ceiling, TODAY) == "fresh"
    stale = dict(ceiling, capturedOn="2026-05-01")
    assert pr.age_days(stale, TODAY) == 171 and pr.expiry_status(stale, TODAY) == "demoted"


def test_transfers_inherit_their_donor_measurements_clock_and_status():
    """E144: a transfer never outlives its donor; editing or authorising it never restarts the donor's clock."""

    kind = {"kind": "user_assumption", "source": "Opus 5.5", "source_kind": "controlled_account_workload_projection"}
    current = route("donor-current", 50.0, models=("claude-opus-5-5",), checked="2026-10-06")
    expired = route("donor-expired", 50.0, models=("claude-opus-5-5",), checked="2026-07-01")
    demoted = route("donor-demoted", 50.0, models=("claude-opus-5-5",), checked="2026-05-01")
    changed = route("donor-changed", 50.0, models=("claude-opus-5-5",), checked="2026-10-06", changeDetectedOn="2026-10-12")
    later = route("donor-later", 50.0, models=("claude-opus-5-5",), checked="2026-10-06", changeDetectedOn="2026-10-25")
    donors = [current, expired, demoted, changed, later]

    def transfer(donor_id):
        return route(f"t-{donor_id}", 50.0, models=("m",), checked="2026-10-18", donorRouteId=donor_id, **kind)

    def candidate(donor_id):
        (item,) = pr.route_candidates("m", "max", [transfer(donor_id)], TODAY, registry=donors + [transfer(donor_id)])
        return item

    fresh = candidate("donor-current")
    assert (fresh["grade"], fresh["expiry"], fresh["evidenceDate"], fresh["donorRouteId"]) == ("assumption", "fresh", "2026-10-06", "donor-current")
    assert candidate("donor-expired")["expiry"] == "expired"
    gone = candidate("donor-demoted")
    assert (gone["grade"], gone["expiry"]) == ("diagnostic", "demoted")
    assert pr.select_route([gone]) is None
    # A scoped change detected after the donor's observation supersedes both; one after the release day is not yet known.
    assert candidate("donor-changed")["expiry"] == "possibly-superseded"
    assert candidate("donor-later")["expiry"] == "fresh"
    # A newer eligible measurement of the donor replaces the old one by naming it.
    assert candidate("donor-current")["expiry"] == "fresh" and candidate("donor-current")["grade"] == "assumption"
    # Donor chains resolve to the measurement; unknown and circular donors fail the build.
    chained = route("chain", 50.0, models=("m",), donorRouteId="t-donor-demoted", **kind)
    registry = {item["id"]: item for item in donors + [transfer("donor-demoted"), chained]}
    assert pr.donor(chained, registry)["id"] == "donor-demoted"
    with pytest.raises(ValueError, match="unknown donor"):
        pr.donor(transfer("nobody"), {})
    with pytest.raises(ValueError, match="unknown donor"):
        pr.expiry_status(transfer("donor-current"), TODAY)
    loop = {"x": {"id": "x", "donorRouteId": "y"}, "y": {"id": "y", "donorRouteId": "x"}}
    with pytest.raises(ValueError, match="circular"):
        pr.donor(loop["x"], loop)


def test_transfers_take_their_donors_valuation_divisor_and_capacity():
    kind = {"kind": "user_assumption", "source": "Opus 5.5", "source_kind": "controlled_account_workload_projection"}
    different = route("d1", 50.0, models=("claude-opus-5-5",), valuationBasisReconciled=False)
    invalid = route("d2", 0.0, models=("claude-opus-5-5",))
    observed = route("d3", 50.0, models=("claude-opus-5-5",), valuationBasis="release", measurementCapacityStatus=pr.CAPACITY_OBSERVED)
    transfers = [route(f"t{index}", 50.0, models=("m",), donorRouteId=f"d{index}", **kind) for index in (1, 2, 3)]
    registry = [different, invalid, observed] + transfers
    rows = {item["route"]["id"]: item for item in pr.admission_table("m", "max", registry, TODAY)}
    assert (rows["t1"]["case"], rows["t1"]["valuation"], rows["t1"]["officialDisplayEligible"]) == (4, "different", False)
    assert (rows["t2"]["case"], rows["t2"]["grade"]) == (5, "diagnostic")
    assert (rows["t3"]["case"], rows["t3"]["valuation"], rows["t3"]["measurementCapacityStatus"]) == (2, "release", pr.CAPACITY_OBSERVED)
    cost = pr.plan_cost(100.0, rows["t3"])
    assert "observed-usage multiple; full utilisation not established" in cost["flags"] and "valuation basis unverified" not in cost["flags"]
    assert (cost["donorRouteId"], cost["evidenceDate"]) == ("d3", "2026-10-10")


def test_route_candidates_filter_by_model_and_required_variant():
    routes = [
        route("a", 50, models=("m",)),
        route("b", 60, models=("other",)),
        route("c", 70, models=("m",), requiredVariant="xhigh"),
        route("d", 80, models=("m",), checked="2026-04-01"),
    ]
    candidates = pr.route_candidates("m", "max", routes, TODAY)
    assert [item["route"]["id"] for item in candidates] == ["a", "d"]
    assert candidates[1]["grade"] == "diagnostic" and candidates[1]["expiry"] == "demoted"
    assert candidates[0]["identification"] == "unidentified"
    assert [item["route"]["id"] for item in pr.route_candidates("m", "XHigh", routes, TODAY)] == ["a", "c", "d"]
    assert pr.route_candidates("m", None, [route("c", 70, models=("m",), requiredVariant="xhigh")], TODAY) == []


def candidate(identifier, multiple, grade, *, fee=20, identification="unidentified", expiry="fresh"):
    return {"route": route(identifier, multiple, fee=fee), "grade": grade, "identification": identification, "expiry": expiry}


def test_select_route_follows_the_e85_comparator():
    controlled_low = candidate("controlled", 8.1, "controlled")
    assumption_high = candidate("assumption", 10.8, "assumption")
    assert pr.select_route([assumption_high, controlled_low])["route"]["id"] == "controlled"
    reports = candidate("reports", 9.0, "reports")
    assert pr.select_route([reports, assumption_high])["route"]["id"] == "reports"
    assert pr.select_route([reports, controlled_low])["route"]["id"] == "controlled"
    set_identified = {"route": route("set", 2.0, valueMultipleLower=0.5, valueMultipleUpper=3.0), "grade": "assumption", "identification": "set-identified", "expiry": "fresh"}
    point_identified = candidate("point", 1.0, "assumption", identification="point-identified")
    assert pr.select_route([controlled_low, set_identified])["route"]["id"] == "set"
    # Overlapping identified multiples: no certified dominance, so point identification wins.
    assert pr.select_route([set_identified, point_identified])["route"]["id"] == "point"
    cheaper_fee = candidate("cheap-fee", 8.1, "controlled", fee=10)
    assert pr.select_route([controlled_low, cheaper_fee])["route"]["id"] == "cheap-fee"
    no_fee = candidate("no-fee", 8.1, "controlled", fee=None)
    assert pr.select_route([no_fee, controlled_low])["route"]["id"] == "controlled"
    tie_b, tie_a = candidate("b-route", 8.1, "controlled"), candidate("a-route", 8.1, "controlled")
    assert pr.select_route([tie_b, tie_a])["route"]["id"] == "a-route"
    prefix_long, prefix_short = candidate("ab", 8.1, "controlled"), candidate("a", 8.1, "controlled")
    assert pr.select_route([prefix_long, prefix_short])["route"]["id"] == "a"
    assert pr.select_route([candidate("diag", 99, "diagnostic")]) is None
    assert pr.select_route([]) is None


def test_route_selection_publishes_the_deciding_key():
    assert pr.route_selection([])["reason"] == "no eligible route"
    single = pr.route_selection([candidate("only", 5.0, "controlled")])
    assert single["selected"]["route"]["id"] == "only" and single["reason"] == "only remaining eligible route"
    # Unidentified routes at equal grade: the larger observed multiple decides, labelled as such.
    observed = pr.route_selection([candidate("pro", 8.0, "controlled"), candidate("max", 12.0, "controlled")])
    assert observed["selected"]["route"]["id"] == "max" and observed["reason"].startswith("larger observed multiple")
    assert observed["tuples"]["pro"] == (0, 3, 8.0, -20.0)
    lite, top = candidate("lite", 1.0, "controlled"), candidate("top", 1.2, "controlled")
    top["route"]["evidenceClass"] = "provider_quota_ceiling"
    assert pr.route_selection([lite, top])["reason"].startswith("larger quota-ceiling multiple")
    points = pr.route_selection([candidate("a", 8.0, "controlled", identification="point-identified"), candidate("b", 12.0, "controlled", identification="point-identified")])
    assert points["reason"] == "only remaining eligible route" and points["dominated"] == {"a": "b"}
    overlapping = [
        {"route": route(name, 10.0, valueMultipleLower=low, valueMultipleUpper=high), "grade": "controlled", "identification": "set-identified", "expiry": "fresh"}
        for name, low, high in (("a", 8.0, 13.0), ("b", 7.0, 12.0))
    ]
    assert pr.route_selection(overlapping)["reason"] == "larger comparison multiple"
    assert pr.route_selection([candidate("a", 8.0, "controlled"), candidate("b", 9.0, "assumption")])["reason"] == "higher evidence grade"
    assert pr.route_selection([candidate("a", 8.0, "controlled", identification="point-identified"), candidate("b", 9.0, "controlled")])["reason"] == "higher identification class"
    assert pr.route_selection([candidate("a", 8.0, "controlled", fee=10), candidate("b", 8.0, "controlled")])["reason"] == "lower gross cash"
    assert pr.route_selection([candidate("b", 8.0, "controlled"), candidate("a", 8.0, "controlled")])["reason"] == "route ID tie-break"


def test_gross_cash_and_lower_bound_comparison():
    assert pr.gross_cash(route("r", 1, fee=20, additionalCashUsd=5)) == 25.0
    assert pr.gross_cash(route("r", 1, fee=None)) == math.inf
    interval = {"route": route("i", 10.0, valueMultipleLower=6.0), "grade": "controlled", "identification": "set-identified", "expiry": "fresh"}
    assert pr.comparison_tuple(interval)[2] == 6.0
    point = candidate("p", 7.0, "controlled", identification="set-identified")
    assert pr.select_route([interval, point])["route"]["id"] == "p"


def test_dominance_filter_sets_aside_certifiably_dearer_routes():
    point_low = candidate("A", 2.0, "controlled", identification="point-identified")
    set_high = {"route": route("B", 10.5, valueMultipleLower=10.0, valueMultipleUpper=11.0), "grade": "controlled", "identification": "set-identified", "expiry": "fresh"}
    remaining, dominated = pr.dominance_filter([point_low, set_high])
    assert [item["route"]["id"] for item in remaining] == ["B"] and dominated == {"A": "B"}
    assert pr.select_route([point_low, set_high])["route"]["id"] == "B"
    # Losing point identification by an epsilon no longer flips the selection.
    point_ten = candidate("B", 10.0, "controlled", identification="point-identified")
    nearly_point = {"route": route("B", 10.0, valueMultipleLower=10.0, valueMultipleUpper=10.001), "grade": "controlled", "identification": "set-identified", "expiry": "fresh"}
    assert pr.select_route([point_low, point_ten])["route"]["id"] == pr.select_route([point_low, nearly_point])["route"]["id"] == "B"
    # A lower-grade route never sets aside a higher-grade one.
    transfer_high = {"route": route("T", 10.5, valueMultipleLower=10.0, valueMultipleUpper=11.0), "grade": "assumption", "identification": "set-identified", "expiry": "fresh"}
    assert pr.dominance_filter([point_low, transfer_high])[1] == {}
    assert pr.select_route([point_low, transfer_high])["route"]["id"] == "A"
    # Unidentified routes neither filter nor are filtered; a set without a recorded upper bound is never dominated.
    unidentified_high = candidate("U", 100.0, "controlled")
    open_set = {"route": route("S", 3.0, valueMultipleLower=1.0), "grade": "controlled", "identification": "set-identified", "expiry": "fresh"}
    assert pr.dominance_filter([point_low, unidentified_high, open_set])[1] == {}
    assert pr.identified_bounds(open_set) == (1.0, math.inf) and pr.identified_bounds(unidentified_high) is None


def test_plan_cost_routes_fallbacks_and_flags():
    assert pr.plan_cost(None, None) == {"costUsd": None, "fallback": None, "flags": []}
    fallback = pr.plan_cost(1000.0, None)
    assert fallback["costUsd"] == 1000.0 and fallback["fallback"] == "api"
    assert "cross-estimand ordering not identified" in fallback["flags"]
    selected = candidate("r", 50.0, "assumption", expiry="possibly-superseded")
    result = pr.plan_cost(1000.0, selected)
    assert result["costUsd"] == 20.0 and result["multiple"] == 50.0
    assert result["flags"] == ["workload-unmatched", "owner-named transfer (assumption)", "possibly-superseded", "valuation basis unverified"]
    identified = pr.plan_cost(1000.0, {**candidate("r", 50.0, "controlled", identification="point-identified"), "route": route("r", 50.0, valuationBasis="release")})
    assert identified["flags"] == [] and identified["identification"] == "point-identified"
    ranged = {"route": route("s", 50.0, valueMultipleLower=40.0, valueMultipleUpper=60.0), "grade": "controlled", "identification": "set-identified", "expiry": "fresh"}
    assert pr.plan_cost(1000.0, ranged)["costUsd"] == 25.0  # scored at the lower bound (E74)


def test_identification_yield_and_exploratory_label():
    rows = {
        "a": candidate("a", 1, "controlled", identification="point-identified"),
        "b": candidate("b", 1, "controlled", identification="set-identified"),
        "c": candidate("c", 1, "assumption"),
        "d": None,
        "e": candidate("e", 1, "assumption"),
    }
    result = pr.identification_yield(rows)
    assert result == {"rows": 5, "pointIdentified": 1, "setIdentified": 1, "unidentified": 3, "exploratory": True}
    assert pr.identification_yield({"a": rows["a"], "b": rows["b"], "c": rows["c"]})["exploratory"] is False
    assert pr.identification_yield({})["exploratory"] is False


def test_admission_table_classifies_every_route_once():
    routes = [
        route("effort", 9, models=("m",), requiredVariant="xhigh"),
        route("transfer", 9, kind="user_assumption", models=("m", "donor"), source="GPT-6.1 Sol", source_kind="controlled_account_workload_projection"),
        route("unmatched", 9, models=("m",)),
        route("basis", 9, models=("m",), valuationBasisReconciled=False),
        route("single-report", 9, kind="user_reported_projection", models=("m",)),
        route("identified", 9, models=("m",), identification="point-identified", valuationBasis="release"),
        route("other-model", 9, models=("x",)),
    ]
    table = {item["route"]["id"]: item for item in pr.admission_table("m", "max", routes, TODAY)}
    assert set(table) == {"effort", "transfer", "unmatched", "basis", "single-report", "identified"}
    assert {key: item["case"] for key, item in table.items()} == {
        "effort": 1, "transfer": 2, "unmatched": 3, "basis": 4, "single-report": 5, "identified": "identified",
    }
    assert [key for key, item in table.items() if item["officialDisplayEligible"]] == ["transfer", "unmatched", "identified"]
    # O7/E123: the unreconciled price basis never reaches the official selector.
    assert pr.route_candidates("m", "max", [routes[3]], TODAY)[0]["grade"] == "diagnostic"
    assert [key for key, item in table.items() if item["planIntervalEligible"]] == ["identified"]


def test_report_sets_are_tested_whole_and_divisors_are_validated():
    """E107: comparable reports 100, 110 and 150 fail together although 100/110 would pass."""

    reports = [comparable_report("a", 100.0), comparable_report("b", 110.0), comparable_report("c", 150.0)]
    assert pr.pooled_reports(reports) is None
    assert pr.pooled_reports(reports[:2]) is not None
    # E109: a zero, infinite or missing multiple can never be a divisor.
    for bad in (route("zero", 0.0), route("inf", float("inf")), route("lower", 5.0, valueMultipleLower=0.0), route("none", None)):
        assert pr.route_candidates("m", "max", [bad], TODAY)[0]["grade"] == "diagnostic"


def test_measurement_objects_make_route_measurement_pairs():
    """E111: two passing but incomparable partitions become two candidates; the comparator picks between them."""

    reports = [
        comparable_report("a", 10.0), comparable_report("b", 11.0),
        comparable_report("c", 30.0, measurementWorkload="chat"), comparable_report("d", 31.0, measurementWorkload="chat"),
    ]
    base = route("r", 1.0, kind="user_reported_projection", models=("m",), independentReports=reports)
    objects = pr.measurement_objects(base)
    assert [item["id"] for item in objects] == ["r#m1", "r#m2"] and objects[1]["reportIds"] == ["c", "d"]
    candidates = pr.route_candidates("m", "max", [base], TODAY)
    assert [item["grade"] for item in candidates] == ["reports", "reports"]
    selection = pr.route_selection(candidates)
    assert selection["selected"]["route"]["id"] == "r#m2" and selection["selected"]["route"]["routeId"] == "r"
    failing = route("f", 1.0, kind="user_reported_projection", models=("m",), independentReports=[comparable_report("a", 10.0), comparable_report("b", 20.0)])
    assert pr.measurement_objects(failing) == [{**failing, "excludedReportIds": []}]
    assert pr.measurement_objects(route("plain", 5.0)) == [route("plain", 5.0)]


def test_pooled_partitions_age_with_their_contributing_reports():
    """E151: each report keeps its own clock; demoted reports leave the partition before pooling and re-testing."""

    def dated(identifier, multiple, day, **overrides):
        return {**comparable_report(identifier, multiple, **overrides), "measurementWindow": {"start": day, "end": day}}

    fresh_pair = [dated("a", 10.0, "2026-10-12"), dated("b", 11.0, "2026-09-01")]
    base = route("r", 1.0, kind="user_reported_projection", models=("m",), checked="2026-10-15", independentReports=fresh_pair + [dated("old", 30.0, "2026-04-01")])
    (pooled,) = pr.measurement_objects(base, TODAY)
    # The demoted report leaves; the rest pool; the partition takes its most advanced contributor stage.
    assert pooled["reportIds"] == ["a", "b"] and pooled["excludedReportIds"] == ["old"]
    assert pooled["partitionStage"] == "possibly-superseded" and pooled["valueMultiple"] == pytest.approx((10 * 11) ** 0.5)
    (candidate_,) = pr.route_candidates("m", "max", [base], TODAY)
    assert (candidate_["grade"], candidate_["expiry"]) == ("reports", "possibly-superseded")
    # Without a release day nothing is excluded, so the three reports fail concordance as a set.
    assert pr.measurement_objects(base)[0]["excludedReportIds"] == [] and "partitionStage" not in pr.measurement_objects(base)[0]
    # When expiry leaves fewer than two reports the route cannot grade as pooled evidence.
    lonely = route("l", 1.0, kind="user_reported_projection", models=("m",), independentReports=[dated("a", 10.0, "2026-10-12"), dated("gone", 10.5, "2026-04-01")])
    (left,) = pr.route_candidates("m", "max", [lonely], TODAY)
    assert left["grade"] == "diagnostic" and left["route"]["excludedReportIds"] == ["gone"]
    # An undated report ages with the route; a report date counts when no window is stated.
    undated = {**comparable_report("u", 10.0)}
    assert pr.report_stage(undated, route("x", 1, checked="2026-05-01"), TODAY) == "demoted"
    assert pr.report_stage({**undated, "reportDate": "2026-10-18"}, route("x", 1, checked="2026-05-01"), TODAY) == "fresh"
    changed = route("x", 1, checked="2026-10-15", changeDetectedOn="2026-10-16")
    assert pr.report_stage({**undated, "reportDate": "2026-10-14"}, changed, TODAY) == "possibly-superseded"


def test_measured_only_selection_drops_transfers_and_reruns_the_selector():
    """E113: the measured-only view keeps exact-route measurements and reruns selection."""

    transfer = candidate("transfer", 50.0, "assumption")
    measured = candidate("measured", 8.0, "controlled")
    report = candidate("report", 9.0, "reports")
    assert pr.route_selection([transfer, report])["selected"]["route"]["id"] == "report"
    view = pr.measured_only_selection([transfer, measured, report])
    assert view["selected"]["route"]["id"] == "measured"
    assert pr.measured_only_selection([transfer])["selected"] is None


def test_route_selection_is_permutation_invariant():
    """E116: shuffling the admissible-candidate file never changes the selected route-measurement pair."""

    import random as _random

    reports = [comparable_report("a", 10.0), comparable_report("b", 10.0), comparable_report("c", 10.0, measurementWorkload="chat"), comparable_report("d", 10.0, measurementWorkload="chat")]
    base = route("r", 1.0, kind="user_reported_projection", models=("m",), independentReports=reports)
    candidates = pr.route_candidates("m", "max", [base, route("q", 10.0, kind="user_reported_projection", models=("m",), independentReports=reports)], TODAY)
    chosen = {pr.select_route(_random.Random(seed).sample(candidates, len(candidates)))["route"]["id"] for seed in range(20)}
    assert chosen == {"q#m1"}


def test_valuation_status_and_interval_eligibility():
    """E138: release / revalued continue; different is diagnostic; an unrecorded basis is flagged and never interval-eligible."""

    assert pr.valuation_status(route("a", 1)) == "unverified"
    assert pr.valuation_status(route("a", 1, valuationBasis="release")) == "release"
    assert pr.valuation_status(route("a", 1, valuationBasis="revalued")) == "revalued"
    assert pr.valuation_status(route("a", 1, valuationBasis="different")) == "different"
    assert pr.valuation_status(route("a", 1, valuationBasisReconciled=False)) == "different"
    same_multiple = [route("now", 9, models=("m",), identification="point-identified", valuationBasis="release"),
                     route("old", 9, models=("m",), identification="point-identified", valuationBasis="different"),
                     route("unknown", 9, models=("m",), identification="point-identified")]
    table = {item["route"]["id"]: item for item in pr.admission_table("m", "max", same_multiple, TODAY)}
    assert table["now"]["officialDisplayEligible"] and table["now"]["planIntervalEligible"]
    assert table["old"]["case"] == 4 and not table["old"]["officialDisplayEligible"]
    assert table["unknown"]["officialDisplayEligible"] and not table["unknown"]["planIntervalEligible"]


def test_measurement_capacity_status():
    """E139: concordance never upgrades capacity; a recorded status wins."""

    assert pr.measurement_capacity_status(route("c", 50)) == pr.CAPACITY_ESTABLISHED
    transfer = route("t", 10, kind="user_assumption", source_kind="controlled_account_workload_projection")
    assert pr.measurement_capacity_status(transfer) == pr.CAPACITY_ESTABLISHED
    reports = route("r", 5, kind="user_reported_projection", independentReports=[comparable_report("a", 5.0), comparable_report("b", 5.2)])
    assert pr.measurement_capacity_status(reports) == pr.CAPACITY_UNVERIFIED
    assert pr.measurement_capacity_status(dict(reports, measurementCapacityStatus=pr.CAPACITY_OBSERVED)) == pr.CAPACITY_OBSERVED
    assert pr.measurement_capacity_status(dict(reports, measurementCapacityStatus="anything else")) == pr.CAPACITY_UNVERIFIED
    flagged = pr.plan_cost(100.0, {"route": reports, "grade": "reports", "identification": "unidentified", "expiry": "fresh"})
    assert "observed-usage multiple; full utilisation not established" in flagged["flags"]
    assert flagged["measurementCapacityStatus"] == pr.CAPACITY_UNVERIFIED
    ceiling = dict(route("q", 1.18, kind="user_assumption"), evidenceClass="provider_quota_ceiling", valuationBasis="release")
    assert pr.measurement_capacity_status(ceiling) == pr.CAPACITY_CEILING
    capped = pr.plan_cost(100.0, {"route": ceiling, "grade": "assumption", "identification": "unidentified", "expiry": "fresh"})
    assert "provider quota ceiling; full use assumed, the optimistic end on use; credits valued at the recorded API rate, not the highest (O46, O125)" in capped["flags"] and "valuation basis unverified" not in capped["flags"]
    assert not any(flag.startswith("observed-usage") for flag in capped["flags"])
    assert "owner-named transfer (assumption)" not in capped["flags"]
    same = pr.plan_cost(100.0, {"route": dict(route("s", 10.0, kind="user_assumption"), sameModelAcrossEfforts=True), "grade": "assumption", "identification": "unidentified", "expiry": "fresh"})
    assert pr.CROSS_EFFORT_FLAG in same["flags"] and "owner-named transfer (assumption)" not in same["flags"]


def test_expired_routes_leave_selection_before_any_fallback():
    """E142: expiry first, then reselection among survivors; API fallback only when nothing survives."""

    fresh = route("fresh", 8.0, models=("m",))
    stale = route("stale", 50.0, models=("m",), checked="2026-04-01")  # past expiry and grace: demoted
    survivors = pr.route_candidates("m", "max", [stale, fresh], TODAY)
    assert pr.select_route(survivors)["route"]["id"] == "fresh"
    transfer_only = route("transfer", 9.0, kind="user_assumption", models=("m", "donor"), source="GPT-6.1 Sol", source_kind="controlled_account_workload_projection")
    assert pr.select_route(pr.route_candidates("m", "max", [stale, transfer_only], TODAY))["route"]["id"] == "transfer"
    nothing = pr.route_candidates("m", "max", [stale], TODAY)
    assert pr.select_route(nothing) is None and pr.plan_cost(100.0, None)["fallback"] == "api"


def test_report_window_admits_only_reports_dated_inside_it():
    """E194: the window is the 30 days ending at the release cutoff (E213); admitted reports age under E151 instead."""

    def document(*routes, start="2026-09-08", end="2026-10-08"):
        return {"evidencePolicy": {"reportingWindow": {"start": start, "end": end}}, "routes": list(routes)}

    inside = {"id": "r1", "valueMultipleKind": "user_reported_projection", "measurementWindow": {"end": "2026-09-25"}}
    controlled = {"id": "c1", "valueMultipleKind": "controlled_account_workload_projection", "sourcePublicationDate": "2026-01-01"}
    pr.check_report_window(document(inside, controlled))
    old = {"id": "r2", "valueMultipleKind": "end_user_report", "reportDate": "2026-08-01"}
    with pytest.raises(ValueError, match=r"r2: end-user report dated outside the report window 2026-09-08 to 2026-10-08 \(E194\)"):
        pr.check_report_window(document(old))
    pr.check_report_window(document({**old, "admittedOn": "2026-08-05"}))
    pooled = {"id": "p", "valueMultipleKind": "community_observed", "independentReports": [{"id": "p1", "reportDate": "2026-10-01"}, {"id": "p2"}]}
    with pytest.raises(ValueError, match="p2: end-user report dated outside"):
        pr.check_report_window(document(pooled))
    with pytest.raises(ValueError, match="must span 30 days"):
        pr.check_report_window(document(inside, end="2026-10-31"))


def test_only_reports_in_the_current_window_count(monkeypatch):
    """O32: a report older than the current 30-day window stays visible but no longer counts toward pooling."""

    def dated(identifier, multiple, day):
        return {**comparable_report(identifier, multiple), "measurementWindow": {"start": day, "end": day}}

    window = {"start": "2026-09-20", "end": "2026-10-20"}
    pair = [dated("new", 10.0, "2026-10-12"), dated("old", 11.0, "2026-09-01")]  # 41 days apart
    base = route("r", 1.0, kind="user_reported_projection", models=("m",), checked="2026-10-15", independentReports=pair)
    assert pr.measurement_objects(base, TODAY)[0]["reportIds"] == ["new", "old"]  # no window: both pool
    (left,) = pr.route_candidates("m", "max", [base], TODAY, window=window)
    assert left["grade"] == "diagnostic" and left["route"]["excludedReportIds"] == ["old"]
    assert pr.in_window({"id": "x"}, window) is False and pr.in_window({"id": "x"}, None) is True
    assert pr.admission_table("m", "max", [base], TODAY, window)[0]["case"] == 5
    # O127: a pair admitted at an earlier release keeps counting after it leaves the window, ageing on its own clock.
    admitted = route("r", 1.0, kind="user_reported_projection", models=("m",), checked="2026-10-15",
                     independentReports=[{**report, "admittedOn": "2026-10-12"} for report in pair])
    (kept,) = pr.measurement_objects(admitted, TODAY, window)
    assert kept["reportIds"] == ["new", "old"] and kept["excludedReportIds"] == []


def test_a_transfer_from_a_report_donor_follows_the_donors_window_status():
    """O32: a transfer whose donor is an end-user report partition lapses when the donor's reports leave the window."""

    def dated(identifier, multiple, day):
        return {**comparable_report(identifier, multiple), "measurementWindow": {"start": day, "end": day}}

    donor_route = route("donor", 1.0, kind="user_reported_projection", models=("x",), checked="2026-10-15",
                        independentReports=[dated("new", 10.0, "2026-10-12"), dated("old", 11.0, "2026-09-01")])
    transfer = route("t", 10.0, kind="user_assumption", models=("m",), checked="2026-10-18", donorRouteId="donor", sourceEvidenceClass="user_reported_projection")
    assert pr.route_candidates("m", "max", [transfer], TODAY, registry=[transfer, donor_route])[0]["grade"] == "assumption"
    lapsed = pr.route_candidates("m", "max", [transfer], TODAY, registry=[transfer, donor_route], window={"start": "2026-09-20", "end": "2026-10-20"})
    assert lapsed[0]["grade"] == "diagnostic"
    assert pr.report_stage({"id": "u", "sourcePublicationDate": "2026-10-18"}, route("x", 1, checked="2026-05-01"), TODAY) == "fresh"


def test_a_report_starting_before_the_window_is_flagged_window_straddling():
    """E201: a counted report whose measurement started before the window is flagged, not dropped."""

    window = {"start": "2026-09-20", "end": "2026-10-20"}
    straddler = {**comparable_report("s", 10.0), "measurementWindow": {"start": "2026-09-10", "end": "2026-10-01"}}
    inside = {**comparable_report("i", 10.5), "measurementWindow": {"start": "2026-10-01", "end": "2026-10-05"}}
    base = route("r", 1.0, kind="user_reported_projection", models=("m",), checked="2026-10-15", independentReports=[straddler, inside])
    (pooled,) = pr.measurement_objects(base, TODAY, window)
    assert pooled["reportIds"] == ["i", "s"] and pooled["windowStraddlingReportIds"] == ["s"]
    assert pr.straddles(straddler, None) is False and pr.straddles({"id": "x"}, window) is False


def test_the_report_window_includes_both_end_days():
    """E213: the window is the closed day interval [V - 30 days, V]: day 30 before the cutoff is in, day 31 is out."""

    window = {"start": "2026-09-21", "end": "2026-10-21"}
    assert pr.in_window({"id": "a", "reportDate": "2026-09-21"}, window) and pr.in_window({"id": "b", "reportDate": "2026-10-21"}, window)
    assert not pr.in_window({"id": "c", "reportDate": "2026-09-20"}, window)


def test_controlled_measurements_record_their_allocation_regime():
    """E220: AGENTS.md requires SemiAnalysis results to preserve the allocation regime they were measured under."""

    controlled = {"id": "c", "valueMultipleKind": "controlled_account_workload_projection", "allocationRegime": "All-Opus allocation"}
    pr.check_allocation_regimes({"routes": [controlled, {"id": "t", "valueMultipleKind": "user_assumption"}]})
    with pytest.raises(ValueError, match=r"c: a controlled measurement must record its allocation regime \(E220\)"):
        pr.check_allocation_regimes({"routes": [{**controlled, "allocationRegime": " "}]})


def test_selected_providers_cite_only_the_owner_selected_analysis():
    """E238: a newer analysis enters only by the owner's selection; until then a route citing it stops the build."""

    selected = {"providers": ["Anthropic"], "sourceUrl": "https://example.test/selected"}
    routes = [{"id": "m", "provider": "Anthropic", "valueMultipleKind": "controlled_account_workload_projection", "sourceUrl": selected["sourceUrl"]},
              {"id": "t", "provider": "Anthropic", "valueMultipleKind": "user_assumption", "sourceEvidenceId": "semianalysis", "sourceUrl": selected["sourceUrl"]},
              {"id": "x", "provider": "xAI", "valueMultipleKind": "user_reported_projection", "sourceUrl": "https://example.test/other"},
              {"id": "o", "provider": "Anthropic", "valueMultipleKind": "user_assumption", "sourceUrl": None}]
    pr.check_selected_analysis({"evidencePolicy": {"selectedSourceException": selected}, "routes": routes})
    pr.check_selected_analysis({"evidencePolicy": {}, "routes": routes})
    newer = {**routes[0], "sourceUrl": "https://example.test/newer"}
    with pytest.raises(ValueError, match=r"m: cites https://example.test/newer, not the owner-selected analysis https://example.test/selected \(E238\)"):
        pr.check_selected_analysis({"evidencePolicy": {"selectedSourceException": selected}, "routes": [newer]})


def test_pooled_reports_name_distinct_observers_and_no_shared_source():
    """E223: independence is distinct observers and no shared upstream source; calendar spacing is not required."""

    one, two = {"id": "r1", "observer": "alice", "upstreamSource": "post-1"}, {"id": "r2", "observer": "bob", "upstreamSource": "post-2"}
    pr.check_report_independence({"routes": [{"id": "x", "independentReports": [one, two]}, {"id": "y"}]})
    for bad in ([one, {**two, "observer": "alice"}], [one, {**two, "upstreamSource": "post-1"}], [one, {**two, "observer": " "}]):
        with pytest.raises(ValueError, match=r"x: pooled reports must name distinct observers .* \(E223\)"):
            pr.check_report_independence({"routes": [{"id": "x", "independentReports": bad}]})


@pytest.mark.parametrize(("age", "stage"), [(30, "fresh"), (31, "possibly-superseded"), (90, "possibly-superseded"), (91, "expired"), (120, "expired"), (121, "demoted")])
def test_route_ages_are_whole_utc_calendar_days_with_strict_thresholds(age, stage):
    """E212: age = date(V) - observation date in whole UTC calendar days; 'more than N days' is strict."""

    release = date(2026, 10, 21)
    assert pr.expiry_status({"id": "r", "sourcePublicationDate": (release - timedelta(days=age)).isoformat()}, release) == stage


def test_change_flagged_needs_a_detected_change_and_a_superseded_stage():
    """E228: only a detected change (not age alone) marks the selected route's evidence as possibly stale."""

    route = {"id": "r", "changeDetectedOn": "2026-10-15"}
    assert pr.change_flagged({"route": route, "expiry": "possibly-superseded"}) and pr.change_flagged({"route": route, "expiry": "expired"})
    assert not pr.change_flagged({"route": {"id": "r"}, "expiry": "possibly-superseded"})
    assert not pr.change_flagged({"route": route, "expiry": "fresh"}) and not pr.change_flagged(None)


def test_label_denied_adds_hard_expiry_and_fault_windows_to_change_flags():
    """O118, O119: a hard-expired route (in grace) or one measured in a fault window competes but earns no label."""

    route = {"id": "r"}
    assert pr.label_denied({"route": route, "expiry": "expired"}) and pr.label_denied({"route": route, "expiry": "fresh", "faultWindow": {"id": "f"}})
    assert pr.label_denied({"route": {"id": "r", "changeDetectedOn": "2026-10-15"}, "expiry": "possibly-superseded"})
    assert not pr.label_denied({"route": route, "expiry": "possibly-superseded", "faultWindow": None}) and not pr.label_denied(None)


def test_a_report_pair_after_a_detected_change_outranks_the_flagged_controlled_route():
    """O73, O78: a controlled measurement keeps precedence unless a detected change flags it and a report pair dated after
    the change exists; then the report pair wins."""

    controlled = candidate("controlled", 58.9, "controlled", expiry="possibly-superseded")
    controlled["route"].update(changeDetectedOn="2026-10-17", sourcePublicationDate="2026-10-06")
    after = candidate("reports-after", 50.0, "reports")
    after["route"]["sourcePublicationDate"] = "2026-10-20"
    before = candidate("reports-before", 50.0, "reports")
    before["route"]["sourcePublicationDate"] = "2026-10-15"
    assert pr.select_route([controlled, after])["route"]["id"] == "reports-after"
    selection = pr.route_selection([controlled, after])
    assert selection["tuples"]["controlled"][1] == pr.POST_CHANGE_SUPERSEDED and selection["tuples"]["reports-after"][1] == pr.GRADE["reports"]
    # A pair dated before the change, an unflagged controlled route, or no report pair: O73 holds.
    assert pr.select_route([controlled, before])["route"]["id"] == "controlled"
    unflagged = {**controlled, "expiry": "fresh"}
    assert pr.select_route([unflagged, after])["route"]["id"] == "controlled"
    assert pr.select_route([controlled, candidate("assumption", 60.0, "assumption")])["route"]["id"] == "controlled"
    assert "postChangeSuperseded" not in controlled  # the input candidates are not mutated
    # I63 L2: every report of the pair must postdate the change, and the pair must be for the same plan.
    straddling = candidate("reports-straddling", 50.0, "reports")
    straddling["route"]["independentReports"] = [{"sourcePublicationDate": "2026-10-15"}, {"reportDate": "2026-10-20"}]
    assert pr.select_route([controlled, straddling])["route"]["id"] == "controlled"
    later_pair = candidate("reports-pair", 50.0, "reports")
    later_pair["route"]["independentReports"] = [{"measurementWindow": {"end": "2026-10-19"}}, {"reportDate": "2026-10-20"}]
    assert pr.select_route([controlled, later_pair])["route"]["id"] == "reports-pair"
    undated = candidate("reports-undated", 50.0, "reports")
    undated["route"]["reports"] = [{}, {"reportDate": "2026-10-20"}]
    assert pr.select_route([controlled, undated])["route"]["id"] == "controlled"
    other_plan = candidate("reports-other-plan", 50.0, "reports")
    other_plan["route"].update(sourcePublicationDate="2026-10-20", plan="Other plan")
    assert pr.select_route([controlled, other_plan])["route"]["id"] == "controlled"


def test_owner_assumption_kinds_are_named_from_one_registry():
    """I71: every enumeration and count of owner assumptions is generated from OWNER_ASSUMPTIONS."""

    assert pr.assumption_kind({"evidenceClass": "provider_quota_ceiling"}) == "ceiling"
    assert pr.assumption_kind({"sameModelAcrossEfforts": True}) == "transfer" and pr.assumption_kind({}) == "transfer"  # O90: O88 routes are measured
    assert pr.assumption_kinds_text() == "an owner-named transfer or an O46 provider quota ceiling"
    assert pr.assumption_kinds_text("and", plural=True).endswith("and O46 provider quota ceilings")
    assert pr.assumption_counts_text({"transfer": 2, "ceiling": 1}) == "2 owner-named transfers and 1 O46 provider quota ceiling"
    assert pr.assumption_counts_text({"transfer": 1}) == "1 owner-named transfer" and pr.assumption_counts_text({}) == "none"


def test_a_same_model_route_shares_its_donors_precedence():
    """O89, O90, I73 L3: an O88 route is measured evidence ranked between an exact-effort measurement and reports; it outranks
    a report pair, loses to a post-change pair as its donor would, and never outranks an exact-effort measurement."""

    def same_model(identifier, multiple, **extra):
        item = candidate(identifier, multiple, "controlled", **extra)
        item["route"].update(sameModelAcrossEfforts=True, valueMultipleKind="user_assumption", sourceEvidenceClass="controlled_account_workload_projection", sourceModel="Elsewhere")
        return item

    same = same_model("same", 10.0)
    assert pr.evidence_grade(same["route"], "m") == "controlled" and pr.grade_rank(same) == pr.CROSS_EFFORT
    after = candidate("reports-after", 12.0, "reports")
    after["route"]["sourcePublicationDate"] = "2026-10-20"
    assert pr.select_route([same, after])["route"]["id"] == "same"
    flagged = {**same, "expiry": "possibly-superseded", "donorChangeDetectedOn": "2026-10-17"}
    assert pr.select_route([flagged, after])["route"]["id"] == "reports-after"
    exact = candidate("exact", 8.0, "controlled")
    assert pr.select_route([same_model("bigger", 20.0), exact])["route"]["id"] == "exact"
    plain = candidate("transfer", 10.0, "assumption")
    assert pr.select_route([plain, after])["route"]["id"] == "reports-after"


def test_every_route_kind_maps_to_one_admission_case_and_same_model_flags_are_checked():
    """I74 M1, L3: an O88 route is case 3 (measured), a transfer case 2, an exact measurement case 3; the build refuses a
    same-model flag without a controlled donor of the same model on the same plan at another configuration."""

    day = date(2026, 10, 25)
    donor = dict(route("donor", 10.0, models=("m",)), plan="Pro", sourceModel="M")
    same = dict(route("same", 10.0, kind="user_assumption", models=("m-high",)), plan="Pro", sourceModel="M", donorRouteId="donor",
                sameModelAcrossEfforts=True, sourceEvidenceClass="controlled_account_workload_projection")
    transfer = dict(route("transfer", 10.0, kind="user_assumption", models=("m-high",)), plan="Pro", sourceModel="Other", donorRouteId="donor",
                    sourceEvidenceClass="controlled_account_workload_projection")
    table = {row["route"]["id"]: row for row in pr.admission_table("m-high", None, [donor, same, transfer], day)}
    assert (table["same"]["case"], table["same"]["crossEffort"]) == (3, True) and table["transfer"]["case"] == 2
    assert pr.admission_table("m", None, [donor], day)[0]["case"] == 3
    pr.check_same_model_routes({"routes": [donor, same]})
    pr.check_same_model_routes({"routes": [donor, same]}, {"m": "M", "m-high": "M"})
    for bad in ({**same, "donorRouteId": "missing"}, {**same, "plan": "Max"}, {**same, "modelIds": ["other-high"]},
                {**same, "valueMultiple": 99.0}, {**same, "allocationRegime": "another regime"}):
        with pytest.raises(ValueError):
            pr.check_same_model_routes({"routes": [donor, bad]})
    with pytest.raises(ValueError):
        pr.check_same_model_routes({"routes": [donor, same]}, {"m": "M", "m-high": "Not M"})
    # O126: with meters recorded, a cross-effort route needs a tokens or credits meter on its plan.
    tokens = {"evidencePolicy": {"meterDenominations": {"Pro": {"denomination": "tokens"}}}}
    pr.check_same_model_routes({"routes": [donor, same], **tokens})
    with pytest.raises(ValueError, match="no recorded meter denomination"):
        pr.check_same_model_routes({"routes": [donor, same], "evidencePolicy": {"meterDenominations": {}}})
    with pytest.raises(ValueError, match="meters messages"):
        pr.check_same_model_routes({"routes": [donor, same], "evidencePolicy": {"meterDenominations": {"Pro": {"denomination": "messages"}}}})


def test_a_controlled_measurement_in_a_fault_window_is_kept_flagged_until_reports_replace_it():
    """O91, O92: a controlled measurement dated inside an acknowledged fault window for its plan (and every route resting on
    it) stays selected and flagged, and yields to a concordant report pair for the same plan; dating fails closed."""

    faults = [{"provider": "P", "plans": ["Pro"], "days": ["2026-09-29..2026-10-16"], "evidence": "acknowledged"}, {"provider": "P", "days": ["2026-10-20"], "evidence": "day"}]
    measured = dict(route("m", 10.0), provider="P", plan="Pro", sourcePublicationDate="2026-10-06")
    assert pr.in_fault_window(measured, faults)["evidence"] == "acknowledged"
    # Published after the window, but its 30 undated days reach back into it.
    assert pr.in_fault_window({**measured, "sourcePublicationDate": "2026-11-01"}, faults)["evidence"] == "acknowledged"
    assert pr.in_fault_window({**measured, "sourcePublicationDate": "2026-12-31"}, faults) is None
    assert pr.in_fault_window({**measured, "plan": "Plus", "sourcePublicationDate": "2026-12-31"}, faults) is None and pr.in_fault_window({**measured, "provider": "Q"}, faults) is None
    assert pr.in_fault_window({**measured, "measurementWindow": {"start": "2026-10-01", "end": "2026-10-03"}}, faults)["evidence"] == "acknowledged"
    assert pr.in_fault_window({**measured, "plan": "Plus", "measurementWindow": {"start": "2026-10-19", "end": "2026-10-21"}}, faults)["evidence"] == "day"
    assert pr.in_fault_window({**measured, "sourcePublicationDate": None}, faults)["evidence"] == "acknowledged"  # undated: fail closed
    assert pr.in_fault_window(measured, None) is None and pr.in_fault_window(dict(measured, valueMultipleKind="user_assumption"), faults) is None
    day = date(2026, 10, 25)
    [kept] = pr.route_candidates("m", None, [measured], day, faults=faults)
    assert kept["grade"] == "controlled" and kept["faultWindow"] == "acknowledged"
    assert pr.FAULT_FLAG in pr.plan_cost(100.0, kept)["flags"]
    transfer = dict(route("t", 10.0, kind="user_assumption", models=("n",)), provider="P", plan="Pro", donorRouteId="m", sourceEvidenceClass="controlled_account_workload_projection")
    assert pr.route_candidates("n", None, [transfer], day, registry=[measured, transfer], faults=faults)[0]["faultWindow"] == "acknowledged"
    reports = candidate("reports", 5.0, "reports")
    reports["route"]["plan"] = "Pro"
    assert pr.select_route([kept, reports])["route"]["id"] == "reports"
    assert pr.select_route([{**kept, "faultWindow": None}, reports])["route"]["id"] == "m"


def test_change_flag_is_inherited_from_the_donor():
    """I76 L2: a transfer or O88 route whose donor carries a detected change is an E228 blocker like its donor."""

    plain = candidate("t", 10.0, "assumption", expiry="possibly-superseded")
    assert not pr.change_flagged(plain) and pr.change_flagged({**plain, "donorChangeDetectedOn": "2026-10-11"})
    # I77 L2: a change dated after the release cutoff does not count.
    assert not pr.change_flagged({**plain, "donorChangeDetectedOn": "2026-11-01"}, date(2026, 10, 25))
    assert pr.change_flagged({**plain, "donorChangeDetectedOn": "2026-10-11"}, date(2026, 10, 25))


def test_a_change_dated_before_the_measurement_never_supersedes_it():
    """I78 L1, L2: a change before the measurement is no E228 blocker and lets no report pair replace it; a fault-window
    assumption keeps its grade key (it already ranks below reports)."""

    measured = candidate("m", 10.0, "controlled", expiry="possibly-superseded")
    measured.update(evidenceDate="2026-10-06")
    measured["route"].update(changeDetectedOn="2026-10-01")
    assert not pr.change_flagged(measured, date(2026, 10, 25))
    # I79 L1: an undated measurement published 2026-10-06 may have been taken from 2026-09-07, so a change on 2026-10-01 counts.
    assert pr.change_flagged({**measured, "earliestEvidenceDate": "2026-09-07"}, date(2026, 10, 25))
    assert pr.measurement_span({"sourcePublicationDate": "2026-10-06"}) == (date(2026, 9, 7), date(2026, 10, 6))
    after = candidate("reports-after", 5.0, "reports")
    after["route"]["sourcePublicationDate"] = "2026-10-20"
    assert pr.select_route([measured, after])["route"]["id"] == "m"
    transfer = {**candidate("t", 10.0, "assumption"), "faultWindow": "acknowledged"}
    assert pr.post_change_ranks([transfer, after])[0].get("postChangeSuperseded") is None


def test_a_lower_of_transfer_follows_its_donor_to_a_replacing_report_pair():
    """O95: when a report pair replaces a fault-window measurement of its model, a lower-of transfer re-takes the lower of
    the plan's effective figures and names its new donor; the build refuses a stored transfer that is not the lowest."""

    faults = [{"provider": "P", "plans": ["Pro"], "days": ["2026-09-29..2026-10-16"], "evidence": "acknowledged"}]
    sol = dict(route("sol", 10.0, models=("sol",)), provider="P", plan="Pro", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    astra = dict(route("astra", 14.0, models=("astra",)), provider="P", plan="Pro", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    luna = dict(route("luna", 10.0, kind="user_assumption", models=("luna",)), provider="P", plan="Pro", sourceEvidenceId="sa", donorRouteId="sol",
                donorRule="lower-of", sourceEvidenceClass="controlled_account_workload_projection")
    day = date(2026, 10, 25)
    registry = {item["id"]: item for item in (sol, astra, luna)}
    assert pr.rebase_lower_of(luna, registry, day, None, faults) is luna  # no report pair: unchanged
    reports = dict(route("sol-reports", 16.0, kind="user_reported_projection", models=("sol",)), plan="Pro",
                   independentReports=[comparable_report("a", 16.0), comparable_report("b", 16.2)])
    registry["sol-thin"] = dict(route("sol-thin", 30.0, kind="user_reported_projection", models=("sol",)), plan="Pro", independentReports=[comparable_report("a", 30.0)])
    assert pr.effective_measurement(sol, registry, day, None, faults)["id"] == "sol"  # one report admits nothing
    registry["sol-reports"] = reports
    assert pr.effective_measurement(sol, registry, day, None, faults)["id"].startswith("sol-reports")  # its measurement object
    assert pr.effective_measurement(sol, registry, day, None, None)["id"] == "sol"  # no fault, no change: Sol's own measurement stands
    rebased = pr.rebase_lower_of(luna, registry, day, None, faults)
    assert (rebased["donorRouteId"], rebased["valueMultiple"], rebased["rebasedFrom"]) == ("astra", 14.0, "sol")
    assert pr.route_candidates("luna", None, [luna], day, registry=list(registry.values()), faults=faults)[0]["donorRouteId"] == "astra"
    assert pr.rebase_lower_of({**luna, "provider": "Q"}, registry, day, None, faults)["donorRouteId"] == "sol"  # no measured figure on its plan
    changed = {**sol, "changeDetectedOn": "2026-10-01"}
    reports_dated = {**reports, "independentReports": [dict(comparable_report("a", 16.0), reportDate="2026-10-20"), dict(comparable_report("b", 16.2), reportDate="2026-10-21")]}
    assert pr.effective_measurement(changed, {**registry, "sol-reports": reports_dated}, day, None, None)["id"].startswith("sol-reports")
    pr.check_lower_of_routes({"routes": [sol, astra, luna]})
    with pytest.raises(ValueError, match="lowest measured figure"):
        pr.check_lower_of_routes({"routes": [sol, astra, {**luna, "donorRouteId": "astra", "valueMultiple": 14.0}]})


def test_every_transfer_follows_its_donor_and_a_replacing_pair_can_be_the_lowest():
    """O96: a single-donor transfer takes its donor's replacing report pair; I80 L4: when the pair is the plan's lowest
    figure the lower-of transfer names the pair's base route, which donor lookup resolves."""

    faults = [{"provider": "P", "plans": ["Pro"], "days": ["2026-09-29..2026-10-16"], "evidence": "acknowledged"}]
    opus = dict(route("opus", 58.0, models=("opus",)), provider="P", plan="Pro", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    sonnet = dict(route("sonnet", 58.0, kind="user_assumption", models=("sonnet",)), provider="P", plan="Pro", donorRouteId="opus",
                  sourceEvidenceClass="controlled_account_workload_projection")
    low = dict(route("opus-reports", 9.0, kind="user_reported_projection", models=("opus",)), plan="Pro",
               independentReports=[comparable_report("a", 9.0), comparable_report("b", 9.1)])
    day = date(2026, 10, 25)
    registry = {item["id"]: item for item in (opus, sonnet, low)}
    rebased = pr.rebase_transfer(sonnet, registry, day, None, faults)
    assert rebased["donorRouteId"] == "opus-reports" and rebased["valueMultiple"] == pytest.approx(9.05, rel=0.01)
    [candidate_] = pr.route_candidates("sonnet", None, [sonnet], day, registry=list(registry.values()), faults=faults)
    assert candidate_["donorRouteId"] == "opus-reports"
    assert pr.rebase_transfer(sonnet, registry, day, None, None) is sonnet  # no fault, no change: the measurement stands
    assert pr.rebase_transfer({**sonnet, "donorRouteId": "missing"}, registry, day, None, faults)["donorRouteId"] == "missing"
    luna = dict(route("luna", 58.0, kind="user_assumption", models=("luna",)), provider="P", plan="Pro", sourceEvidenceId="sa", donorRouteId="opus",
                donorRule="lower-of", sourceEvidenceClass="controlled_account_workload_projection")
    registry["luna"] = luna
    assert pr.rebase_transfer(luna, registry, day, None, faults)["donorRouteId"] == "opus-reports"


def test_donor_following_uses_the_comparators_replacement_test():
    """I81 L1, I82 L1: the effective figure is the comparator's own selection for the donor model: (a) a change dated before
    the measurement replaces nothing; (b) a report route covers every configuration of the AA family it lists (O87), keyed by
    the families map, whatever its requiredVariant; (c) several replacing pairs are taken in comparator order; (d) a demoted
    measurement is replaced by the only eligible route, the pair, for the donor's row and its followers alike."""

    families = {"opus": "Opus", "opus-high": "Opus", "sonnet": "Sonnet"}
    opus = dict(route("opus", 10.0, models=("opus",)), provider="P", plan="Pro", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06",
                changeDetectedOn="2026-09-01")
    sonnet = dict(route("sonnet", 10.0, kind="user_assumption", models=("sonnet",)), provider="P", plan="Pro", donorRouteId="opus",
                  sourceEvidenceClass="controlled_account_workload_projection")
    dated = [dict(comparable_report("a", 5.0), reportDate="2026-10-20"), dict(comparable_report("b", 5.1), reportDate="2026-10-21")]
    pair = dict(route("opus-reports", 5.0, kind="user_reported_projection", models=("opus-high",)), plan="Pro", independentReports=dated,
                requiredVariant="high")
    day = date(2026, 10, 25)
    registry = {item["id"]: item for item in (opus, sonnet, pair)}
    # (a) earliest day 2026-09-07: the 2026-09-01 change cannot have superseded the measurement.
    assert pr.effective_measurement(opus, registry, day, None, None, families) is opus
    assert pr.rebase_transfer(sonnet, registry, day, None, None, families) is sonnet
    # (b) a change inside the span: the pair registered for opus-high (requiredVariant "high") covers opus, its own row and
    # its follower alike; without the families map it covers only its own configuration (never by parsing IDs).
    changed = {**opus, "changeDetectedOn": "2026-10-01"}
    registry["opus"] = changed
    assert pr.report_covers(pair, "opus", families) == "opus-high" and pr.report_covers(pair, "sonnet", families) is None
    assert pr.report_covers(pair, "opus") is None and pr.report_covers(sonnet, "opus", families) is None
    assert pr.effective_measurement(changed, registry, day, None, None, families)["baseRouteId"] == "opus-reports"
    own = pr.select_route(pr.route_candidates("opus", "max", list(registry.values()), day, families=families))
    assert own["grade"] == "reports" and own["route"]["routeId"] == "opus-reports"
    assert pr.rebase_transfer(sonnet, registry, day, None, None, families)["donorRouteId"] == "opus-reports"
    # (c) a second, larger pair wins on the comparator's multiple key whichever comes first in the registry.
    larger = {**pair, "id": "opus-reports-2", "independentReports": [dict(item, multiple=item["multiple"] * 2) for item in dated]}
    for order in ((larger, pair), (pair, larger)):
        ordered = {"opus": changed, **{item["id"]: item for item in order}}
        assert pr.effective_measurement(changed, ordered, day, None, None, families)["baseRouteId"] == "opus-reports-2"
        assert pr.select_route(pr.route_candidates("opus", None, list(ordered.values()), day, families=families))["route"]["routeId"] == "opus-reports-2"
    # (d) the unchanged measurement once demoted (past grace): the pair is the only eligible route, so every row follows it.
    later = date(2027, 2, 10)
    fresh_pair = {**pair, "independentReports": [dict(item, reportDate="2027-02-05") for item in dated]}
    aged = {"opus": opus, "sonnet": sonnet, "opus-reports": fresh_pair}
    assert pr.route_candidates("opus", None, [opus], later)[0]["grade"] == "diagnostic"
    assert pr.effective_measurement(opus, aged, later, None, None, families)["baseRouteId"] == "opus-reports"
    [follower] = pr.route_candidates("sonnet", None, [sonnet], later, registry=list(aged.values()), families=families)
    assert follower["donorRouteId"] == "opus-reports" and follower["grade"] != "diagnostic"
    assert pr.effective_measurement({**opus, "plan": "Max"}, aged, day, None, None, families)["id"] == "opus"  # no pair on its plan


def test_an_o88_route_following_a_report_pair_takes_the_pairs_grade():
    """O97 (I81 L2): an O88 route rebased onto a replacing report pair is graded "reports", loses the O88 flag and names the
    pair; while its donor measurement stands it keeps O90's measured grade."""

    faults = [{"provider": "P", "plans": ["Pro"], "days": ["2026-09-29..2026-10-16"], "evidence": "acknowledged"}]
    opus = dict(route("opus", 58.0, models=("opus",)), provider="P", plan="Pro", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    high = dict(route("opus-high-same", 58.0, kind="user_assumption", models=("opus-high",)), provider="P", plan="Pro", donorRouteId="opus",
                sameModelAcrossEfforts=True, sourceEvidenceClass="controlled_account_workload_projection", sourceModel=opus.get("sourceModel"))
    pair = dict(route("opus-reports", 30.0, kind="user_reported_projection", models=("opus",)), plan="Pro",
                independentReports=[comparable_report("a", 30.0), comparable_report("b", 31.0)])
    day = date(2026, 10, 25)
    registry = [opus, high, pair]
    [standing] = pr.route_candidates("opus-high", None, [high], day, registry=registry)
    assert standing["grade"] == "controlled" and pr.grade_rank(standing) == pr.CROSS_EFFORT
    [following] = pr.route_candidates("opus-high", None, [high], day, registry=registry, faults=faults)
    assert following["grade"] == "reports" and pr.grade_rank(following) == pr.GRADE["reports"]
    assert following["route"]["followsReportPair"] == "opus-reports" and not following["route"]["sameModelAcrossEfforts"]
    cost = pr.plan_cost(100.0, following)
    assert pr.REPORT_PAIR_FLAG in cost["flags"] and pr.CROSS_EFFORT_FLAG not in cost["flags"] and cost["rebasedFrom"] == "opus"
    assert "rebasedFrom" not in pr.plan_cost(100.0, standing)
    # I82 L2: the follower is the pair's whole measurement object under its own identity, not SemiAnalysis's record.
    assert following["route"]["id"] == "opus-high-same" and following["route"]["modelIds"] == ["opus-high"]
    assert following["route"]["valueMultipleKind"] == pair["valueMultipleKind"] and following["route"]["independentReports"] == pair["independentReports"]
    [entry] = [item for item in pr.admission_table("opus-high", None, registry, day, None, faults) if item["route"]["id"] == "opus-high-same"]
    assert entry["crossEffort"] is False
    # I83 L2: where the pair itself covers the configuration (O87), the follower is the same evidence twice and is dropped;
    # a pair's variant restriction never carries over to a follower.
    families = {"opus": "Opus", "opus-high": "Opus"}
    both = pr.route_candidates("opus-high", "high", registry, day, faults=faults, families=families)
    assert [item["route"].get("routeId", item["route"]["id"]) for item in both if item["grade"] != "controlled"] == ["opus-reports"]
    restricted = pr._rebased(high, {**pair, "requiredVariant": "max", "baseRouteId": "opus-reports"})
    assert "requiredVariant" not in restricted


def test_a_transfer_on_a_report_route_without_a_partition_ages_by_its_own_clock():
    """E151: a donor report route with no surviving partition carries no partition stage, so the age clock decides."""

    reports = dict(route("r", 5.0, kind="user_reported_projection", checked="2026-10-01"), plan="Pro")
    transfer = dict(route("t", 5.0, kind="user_assumption", models=("t",)), plan="Pro", donorRouteId="r")
    assert pr.expiry_status(transfer, date(2026, 10, 25), {"r": reports, "t": transfer}) == "fresh"


def test_a_lower_of_transfer_takes_the_lower_of_the_eligible_figures():
    """O104 (I85 L5): with both measured models demoted and a pair for one, the demoted unreplaced figure drops out of the
    minimum, so the transfer follows the pair whether the pair is larger or smaller; with no eligible figure it stays put."""

    families = {"sol": "Sol", "astra": "Astra", "luna": "Luna"}
    sol = dict(route("sol", 10.0, models=("sol",)), provider="P", plan="Pro", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    astra = dict(route("astra", 8.1, models=("astra",)), provider="P", plan="Pro", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    luna = dict(route("luna", 8.1, kind="user_assumption", models=("luna",)), provider="P", plan="Pro", sourceEvidenceId="sa", donorRouteId="astra",
                donorRule="lower-of", sourceEvidenceClass="controlled_account_workload_projection")
    later = date(2027, 2, 10)
    for multiple in (11.25, 6.24):
        dated = [dict(comparable_report("a", multiple), reportDate="2027-02-05"), dict(comparable_report("b", multiple), reportDate="2027-02-06")]
        pair = dict(route("sol-reports", multiple, kind="user_reported_projection", models=("sol",)), plan="Pro", independentReports=dated)
        registry = {item["id"]: item for item in (sol, astra, luna, pair)}
        rebased = pr.rebase_lower_of(luna, registry, later, None, None, families)
        assert rebased["donorRouteId"] == "sol-reports" and rebased["valueMultiple"] == pytest.approx(multiple)
    registry = {item["id"]: item for item in (sol, astra, luna)}
    assert pr.rebase_lower_of(luna, registry, later, None, None, families) is luna  # every figure demoted, none replaced



def test_an_availability_change_only_prints_the_label():
    """O107: an availability-only flag makes the route possibly superseded but blocks no label and gives no report pair
    precedence."""

    measured = candidate("m", 10.0, "controlled", expiry="possibly-superseded")
    measured["route"].update(changeDetectedOn="2026-10-11", blockingChangeOn=None)
    measured.update(earliestEvidenceDate="2026-09-07")
    assert pr.blocking_change(measured["route"]) is None and not pr.change_flagged(measured, date(2026, 10, 25))
    after = candidate("reports-after", 5.0, "reports")
    after["route"]["independentReports"] = [dict(comparable_report("a", 5.0), reportDate="2026-10-20")]
    assert pr.post_change_ranks([measured, after])[0].get("postChangeSuperseded") is None
    assert pr.blocking_change({"changeDetectedOn": "2026-10-11"}) == "2026-10-11"
    assert pr.blocking_change({"changeDetectedOn": "2026-10-07", "blockingChangeOn": "2026-10-17"}) == "2026-10-17"  # I87 M1


def test_a_lower_of_transfer_skips_a_co_donor_the_comparator_excludes():
    """I86 L2: an unreconcilable or non-divisor co-donor leaves the minimum like a demoted one (O104)."""

    sol = dict(route("sol", 10.55, models=("sol",)), provider="P", plan="Plus", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    astra = dict(route("astra", 8.1, models=("astra",)), provider="P", plan="Plus", sourceEvidenceId="sa", sourcePublicationDate="2026-10-06")
    luna = dict(route("luna", 8.1, kind="user_assumption", models=("luna",)), provider="P", plan="Plus", sourceEvidenceId="sa", donorRouteId="astra",
                donorRule="lower-of", sourceEvidenceClass="controlled_account_workload_projection")
    day = date(2026, 10, 25)
    for excluded in ({**astra, "valuationBasisReconciled": False}, {**astra, "valueMultiple": 0}):
        rebased = pr.rebase_lower_of(luna, {"sol": sol, "astra": excluded, "luna": luna}, day, None, None)
        assert rebased["donorRouteId"] == "sol" and rebased["valueMultiple"] == pytest.approx(10.55)
    assert pr.rebase_lower_of(luna, {"sol": sol, "astra": astra, "luna": luna}, day, None, None) is luna  # Astra stays the lowest


def test_a_measurement_span_is_bounded_by_launch_and_schedule():
    """O110: the span starts no earlier than the model's launch or the stated schedule; a change on that day is part of the
    measured regime, so the change floor is the day after."""

    measured = {"sourcePublicationDate": "2026-10-06"}
    assert pr.measurement_span(measured) == (date(2026, 9, 7), date(2026, 10, 6)) and pr.change_floor(measured) == date(2026, 9, 7)
    launched = {**measured, "modelLaunchedOn": "2026-09-22"}
    assert pr.measurement_span(launched)[0] == date(2026, 9, 22) and pr.change_floor(launched) == date(2026, 9, 23)
    scheduled = {**launched, "scheduleFrom": "2026-09-29"}
    assert pr.change_floor(scheduled) == date(2026, 9, 30)
    early = {**measured, "modelLaunchedOn": "2026-09-01"}
    assert pr.change_floor(early) == date(2026, 9, 7)  # launch before the 30-day span bounds nothing
    assert pr.change_floor({}) is None


def test_a_paywalled_article_needs_a_recent_reread():
    """O130: the selected paywalled article's figure table is re-read each release (within 30 days of it, never after)."""

    day = date(2026, 10, 25)
    assert pr.check_source_rereads({"sourceEvidence": {"open": {}}}, day) is None
    reads = {"paywalled": True, "rereads": [{"readOn": "2026-09-01"}, {"readOn": "2026-10-07"}, {"readOn": "2026-11-01"}]}
    assert pr.check_source_rereads({"sourceEvidence": {"sa": reads}}, day) == "2026-10-07"
    for stale in ({"paywalled": True}, {"paywalled": True, "rereads": [{"readOn": "2026-09-24"}]}, {"paywalled": True, "rereads": [{"readOn": "2026-10-26"}]}):
        with pytest.raises(ValueError, match="O130"):
            pr.check_source_rereads({"sourceEvidence": {"sa": stale}}, day)
    assert pr.check_source_rereads({"sourceEvidence": {"sa": {"paywalled": True, "rereads": [{"readOn": "2026-09-25"}]}}}, day) == "2026-09-25"
