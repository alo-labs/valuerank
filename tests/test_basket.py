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


def cai_record(total=290.0, mean=1.0, attempts=(300, 372, 198)):
    return {
        "label": "Codex - GPT (max)",
        "totalCostUsd": total,
        "meanCostPerTaskUsd": mean,
        "pricedTaskCount": None if not mean or total is None else total / mean,
        "components": [{"attempts": count} for count in attempts],
    }


def test_coding_agent_component_prices_the_per_task_metric_over_290_tasks():
    """O50: the Coding Agent Index v2.0 (FrontierCode 100, SWE-Atlas-QnA 124, Terminal-Bench 66 tasks)."""

    component = b.coding_agent_component(cai_record(total=288.6, mean=1.0))
    assert component["costUsd"] == pytest.approx(290.0) and component["completeness"] == b.COMPLETE
    assert component["configuration"] == "Codex - GPT (max)"
    assert component["detail"] == {
        "agent": None,
        "meanCostPerTaskUsd": 1.0,
        "requiredTasks": 290,
        "publishedSumUsd": 288.6,
        "sumTaskEquivalent": pytest.approx(288.6),
        "attempts": 870,
        "requiredAttempts": 870,
    }


def test_coding_agent_component_keeps_attempt_coverage_as_a_diagnostic():
    record = cai_record(attempts=(296, 372, 198))
    record["components"].append({"attempts": None})
    component = b.coding_agent_component(record)
    assert component["detail"]["attempts"] == 866
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


FULL = b.component_cost(1.0, source="s")
DECLINED = b.component_cost(1.0, completeness=b.INCOMPLETE, source="s")


def test_admitted_components_require_two_thirds_of_ranked_rows():
    ranked = ["a", "b", "c"]
    costs = {
        "a": {b.CODING_AGENT_INDEX: FULL, "aa-briefcase": FULL, "scicode": FULL},
        "b": {b.CODING_AGENT_INDEX: FULL, "scicode": FULL},
        "c": {"scicode": FULL},
    }
    admitted = b.admitted_components(costs, ranked)
    assert admitted[b.CODING_AGENT_INDEX] == {"admitted": True, "covered": 2, "available": 2, "ranked": 3}
    assert admitted["aa-briefcase"]["admitted"] is False
    assert admitted["scicode"]["admitted"] is True
    assert admitted["itbench-aa"]["covered"] == 0
    assert set(admitted) == set(b.TARGET_COMPONENTS)


def test_frontiercode_stands_in_only_while_the_coding_agent_index_is_not_admitted():
    """O116: FrontierCode's chart total is a unit only in a ranking that has not admitted the Coding Agent Index (never both)."""

    ranked = ["a", "b", "c"]
    pending = {row: {b.FRONTIERCODE: FULL, "scicode": FULL} for row in ranked}
    pending["a"][b.CODING_AGENT_INDEX] = FULL
    panel = b.admission_panel(pending, ranked)
    assert panel["admitted"] == [b.FRONTIERCODE, "scicode"]
    assert panel["components"][b.FRONTIERCODE]["standsInFor"] == b.CODING_AGENT_INDEX and panel["components"][b.FRONTIERCODE]["eligible"]
    both = {row: {b.FRONTIERCODE: FULL, b.CODING_AGENT_INDEX: FULL, "scicode": FULL} for row in ranked}
    panel = b.admission_panel(both, ranked)
    assert panel["admitted"] == [b.CODING_AGENT_INDEX, "scicode"] and not panel["components"][b.FRONTIERCODE]["eligible"]
    assert b.admission_panel({}, [])["components"][b.FRONTIERCODE]["eligible"]


def test_admission_panel_is_joint_and_deterministic():
    """E95: components that pass alone but not together are admitted in coverage order."""

    ranked = ["a", "b", "c", "d", "e", "f"]
    costs = {row: {"scicode": FULL} for row in ranked}
    for row in ("a", "b", "c", "d", "e"):
        costs[row][b.CODING_AGENT_INDEX] = FULL
    for row in ("b", "c", "d", "e", "f"):
        costs[row]["itbench-aa"] = FULL
    for row in ("a", "b", "c", "d"):
        costs[row]["aa-briefcase"] = FULL
    panel = b.admission_panel(costs, ranked)
    components = panel["components"]
    assert components[b.CODING_AGENT_INDEX]["admitted"] is True
    # {CAI, ITBench, SciCode} and {CAI, AA-Briefcase, SciCode} both reach (3 components, 4 rows): target order picks ITBench.
    assert components["itbench-aa"]["admitted"] is True and panel["objective"] == [3, 4] and panel["feasibleAlternatives"] == 11
    # AA-Briefcase alone covers 4/6, but jointly only b, c, d (3/6): pending.
    assert components["aa-briefcase"]["covered"] == 4 and components["aa-briefcase"]["admitted"] is False
    assert panel["referencePanel"] == ["b", "c", "d", "e"] and panel["jointCovered"] == 4
    assert panel["requiredPanelSize"] == 4 and panel["ranked"] == 6


def test_admission_counts_complete_evidence_not_mere_availability():
    """E101 fixture: exact costs for two-thirds of rows, some carrying AA's declined-task marker."""

    ranked = ["a", "b", "c"]
    costs = {"a": {"aa-briefcase": FULL, "scicode": FULL}, "b": {"aa-briefcase": DECLINED, "scicode": FULL}, "c": {"scicode": FULL}}
    panel = b.admission_panel(costs, ranked)
    briefcase = panel["components"]["aa-briefcase"]
    assert briefcase["available"] == 2 and briefcase["covered"] == 1 and briefcase["admitted"] is False
    assert panel["matrices"]["exactCostAvailable"]["b"]["aa-briefcase"] is True
    assert panel["matrices"]["completeCostEvidence"]["b"]["aa-briefcase"] is False
    assert panel["admitted"] == ["scicode"] and panel["exactCostPanel"] == ["a", "b", "c"]


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


def test_admission_enumerates_subsets_instead_of_a_greedy_order():
    """E140 fixture: A on rows 1-5, B and C on rows 1, 2, 3, 6 (N = 6): a greedy coverage order admits only A."""

    ranked = ["1", "2", "3", "4", "5", "6"]
    costs = {row: {} for row in ranked}
    for row in ("1", "2", "3", "4", "5"):
        costs[row][b.CODING_AGENT_INDEX] = FULL
    for row in ("1", "2", "3", "6"):
        costs[row]["aa-briefcase"] = FULL
        costs[row]["itbench-aa"] = FULL
    panel = b.admission_panel(costs, ranked)
    assert panel["admitted"] == ["itbench-aa", "aa-briefcase"] and panel["referencePanel"] == ["1", "2", "3", "6"]
    assert panel["objective"] == [2, 4] and panel["components"][b.CODING_AGENT_INDEX]["admitted"] is False


def test_admission_units_are_the_named_targets_whatever_the_accounting_representation():
    """E148 fixture (N = 6): unit A on rows 1-4; units B and C on rows 3-6; A with B or C covers only rows 3-4.

    Counting units selects B + C. A finer accounting representation of A (its
    sub-benchmarks as children) is not a set of units: it is rejected, so it can
    never outvote B + C.
    """

    ranked = ["1", "2", "3", "4", "5", "6"]
    costs = {row: {} for row in ranked}
    for row in ("1", "2", "3", "4"):
        costs[row][b.CODING_AGENT_INDEX] = FULL
    for row in ("3", "4", "5", "6"):
        costs[row]["aa-briefcase"] = FULL
        costs[row]["itbench-aa"] = FULL
    panel = b.admission_panel(costs, ranked)
    assert panel["admitted"] == ["itbench-aa", "aa-briefcase"] and panel["referencePanel"] == ["3", "4", "5", "6"]
    children = {row: {key: value for key, value in entry.items() if key != b.CODING_AGENT_INDEX} for row, entry in costs.items()}
    for row in ("1", "2", "3", "4"):
        children[row].update({task: FULL for task in b.CODING_AGENT_TASKS})
    with pytest.raises(ValueError, match="not a unit: frontiercode-v1.1-main, swe-atlas-qna, terminal-bench-v4"):
        b.admission_panel(children, ranked)
