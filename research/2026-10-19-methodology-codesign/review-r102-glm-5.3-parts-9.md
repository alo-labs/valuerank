0. Read check

Part 9 — read to its end.

First line: "Scoring with frozen, per-basis anchors in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); anchor object (E20), identified by anchor version, basis and workload hash…"

Final sentence: "Code Migration v1.1 (Vals AI; code porting graded by hidden tests, 130 tasks; Pi agent harness for every model) | 6% | — | — | hidden-test pass rate (%), anchors 0–100; Vals' standard error recorded |"

Part 10 — read to its end.

First line: "| | LiveBench 2.0 Overall (release 2026-10-25, owner decisions O67 and O139; LiveBench's weighted mean of its seven categories, Long Agentic, Reasoning, Coding, Browser, Data Analysis, Research and Design, all needed in the SDLC; … | 15% | — | — | the release's weighted mean of the seven category scores to two decimals (its _overall_weights: Long Agentic 2, Coding 1.5, Design 1.5, the others 1), as LiveBench's site computes it, anchors 0–100 |"

Final sentence: "Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias."

Both parts were read in full; the review below covers only what they state.

1. Findings by severity

Critical

None.

High

The Bug Hunt match key's version-number tolerance can admit a different release as exact-variant evidence (E206). The rule states that "a scoreboard name may add only a version number," so "Muse Wonder 1.0" matches "Muse Wonder." As written, this also makes "Model X 2.0" match "Model X" — a new release of the same family, not an alias. This sits in direct tension with the fixed exact-variant policy, which the draft itself applies strictly elsewhere (Vals' "DeepSeek V4.1 Flash of 2026-09-10 is a different release from DeepSeek V4.1 Flash 1017 and is never mapped to it"), and with the largest-sample rule, which would silently switch a ranked row's record to the newer version's results whenever it posts a larger N. A mis-attributed run on an 8–15%-of-quality leaf moves ~1 value point, and it would do so with no build stop, because the build only stops on equal-N ties, not on version mismatches. Change: restrict the tolerance to a registered alias list (each pair carrying evidence that both names denote the same release — provider documentation or the board's own notes), and stop the build on any version-suffixed scoreboard name whose base name matches a roster model but is not on the alias list, mirroring E225's closed-list treatment of Terminal-Bench agents.

Medium

The common-leaf ranking's software-engineering weights do not match the decision that O121 cites for them. O121 defines the diagnostic as "the ten shared leaves at O55 weights," but the table's common-leaf column shows FrontierCode 25 / Terminal-Bench 20 / Bug Hunt 15, which is exactly O49's ten-leaf weighting — not O55's, whose per-ranking SE weights were 18/14/10 (max-effort, pre-O61), 15/11/8 (O61) or 21/17/12 (AI Coding Daily), none of which renormalises to 25/20/15. The common-leaf ranking's bar answers are printed beside the leading rankings' (O121), so its published output rests on weights whose derivation no reader can reconstruct from the stated rule. Change: state the derivation in the leaf table (e.g., "common-leaf SE weights = O49's ten-leaf weights"), or correct whichever of the table or the O121 reference is wrong.

The E304 freeze-stop path leaves stale anchors in force with no published staleness signal or remedy. When a re-freeze stops for lack of two measured Plan references, "the previous anchor objects stay in force for both bases," so a new cohort is scored on anchors frozen over an older cohort. The clip gate catches egregious mismatch, but moderate staleness passes silently, and if the gate then holds, its named remedy — the O12 versioned re-freeze — is exactly the operation that just failed, creating a potential hold loop until the staged plan-allowance research (O164, monthly per cell) produces a second measured row. Change: publish an anchor-staleness status whenever the freeze stops (anchor version in force, its freeze date, count of current ranked rows not in its reference cohort, e.g., anchors.staleSince in scores.json), and escalate to a named owner decision after, say, two consecutive stopped freezes.

Cross-source disagreement on Terminal-Bench gap fills is diagnostic-only, with no action threshold and panels too small to inform it. E229 reports τ_b 0.74 with a +1.7-point offset on just 5 common rows in the max-effort ranking and "undefined (panel too small)" on 1 row in the other ranking; the agent-preference order puts Terminus 2 ahead of AA's own mini-SWE-agent harness. A harness-mixed row carries the offset directly into an 11–20%-of-quality leaf with only a flag. (Today no row is harness-mixed, so this is cheap to fix before it fires.) Change: pre-register a per-row sensitivity for harness-mixed rows (rescore with the measured tbench.ai-minus-AA mean offset removed, publish the rank delta), and print τ_b only above a minimum common panel (e.g., 8 rows), otherwise "insufficient panel," so a small-panel τ_b is never read as evidence of agreement.

Low

The cost-score formula's domain excludes zero-cost rows without saying what happens to them. S_C uses ln c, and the gate population G requires a positive cost, but the part never states how a zero-cost row (a free tier in force) is scored. If E149's cost-boundary rule governs this, cite it where the formula is; otherwise define it (e.g., S_C = 100 at c = 0, flagged) so a free plan entering the cohort cannot produce an undefined score.

The anchor-object hash identifies less than it claims to. The hash "covers the workload's component set only," so two rankings' workloads share a hash while being different anchor objects — the composite key (version, basis, hash) does the identifying, and an equal hash implies "no comparability across rankings." Change: include a digest of the reference set (configuration ids and frozen costs) in the hash so the hash alone identifies the object and cross-ranking hash collisions are self-describing.

E268's recency fallback picks a harness arbitrarily. When no AI Coding Daily row matches the Bug Hunt harness, "the row with the latest test date among … all rows" is taken — recency decides which harness represents the configuration, with no documented relation to the row's other evidence. Change: prefer a registered default-harness order (as the Terminal-Bench agent preference does) over recency, or stop for owner adjudication.

AI Coding Daily provenance should record the judging method. Unlike LiveBench, whose design uses prepackaged answers judged without an external AI system, AI Coding Daily is "judged code quality" with no statement in this part of who or what judges. Recording the judge/method per row in the registry (alongside the harness already recorded) keeps a 10% leaf auditable if the board changes its judging process.
siliconangle

Checks that passed and are worth noting positively: the retired Omniscience formula's non-monotonicity arithmetic (98/1/1 → 82 vs 99/1/0 → 66) is correct, and z = (I + 100)/2 is monotone; E311's variance bound p̃(1−p̃)/n as the maximum for a mean of n independent scores in is correct (Bhatia–Davis); the LiveBench SD formula and its √2 halved-counts bracket are algebraically right; O122's coding-specific share recomputes to 51% exactly as printed; O170's fixture (109.6/122.3 ≈ 89.6) checks out; and the E181 sensitivity's 400-points-per-tenfold-odds scale is the standard Elo logistic convention, so using it as a labelled assumption while AA states none is sound.
0

2. Methodology design recommendations

Prioritised, all implementable from public data and routine refreshes:

Registered alias list for Bug Hunt (implements Finding 1). A versioned table in the evidence bundle: (scoreboard name, roster name, evidence link). Build rule: exact match → alias-list match → stop. This preserves E206's intent (boards add cosmetic version labels) while closing the release-boundary hole, and it is the same pattern already proven by E225's closed agent list.

Anchor-staleness publication (implements Finding 3). On every freeze that stops under E304, emit anchors.status = "in-force-not-refrozen", anchors.frozenAt, and the share of current ranked rows outside the reference cohort; after two consecutive stopped freezes, surface it in the release record beside releaseHold so the O12-hold loop is visible rather than implicit.

Harness-mixed sensitivity for Terminal-Bench (implements Finding 4). For each harness-mixed row, publish S_Q and rank with the leaf rescored as (tbench.ai value − mean cross-source offset), plus the common-panel size; gate the printed τ_b on a minimum panel of 8. Zero cost while no rows are harness-mixed, and it becomes a ready-made E234-style removal sensitivity the moment one appears.

State the zero-cost rule at the formula. One sentence next to S_C: domain c > 0; a row with cost 0 (free tier in force) takes S_C = 100 with a flag, or is governed by the cited cost-boundary rule. Prevents an undefined score the first time a free plan enters a scored Plan row.

Self-describing anchor hash (implements Finding 6). Hash = H(component set ‖ sorted reference configuration ids ‖ frozen reference costs). Equal hashes then do imply identical anchor objects, and the current "equal hashes imply no comparability" caveat disappears.

Common-leaf derivation note (implements Finding 2). A one-line footnote in the leaf table naming the governing decision for the 25/20/15 SE weights, so the diagnostic ranking's printed bar answers are traceable.

3. Questions for the owner

Is there (or should there be) a registered alias list behind E206's version-number tolerance, and if not, do you want unmatched version-suffixed scoreboard names to stop the build rather than match silently? This determines whether Finding 1's fix is a new registry or a build-rule change.

Does an existing rule (E149's cost boundary?) define S_C for a row whose cost is exactly zero, and if so, should it be cited beside the S_C formula?

For O121's common-leaf ranking, do the 25/20/15 software-engineering weights derive from O49's ten-leaf set rather than O55 — and if the table is right, may the O121 citation be corrected (or vice versa)?

If a re-freeze stops under E304 and the clip gate subsequently holds a release, what is the intended published remedy while the O12 re-freeze remains unavailable for lack of a second measured Plan reference?

4. Verdict

VERDICT: HAS FEEDBACK