"""Tests for the published diagnostics."""

from __future__ import annotations

import pytest

from valuerank import diagnostics as dg


def test_kendall_tau_b_including_ties():
    assert dg.kendall_tau_b([1, 2, 3], [1, 2, 3]) == pytest.approx(1.0)
    assert dg.kendall_tau_b([1, 2, 3], [3, 2, 1]) == pytest.approx(-1.0)
    # One tie in x and one tie in y.
    tau = dg.kendall_tau_b([1, 1, 2, 3], [1, 2, 3, 3])
    assert tau == pytest.approx(4 / 5)
    assert dg.kendall_tau_b([1, 1], [2, 2]) is None
    assert dg.kendall_tau_b([1, 1, 1], [1, 2, 3]) is None
    with pytest.raises(ValueError):
        dg.kendall_tau_b([1], [1, 2])


def test_bootstrap_tau_interval_and_undefined_panels():
    low, high = dg.bootstrap_tau([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6, 5], draws=300)
    assert -1.0 <= low <= high <= 1.0
    assert dg.bootstrap_tau([1, 1], [2, 2], draws=10) is None


def test_agreement_reports_panel_and_status():
    first = {"a": 1, "b": 2, "c": 3, "d": None, "only-first": 9}
    second = {"a": 1, "b": 2, "c": 3, "d": 4}
    result = dg.agreement(first, second, label="quality agreement")
    assert result["panel"] == ["a", "b", "c"] and result["excluded"] == ["d", "only-first"]
    assert result["tau"] == pytest.approx(1.0) and result["status"] == "defined"
    # Reviewer 72: the mean offset (second minus first) is published beside tau-b, which cannot see a level shift.
    shifted = dg.agreement({"a": 1, "b": 2, "c": 3}, {"a": 3, "b": 4, "c": 5}, label="x")
    assert shifted["tau"] == pytest.approx(1.0) and shifted["meanOffset"] == pytest.approx(2.0)
    small = dg.agreement({"a": 1}, {"a": 1}, label="x")
    assert small["status"] == "undefined (panel too small)" and small["tau"] is None and small["meanOffset"] is None
    flat = dg.agreement({"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 2, "c": 3}, label="x")
    assert flat["status"] == "undefined (no rank variation)" and flat["interval"] is None


def test_workload_crosscheck_thresholds():
    rows = [f"r{i}" for i in range(10)]
    basket = {row: float(i + 1) for i, row in enumerate(rows)}
    aligned = dg.workload_crosscheck(dict(basket), basket, label="DeepSWE")
    assert aligned["warning"] is None and aligned["tau"] == pytest.approx(1.0)
    reversed_order = {row: float(10 - i) for i, row in enumerate(rows)}
    assert dg.workload_crosscheck(reversed_order, basket, label="DeepSWE")["warning"] == "low agreement"
    mixed = {row: float(value) for row, value in zip(rows, [3, 1, 2, 5, 4, 7, 6, 10, 8, 9])}
    result = dg.workload_crosscheck(mixed, basket, label="TB")
    assert result["tau"] >= 0.5 and result["interval"][0] < 0.5 and result["warning"] == "uncertain agreement"
    paired_swaps = {row: float(value) for row, value in zip(rows, [2, 1, 4, 3, 6, 5, 8, 7, 10, 9])}
    assert dg.workload_crosscheck(paired_swaps, basket, label="TB")["warning"] is None
    few = dg.workload_crosscheck({"a": 1, "b": 2}, {"a": 1, "b": 2}, label="TB")
    assert few["warning"] is None and few["status"].startswith("undefined")


def test_cost_per_solve():
    assert dg.cost_per_solve(2.0, 0.5) == 4.0
    assert dg.cost_per_solve(2.0, 0.0) == float("inf")
    assert dg.cost_per_solve(None, 0.5) is None


def test_competition_ranks():
    assert dg.competition_ranks({"a": 1, "b": 1, "c": 3}, lower_is_better=True) == {"a": 1, "b": 1, "c": 3}
    assert dg.competition_ranks({"a": 1, "b": 2}, lower_is_better=False) == {"a": 2, "b": 1}


def test_matched_cost_needs_every_family():
    assert dg.matched_cost({"deepswe": 100.0, "frontiercode": 50.0}, {"deepswe": 3, "frontiercode": 1}) == pytest.approx(87.5)
    assert dg.matched_cost({"deepswe": 100.0}, {"deepswe": 3, "frontiercode": 1}) is None


def test_matched_cost_warnings_reversals_and_ratio_rank_rule():
    rows = [f"r{i}" for i in range(8)]
    basket = {row: 100.0 * (i + 1) for i, row in enumerate(rows)}
    matched = {row: basket[row] * 0.1 for row in rows}
    matched["r0"] = basket["r0"] * 0.1 * 12  # r0 becomes the dearest on the matched workload
    result = dg.matched_cost_warnings(matched, basket)
    warning = result["warnings"]["r0"]
    assert warning["ratioRankWarning"] is True and "r1" in warning["reversals"]
    assert result["warnings"]["r4"]["ratioRankWarning"] is False
    assert dg.matched_cost_warnings({"a": 1.0}, {"a": 1.0}) == {"panel": ["a"], "warnings": {}}


def test_effective_weights_and_non_discriminating_leaves():
    z = {"a": [10, 20, 30], "b": [50, 51, 52], "c": [5, None], "d": [None]}
    weights = {"a": 1.0, "b": 1.0, "c": 1.0, "d": 1.0}
    effective = dg.effective_weights(z, weights)
    assert set(effective) == {"a", "b"} and sum(effective.values()) == pytest.approx(1.0)
    assert dg.non_discriminating(z) == ["b"]
    assert dg.effective_weights({"a": [1, 1]}, {"a": 1.0}) == {}


def test_exposure_shares_by_attribute():
    attributes = {"x": {"execution": "AA"}, "y": {"execution": "AA"}, "z": {"execution": "tbench.ai"}}
    shares = dg.exposure(attributes, {"x": 30, "y": 50, "z": 20}, "execution")
    assert shares == {"AA": pytest.approx(0.8), "tbench.ai": pytest.approx(0.2)}


def test_paired_rank_change_on_the_common_panel():
    baseline = {"a": 90, "b": 80, "c": 70, "gone": 60}
    branch = {"a": 70, "b": 80, "c": 75, "new": 99}
    result = dg.paired_rank_change(baseline, branch)
    assert result["panel"] == ["a", "b", "c"] and result["excluded"] == ["gone", "new"]
    assert result["changes"] == {"a": 2, "b": -1, "c": -1}
    assert result["maxAbsChange"] == 2 and result["maxRow"] == "a"
    empty = dg.paired_rank_change({"a": 1}, {"b": 1})
    assert empty["maxAbsChange"] is None and empty["maxRow"] is None
    cheaper = dg.paired_rank_change({"a": 1.0, "b": 2.0}, {"a": 3.0, "b": 2.0}, higher_is_better=False)
    assert cheaper["changes"] == {"a": 1, "b": -1}


def test_matched_cost_diagnostic_object_and_bridge():
    leaf_map = {"deepswe": "deepswe", "frontierCode": "frontiercode"}
    old = dg.diagnostic_object({"deepswe": 3, "frontiercode": 1}, leaf_map, "first-party list", "frozen before ranks")
    same = dg.diagnostic_object({"frontiercode": 1, "deepswe": 3}, dict(reversed(list(leaf_map.items()))), "first-party list", "frozen before ranks")
    assert old["id"] == same["id"] and old["families"] == ["deepswe", "frontiercode"]
    new = dg.diagnostic_object({"deepswe": 1, "frontiercode": 1}, leaf_map, "first-party list", "frozen before ranks")
    assert new["id"] != old["id"]
    old_costs = {"a": {"deepswe": 100.0, "frontiercode": 50.0}, "b": {"deepswe": 10.0}, "gone": {"deepswe": 1.0, "frontiercode": 1.0}}
    new_costs = {"a": {"deepswe": 120.0, "frontiercode": 50.0}, "b": {"deepswe": 10.0, "frontiercode": 5.0}}
    bridge = dg.matched_cost_bridge(old, new, old_costs, new_costs)
    assert bridge["panel"] == ["a"] and bridge["sameObject"] is False
    row = bridge["rows"]["a"]
    assert row["old"] == pytest.approx(87.5) and row["dataRefresh"] == pytest.approx(15.0)
    assert row["composition"] == pytest.approx(85.0 - 102.5) and row["new"] == pytest.approx(85.0)


def test_group_drift_on_a_common_complete_panel():
    """E114: spread shares against nominal shares renormalised over the same eligible leaves."""

    weights = {"a": 30.0, "b": 10.0, "c": 10.0}
    groups = {"a": "swe", "b": "swe", "c": "knowledge"}
    z = {"a": [10.0, 20.0, 30.0], "b": [50.0, 51.0, 52.0], "c": [0.0, 50.0, 100.0]}
    result = dg.group_drift(z, weights, groups)
    assert result["status"] == "estimated" and result["eligibleLeaves"] == ["a", "c"]
    swe, knowledge = result["groups"]["swe"], result["groups"]["knowledge"]
    assert swe["nominalShare"] == pytest.approx(0.75) and knowledge["nominalShare"] == pytest.approx(0.25)
    assert knowledge["spreadShare"] == pytest.approx(408.248 / (244.949 + 408.248), rel=1e-4)
    assert knowledge["flag"] is True and swe["flag"] is False
    assert result["excludedLeaves"] == ["b"]
    assert dg.group_drift({"a": [1.0, 2.0]}, weights, groups)["status"] == dg.INSUFFICIENT_PANEL
    assert dg.group_drift({"a": [1.0, 2.0, 3.0], "b": [1.0, 2.0]}, weights, groups)["status"] == dg.INSUFFICIENT_PANEL
    # E153: no eligible leaf, or eligible leaves without weight, leave nothing to allocate and raise no flag.
    flat = dg.group_drift({"a": [1.0, 1.0, 1.0]}, weights, groups)
    assert flat["status"] == dg.NO_DISPERSION and flat["groups"] == {} and flat["excludedLeaves"] == ["a"]
    assert dg.group_drift({"a": [10.0, 20.0, 30.0]}, {"a": 0.0}, groups)["status"] == dg.NO_DISPERSION


def test_dispersion_shares_and_covariance_allocation():
    """E153/E81: normalised weighted spread and signed covariance allocation on one common complete panel."""

    weights = {"a": 30.0, "b": 10.0}
    z = {"a": [10.0, 20.0, 30.0], "b": [30.0, 20.0, 10.0]}
    spread = dg.dispersion_shares(z, weights)
    assert spread["status"] == "estimated" and spread["shares"]["a"] == pytest.approx(0.75)
    allocation = dg.covariance_allocation(z, weights)
    assert allocation["status"] == "estimated" and sum(allocation["allocation"].values()) == pytest.approx(1.0)
    assert allocation["allocation"]["b"] < 0  # b moves against the composite
    assert dg.dispersion_shares({"a": [1.0, 2.0]}, weights)["status"] == dg.INSUFFICIENT_PANEL
    assert dg.dispersion_shares({"a": [5.0, 5.0, 5.0]}, weights) == {"status": dg.NO_DISPERSION, "shares": {}}
    assert dg.covariance_allocation({"a": [1.0, 2.0]}, weights)["status"] == dg.INSUFFICIENT_PANEL
    cancel = dg.covariance_allocation({"a": [10.0, 20.0, 30.0], "b": [60.0, 30.0, 0.0]}, weights)
    assert cancel["status"].startswith("not estimable on this panel")
