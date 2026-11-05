Both parts are read in full. Before writing the review, I'll run a few targeted web checks on factual claims these parts make about external benchmarks (LiveBench 2.0 weighting, GDPval-AA's Elo methodology, and the Vals/AI Coding Daily harness claims).
0. Read check

Both listed parts were opened through the GitHub connector and read to their end.

Part 7 (draft-r160-part-7-of-14.md) — first line: "- Scoring with frozen, per-basis anchors in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); anchor object (E20), identified by anchor version, basis and workload hash …" (the line continues; it opens the cost-scoring block and ends the file at the leaf table). Last 12 words: "no value for 10 of 19 cohort rows in the 2026-10-17 snapshot".

Part 8 (draft-r160-part-8-of-14.md) — first line: "- GDPval temporal estimand (E90, owner decision O70, 2026-10-25): the leaf is the GDPval-AA v2.1 Elo that AA's model page displays at the release's capture, the leaderboard value, which AA refits as models join …". Last 12 words: "a bias bound in the identification layer); repetitions are not a bias".

1. Findings by severity

Critical

None.

High

The claim "Cognition does not run FrontierCode 2.0" looks stale. The draft uses this to justify why Cognition's board "no longer fills" the FrontierCode leaf and why no cross-check exists for the 2.0 era. External reporting dated 2026-10-30 says Cognition reported FrontierCode 2.0 results — Gemini 4 Carbon at 40% and $4.04 per task, behind Claude Opus 5.5, GPT-6 Astra and Claude Sonnet 5.5 — and FrontierCode 2.0 is Cognition's own 132-task benchmark, co-launched with AA's Index v5. Why it hurts: FrontierCode 2.0 carries 15% (max-effort) and 21% (AI Coding Daily) of quality, and a wrong premise here can (a) leave a configuration listed rather than ranked under O36's logged-search path when usable public evidence exists, and (b) silently drop the E234-style AA-vs-Cognition cross-check that existed for 1.1 (τ_b 0.73). Recommended change: re-verify Cognition's board at every refresh (it is already re-read under O68's board sweep); if 2.0 rows exist, register Cognition as the FrontierCode 2.0 gap-fill/cross-check source under the same discipline as Terminal-Bench's tbench.ai fill (exact model+effort, one row per agent, registered order, never best-of) and publish the E229-style τ_b and mean offset for 2.0. This is not a repeat of E234: the new argument is the 2026-10-30 report contradicting the stated premise.
heise
+2

Plan-basis anchor panels include API fallbacks and owner-assumed transfers, compressing Plan cost scores. E160 freezes Plan anchors over "every plan row" of the reference configurations — measured routes, assumptions and API-cost fallbacks alike — with c_H = dearest reference × 2. When the dearest references are API fallbacks (typically an order of magnitude above plan prices), the log anchor range widens and all measured plan rows compress into a narrow cost-score band, attenuating the 25% cost term so the Plan value ranking drifts toward a quality ranking. This hurts the objective (Plan buyers ranked separately on value, O1/O3) even though the choice is disclosed via E164's calibration. Recommended change: (a) every release, publish the Plan anchor pair and the Plan-basis cost-score dispersion under both the full panel and a measured-only panel, plus the τ_b of Plan value scores between them (same shape as E288); (b) as an editor change to E160/E253 with an owner sign-off — score all Plan rows on measured-only anchors and remove non-measured rows from the clip-gate population n. The draft's stated reason for the wide panel ("a narrower panel would clip them") dissolves once the gate population is restricted, because the O118-style treatment (fallbacks compete as blockers, never earn labels) already covers their competitive role. Rows stay scored and flagged in the table, so O13/O16 are respected.

Medium

LiveBench 2.0 Overall's SD is computed on 2026-10-14 task counts kept for releases that publish none. Category task counts are extremely uneven (Long Agentic 18, Reasoning 202, Coding 29, Browser 25, Data Analysis 150, Research 22, Design 25 in the first release), so a composition change in the read release would materially distort the SD, and Long Agentic's n = 18 already dominates the variance. The formula itself is correct for a weighted binomial mean, and LiveBench's own Overall weights (Long Agentic 2×, Coding 1.5×, Design 1.5×, rest 1×) match what the draft uses. Recommended change: publish the SD as a bracket — the current value plus a conservative variant (e.g., each category's n at half its 2026-10-14 value, or the smallest published count where unknown) — labelled as an assumption in S1T, and keep the build stop on weight changes only. Sensitivity-only, implementable from captured data.
livebench
+3

Bug Hunt's harness is chosen by largest-N and can switch between releases, but the impact of the choice is never quantified. E206 and E224 publish per-harness means, yet nothing bounds how much the leaf (8–15% of quality) moves when the record's harness changes. Since the estimand is "model plus harness" and vendor CLIs differ, cross-model comparability silently embeds harness quality. Recommended change: a labelled sensitivity that recomputes affected rows' Bug Hunt leaf at the cross-harness minimum and maximum and publishes the largest resulting value-point and adjacent-rank movement, so the disclosed limitation becomes a measured one. (This is not the rejected "within-family sibling evidence diagnostic"; it uses the same model's already-published runs.)

Low

E229's cross-source agreement is underpowered as published. τ_b 0.74 with offset +1.7 on 5 rows, undefined on 1, is close to uninformative. Recommended change: pool the matched AA/tbench.ai panels across the last k releases from the evidence-bundle captures, print the pooled τ_b beside the per-release value, and state the minimum detectable offset at the current panel size.

The anchor-object hash covers only the component set, so equal hashes across rankings denote non-comparable objects. That is stated, but any consumer joining scores.json on the hash alone would merge distinct anchor objects. Recommended change: fold the ranking id and basis into the hash string (or rename the field to workloadComponentHash) so a misjoin is structurally impossible.

Attempts reconciliation is asserted but not instantiated in these parts. The section names the manifest fields and the "bias bound" but gives no arithmetic or example (for instance, a tbench.ai gap-fill row whose attempt budget differs from AA's run). Recommended change: add one worked example of the bound's computation, and record FrontierCode 2.0's three-runs-per-task execution policy in the per-leaf attempt manifest — the draft states repetitions "affect precision only", but the 2.0 run count appears nowhere in the leaf table or the manifest description.
techtimes
+1

One point checked and found sound, not a finding: the GDPval temporal-estimand paragraph (E90/O70) is corroborated externally — AA freezes a model's GDPval-AA Elo at addition for its Index contribution under the clamp((Elo − 500)/2000) transform the draft reuses, while third-party Elo leaderboards are relative and shift as models join, and GDPval-AA derives Elo from blind pairwise comparisons. The leaf rule, the movement diagnostic and the observed 0-of-27 movement are consistent with that evidence.
artificialanalysis
+2

2. Methodology design recommendations

Prioritised, all implementable from routinely refreshable public data:

Measured-only Plan anchor duality (addresses the High finding). Keep one Plan anchor object per ranking frozen over measured reference rows only (E170 outcome 1–2 rows with complete cost evidence); score fallback and assumed-transfer rows on those anchors, flag them, and exclude them from the clip-gate population. Publish, per release: both anchor pairs, the Plan-basis cost-score SD under each, and the τ_b of Plan value scores under each. Existing fixture set extends naturally (a fallback row beyond the measured anchors is disclosed like O58's listed rows).

Register Cognition as a FrontierCode 2.0 source. Extend the O37-style priority chain (AA's run, then Cognition's 2.0 board at exact model+effort, one row per agent, registered order) and add an E229-style agreement diagnostic (τ_b plus mean offset, panel size printed). Cross-checks AA's private-benchmark run — 60% of AA's v5 index weight is now private tests, which raises the value of any independent second execution.
ai-tldr

Bracket the LiveBench SD as described in Medium: SD_low from kept 2026-10-14 counts, SD_high from a conservative count assumption, both labelled, entering S1T only.

Bug Hunt harness sensitivity: cross-harness min/max leaf recomputation with published value-point and rank deltas, alongside E224's per-harness means.

Pool agreement diagnostics across releases (E229, E288): a rolling panel built from the evidence bundle's pinned captures, so power grows with each refresh instead of resetting.

3. Questions for the owner

Does your Cognition board capture (re-read under O68) show FrontierCode 2.0 rows, as the 2026-10-30 reporting of Cognition-published 2.0 scores suggests ? If yes, do you want Cognition registered as the 2.0 gap-fill/cross-check, or is AA-exclusivity intended for the v5 leaf?
digg

Would you accept restricting the Plan clip-gate population to measured rows so Plan anchors can be frozen on measured routes only, with fallbacks scored on those anchors and flagged (an amendment to E160/E253, since O48's one-row-per-plan rule is untouched)?

Should the LiveBench S1T SD be published as a bracket whenever the read release publishes no task counts, or do you prefer the single kept-counts figure as it stands?

4. Verdict

VERDICT: HAS FEEDBACK