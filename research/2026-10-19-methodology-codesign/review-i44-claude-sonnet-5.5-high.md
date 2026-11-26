# Internal review I44 — Claude Sonnet 5.5 (effort high) on draft r102

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r102"
- Last line of the draft (folded line 953): "LiveBench 2.0 Overall ties FrontierCode (owner clarification of O61), and states the O61 bar re-freeze. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "bar re-freeze. Every change is recorded with its rationale in the ledger."
- Also read: the whole folded draft (lines 1–953, in chunks); `reviewer-prompt.md`; `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (O45–O62, E247–E265, I28–I43); `AGENTS.md` at the repo root (the repository copy, which already carries O57–O62 and the LiveBench Overall wording); the source `draft-r102.src.md` for the placeholders.
- Checked against repository data and code: `data/scores.json` (both rankings' rows, `barPolicy.bars`, `barCurrency`, `displayedCheapest`, `diagnostics.familyPrimary`, `diagnostics.gapFillBars`, `measuredOnlyPlanView.calibration`, `sourceClocks`, per-row `cost` completeness and `indexReconciliation`, `valuationGate`), `data/aa_frontier_capture.json` (cohort recomputed from the 189 points: 18 frontier, 11 near, every gap, the first vertex GPT-6 Luna (low) at 10.63 equal to the cheapest plotted point), `data/v3_frozen.json` and `data/v3_frozen_aicd.json` (anchors and their references), `data/plan_cost_routes.json` (SemiAnalysis record, route classes, the one end-user report), `data/leaf_evidence.json` and `open-web-discovery-2026-10-23.json` (search log), `data/swe_tracks.json` (source metadata), `valuerank/quality.py` (leaf table), `valuerank/anchors.py` (clip gate, exchange rate), `valuerank/value_v3.py` (`freeze`, `check_leaf_searches`, `check_open_web`), `valuerank/draft_figures.py` (the lint), and `python3 -m valuerank.draft_figures check` (passes, no output).
- Verified as correct and not raised: leaf weights sum to 100 in both rankings (max-effort 15 + 11 + 8 + 5 + 6 + 15 = 60, Coding Daily 21 + 17 + 12 + 10 = 60, the other 40 unchanged), 13 and 11 leaves, the 66/34 and 78/22 source shares and the 34% and 22% leave-AA-out weights, the 86.7% basket-scope retention, the ladder positions and fixtures (n = 9, 15, 32) and the bar-reach counts (7, 5, 3 of 9 and 12, 8, 5 of 15), the exchange rate and its offset (25 ln 2 / ln(18,703.43 / 62.86) = 3.04; ÷ 0.75 = 4.06), the noise margin against the separability threshold (3.8 ÷ 0.75 relation), the admission arithmetic (⌈2·9/3⌉ = 6 and ⌈2·15/3⌉ = 10; 2⁸ − 1 = 255 and 2⁷ − 1 = 127 feasible subsets), the cohort and its 18 / 11 split, every near-gap figure and each family primary (GPT-5.6 Luna (low) and Gemini 4 Argon (high) at 1, GPT-6 Astra (xhigh) at 2, DeepSeek V4.1 Flash 1017 (max) and MiniMax-M3.1-Flash at 3), the nine excluded configurations (2 + 2 + 2 + 3), the 20 / 14 / 9 / 4 / 20-of-29 arithmetic, the Plan row counts (11 measured + 14 transfer or ceiling + 2 API fallback = 27), the Clopper–Pearson closed forms and δ = 0.05/16, the report-window arithmetic (31 dates) and the E212 age dates (2026-11-05, 2027-01-05, 2027-02-04), the O59/O60 source clocks (Vals 07:58:05Z and LiveBench and AI Coding Daily 07:58:31Z after the 06:26:23Z cutoff, all with an update date before 2026-10-23; tbench.ai captured before the cutoff), the gap-fill bar survival (all twelve bars survive), the "every ranked row compatible as captured" and "Index total reproduced" statements (every row's reconstruction matches AA's total to 1e-15), and the AICD Plan anchor setters named in the E249 sentence.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

None.

**Low**

**L1. A current-release sentence with hard-coded configuration names escapes the figure check (location: folded line 373–374, source line 61, the "AI Coding Daily ranking: Claude Haiku 5.5 (medium) on Claude Pro … and Gemini 4 Argon (high) on API-cost fallback" sentence).**
Issue: the sentence names the two rows that set the AI Coding Daily ranking's official Plan anchors (low: Claude Haiku 5.5 (medium) on Claude Pro, an owner-named transfer; high: Gemini 4 Argon (high), API-cost fallback). I checked it against `data/v3_frozen_aicd.json` (cheapest plan reference `claude-haiku-5-5-medium@claude-pro` at 0.779, dearest `gemini-4-argon@api` at 1,857.9) and `measuredOnlyPlanView.calibration.workloads[...].officialAnchorProvenance`, and it is correct today. It is, however, a current-release fact written by hand, with no placeholder, and the lint cannot see it: `draft_figures.lint` reads configuration names only in sentences that contain the word "today", and this sentence does not. That is a defect in the check, not in the placeholder resolution: E265 promises that every current-release figure is a placeholder, and the next re-freeze would leave this sentence stale without failing the build. The same gap holds for the other configuration-name sentences without "today" (source line 28, the 38 tie; source line 59, GPT-6 Astra (max)'s route move, which is historical and correct).
Change: resolve the setters from `officialAnchorProvenance` (a `{{fig:…}}` entry for each ranking, as the max-effort case already prints in scores.md), and extend the configuration-name lint from "today" sentences to every undated sentence outside the bold rule labels and fixtures, with a short allow-list for historical statements.

**L2. The Plan anchor references are described as configurations in two places and as plan rows in three (location: folded lines 381 and 385–386 against 370, 372–373 and E249).**
Issue: "on the Plan basis the same configurations at their displayed Plan cost" (anchor-panel policy) and "the Plan references are the same configurations at their displayed Plan cost" (the E184 migration sentence) read as one cost per configuration. O48/E245/E249 and the code (`value_v3.freeze`: "the Plan anchor references are the plan rows of the reference configurations") put every plan row of a reference configuration into the Plan anchor object (the max-effort main workload's Plan low reference is `gpt-6-luna@chatgpt-pro-500`, not Luna's representative row; the Plan references include `claude-haiku-5-5-max@claude-pro`, `…@claude-max-5x` and `…@claude-max-20x` together). The precedence rule resolves it (the later-numbered E245 governs E160), so no two faithful implementers are left in doubt after reading the whole draft, but a reader of E160 alone would build the anchors from representative rows, whose low end differs.
Change: say "the plan rows of those configurations at their displayed Plan cost" in both places.

**L3. The tie example at the rendered frontier lists two rows where three display 38 (location: folded line 73, source line 28).**
Issue: "Rounded tooltip values tie (GPT-6 Luna (max) and MiMo-V2.6-Flash both display 38)". Claude Haiku 5.5 (high) also displays 38 at 94.07 and is a rendered-frontier vertex (capture: 38 at 94.07, 38 at 109.55, 38 at 122.05), so "both" understates the tie that the sentence uses to justify never recomputing membership from rounded values. The statement is an illustration, not a rule, so nothing downstream changes.
Change: say "GPT-6 Luna (max), MiMo-V2.6-Flash and Claude Haiku 5.5 (high) all display 38", or generate the list from the capture.

**L4. The Bug Hunt record-selection bullet has a typographical slip and states one build check twice (location: folded lines 478–481, source line 89).**
Issue: "…so no implementation breaks the tie silently; At the 2026-10-23 refresh" (capital after a semicolon), and "The build checks every matched record against the pinned scoreboard … and fails on a record that is neither the largest-sample result nor carries a reason" is followed, after one more sentence, by "The build checks every matched record against this rule."
Change: start a new sentence at "At the 2026-10-23 refresh" and delete the closing duplicate.

**L5. "Every definition below is evaluated within one ranking" is wider than the Normative section (location: folded line 599).**
Issue: the first Normative bullet says every definition below is evaluated within one ranking, but the cohort rule (which is the AA cohort, shared by both rankings), the Omniscience counts and the harness-stress branch are not ranking-specific. A literal reading asks for a ranking-scoped cohort rule, which O51 does not have.
Change: "Every definition below that uses leaves, anchors, bars or cohort rows is evaluated within one ranking; the cohort rule and the Omniscience counts are common to both."

**L6. Internal review identifiers appear in the published specification (location: Output 1 "Rank separability", "Transfer tolerance" and "Noise band", Output 3, the gap-fill paragraph and the E238 paragraph: "I28", "I42 L2", "I42 L3", "I42 L4").**
Issue: readers of the published draft cannot resolve "I42 L4" or "I28 M2" without the ledger. The rule numbers (E, O) are defined in the ledger the draft points to; the review labels are not part of the rule set.
Change: replace each with the E or O number that adopted the point (E258 for the pair span, E254 for the Terminal-Bench panel) or drop it.

## 2. Methodology design recommendations

1. (Priority 1, implements L1.) Move the last hand-written current-release facts into the figures manifest: the Plan anchor setters per ranking, the tie list at the rendered frontier, and the "no ranked row is in this state" / "every ranked row … reproduces its total" statements. The last group is a boolean over `rows[*].valuationGate.outcome`, `rows[*].cost.partialComponents` and `indexReconciliation`; a `{{fig:…}}` that renders "no ranked row" or the list of exceptions makes those statements fail the check the day one row is not compatible as captured. Today five qualitative "every ranked row of both rankings …" claims (the Index-reconstruction sentence in Cost, the E203/E243 ladder sentence in Output 3, the O36 provisional-row sentence and the valuation-gate paragraph) are true (I verified each against the data) but unmarked.
2. (Priority 2.) Disclose when adjacent ladder rungs are closer than the quality noise margin. In the max-effort ranking the headline bar is 64.26 and the upper-quartile bar 65.00 (the one-row-per-family upper quartile is 64.29), 0.7 points apart against a margin of 3.8, so the two bars decide almost the same cheapest-row question and the "ladder of three" reads as two distinct levels. A one-line printed flag ("bars within the noise margin: 64.3 and 65.0") would tell a reader how many distinct claims the ladder makes. Informational only, no bar changes (O34, O44).
3. (Priority 3.) Print, beside the Plan anchors, how many of the references are owner-named transfers or API-cost fallbacks (today the low end of every Plan anchor object and the high end are such rows). E164 and E249 already identify the setters; a count over all references would show how much of the Plan exchange rate rests on assumption. Diagnostic only.

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: NO FURTHER FEEDBACK
