"""Unit tests for the pure helpers of the Markdown emitter."""

from test_publication import FOOTNOTE, SELECTION
from valuerank import emit_docs as ed
from valuerank.publication import model_inclusion


def test_number_formatters():
    assert ed.fnum(1.234) == "1.23"
    assert ed.fnum(1.234, 1) == "1.2"
    assert ed.fnum(None) == "—"
    assert ed.fnum("x", dash="n/a") == "n/a"
    assert ed.pct(0.1234) == "12.34%"
    assert ed.pct(0.5, 0) == "50%"
    assert ed.pct(None) == "—"
    assert ed.usd(1234.5) == "$1,234.50"
    assert ed.usd(0.12345, 4) == "$0.1235"
    assert ed.usd(None) == "—"
    assert ed.share(0.5734) == "57.3%"
    assert ed.names(["a", "b"]) == "a, b"
    assert ed.names([]) == "none"
    assert ed.series([]) == "none" and ed.series(["a"]) == "a"
    assert ed.series(["a", "b"]) == "a and b" and ed.series(["a", "b", "c"]) == "a, b and c"


def test_markdown_table_aligns_numeric_columns_and_escapes_cells():
    table = ed.markdown_table(["Name", "Value"], [["a|b", 1], ["c\nd", 2.5]], numeric={1}).splitlines()
    assert table == ["| Name | Value |", "|---|---:|", "| a\\|b | 1 |", "| c d | 2.5 |"]
    assert ed.markdown_table(["Only"], []) == "| Only |\n|---|"


def test_component_labels_fall_back_to_the_key():
    assert ed.component_label("coding-agent-index") == "Coding Agent Index"
    assert ed.component_label("unknown-component") == "unknown-component"


def test_configuration_and_model_labels():
    names = {"m": "Model M"}
    assert ed.configuration_label({"id": "m", "effort": "max"}, names) == "Model M (max)"
    assert ed.configuration_label({"id": "m", "effort": None}, names) == "Model M"
    entry = {"name": "Model M", "slug": "model-m"}
    assert ed.model_link(entry) == "[Model M](https://valuerank.alolabs.dev/models/model-m/)"
    assert ed.model_link(entry, "Model M (max)") == "[Model M (max)](https://valuerank.alolabs.dev/models/model-m/)"


def entry_with(**cost):
    base = {"subset": False, "partialComponents": [], "fallback": None, "route": None}
    return {"cost": {**base, **cost}, "coverage": {"provisional": False}}


def test_short_flags_name_every_condition_in_legend_order():
    assert ed.short_flags(entry_with(), {}) == "—"
    everything = entry_with(subset=True, partialComponents=["gdp-pdf"], fallback="api")
    everything["coverage"]["provisional"] = True
    assert ed.short_flags(everything, {"aaCostCaveat": "note"}) == (
        "subset cost, provisional quality, partial component, AA cost caveat, API-cost fallback"
    )
    assert [word for word, _text in ed.FLAG_LEGEND] == [
        "subset cost", "provisional quality", "partial component", "AA cost caveat", "API-cost fallback",
    ]


def test_route_text_names_the_route_or_a_dash():
    assert ed.route_text(entry_with()) == "—"
    route = {"planLabel": "Plan X", "valueMultiple": 10.772, "grade": "measured"}
    assert ed.route_text(entry_with(route=route)) == "Plan X (10.772×, measured)"


def test_run_labels_mark_the_endpoint_heavy_kernel():
    assert ed.run_label({"stratum": "S1", "alternative": False}) == "S1"
    assert ed.run_label({"stratum": "S1", "alternative": True}) == "S1 endpoint-heavy"


def test_rank_change_text_reports_the_largest_moves():
    def label(ids):
        return ", ".join(ids)

    assert ed.rank_change_text({"a": 0, "b": 0}, label) == "no rank changes"
    assert ed.rank_change_text({"a": 2, "b": -2, "c": 1, "d": 0}, label) == "3 rows move; largest move 2 (a, b)"


def test_terminal_bench_and_deepswe_tables():
    tb4 = ed.tb4_table([{"rankLabel": "1", "baseModel": "B", "agent": "A", "resolutionRatePct": 50.0, "uncertaintyPct": 2.0, "tokens": "1M", "costUsd": 1234.4}])
    assert tb4 == "| 1 | B | A | 50.0% ± 2.0% | 1M | $1,234 |"
    unpriced = ed.tb4_table([{"rankLabel": "2", "baseModel": "M", "agent": "A", "resolutionRatePct": 14.5, "uncertaintyPct": 2.9, "tokens": "9.0B", "costUsd": None}])
    assert unpriced == "| 2 | M | A | 14.5% ± 2.9% | 9.0B | — |"
    rows = ed.deepswe_chart_table([
        {"sourceOrder": 1, "agent": "A", "model": "M", "effort": "high", "scorePct": 50.0, "valueRankModelId": "x", "matchNote": "ok"},
        {"sourceOrder": 2, "agent": "B", "model": "N", "scorePct": 40.0, "matchStatus": "not_selected"},
    ]).splitlines()
    assert rows == ["| 1 | A | M | high | 50.0% | Exact: x | ok |", "| 2 | B | N | not shown | 40.0% | not selected | — |"]


def test_model_inclusion_markdown_lists_rules_facts_families_and_footnotes():
    text = ed.model_inclusion_markdown(model_inclusion(SELECTION, [{"name": "Haiku", "aaFrontierFootnote": FOOTNOTE}]))
    assert text.startswith("## Model inclusion\n")
    assert "**Frontier rule.**" in text and "**Near-frontier rule.**" in text
    assert "Chart observed 2026-10-17T18:48:27Z" in text and "Within 3 Index points of the frontier at its cost." in text
    assert "- GPT-6 Luna: GPT-6 Luna (max)" in text
    assert "- Gemini 4 Argon: Gemini 4 Argon (high), 2 Index points below the frontier" in text
    assert "- GPT-6 Astra: GPT-6 Astra (xhigh), 1.5 Index points below the frontier" in text
    assert f"AA footnote (Haiku): {FOOTNOTE}" in text


def test_model_inclusion_markdown_says_one_index_point_in_the_singular():
    selection = {"nearFrontierFamilies": [{"family": "F", "configuration": "F (high)", "intelligenceGap": 1}]}
    assert "- F: F (high), 1 Index point below the frontier" in ed.model_inclusion_markdown(model_inclusion(selection, []))


def test_model_inclusion_markdown_with_no_data_renders_only_the_rules():
    text = ed.model_inclusion_markdown(model_inclusion(None, []), level="###")
    assert text.startswith("### Model inclusion")
    assert "Frontier families" not in text and "Near-frontier families" not in text and "footnote" not in text
    assert "Near-frontier rule" in text
