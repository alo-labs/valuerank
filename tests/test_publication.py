"""The shared public vocabulary: route evidence labels and the model-inclusion policy."""

from valuerank import publication as pub

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


def test_evidence_labels():
    assert pub.plan_evidence_label({"evidenceClass": "user_assumption"}) == "Provisional assumption"
    assert pub.plan_evidence_label({"evidenceClass": "controlled_account_workload_projection"}).startswith("Controlled account")
    assert pub.plan_evidence_label({"evidenceClass": "other_kind"}) == "other kind"
    assert pub.plan_evidence_label({}) == "Unclassified"


def test_benchmark_urls_share_the_source_constants():
    assert pub.BENCHMARK_URLS["Terminal-Bench 4.0"] == pub.TERMINAL_BENCH_URL
    assert pub.BENCHMARK_URLS["DeepSWE pass@1"] == pub.AA_DEEPSWE_URL
    assert pub.BENCHMARK_URLS["Bug Hunt Bench"] == pub.BUG_HUNT_URL


class TestModelInclusion:
    def test_absent_selection_has_only_the_rules(self):
        inclusion = pub.model_inclusion(None, [])
        assert inclusion["observation"] is None
        assert inclusion["frontierFamilies"] == [] and inclusion["nearFrontierFamilies"] == [] and inclusion["footnotes"] == []
        assert "rendered" in inclusion["frontierRule"] and "3 points" in inclusion["nearFrontierRule"]
        assert inclusion["policyText"] is None

    def test_facts_are_read_from_the_selection(self):
        inclusion = pub.model_inclusion(SELECTION, [])
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
        inclusion = pub.model_inclusion({"nearFrontierPolicy": {"maxIntelligenceGap": 5}}, [])
        assert "5 points" in inclusion["nearFrontierRule"] and inclusion["nearFrontierGap"] == "5"
        assert pub.model_inclusion(None, [])["nearFrontierGap"] == "3"

    def test_partial_selection_omits_missing_facts(self):
        inclusion = pub.model_inclusion({"capturedAt": "2026-10-17T18:48:27Z"}, [])
        assert inclusion["observation"] == "Chart observed 2026-10-17T18:48:27Z."
        assert inclusion["nearFrontierStatus"] is None
        assert pub.model_inclusion({"nearFrontierPointN": 1, "nearFrontierFamilyN": 1}, [])["observation"] == (
            "1 plotted point across 1 family is near-frontier."
        )
        assert pub.model_inclusion({"nearFrontierPointN": 2}, [])["observation"] == "2 plotted points are near-frontier."
        assert pub.model_inclusion({"indexVersion": "4.3.2", "sourceUniverse": {"plottedPointN": 1}}, [])["observation"] == (
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
        assert pub.model_inclusion(None, models)["footnotes"] == [
            {"text": FOOTNOTE, "models": ["Haiku A", "Haiku B"]},
            {"text": "Another note.", "models": ["Distinct"]},
        ]

    def test_footnote_names_carry_the_effort_so_ranked_siblings_read_distinctly(self):
        """O33: a family's primary is named without its effort, so the effort is added unless the name ends with it."""

        models = [
            {"name": "Claude Haiku 5.5", "aaVariant": "xhigh", "aaFrontierFootnote": FOOTNOTE},
            {"name": "Claude Haiku 5.5 (max)", "aaVariant": "max", "aaFrontierFootnote": FOOTNOTE},
            {"name": "MiMo-V2.6-Flash", "aaVariant": None, "aaFrontierFootnote": FOOTNOTE},
        ]
        assert pub.model_inclusion(None, models)["footnotes"] == [
            {"text": FOOTNOTE, "models": ["Claude Haiku 5.5 (xhigh)", "Claude Haiku 5.5 (max)", "MiMo-V2.6-Flash"]},
        ]
