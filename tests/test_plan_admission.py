"""Owner decision O81: the build decides O71 plan admission from the report table (E270, O11, O76, O80)."""

from __future__ import annotations

import json
from datetime import date

import pytest

from valuerank import plan_admission as pa
from valuerank.paths import DATA

DAY = date(2026, 10, 25)
PROFILE = {
    "partitionSplits": [{"provider": "A", "date": "2026-10-17T13:00:00Z", "type": "limit"}, {"provider": "O", "date": "2026-10-11", "type": "price"},
                        {"provider": "O", "date": "2026-10-20", "type": "metering"}],
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
    # I79 L2: a weekly reading without a stated start covers the 7 days ending on its date, so one on 2026-10-20 spans the
    # 2026-10-17 split; a 5-hour reading is its own day.
    assert pa.partition(report("g", start=None, end="2026-10-20"), splits) is None
    assert pa.partition(report("g", start=None, end="2026-10-25"), splits) == 1
    assert pa.partition(report("g", start=None, end="2026-10-20", unit="5h"), splits) == 1


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
    assert cells(report("a", start="2026-10-18", end="2026-10-18", low=100), report("b", start="2026-10-19", end="2026-10-19", low=125))[("Pro", "week", "global")]["status"] == "fails: largest lower bound 1.25× the smallest upper bound (O86 allows 1.20×) in the current partition"
    # O86: coarse whole-percent readings 7% apart share a value, though their whole span is 1.23x.
    coarse = cells(report("a", start="2026-10-18", end="2026-10-18", low=7.84, high=9.04), report("b", start="2026-10-19", end="2026-10-19", low=8.40, high=9.68))
    assert coarse[("Pro", "week", "global")]["status"] == "passes"
    # O87: reports at different efforts pool for the model, keyed without the effort suffix.
    reports = [report("a", start="2026-10-18", end="2026-10-18", effort="high"), {**report("b", start="2026-10-19", end="2026-10-19", effort="low"), "modelId": "m-max"}]
    pooled = pa.evaluate({**DOCUMENT, "reports": reports}, PROFILE, DAY, {"m": "M", "m-max": "M"})[0]
    assert (pooled["modelId"], pooled["status"], pooled["efforts"], pooled["configurations"]) == ("M", "passes", ["high", "low"], ["m", "m-max"])
    assert len(pa.evaluate({**DOCUMENT, "reports": reports}, PROFILE, DAY)) == 2  # I69 L2: an ID is never parsed for its effort
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
    pa.check_routes([{**routes[0], "modelIds": ["m-high"]}], cells, {"m-high"}, {"end_user_report"}, {"m-high": "m"})  # O87
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
    assert by[("Google AI Pro", "gemini-4-argon")]["status"] == "fails: largest lower bound 1.35× the smallest upper bound (O86 allows 1.20×) in the current partition"


def test_only_limit_and_price_changes_split_partitions():
    """O99: a metering-only announcement is logged and splits nothing; an untyped or unknown record stops the build."""

    splits = pa.splitting(PROFILE["partitionSplits"])
    assert [item["date"] for item in splits] == ["2026-10-17T13:00:00Z", "2026-10-11"]
    assert pa.partition(report("h", provider="O", start="2026-10-20", end="2026-10-20"), splits) == 1  # no split on the 20th
    # I86 M1: a report measured on a metering-only day is not excluded as spanning a split.
    assert pa.exclusion(report("h", provider="O", start="2026-10-20", end="2026-10-20"), PROFILE, date(2026, 10, 25)) is None
    with pytest.raises(ValueError, match="needs a type"):
        pa.splitting([{"provider": "O", "date": "2026-10-20"}])
    with pytest.raises(ValueError, match="needs a type"):
        pa.splitting([{"provider": "O", "date": "2026-10-20", "type": "rumour"}])


def test_route_change_flags_rest_on_typed_limit_or_price_records():
    """O101, I84 L2: a route's change flag needs a limit or price record for its provider and plan on that date."""

    records = [{"provider": "O", "date": "2026-10-11", "type": "price"}, {"provider": "O", "date": "2026-10-20", "type": "metering"},
               {"provider": "A", "plans": ["Pro"], "date": "2026-10-17T13:00:00Z", "type": "limit"}]
    pa.check_change_flags([{"id": "r1", "provider": "O", "plan": "Plus", "changeDetectedOn": "2026-10-11"},
                           {"id": "r2", "provider": "A", "plan": "Pro", "changeDetectedOn": "2026-10-17"}, {"id": "r3", "provider": "O", "plan": "Plus"}], records)
    for bad in ({"id": "m", "provider": "O", "plan": "Plus", "changeDetectedOn": "2026-10-20"},
                {"id": "p", "provider": "A", "plan": "Max", "changeDetectedOn": "2026-10-17"}):
        with pytest.raises(ValueError, match="no typed limit, price, credit or availability change record"):
            pa.check_change_flags([bad], records)
    # O105: a model-availability record flags the plan's routes but splits nothing.
    availability = [{"provider": "O", "date": "2026-10-22", "type": "availability"}]
    pa.check_change_flags([{"id": "a", "provider": "O", "plan": "Plus", "changeDetectedOn": "2026-10-22"}], availability)
    assert pa.splitting(availability) == []



def test_change_records_produce_their_route_flags():
    """I86 L3, O107, I87 M1 and L1: a controlled route carries the earliest applicable record as its label date, and a
    separate blocking date when the earliest limit or price record from there on differs (null when none); a later limit
    change after an earlier availability record still blocks."""

    records = [{"provider": "O", "date": "2026-10-11", "type": "price"}, {"provider": "O", "date": "2026-10-20", "type": "metering"},
               {"provider": "K", "date": "2026-10-22", "type": "availability"}, {"provider": "O", "date": "2027-01-01", "type": "limit"},
               {"provider": "A", "date": "2026-10-07", "type": "availability"}, {"provider": "A", "date": "2026-10-17T13:00:00Z", "type": "limit"}]
    measured = {"valueMultipleKind": "controlled_account_workload_projection", "sourcePublicationDate": "2026-10-06"}
    day = date(2026, 10, 25)
    good = [{**measured, "id": "o", "provider": "O", "plan": "Plus", "changeDetectedOn": "2026-10-11"},
            {**measured, "id": "k", "provider": "K", "plan": "Pro", "changeDetectedOn": "2026-10-22", "blockingChangeOn": None},
            {**measured, "id": "a", "provider": "A", "plan": "Pro", "changeDetectedOn": "2026-10-07", "blockingChangeOn": "2026-10-17"},
            {**measured, "id": "n", "provider": "N", "plan": "Pro"},
            {"id": "c", "valueMultipleKind": "user_assumption", "provider": "K", "plan": "Pro", "changeDetectedOn": "2026-10-22", "blockingChangeOn": None},
            {"id": "t", "valueMultipleKind": "user_assumption", "provider": "O", "plan": "Plus"}]
    pa.check_change_records(good, records, day)
    for bad, message in (({**good[0], "changeDetectedOn": None}, "must be 2026-10-11"), ({**good[1], "blockingChangeOn": "2026-10-22"}, "must be None"),
                         ({**good[0], "blockingChangeOn": "2026-10-11"}, "must be omitted"), ({**good[2], "blockingChangeOn": None}, "must be 2026-10-17"),
                         ({**good[4], "blockingChangeOn": "x"}, "must be None"), ({**good[5], "blockingChangeOn": None}, "without a change flag"),
                         ({**good[0], "sourcePublicationDate": "2026-11-20"}, "must be None")):
        with pytest.raises(ValueError, match=message):
            pa.check_change_records([bad], records, day)


def test_a_credit_grant_flags_and_blocks_without_splitting():
    """O111: a credit record supports and blocks a flag but splits no partition; O110: a change on the launch day does not
    flag the launched model's measurement."""

    records = [{"provider": "A", "plans": ["Max"], "date": "2026-10-07", "type": "credit"},
               {"provider": "A", "plans": ["Max"], "date": "2026-09-22", "type": "limit"}]
    assert pa.splitting(records) == [records[1]]
    measured = {"valueMultipleKind": "controlled_account_workload_projection", "sourcePublicationDate": "2026-10-06", "modelLaunchedOn": "2026-09-22"}
    pa.check_change_records([{**measured, "id": "m", "provider": "A", "plan": "Max", "changeDetectedOn": "2026-10-07"}], records, date(2026, 10, 25))
    pa.check_change_flags([{"id": "m", "provider": "A", "plan": "Max", "changeDetectedOn": "2026-10-07"}], records)


def test_meter_families_and_resets():
    """O113: a record naming a meter family reaches every plan on it, and an unknown family stops the build; O112: a reading
    spanning a reset day is excluded, and a reset flags and splits nothing."""

    profile = {"meterFamilies": {"C": ["Pro", "Max (tier unstated)"]},
               "partitionSplits": [{"provider": "A", "meterFamily": "C", "date": "2026-10-17", "type": "limit"},
                                   {"provider": "O", "date": "2026-10-07", "type": "reset"}]}
    records = pa.profile_records(profile)
    assert records[0]["plans"] == ["Pro", "Max (tier unstated)"] and pa.splitting(records) == [records[0]]
    assert pa.applies(records[0], {"provider": "A", "plan": "Max (tier unstated)"})
    with pytest.raises(ValueError, match="unknown meter family"):
        pa.profile_records({"partitionSplits": [{"provider": "A", "meterFamily": "X", "date": "2026-10-17", "type": "limit"}]})
    day = date(2026, 10, 25)
    assert pa.exclusion(report("r", provider="O", start="2026-10-06", end="2026-10-07"), profile, day) == "spans a provider meter reset (O112)"
    assert pa.exclusion(report("s", provider="O", start="2026-10-08", end="2026-10-09"), profile, day) is None
    assert pa.spans_reset(report("t", provider="A", start="2026-10-06", end="2026-10-07"), records) is False
