"""Unit tests for the pure helpers of the publication emitter."""

from valuerank import emit_docs as ed

WEIGHTS = [
    {"key": "a", "label": "Alpha", "priority": 3, "weightPct": 60.0, "higherBetter": True},
    {"key": "b", "label": "Beta", "priority": 1, "weightPct": 40.0, "higherBetter": False},
]


def test_number_formatters():
    assert ed.fnum(1.234) == "1.23"
    assert ed.fnum(1.234, 1) == "1.2"
    assert ed.fnum(None) == "—"
    assert ed.fnum("x", dash="n/a") == "n/a"
    assert ed.pct(0.1234) == "12.34%"
    assert ed.pct(None) == "—"
    assert ed.names(["a", "b"]) == "a, b"
    assert ed.names([]) == "none"


def test_benchmark_links():
    assert ed.md_benchmark_link("SciCode") == "[SciCode](https://artificialanalysis.ai/evaluations/scicode)"
    assert ed.md_benchmark_link("Unknown thing") == "Unknown thing"
    assert ed.html_external_link("A&B", 'u"v') == '<a href="u&quot;v" target="_blank" rel="noopener">A&amp;B</a>'


class TestMetricCoverageSummary:
    def test_uses_declared_coverage(self):
        model = {"dims": {"a": 1.0}, "metricCoverage": {"missingKeys": ["b"], "availablePriority": 3, "totalPriority": 4, "coveragePct": 75}}
        assert ed.metric_coverage_summary(model, WEIGHTS) == ("75.00% (3/4 priority)", "Beta")

    def test_derives_everything_when_coverage_is_absent(self):
        model = {"dims": {"a": 1.0, "b": None}}
        assert ed.metric_coverage_summary(model, WEIGHTS) == ("75.00% (3/4 priority)", "Beta")

    def test_nothing_missing(self):
        model = {"dims": {"a": 1.0, "b": 2.0}, "metricCoverage": {"missingKeys": None}}
        assert ed.metric_coverage_summary(model, WEIGHTS) == ("100.00% (4/4 priority)", "none")

    def test_zero_total_priority_has_no_percentage(self):
        zero = [{"key": "a", "label": "Alpha"}]
        assert ed.metric_coverage_summary({"dims": {}}, zero) == ("—", "Alpha")


class TestTables:
    def test_dimension_table_numbers_weights(self):
        assert ed.dimension_table(WEIGHTS).splitlines() == ["| 1 | Alpha | 60.00% | higher |", "| 2 | Beta | 40.00% | lower |"]

    def test_norm_values_marks_missing_dimensions(self):
        assert ed.norm_values({"dims": {"a": 12.345}}, WEIGHTS) == "12.3, ⊘"

    def test_primary_rows_render_rank_and_dash(self):
        rows = ed.primary_rows(
            [{"name": "M1", "rank": 1, "overallScore": 80.0, "qualityScore": 70.0, "costComposite": 55.5, "dims": {"a": 1, "b": 2}},
             {"name": "M2", "dims": {}}],
            WEIGHTS,
        ).splitlines()
        assert rows[0].startswith("| 1 | M1 | 80.0 | 70.0 | 55.50 | 100.00% (4/4 priority) | Missing: none |")
        assert rows[1].startswith("| — | M2 | — | — | — | 0.00% (0/4 priority)") and rows[1].endswith("Missing: Alpha, Beta |")

    def test_livebench_and_tb4_tables(self):
        live = ed.livebench_table([{"name": "N", "livebenchModel": "lb", "instructionFollowingScore": 1.0, "overallScore": 2.0, "costPerSuccessfulTaskUsd": 0.5}])
        assert live == "| N | lb | 1.00 | 2.00 | $0.5000 |"
        tb4 = ed.tb4_table([{"rankLabel": "1", "baseModel": "B", "agent": "A", "resolutionRatePct": 50.0, "uncertaintyPct": 2.0, "tokens": "1M", "costUsd": 1234.4}])
        assert tb4 == "| 1 | B | A | 50.0% ± 2.0% | 1M | $1,234 |"

    def test_bug_hunt_tables(self):
        record = {"fixedOf105": 50, "sampleN": 3, "aggregation": "mean", "effort": "high", "effortStatus": "owner", "harness": "H", "route": "R",
                  "matched": True, "evaluatedModel": "E", "sourceUrl": "http://s",
                  "availableOwnerConfigurations": [{"fixedOf105": 40, "selected": False, "selectionReason": "why"}, {"fixedOf105": 41, "selected": True}]}
        emphasis = ed.bug_hunt_emphasis_table({"ranking": [{"modelId": "m", "rank": 1, "name": "N", "emphasisScore": 90.0, "primaryRank": 2}]}, {"m": record})
        assert emphasis == "| 1 | N | 50/105 | 90.0 | n=3 (mean) | high (owner) | H / R | 2 |"
        raw = ed.bug_hunt_raw_table([{"id": "m", "name": "N"}, {"id": "u", "name": "U"}], {"m": record, "u": {"matchStatus": "mismatch"}}).splitlines()
        assert raw[0] == "| [N](http://s) | 50 | 3 / mean | E | high (owner) | H | R | Matched |"
        assert raw[1] == "| [U](https://bughunt.productcompass.pm/) | — | — / — | — | — (—) | — | — | mismatch |"
        assert len(raw) == 3 and "excluded from selected variant: why" in raw[2]

    def test_bug_hunt_raw_table_default_selection_reason(self):
        record = {"matched": True, "availableOwnerConfigurations": [{"fixedOf105": 1}], "note": "n"}
        last = ed.bug_hunt_raw_table([{"id": "m", "name": "N"}], {"m": record}).splitlines()[-1]
        assert last.endswith("excluded from selected variant: n |")

    def test_deepswe_chart_table_covers_matched_and_unmatched(self):
        rows = ed.deepswe_chart_table([
            {"sourceOrder": 1, "agent": "A", "model": "M", "effort": "high", "scorePct": 50.0, "valueRankModelId": "x", "matchNote": "ok"},
            {"sourceOrder": 2, "agent": "B", "model": "N", "scorePct": 40.0, "matchStatus": "not_selected"},
        ]).splitlines()
        assert rows == ["| 1 | A | M | high | 50.0% | Exact: x | ok |", "| 2 | B | N | not shown | 40.0% | not selected | — |"]


class TestPlanHelpers:
    def test_evidence_labels(self):
        assert ed.plan_evidence_label({"evidenceClass": "user_assumption"}) == "Provisional assumption"
        assert ed.plan_evidence_label({"evidenceClass": "controlled_account_workload_projection"}).startswith("Controlled account")
        assert ed.plan_evidence_label({"evidenceClass": "other_kind"}) == "other kind"
        assert ed.plan_evidence_label({}) == "Unclassified"

    def test_usd_and_source(self):
        assert ed.plan_usd(1234.5, "n/a") == "$1,234.50"
        assert ed.plan_usd(None, "n/a") == "n/a"
        assert ed.plan_source_html({"sourceUrl": "http://x"}) == ed.html_external_link("Source", "http://x")
        assert ed.plan_source_html({}) == "User assumption"

    def test_intelligence_labels(self):
        aa = {"models": {"m": {"metricSources": {"intelligenceIndex": {"precision": "display-rounded"}}}, "n": {"extraction": {"precision": "display-rounded"}}}}
        assert ed.plan_intelligence_label({"id": "m", "intelligenceIndex": 60.0}, aa) == "60 (rounded)"
        assert ed.plan_intelligence_label({"id": "n", "intelligenceIndex": 61.5}, aa) == "61.5 (rounded)"
        assert ed.plan_intelligence_label({"id": "z", "intelligenceIndex": 60.25, "intelligenceIndexStatus": "estimated"}, aa) == "60.25 (estimated)"
        assert ed.plan_intelligence_label({"id": "z"}, {}) == "—"

    def test_markdown_table_escapes_pipes_and_links_sources(self):
        table = ed.plan_markdown_table(["H1", "H2"], [["a|b", "https://x.test"], ["c\nd", 1]]).splitlines()
        assert table == ["| H1 | H2 |", "|---|---|", "| a\\|b | [Source](https://x.test) |", "| c d | 1 |"]

    def test_html_table_escapes_cells_and_links_sources(self):
        table = ed.plan_html_table(["H<1"], [["<b>"], ["https://x.test"]])
        assert '<th scope="col">H&lt;1</th>' in table
        assert "<td>&lt;b&gt;</td>" in table
        assert 'href="https://x.test"' in table
