"""Owner decision O81: the build decides O71 plan admission from the report table (E270, O11, O76, O80)."""

from __future__ import annotations

import json
from datetime import date

import pytest

from valuerank import plan_admission as pa
from valuerank.paths import DATA

DAY = date(2026, 10, 25)
PROFILE = {
    "partitionSplits": [{"provider": "A", "date": "2026-10-17T13:00:00Z"}, {"provider": "O", "date": "2026-10-11"}],
    "accountingFaultDays": [{"provider": "O", "days": ["2026-10-16"]}, {"provider": "O", "plans": ["P500"], "days": ["2026-09-29..2026-10-14"]}],
}
DOCUMENT = {"listedPlans": {"Pro": 20, "P500": 500, "Plus": 20}, "speedModeMultipliers": {"O": {"fast": 2.5}}}


def report(identifier, provider="A", plan="Pro", start="2026-10-01", end="2026-10-02", low=100.0, high=None, unit="week", **extra):
    return {"id": identifier, "provider": provider, "plan": plan, "modelId": "m", "observer": identifier, "windowStart": start, "windowEnd": end,
            "unit": unit, "valueLower": low, "valueUpper": high if high is not None else low, **extra}


def test_partitions_follow_instant_and_whole_day_splits():
    splits = PROFILE["partitionSplits"]
    assert pa.partition(report("a", end="2026-10-17T13:00:00Z"), splits) == 0
    assert pa.partition(report("b", start="2026-10-17T13:00:00Z", end="2026-10-18"), splits) == 1
    assert pa.partition(report("c", start="2026-10-17", end="2026-10-18"), splits) is None
    assert pa.partition(report("d", provider="O", start="2026-10-10", end="2026-10-10"), splits) == 0
    assert pa.partition(report("e", provider="O", start="2026-10-11", end="2026-10-11"), splits) is None
    assert pa.partition(report("f", provider="O", start="2026-10-12", end="2026-10-12"), splits) == 1
    assert pa.partition(report("g", start=None, end="2026-10-20"), splits) == 1  # a report without a start is its end day


def test_exclusions_follow_e270():
    for extra, reason in (({"lowerBound": True}, "lower bound"), ({"mixedModel": True}, "mixed-model"), ({"aggregator": True}, "aggregator"),
                          ({"modelId": None}, "model not stated"), ({"modelUnstated": True}, "model not stated"), ({"challenged": True}, "challenged"),
                          ({"tierUnstated": True}, "tier not stated"), ({"derived": True}, "own arithmetic"), ({"anomaly": True}, "anomaly")):
        assert reason in pa.exclusion({**report("x"), **extra}, PROFILE, DAY)
    assert "outside the report window" in pa.exclusion(report("old", start="2026-09-01", end="2026-09-20"), PROFILE, DAY)
    assert "outside the report window" in pa.exclusion(report("late", start="2026-10-26", end="2026-10-27"), PROFILE, DAY)
    assert "accounting-fault day" in pa.exclusion(report("f", provider="O", start="2026-10-16", end="2026-10-16"), PROFILE, DAY)
    assert "accounting-fault day" in pa.exclusion(report("u", provider="O", plan="P500", start="2026-10-12", end="2026-10-12"), PROFILE, DAY)
    assert pa.exclusion(report("ok", provider="O", plan="Plus", start="2026-10-12", end="2026-10-12"), PROFILE, DAY) is None
    assert "spans a partition split" in pa.exclusion(report("s", start="2026-10-17", end="2026-10-18"), PROFILE, DAY)
    assert pa.converted(report("fast", provider="O", low=100, high=110, speedMode="fast"), DOCUMENT["speedModeMultipliers"]) == (250, 275)
    assert pa.converted(report("slow", provider="A", low=100, speedMode="fast"), DOCUMENT["speedModeMultipliers"]) == (100, 100)


def test_cells_pass_only_on_two_firm_concordant_reports_in_the_current_partition():
    def cells(*reports):
        return {(cell["plan"], cell["unit"], cell["region"]): cell for cell in pa.evaluate({**DOCUMENT, "reports": list(reports)}, PROFILE, DAY)}

    passing = cells(report("a", start="2026-10-18", end="2026-10-19", low=100, high=110), report("b", start="2026-10-20", end="2026-10-20", low=105),
                    report("before", end="2026-10-03", low=500), report("p", start="2026-10-21", end="2026-10-21", low=108, provisional=True))[("Pro", "week", "global")]
    assert passing["status"] == "passes" and passing["value"] == pytest.approx(105) and passing["range"] == [100, 110]
    assert passing["admittingObservers"] == ["a", "b"]
    assert passing["monthlyUsd"] == pytest.approx(105 * 4.33) and passing["multiple"] == pytest.approx(105 * 4.33 / 20)
    assert cells(report("a", start="2026-10-18", end="2026-10-18", low=100), report("b", start="2026-10-19", end="2026-10-19", low=125))[("Pro", "week", "global")]["status"] == "fails: range 1.25× over the current partition"
    assert cells(report("a", start="2026-10-18", end="2026-10-18"), report("p", start="2026-10-19", end="2026-10-19", provisional=True))[("Pro", "week", "global")]["status"].startswith("fails: 1 non-provisional")
    assert cells(report("h", unit="5h"))[("Pro", "5h", "global")]["status"] == "fails: a 5-hour figure never converts to a billing period (O82)"
    legacy = cells(report("r", start="2026-10-18", end="2026-10-18", plan="Legacy"), report("s", start="2026-10-19", end="2026-10-19", plan="Legacy"))
    assert legacy[("Legacy", "week", "global")]["status"] == "passes" and legacy[("Legacy", "week", "global")]["listed"] is False
    assert legacy[("Legacy", "week", "global")]["multiple"] is None
    cn = cells(report("cn", region="CN"))[("Pro", "week", "CN")]
    assert cn["status"].startswith("fails: ") and cn["listed"] is False
    monthly = cells(report("m1", start="2026-10-18", end="2026-10-18", unit="month"), report("m2", start="2026-10-19", end="2026-10-19", unit="month"))[("Pro", "month", "global")]
    assert monthly["monthlyUsd"] == pytest.approx(100) and monthly["multiple"] == pytest.approx(5)
    with pytest.raises(ValueError, match="one observer reports twice"):
        cells(report("a", start="2026-10-18", end="2026-10-18"), {**report("b", start="2026-10-19", end="2026-10-19"), "observer": "a"})


def test_a_report_route_needs_a_passing_cell_with_the_same_reports():
    cells = [{"plan": "Pro", "modelId": "m", "status": "passes", "admittingObservers": ["a", "b"]},
             {"plan": "Pro", "modelId": "m", "status": "passes", "admittingObservers": ["c", "d"]}, {"plan": "Max", "modelId": "m", "status": "fails: x"}]
    pair = [{"observer": "b"}, {"observer": "a"}]
    routes = [{"id": "ok", "plan": "Pro", "modelIds": ["m"], "valueMultipleKind": "end_user_report", "independentReports": pair},
              {"id": "other", "plan": "Max", "modelIds": ["outside"], "valueMultipleKind": "end_user_report"},
              {"id": "controlled", "plan": "Max", "modelIds": ["m"], "valueMultipleKind": "controlled_account_workload_projection"}]
    pa.check_routes(routes, cells, {"m"}, {"end_user_report"})
    with pytest.raises(ValueError, match="no passing O71 cell"):
        pa.check_routes(routes[:1], [{**cells[0], "listed": False}], {"m"}, {"end_user_report"})
    pa.check_routes([{**routes[0], "independentReports": [{"observer": "d"}, {"observer": "c"}]}], cells, {"m"}, {"end_user_report"})
    with pytest.raises(ValueError, match="no passing O71 cell supports a report route for m on Max"):
        pa.check_routes([{"id": "bad", "plan": "Max", "modelIds": ["m"], "valueMultipleKind": "end_user_report"}], cells, {"m"}, {"end_user_report"})
    with pytest.raises(ValueError, match="are not a passing cell's admitting reports"):
        pa.check_routes([{"id": "odd", "plan": "Pro", "modelIds": ["m"], "valueMultipleKind": "end_user_report", "independentReports": [{"observer": "c"}, {}]}],
                        cells, {"m"}, {"end_user_report"})


def test_the_committed_report_table_admits_no_cell_today():
    """The O71 outcome: no cohort model × plan has two concordant user reports (stages 1-3)."""

    document = json.loads((DATA / "plan_reports.json").read_text())
    profile = json.loads((DATA / "plan_cost_routes.json").read_text())["evidencePolicy"]["reportEligibilityProfile"]
    cells = pa.evaluate(document, profile, DAY)
    assert cells and not [cell for cell in cells if cell["status"] == "passes"]
    by = {(cell["plan"], cell["modelId"]): cell for cell in cells}
    assert by[("Google AI Pro", "gemini-4-argon")]["status"] == "fails: range 1.71× over the current partition"
