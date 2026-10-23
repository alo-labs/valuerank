# Internal review I25 — Claude Sonnet 5.5 (effort low) on draft r84

## 0. Read check
First line: "# ValueRank methodology — draft r84". Last 12 words of the last line: "remain pending until complete exact-variant cost evidence covers two-thirds of cohort rows jointly with the admitted components (E95, E101)." (The reviewer first quoted 7 words and corrected itself.)
(All 1039 lines read in four chunks; ledger-brief.md in full; the ledger's O36–O38 section and I20–I24 reviews, the rest grepped; AGENTS.md and the relevant parts of value_v3.py and frontier.py. No web search. Arithmetic and fixtures verified by hand and with a short simulation: ladder positions, quality bounds [42, 72], Omniscience vectors, the 91.5% / 86.7% kernel fixture, the Clopper–Pearson δ, the E88, E43 and E50 fixtures, the lifecycle dates and the exchange-rate formula.)

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. S1M is described as active in three places (the Measurement layer bullet: "Active v1 streams quantify reporting precision in S0 and conventional Terminal-Bench CI-range sensitivity in S1M"; the E155 descriptions: S1M is "S1 plus conventional range sensitivity inside Terminal-Bench's published 95% confidence interval"; Outputs: "published beside S1"), while E236 marks it dormant: since O37 the Terminal-Bench leaf is AA's own run, which has no interval, so S1M widens only a tbench.ai gap fill and today equals S1. E155 prints these descriptions beside every uncertainty output, telling readers a published confidence interval enters the shares when none does; the release-text lint cannot catch it because the stream is nominally registered. Make every generated description conditional ("S1M: dormant (no leaf is a tbench.ai gap fill); equals S1") and say in the Measurement layer bullet that no confidence interval enters any v1 stream today.

M2. The bar results gap fills can change are not tested (E234; Cohort). Eight FrontierCode leaves come from Cognition, which reads 2.5 points higher on average and 11.8 at most, and keep label eligibility; the removal sensitivity reports value-rank changes only (`gap_fill_sensitivity` returns rankChanges only). The headline "GPT-6.1 Sol (medium) confirmed cheapest" rests on a row whose FrontierCode is a Cognition fill (quality 58.54 against H = 55.31; the 3.2-point margin exceeds the 1.2-point worst-case leaf effect today, but nothing checks this in general, and the bar is a threshold where the offset matters). Extend E234 to the bar outputs on both bases: for every row that qualifies or is cheapest only because of a fill, publish whether qualification and the cheapest label survive (a) removal of the filled leaves with renormalisation and (b) the filled leaf lowered by the measured offset; sensitivity only.

M3. Revisions of the owner-selected SemiAnalysis article are not covered (E238; line 356: where SemiAnalysis publishes a per-(plan, model) measurement it replaces the transfer). If the same URL is edited in place (e.g. adding a model's multiples), one implementation reads the new numbers and another holds to the 2026-10-06 capture; the E194 date would hide the edit. Pin the selected analysis by URL plus content hash; a changed hash at the selected URL is a scoped change-detection trigger; its new per-model measurements stay diagnostic until the owner re-selects, and the clock then runs from the revision date.

**Low**

L1. "Cost ratio to the frontier" (required by AGENTS.md; the draft says each near point "publishes its cost ratio to the frontier for information only") is never defined; the code (frontier.py) uses the point's cost divided by the cheapest frontier cost that reaches the point's Index. Add the formula and say whether rounded or unrounded Index is used.

L2. "Both are diagnostics and change no score" in the Comparability record (E237) follows the description of scored fills; say "the comparability records are diagnostics".

L3. The harness-stress band is "unevaluable while each configuration has one agent", but it is estimated from same-model cross-agent spreads on tbench.ai, which exist for many non-cohort models; this leaves DeepSWE (30%) and Bug Hunt (10%) with no harness-stress result although vendor harnesses differ across rows. Let the band use any tbench.ai model with two or more agents, as stress only, never in Θ.

## 2. Methodology design recommendations
1. Fix M1–M3 first (text and registry changes).
2. A rank-resolution diagnostic (re-raising the rejected binomial idea): O25 says only that run-to-run noise "appears only in scenario shares"; the ban is the editor decision E155, not the owner. A plug-in binomial standard error from published task counts (DeepSWE 113, FrontierCode 100, Terminal-Bench 66, Omniscience 6,000, …) is parameter-free and routine; a named, non-authorising stream labelled an independent-task approximation (conservative, since models share tasks), printed beside the ranks as "ranks within X value points are not separable".
3. Generalise E235: index every rule dormant or vacuous today (Plan interval machinery, S1M, the harness stress branch, the kernel-check design beyond singletons) as one manifest entry each; more than half the normative text is now unexercised.

## 3. Questions for the owner
1. Should a re-publication of the selected SemiAnalysis article at the same URL (M3) re-trigger the 2026-10-07 selection, or count only when you re-select it?
2. Do you accept a non-authorising task-sampling stream (recommendation 2) as consistent with O25?

## 4. Verdict
VERDICT: HAS FEEDBACK
