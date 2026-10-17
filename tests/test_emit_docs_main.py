"""End-to-end behaviour of ``emit_docs.main`` against temporary repo copies."""

import json
import re
import runpy
import sys

import pytest

from test_emit_docs_support import CODING, SITE, committed, edit_json, emit, site_text
from valuerank import emit_docs
from valuerank import paths


@pytest.fixture
def emitted(repo_copy, pinned_clock):
    assert emit(repo_copy) == 0
    return repo_copy


def scores_document():
    return json.loads(committed("data/scores.json"))


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


def test_readme_ranks_models_in_order(emitted):
    scores = scores_document()
    ranked = [m for m in scores["models"] if m.get("rankingEligible") is True]
    rows = table_rows((emitted / "README.md").read_text(), "| Rank | Model | Overall")
    assert [row.split(" | ")[1] for row in rows] == [m["name"] for m in ranked]
    assert [row.split(" | ")[0] for row in rows] == [f"| {m['rank']}" for m in ranked]
    readme = (emitted / "README.md").read_text()
    assert f"**Scope:** {len(ranked)} primary-ranked models" in readme
    assert f"**{', '.join(scores['pareto'])}**" in readme
    assert readme.startswith("# ValueRank\n")
    assert "## AA intelligence and total-cost comparison" in readme


def test_methodology_lists_retained_weights_summing_to_100(emitted):
    scores = scores_document()
    text = (emitted / "methodology.md").read_text()
    rows = table_rows(text, "| # | Dimension | ValueRank weight")
    assert len(rows) == len(scores["weights"])
    percentages = [float(re.search(r"([\d.]+)%", row).group(1)) for row in rows]
    assert sum(percentages) == pytest.approx(100.0, abs=0.05)
    assert "\n\n## Subscription evidence policy\n\n" in text


def test_scores_md_pareto_line_matches_scores_json(emitted):
    scores = scores_document()
    text = (emitted / "scores.md").read_text()
    assert f"Undominated on composite cost versus quality: **{', '.join(scores['pareto'])}**." in text
    assert text.startswith(f"# ValueRank {emit_docs.VERSION} Scores")
    order = re.search(r"Dimension order is the order in weights above:\n\n\[(.*?)\]", text).group(1)
    assert order == ", ".join(w["key"] for w in scores["weights"])


def test_raw_data_lists_every_deepswe_configuration(emitted):
    configs = json.loads(committed("data/aa_deepswe.json"))["configurations"]
    text = (emitted / "raw-data.md").read_text()
    rows = table_rows(text, "| # | Agent | Evaluated model variant")
    assert len(rows) == len(configs)
    for row, config in zip(rows, configs):
        assert row.startswith(f"| {config['sourceOrder']} | {config['agent']} | {config['model']} |")
    assert f"The AA chart publishes {len(configs)} DeepSWE v1.1" in text


def test_site_chart_tabs_start_with_pareto_then_livebench(emitted):
    html = site_text(emitted)
    tabs = re.search(r'<div class="chart-tabs">([\s\S]*?)</div>', html).group(1)
    charts = re.findall(r'data-chart="([^"]+)"', tabs)
    assert charts[:2] == ["pareto", "livebenchPareto"]
    assert len(charts) == len(set(charts))
    assert ">ValueRank Pareto Frontier<" in tabs


def test_site_is_stamped_with_version_date_and_cohort(emitted):
    html = site_text(emitted)
    scores = scores_document()
    n = len([m for m in scores["models"] if m.get("rankingEligible") is True])
    assert f"{emit_docs.DATE} · {n} models · {len(scores['weights'])} scored dimensions" in html
    assert html.count("<!-- aa-reconciliation:start -->") == 1
    assert html.index("<!-- aa-reconciliation:start -->") < html.index("</main>")


def test_coding_agents_page_is_marked_historical(emitted):
    page = (emitted / CODING).read_text()
    assert "<th>TB2.1 (historical)</th>" in page
    assert "Historical snapshot · 42 agent variants" in page


def test_coding_agents_page_absent_is_skipped(repo_copy, pinned_clock):
    (repo_copy / CODING).unlink()
    assert emit(repo_copy) == 0
    assert not (repo_copy / CODING).exists()
    assert (repo_copy / SITE).exists()


def test_summary_json_is_printed(repo_copy, pinned_clock, capsys):
    emit(repo_copy)
    out = capsys.readouterr().out
    summary = json.loads(out[out.rindex('{\n  "version"'):])
    assert summary["version"] == emit_docs.VERSION
    assert summary["outputs"][-1] == "site/coding-agents/index.html"


def test_dropped_dimensions_declared_in_scores_are_used(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc.update(droppedDimensions=[{"label": "Zeta bench", "missing": ["m1", "m2"], "reason": "coverage gap"}]))
    assert emit(repo_copy) == 0
    assert "| Zeta bench | m1, m2 | coverage gap |" in (repo_copy / "methodology.md").read_text()


def test_unknown_weight_dimension_is_rejected(repo_copy, pinned_clock):
    def add_weight(doc):
        doc["weights"].append({"key": "bogus", "label": "Bogus", "weightPct": 0.0, "higherBetter": True, "priority": 0})

    edit_json(repo_copy, "scores.json", add_weight)
    with pytest.raises(SystemExit, match=r"site dimension metadata missing: \['bogus'\]"):
        emit(repo_copy)


def test_macro_category_without_dimensions_is_left_out(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", lambda doc: doc.update(weights=[w for w in doc["weights"] if w["key"] != "livebenchInstructionFollowing"]))
    assert emit(repo_copy) == 0
    macro = re.search(r"const MACRO_CATS = (\[.*?\]);", site_text(repo_copy), re.S).group(1)
    assert "Language" not in macro


def test_main_guard_runs_the_emitter(repo_copy, pinned_clock, monkeypatch, capsys):
    monkeypatch.setattr(paths, "ROOT", repo_copy)
    monkeypatch.setattr(paths, "DATA", repo_copy / "data")
    monkeypatch.delitem(sys.modules, "valuerank.emit_docs")
    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.emit_docs", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert (repo_copy / "README.md").read_text() == committed("README.md")
    assert '"version": "v1.9.6"' in capsys.readouterr().out
