"""Tests for the v3 quality leaf table, transforms, coverage, bounds and provisional rule."""

from __future__ import annotations

import pytest

from valuerank import quality as q


def full_observations(z: float = 50.0) -> dict:
    return {leaf.key: q.Observation(z) for leaf in q.LEAVES}


def test_leaf_weights_sum_to_the_group_shares_and_to_100():
    assert sum(leaf.weight for leaf in q.LEAVES) == pytest.approx(100.0)
    for group, share in q.GROUPS.items():
        assert sum(leaf.weight for leaf in q.LEAVES if leaf.group == group) == pytest.approx(share)
    assert set(q.GROUP_LABELS) == set(q.GROUPS)
    assert q.LEAF_BY_KEY["omniscience"].weight == 10.0  # O26: instruction following retired
    assert "livebenchIF" not in q.LEAF_BY_KEY


def test_source_shares_split_aa_run_and_independent_weight():
    shares = q.source_shares()
    # O37: Terminal-Bench is AA's own run; in the max-effort ranking Bug Hunt, LiveBench 2.0 Overall and the Vals leaves are
    # independent (O55, O61).
    assert shares["aa"] == pytest.approx(0.66)
    assert shares["independent"] == pytest.approx(0.34)
    with q.active_track("aicd"):
        assert q.source_shares() == {"aa": pytest.approx(0.78), "independent": pytest.approx(0.22)}


def test_each_ranking_weighs_100_percent_with_software_engineering_at_60():
    """O53-O55: both rankings keep the group shares; the active ranking is restored after the block."""

    for track, leaves in q.TRACKS.items():
        assert sum(leaf.weight for leaf in leaves) == pytest.approx(100.0), track
        assert sum(leaf.weight for leaf in leaves if leaf.group == "swe") == pytest.approx(60.0), track
    with q.active_track("aicd") as leaves:
        assert q.TRACK == "aicd" and q.LEAVES is leaves and "aiCodingDaily" in q.LEAF_BY_KEY
    assert q.TRACK == q.DEFAULT_TRACK == "max" and "aiCodingDaily" not in q.LEAF_BY_KEY
    assert set(q.ALL_LEAVES) == {leaf.key for leaves in q.TRACKS.values() for leaf in leaves}


def test_ai_coding_daily_points_are_scored_out_of_60():
    assert q.aicd_z(45.0).z == pytest.approx(75.0) and q.aicd_z(70.0).z == 100.0
    assert q.unclipped_z("aiCodingDaily", 66.0) == pytest.approx(110.0)
    # A leaf outside the active ranking keeps its own nominal weight in the clipping audit.
    assert q.clip_audit("aiCodingDaily", 30.0)["weight"] == 10.0


def test_observation_bounds_are_clipped_to_the_domain():
    assert (q.Observation(99.9, 0.5).low, q.Observation(99.9, 0.5).high) == (pytest.approx(99.4), 100.0)
    assert (q.Observation(0.2, 0.5).low, q.Observation(0.2, 0.5).high) == (0.0, pytest.approx(0.7))


def test_percent_and_fraction_transforms_clip_and_scale_precision():
    assert q.percent_z(78.8, 0.05) == q.Observation(78.8, 0.05)
    assert q.percent_z(120.0).z == 100.0 and q.percent_z(-5.0).z == 0.0
    observation = q.fraction_z(0.796666666666667, 0.0005)
    assert observation.z == pytest.approx(79.6666666666667)
    assert observation.half_width == pytest.approx(0.05)


def test_gdpval_logistic_alternative_is_the_win_probability_against_aa_anchor():
    """E181: 50 at AA's anchor (1600), 100/(1 + 10^-1) one tenfold-odds step (400 Elo) above it."""

    assert q.gdpval_logistic_z(1600.0) == pytest.approx(50.0)
    assert q.gdpval_logistic_z(2000.0) == pytest.approx(100.0 / 1.1)
    assert q.gdpval_logistic_z(1200.0) == pytest.approx(100.0 / 11.0)


def test_gdpval_transform_matches_aa_integration():
    assert q.gdpval_z(1555.91).z == pytest.approx(52.7955)
    assert q.gdpval_z(400.0).z == 0.0
    assert q.gdpval_z(3000.0).z == 100.0
    assert q.gdpval_z(1500.0, 0.005).half_width == pytest.approx(0.00025)


def test_bug_hunt_release_vector():
    assert round(q.bug_hunt_z(52).z, 2) == 49.52
    assert q.bug_hunt_z(44.3, 0.05).half_width == pytest.approx(100 * 0.05 / 105)


def test_omniscience_index_is_monotone_in_outcomes():
    """O28: z = (I + 100) / 2 with I = 100 (correct - incorrect) / all questions."""

    assert q.omniscience_index_z(50.0).z == 75.0 and q.omniscience_index_z(-100.0).z == 0.0
    assert q.omniscience_from_counts(60, 0, 10, 30) == (pytest.approx(50.0), pytest.approx(75.0))
    # Kimi K3's fixture: turning an abstention into a correct answer raises the score (the retired (2A + N)/3 fell 82 -> 66).
    assert q.omniscience_from_counts(99, 0, 1, 0)[1] > q.omniscience_from_counts(98, 0, 1, 1)[1]
    assert q.omniscience_from_counts(60, 0, 9, 31)[1] > q.omniscience_from_counts(60, 0, 10, 30)[1]
    assert q.omniscience_from_counts(0, 0, 0, 10) == (0.0, 50.0)  # all abstention
    # Reconciliation with AA's accuracy and conditional hallucination rate (GPT-6 Astra xhigh, 2026-10-17 snapshot).
    assert q.omniscience_index_from_rates(0.6185, 0.4831804281345566) == pytest.approx(43.416666666666664)


def test_summarize_full_coverage_row():
    summary = q.summarize(full_observations(50.0))
    assert summary.coverage == pytest.approx(1.0)
    assert summary.displayed == pytest.approx(50.0)
    assert (summary.lower, summary.upper) == (pytest.approx(50.0), pytest.approx(50.0))
    assert summary.provisional is False and summary.provisional_reasons == ()
    assert summary.swe_leaves == 6 and summary.swe_weight == pytest.approx(0.6)


def test_summarize_renormalises_over_observed_leaves_and_bounds_missing_ones():
    observations = full_observations(80.0)
    observations["bugHunt"] = q.Observation(20.0, 1.0)
    del observations["hle"]
    summary = q.summarize(observations)
    expected_coverage = 1 - (5 / 3) / 100
    assert summary.coverage == pytest.approx(expected_coverage)
    weighted = sum(leaf.weight * observations[leaf.key].z for leaf in q.LEAVES if leaf.key in observations)
    assert summary.displayed == pytest.approx(weighted / (100 * expected_coverage))
    assert summary.lower == pytest.approx((weighted - 8 * 1.0) / 100)
    assert summary.upper == pytest.approx((weighted + 8 * 1.0 + (5 / 3) * 100) / 100)
    assert summary.provisional is False


def test_provisional_rule_reports_every_failed_condition():
    observations = {"bugHunt": q.Observation(40.0), "gdpval": q.Observation(60.0)}
    with q.active_track("aicd"):
        summary = q.summarize(observations)
    assert summary.provisional is True
    assert summary.provisional_reasons == (
        "coverage 22% below 70%",
        "1 SWE leaves observed (need 2)",
        "observed SWE weight 12% below 40%",
        "FrontierCode 2.0 missing",
    )


def test_provisional_when_only_frontiercode_is_missing():
    with q.active_track("aicd"):
        observations = full_observations()
        del observations["frontierCode"]
        summary = q.summarize(observations)
    assert summary.coverage == pytest.approx(0.79)
    # Coverage clears 70%, but the other SWE leaves carry only 39% of quality, and FrontierCode weighs 21% (O55).
    assert summary.provisional_reasons == ("observed SWE weight 39% below 40%", "FrontierCode 2.0 missing")


def test_summarize_with_no_observations_has_no_displayed_quality():
    summary = q.summarize({})
    assert summary.displayed is None and summary.coverage == 0.0
    assert (summary.lower, summary.upper) == (0.0, 100.0)


def test_summarize_rejects_unknown_leaves():
    with pytest.raises(ValueError, match="unknown quality leaves: livebenchIF"):
        q.summarize({"livebenchIF": q.Observation(1.0)})


def test_composite_requires_every_leaf():
    values = {leaf.key: 40.0 for leaf in q.LEAVES}
    assert q.composite(values) == pytest.approx(40.0)
    del values["critpt"]
    with pytest.raises(ValueError, match="missing: critpt"):
        q.composite(values)


def test_clip_audit_discloses_saturation_and_rejects_domain_violations():
    """E110: valid saturation is disclosed; values outside the documented domain are rejected."""

    inside = q.clip_audit("terminalBench", 72.0)
    assert inside["domainValid"] and inside["anchorPosition"] == "inside" and inside["action"] == "none" and inside["clippingAmount"] == 0.0
    high_elo = q.clip_audit("gdpval", 2700.0)
    assert high_elo["anchorPosition"] == "above" and high_elo["clippingAmount"] == pytest.approx(10.0) and high_elo["action"] == "disclose saturation"
    assert q.clip_audit("gdpval", 400.0)["anchorPosition"] == "below"
    assert q.clip_audit("bugHunt", 52.0)["unclippedZ"] == pytest.approx(49.5238, abs=1e-4)
    assert q.clip_audit("hle", 0.5)["unclippedZ"] == 50.0
    omni = q.clip_audit("omniscience", 43.4)
    assert omni["raw"] == 43.4 and omni["unclippedZ"] == pytest.approx(71.7)
    for key, raw in (("terminalBench", 101.0), ("tbScience", -0.1), ("omniscience", 120.0), ("gdpval", float("nan")), ("lcr", True), ("hle", None)):
        bad = q.clip_audit(key, raw)
        assert bad["domainValid"] is False and bad["action"].startswith("reject") and bad["unclippedZ"] is None
