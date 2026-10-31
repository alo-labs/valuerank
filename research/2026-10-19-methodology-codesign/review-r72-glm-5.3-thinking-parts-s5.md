0. Read check

Part 5 (research/2026-10-19-methodology-codesign/perplexity/parts-r154/draft-r154-part-5-of-13.md, read in full to its end):

First line: "Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V], compared as UTC calendar dates (date(V) − 30 days ≤ d ≤ date(V), with a timestamped E194 date truncated to its UTC date; …"

Last 12 words: "no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

Part 6 (.../draft-r154-part-6-of-13.md, read in full to its end):

First line: "- Assumptions: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, …"

Last 12 words: "value; no epsilon is introduced. Domain validity is separate from evidence completeness."

Both parts were read to their end.

1. Findings by severity

Critical

None.

High

H1 — Part 5's report-lapse rules contradict owner decision O127. Part 5 states that a report admitted at an earlier release "no longer counts once it is outside the current window", that "each release rebuilds every report partition from in-window reports only, so a report-based route lapses to diagnostic without fresh reports", and carries fixtures to that effect (two concordant reports 41 days apart → older one leaves the partition → route diagnostic) . O127 (Round 12, 2026-10-29) says the opposite: "an admitted report pair keeps counting after the 30-day window and ages like a measurement." Since parts 5–6 otherwise reflect decisions dated through 2026-10-30 (O113, O115, E271, O125, O126), this block looks un-updated rather than intentionally scoped. Why it hurts the objective: the two texts give opposite answers to whether a Plan route based on a user-report pair survives between releases; whichever an implementer follows changes the Plan ranking's composition, and the published fixtures test the superseded rule. Recommended change: scope O32 to initial admission only (a pair is admitted only from in-window reports under the E270 profile), then hand the admitted pair to the E151/O13 clock per O127; rewrite the partition-rebuild sentence to "in-window reports plus admitted pairs"; replace the 41-days fixture with one where an admitted pair 41 days old keeps its route and merely ages a stage.

H2 — Owner decision challenge (O46/O125): the MiMo ceiling's direction is internally contradictory. The ceiling is computed with deliberately low rates — "for Pro its cache-hit rate and the lower of its two published rates" — yet each row is "flagged as the most the plan can give, the optimistic end of the multiple" . A number computed at the lowest published rate is a lower estimate of deliverable API value, not "the most"; and it is scored as the row's multiple while set-identified multiples are scored at their lower bound (E74, which the draft itself contrasts). A buyer comparing a MiMo Token Plan row with an E74-scored row cannot tell which end of the value range each represents. Recommended change: publish a two-sided ceiling 
[
credits
×
𝑟
low
÷
fee
,
 credits
×
𝑟
high
÷
fee
]
[credits×r
low
	​

÷fee, credits×r
high
	​

÷fee] from the two published rates (both already recorded per route, E261), score at the low end for consistency with E74, and label the interval's direction; the O62/O11 replacement rule is untouched. What is new: the O125 direction debate did not notice that the rate-selection rule already biases the number downward, so "the most" and "the lower rate" cannot both hold — this is an inconsistency inside the decision, not a re-litigation of it.

Medium

M1 — The O115 clip band names no report set. The concordance band 
[
largest lower
÷
1.20
,
 
1.20
×
smallest upper
]
[largest lower÷1.20, 1.20×smallest upper] is applied to the pooled value, but the draft never states whether "largest lower" and "smallest upper" are taken over all eligible reports of the current partition ("provisional ones included") or only over the non-provisional E33 pool whose midpoints are averaged . As written, a provisional report (e.g., an inferred model version) — which cannot be one of the two reports that admit a route — can move a scored route's multiple through the band. Recommended change: declare the band's report set explicitly (the same set as the range test is the natural choice), and add a fixture with a provisional outlier report showing its effect (or non-effect) on the pooled value.

M2 — Search-stage coverage and provenance are the weakest link in the O71 chain. The build environment cannot reach reddit.com (only archive mirrors), X, Zhihu, LINUX DO search, GitHub search, or YouTube pages, and the Silver Bullet stage ran degraded (no search-cli, one retriever) . Yet Reddit/X are the primary venues for end-user allowance reports, GitHub issues supplied the claude-code 102667 meter-change evidence, and archive mirrors are accepted with no freshness rule. Why it hurts: the O72 fallback (owner-authorised routes) then persists because the search could not see the evidence, not because it is absent — undermining the "recommendations implementable from public data refreshed routinely" constraint. Recommended change: add a mirror-provenance block to plan_reports.json (original URL, mirror URL, snapshot date), require snapshot dates inside the report window, flag degraded stage runs in the published summary, and add one out-of-band live verification per admitted report as a manual release step.

Low

L1 — Donor replacement is manual. E144 says a newer controlled measurement of the donor model "replaces the old donor only by being named" . Add a build diagnostic listing donor model/route pairs with a newer eligible measurement that has not been named; replacement stays editorial, but staleness becomes visible.

L2 — Midpoints are on the wrong scale. Range-valued reports pool on arithmetic midpoints while the concordance test is a ratio test (1.20×) . Use geometric midpoints 
𝑙
𝑜
⋅
ℎ
𝑖
lo⋅hi
	​

 for range reports before clipping, so the central estimate matches the multiplicative scale of the test.

L3 — Vacuous machinery is invisible. E54, E80, E105 and E124/E130 have no current yield (no admitted source provides burn evidence; 
𝑑
𝑖
𝐴
d
iA
	​

 is "today none") . Publish an E235-style manifest of currently-vacuous rules so readers can tell live machinery from forward structure.

L4 — The two end-user meter fits (Claude Max, Kimi's China-region tiers) are listed but "not yet evaluated" ; that evaluation is the only current path off the structural "workload-unmatched: exploratory" label. Schedule it explicitly each release until resolved.

2. Methodology design recommendations

Prioritised; all implementable from routinely refreshable public data:

Two-sided MiMo ceiling (fixes H2). For each tier: 
𝐿
=
credits
×
𝑟
min
⁡
÷
fee
L=credits×r
min
	​

÷fee, 
𝑈
=
credits
×
𝑟
max
⁡
÷
fee
U=credits×r
max
	​

÷fee, both rates already captured per route (E261); score at 
𝐿
L (E74-consistent), publish 
[
𝐿
,
𝑈
]
[L,U], flag direction. Build re-check extends naturally to both ends with the existing 0.0005 tolerance.

O127-aligned pair persistence (fixes H1). Admission gate: in-window, E270-eligible, ≥2 non-provisional observers, O86 concordance. Once admitted, the pair's route persists and ages under the E151/O13 clock; partitions rebuild from in-window reports plus admitted pairs; fixtures updated accordingly.

Declare the clip band and pool in log space (fixes M1, L2). Cell value 
=
exp
⁡
(
1
𝑛
∑
𝑖
ln
⁡
𝑚
~
𝑖
)
=exp(
n
1
	​

∑
i
	​

ln
m
~
i
	​

), with 
𝑚
~
𝑖
=
min
⁡
(
1.20
𝐴
,
max
⁡
(
𝐵
/
1.20
,
 
𝑚
𝑖
)
)
m
~
i
	​

=min(1.20A,max(B/1.20, m
i
	​

)), 
𝐴
A = smallest upper bound and 
𝐵
B = largest lower bound over the declared report set (recommend: the range-test set, provisional included).

Mirror provenance schema (fixes M2). Fields mirror_url, snapshot_date, original_url in plan_reports.json; build fails if a snapshot date falls outside the report window; degraded stage runs (no search-cli, unreachable venues) printed in the release summary.

Donor-staleness diagnostic (fixes L1). A build table of donors with newer eligible measurements not yet named, published with the transfer registry.

Vacuous-machinery manifest (fixes L3). One indexed entry per rule with zero current applicability, E235-style.

3. Questions for the owner

Does O127 fully supersede part 5's O32 rebuild text (admitted pairs persist and age under E151/O13), or does the in-window rebuild still govern and O127 mean something narrower? The answer decides whether H1's fix is a text rewrite or a rule amendment.

For the MiMo ceiling, is the published number intended as a lower estimate of deliverable value (then the "most the plan can give" flag is wrong) or an upper bound (then the low-rate selection is wrong)? The answer decides which end of the two-sided interval is scored.

4. Verdict

VERDICT: HAS FEEDBACK