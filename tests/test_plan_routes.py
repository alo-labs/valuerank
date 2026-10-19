"""Tests for v3 Plan route admission, expiry, route choice and Plan cost."""

from __future__ import annotations

import math
from datetime import date

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
    del undated["checkedOn"]
    assert pr.age_days(undated, TODAY) is None and pr.expiry_status(undated, TODAY) == "fresh"
    assert pr.age_days(dict(undated, validFrom="2026-10-09"), TODAY) == 10


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
    assert result["flags"] == ["workload-unmatched", "owner-named transfer (assumption)", "possibly-superseded"]
    identified = pr.plan_cost(1000.0, candidate("r", 50.0, "controlled", identification="point-identified"))
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
        route("identified", 9, models=("m",), identification="point-identified"),
        route("other-model", 9, models=("x",)),
    ]
    table = {item["route"]["id"]: item for item in pr.admission_table("m", "max", routes, TODAY)}
    assert set(table) == {"effort", "transfer", "unmatched", "basis", "single-report", "identified"}
    assert {key: item["case"] for key, item in table.items()} == {
        "effort": 1, "transfer": 2, "unmatched": 3, "basis": 4, "single-report": 5, "identified": "identified",
    }
    assert [key for key, item in table.items() if item["officialDisplayEligible"]] == ["transfer", "unmatched", "basis", "identified"]
    assert [key for key, item in table.items() if item["planIntervalEligible"]] == ["identified"]
