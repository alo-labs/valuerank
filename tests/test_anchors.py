"""Tests for frozen anchors, cost scores, the clip gate and the exchange-rate disclosures."""

from __future__ import annotations

import math

import pytest

from valuerank import anchors as a

REFERENCE = {"cheap": 100.0, "mid": 800.0, "dear": 5000.0, "unpriced": None}


def anchor():
    return a.anchor_object(REFERENCE, basis="api", workload="w1")


def test_anchor_object_pads_the_reference_extremes_by_two():
    anchors = anchor()
    assert anchors["low"] == 50.0 and anchors["high"] == 10000.0
    assert anchors["referenceIds"] == ["cheap", "dear", "mid"]
    assert anchors["basis"] == "api" and anchors["workload"] == "w1" and anchors["padding"] == 2.0


def test_anchor_object_rejects_empty_or_non_positive_references():
    with pytest.raises(ValueError, match="no reference costs for the plan anchors"):
        a.anchor_object({"x": None}, basis="plan", workload=None)
    with pytest.raises(ValueError, match="must be finite and positive"):
        a.anchor_object({"x": 0.0}, basis="api", workload=None)


def test_reference_cohort_never_clips_and_scores_are_log_scaled():
    anchors = anchor()
    for value in (100.0, 800.0, 5000.0):
        assert 0.0 < a.cost_score(value, anchors) < 100.0
    # Equal cost ratios move the score by equal amounts.
    step = a.cost_score(100.0, anchors) - a.cost_score(200.0, anchors)
    assert a.cost_score(1000.0, anchors) - a.cost_score(2000.0, anchors) == pytest.approx(step)
    assert a.cost_score(50.0, anchors) == pytest.approx(100.0)
    assert a.cost_score(10000.0, anchors) == pytest.approx(0.0)


def test_cost_score_clips_and_keeps_the_unclipped_value():
    anchors = anchor()
    assert a.cost_score(10.0, anchors) == 100.0
    assert a.unclipped_score(10.0, anchors) > 100.0
    assert a.cost_score(40000.0, anchors) == 0.0
    assert a.unclipped_score(40000.0, anchors) < 0.0
    assert a.cost_score(None, anchors) is None
    assert a.cost_score(0.0, anchors) is None


def test_beyond_factor_measures_distance_outside_the_anchors():
    anchors = anchor()
    assert a.beyond_factor(25.0, anchors) == 2.0
    assert a.beyond_factor(30000.0, anchors) == 3.0
    assert a.beyond_factor(500.0, anchors) == 1.0


def test_clip_gate_allowance_and_far_rows():
    anchors = anchor()
    inside = {f"r{index}": 500.0 for index in range(20)}
    gate = a.clip_gate(dict(inside, one=40.0, two=12000.0, missing=None), anchors)
    assert gate["clipped"] == ["one", "two"] and gate["allowance"] == pytest.approx(2.2)
    assert gate["beyondFactorLimit"] == [] and gate["hold"] is False
    gate = a.clip_gate(dict(inside, one=40.0, two=12000.0, three=45.0), anchors)
    assert gate["hold"] is True  # three clipped rows exceed max(1, 2.3)
    gate = a.clip_gate({"far": 20.0}, anchors)
    assert gate["beyondFactorLimit"] == ["far"] and gate["hold"] is True and gate["allowance"] == 1.0


def test_exchange_rate_and_its_curve():
    anchors = anchor()
    rate = a.exchange_rate(anchors, 0.25)
    span = math.log(200.0)
    assert rate["valuePointsPerCostDoubling"] == pytest.approx(25 * math.log(2) / span)
    assert rate["qualityPointsPerCostDoubling"] == pytest.approx(25 * math.log(2) / (0.75 * span))
    assert rate["anchorRatio"] == pytest.approx(200.0)
    curve = a.exchange_rate_curve(0.25, [10.0, 100.0])
    assert [point["anchorRatio"] for point in curve] == [10.0, 100.0]
    assert curve[0]["qualityPointsPerCostDoubling"] > curve[1]["qualityPointsPerCostDoubling"]


def test_cost_influence_flags_a_low_cost_share():
    result = a.cost_influence([50.0, 50.0, 50.0], [10.0, 50.0, 90.0], 0.25)
    assert result["costShare"] == 0.0 and result["flag"] is True
    result = a.cost_influence([0.0, 100.0], [40.0, 60.0], 0.25)
    assert result["costShare"] == pytest.approx(0.25 * 50 / (0.25 * 50 + 0.75 * 10))
    assert result["flag"] is False
    assert a.cost_influence([1.0], [2.0, 3.0], 0.25) == {"costShare": None, "flag": False, "qualityFlag": False, "varianceAllocation": None}
    dominant = a.cost_influence([0.0, 100.0], [50.0, 50.1], 0.25)
    assert dominant["costShare"] > 0.9 and dominant["qualityFlag"] is True and dominant["flag"] is False
    flat = a.cost_influence([5.0, 5.0], [7.0, 7.0], 0.25)
    assert flat["costShare"] is None and flat["flag"] is False and flat["varianceAllocation"] is None


def test_variance_allocation_splits_value_variance_and_sees_offsetting_terms():
    """E189: the two contributions sum to 1; negatively correlated terms can contribute less than their SDs suggest."""

    allocation = a.variance_allocation([0.0, 50.0, 100.0], [40.0, 50.0, 60.0], 0.25)
    assert allocation["cost"] + allocation["quality"] == pytest.approx(1.0)
    # Dearer models score higher on quality: cost and quality offset, and cost's contribution can turn negative.
    offset = a.variance_allocation([100.0, 50.0, 0.0], [10.0, 50.0, 100.0], 0.25)
    assert offset["cost"] < 0 < offset["quality"] and offset["cost"] + offset["quality"] == pytest.approx(1.0)
    # I38: no split below three rows, nor when the value scores do not vary.
    assert a.variance_allocation([0.0, 100.0], [40.0, 60.0], 0.25) is None
    assert a.variance_allocation([5.0, 5.0, 5.0], [7.0, 7.0, 7.0], 0.25) is None


def test_panel_cost_influence_uses_the_common_workload_panel():
    rows = [
        {"id": "a", "workloadId": "W", "costScore": 0.0, "qualityScore": 40.0},
        {"id": "b", "workloadId": "W", "costScore": 100.0, "qualityScore": 60.0},
        {"id": "s1", "workloadId": "W-sub", "costScore": 90.0, "qualityScore": 50.0},
        {"id": "s2", "workloadId": "W-sub", "costScore": 90.0, "qualityScore": 50.0},
        {"id": "lone", "workloadId": "W-other", "costScore": 10.0, "qualityScore": 70.0},
        {"id": "unscored", "workloadId": "W", "costScore": None, "qualityScore": 55.0},
    ]
    result = a.panel_cost_influence(rows, 0.25, "W")
    headline = result["commonWorkload"]
    assert headline["panel"] == ["a", "b"] and headline["excluded"] == ["lone", "s1", "s2", "unscored"]
    assert headline["costShare"] == pytest.approx(0.25 * 50 / (0.25 * 50 + 0.75 * 10)) and headline["status"] == "defined"
    assert result["flag"] is False
    assert result["subsetStrata"]["W-sub"]["status"] == "undefined — no composite dispersion"
    assert result["subsetStrata"]["W-other"]["status"] == "undefined (panel too small)"
    assert result["displayedTableDispersion"]["panel"] == ["a", "b", "lone", "s1", "s2"]


def test_value_score_needs_cost_and_quality():
    assert a.value_score(80.0, 60.0, 0.25) == pytest.approx(65.0)
    assert a.value_score(None, 60.0, 0.25) is None
    assert a.value_score(80.0, None, 0.25) is None


def test_numerical_domains_are_validated():
    """E109: only finite, strictly positive values are scoreable; zero and infinities never score."""

    assert a.scoreable(1.0) and a.scoreable(3)
    assert not any(a.scoreable(value) for value in (0, 0.0, -1.0, float("inf"), float("nan"), None, True, "5"))
    anchors = a.anchor_object({"x": 10.0, "y": 1000.0}, basis="api", workload="w")
    assert a.cost_score(0.0, anchors) is None and a.cost_score(float("inf"), anchors) is None
    with pytest.raises(ValueError, match="finite and positive"):
        a.anchor_object({"x": float("inf")}, basis="api", workload="w")


def test_trimmed_anchor_object_is_a_percentile_diagnostic():
    costs = {f"r{i}": float(value) for i, value in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000])}
    trimmed = a.trimmed_anchor_object(costs, basis="api", workload="w")
    assert trimmed["low"] == pytest.approx(2.0 / 2) and trimmed["high"] == pytest.approx(10.0 * 2)
    assert trimmed["rule"].startswith("P10") and a.anchor_object(costs, basis="api", workload="w")["high"] == 2000.0
    with pytest.raises(ValueError, match="at least two"):
        a.trimmed_anchor_object({"x": 1.0, "y": None}, basis="plan", workload="w")
