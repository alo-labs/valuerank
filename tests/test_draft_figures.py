"""E265: the methodology draft's current figures are placeholders rendered from the build, and a check keeps them so."""

from __future__ import annotations

import json
import re
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
    routed = f.lint("Low end: GPT-6.1 Terra (max) on API-cost fallback and GPT-6 Luna (max) on ChatGPT Pro 500.", names, configurations, "2026-10-23")
    assert routed[0].startswith("line 1: unmarked configuration route(s) GPT-6.1 Terra (max), GPT-6 Luna (max)")
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


def test_pointers_name_a_field_every_ranking_has():
    """I47/I48: a pointer to generated output names a scores.json field, and that field resolves in every ranking."""

    text = "\n".join([
        "Bands are printed beside the ranks (scores.md; scores.json `diagnostics.rankSeparability.<basis>.bands`).",
        "The basket is in scores.json `admission` and the naming in scores.json `aaPlottedNames`.",
        "Shares are printed in scores.md.",
        "A bad field: scores.json `diagnostics.noSuchThing`.",
        "## Revision history",
        "History may cite scores.md freely.",
    ])
    problems = f.pointer_problems(text, SCORES)
    assert problems == ["line 1: the specification cites a generated document; cite the scores.json field instead: Bands are printed beside the ranks "
                        "(scores.md; scores.json `diagnostics.rankSeparability.<basis>.bands`).",
                        "line 3: the specification cites a generated document; cite the scores.json field instead: Shares are printed in scores.md.",
                        "pointer scores.json `diagnostics.noSuchThing` does not resolve in every ranking"]


def test_registry_facts_are_figures_and_typed_values_fail_even_in_dated_sentences():
    """I50 L5: the report window, search cutoff, evidence stages and vertex check come from the registry, and typing one
    by hand fails in any sentence that speaks of it, dated or not."""

    manifest = f.named_figures(SCORES)
    assert manifest["evidence.windowStart"] < manifest["evidence.windowEnd"] and int(manifest["evidence.searchGapDays"]) >= 0
    assert manifest["semianalysis.lastCurrent"] < manifest["semianalysis.supersededFrom"] < manifest["semianalysis.expiredFrom"] < manifest["semianalysis.demotedFrom"]
    assert manifest["aa.vertices"] == str(len(json.loads((DATA / "aa_frontier_capture.json").read_text())["frontier"]))
    text = "\n".join([
        f"On 2026-10-17 all {manifest['aa.vertices']} vertices matched at {manifest['aa.vertexMatchPx']} px.",
        f"Today all {{{{fig:aa.vertices}}}} vertices matched; the window is {{{{fig:evidence.windowStart}}}} to now.",
        f"AA's chart was captured {manifest['aa.capturedAt']}, previously {manifest['aa.previousCapture']}.",
        f"The report window opened on {manifest['evidence.windowStart']}; on 2026-09-01 it was expired from {manifest['semianalysis.expiredFrom']}.",
        "## Revision history",
        f"r1 typed {manifest['aa.vertices']} vertices.",
    ])
    problems = f.registry_problems(text, manifest)
    assert [problem.split(";")[0] for problem in problems] == [
        "line 1: registry value(s) typed by hand (aa.vertices, aa.vertexMatchPx)",
        "line 3: registry value(s) typed by hand (aa.capturedAt, aa.previousCapture)",
        "line 4: registry value(s) typed by hand (evidence.windowStart, semianalysis.expiredFrom)"]


def test_registry_figures_name_changes_and_refuse_two_semianalysis_dates():
    capture = json.loads((DATA / "aa_frontier_capture.json").read_text())
    plan = json.loads((DATA / "plan_cost_routes.json").read_text())
    capture["comparison_to_previous_capture"].update(added=["A (max)"], removed=["B (low)"])
    assert f.registry_figures(capture, plan, "2026-10-23")["aa.vertexChanges"] == "A (max) entered and B (low) left"
    plan["routes"] = [dict(route, sourcePublicationDate="2026-01-01") if i == 0 and route.get("sourceEvidenceId") == "semianalysis" else route
                      for i, route in enumerate(sorted(plan["routes"], key=lambda route: route.get("sourceEvidenceId") != "semianalysis"))]
    plan["routes"][0]["valueMultipleKind"] = "controlled_account_workload_projection"
    with pytest.raises(f.FigureError, match="one SemiAnalysis observation date"):
        f.registry_figures(capture, plan, "2026-10-23")
    plan["routes"] = [route for route in plan["routes"] if route.get("sourceEvidenceId") != "semianalysis"] + [plan["routes"][1]]
    plan["routes"] = [route for route in plan["routes"] if route.get("valueMultipleKind") not in f.pr.REPORT_KINDS]
    assert f.registry_figures(capture, plan, "2026-10-23")["evidence.reportRoutes"] == "none"


def test_duplicate_rows_name_the_chosen_harness(tmp_path):
    """I50 M2: a configuration a board lists twice is named with the row the selection rule chose (no board lists a v5
    configuration twice, so one AI Coding Daily record is given a second row)."""

    assert f.named_figures(SCORES)["duplicateRows"] == "none"
    data = tmp_path / "data"
    shutil.copytree(DATA, data, ignore=shutil.ignore_patterns("site", "*.html"))
    tracks = json.loads((data / "swe_tracks.json").read_text())
    record = next(record for record in tracks["records"] if record["leaf"] == "aiCodingDaily" and record["modelId"] == "gpt-6.1-sol-high")
    record.update(harness="Codex CLI", selection="one of 2 rows for this configuration, chosen by the harness of its Bug Hunt record (I50 M2)",
                  alternates=[{"harness": "OpenCode", "tested": "2026-10-17", "value": record["value"] - 1}])
    (data / "swe_tracks.json").write_text(json.dumps(tracks))
    assert f.named_figures(SCORES, data)["duplicateRows"] == (
        f"{f.display_names(SCORES)['gpt-6.1-sol-high']} on AI Coding Daily (Codex CLI chosen over OpenCode by the harness of its Bug Hunt record)")


def test_names_render_from_ids_and_names_in_undated_sentences_are_flagged():
    """I52 L6: a configuration named in a sentence about the current release is a {{name:ID}} placeholder."""

    names, configurations = f.known_names(SCORES), f.configuration_names(SCORES)
    assert f.render("{{name:gpt-6-astra}}", SCORES, {}) == f.display_names(SCORES)["gpt-6-astra"]
    with pytest.raises(f.FigureError, match="no configuration 'gone'"):
        f.render("{{name:gone}}", SCORES, {})
    problems = f.lint("The near set grew by GPT-6 Luna (max).\nThe near set grew by {{name:gpt-6-luna}}.\nA fixture with GPT-6 Luna (max).",
                      names, configurations, "2026-10-23")
    assert len(problems) == 1 and problems[0].startswith("line 1: unmarked configuration name(s) GPT-6 Luna (max) in an undated sentence")


def test_gap_fill_bars_figure_names_a_changed_bar():
    changed = json.loads(json.dumps(SCORES))
    changed["v3"]["diagnostics"]["gapFillBars"]["bases"]["api"][0]["survives"] = False
    assert f.named_figures(changed)["gapFillBars"].startswith("a bar's row changes at max api ")
    assert f.named_figures(SCORES)["gapFillBars"] == "every bar of every ranking keeps its row in all three"


def test_subset_strata_and_excluded_missing_leaves_render_from_the_build():
    """I53 M2, L3: the subset stratum's status and the excluded rows' missing leaves are figures."""

    manifest = f.named_figures(SCORES)
    strata = [item for section in (SCORES["v3"], *SCORES["v3Tracks"].values()) for basis in ("api", "plan")
              for item in section["costInfluence"][basis].get("subsetStrata", {}).values()]
    assert all(item["status"] in manifest["subsetStrata"] for item in strata) and manifest["excluded.missingCore"]
    empty = json.loads(json.dumps(SCORES))
    for section in (empty["v3"], *empty["v3Tracks"].values()):
        section["costInfluence"]["api"]["subsetStrata"] = section["costInfluence"]["plan"]["subsetStrata"] = {}
        section["incompleteEvidence"] = []
    figures = f.named_figures(empty)
    assert figures["subsetStrata"] == "no ranking has a subset stratum" and figures["excluded.missingCore"] == "none"


def test_excluded_configurations_partition_into_five_classes():
    """I58 M1: every excluded configuration falls in exactly one class, or the figures stop."""

    names = f.display_names(SCORES)
    order = lambda ids: f.series([names[item] for item in sorted(ids)])
    excluded = {item["id"] for item in SCORES["v3"]["incompleteEvidence"]} & {item["id"] for item in SCORES["v3Tracks"]["aicd"]["incompleteEvidence"]}
    figures = f.family_figures(SCORES, excluded, order)
    assert figures["excluded.frontierPrimaries"] == "Claude Opus 5.5 (xhigh), Gemini 4 Carbon (high), GPT-6 Astra (xhigh) and MiMo-V2.6-Flash"
    assert figures["excluded.frontierPoints"] == "Claude Haiku 5.5 (low), GPT-6 Luna (low), GPT-6.1 Sol (xhigh) and GPT-6.1 Terra (low)"
    assert figures["excluded.nearPrimaries"] == figures["excluded.nearPoints"] == figures["excluded.nearFamilyPoints"] == "none"
    with pytest.raises(f.FigureError, match="do not partition"):
        f.family_figures(SCORES, excluded | {"not-in-the-cohort"}, order)


def test_a_model_name_with_digits_is_not_a_count():
    names = f.known_names(SCORES)
    assert f.lint("Shown on the Claude Haiku 5.5 rows.", names, f.configuration_names(SCORES), "2026-10-25") == []
    assert f.lint("Shown on 12 rows.", names, f.configuration_names(SCORES), "2026-10-25")


def test_absence_statements_carry_a_marker_whose_claim_holds(tmp_path):
    """I60 M2: a sentence saying a source publishes or carries no field carries an {{absent:KEY}} marker, and the claim
    is tested against the pinned data, so a field that appears forces the sentence to change."""

    # Every claim the published draft cites holds against the pinned data. (bughunt.minimaxFlash names MiniMax-M3.1-Flash,
    # which left the cohort at v5 and has no Bug Hunt search record any more; the draft no longer cites it.)
    cited = set(re.findall(r"\{\{absent:([^}|]+)\}\}", f.latest_source().read_text()))
    assert cited and cited <= set(f.ABSENCE_CLAIMS)
    assert all(f.ABSENCE_CLAIMS[key][1](DATA) for key in cited)
    text = "\n".join([
        "AA publishes no interval for that leaf.",
        "AA's run publishes no interval{{absent:aa.terminalBenchInterval}}.",
        "The board publishes no error{{absent:aicd.error}}.",
        "## Revision history",
        "History is not captured here.",
    ])
    assert f.absence_problems(text) == ["line 1: an absence statement without an {{absent:KEY}} marker: AA publishes no interval for that leaf."]
    assert f.render("x{{absent:aicd.error}}y", SCORES, {}) == "xy"
    with pytest.raises(f.FigureError, match="no absence claim 'nope'"):
        f.render("{{absent:nope}}", SCORES, {})
    # A field that appears in the pinned data makes the claim fail.
    data = tmp_path / "data"
    shutil.copytree(DATA, data, ignore=shutil.ignore_patterns("site", "*.html"))
    snapshot = json.loads((data / "aa" / "aa_v432_snapshot.json").read_text())
    snapshot["pages"][0]["model"]["terminalBench40Interval"] = {"lower": 1, "upper": 2}
    (data / "aa" / "aa_v432_snapshot.json").write_text(json.dumps(snapshot))
    assert f.absence_problems("AA's run publishes no interval{{absent:aa.terminalBenchInterval}}.", data) == [
        "line 1: absence claim aa.terminalBenchInterval (AA's pages carry no Terminal-Bench 4.0 interval) no longer holds; rewrite the sentence"]
    assert not f.ABSENCE_CLAIMS["aa.leafIntervals"][1](data)


def test_absence_claim_helpers_read_nested_keys_and_registries(tmp_path):
    assert f._keys({"a": [{"b": 1}, {"c": {"d": 2}}]}) == {"a", "b", "c", "d"}
    data = tmp_path / "data"
    data.mkdir()
    (data / "bug_hunt.json").write_text(json.dumps({"models": [{"modelId": "m", "fixedOf105": None}]}))
    (data / "leaf_evidence.json").write_text(json.dumps({"searches": [{"modelId": "m", "leaf": "bugHunt", "result": "not found"}]}))
    assert f._bug_hunt_search_empty("m")(data) and not f._bug_hunt_search_empty("other")(data)
    (data / "plan_cost_routes.json").write_text(json.dumps({"routes": [{"sourceEvidenceId": "semianalysis", "contentSha256": "x"}]}))
    assert not f._semianalysis_unhashed(data)
    assert f.fmt(-0.83, "signed.2", {}) == "−0.83" and f.fmt(4.1, "signed.2", {}) == "+4.10"


def test_lint_flags_a_hand_typed_list_of_owner_assumptions():
    """I72 L1: transfers listed beside fallbacks or ceilings must come with every owner-assumption kind."""

    flagged = "The anchors include owner-named transfers and API-cost fallbacks alike."
    assert any("owner-named transfers listed" in problem for problem in f.lint(flagged, []))
    assert any("owner-named transfers listed" in problem for problem in f.lint("Ceilings, fallbacks and owner-named transfers count.", []))
    for fine in ("The anchors include owner assumptions of every kind and API-cost fallbacks alike.",
                 "Rows on {{fig:evidence.assumptionKinds}}, owner-named transfers and fallbacks.", "An owner-named transfer names its donor."):
        assert not any("owner-named transfers listed" in problem for problem in f.lint(fine, []))


def test_the_generated_docs_are_held_to_the_assumption_list_rule(tmp_path):
    """I73 L1: README, methodology and scores are scanned too; a missing doc is skipped."""

    (tmp_path / "methodology.md").write_text("The Plan anchors include transfers and fallbacks.\nThey include owner assumptions and API fallbacks.\n")
    problems = f.assumption_list_problems(tmp_path)
    assert len(problems) == 1 and problems[0].startswith("methodology.md: line 1:")
    assert f.assumption_list_problems(ROOT) == []
