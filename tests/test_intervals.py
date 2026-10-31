"""Tests for the interval outputs: frontier membership and cheapest above a bar (exact decisions)."""

from __future__ import annotations

import pytest

from valuerank import intervals as iv
from valuerank.intervals import Affine, Box, Reference, SharedBox


def test_box_validation():
    with pytest.raises(ValueError, match="invalid admissible box for x"):
        Box("x", 0.0, 1.0, 1.0, 2.0)
    with pytest.raises(ValueError):
        Box("x", 2.0, 1.0, 1.0, 2.0)
    with pytest.raises(ValueError):
        Box("x", 1.0, 2.0, 3.0, 2.0)


def test_frontier_with_independent_boxes():
    boxes = [
        Box("cheap", 10, 10, 40, 40),
        Box("strong", 100, 100, 80, 80),
        Box("dominated", 120, 120, 70, 70),
        Box("overlap", 95, 130, 75, 85),
    ]
    result = iv.frontier(boxes)
    assert result["cheap"]["definite"] == iv.CERTIFIED and result["cheap"]["possible"] == iv.CERTIFIED
    assert result["dominated"]["possible"] == iv.DISPROVED
    assert result["dominated"]["possibleBlockedBy"] == ["strong"]
    assert result["overlap"]["possible"] == iv.CERTIFIED  # at its best corner it is cheaper and better
    assert result["overlap"]["definite"] == iv.DISPROVED
    assert result["overlap"]["definiteCounterexample"] == "strong"
    assert result["strong"]["definite"] == iv.DISPROVED  # the overlapping row can dominate it
    assert result["cheap"]["possibleWitness"] == {"row": "best corner", "others": "worst corners"}
    assert result["dominated"]["possibleWitness"] is None


def test_exact_ties_never_dominate():
    result = iv.frontier([Box("a", 5, 5, 50, 50), Box("b", 5, 5, 50, 50)])
    assert result["a"]["definite"] == iv.CERTIFIED and result["b"]["definite"] == iv.CERTIFIED


def test_frontier_with_declared_shared_factors_is_unresolved():
    result = iv.frontier([Box("a", 1, 2, 3, 4)], shared_factors=("price list",))
    assert result["a"]["possible"] == iv.UNRESOLVED and "shared factors" in result["a"]["reason"]


def test_shared_factor_interior_witness_release_vector():
    i = SharedBox("i", Affine(1), Affine(1), Affine(1.2), Affine(1.2))
    j = SharedBox("j", Affine(0), Affine(0), Affine(0, 2), Affine(0, 2))
    k = SharedBox("k", Affine(0), Affine(0), Affine(2, -2), Affine(2, -2))
    result = iv.frontier_shared([i, j, k], 0.0, 1.0)
    assert result["i"]["possible"] == iv.CERTIFIED
    assert 0.4 < result["i"]["possibleWitnessT"] < 0.6
    assert result["i"]["definite"] == iv.DISPROVED
    # Endpoints alone would miss it: at t = 0 and t = 1 a competitor dominates i.
    assert iv._dominance_verdict((0, 0), (2, 2), (1, 1), (1.2, 1.2)) == "all"


def test_shared_factor_definite_member_and_disproved_possible():
    leader = SharedBox("leader", Affine(1), Affine(1), Affine(90), Affine(90))
    laggard = SharedBox("laggard", Affine(5), Affine(5), Affine(10, 1), Affine(10, 1))
    result = iv.frontier_shared([leader, laggard], 0.0, 1.0)
    assert result["leader"]["definite"] == iv.CERTIFIED and result["leader"]["possible"] == iv.CERTIFIED
    assert result["laggard"]["possible"] == iv.DISPROVED and result["laggard"]["possibleWitnessT"] is None
    assert result["laggard"]["definite"] == iv.DISPROVED


def test_shared_factor_search_returns_unresolved_at_the_depth_limit():
    # j touches i's quality exactly at an interior point; at depth 0 nothing is decided.
    i = SharedBox("i", Affine(1), Affine(1), Affine(1.0), Affine(1.0))
    j = SharedBox("j", Affine(0), Affine(0), Affine(0, 2), Affine(0, 2))
    result = iv.frontier_shared([i, j], 0.0, 1.0, depth=0)
    assert result["i"]["possible"] == iv.UNRESOLVED and result["i"]["definite"] == iv.UNRESOLVED


def test_search_reports_absent_when_both_halves_are_absent():
    assert iv._search(lambda lo, hi: "some" if hi - lo > 0.5 else "none", 0.0, 1.0, 3) == ("absent", None)
    assert iv._search(lambda lo, hi: "some" if lo < 0.5 else "all", 0.0, 1.0, 3) == ("found", 0.75)
    # Undecided halves at the depth limit leave the search unresolved.
    assert iv._search(lambda lo, hi: "some", 0.0, 1.0, 1) == ("unresolved", None)


def test_recheck_rejects_a_witness_that_fails_as_a_point():
    assert iv._recheck(lambda lo, hi: "some", ("found", 0.3)) == ("unresolved", None)
    assert iv._recheck(lambda lo, hi: "all", ("found", 0.3)) == ("found", 0.3)
    assert iv._recheck(lambda lo, hi: "some", ("absent", None)) == ("absent", None)


def test_dominance_verdicts():
    assert iv._dominance_verdict((1, 1), (2, 2), (1, 1), (2, 2)) == "none"  # exact tie
    assert iv._dominance_verdict((0, 2), (1, 3), (1, 1), (2, 2)) == "some"
    assert iv._dominance_verdict((3, 4), (5, 6), (1, 2), (1, 2)) == "none"
    assert iv._dominance_verdict((0, 0), (0, 1), (1, 1), (2, 2)) == "none"


def test_qualification_against_the_reference():
    reference = Reference("ref", 50, 60)
    assert iv.qualification(Box("ref", 1, 1, 50, 60), reference) == {"confirmed": iv.CERTIFIED, "possible": iv.CERTIFIED}
    assert iv.qualification(Box("a", 1, 1, 61, 70), reference) == {"confirmed": iv.CERTIFIED, "possible": iv.CERTIFIED}
    assert iv.qualification(Box("b", 1, 1, 55, 58), reference) == {"confirmed": iv.DISPROVED, "possible": iv.CERTIFIED}
    assert iv.qualification(Box("c", 1, 1, 10, 49), reference) == {"confirmed": iv.DISPROVED, "possible": iv.DISPROVED}


def test_bar_interior_witness_release_vector():
    # i: C=1, Q=5; j: C=0, Q=4; Q_r in [0, 10]: i is possibly cheapest via Q_r in (4, 5].
    boxes = [Box("i", 1, 1, 5, 5), Box("j", 0.5, 0.5, 4, 4)]
    result = iv.cheapest_above_bar(boxes, Reference("r", 0, 10))
    assert result["rows"]["i"]["possibleCheapest"] == iv.CERTIFIED
    assert result["rows"]["i"]["witnessReferenceQuality"] == 5
    assert result["possibleCheapest"] == ["i", "j"]
    assert result["confirmedCheapest"] is None  # neither confirmed-qualifies


def test_confirmed_unique_cheapest_ties_and_provisional_rows():
    reference = Reference("ref", 50, 50)
    unique = iv.cheapest_above_bar([Box("a", 10, 12, 70, 72), Box("b", 15, 20, 60, 65), Box("weak", 1, 1, 10, 20)], reference)
    assert unique["confirmedCheapest"] == "a"
    assert unique["rows"]["weak"]["possibleCheapest"] == iv.DISPROVED
    tie = iv.cheapest_above_bar([Box("a", 10, 10, 70, 70), Box("b", 10, 10, 60, 60)], reference)
    assert tie["confirmedCheapest"] is None and tie["possibleCheapest"] == ["a", "b"]
    provisional = iv.cheapest_above_bar([Box("a", 10, 10, 70, 70, provisional=True)], reference)
    assert provisional["confirmedCheapest"] is None and provisional["possibleCheapest"] == ["a"]
    singleton = iv.cheapest_above_bar([Box("a", 10, 10, 70, 70)], reference)
    assert singleton["confirmedCheapest"] == "a"


def test_reference_as_competitor_and_as_candidate():
    reference = Reference("ref", 60, 60)
    # The reference competes and is surely cheaper than i: i can never be cheapest.
    result = iv.cheapest_above_bar([Box("i", 10, 10, 90, 90), Box("ref", 5, 5, 60, 60)], reference)
    assert result["rows"]["i"]["possibleCheapest"] == iv.DISPROVED
    assert result["rows"]["ref"]["possibleCheapest"] == iv.CERTIFIED
    assert result["confirmedCheapest"] == "ref"
    # A row whose best quality is below the reference's lowest value cannot be in K_r.
    low = iv.cheapest_above_bar([Box("i", 1, 1, 10, 20)], Reference("ref", 30, 40))
    assert low["rows"]["i"]["possibleCheapest"] == iv.DISPROVED


def test_bar_with_shared_factors_is_unresolved():
    assert iv.cheapest_above_bar([Box("a", 1, 1, 1, 1)], Reference("r", 0, 1), shared_factors=("x",))["status"] == iv.UNRESOLVED


def test_row_local_coupling_is_not_decided_at_corners():
    """E89 release test: i is dominated for every t although its box corner (1, 1) is undominated."""

    enclosure = [Box("i", 1, 2, 0, 1), Box("j", 1, 1, 0.5, 0.5), Box("k", 1.5, 1.5, 1, 1)]
    # The product enclosure alone would wrongly certify a possible membership.
    assert iv.frontier(enclosure)["i"]["possible"] == iv.CERTIFIED
    coupled = [Box("i", 1, 2, 0, 1, coupled=True)] + enclosure[1:]
    assert iv.frontier(coupled)["i"]["possible"] == iv.UNRESOLVED
    assert "E89" in iv.cheapest_above_bar(coupled, Reference("j", 0.5, 0.5))["reason"]
    # Solved over the coupled primitive t: C_i = 1 + t, Q_i = t.
    rows = [
        SharedBox("i", Affine(1, 1), Affine(1, 1), Affine(0, 1), Affine(0, 1)),
        SharedBox("j", Affine(1), Affine(1), Affine(0.5), Affine(0.5)),
        SharedBox("k", Affine(1.5), Affine(1.5), Affine(1), Affine(1)),
    ]
    result = iv.frontier_shared(rows, 0.0, 1.0)
    assert result["i"]["possible"] == iv.DISPROVED and result["i"]["definite"] == iv.DISPROVED


def test_validated_root_certificates_are_exact():
    """E108 fixtures: x^2 = 2 on [1, 2] has an irrational root; on [1, 1.4] it has none."""

    square_minus_two = (-2, 0, 1)
    assert iv.validated_root(square_minus_two, 1, 2) == iv.CERTIFIED
    assert iv.validated_root(square_minus_two, 1, 1.4) == iv.DISPROVED
    assert iv.validated_root(square_minus_two, -1.4, -1) == iv.DISPROVED  # decreasing branch
    assert iv.validated_root(square_minus_two, -1, 1) == iv.UNRESOLVED  # no sign change, slope changes sign
    assert iv.validated_root((-4, 0, 1), 2, 3) == iv.CERTIFIED  # exact root at an endpoint
    assert iv.point_certifies(square_minus_two, 1.414214) is False  # residual about 1e-6
    assert iv.point_certifies((-4, 0, 1), 2) is True
    assert iv._power_range(iv.Fraction(-2), iv.Fraction(1), 3) == (iv.Fraction(-8), iv.Fraction(1))
