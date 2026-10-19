"""Tests for the SDLC cost basket: component costs, completeness, admission and row cost."""

from __future__ import annotations

import pytest

from valuerank import basket as b

ALL_TASKS = {**b.INDEX_SDLC_TASKS, **b.INDEX_RESIDUAL_TASKS}


def evaluations(cost_per_task: float = 0.5, skip: str | None = None) -> list[dict]:
    return [{"slug": slug, "costPerTask": cost_per_task} for slug in ALL_TASKS if slug != skip]


def published_total(cost_per_task: float = 0.5) -> float:
    return cost_per_task * sum(ALL_TASKS.values())


def test_index_components_reconcile_to_the_published_total():
    components, reconciliation = b.index_components(evaluations(), published_total())
    assert set(components) == set(b.INDEX_SDLC_TASKS)
    assert components["aa-briefcase"]["costUsd"] == pytest.approx(0.5 * 91)
    assert components["aa-briefcase"]["completeness"] == b.COMPLETE
    assert components["scicode"]["detail"] == {"tasks": 288, "costPerTaskUsd": 0.5}
    assert reconciliation["sdlcSevenUsd"] == pytest.approx(0.5 * sum(b.INDEX_SDLC_TASKS.values()))
    assert reconciliation["residualUsd"] == pytest.approx(0.5 * sum(b.INDEX_RESIDUAL_TASKS.values()))
    assert reconciliation["reconciled"] is True and reconciliation["relativeError"] == pytest.approx(0.0)


def test_index_components_unresolved_when_totals_disagree():
    components, reconciliation = b.index_components(evaluations(), published_total() * 1.01)
    assert reconciliation["reconciled"] is False
    assert reconciliation["relativeError"] == pytest.approx(0.01 / 1.01)
    assert {item["completeness"] for item in components.values()} == {b.UNRESOLVED}


def test_index_components_without_a_full_set_or_published_total_cannot_reconcile():
    components, reconciliation = b.index_components(evaluations(skip="critpt"), published_total())
    assert reconciliation["relativeError"] is None and reconciliation["reconciled"] is False
    assert len(components) == 7
    components, reconciliation = b.index_components(evaluations(skip="scicode"), None)
    assert "scicode" not in components and reconciliation["publishedTotalUsd"] is None
    _components, reconciliation = b.index_components(evaluations(), 0)
    assert reconciliation["relativeError"] is None
    _components, reconciliation = b.index_components([{"slug": "aa-briefcase", "costPerTask": None}], 10.0)
    assert reconciliation["sdlcSevenUsd"] == 0


def cai_record(total=303.0, mean=1.0, attempts=(339, 372, 198)):
    return {
        "label": "Codex - GPT (max)",
        "totalCostUsd": total,
        "meanCostPerTaskUsd": mean,
        "pricedTaskCount": None if not mean or total is None else total / mean,
        "components": [{"attempts": count} for count in attempts],
    }


def test_coding_agent_component_prices_the_per_task_metric_over_303_tasks():
    component = b.coding_agent_component(cai_record(total=301.6, mean=1.0))
    assert component["costUsd"] == pytest.approx(303.0) and component["completeness"] == b.COMPLETE
    assert component["configuration"] == "Codex - GPT (max)"
    assert component["detail"] == {
        "meanCostPerTaskUsd": 1.0,
        "requiredTasks": 303,
        "publishedSumUsd": 301.6,
        "sumTaskEquivalent": pytest.approx(301.6),
        "attempts": 909,
        "requiredAttempts": 909,
    }


def test_coding_agent_component_keeps_attempt_coverage_as_a_diagnostic():
    record = cai_record(attempts=(335, 372, 198))
    record["components"].append({"attempts": None})
    component = b.coding_agent_component(record)
    assert component["detail"]["attempts"] == 905
    assert component["completeness"] == b.COMPLETE  # attempt coverage is a precision diagnostic (E53)


def test_coding_agent_component_absent_or_unpriced():
    assert b.coding_agent_component(None) is None
    assert b.coding_agent_component(cai_record(mean=None)) is None
    assert b.coding_agent_component(cai_record(mean=0.0)) is None
    record = cai_record(total=None)
    del record["components"]
    component = b.coding_agent_component(record)
    assert component["detail"]["attempts"] == 0 and component["detail"]["sumTaskEquivalent"] is None


def test_chart_component_rounding_and_declined_marker():
    row = {"model": "GPT-6 Luna (max)", "totalUsdLabel": "$9", "totalUsd": 9, "declinedTasks": False}
    component = b.chart_component(row, source="chart")
    assert component["costUsd"] == 9.0 and component["halfWidthUsd"] == 0.5
    assert component["completeness"] == b.COMPLETE and component["detail"] == {"label": "$9"}
    declined = dict(row, declinedTasks=True)
    assert b.chart_component(declined, source="chart")["completeness"] == b.INCOMPLETE
    assert b.chart_component(None, source="chart") is None
    assert b.chart_component(dict(row, totalUsd=None), source="chart") is None


def test_admitted_components_require_two_thirds_of_ranked_rows():
    ranked = ["a", "b", "c"]
    costs = {
        "a": {b.CODING_AGENT_INDEX: {}, "frontiercode": {}, "scicode": {}},
        "b": {b.CODING_AGENT_INDEX: {}, "scicode": {}},
        "c": {"scicode": {}},
    }
    admitted = b.admitted_components(costs, ranked)
    assert admitted[b.CODING_AGENT_INDEX] == {"admitted": True, "referencePanel": ["a", "b"], "covered": 2, "ranked": 3}
    assert admitted["frontiercode"]["admitted"] is False
    assert admitted["scicode"]["admitted"] is True
    assert admitted["itbench-aa"]["covered"] == 0
    assert set(admitted) == set(b.TARGET_COMPONENTS)


def test_admission_panel_is_joint_and_deterministic():
    """E95: components that pass alone but not together are admitted in coverage order."""

    ranked = ["a", "b", "c", "d", "e", "f"]
    costs = {row: {"scicode": {}} for row in ranked}
    for row in ("a", "b", "c", "d", "e"):
        costs[row][b.CODING_AGENT_INDEX] = {}
    for row in ("b", "c", "d", "e", "f"):
        costs[row]["frontiercode"] = {}
    for row in ("a", "b", "c", "d"):
        costs[row]["itbench-aa"] = {}
    panel = b.admission_panel(costs, ranked)
    assert panel["admissionOrder"][:4] == ["scicode", b.CODING_AGENT_INDEX, "frontiercode", "itbench-aa"]
    components = panel["components"]
    assert components[b.CODING_AGENT_INDEX]["admitted"] is True  # 5/6 jointly with SciCode
    assert components["frontiercode"]["admitted"] is True and components["frontiercode"]["referencePanel"] == ["b", "c", "d", "e"]
    # ITBench alone covers 4/6, but jointly only b, c, d (3/6): pending.
    assert components["itbench-aa"]["covered"] == 4 and components["itbench-aa"]["admitted"] is False
    assert panel["referencePanel"] == ["b", "c", "d", "e"] and panel["jointCovered"] == 4
    assert panel["requiredPanelSize"] == 4 and panel["ranked"] == 6


def test_admitted_components_with_no_ranked_rows():
    admitted = b.admitted_components({}, [])
    assert all(item["admitted"] is False for item in admitted.values())


def test_workload_hash_is_order_independent():
    assert b.workload_hash(["x", "y"]) == b.workload_hash(["y", "x"])
    assert b.workload_hash(["x"]) != b.workload_hash(["x", "y"])
    assert len(b.workload_hash(["x"])) == 16


def comp(cost, half=0.0, status=b.COMPLETE):
    return b.component_cost(cost, half_width=half, completeness=status, source="s")


def test_row_cost_full_subset_partial_and_empty():
    admitted = ["p", "q", "r"]
    full = b.row_cost({"p": comp(10.0), "q": comp(20.0, 0.5), "r": comp(30.0)}, admitted)
    assert full["costUsd"] == 60.0 and (full["lowUsd"], full["highUsd"]) == (59.5, 60.5)
    assert full["fullCost"] is True and full["subset"] is False and full["workload"] == b.workload_hash(admitted)
    subset = b.row_cost({"p": comp(10.0), "r": comp(30.0)}, admitted)
    assert subset["subset"] is True and subset["missingComponents"] == ["q"] and subset["fullCost"] is False
    assert subset["workload"] == b.workload_hash(["p", "r"])
    partial = b.row_cost({"p": comp(10.0), "q": comp(20.0, status=b.INCOMPLETE), "r": comp(30.0)}, admitted)
    assert partial["partialComponents"] == ["q"] and partial["fullCost"] is False and partial["subset"] is False
    empty = b.row_cost({}, admitted)
    assert empty["costUsd"] is None and empty["lowUsd"] is None and empty["workload"] is None and empty["fullCost"] is False


def test_expenditure_shares_and_concentration():
    shares, hhi = b.expenditure_shares({"p": comp(25.0), "q": comp(75.0)}, ["p", "q", "r"])
    assert shares == {"p": 0.25, "q": 0.75}
    assert hhi == pytest.approx(0.625)
    assert b.expenditure_shares({}, ["p"]) == ({}, None)
    assert b.expenditure_shares({"p": comp(0.0)}, ["p"]) == ({}, None)
