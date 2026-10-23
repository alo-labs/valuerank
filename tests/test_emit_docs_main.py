"""End-to-end behaviour of ``emit_docs.main`` against temporary repo copies (methodology v3)."""

import copy
import json
import re
import runpy
import shutil
import sys

import pytest

from test_emit_docs_support import committed, edit_json, emit
from valuerank import emit_docs
from valuerank import paths


@pytest.fixture
def emitted(repo_copy, pinned_clock):
    assert emit(repo_copy) == 0
    return repo_copy


def v3_document():
    return json.loads(committed("data/scores.json"))["v3"]


def table_rows(text, header_prefix):
    """Rows of the markdown table whose header line starts with ``header_prefix``."""

    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(header_prefix))
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        rows.append(line)
    return rows


def cells(row):
    return [cell.strip() for cell in row.strip("|").split(" | ")]


def test_readme_ranks_configurations_in_plan_order(emitted):
    v3 = v3_document()
    readme = (emitted / "README.md").read_text()
    rows = [cells(row) for row in table_rows(readme, "| Plan rank | API rank | Configuration")]
    by_plan = sorted((row for row in v3["rows"] if row["planScore"]["rank"] is not None), key=lambda row: row["planScore"]["rank"])
    ranked, unranked = rows[:len(by_plan)], rows[len(by_plan):]
    assert [int(row[0]) for row in ranked] == [row["planScore"]["rank"] for row in by_plan]
    assert [int(row[1]) for row in ranked] == [row["api"]["rank"] for row in by_plan]
    assert [row[3] for row in ranked] == [f"{row['planScore']['value']:.1f}" for row in by_plan]
    assert [row[4] for row in ranked] == [f"{row['api']['value']:.1f}" for row in by_plan]
    # O53/O54: the leading max-effort ranking has one configuration per family at its top effort.
    assert rows[0][2].startswith("[Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/)")
    assert any(row[2].startswith("[GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/)") for row in ranked)
    # Every cohort configuration has an AA cost today, so no row is unranked for want of one.
    assert unranked == []
    assert "- **no cost**: AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown." in readme
    assert readme.startswith("# ValueRank\n")
    scored = sum(1 for row in v3["rows"] if row["api"]["rank"] is not None)
    assert f"**Scope:** {len(v3['rows'])} cohort configurations ({scored} with a value score)" in readme and scored == len(v3["rows"])
    assert f"**Methodology:** {v3['methodologyVersion']} · {v3['basketVersion']} · anchor version {v3['anchorVersion']}" in readme
    assert "## AA intelligence and total-cost comparison" in readme


def test_readme_flags_fallback_and_subset_rows(emitted):
    readme = (emitted / "README.md").read_text()
    rows = {cells(row)[2].split("](")[0].lstrip("["): cells(row) for row in table_rows(readme, "| Plan rank | API rank | Configuration")}
    assert rows["Gemini 4 Argon (high)"][9] == "—" and rows["Gemini 4 Argon (high)"][10] == "API-cost fallback"
    # O50/O17: the max-effort ranking admits the Coding Agent Index, which MiMo-V2.6-Pro lacks; O46: its quota-ceiling route.
    assert rows["MiMo-V2.6-Pro"][10] == "subset cost"
    assert rows["MiMo-V2.6-Pro"][9] == "MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption)"
    assert rows["GPT-6 Astra (max)"][6] == "100%" and rows["GPT-6 Astra (max)"][10] == "—"
    assert rows["Claude Haiku 5.5 (max)"][10] == "AA cost caveat"
    assert rows["DeepSeek V4.1 Flash 1017 (max)"][10] == "subset cost, API-cost fallback"
    # O45: GPT-6.1 Sol keeps its own SemiAnalysis figure.
    assert rows["GPT-6.1 Sol (max)"][9] == "ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured)"


def test_readme_states_what_the_interval_outputs_support(emitted):
    readme = (emitted / "README.md").read_text()
    assert "the definite frontier (no configuration can beat it on both cost and quality" in readme
    assert "GPT-6 Luna (max); the possible frontier adds none. Not evaluable on this workload: DeepSeek V4.1 Flash 1017 (max), MiMo-V2.6-Pro." in readme
    # E192: the bar is a quality level, so the output compares alternatives instead of returning the bar setter.
    assert "Cheapest at or above quality 54.2: GPT-6.1 Sol (max) (confirmed)." in readme
    # E196: the nominal cost weight is printed with cost's share of the variance in value.
    assert "value is a 25% cost score (nominal weight; 103% of API and 20% of Plan value variance)" in readme
    assert "Plan basis: interval outputs not evaluated (no row has FullCost and an identified M_W (E61/E67))." in readme
    assert "so the Plan ranking is labelled exploratory" in readme
    assert "Claude Opus 5.5 leads the Plan ranking at 64.3; MiMo-V2.6-Pro leads the API ranking at 60.3 (subset cost); Claude Opus 5.5 leads on quality." in readme
    # The quality rank covers every cohort row with quality evidence, a cost-less one included (its quality is shown).
    # E203: the displayed record on the headline scale, beside the interval claims.
    assert "- API basis, displayed record (not a claim; E203): cheapest at or above quality 64.3: GPT-6.1 Sol (max) ($1,233.11 per basket run; 5 reach it)" in readme
    # O50: the max-effort ranking admits the Coding Agent Index v2.0, so the coding share names it and its unrewarded SWE-Atlas QnA.
    assert ("Coding and terminal tasks (Coding Agent Index, Terminal-Bench 4.0 (AA Index run), SciCode) make up 50% of the basket's cost (median over 7 configurations "
            "with the full basket; 45% to 85%); AA-Briefcase, GDP.pdf, which have no quality leaf, make up 18%; the Coding Agent Index's SWE-Atlas QnA") in readme
    assert "- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 64.3 over 9 configurations" in (emitted / "scores.md").read_text()
    assert "SciCode and AA-LCR once at API rates" in readme


def test_methodology_leaf_weights_fill_the_quality_share(emitted):
    text = (emitted / "methodology.md").read_text()
    rows = [cells(row) for row in table_rows(text, "| Leaf | Group | Weight, max-effort ranking | Weight, AI Coding Daily ranking")]
    # O53-O55: every leaf of either ranking, with a dash where a ranking does not use it; each column fills 100% of quality.
    assert len(rows) == 14
    for column in (2, 3):
        assert sum(float(row[column].rstrip("%")) for row in rows if row[column] != "—") == pytest.approx(100.0, abs=0.05)
    assert "Value on a basis = **25%** × cost score + **75%** × quality score" in text
    cohort = text.split("## Cohort\n", 1)[1].split("\n## ", 1)[0]
    assert "- On AA's rendered frontier (5):" in cohort and "- Near-frontier family (2):" in cohort
    assert "- Plotted on or near AA's rendered frontier, another effort of a frontier or near family (O51) (2): GPT-6 Astra (max), Claude Haiku 5.5 (max)" in cohort
    # O36/O38: configurations still missing a benchmark after the logged search are listed with the gap, not ranked; O53 names
    # those the AI Coding Daily ranking ranks.
    assert ("20 more cohort configurations are listed, not ranked, because a quality benchmark is still missing after an exhaustive search logged within 7 days "
            "of the cutoff (O36; a required frontier family is listed the same way, O38): GPT-6.1 Sol (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), "
            "LiveBench 2.0 Overall);") in cohort
    assert "MiMo-V2.6-Flash (no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals)" in cohort
    assert "Of these, 11 are ranked in the AI Coding Daily ranking (O53): GPT-6.1 Sol (high), Claude Opus 5.5 (high)," in cohort
    assert "The remaining 32 roster models are not ranked" in cohort
    assert "- Claude: User authorizes (2026-10-18, Option 2)" in text


def test_scores_md_ranking_matches_scores_json(emitted):
    v3 = v3_document()
    text = (emitted / "scores.md").read_text()
    assert text.startswith(f"# ValueRank {emit_docs.VERSION} Scores")
    rows = [cells(row) for row in table_rows(text, "| Configuration | Plan rank | Plan value")]
    by_plan = sorted(v3["rows"], key=lambda row: (row["planScore"]["rank"] is None, row["planScore"]["rank"] or 0))
    assert [row[2] for row in rows] == [f"{row['planScore']['value']:.2f}" for row in by_plan]
    assert [row[6] for row in rows] == [f"{row['api']['costScore']:.2f}" for row in by_plan]
    # 32 outside the cohort (O51) and 20 cohort rows without the max-effort ranking's set (O36, O53), 11 of them ranked in the other ranking.
    assert len(table_rows(text, "| Model | Reasons")) == 52
    assert "### API basis: rank 1" in text and "### Plan basis: on the frontier" in text
    # O48: the Plan streams exclude transfer-dependent plan rows, each named as a configuration on its plan.
    assert "Plan streams S1, S2, S1 endpoint-heavy, S1M and S1T run with owner-named transfers off (E167): Claude Haiku 5.5 (max) on Claude Max 20x," in text
    assert "| $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis |" in text
    assert "| Gemini 4 Argon (high) | — | — | — |" in text
    assert "| quality 65.0 | Claude Sonnet 5.5 (max) | not scenario-supported |" in text


def test_scores_md_prints_a_dash_for_a_configuration_without_a_rank(repo_copy, pinned_clock):
    """AGENTS.md: a configuration without a cost has no value score and no rank; like README, scores.md prints "—"."""

    def drop_cost(document):
        row = next(row for row in document["v3"]["rows"] if row["id"] == "gemini-4-argon")
        for basis in ("api", "planScore"):
            row[basis].update(rank=None, value=None, costScore=None)
        for plan_row in document["v3"]["planRows"]:
            if plan_row["configurationId"] == "gemini-4-argon":
                plan_row.update(rank=None, value=None, costScore=None)

    edit_json(repo_copy, "scores.json", drop_cost)
    assert emit(repo_copy) == 0
    text = (repo_copy / "scores.md").read_text()
    rows = {cells(row)[0].split("](")[0].lstrip("["): cells(row) for row in table_rows(text, "| Configuration | Plan rank | Plan value")}
    no_cost = rows["Gemini 4 Argon (high)"]
    assert no_cost[1] == "—" and no_cost[4] == "—", no_cost


def test_raw_data_lists_every_deepswe_configuration_and_bundle_artifact(emitted):
    configs = json.loads(committed("data/aa_deepswe.json"))["configurations"]
    text = (emitted / "raw-data.md").read_text()
    rows = table_rows(text, "| # | Agent | Evaluated model variant")
    assert len(rows) == len(configs)
    for row, config in zip(rows, configs):
        assert row.startswith(f"| {config['sourceOrder']} | {config['agent']} | {config['model']} |")
    assert f"The AA chart published {len(configs)} DeepSWE v1.1" in text
    bundle = v3_document()["evidenceBundle"]
    assert len(table_rows(text, "| Key | Artifact | SHA-256")) == len(bundle["artifacts"])
    assert bundle["artifacts"][0]["sha256"] in text


def test_readme_files_section_points_at_the_generated_site_pages(emitted):
    files = (emitted / "README.md").read_text().split("\n## Files\n", 1)[1]
    assert "- [https://valuerank.alolabs.dev/](https://valuerank.alolabs.dev/): website, generated by `valuerank.site.build` (source under [valuerank/site/](valuerank/site/))" in files
    assert "- [https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/](https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/): current Terminal-Bench 4.0 score-versus-cost page" in files
    assert "- [data/](data/)" in files and "- [docs/](docs/README.md)" in files


def test_summary_json_lists_only_the_markdown_outputs(repo_copy, pinned_clock, capsys):
    emit(repo_copy)
    out = capsys.readouterr().out
    summary = json.loads(out[out.rindex('{\n  "version"'):])
    assert summary["version"] == emit_docs.VERSION
    assert summary["methodology"] == v3_document()["methodologyVersion"]
    assert summary["outputs"] == ["README.md", "methodology.md", "scores.md", "raw-data.md"]


def test_emitting_without_a_site_directory_succeeds_and_creates_none(repo_copy, pinned_clock):
    shutil.rmtree(repo_copy / "site")
    assert emit(repo_copy) == 0
    assert not (repo_copy / "site").exists()


def test_main_guard_runs_the_emitter(repo_copy, pinned_clock, monkeypatch, capsys):
    monkeypatch.setattr(paths, "ROOT", repo_copy)
    monkeypatch.setattr(paths, "DATA", repo_copy / "data")
    monkeypatch.delitem(sys.modules, "valuerank.emit_docs")
    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.emit_docs", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert (repo_copy / "README.md").read_text() == committed("README.md")
    assert f'"version": "{emit_docs.VERSION}"' in capsys.readouterr().out


# --- branches the committed snapshot does not reach ---------------------------------------------


def test_stale_scenarios_publish_no_shares(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc["v3"].__setitem__("scenarios", {"status": "stale (inputs changed since the scenario run)"}))
    assert emit(repo_copy) == 0
    assert "Scenario outputs are stale (inputs changed since the scenario run); no shares are published" in (repo_copy / "scores.md").read_text()
    assert "(scenario outputs stale (inputs changed since the scenario run))" in (repo_copy / "methodology.md").read_text()


def test_no_bar_label_candidates_leave_out_the_label_table(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc["v3"]["scenarios"].__setitem__("barLabels", []))
    assert emit(repo_copy) == 0
    assert "Cheapest-above-the-bar labels" not in (repo_copy / "scores.md").read_text()


def evaluated_plan_intervals(document):
    v3 = document["v3"]
    plan = copy.deepcopy(v3["intervals"]["api"])
    plan["unevaluable"] = []
    bar = plan["bars"][0]
    bar["confirmedCheapest"] = None
    bar["possibleCheapest"] = ["gpt-6-luna", "deepseek-v4-1-flash-1017"]
    plan["bars"].append({**copy.deepcopy(bar), "status": "unresolved"})
    plan["bars"].append({**copy.deepcopy(bar), "confirmedCheapest": "deepseek-v4-1-flash-1017"})
    # E183: an O29 blocker competes without a label of its own.
    plan["blockers"] = ["gemini-4-argon"]
    plan["frontier"]["gemini-4-argon"] = {"status": "no interval label"}
    bar["rows"]["gemini-4-argon"] = {"status": "no interval label"}
    v3["intervals"]["plan"] = plan


def test_plan_interval_outputs_and_unconfirmed_bars_are_described(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", evaluated_plan_intervals)
    assert emit(repo_copy) == 0
    readme = (repo_copy / "README.md").read_text()
    plan_sentence = next(line for line in readme.splitlines() if line.startswith("- Plan basis, main workload"))
    assert "Not evaluable" not in plan_sentence
    assert "Cheapest at or above quality 64.3: not unique; possibly GPT-6 Luna (max), DeepSeek V4.1 Flash 1017 (max)." in plan_sentence
    assert "Cheapest at or above quality 64.3: unresolved." in plan_sentence
    assert plan_sentence.endswith("Cheapest at or above quality 64.3: DeepSeek V4.1 Flash 1017 (max) (confirmed). (Bar comparison: compares 5 configurations that can qualify.)")
    scores = (repo_copy / "scores.md").read_text()
    assert "**Plan basis, main workload: frontier.** Not evaluable: none." in scores
    assert "Status certified; confirmed cheapest: none." in scores
    assert "Status unresolved." in scores
    assert "Competing without a label (AA cost on a price not in force, O29): Gemini 4 Argon (high)." in plan_sentence
    assert "Competing without a label (AA cost on a price not in force, O29, E183): Gemini 4 Argon (high)." in scores


def test_unevaluable_rows_and_subset_workload_intervals_are_printed(repo_copy, pinned_clock):
    """E190: interval outputs on a subset workload follow the main ones; unevaluable rows are named."""

    def subset_intervals(document):
        v3 = document["v3"]
        v3["intervals"]["api"]["unevaluable"] = ["gemini-4-argon"]
        v3["subsetIntervals"] = {"subset": {"components": ["gdpval-aa"], "api": copy.deepcopy(v3["intervals"]["api"]), "plan": copy.deepcopy(v3["intervals"]["plan"])}}

    edit_json(repo_copy, "scores.json", subset_intervals)
    assert emit(repo_copy) == 0
    readme = (repo_copy / "README.md").read_text()
    assert "Not evaluable on this workload: Gemini 4 Argon (high)." in readme
    assert "subset workload (GDPval-AA; orderings across workloads not identified)" in (repo_copy / "scores.md").read_text()


def test_an_undefined_variance_allocation_prints_only_the_nominal_weight(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc["v3"]["costInfluence"]["plan"]["commonWorkload"].__setitem__("varianceAllocation", None))
    assert emit(repo_copy) == 0
    readme = (repo_copy / "README.md").read_text()
    assert "value is a 25% cost score (nominal weight) plus 75% quality" in readme and "That weight is nominal" not in readme


def test_policy_applications_are_printed_only_when_recorded(repo_copy, pinned_clock):
    edit_json(repo_copy, "plan_cost_routes.json", lambda doc: doc["evidencePolicy"].pop("mimoApplication"))
    assert emit(repo_copy) == 0
    text = (repo_copy / "methodology.md").read_text()
    assert "- MiMo:" not in text and "- GPT: User authorizes" in text


def test_a_ranked_row_without_an_inclusion_reason_is_refused(repo_copy, pinned_clock):
    def drop_reasons(document):
        next(model for model in document["models"] if model["id"] == "gemini-4-argon")["rankingInclusionReasons"] = []

    edit_json(repo_copy, "scores.json", drop_reasons)
    with pytest.raises(ValueError, match="gemini-4-argon has no recorded cohort inclusion reason"):
        emit(repo_copy)


def test_terminal_bench_harness_diagnostic_reports_tau_when_defined(repo_copy, pinned_clock):
    def undefined_agreement(document):
        document["v3"]["diagnostics"]["qualityAgreement"].update(tau=None, interval=None, status="undefined (panel too small)")
        document["v3"]["diagnostics"]["groupDrift"].pop("groups")

    edit_json(repo_copy, "scores.json", undefined_agreement)
    assert emit(repo_copy) == 0
    text = (repo_copy / "scores.md").read_text()
    assert "- **Quality agreement:** quality agreement (matched-panel sensitivity): undefined (panel too small); panel of 9 rows." in text
    assert re.search(r"- \*\*Group drift:\*\* estimated\.\n", text)


def test_calibration_without_official_anchors_or_values_says_so(repo_copy, pinned_clock):
    def no_calibration(document):
        calibration = document["v3"]["measuredOnlyPlanView"]["calibration"]
        for item in calibration["workloads"].values():
            item["officialAnchorProvenance"] = None
            item["status"] = "measured-evidence calibration unavailable (fewer than two measured references)"
        calibration.update(status="measured-evidence calibration unavailable", values={}, reversals=[], maxAbsValueChange=None)

    edit_json(repo_copy, "scores.json", no_calibration)
    assert emit(repo_copy) == 0
    text = (repo_copy / "scores.md").read_text()
    section = text.split("#### Measured-evidence calibration (diagnostic)", 1)[1].split("## Interval outputs", 1)[0]
    assert "Status: measured-evidence calibration unavailable." in section
    # The max-effort ranking has a main and a subset workload (O17), each with its own anchors.
    assert section.count("The workload has no official Plan anchors.") == 2
    assert "Value on measured anchors" not in section and "Pairwise reversals" not in section


def test_calibration_reports_reversals_and_the_official_anchor_extremes(emitted):
    section = (emitted / "scores.md").read_text().split("#### Measured-evidence calibration (diagnostic)", 1)[1].split("## Interval outputs", 1)[0]
    assert "Official Plan anchors are set by GPT-6 Luna (max) on ChatGPT Pro 500 (owner-named transfer) at the low end and Gemini 4 Argon (high) on API-cost fallback at the high end." in section
    assert "Pairwise reversals: Claude Opus 5.5 (max) and GPT-6.1 Sol (max). Largest value change: 3.94 points." in section
    methodology = (emitted / "methodology.md").read_text()
    assert "labelled conventional CI-range sensitivity (endpoint-conditioned; no tail model) under its interpretation contract (E165" in methodology


def test_release_text_lint_blocks_a_sentence_that_puts_run_ranges_into_scenario_shares(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc["v3"]["scenarios"].__setitem__("notQuantified", ["benchmark run-to-run ranges enter the S2 scenario shares"]))
    with pytest.raises(ValueError, match=r"release-text lint \(E155\) rejects: methodology.md: - benchmark run-to-run ranges enter the S2 scenario shares"):
        emit(repo_copy)
