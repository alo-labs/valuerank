"""v3 cost diagnostics: Index figures, basket readiness, the SWE companion and the matched-cost object."""

from __future__ import annotations

import pytest

from valuerank import basket
from valuerank import cost_diagnostics as cd
from valuerank import quality as q

MAIN = "w-main"


def evaluations(cost_per_task: float, *, skip=()) -> list[dict]:
    tasks = {**basket.INDEX_SDLC_TASKS, **basket.INDEX_RESIDUAL_TASKS}
    return [{"slug": slug, "costPerTask": cost_per_task} for slug in tasks if slug not in skip]


def make_row(row_id: str, *, cai=100.0, tb=50.0, index_cost=1.0, workload=MAIN, skip=(), z=50.0, half=0.0, cost=None, complete=True):
    components = {key: {"costUsd": 10.0, "completeness": basket.COMPLETE} for key in basket.INDEX_SDLC_TASKS}
    components["terminalbench-4-0"] = {"costUsd": tb, "completeness": basket.COMPLETE}
    if cai is not None:
        components[basket.CODING_AGENT_INDEX] = {"costUsd": cai, "completeness": basket.COMPLETE if complete else basket.UNRESOLVED}
    admitted = [key for key in components if components[key]["completeness"] == basket.COMPLETE]
    total = cost if cost is not None else sum(components[key]["costUsd"] for key in admitted)
    return {
        "id": row_id,
        "page": {"intelligenceIndexEvaluations": evaluations(index_cost, skip=skip)},
        "components": components,
        "cost": {"workload": workload, "costUsd": total, "lowUsd": total - half, "highUsd": total + half, "components": admitted},
        "evidence": {"observations": {leaf.key: q.Observation(z) for leaf in q.LEAVES}},
    }


def admission(rows):
    components = {component: {"admitted": component not in basket.CHART_COMPONENTS, "available": len(rows), "covered": len(rows)} for component in basket.TARGET_COMPONENTS}
    return {"components": components, "admitted": [key for key, item in components.items() if item["admitted"]]}


def test_index_diagnostics_divide_the_total_by_the_index():
    page = {"intelligenceIndex": 50.0, "intelligenceIndexCost": {"total": 1000.0}, "canonicalIntelligenceIndexTokenCount": {"output": 5}, "outputSpeedVariance": {"median": 70.0}}
    assert cd.index_diagnostics(page) == {
        "intelligenceIndex": 50.0, "indexTotalCostUsd": 1000.0, "usdPerIndexPoint": 20.0, "indexTokens": {"output": 5}, "outputSpeedTokensPerSecond": 70.0,
    }
    assert cd.index_diagnostics({"intelligenceIndex": 0, "intelligenceIndexCost": {"total": 5.0}})["usdPerIndexPoint"] is None
    empty = cd.index_diagnostics({})
    assert empty["usdPerIndexPoint"] is None and empty["indexTotalCostUsd"] is None and empty["outputSpeedTokensPerSecond"] is None


def test_basket_readiness_prices_leaves_by_family_and_reports_concentration():
    rows = [make_row("a"), make_row("b", cai=None), make_row("s", workload="w-subset"), make_row("z", cost=0.0)]
    result = cd.basket_readiness(rows, admission(rows), MAIN)
    agents = result["components"][basket.CODING_AGENT_INDEX]
    assert agents["status"] == "admitted" and agents["tasks"] == 303 and agents["missingConfigurations"] == ["b"]
    assert agents["pricedQualityWeight"] == pytest.approx(0.40)  # DeepSWE 30% and Terminal-Bench 10% run inside it
    assert result["components"]["frontiercode"]["status"] == "pending capture"
    assert result["components"]["frontiercode"]["tasks"] == "chart total (no task count)"
    assert result["components"]["frontiercode"]["missingConfigurations"] == ["a", "b", "s", "z"]
    assert result["components"]["scicode"]["tasks"] == 288 and result["components"]["aa-briefcase"]["pricedQualityWeight"] == 0.0
    assert result["pricedLeaves"] == ["automationBench", "deepswe", "gdpval", "lcr", "scicode", "terminalBench"]
    assert result["pricedMixCoverage"] == pytest.approx(2.0 / 3.0)
    assert set(result["expenditure"]) == {"a", "b"}  # main workload with a positive cost only
    shares = result["expenditure"]["a"]["shares"]
    assert sum(shares.values()) == pytest.approx(1.0) and result["expenditure"]["a"]["hhi"] == pytest.approx(sum(s * s for s in shares.values()))
    assert result["overlap"] == {"terminal-bench-v4": [basket.CODING_AGENT_INDEX, "terminalbench-4-0"]}
    assert result["familyConcentration"] == {basket.CODING_AGENT_INDEX: cd.POOLED}


def test_swe_companion_flags_a_ratio_far_from_the_median():
    rows = [make_row("a"), make_row("b"), make_row("c"), make_row("far", cost=10000.0), make_row("none", cai=None), make_row("s", workload="w-subset")]
    result = cd.swe_companion(rows, MAIN)
    assert set(result["rows"]) == {"a", "b", "c", "far"} and result["unidentified"] == ["none"]
    assert result["rows"]["far"]["flag"] is True and result["rows"]["a"]["flag"] is False
    assert result["rows"]["a"]["cSweUsd"] == pytest.approx(150.0)
    assert cd.swe_companion([make_row("none", cai=None)], MAIN)["medianRatio"] is None


def test_matched_cost_reversals_need_separated_basket_intervals_and_warnings_need_a_rank_gap():
    rows = [make_row(f"r{i}", index_cost=1.0 + i, cai=100.0 * (8 - i)) for i in range(8)]
    rows.append(make_row("overlap", index_cost=1.0, cai=100.0, half=1000.0))
    rows.append(make_row("gap", skip=("critpt",)))
    rows.append(make_row("subset", workload="w-subset"))
    rows.append(make_row("unsolved", index_cost=2.0, z=0.0))
    result = cd.matched_cost(rows, MAIN)
    assert result["status"] == "evaluated" and result["pricedQualityWeight"] == pytest.approx(0.5)
    assert set(result["unpricedLeaves"]) == {"deepswe", "bugHunt", "frontierCode"}
    assert result["unidentified"] == ["gap", "subset"]
    assert sum(result["definition"]["weights"].values()) == pytest.approx(1.0) and len(result["definition"]["id"]) == 16
    # The r-rows price in opposite orders on C^match and C_W; the wide 'overlap' row never forms a reversal.
    assert ["r0", "r7"] in result["reversals"] and not any("overlap" in pair for pair in result["reversals"])
    assert result["warnings"] and all(abs(result["rows"][row]["matchRank"] - result["rows"][row]["basketRank"]) > 3 for row in result["warnings"])
    feasibility = result["feasibility"]
    assert feasibility["r0"]["terminalBench"]["costPerSolvedTaskUsd"] == pytest.approx(66.0 / (66 * 0.5))
    assert feasibility["r0"]["gdpval"]["costPerSolvedTaskUsd"] is None  # an Elo score is not a solved fraction
    assert feasibility["unsolved"]["lcr"]["costPerSolvedTaskUsd"] is None and feasibility["gap"]["critpt"]["passCostUsd"] is None


def test_matched_cost_is_unidentified_below_forty_percent_priced_weight(monkeypatch):
    monkeypatch.setattr(cd, "MATCHED_FAMILIES", {"lcr": cd.MATCHED_FAMILIES["lcr"]})
    result = cd.matched_cost([make_row("a")], MAIN)
    assert result["status"] == "unidentified (priced quality weight below 40%)" and result["rows"] == {} and result["warnings"] == []


def test_matched_cost_without_a_panel_has_no_median():
    empty = cd.matched_cost([make_row("s", workload="w-subset")], MAIN)
    assert empty["status"] == "evaluated" and empty["panel"] == [] and empty["medianRatio"] is None and empty["unidentified"] == ["s"]
