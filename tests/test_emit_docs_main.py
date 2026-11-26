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
    assert rows[0][2].startswith("[GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/)")
    assert any(row[2].startswith("[Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/)") for row in ranked)
    # Every cohort configuration has an AA cost today, so no row is unranked for want of one; since the 2026-11-26 release no
    # ranked row is on a subset workload either (MiMo-V2.6-Pro left the cohort), so nothing follows the ranked rows. The O184
    # placement of a subset-workload row is rebuilt synthetically in test_readme_places_a_subset_workload_row_after_the_ranked_rows.
    assert unranked == []
    assert "- **no cost**: AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown." in readme
    assert readme.startswith("# ValueRank\n")
    scored = sum(1 for row in v3["rows"] if row["api"]["value"] is not None)
    assert f"**Scope:** {len(v3['rows'])} cohort configurations ({scored} with a value score)" in readme and scored == len(v3["rows"])
    assert f"**Methodology:** {v3['methodologyVersion']} · {v3['basketVersion']} · anchor version {v3['anchorVersion']}" in readme
    assert "## AA intelligence and total-cost comparison" in readme


def test_readme_places_a_subset_workload_row_after_the_ranked_rows(repo_copy, pinned_clock):
    """O184: a subset-workload row follows the main-workload ranked rows with its rank within its own workload. No current row
    is on a subset workload (MiMo-V2.6-Pro, the 2026-11-01 example, left the cohort), so GPT-6 Luna (max) is made one here."""

    def subset_row(document):
        row = next(row for row in document["v3"]["rows"] if row["id"] == "gpt-6-luna")
        for basis in ("api", "planScore"):
            row[basis].update(rank=None, rankWithinWorkload=1)
        row["cost"]["subset"] = True
        for plan_row in document["v3"]["planRows"]:
            if plan_row["configurationId"] == "gpt-6-luna":
                plan_row.update(rank=None, rankWithinWorkload=1)

    edit_json(repo_copy, "scores.json", subset_row)
    assert emit(repo_copy) == 0
    rows = [cells(row) for row in table_rows((repo_copy / "README.md").read_text(), "| Plan rank | API rank | Configuration")]
    assert [row[2].split("]")[0] for row in rows[:-1]] == ["[GPT-6.1 Sol (max)", "[Claude Sonnet 5.5 (max)", "[Claude Opus 5.5 (max)", "[GPT-6 Astra (max)"]
    assert (rows[-1][0], rows[-1][1], rows[-1][2].split("]")[0]) == ("1 (own workload, O184)", "1 (own workload, O184)", "[GPT-6 Luna (max)")
    assert rows[-1][10].startswith("subset cost")


def ranking_rows(text, heading=None):
    """The README ranking table rows by configuration label; ``heading`` picks the table after that heading."""

    if heading is not None:
        text = text.split(heading, 1)[1]
    return {cells(row)[2].split("](")[0].lstrip("["): cells(row) for row in table_rows(text, "| Plan rank | API rank | Configuration")}


def test_readme_flags_fallback_and_subset_rows(emitted):
    readme = (emitted / "README.md").read_text()
    rows = ranking_rows(readme)
    # E37: AA marks tasks of one of Claude Opus 5.5 (max)'s basket components missing or declined.
    # O175: the Opus rows' 0.03-0.04% Index residual is within the materiality band, so no partial component.
    assert rows["Claude Opus 5.5 (max)"][10] == "route possibly superseded"
    assert rows["GPT-6 Astra (max)"][6] == "100%" and rows["GPT-6 Astra (max)"][10] == "route possibly superseded"
    # O91-O95: a route resting on a controlled measurement inside an accounting-fault window is flagged.
    assert rows["GPT-6.1 Sol (max)"][10] == "route possibly superseded, fault window"
    # O45: GPT-6.1 Sol keeps its own SemiAnalysis figure; another Claude model takes Opus 5.5's figure as an assumption.
    assert rows["GPT-6.1 Sol (max)"][9] == "ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured)"
    assert rows["Claude Sonnet 5.5 (max)"][9] == "Claude Pro $20 · common Claude assumption (58.9×, assumption)"
    # AA states its published cost for Claude Haiku 5.5 omits a pricing term (ranked in the AI Coding Daily ranking).
    aicd = ranking_rows(readme, "### AI Coding Daily ranking")
    assert aicd["Claude Haiku 5.5 (high)"][10] == "AA cost caveat, route possibly superseded"
    # O13/O17: rows without an admitted Plan route are flagged API-cost fallback and show no route; a row scored on a
    # subset workload is flagged subset cost. Since 2026-11-26 no ranked row is either (both cases are rebuilt synthetically in
    # test_readme_flags_an_api_cost_fallback_row_and_a_subset_cost_row).
    fallback = {label for label, row in rows.items() if "API-cost fallback" in row[10]}
    subset = {label for label, row in rows.items() if "subset cost" in row[10]}
    assert fallback == set()
    assert subset == set()
    # O198: a cohort model OpenCode lists takes OpenCode Go's published dollar limit over the $10 fee as a Plan row. DeepSeek
    # V4.1 Flash and Gemini 4 Argon (the 2026-11-01 examples) left the cohort; GPT-6 Luna (max) is the current one: its route
    # opencode-go-gpt-6-luna-dollar-limit has monthlyLimitUsd 15 on planPriceUsd 10 (1.5x), $174.72 / 1.5 = $116.48.
    plans = [cells(row) for row in table_rows(readme, "| Plan rank | Configuration | Plan | Value Multiple")]
    assert ["GPT-6 Luna (max)", "OpenCode Go", "1.5×", "$116.48", "51.8", "41.4", "assumption"] in [row[1:8] for row in plans]


def test_readme_flags_an_api_cost_fallback_row_and_a_subset_cost_row(repo_copy, pinned_clock):
    """O13/O17: a row without an admitted Plan route is flagged API-cost fallback and shows no route; a row scored on a
    subset workload is flagged subset cost (no current row is either, so both are set on scores.json)."""

    def fallback_and_subset(document):
        rows = {row["id"]: row for row in document["v3"]["rows"]}
        plan = rows["gpt-6-luna"]["plan"]
        plan.update(fallback="api", routeId=None, amount=None, selectedIdentification=None, grade=None, flags=[], selectionReason=None)
        rows["claude-sonnet-5-5"]["cost"]["subset"] = True

    edit_json(repo_copy, "scores.json", fallback_and_subset)
    assert emit(repo_copy) == 0
    rows = ranking_rows((repo_copy / "README.md").read_text())
    assert rows["GPT-6 Luna (max)"][9] == "—" and rows["GPT-6 Luna (max)"][10] == "API-cost fallback"
    assert rows["Claude Sonnet 5.5 (max)"][10] == "subset cost, route possibly superseded"
    scores = {cells(row)[0].split("](")[0].lstrip("["): cells(row)
              for row in table_rows((repo_copy / "scores.md").read_text(), "| Configuration | Plan rank | Plan value")}
    assert scores["Claude Sonnet 5.5 (max)"][-1] == "subset" and scores["GPT-6 Luna (max)"][-1] == "main"
    # E166: an API-fallback row publishes no route, amount or identification.
    assert "| GPT-6 Luna (max) | — | — | — | — |" in (repo_copy / "scores.md").read_text()


def test_readme_states_what_the_interval_outputs_support(emitted):
    readme = (emitted / "README.md").read_text()
    assert "the definite frontier (no configuration can beat it on both cost and quality" in readme
    # E190: the frontier names the configurations it cannot evaluate; since 2026-11-26 there are none (no subset-workload row,
    # intervals.api.unevaluable == []), so the sentence ends with the possible frontier. Naming them is rebuilt synthetically in
    # test_unevaluable_rows_and_subset_workload_intervals_are_printed.
    api_sentence = next(line for line in readme.splitlines() if line.startswith("- API basis, main workload"))
    assert "is GPT-6.1 Sol (max), GPT-6 Astra (max), GPT-6 Luna (max); the possible frontier adds none. Cheapest at or above" in api_sentence
    assert "Not evaluable" not in api_sentence
    # E192: the bars are quality levels (the O34 ladder over the 5 ranked rows: 63.9 Sonnet, 64.3 Opus, 64.3 Sol), so each output
    # compares alternatives instead of returning the bar setter. O187: with 5 rows the like-for-like workload cross-check
    # panel is below its 8-row floor (diagnostics.workloadCrossCheck n 5, minRows 8), so every bar's label is withheld.
    withheld = ("labels withheld: the ranking's like-for-like workload cost check (basket cost against Terminal-Bench cost per attempted task) "
                "cannot be computed (a panel below the 8-row floor or no rank variation), so no label is cleared by it (O187).")
    assert api_sentence.count(f"Cheapest at or above quality 64.3: {withheld}") == 2
    assert api_sentence.count(f"Cheapest at or above quality 63.9: {withheld}") == 1
    assert "(confirmed)" not in api_sentence and "Bar comparison" not in api_sentence
    # E196: the nominal cost weight is printed with cost's share of the variance in value
    # (costInfluence.{api,plan}.commonWorkload.varianceAllocation.cost = 0.643 and 0.026).
    assert "value is a 25% cost score (nominal weight; 64% of API and 3% of Plan value variance)" in readme
    assert ("That weight is nominal: on the current panel cost accounts for 64% of the variance in API value and 3% in Plan value, "
            "because cost scores spread more than quality scores") in readme
    assert "Plan basis: interval outputs not evaluated (no row has FullCost and an identified M_W (E61/E67))." in readme
    assert "so the Plan ranking is labelled exploratory" in readme
    assert "GPT-6.1 Sol (max) leads the Plan ranking at 68.0; GPT-6.1 Sol (max) leads the API ranking at 60.6; GPT-6 Astra (max) leads on quality." in readme
    # The quality rank covers every cohort row with quality evidence, a cost-less one included (its quality is shown).
    # E203: the displayed record on the headline scale, beside the interval claims (displayedCheapest.api.bars).
    assert ("- API basis, displayed record (not a claim; E203): cheapest at or above quality 64.3: GPT-6.1 Sol (max) ($1,435.80 per basket run; 3 reach it); "
            "at or above quality 63.9: GPT-6.1 Sol (max) ($1,435.80 per basket run; 4 reach it); "
            "at or above quality 64.3: GPT-6.1 Sol (max) ($1,435.80 per basket run; 2 reach it).") in readme
    # O143: cheaper same-family efforts on AA's chart that the ranking could not evaluate are named beside the displayed record.
    assert ("- API basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below GPT-6.1 Sol (max): "
            "GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).") in readme
    # Claude Haiku 5.5 (max) is no longer ranked here, so the Plan basis names GPT-6.1 Sol (max)'s siblings only.
    assert ("- Plan basis, cheaper same-family efforts on AA's chart that this ranking could not evaluate (O143, E201c): below GPT-6.1 Sol (max): "
            "GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low).") in readme
    # O50: the max-effort ranking admits the Coding Agent Index (v2.1: 124 of its 322 tasks are SWE-Atlas QnA), so the coding share
    # names it and its unrewarded SWE-Atlas QnA. Since O210 GDP.pdf has a quality leaf, so AA-Briefcase alone has none.
    assert ("Coding and terminal tasks (Coding Agent Index, Terminal-Bench 4.1 (AA Index run), FrontierCode 2.0) make up 58% of the basket's cost (median over 5 configurations "
            "with the full basket; 53% to 60%); with Terminal-Bench-Science's terminal tasks, whose quality O136 files under science, 73% (69% to 76%; E343); "
            "AA-Briefcase, which has no quality leaf, makes up 15%; the Coding Agent Index's SWE-Atlas QnA (124 of its 322 tasks) has no quality leaf either") in readme
    # Reviewer 79 (E299): the O145 retained rows leave the frontier-only population (5 ranked, 3 retained: GPT-6 Astra, Claude
    # Sonnet 5.5, GPT-6 Luna), leaving GPT-6.1 Sol (max) and Claude Opus 5.5 (max) (diagnostics.frontierAnchors.bar).
    assert ("- **Frontier-families bar (E199, sensitivity; the frozen bar stays primary):** quality 64.3 over 2 configurations; cheapest at or above it on the "
            "API main workload: GPT-6.1 Sol (max) (confirmed) (compares 3 configurations that can qualify).") in (emitted / "scores.md").read_text()
    assert "FrontierCode 2.0 and Terminal-Bench-Science once at API rates" in readme


def test_methodology_leaf_weights_fill_the_quality_share(emitted):
    text = (emitted / "methodology.md").read_text()
    rows = [cells(row) for row in table_rows(text, "| Leaf | Group | Weight, max-effort ranking | Weight, AI Coding Daily ranking")]
    # O53-O55: every leaf of either ranking, with a dash where a ranking does not use it; each column fills 100% of quality.
    # 15 leaves since the GDP.pdf leaf (gdpPdf, 5%, O210) joined GDPval-AA (now 5%) in general professional work.
    assert len(rows) == 15
    assert any(row[0].startswith("[GDP.pdf (AA)]") and row[2:5] == ["5.00%", "5.00%", "5.00%"] for row in rows)
    for column in (2, 3, 4):
        assert sum(float(row[column].rstrip("%")) for row in rows if row[column] != "—") == pytest.approx(100.0, abs=0.05)
    assert "Value on a basis = **25%** × cost score + **75%** × quality score" in text
    cohort = text.split("## Cohort\n", 1)[1].split("\n## ", 1)[0]
    # data/scores.json models[].aaFrontierTier: GPT-6.1 Sol (max) and Claude Opus 5.5 (max) are "near" (gaps 2 and 3); the
    # frontier family GPT-6.2 Sol is listed, not ranked, so no ranked row sits on the rendered frontier itself.
    assert "- On AA's rendered frontier" not in cohort and "- Near-frontier family (1): Claude Opus 5.5 (max)" in cohort
    assert "- Plotted on or near AA's rendered frontier, another effort of a frontier or near family (O51) (1): GPT-6.1 Sol (max)" in cohort
    # O145: configurations that left the frontier and near gap at this release are kept one more release (aaFrontierTier "left cohort").
    assert ("- Left the frontier and near gap at this release, kept one more release (O145) (3): GPT-6 Astra (max), "
            "Claude Sonnet 5.5 (max), GPT-6 Luna (max)") in cohort
    # O36/O38: configurations still missing a benchmark after the logged search are listed with the gap, not ranked; O53 names
    # those the AI Coding Daily ranking ranks (14 listed here plus GPT-6 Luna (max) make its 15 rows).
    assert ("40 more cohort configurations are listed, not ranked, because a quality benchmark is still missing after an exhaustive search logged within 7 days "
            "of the cutoff (O36; a required frontier family is listed the same way, O38): GPT-6.1 Sol (high) (no Vibe Code Bench v1.1 (Vals), "
            "Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6.1 Terra (max) (no Code Migration v1.1 (Vals));") in cohort
    assert "MiMo-V2.6-Flash (no Bug Hunt Bench, LiveBench 2.0 Overall)" in cohort
    assert "GPT-6.2 Sol (max) (no Code Migration v1.1 (Vals), GDPval-AA v2.1, AA-LCR v1.1)" in cohort
    assert "Of these, 14 are ranked in the AI Coding Daily ranking (O53): GPT-6.1 Sol (high), GPT-6.1 Terra (max), GPT-6.1 Sol (medium)," in cohort
    # The v5 cohort is the whole 45-configuration roster (5 ranked + 40 listed), so no roster model is left outside it;
    # any "remaining roster models" sentence must count none.
    remaining = re.search(r"The remaining (\d+) roster models? (?:is|are) not ranked", cohort)
    assert remaining is None or remaining.group(1) == "0"
    assert "- Claude: User authorizes (2026-10-18, Option 2)" in text


def test_scores_md_ranking_matches_scores_json(emitted):
    v3 = v3_document()
    text = (emitted / "scores.md").read_text()
    assert text.startswith(f"# ValueRank {emit_docs.VERSION} Scores")
    rows = [cells(row) for row in table_rows(text, "| Configuration | Plan rank | Plan value")]
    by_plan = sorted(v3["rows"], key=lambda row: (row["planScore"]["rank"] is None, row["planScore"]["rank"] or 0))
    assert [row[2] for row in rows] == [f"{row['planScore']['value']:.2f}" for row in by_plan]
    assert [row[6] for row in rows] == [f"{row['api']['costScore']:.2f}" for row in by_plan]
    # 40 cohort rows without the max-effort ranking's set (O36, O53; v3.incompleteEvidence has 40 entries, 45 - 5 ranked); the
    # v5 cohort is the whole roster, so none is outside it (O51).
    assert len(table_rows(text, "| Model | Reasons")) == len(v3["incompleteEvidence"]) == 40
    assert "### API basis: rank 1" in text and "### Plan basis: on the frontier" in text
    # O48: the Plan streams exclude transfer-dependent plan rows, each named as a configuration on its plan (the max-effort
    # ranking's 8 owner-assumption rows: Claude Sonnet 5.5 on three Claude plans, GPT-6 Luna on four ChatGPT plans and OpenCode Go).
    assert ("Plan streams S1, S2, S1 endpoint-heavy, S1M, S1T and S1T recentred run with owner assumptions off (owner-named transfers, O46 provider quota ceilings "
            "and O198 published dollar limits; E167): Claude Sonnet 5.5 (max) on Claude Max 20x, Claude Sonnet 5.5 (max) on Claude Max 5x, "
            "Claude Sonnet 5.5 (max) on Claude Pro, GPT-6 Luna (max) on ChatGPT Plus, GPT-6 Luna (max) on ChatGPT Pro 100, GPT-6 Luna (max) on ChatGPT Pro 200, "
            "GPT-6 Luna (max) on ChatGPT Pro 500, GPT-6 Luna (max) on OpenCode Go depend on an owner assumption") in text
    assert "| $1,178 per month: assumed API-equivalent consumption (owner-named transfer) from claude-pro-opus55-semianalysis |" in text
    assert "| GPT-6.1 Sol (max) | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | $5,386 per month: measured-workload capacity |" in text
    # The kernel checks are all met for the headline bar's candidate, but O187 withholds the label (cross-check panel of 5 < 8).
    assert ("| quality 64.3 | GPT-6.1 Sol (max) | labels withheld: the ranking's like-for-like workload cost check (basket cost against Terminal-Bench "
            "cost per attempted task) cannot be computed (a panel below the 8-row floor or no rank variation), so no label is cleared by it (O187) "
            "| 100.0% to 100.0% | UU met, UH met, HU met, HH met | no |") in text


def test_scores_md_prints_a_dash_for_a_configuration_without_a_rank(repo_copy, pinned_clock):
    """AGENTS.md: a configuration without a cost has no value score and no rank; like README, scores.md prints "—"."""

    def drop_cost(document):
        row = next(row for row in document["v3"]["rows"] if row["id"] == "gpt-6-luna")
        for basis in ("api", "planScore"):
            row[basis].update(rank=None, value=None, costScore=None)
        for plan_row in document["v3"]["planRows"]:
            if plan_row["configurationId"] == "gpt-6-luna":
                plan_row.update(rank=None, value=None, costScore=None)

    edit_json(repo_copy, "scores.json", drop_cost)
    assert emit(repo_copy) == 0
    text = (repo_copy / "scores.md").read_text()
    rows = {cells(row)[0].split("](")[0].lstrip("["): cells(row) for row in table_rows(text, "| Configuration | Plan rank | Plan value")}
    no_cost = rows["GPT-6 Luna (max)"]
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
    assert "- [https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/](https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/): current Terminal-Bench 4.1 score-versus-cost page" in files
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
    def no_labels(doc):
        for section in (doc["v3"], *doc["v3Tracks"].values()):
            section["scenarios"]["barLabels"] = []

    edit_json(repo_copy, "scores.json", no_labels)
    assert emit(repo_copy) == 0
    assert "Cheapest-above-the-bar labels" not in (repo_copy / "scores.md").read_text()


def evaluated_plan_intervals(document):
    v3 = document["v3"]
    plan = copy.deepcopy(v3["intervals"]["api"])
    plan["unevaluable"] = []
    bar = plan["bars"][0]
    # Since 2026-11-26 every committed bar is withheld under O187 (cross-check panel of 5 < 8 rows), so the evaluated
    # (certified) outcomes are set here; O182: the uncertain cross-check agreement that makes labels carry the warning is
    # likewise set, because the committed check is undefined (panel too small).
    bar["status"] = "certified"
    v3["diagnostics"]["workloadCrossCheck"].update(tau=0.4, interval=[0.0, 0.8], status="defined", warning="uncertain agreement")
    bar["confirmedCheapest"] = None
    bar["possibleCheapest"] = ["gpt-6-luna", "gpt-6.1-sol"]
    plan["bars"].append({**copy.deepcopy(bar), "status": "unresolved"})
    plan["bars"].append({**copy.deepcopy(bar), "confirmedCheapest": "gpt-6-astra"})
    # E183: an O29 blocker competes without a label of its own.
    plan["blockers"] = ["claude-sonnet-5-5"]
    plan["frontier"]["claude-sonnet-5-5"] = {"status": "no interval label: AA cost on a price not in force at V (O29); competes over its current-tariff hull"}
    bar["rows"]["claude-sonnet-5-5"] = {"status": "no interval label"}
    v3["intervals"]["plan"] = plan


def test_plan_interval_outputs_and_unconfirmed_bars_are_described(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", evaluated_plan_intervals)
    assert emit(repo_copy) == 0
    readme = (repo_copy / "README.md").read_text()
    plan_sentence = next(line for line in readme.splitlines() if line.startswith("- Plan basis, main workload"))
    assert "Not evaluable" not in plan_sentence
    # The headline bar is the lower-median quality, 64.3 (Claude Opus 5.5 (max)'s 64.32), comparing 3 configurations.
    assert "Cheapest at or above quality 64.3: not unique; possibly GPT-6 Luna (max), GPT-6.1 Sol (max)." in plan_sentence
    assert "Cheapest at or above quality 64.3: unresolved." in plan_sentence
    assert "Cheapest at or above quality 64.3: GPT-6 Astra (max) (confirmed). (Bar comparison: compares 3 configurations that can qualify.)" in plan_sentence
    # Reviewer 72 (O63): the labelled rows' safety-refusal flags follow the labels (rows[].agentSafety: 966 attempts this release).
    assert "GPT-6.1 Sol (max) (15 blocked and 0 fallback attempts of 966)." in plan_sentence
    # O182: under uncertain agreement the labels are issued and carry the cross-check warning.
    assert plan_sentence.endswith("`diagnostics.workloadCrossCheck.attribution`.") and "O160, O183" in plan_sentence
    scores = (repo_copy / "scores.md").read_text()
    assert "**Plan basis, main workload: frontier.** Not evaluable: none." in scores
    assert "Status certified; confirmed cheapest: none." in scores
    assert "Status unresolved." in scores
    blocker = "Competing without a label of its own (E183): Claude Sonnet 5.5 (max): AA cost on a price not in force at V (O29); competes over its current-tariff hull."
    assert blocker in plan_sentence
    assert blocker in scores


def test_unevaluable_rows_and_subset_workload_intervals_are_printed(repo_copy, pinned_clock):
    """E190: interval outputs on a subset workload follow the main ones; unevaluable rows are named."""

    def subset_intervals(document):
        v3 = document["v3"]
        v3["intervals"]["api"]["unevaluable"] = ["claude-opus-5-5", "gpt-6-luna"]
        v3["subsetIntervals"] = {"subset": {"components": ["aa-briefcase", "gdp-pdf"], "api": copy.deepcopy(v3["intervals"]["api"]), "plan": copy.deepcopy(v3["intervals"]["plan"])}}

    edit_json(repo_copy, "scores.json", subset_intervals)
    assert emit(repo_copy) == 0
    readme = (repo_copy / "README.md").read_text()
    assert "Not evaluable on this workload: Claude Opus 5.5 (max), GPT-6 Luna (max)." in readme
    assert "subset workload (AA-Briefcase, GDP.pdf; orderings across workloads not identified)" in (repo_copy / "scores.md").read_text()


def test_an_undefined_variance_allocation_prints_only_the_nominal_weight(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc["v3"]["costInfluence"]["plan"]["commonWorkload"].__setitem__("varianceAllocation", None))
    assert emit(repo_copy) == 0
    readme = (repo_copy / "README.md").read_text()
    assert "value is a 25% cost score (nominal weight) plus 75% quality" in readme and "That weight is nominal" not in readme


def test_a_ranked_row_without_route_pairs_has_no_alternatives_row(repo_copy, pinned_clock):
    """E171/E179: a ranked row with no admissible route-measurement pair is left out of the route-alternatives table."""

    def drop_pairs(doc):
        row = next(item for item in doc["v3"]["rows"] if item["plan"]["routeAlternatives"]["pairs"])
        row["plan"]["routeAlternatives"]["pairs"] = []

    assert emit(repo_copy) == 0
    before = (repo_copy / "scores.md").read_text()
    edit_json(repo_copy, "scores.json", drop_pairs)
    assert emit(repo_copy) == 0
    assert (repo_copy / "scores.md").read_text() != before


def test_policy_applications_are_printed_only_when_recorded(repo_copy, pinned_clock):
    edit_json(repo_copy, "plan_cost_routes.json", lambda doc: doc["evidencePolicy"].pop("mimoApplication"))
    assert emit(repo_copy) == 0
    text = (repo_copy / "methodology.md").read_text()
    assert "- MiMo:" not in text and "- GPT: User authorizes" in text


def test_a_ranked_row_without_an_inclusion_reason_is_refused(repo_copy, pinned_clock):
    def drop_reasons(document):
        next(model for model in document["models"] if model["id"] == "gpt-6-luna")["rankingInclusionReasons"] = []

    edit_json(repo_copy, "scores.json", drop_reasons)
    with pytest.raises(ValueError, match="gpt-6-luna has no recorded cohort inclusion reason"):
        emit(repo_copy)


def test_terminal_bench_harness_diagnostic_reports_tau_when_defined(repo_copy, pinned_clock):
    def undefined_agreement(document):
        document["v3"]["diagnostics"]["qualityAgreement"].update(tau=None, interval=None, status="undefined (panel too small)")
        document["v3"]["diagnostics"]["groupDrift"].pop("groups")

    edit_json(repo_copy, "scores.json", undefined_agreement)
    assert emit(repo_copy) == 0
    text = (repo_copy / "scores.md").read_text()
    # The panel is the 5 ranked rows (diagnostics.qualityAgreement.panel).
    assert "- **Quality agreement:** quality agreement (matched-panel sensitivity): undefined (panel too small); panel of 5 rows." in text
    assert re.search(r"- \*\*Group drift:\*\* estimated\.\n", text)


def test_calibration_without_official_anchors_or_values_says_so(repo_copy, pinned_clock):
    def no_calibration(document):
        # O90: the AI Coding Daily ranking now has measured references too, so both rankings lose their calibration here.
        for section in [document["v3"], *document.get("v3Tracks", {}).values()]:
            calibration = section["measuredOnlyPlanView"]["calibration"]
            for item in calibration["workloads"].values():
                item["officialAnchorProvenance"] = None
                item["status"] = "measured-evidence calibration unavailable (fewer than two measured references)"
            calibration.update(status="measured-evidence calibration unavailable", values={}, reversals=[], maxAbsValueChange=None)

    edit_json(repo_copy, "scores.json", no_calibration)
    assert emit(repo_copy) == 0
    text = (repo_copy / "scores.md").read_text()
    section = text.split("#### Measured-evidence calibration (diagnostic)", 1)[1].split("## Interval outputs", 1)[0]
    assert "Status: measured-evidence calibration unavailable." in section
    # Each of the three rankings' calibrations has one workload: since 2026-11-26 the max-effort ranking has no subset workload
    # (MiMo-V2.6-Pro left the cohort), and the AI Coding Daily and O121 diagnostic rankings have measured references (O90).
    assert section.count("The workload has no official Plan anchors.") == 3
    assert "Value on measured anchors" not in section and "Pairwise reversals" not in section


def test_calibration_reports_reversals_and_the_official_anchor_extremes(emitted):
    section = (emitted / "scores.md").read_text().split("#### Measured-evidence calibration (diagnostic)", 1)[1].split("## Interval outputs", 1)[0]
    # O157: the Plan anchors are measured plan rows only, so no owner assumption or API-cost fallback sets them; the
    # setter's label names its measurement.
    # The max-effort ranking has one workload now (no subset workload), so its anchor sentence appears once.
    assert section.count("Official Plan anchors are set by GPT-6.1 Sol (max) on ChatGPT Pro 500 (controlled measurement) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end.") == 1
    assert "owner-named transfer) at the" not in section and "on API-cost fallback at the" not in section
    # A frozen setter at another effort of the same model is named at its own effort (O91): the common-leaf ranking's low
    # setter and both of the AI Coding Daily ranking's setters (measuredOnlyPlanView.calibration.workloads[].officialAnchorProvenance).
    assert "Official Plan anchors are set by GPT-6.1 Sol (low) on ChatGPT Pro 500 (same-model measurement from another effort) at the low end and GPT-6 Astra (max) on ChatGPT Plus (controlled measurement) at the high end." in section
    assert "Official Plan anchors are set by GPT-6.1 Sol (low) on ChatGPT Pro 500 (same-model measurement from another effort) at the low end and GPT-6 Astra (high) on ChatGPT Plus (same-model measurement from another effort) at the high end." in section
    # Reversals and the largest value change per ranking (calibration.reversals, calibration.maxAbsValueChange): the common-leaf
    # ranking has three reversals (2.56), the AI Coding Daily (2.79) and max-effort (3.29) rankings none.
    assert ("Pairwise reversals: Claude Opus 5.5 (xhigh) and GPT-6.1 Sol (medium); GPT-6 Astra (max) and GPT-6.1 Sol (low); "
            "GPT-6 Astra (high) and GPT-6.1 Sol (low). Largest value change: 2.56 points.") in section
    assert "Pairwise reversals: none. Largest value change: 2.79 points." in section
    assert "Pairwise reversals: none. Largest value change: 3.29 points." in section
    methodology = (emitted / "methodology.md").read_text()
    assert "labelled conventional CI-range sensitivity (endpoint-conditioned; no tail model) under its interpretation contract (E165" in methodology


def test_release_text_lint_blocks_a_sentence_that_puts_run_ranges_into_scenario_shares(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc["v3"]["scenarios"].__setitem__("notQuantified", ["benchmark run-to-run ranges enter the S2 scenario shares"]))
    with pytest.raises(ValueError, match=r"release-text lint \(E155\) rejects: methodology.md: - benchmark run-to-run ranges enter the S2 scenario shares"):
        emit(repo_copy)


def test_a_basis_without_blockers_names_none(repo_copy, pinned_clock):
    """I79: the blocker sentence appears only when some row competes without a label."""

    def no_blockers(document):
        for section in [document["v3"], *document["v3Tracks"].values()]:
            api = section["intervals"]["api"]
            for row_id in api.get("blockers", []):
                api["frontier"].pop(row_id, None)
                for bar in api.get("bars", []):
                    bar.get("rows", {}).pop(row_id, None)
            api["blockers"] = []

    edit_json(repo_copy, "scores.json", no_blockers)
    assert emit(repo_copy) == 0
    readme = (repo_copy / "README.md").read_text()
    api_sentence = next(line for line in readme.splitlines() if line.startswith("- API basis, main workload"))
    assert "Competing without a label" not in api_sentence
    assert "**API basis, main workload: frontier.** Not evaluable:" in (repo_copy / "scores.md").read_text()
