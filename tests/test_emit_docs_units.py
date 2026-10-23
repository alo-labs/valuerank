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
    # O33: a ranked sibling's name already carries its effort, which is not repeated.
    assert ed.configuration_label({"id": "s", "effort": "xhigh"}, {"s": "Model M (xhigh)"}) == "Model M (xhigh)"
    entry = {"name": "Model M", "slug": "model-m"}
    assert ed.model_link(entry) == "[Model M](https://valuerank.alolabs.dev/models/model-m/)"
    assert ed.model_link(entry, "Model M (max)") == "[Model M (max)](https://valuerank.alolabs.dev/models/model-m/)"


def entry_with(**cost):
    base = {"subset": False, "partialComponents": [], "fallback": None, "route": None, "apiUsd": 100.0}
    return {"cost": {**base, **cost}, "coverage": {"provisional": False}}


UNVERIFIED = {"valuationGate": {"outcome": "valuation basis unverified"}}


def test_short_flags_name_every_condition():
    assert ed.short_flags(entry_with(), {}) == "—"
    everything = entry_with(subset=True, partialComponents=["gdp-pdf"], fallback="api")
    everything["coverage"]["provisional"] = True
    claimed = {"quality": {"leaves": {"deepswe": {"sourceType": "model_provider_claim"}, "hle": {}}}}
    flags = ed.short_flags(everything, {"aaCostCaveat": "note", **UNVERIFIED, **claimed}).split(", ")
    assert sorted(flags) == sorted(["subset cost", "provider-claimed leaf", "provisional quality", "partial component", "valuation basis unverified", "AA cost caveat", "API-cost fallback"])
    assert [word for word, _text in ed.FLAG_LEGEND] == [
        "subset cost", "provider-claimed leaf", "provisional quality", "partial component", "valuation basis unverified", "no cost", "AA cost caveat", "API-cost fallback",
    ]
    assert ed.short_flags(entry_with(), {"valuationGate": {"outcome": "compatible as captured"}}) == "—"
    assert ed.short_flags(entry_with(), UNVERIFIED) == "valuation basis unverified"


def test_a_row_without_a_cost_is_flagged_no_cost_and_nothing_cost_derived():
    """AGENTS.md: no cost means no value score; "subset cost" and "valuation basis unverified" describe a cost, so they are suppressed."""

    costless = entry_with(subset=True, apiUsd=None)
    costless["coverage"]["provisional"] = True
    assert ed.short_flags(costless, UNVERIFIED) == "provisional quality, no cost"
    assert ed.short_flags(entry_with(apiUsd=None), {}) == "no cost"


def test_short_flags_follow_the_legend_order():
    everything = entry_with(subset=True, partialComponents=["gdp-pdf"], fallback="api")
    everything["coverage"]["provisional"] = True
    flags = ed.short_flags(everything, {"aaCostCaveat": "note", **UNVERIFIED}).split(", ")
    legend = [word for word, _text in ed.FLAG_LEGEND]
    assert flags == sorted(flags, key=legend.index)


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


def test_plan_amount_text_names_the_kind_and_the_donor():
    amount = {"amountUsd": 1178.0, "feePeriod": "month", "amountKind": "measured-workload capacity", "donorRouteId": None}
    assert ed.plan_amount_text(amount) == "$1,178 per month: measured-workload capacity"
    assert ed.plan_amount_text({**amount, "amountUsd": None, "donorRouteId": "d"}) == "fee not established: measured-workload capacity from d"
    assert ed.plan_amount_text(None) == "—"


def test_agreement_text_reports_tau_or_the_undefined_status():
    defined = {"label": "quality agreement", "tau": 0.5, "interval": [0.1, 0.8], "panel": ["a", "b", "c"], "status": "defined"}
    assert ed.agreement_text(defined) == "quality agreement: Kendall tau 0.50 (interval 0.10 to 0.80) on 3 rows."
    undefined = {"label": "x", "tau": None, "interval": None, "panel": ["a"], "status": "undefined (panel too small)"}
    assert ed.agreement_text(undefined) == "x: undefined (panel too small); panel of 1 rows."


def test_dispersion_text_shows_the_sd_and_covariance_term():
    assert ed.dispersion_text({"status": "defined", "valueSd": 1.234, "covarianceTerm": -0.05}) == "1.23 (-0.05)"
    assert ed.dispersion_text({"status": "no scenario SD defined"}) == "no scenario SD defined"


class StubFacts:
    """The slice of emit_docs.Facts the cost-diagnostics section reads."""

    def __init__(self, diagnostics, **v3):
        self.v3 = {"diagnostics": diagnostics, **v3}
        self.scores, self.tb4 = {"models": []}, {"rows": []}

    @staticmethod
    def labels(row_ids):
        return ", ".join(row_ids)

    @staticmethod
    def label(row_id):
        return row_id


def cost_world(**overrides):
    diagnostics = {
        "basketReadiness": {"pricedMixCoverage": 2 / 3, "pricedLeaves": ["terminalBench", "lcr"], "components": {"coding-agent-index": {"status": "pending capture"}, "scicode": {"status": "admitted"}}},
        "sweCompanion": {"rows": {"a": {"flag": True}, "b": {"flag": False}}},
        "costedBarLadder": {"excluded": ["a"], "population": 2, "levels": [50.0, 45.04, 55.0]},
        "matchedCost": {"status": "evaluated", "pricedQualityWeight": 0.5, "reversals": [["a", "b"]], "warnings": []},
        "commonLeaf": {"sparseLeaves": [], "barReach": [], "bases": {basis: {"rankChanges": {"changes": {}}} for basis in ("api", "plan")}, "rows": {}, "flagged": []},
        "frontierAnchors": {"status": "evaluated", "references": ["a", "b"], "bases": {basis: {"rankChanges": {"changes": {"a": 1, "b": -1}}, "exchangeRate": {"valuePointsPerCostDoubling": 3.0}, "frozenExchangeRate": {"valuePointsPerCostDoubling": 3.5}} for basis in ("api", "plan")}, "bar": {"status": "unavailable: fewer than 2 non-provisional frontier-family configurations"}},
        "familyPrimary": {"status": "evaluated", "population": ["a", "b"], "references": ["a", "b"],
                          "ladder": [{"level": 58.27}, {"level": 50.01}, {"level": 60.88}], "frozenLadder": [{"level": 56.7}, {"level": 48.06}, {"level": 60.88}],
                          "bases": {basis: {"rankChanges": {"changes": {"a": 1, "b": -1}}, "exchangeRate": {"valuePointsPerCostDoubling": 3.04}, "frozenExchangeRate": {"valuePointsPerCostDoubling": 2.74}} for basis in ("api", "plan")}},
        "costComponentFamily": [
            {"component": "scicode", "bases": {basis: {"recalibrated": {"rankChanges": {"changes": {"a": 1, "b": -1}}, "exchangeRate": {"valuePointsPerCostDoubling": 5.0}}} for basis in ("api", "plan")}},
            {"component": "coding-agent-index", "status": "not in the admitted basket"},
        ],
        "subsetBridges": [{
            "subsetRows": ["s"], "missingComponents": ["coding-agent-index"], "pairedRows": ["a", "b"],
            "missingExpenditureShare": {"coding-agent-index": {"median": 0.4, "min": 0.1, "max": 0.6, "n": 2}, "other": {"median": None, "min": None, "max": None, "n": 0}},
            "bases": {"api": {"status": "evaluated", "valueDifference": {"median": -1.0, "min": -2.0, "max": 0.5}, "rankChanges": {"changes": {"a": 0, "b": 0}}},
                      "plan": {"status": "unavailable: fewer than 2 complete-evidence references"}},
        }],
    }
    diagnostics.update(overrides)
    currency = {"lifetime": "until the next re-freeze", "bars": [{"level": 56.7, "reachN": 18, "populationN": 35}], "currentLadder": [{"level": 56.7}], "flag": None}
    rows = [{"id": row_id, "quality": {"leaves": {}}, "plan": plan} for row_id, plan in
            (("a", {"mixCheck": "mix unidentified"}), ("b", {"mixCheck": "mix unidentified"}), ("c", {"mixCheck": "mix not reported"}), ("d", None))]
    observed = {"status": "evaluated", "bars": [{"bar": "bar:x", "possibleQualifierN": 17, "confirmedQualifierN": 5, "confirmedCheapest": None, "possibleCheapest": ["a", "b"]},
                                                {"bar": "bar:y", "possibleQualifierN": 3, "confirmedQualifierN": 3, "confirmedCheapest": "a", "possibleCheapest": ["a"]}]}
    policy = {"bars": [{"id": "bar:x", "level": 56.7}, {"id": "bar:y", "level": 60.9}]}
    required = {"status": "evaluated", "bars": [{"bar": "bar:x", "level": 56.7, "rows": [{"row": "a", "required": 27.3, "missing": ["frontierCode", "terminalBench"]}, {"row": "b", "required": None, "missing": []}]}]}
    return StubFacts(diagnostics, barCurrency=currency, rows=rows, observedRangeBars=observed, barPolicy=policy, requiredMissingScores=required)


def test_cost_diagnostics_markdown_covers_readiness_family_and_subset_bridges():
    text = ed.cost_diagnostics_markdown(cost_world())
    assert "priced leaves cover 67% of nominal quality weight (Terminal-Bench 4.0 (AA run), AA-LCR v1.1)" in text and "pending components: Coding Agent Index" in text
    assert "flagged far from the median ratio: a." in text and "reversals with separated intervals: 1" in text
    assert "have no cost (a); without them (2 rows) the ladder (headline, lower quartile, upper quartile) would be 50.0 / 45.0 / 55.0." in text
    assert ed.costed_ladder_text({"excluded": [], "population": 3, "levels": []}, StubFacts({})).endswith("today every such row has a cost, so the ladder is unchanged.")
    assert "| Coding Agent Index | — | — | — |" in text and "2 rows move; largest move 1" in text
    assert "values change by -1.00 points (median; -2.00 to 0.50)" in text
    assert "is 40% of the full basket (median; 10% to 60% over 2 rows)" in text and "other: no expenditure evidence" in text
    assert "Plan: unavailable: fewer than 2 complete-evidence references" in text and "the direction of its subset effect is not known" in text
    assert "anchors rebuilt from the 2 frontier and near-frontier references move API 2 rows move" in text and "(value points per cost doubling 3.00 vs 3.50 frozen)" in text
    quiet = ed.cost_diagnostics_markdown(cost_world(subsetBridges=[], matchedCost={"status": "unidentified (priced quality weight below 40%)"}, sweCompanion={"rows": {}},
                                                    frontierAnchors={"status": "unavailable: fewer than 2 frontier-family references", "bar": {"status": "unavailable"}}))
    assert "- **Frontier-families anchors (E187, diagnostic):** unavailable: fewer than 2 frontier-family references." in quiet
    assert "the ladder (headline, lower quartile, upper quartile) would be 58.3 / 50.0 / 60.9 against 56.7 / 48.1 / 60.9 frozen; anchors rebuilt from its 2 references move API 2 rows move" in text
    assert "(value points per cost doubling 3.04 vs 2.74 frozen)." in text
    assert ed.search_gap_text({"reportingWindow": {"end": "2026-10-21"}, "searchCutoff": "2026-10-08"}) == "; end-user reports were last searched on 2026-10-08, so reports dated in the 13 days after it were not searched"
    assert ed.search_gap_text({"reportingWindow": {"end": "2026-10-21"}, "searchCutoff": "2026-10-21"}) == ed.search_gap_text({"reportingWindow": {"end": "2026-10-21"}}) == ""
    assert "- **Bar currency (E207, informational):** rows reaching each frozen bar: quality 56.7: 18 of 35; the current population would freeze 56.7; lifetime until the next re-freeze; no staleness flag." in text
    assert "- **Token mix (E208):** 1 selected routes: mix not reported; 2 selected routes: mix unidentified." in text
    stale = ed.bar_currency_text({"lifetime": "l", "bars": [], "currentLadder": [], "flag": "headline bar below"})
    assert "no bar frozen; the current population would freeze unavailable" in stale and stale.endswith("flag: headline bar below.")
    assert ed.mix_check_text([{"plan": None}]) == "- **Token mix (E208):** no selected Plan route."
    assert ("- **Observed-range sensitivity (E219, not evidence; no label changes):** with each missing leaf inside the cohort's observed range for that leaf, "
            "quality 56.7: 17 can qualify, 5 confirmed; possibly cheapest a, b; quality 60.9: 3 can qualify, 3 confirmed; a confirmed cheapest.") in text
    assert ed.observed_range_text({"status": "unavailable: no bar"}, StubFacts({})).endswith("unavailable: no bar.")
    assert ("- **What would settle the headline bar (E221, not a claim):** rows that can but need not reach quality 56.7, with the mean score their missing leaves would need: "
            "a 27.3 (FrontierCode 1.1, Terminal-Bench 4.0 (AA run)); b (no missing leaf; reporting precision only).") in text
    assert ed.required_scores_text({"status": "evaluated", "bars": [{"bar": "x", "level": 50.0, "rows": []}]}, StubFacts({})).endswith("no row is open at quality 50.0.")
    assert ed.required_scores_text({"status": "evaluated", "bars": []}, StubFacts({})).endswith("no bar.")
    assert ed.required_scores_text({"status": "unavailable: x", "bars": []}, StubFacts({})).endswith("unavailable: x.")
    lone = ed.family_primary_text({"status": "unavailable: fewer than 2 family-primary references", "population": ["a"], "references": ["a"], "ladder": [], "frozenLadder": []}, StubFacts({}))
    assert lone.endswith("would be unavailable against unavailable frozen; anchors unavailable: fewer than 2 family-primary references.")
    assert "No row is scored on a subset workload." in quiet and "unidentified (priced quality weight below 40%)." in quiet and "flagged far from the median ratio: none." in quiet


def test_policy_bar_text_covers_each_outcome():
    """E199: the frontier-families bar sentence for unavailable, unresolved, confirmed and non-unique results."""

    class Facts:
        label = staticmethod(lambda row_id: row_id.upper())
        labels = staticmethod(lambda row_ids: ", ".join(row_id.upper() for row_id in row_ids))

    bar = {"level": 55.04}
    assert ed.policy_bar_text({"status": "unavailable: too few"}, Facts).endswith("unavailable: too few.")
    unresolved = {"status": "evaluated", "population": ["a", "b"], "bar": bar, "api": {"status": "unresolved"}}
    assert ed.policy_bar_text(unresolved, Facts).endswith("quality 55.0 over 2 configurations; API main workload unresolved.")
    confirmed = {**unresolved, "api": {"status": "certified", "confirmedCheapest": "a", "possibleCheapest": ["a"], "comparison": "compares 2 configurations that can qualify"}}
    assert "cheapest at or above it on the API main workload: A (confirmed) (compares 2" in ed.policy_bar_text(confirmed, Facts)
    open_ = {**unresolved, "api": {**confirmed["api"], "confirmedCheapest": None, "possibleCheapest": ["a", "b"]}}
    assert "not unique; possibly A, B" in ed.policy_bar_text(open_, Facts)


def test_coding_share_text_reports_the_median_coding_share():
    """E200: coding and terminal tasks' share of the basket's cost, over full-basket rows only."""

    def row(costs, full=True):
        return {"cost": {"fullCost": full, "costUsd": sum(costs.values()), "components": list(costs),
                         "componentsDetail": {key: {"costUsd": value} for key, value in costs.items()}}}

    rows = [row({"coding-agent-index": 40.0, "gdpval-aa": 60.0}), row({"coding-agent-index": 10.0, "scicode": 10.0, "gdpval-aa": 80.0}), row({"gdpval-aa": 5.0}, full=False)]
    text = ed.coding_share_text({"rows": rows, "admission": {"admitted": ["gdpval-aa"]}})
    assert "make up 30% of the basket's cost (median over 2 configurations with the full basket; 20% to 40%)" in text and "SWE-Atlas" not in text
    # O50: SWE-Atlas QnA's share is stated only while the Coding Agent Index is in the basket.
    with_index = ed.coding_share_text({"rows": rows, "admission": {"admitted": ["coding-agent-index", "gdpval-aa"]}})
    assert "SWE-Atlas QnA (124 of its 290 tasks) has no quality leaf either" in with_index
    assert ed.coding_share_text({"rows": rows[2:], "admission": {"admitted": []}}) == ""


def test_displayed_cheapest_sentences_name_the_row_or_none():
    """E203: one sentence per basis, each bar with its cheapest row and cost, or none."""

    class Facts:
        labels = staticmethod(lambda row_ids: ", ".join(row_ids))
        v3 = {"displayedCheapest": {basis: {"bars": [
            {"level": 50.0, "cheapest": ["a"], "costUsd": 12.0, "qualifierN": 3},
            {"level": 70.0, "cheapest": [], "costUsd": None, "qualifierN": 0},
        ]} for basis in ("api", "plan")},
              "diagnostics": {"gapFillBars": {"bases": {"api": [], "plan": []}}}}

    api, plan = ed.displayed_cheapest_sentences(Facts)
    assert api == "API basis, displayed record (not a claim; E203): cheapest at or above quality 50.0: a ($12.00 per basket run; 3 reach it); at or above quality 70.0: none."
    assert plan.startswith("Plan basis, displayed record")
    # O44 companions, E234 fill sensitivity and O43's scope note appear only when present.
    for basis in ("api", "plan"):
        Facts.v3["displayedCheapest"][basis]["margin"] = 4.5
        Facts.v3["displayedCheapest"][basis]["bars"][0]["margin"] = {"level": 54.5, "cheapest": ["b"], "costUsd": 20.0, "qualifierN": 2}
        Facts.v3["displayedCheapest"][basis]["bars"][1]["margin"] = {"level": 74.5, "cheapest": [], "costUsd": None, "qualifierN": 0}
    Facts.v3["diagnostics"]["gapFillBars"]["bases"]["api"] = [{"level": 50.0, "survives": False}]
    Facts.v3["listedIndicative"] = [{"name": "Listed X"}]
    sentences = ed.displayed_cheapest_sentences(Facts)
    assert sentences[1] == ("API basis, noise-margin companion (O44; each bar plus 4.5 quality points, so the bar's own configuration cannot decide it): "
                            "cheapest at or above quality 54.5: b ($20.00 per basket run); at or above quality 74.5: none.")
    assert sentences[-2].endswith("at API quality 50.0.") and sentences[-1].endswith("(O43): Listed X.")
    assert ed.basket_runs_text({"amountUsd": 1178.0, "feePeriod": "month"}, 9373.65) == "0.13 per month"
    assert ed.basket_runs_text(None, 10.0) == ed.basket_runs_text({"amountUsd": None}, 10.0) == ed.basket_runs_text({"amountUsd": 5.0}, None) == "—"


def test_cross_harness_text_lists_or_says_none():
    """E224: the Bug Hunt cross-harness sentence."""

    class Facts:
        names = {"g": "Gemini"}
        scores = {"models": [{"id": "g", "rankingEligible": True, "bugHuntCrossHarness": [{"harness": "A CLI", "fixedOf105": 40.7, "runs": 3}, {"harness": "B CLI", "fixedOf105": 33.0, "runs": 1}]},
                             {"id": "h", "rankingEligible": False, "bugHuntCrossHarness": [{"harness": "A", "fixedOf105": 1.0, "runs": 1}]}]}

    assert ed.cross_harness_text(Facts) == "Cross-harness results at the same effort (E224, diagnostic): Gemini: A CLI 40.7 (3 runs), B CLI 33.0 (1 run)."
    Facts.scores = {"models": []}
    assert ed.cross_harness_text(Facts).startswith("No ranked configuration has Bug Hunt results on two harnesses")


def test_selected_agents_text_counts_in_registered_order():
    """E225: cohort rows per selected Terminal-Bench agent."""

    class Facts:
        scores = {"models": [{"id": "claude-opus-5-5", "aaVariant": "max", "rankingEligible": True},
                             {"id": "gpt-6-astra", "aaVariant": "max", "rankingEligible": True},
                             {"id": "glm-5.3", "aaVariant": "max", "rankingEligible": False}]}

    rows = [{"model": "Opus 5.5 (max)", "agent": "Claude Code"}, {"model": "GPT-6 Astra (max)", "agent": "Codex"}]
    assert ed.selected_agents_text(Facts, {"rows": rows}).endswith("(E225): Claude Code 1, Codex 1.")
    assert ed.selected_agents_text(Facts, {"rows": []}).endswith("(E225): none.")


def test_common_leaf_and_harness_texts():
    """E226/E227 diagnostic sentences."""

    class Facts:
        label = staticmethod(lambda row_id: row_id.upper())
        labels = staticmethod(lambda row_ids: ", ".join(row_id.upper() for row_id in row_ids))
        tb4 = {"rows": [{"model": "Opus 5.5 (max)", "agent": "Claude Code"}]}
        # O37: the Terminal-Bench leaf's agent is its provenance (AA's own run), not tbench.ai's row.
        v3 = {"rows": [{"id": "claude-opus-5-5", "quality": {"leaves": {"terminalBench": {"agent": "mini-SWE-agent"}}}}, {"id": "x", "quality": {"leaves": {}}}]}
        scores = {"models": [{"id": "claude-opus-5-5", "aaVariant": "max", "rankingEligible": True, "bugHunt": {"matched": True, "harness": "Claude Code"}},
                             {"id": "x", "rankingEligible": True, "bugHunt": {"matched": False, "harness": "Codex CLI"}},
                             {"id": "y", "rankingEligible": False}]}

    diagnostic = {"sparseLeaves": ["frontierCode"], "barReach": [{"level": 56.7, "displayedReachN": 18, "commonLeafReachN": 20}],
                  "bases": {basis: {"rankChanges": {"changes": {"a": 2, "b": -2}}} for basis in ("api", "plan")},
                  "rows": {"a": {"effect": -5.04}}, "flagged": ["a"]}
    text = ed.common_leaf_text(diagnostic, Facts)
    assert "(FrontierCode 1.1), API 2 rows move; largest move 2 (A, B)" in text and "quality 56.7: 18 → 20" in text and text.endswith("A -5.0.")
    assert ed.common_leaf_text({**diagnostic, "sparseLeaves": [], "flagged": []}, Facts).endswith("one cost doubling's worth: none.")
    assert ed.harness_by_leaf_text(Facts) == "- **Harness by leaf (E227):** Terminal-Bench: mini-SWE-agent 1; Bug Hunt: Claude Code 1."
    Facts.scores = {"models": []}
    assert ed.harness_by_leaf_text(Facts).endswith("Bug Hunt: none.")


def test_gap_fill_and_incomplete_texts_without_rows():
    """E234/O36: with no gap fill and no listed configuration the sentences say so or are omitted."""

    class Facts:
        v3 = {"incompleteEvidence": []}
        scores = {"models": []}

    assert ed.gap_fill_text({"rows": {}, "bases": {}}, Facts).endswith("no ranked row has a leaf from another party or the provider.")
    assert ed.incomplete_text(Facts) == ""
    Facts.v3 = {"incompleteEvidence": [{"id": "x", "name": "X", "missing": ["bugHunt"]}]}
    Facts.scores = {"models": [{"id": "x", "rankingInclusionReasons": ["Required AA Intelligence Index versus total-evaluation-cost frontier family"]}]}
    assert ed.incomplete_text(Facts).endswith("(O36, O38): X (an AA frontier family; no Bug Hunt Bench).")


def test_gap_fill_bars_text_says_whether_each_bar_survives():
    """E234: the displayed-record cheapest row with fills as published, removed and lowered by the offset."""

    class Facts:
        labels = staticmethod(lambda row_ids: ", ".join(row_ids))

    same = {"level": 55.3, "published": ["a"], "removed": ["a"], "lowered": ["a"], "survives": True}
    flip = {"level": 59.6, "published": ["a"], "removed": [], "lowered": ["b"], "survives": False}
    text = ed.gap_fill_bars_text({"meanOffset": 2.53, "bases": {"api": [same], "plan": [flip]}}, Facts)
    assert "lowered by the mean offset 2.5 points" in text and "API quality 55.3: a in all three" in text
    assert text.endswith("Plan quality 59.6: a as published, none with the fills removed, b with third-party fills lowered by the offset.")
    assert "no measured offset" in ed.gap_fill_bars_text({"meanOffset": None, "bases": {"api": [], "plan": []}}, Facts)


def test_band_and_listed_indicative_texts():
    """O42 bands print as a rank range (or one rank); O41's table is omitted when nothing is listed."""

    class Facts:
        # O48: a configuration's Plan band is its own plan row's; I28: a band resting on a transfer is marked.
        v3 = {"listedIndicative": [], "rows": [{"id": "x", "planRowId": "x@pro"}],
              "diagnostics": {"rankSeparability": {"plan": {"bands": {"x@pro": [3, 3], "y@pro": [2, 4]}}, "api": {"bands": {"x": [1, 4]}},
                                                   "planAssumedRouteRows": ["y@pro"]}}}

    assert ed.listed_indicative_text(Facts) == ""
    assert ed.band_text(Facts, "x") == "3 / 1–4" and ed.band_text(Facts, "y") == "— / —"
    assert ed.band_text(Facts, "y@pro") == "2–4† / —"


def test_open_web_plan_row_and_costed_ladder_texts():
    """E240's discovery step, O48's plan-row table and I28's ladder sensitivity."""

    assert ed.open_web_text(None) == "—"
    step = {"searchedOn": "2026-10-23", "queries": ["q1", "q2"], "candidates": [{"resolution": "reject"}, {"resolution": "register"}]}
    assert ed.open_web_text(step) == "2026-10-23: 2 queries, 2 candidates (1 registered, 1 rejected)"

    class Facts:
        v3 = {"planRows": [
            {"id": "x@pro", "configurationId": "x", "plan": "Pro", "multiple": 2.5, "costUsd": 4.0, "value": 61.0, "quality": 70.0, "grade": "controlled", "rank": 1},
            {"id": "y@api", "configurationId": "y", "plan": None, "multiple": None, "costUsd": 9.0, "value": 50.0, "quality": 60.0, "grade": None, "rank": 2},
            {"id": "z@api", "configurationId": "z", "plan": None, "multiple": None, "costUsd": None, "value": None, "quality": 60.0, "grade": None, "rank": None},
        ], "diagnostics": {"rankSeparability": {"plan": {"bands": {"x@pro": [1, 2]}}, "planAssumedRouteRows": ["x@pro"]}}}

        @staticmethod
        def label(model_id):
            return model_id.upper()

    table = ed.plan_rows_table(Facts)
    assert "| 1 | X | Pro | 2.5× | $4.00 | 61.0 | 70.0 | controlled | 1–2† |" in table
    assert "| 2 | Y | API-cost fallback (no admitted plan) | — | $9.00 | 50.0 | 60.0 | fallback | — |" in table and "| Z |" not in table

    class Labels:
        @staticmethod
        def labels(ids):
            return ", ".join(ids)

    assert ed.costed_ladder_text({"excluded": [], "population": 3, "levels": []}, Labels).endswith("the ladder is unchanged.")
    assert ed.costed_ladder_text({"excluded": ["w"], "population": 2, "levels": [50.0, 40.0, 60.0]}, Labels).endswith(
        "(w); without them (2 rows) the ladder (headline, lower quartile, upper quartile) would be 50.0 / 40.0 / 60.0.")
    assert "would be unavailable" in ed.costed_ladder_text({"excluded": ["w"], "population": 1, "levels": []}, Labels)


def test_influence_text_explains_a_negative_cost_allocation_and_workload_dash():
    """E196: a negative covariance allocation means cost offsets quality; a row without a cost has no workload."""

    def v3(api, plan):
        return {"costInfluence": {basis: {"commonWorkload": {"varianceAllocation": {"cost": share}}} for basis, share in (("api", api), ("plan", plan))}}

    negative = ed.influence_text(v3(-0.12, 0.3))
    assert "covariance allocation of value variance is -12% on the API basis and 30% on the Plan basis" in negative
    assert "cost accounts for 40% of the variance in API value and 30% in Plan value" in ed.influence_text(v3(0.4, 0.3))
    assert ed.workload_text({"cost": {"apiUsd": None}}) == ed.DASH
