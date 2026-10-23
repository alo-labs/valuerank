"""E265: the methodology draft's current figures are placeholders rendered from the build, and a check keeps them so."""

from __future__ import annotations

import json
import runpy
import shutil
import sys

import pytest

from valuerank import draft_figures as f
from valuerank.paths import DATA, ROOT

SCORES = json.loads((DATA / "scores.json").read_text())


def test_the_published_draft_is_the_rendering_of_its_source():
    """The real check: the newest draft matches its source against the current data, with nothing left unmarked."""

    assert f.check() == []


def test_resolve_reads_keys_indices_selectors_and_quoted_keys():
    document = {"rows": [{"id": "a", "v": {"0.3": 2}}, {"id": "b", "v": [5, 6]}]}
    assert f.resolve(document, 'rows[id=a].v["0.3"]') == 2
    assert f.resolve(document, "rows[1].v[1]") == 6
    with pytest.raises(f.FigureError, match="0 items with id=c"):
        f.resolve(document, "rows[id=c].v")
    with pytest.raises(f.FigureError, match="no key 'w'"):
        f.resolve(document, "rows[0].w")


def test_formats_cover_numbers_names_lists_and_ranges():
    names = {"a": "A (max)", "b": "B"}
    assert [f.fmt(value, spec, names) for value, spec in (
        (3, None), ("x", None), ([1, 2], "count"), ("a", "name"), (["a", "b"], "names"), ([], "names"), (["p", "q", "r"], "list"),
        (7, "str"), ([2, 2], "range"), ([1, 3], "range"), (2.6, "int"), (-0.904, "pct.0"), (1233.11, "usd.2"), (12078.25, ",.1f"), (3.014, ".2f"),
    )] == ["3", "x", "2", "A (max)", "A (max) and B", "none", "p, q and r", "7", "2", "1–3", "3", "-90%", "$1,233.11", "12,078.2", "3.01"]
    for value, spec, message in ((1.5, None, "needs a format"), (True, None, "needs a format"), ("x", ".2f", "not a number"), (1.0, "bogus", "unknown format")):
        with pytest.raises(f.FigureError, match=message):
            f.fmt(value, spec, names)


def test_render_resolves_every_scope_and_names_its_failures():
    manifest = {"cohort.plotted": "29"}
    text = "{{fig:cohort.plotted}} / {{max:anchorVersion}} / {{aicd:anchorVersion}} / {{top:aaPlottedNames.noEffort|list}}"
    assert f.render(text, SCORES, manifest).startswith(f"29 / {SCORES['v3']['anchorVersion']} / {SCORES['v3Tracks']['aicd']['anchorVersion']} / ")
    with pytest.raises(f.FigureError, match="no named figure"):
        f.render("{{fig:missing}}", SCORES, manifest)
    with pytest.raises(f.FigureError, match="max:rows"):
        f.render("{{max:rows[99].id}}", SCORES, manifest)


def test_the_manifest_covers_both_rankings_and_the_external_facts():
    manifest = f.named_figures(SCORES)
    assert {"max.weight.livebench2Overall", "aicd.weight.aiCodingDaily", "max.share.independent", "cohort.plotted", "excluded.names",
            "aa.firstVertex", "max.beyondAnchors.api", "mimoCeilings.tiers"} <= set(manifest)
    assert manifest["max.weight.livebench2Overall"] == "15" and manifest["max.share.independent"] == "34%"
    assert all(isinstance(value, str) for value in manifest.values())


def test_lint_flags_unmarked_today_figures_names_and_undated_counts():
    names = f.known_names(SCORES)
    configurations = f.configuration_names(SCORES)
    source = "\n".join([
        "Today the margin is 4.0 and GPT-6 Luna (max) leads.",
        "Today the margin is {{max:x}} under O39 and version 3, with 1.96 × √2 for Claude Opus 5.5 on 2026-10-23.",
        "The basket prices 7 of 9.",
        "On 2026-10-19 the basket priced 7 of 9.",
        "## Revision history",
        "Today the margin was 4.0.",
    ])
    problems = f.lint(source, names, configurations)
    assert len(problems) == 3
    assert "unmarked configuration name(s) GPT-6 Luna (max)" in problems[0] and "unmarked figure(s) 4.0" in problems[1]
    assert "unmarked count(s) 7 of 9" in problems[2]
    assert f.lint("A rule with no history section.", names, configurations) == []
    # I43: counts of cohort things and dollar amounts are figures too, and a same-day or bold-label date does not date them.
    widened = f.lint("\n".join([
        "The max-effort ranking has 14 leaves.",
        "- **Cohort (owner decision O51, 2026-10-23)**: 29 configurations at $10.63.",
        "On 2026-10-19 it had 14 leaves; at O53 it had 13 leaves.",
        "A fixture with 3 rows; 4 against 5 headline qualifiers.",
    ]), names, configurations, "2026-10-23")
    assert [problem.split(" in an")[0] for problem in widened] == [
        "line 1: unmarked count(s) 14 leaves", "line 2: unmarked count(s) 29 configurations, $10.63", "line 4: unmarked count(s) 4 against 5"]
    # I44 L1: a configuration named with its plan or fallback states a current route.
    routed = f.lint("Low end: GPT-6 Luna (max) on ChatGPT Pro 500 and Gemini 4 Argon (high) on API-cost fallback.", names, configurations, "2026-10-23")
    assert routed[0].startswith("line 1: unmarked configuration route(s) Gemini 4 Argon (high), GPT-6 Luna (max)")
    assert f.dated("**Rule (O1, 2026-10-01)**: text", "2026-10-23") is False and f.dated("Seen on 2026-10-23.", "2026-10-23") is False
    assert f.dated("Seen on 2026-10-01.", None) is True


def test_plan_band_figures_name_straddlers_and_wide_spans():
    section = {"diagnostics": {"rankSeparability": {"plan": {"bands": {"a@1": [1, 2], "a@2": [3, 3], "b@1": [1, 2]}, "medianSeparation": 1.0}}},
               "planRows": [{"id": "a@1", "configurationId": "a", "value": 10.0}, {"id": "a@2", "configurationId": "a", "value": 8.0},
                            {"id": "b@1", "configurationId": "b", "value": None}]}
    figures = f.plan_band_figures("max", section, {"a": "A (max)", "b": "B"})
    assert figures == {"max.planBandStraddlers": "A (max)", "max.planSpanBeyondThreshold": "A (max)"}


def copy_world(tmp_path):
    spec, data = tmp_path / "spec", tmp_path / "data"
    spec.mkdir()
    shutil.copytree(DATA, data, ignore=shutil.ignore_patterns("site", "*.html"))
    source = f.latest_source()
    shutil.copy2(source, spec / source.name)
    shutil.copy2(f.published(source), spec / f.published(source).name)
    return spec, data, source.name


def test_check_reports_a_stale_draft_a_stale_manifest_and_a_broken_placeholder(tmp_path):
    spec, data, name = copy_world(tmp_path)
    assert f.check(spec, data) == []
    (spec / name.replace(".src.md", ".md")).write_text("stale")
    (data / f.MANIFEST).write_text("{}")
    problems = f.check(spec, data)
    assert any("is not the rendering" in problem for problem in problems) and any("data/figures.json is stale" in problem for problem in problems)
    (spec / name).write_text("{{fig:missing}}")
    assert f.check(spec, data) == [f"{name}: no named figure 'missing'"]
    (spec / name).unlink()
    with pytest.raises(f.FigureError, match="no draft source"):
        f.latest_source(spec)


def test_main_writes_the_manifest_renders_and_checks(tmp_path, capsys):
    spec, data, name = copy_world(tmp_path)
    (spec / name.replace(".src.md", ".md")).unlink()
    assert f.main(["manifest"], spec, data) == 0 and json.loads((data / f.MANIFEST).read_text())
    assert f.main(["check"], spec, data) == 1 and "is not the rendering" in capsys.readouterr().err
    assert f.main(["render"], spec, data) == 0
    assert f.main(["check"], spec, data) == 0


def test_module_entry_point(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["draft_figures", "check"])
    monkeypatch.delitem(sys.modules, "valuerank.draft_figures", raising=False)
    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.draft_figures", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert ROOT.exists()
