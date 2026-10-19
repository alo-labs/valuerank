"""Tests for Plan capacity under usage windows: semantics, verification, bounds and the release fixtures."""

from __future__ import annotations

import itertools
import math

import pytest

from valuerank import plan_capacity as pc
from valuerank.plan_capacity import Demand, Window

DEMAND = {"output": 1.0}
WORKLOAD = Demand(DEMAND, "workload-pass")


def window(name, length, budget, semantics, **extra):
    return Window(name, length, budget, semantics, burn=extra.pop("burn", {"output": 1.0}), **extra)


def test_window_validation_and_unit_burn():
    with pytest.raises(ValueError, match="invalid window w"):
        Window("w", 0, 1.0, "fixed")
    with pytest.raises(ValueError):
        Window("w", 5, 1.0, "rolling")
    with pytest.raises(ValueError):
        Window("w", 5, -1.0, "fixed")
    w = Window("w", 5, 10.0, "fixed", burn={"input": 0.5, "output": 2.0})
    assert pc.unit_burn(w, {"input": 4.0, "output": 1.0, "cache": 9.0}) == 4.0


def test_release_fixture_two_bursts_one_hour_apart_are_infeasible_six_hours_apart_feasible():
    # 15-minute grid: a 5-hour window is 20 steps; each burst is 60% of the 5-hour cap.
    for semantics in ("session", "sliding"):
        five_hour = window("5h", 20, 100.0, semantics)
        close = [0.0] * 60
        close[0], close[4] = 60.0, 60.0
        assert pc.verify_schedule(close, [five_hour], DEMAND) is False
        apart = [0.0] * 60
        apart[0], apart[24] = 60.0, 60.0
        assert pc.verify_schedule(apart, [five_hour], DEMAND) is True


def test_session_windows_run_back_to_back_and_differ_from_sliding():
    # Session semantics allow a full budget at the end of one session and again at the start of the next.
    session = window("5h", 4, 10.0, "session")
    sliding = window("5h", 4, 10.0, "sliding")
    # A session opened at step 0 ends after step 3, so step 4 opens a fresh session; a sliding window sees 19.
    schedule = [1.0, 0.0, 0.0, 9.0, 10.0, 0.0, 0.0, 0.0]
    assert pc.verify_schedule(schedule, [session], DEMAND) is True
    assert pc.verify_schedule(schedule, [sliding], DEMAND) is False
    # A session starts at first use, not at step 0.
    late = [0.0, 0.0, 0.0, 10.0, 10.0, 0.0, 0.0, 0.0]
    assert pc.verify_schedule(late, [session], DEMAND) is False
    assert pc.greedy_schedule([session], DEMAND, 9) == [10.0, 0, 0, 0, 10.0, 0, 0, 0, 10.0]


def test_fixed_windows_respect_their_phase():
    weekly = window("week", 7, 70.0, "fixed", phase=3)
    schedule = pc.greedy_schedule([weekly], DEMAND, 10)
    assert schedule[:3] == [70.0, 0.0, 0.0] and schedule[3] == 70.0
    assert pc.verify_schedule(schedule, [weekly], DEMAND) is True
    assert pc.verify_schedule([70.0, 1.0] + [0.0] * 8, [weekly], DEMAND) is False


def test_step_limits_negative_amounts_and_free_windows():
    free = window("free", 5, 10.0, "fixed", burn={})
    assert pc.greedy_schedule([free], DEMAND, 3) == [0.0, 0.0, 0.0]
    assert pc.greedy_schedule([free], DEMAND, 3, step_limit=2.0) == [2.0, 2.0, 2.0]
    assert pc.verify_schedule([2.0, 3.0], [free], DEMAND, step_limit=2.0) is False
    assert pc.verify_schedule([-1.0], [free], DEMAND) is False
    assert pc.verify_schedule([5.0, 5.0], [free], DEMAND) is True


def brute_force_optimum(windows, horizon, cap):
    """Exhaustive integer optimum (interval-constraint LPs with integer caps have integral optima)."""

    best = 0
    for schedule in itertools.product(range(cap + 1), repeat=horizon):
        if pc.verify_schedule(list(schedule), windows, DEMAND):
            best = max(best, sum(schedule))
    return best


@pytest.mark.parametrize("semantics", ["fixed", "sliding", "session"])
def test_greedy_matches_the_exhaustive_optimum_on_small_instances(semantics):
    short = window("short", 2, 2.0, semantics)
    long = window("long", 5, 3.0, "fixed" if semantics != "sliding" else "sliding")
    greedy = sum(pc.greedy_schedule([short, long], DEMAND, 6))
    assert greedy == brute_force_optimum([short, long], 6, 2)


def test_capacity_bounds_and_certification():
    weekly = window("week", 672, 1000.0, "fixed")
    five_hour = window("5h", 20, 50.0, "session")
    result = pc.capacity([five_hour, weekly], WORKLOAD, 672 * 4, grid_minutes=15)
    assert result["status"] == "verified"
    assert result["feasibleLowerBound"] == pytest.approx(4000.0)  # the weekly cap binds
    assert result["relaxedUpperBound"] == pytest.approx(4000.0) and result["pointCertified"] is True
    # Loosening the non-binding 5-hour cap cannot change a weekly-binding plan.
    looser = pc.capacity([window("5h", 20, 80.0, "session"), weekly], WORKLOAD, 672 * 4, grid_minutes=15)
    assert looser["feasibleLowerBound"] == pytest.approx(result["feasibleLowerBound"])
    # A tighter quota cannot increase capacity.
    tighter = pc.capacity([five_hour, window("week", 672, 900.0, "fixed")], WORKLOAD, 672 * 4, grid_minutes=15)
    assert tighter["feasibleLowerBound"] <= result["feasibleLowerBound"]


def test_misaligned_fixed_windows_count_their_partial_instances():
    # Horizon 5, length 3, phase 1: steps {0}, {1, 2, 3}, {4} are three instances.
    shifted = window("w", 3, 10.0, "fixed", phase=1)
    assert pc.instance_count(shifted, 5) == 3
    result = pc.capacity([shifted], WORKLOAD, 5, grid_minutes=15)
    assert result["feasibleLowerBound"] == pytest.approx(30.0)
    assert result["relaxedUpperBound"] == pytest.approx(30.0) and result["pointCertified"] is True
    assert pc.instance_count(window("s", 3, 1.0, "sliding"), 5) == 2


def test_capacity_reports_an_interval_when_the_bounds_differ(monkeypatch):
    monkeypatch.setattr(pc, "relaxed_upper_bound", lambda *args, **kwargs: 50.0)
    result = pc.capacity([window("w", 3, 10.0, "fixed")], WORKLOAD, 3, grid_minutes=15)
    assert result["feasibleLowerBound"] == pytest.approx(10.0) and result["relaxedUpperBound"] == 50.0
    assert result["pointCertified"] is False


def test_capacity_unbounded_without_constraints():
    unbounded = pc.capacity([window("free", 3, 1.0, "fixed", burn={})], WORKLOAD, 4, grid_minutes=60)
    assert unbounded["capacityBoundedness"] == "unbounded" and unbounded["relaxedUpperBound"] is None
    assert unbounded["pointCertified"] is False


def test_capacity_marks_an_unverified_schedule_unresolved(monkeypatch):
    monkeypatch.setattr(pc, "greedy_schedule", lambda *args, **kwargs: [999.0])
    result = pc.capacity([window("w", 1, 1.0, "fixed")], WORKLOAD, 1, grid_minutes=15)
    assert result["status"] == "unresolved" and result["feasibleLowerBound"] is None
    assert result["schedule"] is None and result["pointCertified"] is False


def test_value_multiple():
    assert pc.value_multiple(10.0, 30.0, 20.0) == pytest.approx(15.0)
    assert pc.value_multiple(10.0, 30.0, 0.0) is None


def test_a_step_limit_spreads_a_session_budget_across_steps():
    session = window("5h", 4, 10.0, "session")
    schedule = pc.greedy_schedule([session], DEMAND, 6, step_limit=3.0)
    assert schedule == [3.0, 3.0, 3.0, 1.0, 3.0, 3.0]
    assert pc.verify_schedule(schedule, [session], DEMAND, step_limit=3.0) is True


def test_demand_objects_carry_units_and_reconcile_to_cost():
    prices = {"input": 2e-6, "output": 10e-6}
    per_task = {
        "deepswe": Demand({"input": 1000.0, "output": 100.0}, "per-task", "deepswe"),
        "scicode": Demand({"input": 200.0, "output": 50.0}, "per-task", "scicode"),
    }
    passes = [pc.component_pass(per_task["deepswe"], 113), pc.component_pass(per_task["scicode"], 288)]
    assert passes[0].unit == "component-pass" and passes[0].tokens == {"input": 113000.0, "output": 11300.0}
    workload = pc.workload_pass(passes)
    assert workload.unit == "workload-pass"
    # p . d_ie = C_ie for every component and p . d_iW = C_iW.
    assert pc.priced(workload, prices) == pytest.approx(sum(pc.priced(item, prices) for item in passes))
    assert pc.priced(passes[0], prices) == pytest.approx(113 * (1000 * 2e-6 + 100 * 10e-6))
    with pytest.raises(ValueError, match="unknown demand unit"):
        Demand({}, "per-run")
    with pytest.raises(ValueError, match="per-task vector"):
        pc.component_pass(passes[0], 2)
    with pytest.raises(ValueError, match="component-pass vectors"):
        pc.workload_pass([per_task["deepswe"]])


def test_capacity_rejects_a_per_task_vector_whatever_its_entries():
    """E94 units fixture: numerically plausible entries do not make a per-task vector a workload pass."""

    with pytest.raises(ValueError, match="workload-pass demand"):
        pc.capacity([window("w", 3, 10.0, "fixed")], Demand(DEMAND, "per-task"), 3, grid_minutes=15)
