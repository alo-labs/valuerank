"""Tests for the scenario engine: kernels, strata, weights, frequencies and the sequential precision rule."""

from __future__ import annotations

import random

import pytest

from valuerank import quality as q
from valuerank import scenarios as sc
from valuerank.scenarios import Kernel, RowInputs

ANCHORS = {"low": 10.0, "high": 1000.0}


def full_row(name, z, cost, **extra):
    leaves = {leaf.key: Kernel("fixed", (z,)) for leaf in q.LEAVES}
    leaves.update(extra.pop("leaves", {}))
    return RowInputs(name, leaves, Kernel("fixed", (cost,)), **extra)


def test_kernels_draw_their_families():
    rng = random.Random(1)
    assert Kernel("fixed", (3.0,)).draw(rng) == 3.0
    value = Kernel("uniform", (10.0, 20.0)).draw(rng)
    assert 10.0 <= value <= 20.0
    heavy = Kernel("uniform", (10.0, 20.0), "endpoint-heavy")
    assert 10.0 <= heavy.draw(rng, use_alternative=True) <= 20.0
    assert 10.0 <= Kernel("uniform", (10.0, 20.0)).draw(rng, use_alternative=True) <= 20.0
    runs = Kernel("runs", (40.0, 50.0, 60.0)).draw(rng)
    assert 40.0 <= runs <= 60.0
    with pytest.raises(ValueError, match="unknown kernel family: normal"):
        Kernel("normal", (0, 1)).draw(rng)


def test_dirichlet_and_hierarchical_weights_preserve_totals():
    rng = random.Random(2)
    shares = sc.dirichlet(rng, [1.0, 2.0, 3.0])
    assert sum(shares) == pytest.approx(1.0)
    weights = sc.hierarchical_weights(rng)
    assert set(weights) == {leaf.key for leaf in q.LEAVES}
    assert sum(weights.values()) == pytest.approx(100.0)
    assert sc.nominal_weights()["deepswe"] == 30.0


def test_hierarchical_weights_keep_the_nominal_means():
    rng = random.Random(3)
    totals = {leaf.key: 0.0 for leaf in q.LEAVES}
    draws = 2000
    for _ in range(draws):
        for key, value in sc.hierarchical_weights(rng).items():
            totals[key] += value
    for leaf in q.LEAVES:
        assert totals[leaf.key] / draws == pytest.approx(leaf.weight, rel=0.08)


def test_missing_ranges_use_observed_values_and_default_to_the_domain():
    rows = [
        RowInputs("a", {"deepswe": Kernel("fixed", (40.0,)), "bugHunt": Kernel("runs", (30.0, 50.0))}, Kernel("fixed", (1.0,))),
        RowInputs("b", {"deepswe": Kernel("fixed", (70.0,))}, Kernel("fixed", (1.0,))),
    ]
    ranges = sc.missing_ranges(rows)
    assert ranges["deepswe"] == (40.0, 70.0)
    assert ranges["bugHunt"] == (40.0, 40.0)
    assert ranges["critpt"] == (0.0, 100.0)


def test_draw_scenario_strata():
    rng = random.Random(4)
    partial = RowInputs("p", {"deepswe": Kernel("fixed", (80.0,))}, Kernel("uniform", (90.0, 110.0)))
    s0 = sc.draw_scenario([partial], "S0", rng)
    assert s0["p"][1] == pytest.approx(80.0) and 90.0 <= s0["p"][0] <= 110.0
    s1 = sc.draw_scenario([partial], "S1", rng)
    assert 0.0 <= s1["p"][1] <= 100.0 and s1["p"][1] != pytest.approx(80.0)
    alternative = sc.draw_scenario([partial], "S1", rng, alternative=True, ranges={"deepswe": (0, 0), **{leaf.key: (50.0, 50.0) for leaf in q.LEAVES}})
    assert alternative["p"][1] == pytest.approx(0.3 * 80 + 0.7 * 50)
    alternative_default = sc.draw_scenario([partial], "S1", rng, alternative=True)
    assert 0.0 <= alternative_default["p"][1] <= 100.0
    s2 = sc.draw_scenario([full_row("f", 60.0, 100.0)], "S2", rng)
    assert s2["f"][1] == pytest.approx(60.0)
    with pytest.raises(ValueError, match="unknown stratum: S9"):
        sc.draw_scenario([partial], "S9", rng)


def test_values_ranks_frontier_and_cheapest_qualifier():
    scenario = {"a": (100.0, 80.0), "b": (50.0, 60.0), "c": (200.0, 70.0), "d": (50.0, 60.0)}
    values = sc.scenario_values(scenario, ANCHORS, 0.25)
    assert values["a"] == pytest.approx(0.25 * 50 + 0.75 * 80)
    assert sc.ranks({"x": 3.0, "y": 3.0, "z": 1.0}) == {"x": 1, "y": 1, "z": 3}
    assert sc.frontier_rows(scenario) == {"a", "b", "d"}
    assert sc.cheapest_qualifier(scenario, "c") == "a"
    assert sc.cheapest_qualifier(scenario, "b") is None  # b and d tie at the cheapest cost
    assert sc.cheapest_qualifier({"only": (5.0, 10.0), "ref": (1.0, 50.0)}, "ref") == "ref"
    assert sc.cheapest_qualifier({"ref": (1.0, 50.0)}, "ref") == "ref"


def test_standard_error():
    assert sc.standard_error(0.5, 100) == pytest.approx(0.05)
    assert sc.standard_error(0.5, 0) == 0.0


def test_shares_report_frequencies_with_monte_carlo_errors():
    rows = [full_row("strong", 80.0, 100.0), full_row("cheap", 40.0, 20.0), full_row("weak", 20.0, 500.0)]
    result = sc.shares(rows, "S0", 200, 7, ANCHORS, 0.25, references=("cheap",))
    assert result["scenarios"] == 200 and result["seed"] == 7 and result["stratum"] == "S0"
    assert result["rows"]["strong"]["top1"]["share"] == 1.0
    assert result["rows"]["weak"]["frontier"]["share"] == 0.0
    assert result["rows"]["strong"]["qualifies"]["cheap"] == 1.0
    assert result["rows"]["weak"]["qualifies"]["cheap"] == 0.0
    assert result["rows"]["cheap"]["top3"]["monteCarloSe"] == 0.0
    alternative = sc.shares(rows, "S1", 50, 7, ANCHORS, 0.25, alternative=True)
    assert alternative["alternative"] is True and alternative["rows"]["strong"]["qualifies"] == {}


def test_regularized_beta_and_clopper_pearson():
    assert sc.regularized_beta(0.0, 2, 3) == 0.0
    assert sc.regularized_beta(1.0, 2, 3) == 1.0
    assert sc.regularized_beta(0.5, 1, 1) == pytest.approx(0.5)
    assert sc.regularized_beta(0.9, 2, 2) == pytest.approx(3 * 0.81 - 2 * 0.729)  # 3x^2 - 2x^3
    assert sc.regularized_beta(0.1, 2, 2) == pytest.approx(3 * 0.01 - 2 * 0.001)
    lower, upper = sc.clopper_pearson(5, 10, 0.05)
    assert lower == pytest.approx(0.1871, abs=1e-4) and upper == pytest.approx(0.8129, abs=1e-4)
    assert sc.clopper_pearson(0, 10, 0.05) == (0.0, pytest.approx(0.3085, abs=1e-4))
    assert sc.clopper_pearson(10, 10, 0.05) == (pytest.approx(0.6915, abs=1e-4), 1.0)


def test_sequential_threshold_met_not_met_and_unresolved():
    rng = random.Random(5)
    met = sc.sequential_threshold(lambda r: True, rng, batch=100, looks=4)
    assert met["status"] == "met" and met["looks"] == 1
    not_met = sc.sequential_threshold(lambda r: r.random() < 0.5, rng, batch=200, looks=4)
    assert not_met["status"] == "not met"
    borderline = sc.sequential_threshold(lambda r: r.random() < 0.9, rng, batch=50, looks=2)
    assert borderline["status"] == "scenario threshold unresolved" and borderline["scenarios"] == 100


def test_scenario_supported_cheapest_needs_a_non_provisional_candidate():
    reference = full_row("ref", 50.0, 100.0)
    rule = {"batch": 100, "looks": 2}
    eligible = sc.scenario_supported_cheapest([full_row("c", 60.0, 10.0), reference], "c", "ref", "S1", random.Random(5), **rule)
    assert eligible["status"] == "met" and eligible["label"] is True
    assert eligible["decisionTarget"]["qualityEquation"] == "full composite"
    # A provisional singleton that is cheapest in every scenario keeps its frequency but gets no label.
    provisional = sc.scenario_supported_cheapest([full_row("c", 60.0, 10.0, provisional=True), reference], "c", "ref", "S1", random.Random(5), **rule)
    assert provisional["share"] == 1.0 and provisional["uniqueLabelEligible"] is False and provisional["label"] is False
    # A cheaper provisional qualifier still competes and blocks the candidate.
    blocked = sc.scenario_supported_cheapest([full_row("c", 60.0, 10.0), full_row("p", 70.0, 5.0, provisional=True), reference], "c", "ref", "S1", random.Random(5), **rule)
    assert blocked["status"] == "not met" and blocked["label"] is False


def test_shares_fix_the_panel_and_report_pairwise_win_tie_loss():
    rows = [full_row("a", 60.0, 10.0), full_row("b", 60.0, 10.0), full_row("c", 40.0, 10.0)]
    result = sc.shares(rows, "S0", 20, 9, ANCHORS, 0.25, pairs=(("a", "b"), ("a", "c"), ("c", "a")))
    assert result["panel"] == ["a", "b", "c"] and result["panelSize"] == 3
    # Tied rows share the better competition rank, so both hold rank 1.
    assert result["rows"]["a"]["top1"]["share"] == result["rows"]["b"]["top1"]["share"] == 1.0
    assert [item["tie"] for item in result["pairwise"]] == [1.0, 0.0, 0.0]
    assert result["pairwise"][1]["win"] == 1.0 and result["pairwise"][2]["loss"] == 1.0


def test_singleton_group_within_weight_is_exactly_one():
    """E99: a one-leaf group takes its whole group share; no within-group draw."""

    groups = list(q.GROUPS)
    single = [group for group in groups if len([leaf for leaf in q.LEAVES if leaf.group == group]) == 1]
    assert single
    weights = sc.hierarchical_weights(random.Random(7))
    replay = sc.dirichlet(random.Random(7), [sc.GROUP_CONCENTRATION * q.GROUPS[group] / 100.0 for group in groups])
    for group in single:
        leaf = next(leaf for leaf in q.LEAVES if leaf.group == group)
        assert weights[leaf.key] == 100.0 * replay[groups.index(group)]


def test_only_the_full_composite_s1_core_branch_authorises_the_label():
    """E100 fixture: 70% coverage, observed leaves at 100, against a fully observed reference at 80."""

    observed = {leaf.key: Kernel("fixed", (100.0,)) for leaf in q.LEAVES if leaf.key not in {"bugHunt", "terminalBench", "automationBench"}}
    candidate = RowInputs("c", observed, Kernel("fixed", (10.0,)))
    reference = full_row("ref", 80.0, 100.0)
    s0 = sc.scenario_supported_cheapest([candidate, reference], "c", "ref", "S0", random.Random(11), batch=500, looks=2)
    assert s0["share"] == 1.0 and s0["labelAuthorized"] is False and s0["label"] is False
    assert s0["decisionTarget"]["qualityEquation"] == "observed leaves"
    # Full composite: 70 + 0.1 * (U1 + U2 + U3) >= 80 holds with probability 5/6, below the 90% bar.
    s1 = sc.scenario_supported_cheapest([candidate, reference], "c", "ref", "S1", random.Random(11), batch=1000, looks=2)
    assert s1["labelAuthorized"] is True and s1["status"] == "not met" and s1["label"] is False
    assert s1["share"] == pytest.approx(5 / 6, abs=0.04)
    alternative = sc.scenario_supported_cheapest([full_row("c", 60.0, 10.0), reference], "c", "ref", "S1", random.Random(5), alternative=True, batch=100, looks=1)
    assert alternative["labelAuthorized"] is True and alternative["decisionTarget"]["kernel"] == "endpoint-heavy alternative"
    blocks = sc.scenario_supported_cheapest([full_row("c", 60.0, 10.0), reference], "c", "ref", "S1", random.Random(5), alternative_rows=frozenset({"ref"}), batch=100, looks=1)
    assert blocks["decisionTarget"]["kernel"] == "block assignment" and blocks["decisionTarget"]["endpointHeavyRows"] == ["ref"]


def test_kernel_robust_label_needs_every_kernel():
    """E112 fixture: 70% coverage, one missing 10% leaf in each of three groups, reference at 78.

    The candidate qualifies when 70 + 0.1 * (U1 + U2 + U3) >= 78: about 91.5% of
    uniform draws but 86.7% of arcsine (endpoint-heavy) draws, so no label.
    """

    missing = {"bugHunt", "automationBench", "omniscience"}
    candidate = RowInputs("c", {leaf.key: Kernel("fixed", (100.0,)) for leaf in q.LEAVES if leaf.key not in missing}, Kernel("fixed", (10.0,)))
    reference = full_row("ref", 78.0, 100.0)
    result = sc.kernel_robust_cheapest([candidate, reference], "c", "ref", 21, batch=10000, looks=2)
    primary, heavy = result["assignments"]["UUU"], result["assignments"]["HUU"]
    assert sorted(result["assignments"]) == ["HHU", "HUU", "UHU", "UUU"]  # no competitors: the competitor block is empty
    assert primary["status"] == "met" and primary["share"] == pytest.approx(0.915, abs=0.01)
    assert heavy["status"] == "not met" and heavy["share"] == pytest.approx(0.867, abs=0.01)
    assert result["label"] is False and result["reading"] == "primary-kernel frequency >= 90%; kernel-sensitive"
    assert result["frequencyRange"][0] < 0.9 <= result["frequencyRange"][1]
    always = sc.kernel_robust_cheapest([full_row("c", 80.0, 10.0), reference, full_row("x", 90.0, 500.0)], "c", "ref", 3, batch=100, looks=1)
    assert len(always["assignments"]) == 8 and always["label"] is True and always["reading"].startswith("supported under the registered kernel checks")
    provisional = sc.kernel_robust_cheapest([full_row("c", 80.0, 10.0, provisional=True), reference], "c", "ref", 3, batch=100, looks=1)
    assert provisional["label"] is False and provisional["reading"] == "frequency only (provisional row)"
    never = sc.kernel_robust_cheapest([full_row("c", 50.0, 10.0), reference], "c", "ref", 3, batch=100, looks=1)
    assert never["reading"] == "not scenario-supported"
    itself = sc.kernel_assignments([reference], "ref", "ref")
    assert [item["id"] for item in itself] == ["UUU", "HHU"]  # candidate and reference blocks coincide
