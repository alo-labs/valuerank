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
        assert ed.metric_coverage_summary(model, WEIGHTS) == ("75.00% (3/4 quality priority)", "Beta")

    def test_derives_everything_when_coverage_is_absent(self):
        model = {"dims": {"a": 1.0, "b": None}}
        assert ed.metric_coverage_summary(model, WEIGHTS) == ("75.00% (3/4 quality priority)", "Beta")

    def test_nothing_missing(self):
        model = {"dims": {"a": 1.0, "b": 2.0}, "metricCoverage": {"missingKeys": None}}
        assert ed.metric_coverage_summary(model, WEIGHTS) == ("100.00% (4/4 quality priority)", "none")

    def test_cost_share_is_named_when_the_model_has_a_cost(self):
        model = {"dims": {"a": 1.0}, "metricCoverage": {"costAvailable": True, "missingKeys": ["b"], "availablePriority": 3, "totalPriority": 4, "coveragePct": 81.25}}
        assert ed.metric_coverage_summary(model, WEIGHTS) == ("81.25% (cost + 3/4 quality priority)", "Beta")

    def test_a_cost_weight_without_priority_counts_as_zero_priority(self):
        weights = [{"key": "costComposite", "label": "Cost", "priority": None}, *WEIGHTS]
        assert ed.metric_coverage_summary({"dims": {"a": 1.0, "costComposite": 5.0}}, weights) == ("75.00% (3/4 quality priority)", "Beta")

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
        assert rows[0].startswith("| 1 | M1 | 80.0 | 70.0 | 55.50 | 100.00% (4/4 quality priority) | Missing: none |")
        assert rows[1].startswith("| — | M2 | — | — | — | 0.00% (0/4 quality priority)") and rows[1].endswith("Missing: Alpha, Beta |")

    def test_livebench_and_tb4_tables(self):
        live = ed.livebench_table([{"name": "N", "livebenchModel": "lb", "instructionFollowingScore": 1.0, "overallScore": 2.0, "costPerSuccessfulTaskUsd": 0.5}])
        assert live == "| N | lb | 1.00 | 2.00 | $0.5000 |"
        tb4 = ed.tb4_table([{"rankLabel": "1", "baseModel": "B", "agent": "A", "resolutionRatePct": 50.0, "uncertaintyPct": 2.0, "tokens": "1M", "costUsd": 1234.4}])
        assert tb4 == "| 1 | B | A | 50.0% ± 2.0% | 1M | $1,234 |"
        unpriced = ed.tb4_table([{"rankLabel": "2", "baseModel": "M", "agent": "A", "resolutionRatePct": 14.5, "uncertaintyPct": 2.9, "tokens": "9.0B", "costUsd": None}])
        assert unpriced == "| 2 | M | A | 14.5% ± 2.9% | 9.0B | — |"

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


SELECTION = {
    "capturedAt": "2026-10-17T18:48:27Z",
    "indexVersion": "4.3.2",
    "sourceUniverse": {"selectedModelN": 694, "plottedPointN": 189, "observedFrontierPointN": 18},
    "familyN": 7,
    "nearFrontierPolicy": {"maxIntelligenceGap": 3, "basis": "public rounded Index", "text": "Within 3 Index points of the frontier at its cost."},
    "nearFrontierPointN": 9,
    "nearFrontierFamilyN": 2,
    "nearFrontierRequiredModelN": 2,
    "nearFrontierDeferredN": 0,
    "frontierFamilies": [{"family": "GPT-6 Luna", "modelId": "gpt-6-luna", "configuration": "GPT-6 Luna (max)"}],
    "nearFrontierFamilies": [
        {"family": "Gemini 4 Argon", "modelId": "gemini-4-argon", "configuration": "Gemini 4 Argon (high)", "intelligenceGap": 2},
        {"family": "GPT-6 Astra", "modelId": "gpt-6-astra", "configuration": "GPT-6 Astra (xhigh)", "intelligenceGap": 1.5},
    ],
}
FOOTNOTE = "Claude Haiku 5.5 has 5x higher pricing on longer-context inputs."


class TestModelInclusion:
    def test_absent_selection_has_only_the_rules(self):
        inclusion = ed.model_inclusion(None, [])
        assert inclusion["observation"] is None
        assert inclusion["frontierFamilies"] == [] and inclusion["nearFrontierFamilies"] == [] and inclusion["footnotes"] == []
        assert "rendered" in inclusion["frontierRule"] and "3 points" in inclusion["nearFrontierRule"]
        assert inclusion["policyText"] is None

    def test_facts_are_read_from_the_selection(self):
        inclusion = ed.model_inclusion(SELECTION, [])
        assert inclusion["observation"] == (
            "Chart observed 2026-10-17T18:48:27Z (Intelligence Index v4.3.2): 694 catalog models selected, 189 plotted points and "
            "18 rendered Pareto vertices across 7 families. 9 plotted points across 2 families are near-frontier."
        )
        assert inclusion["policyText"] == "Within 3 Index points of the frontier at its cost."
        assert inclusion["frontierFamilies"] == [{"family": "GPT-6 Luna", "configuration": "GPT-6 Luna (max)"}]
        assert inclusion["nearFrontierFamilies"][0] == {"family": "Gemini 4 Argon", "configuration": "Gemini 4 Argon (high)", "gap": "2"}
        assert inclusion["nearFrontierFamilies"][1]["gap"] == "1.5"
        assert "2 required" in inclusion["nearFrontierStatus"] and "0 deferred" in inclusion["nearFrontierStatus"]

    def test_threshold_follows_the_policy(self):
        inclusion = ed.model_inclusion({"nearFrontierPolicy": {"maxIntelligenceGap": 5}}, [])
        assert "5 points" in inclusion["nearFrontierRule"] and inclusion["nearFrontierGap"] == "5"
        assert ed.model_inclusion(None, [])["nearFrontierGap"] == "3"

    def test_partial_selection_omits_missing_facts(self):
        inclusion = ed.model_inclusion({"capturedAt": "2026-10-17T18:48:27Z"}, [])
        assert inclusion["observation"] == "Chart observed 2026-10-17T18:48:27Z."
        assert inclusion["nearFrontierStatus"] is None
        assert ed.model_inclusion({"nearFrontierPointN": 1, "nearFrontierFamilyN": 1}, [])["observation"] == (
            "1 plotted point across 1 family is near-frontier."
        )
        assert ed.model_inclusion({"nearFrontierPointN": 2}, [])["observation"] == "2 plotted points are near-frontier."
        assert ed.model_inclusion({"indexVersion": "4.3.2", "sourceUniverse": {"plottedPointN": 1}}, [])["observation"] == (
            "Chart observed (Intelligence Index v4.3.2): 1 plotted point."
        )

    def test_footnotes_are_grouped_once_per_distinct_text(self):
        models = [
            {"name": "Haiku A", "aaFrontierFootnote": FOOTNOTE},
            {"name": "Haiku B", "aaFrontierFootnote": FOOTNOTE},
            {"name": "Other", "aaFrontierFootnote": None},
            {"name": "NoField"},
            {"name": "Distinct", "aaFrontierFootnote": "Another note."},
        ]
        assert ed.model_inclusion(None, models)["footnotes"] == [
            {"text": FOOTNOTE, "models": ["Haiku A", "Haiku B"]},
            {"text": "Another note.", "models": ["Distinct"]},
        ]

    def test_markdown_lists_rules_facts_families_and_footnotes(self):
        text = ed.model_inclusion_markdown(ed.model_inclusion(SELECTION, [{"name": "Haiku", "aaFrontierFootnote": FOOTNOTE}]))
        assert text.startswith("## Model inclusion\n")
        assert "**Frontier rule.**" in text and "**Near-frontier rule.**" in text
        assert "Chart observed 2026-10-17T18:48:27Z" in text and "Within 3 Index points of the frontier at its cost." in text
        assert "- GPT-6 Luna: GPT-6 Luna (max)" in text
        assert "- Gemini 4 Argon: Gemini 4 Argon (high), 2 Index points below the frontier" in text
        assert f"AA footnote (Haiku): {FOOTNOTE}" in text

    def test_markdown_with_no_data_renders_only_the_rules(self):
        text = ed.model_inclusion_markdown(ed.model_inclusion(None, []))
        assert "Frontier families" not in text and "Near-frontier families" not in text and "footnote" not in text
        assert text.count("\n## ") == 0 and "Near-frontier rule" in text
