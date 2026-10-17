"""Tests for the Intelligence Index vs. cost Pareto-frontier module."""

import json
import runpy
import sys

import pytest

from valuerank import frontier as fr


def pt(name, intelligence, cost, family=None, effort=None, **extra):
    return {
        "name": name,
        "family": family or name,
        "effort": effort,
        "intelligence": intelligence,
        "cost_usd": cost,
        **extra,
    }


# A: cheapest; B, B2: exact tie; C: best; D: same intelligence as B but costlier
# (dominated); E: expensive and weak (dominated).
A = pt("A", 10.0, 1.0)
B = pt("B", 20.0, 5.0)
B2 = pt("B2", 20.0, 5.0)
C = pt("C", 30.0, 20.0)
D = pt("D", 20.0, 8.0)
E = pt("E", 5.0, 50.0)
POINTS = [E, D, C, B2, A, B]


def names(items):
    return [p["name"] for p in items]


# --- pareto_frontier -------------------------------------------------------


def test_frontier_known_set_sorted_by_cost_with_tie_kept():
    result = fr.pareto_frontier(POINTS)
    assert names(result) == ["A", "B", "B2", "C"]
    assert [p["cost_usd"] for p in result] == [1.0, 5.0, 5.0, 20.0]
    assert all(p["frontier"] is True for p in result)


def test_frontier_excludes_equal_intelligence_higher_cost():
    assert "D" not in names(fr.pareto_frontier(POINTS))
    assert "E" not in names(fr.pareto_frontier(POINTS))


def test_frontier_equal_cost_lower_intelligence_is_dominated():
    low = pt("low", 10.0, 5.0)
    result = fr.pareto_frontier([low, B])
    assert names(result) == ["B"]


def test_frontier_copies_and_preserves_extra_keys():
    p = pt("X", 1.0, 1.0, url="u", extra=[1])
    result = fr.pareto_frontier([p])
    assert result[0]["url"] == "u" and result[0]["extra"] == [1]
    assert result[0] is not p
    assert "frontier" not in p


def test_frontier_is_deterministic_for_ties():
    assert names(fr.pareto_frontier(POINTS)) == names(
        fr.pareto_frontier(list(reversed(POINTS))))


def test_frontier_empty():
    assert fr.pareto_frontier([]) == []


# --- frontier_gaps ---------------------------------------------------------


def test_gaps_hand_computed():
    frontier = fr.pareto_frontier(POINTS)
    out = {p["name"]: p for p in fr.frontier_gaps(POINTS, frontier)}
    # D: cost 8 -> best frontier intelligence at cost<=8 is 20 -> gap 0;
    # cheapest frontier cost reaching 20 is 5 -> ratio 8/5 = 1.6.
    assert out["D"]["intelligence_gap"] == 0.0
    assert out["D"]["cost_ratio"] == pytest.approx(1.6)
    # E: cost 50 -> best at cost<=50 is 30 -> gap 25; intelligence 5 reached
    # at cost 1 -> ratio 50.
    assert out["E"]["intelligence_gap"] == 25.0
    assert out["E"]["cost_ratio"] == 50.0


def test_gaps_for_frontier_points_are_neutral():
    frontier = fr.pareto_frontier(POINTS)
    out = {p["name"]: p for p in fr.frontier_gaps(POINTS, frontier)}
    for n in ("A", "B", "B2", "C"):
        assert out[n]["intelligence_gap"] == 0
        assert out[n]["cost_ratio"] == 1.0


def test_gaps_nonfrontier_with_real_shortfall():
    # F: cost 6, intelligence 15 -> best at cost<=6 is 20 -> gap 5.
    f = pt("F", 15.0, 6.0)
    pts = [A, B, C, f]
    out = {p["name"]: p for p in fr.frontier_gaps(pts, fr.pareto_frontier(pts))}
    assert out["F"]["intelligence_gap"] == 5.0
    assert out["F"]["cost_ratio"] == pytest.approx(6.0 / 5.0)


def test_gaps_none_when_no_frontier_at_or_below_cost():
    cheap = pt("cheap", 1.0, 0.5)
    out = fr.frontier_gaps([cheap], [C])
    assert out[0]["intelligence_gap"] is None
    assert out[0]["cost_ratio"] == pytest.approx(0.5 / 20.0)


def test_gaps_none_when_no_frontier_reaches_intelligence():
    strong = pt("strong", 99.0, 100.0)
    out = fr.frontier_gaps([strong], [A])
    assert out[0]["cost_ratio"] is None
    assert out[0]["intelligence_gap"] == 0.0


def test_gaps_zero_reference_cost_gives_none_ratio():
    free = pt("free", 10.0, 0.0)
    paid = pt("paid", 10.0, 2.0)
    out = {p["name"]: p for p in fr.frontier_gaps(
        [free, paid], fr.pareto_frontier([free, paid]))}
    assert out["free"]["cost_ratio"] == 1.0
    assert out["paid"]["cost_ratio"] is None


def test_gaps_preserve_extra_keys_and_do_not_mutate():
    p = pt("F", 15.0, 6.0, note="keep")
    out = fr.frontier_gaps([p], fr.pareto_frontier([A, B, C]))
    assert out[0]["note"] == "keep"
    assert "intelligence_gap" not in p


# --- classify --------------------------------------------------------------

LADDER = [pt("A", 10.0, 1.0), pt("B", 20.0, 5.0), pt("C", 30.0, 20.0)]


def tiers(extra, **kw):
    return {p["name"]: p["tier"] for p in fr.classify(LADDER + extra, **kw)}


def test_classify_frontier_points():
    t = tiers([])
    assert set(t.values()) == {"frontier"}


def test_classify_equal_intelligence_higher_cost_is_near_by_zero_gap():
    # D matches the best frontier intelligence at its cost (gap 0).
    assert {p["name"]: p["tier"] for p in fr.classify(POINTS)}["D"] == "near"


def test_classify_gap_boundary_inclusive():
    # Gap exactly 3.0 (best at cost<=40 is 30; intelligence 27).
    assert tiers([pt("H", 27.0, 40.0)])["H"] == "near"
    # Gap 3.1 is dominated.
    assert tiers([pt("H", 26.9, 40.0)])["H"] == "dominated"


def test_classify_zero_gap_is_near_even_with_high_cost_ratio():
    # Gap 0 (B's 20 is reachable below cost 8.95) but ratio 8.95 / 5 = 1.79.
    out = {p["name"]: p for p in fr.classify(LADDER + [pt("L", 20.0, 8.95)])}
    assert out["L"]["tier"] == "near"
    assert out["L"]["intelligence_gap"] == 0.0
    assert out["L"]["cost_ratio"] == pytest.approx(1.79)


def test_classify_large_gap_is_dominated_even_with_low_cost_ratio():
    # Gap 20 - 7 = 13 although the point costs only 1.38x the cheapest
    # frontier point that reaches Index 7.
    ladder = [pt("X", 20.0, 5.0), pt("C", 30.0, 20.0)]
    out = {p["name"]: p for p in fr.classify(ladder + [pt("W", 7.0, 6.9)])}
    assert out["W"]["tier"] == "dominated"
    assert out["W"]["intelligence_gap"] == 13.0
    assert out["W"]["cost_ratio"] == pytest.approx(1.38)


def test_classify_point_cheaper_than_every_frontier_point_is_dominated(monkeypatch):
    cheap = pt("cheap", 29.0, 0.5)
    monkeypatch.setattr(fr, "pareto_frontier", lambda points: [
        {**C, "frontier": True}])
    out = {p["name"]: p for p in fr.classify([C, cheap])}
    assert out["cheap"]["intelligence_gap"] is None
    assert out["cheap"]["tier"] == "dominated"
    assert out["C"]["tier"] == "frontier"


def test_classify_custom_gap_threshold():
    extra = [pt("L", 12.0, 7.6)]  # gap 8
    assert tiers(extra, max_intelligence_gap=8.0)["L"] == "near"
    assert tiers(extra, max_intelligence_gap=7.9)["L"] == "dominated"


def test_classify_has_no_cost_ratio_parameter():
    with pytest.raises(TypeError):
        fr.classify(LADDER, max_cost_ratio=1.5)
    assert not hasattr(fr, "MAX_COST_RATIO")


def test_classify_preserves_extra_keys_and_metrics():
    out = fr.classify([pt("H", 27.0, 40.0, note="n")] + LADDER)
    h = next(p for p in out if p["name"] == "H")
    assert h["note"] == "n"
    assert h["intelligence_gap"] == 3.0 and h["cost_ratio"] == 2.0
    assert h["frontier"] is False
    assert next(p for p in out if p["name"] == "A")["frontier"] is True


def test_classify_empty():
    assert fr.classify([]) == []


# --- family_selection ------------------------------------------------------


def fam(name, intelligence, cost, family, effort=None):
    return pt(name, intelligence, cost, family=family, effort=effort)


def test_family_prefers_frontier_over_near_and_orders_groups():
    pts = [
        fam("F1 (low)", 10.0, 1.0, "F1", "low"),
        fam("F1 (high)", 20.0, 5.0, "F1", "high"),   # frontier, best of F1
        fam("F1 (max)", 21.0, 25.0, "F1", "max"),    # near: gap 0
        fam("G (x)", 30.0, 20.0, "G"),               # frontier, highest overall
        fam("N (a)", 27.0, 40.0, "N"),               # near by gap 3
        fam("Z", 1.0, 100.0, "Z"),                   # dominated: dropped
    ]
    out = fr.family_selection(fr.classify(pts), {"G"})
    assert [r["family"] for r in out] == ["G", "F1", "N"]
    assert [r["tier"] for r in out] == ["frontier", "frontier", "near"]
    f1 = out[1]
    assert f1["configuration"]["name"] == "F1 (high)"
    assert f1["other_configurations"] == ["F1 (low)", "F1 (max)"]
    assert [r["in_roster"] for r in out] == [True, False, False]


def test_family_near_tiebreak_gap_then_cost():
    base = [pt("A", 10.0, 1.0), pt("C", 30.0, 20.0)]
    pts = base + [
        fam("N1", 28.0, 60.0, "N"),   # gap 2
        fam("N2", 29.0, 70.0, "N"),   # gap 1 -> best
        fam("N3", 29.0, 65.0, "N"),   # gap 1, cheaper -> wins tie
    ]
    out = fr.family_selection(fr.classify(pts), set())
    n = next(r for r in out if r["family"] == "N")
    assert n["tier"] == "near"
    assert n["configuration"]["name"] == "N3"
    assert n["other_configurations"] == ["N1", "N2"]


def test_family_frontier_tiebreak_highest_intelligence_then_cost():
    pts = [fam("P1", 20.0, 5.0, "P"), fam("P2", 30.0, 20.0, "P")]
    out = fr.family_selection(fr.classify(pts), set())
    assert out[0]["configuration"]["name"] == "P2"
    # exact tie: lowest cost then name decides deterministically
    tie = [fam("T2", 20.0, 5.0, "T"), fam("T1", 20.0, 5.0, "T")]
    out = fr.family_selection(fr.classify(tie), set())
    assert out[0]["configuration"]["name"] == "T1"


def test_family_orders_by_intelligence_desc_within_tier():
    pts = [pt("A", 10.0, 1.0), pt("C", 30.0, 20.0),
           pt("N1", 27.0, 40.0), pt("N2", 28.0, 45.0)]
    out = fr.family_selection(fr.classify(pts), set())
    assert [r["family"] for r in out] == ["C", "A", "N2", "N1"]


def test_family_empty():
    assert fr.family_selection([], set()) == []


# --- parse_tooltip ---------------------------------------------------------

TIP = (
    "Claude Opus 5.5 (max with fallback)\nArtificial Analysis Intelligence "
    "Index\n58\nCost to Run Intelligence Index (USD, Log Scale)\n$8,708.20"
)


def test_parse_fallback_effort_and_thousands():
    assert fr.parse_tooltip(TIP) == {
        "name": "Claude Opus 5.5 (max with fallback)",
        "family": "Claude Opus 5.5",
        "effort": "max with fallback",
        "intelligence": 58.0,
        "cost_usd": 8708.20,
        "footnote": None,
    }


def test_parse_simple_effort():
    tip = ("GPT-6 Luna (low)\nArtificial Analysis Intelligence Index\n22\n"
           "Cost to Run Intelligence Index (USD, Log Scale)\n$10.63")
    out = fr.parse_tooltip(tip)
    assert (out["family"], out["effort"]) == ("GPT-6 Luna", "low")
    assert out["intelligence"] == 22.0 and out["cost_usd"] == 10.63


def test_parse_no_effort_blank_lines_and_reordered_fields():
    tip = ("\n  Gemini 3.8 Flash \n\nCost to Run Intelligence Index (USD)\n"
           "$1,234\nArtificial Analysis Intelligence Index\n47.5\n")
    out = fr.parse_tooltip(tip)
    assert out["name"] == "Gemini 3.8 Flash"
    assert out["family"] == "Gemini 3.8 Flash" and out["effort"] is None
    assert out["intelligence"] == 47.5 and out["cost_usd"] == 1234.0


STAR_TIP = (
    "Claude Haiku 5.5 (medium)*\nCost to Run Intelligence Index (USD, Log Scale)\n"
    "$56.36\nArtificial Analysis Intelligence Index\n34\nClick for more info\n\n"
    "* Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which "
    "are not currently reflected; see the methodology page."
)


def test_parse_starred_tooltip_strips_star_and_collects_footnote():
    out = fr.parse_tooltip(STAR_TIP)
    assert out == {
        "name": "Claude Haiku 5.5 (medium)",
        "family": "Claude Haiku 5.5",
        "effort": "medium",
        "intelligence": 34.0,
        "cost_usd": 56.36,
        "footnote": ("Claude Haiku 5.5 has 5x higher pricing on longer-context "
                     "inputs which are not currently reflected; see the "
                     "methodology page."),
    }


def test_parse_footnote_lines_do_not_leak_into_metrics_and_join():
    tip = ("M*\nArtificial Analysis Intelligence Index\n10\n"
           "* Artificial Analysis Intelligence Index is rescaled\n"
           "Cost to Run Intelligence Index\n$5\nClick for more info\n"
           "* second note")
    out = fr.parse_tooltip(tip)
    assert out["name"] == "M" and out["intelligence"] == 10.0
    assert out["cost_usd"] == 5.0
    assert out["footnote"] == ("Artificial Analysis Intelligence Index is "
                               "rescaled second note")


def test_parse_click_for_more_info_is_ignored_and_footnote_absent_is_none():
    out = fr.parse_tooltip(TIP + "\nClick for more info")
    assert out["footnote"] is None
    assert out["name"] == "Claude Opus 5.5 (max with fallback)"


def test_parse_missing_numbers_returns_none():
    assert fr.parse_tooltip("") is None
    assert fr.parse_tooltip("Name only") is None
    no_cost = "M\nArtificial Analysis Intelligence Index\n58"
    assert fr.parse_tooltip(no_cost) is None
    no_int = "M\nCost to Run Intelligence Index\n$5"
    assert fr.parse_tooltip(no_int) is None


def test_parse_non_numeric_value_returns_none():
    tip = ("M\nArtificial Analysis Intelligence Index\nn/a\n"
           "Cost to Run Intelligence Index\n$5")
    assert fr.parse_tooltip(tip) is None


def test_parse_label_as_last_line_returns_none():
    tip = "M\nCost to Run Intelligence Index\n$5\nArtificial Analysis Intelligence Index"
    assert fr.parse_tooltip(tip) is None


# --- CLI -------------------------------------------------------------------


def tip(name, intel, cost):
    return (f"{name}\nArtificial Analysis Intelligence Index\n{intel}\n"
            f"Cost to Run Intelligence Index (USD, Log Scale)\n${cost}")


def write_capture(tmp_path):
    cap = {"points": [
        {"tip": tip("Alpha (low)", 10, "1.00"), "x": 1},
        {"tip": tip("Alpha (high)", 20, "5.00"), "x": 2},
        {"tip": tip("Beta", 30, "20.00"), "x": 3},
        {"tip": tip("Gamma-Pro", 27, "40.00"), "x": 4},
        {"tip": tip("Delta", 1, "100.00"), "x": 5},
        {"tip": "garbage", "x": 6},
    ]}
    path = tmp_path / "cap.json"
    path.write_text(json.dumps(cap))
    return path


def test_cli_without_roster(tmp_path, capsys):
    assert fr.main([str(write_capture(tmp_path))]) == 0
    rep = json.loads(capsys.readouterr().out)
    assert [p["name"] for p in rep["frontier"]] == [
        "Alpha (low)", "Alpha (high)", "Beta"]
    assert [p["name"] for p in rep["near"]] == ["Gamma-Pro"]
    assert rep["counts"] == {"total": 5, "frontier": 3, "near": 1,
                             "dominated": 1, "unparsed": 1}
    assert rep["unparsed"] == [{"tip": "garbage", "x": 6}]
    assert rep["frontier"][0]["x"] == 1  # extra capture keys preserved
    assert [f["family"] for f in rep["families"]] == [
        "Beta", "Alpha", "Gamma-Pro"]
    assert all(f["in_roster"] is False for f in rep["families"])


def test_cli_reports_footnotes_and_gap_only_near_policy(tmp_path, capsys):
    cap = {"points": [
        {"tip": tip("Alpha (low)", 10, "1.00")},
        {"tip": tip("Alpha (high)", 20, "5.00")},
        {"tip": tip("Beta", 30, "20.00")},
        # gap 0, cost ratio 1.79: near under the gap-only policy
        {"tip": tip("Slow (x)", 20, "8.95")},
        # gap 13, cost ratio 1.38: dominated
        {"tip": tip("Weak", 7, "6.90")},
        {"tip": STAR_TIP.replace("$56.36", "$57.00")},
    ]}
    path = tmp_path / "cap.json"
    path.write_text(json.dumps(cap))
    assert fr.main([str(path)]) == 0
    rep = json.loads(capsys.readouterr().out)
    assert {p["name"] for p in rep["near"]} == {"Slow (x)"}
    assert rep["near"][0]["cost_ratio"] == pytest.approx(1.79)
    assert rep["counts"] == {"total": 6, "frontier": 4, "near": 1,
                             "dominated": 1, "unparsed": 0}
    haiku = next(p for p in rep["frontier"] if p["family"] == "Claude Haiku 5.5")
    assert haiku["name"] == "Claude Haiku 5.5 (medium)"
    assert haiku["footnote"].startswith("Claude Haiku 5.5 has 5x higher pricing")
    assert next(p for p in rep["frontier"] if p["family"] == "Beta")["footnote"] is None


def test_cli_with_roster(tmp_path, capsys):
    roster = tmp_path / "roster.json"
    roster.write_text(json.dumps([
        {"id": "gamma-pro", "displayName": "gamma pro", "urls": []},
        {"id": "beta", "displayName": "BETA", "urls": []},
    ]))
    assert fr.main([str(write_capture(tmp_path)), "--roster", str(roster)]) == 0
    rep = json.loads(capsys.readouterr().out)
    flags = {f["family"]: f["in_roster"] for f in rep["families"]}
    assert flags == {"Beta": True, "Alpha": False, "Gamma-Pro": True}


def test_main_guard(tmp_path, capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["frontier", str(write_capture(tmp_path))])
    monkeypatch.delitem(sys.modules, "valuerank.frontier")
    with pytest.raises(SystemExit) as exc:
        runpy.run_module("valuerank.frontier", run_name="__main__")
    assert exc.value.code == 0
    assert json.loads(capsys.readouterr().out)["counts"]["total"] == 5
