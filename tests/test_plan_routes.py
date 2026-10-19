"""Tests for v3 Plan route admission, expiry, route choice and Plan cost."""

from __future__ import annotations

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
    assert pr.concordant_pool([10.0, 0, None]) is None


def test_evidence_grades():
    measured = route("a", 50, models=("claude-opus-5-5",), source="Opus 5.5")
    assert pr.evidence_grade(measured, "claude-opus-5-5") == "measured"
    shared_controlled = route("b", 50, models=("x", "y"))
    assert pr.evidence_grade(shared_controlled, "x") == "assumption"
    transfer = route("c", 10, kind="user_assumption", models=("gpt-6.1-sol", "gpt-6-sol"), source="GPT-6.1 Sol", source_kind="controlled_account_workload_projection")
    assert pr.evidence_grade(transfer, "gpt-6.1-sol") == "measured"  # the donor's own measurement
    assert pr.evidence_grade(transfer, "gpt-6-sol") == "assumption"
    report = route("d", 5, kind="user_reported_projection", models=("grok-4.7",), source="Grok 4.7 XHigh")
    assert pr.evidence_grade(report, "grok-4.7") == "diagnostic"
    concordant = dict(report, independentReports=[5.0, 5.5])
    assert pr.evidence_grade(concordant, "grok-4.7") == "measured"
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


def test_select_route_is_lexicographic():
    measured_low = candidate("measured", 8.1, "measured")
    assumption_high = candidate("assumption", 10.8, "assumption")
    assert pr.select_route([assumption_high, measured_low])["route"]["id"] == "measured"
    identified = candidate("identified", 2.0, "assumption", identification="set-identified")
    assert pr.select_route([measured_low, identified])["route"]["id"] == "identified"
    cheaper_fee = candidate("cheap-fee", 8.1, "measured", fee=10)
    assert pr.select_route([measured_low, cheaper_fee])["route"]["id"] == "cheap-fee"
    no_fee = candidate("no-fee", 8.1, "measured", fee=None)
    assert pr.select_route([no_fee, measured_low])["route"]["id"] == "measured"
    assert pr.select_route([candidate("diag", 99, "diagnostic")]) is None
    assert pr.select_route([]) is None


def test_plan_cost_routes_fallbacks_and_flags():
    assert pr.plan_cost(None, None) == {"costUsd": None, "fallback": None, "flags": []}
    fallback = pr.plan_cost(1000.0, None)
    assert fallback["costUsd"] == 1000.0 and fallback["fallback"] == "api"
    assert "cross-estimand ordering not identified" in fallback["flags"]
    selected = candidate("r", 50.0, "assumption", expiry="possibly-superseded")
    result = pr.plan_cost(1000.0, selected)
    assert result["costUsd"] == 20.0 and result["multiple"] == 50.0
    assert result["flags"] == ["workload-unmatched", "owner-named transfer (assumption)", "possibly-superseded"]
    identified = pr.plan_cost(1000.0, candidate("r", 50.0, "measured", identification="point-identified"))
    assert identified["flags"] == [] and identified["identification"] == "point-identified"


def test_identification_yield_and_exploratory_label():
    rows = {
        "a": candidate("a", 1, "measured", identification="point-identified"),
        "b": candidate("b", 1, "measured", identification="set-identified"),
        "c": candidate("c", 1, "assumption"),
        "d": None,
        "e": candidate("e", 1, "assumption"),
    }
    result = pr.identification_yield(rows)
    assert result == {"rows": 5, "pointIdentified": 1, "setIdentified": 1, "unidentified": 3, "exploratory": True}
    assert pr.identification_yield({"a": rows["a"], "b": rows["b"], "c": rows["c"]})["exploratory"] is False
    assert pr.identification_yield({})["exploratory"] is False
