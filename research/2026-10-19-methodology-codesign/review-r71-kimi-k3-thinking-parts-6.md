I'll start by locating the GitHub file-read tool.
Part 6 read in full. Now part 7.
Part 7 read in full. Now part 8.
Part 8 read in full. Now part 9.
0. Read check

All four listed parts were read to their end via the GitHub connector at commit 0ab322c5c47c55684a7a060e49d4b24e3130674f.

Part 6 — first line (opening, line continues): "- Assumptions: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, a transfer with its donor measurement identified; neither identifies M_W." Last 12 words: "best value; no epsilon is introduced. Domain validity is separate from evidence completeness."

Part 7 — first line (opening, line continues): "- Scoring with frozen, per-basis anchors in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); …" Last 12 words: "Daily on a harness chosen per model) are disclosed as a limitation."

Part 8 — first line (opening, line continues): "- Added leaves (owner decisions O53–O55; E252, E256, E257): their evidence is data/swe_tracks.json, built by research/2026-10-23-swe-benchmarks/build_swe_tracks.py from the verified coverage captures …" Last 12 words: "predictive run-to-run variation, and only interpretations the public evidence supports are published."

Part 9 — first line (opening, line continues): "Results are published per stratum (S0, S1, S2; transfers on/off; leave-AA-out), never averaged into one figure, as scenario shares …" Last 12 words: "with a displayed quality, ordered by displayed quality ascending, then configuration ID." (the bar-policy list runs into part 10, which is out of this pass's scope.)

1. Findings by severity

Critical: None.

High: None.

Medium:

Quota ceilings are scored at the optimistic end, against the draft's own conservative convention. A set-identified 
𝑀
𝑊
∈
[
𝐿
,
𝑈
]
M
W
	​

∈[L,U] enters the displayed score at its lower bound 
𝐿
L ("lower-capacity-bound scoring convention", E74), yet a MiMo O46 row displays the ceiling — the quota-implied upper bound — as its point multiple. Since real consumption can only meet or undershoot the ceiling, this systematically flatters MiMo rows against measured routes in the ordered Plan table. Why it hurts: ValueRank's objective is a defensible value ranking; direction-of-error consistency is exactly what makes label-free scored rows defensible. The tension with the fixed evidence policy ("no provider marketing quotas as numerator") is also only resolved by an inline exception sentence, not a graded status. Recommended change (Owner decision challenge — the new argument is the E74 direction inconsistency, not the authorisation itself): display MiMo Plan rows on the interval 
[
𝐶
𝑊
×
𝑓
fee
,
𝐶
𝑊
×
𝑓
ceiling
]
[C
W
	​

×f
fee
	​

,C
W
	​

×f
ceiling
	​

] or score them at a conservative end like every other uncertain numerator, keeping the labelled ceiling as the diagnostic; formalise the O46 exception as a registered grading kind in the E106 decision table so the "no marketing quotas" rule and O46 no longer read as contradictory texts.

O88 cross-effort transport is graded "measured evidence" unconditionally, but effort-invariance of a multiple only holds when the plan's meter is token- or credit-denominated. A burn-rate or message-quota measurement (SemiAnalysis-style figures bound by E246, user reports pooled across efforts by O87) measures API-valued consumption per unit cash at one effort; if the quota is denominated in messages or 5-hour windows, tokens per message differ by effort, so 
𝑀
observed
M
observed
	​

 at low effort does not equal 
𝑀
observed
M
observed
	​

 at max. Because O88 routes are admitted to the measured-only view (E113) and graded measured under O90, the "measured-only" view silently contains assumption-grade cross-effort transport for message-denominated meters. Owner decision challenge (O87/O88–O90; the new argument is conditioning validity on meter denomination, which the draft nowhere records). Recommended change: add a registry field quota_denomination (tokens / credits / messages / requests / time-window) per plan; classify O88 routes as measured only for token/credit meters and as a labelled donor-assumption (like the O45 lower-of transfer) otherwise. This is implementable from public plan documentation and refreshed on the normal capture cycle.

Same-execution quality and cost are drawn independently in the scenario engine. Since O37, the Terminal-Bench quality leaf and the priced Terminal-Bench basket component are AA's same run ("quality and cost read the same run"), and FrontierCode similarly underlies both an AA-run leaf and an AA-run cost execution. The uncertainty layers draw leaf values (S1T) and cost reporting precision (S0) independently unless paired public observations exist, and the drift toward same-run leaves increases the share of weight where this coupling is real but unmodelled: value-score noise bands and separability thresholds are computed as if the 11%–17% TB leaf and its cost component covary only by chance. Why it hurts: separability is printed beside the ranking as the credibility statistic (O39/O42); understated joint variation makes adjacent ranks look more separable than the evidence supports, and the sign is unknown ex ante. Recommended change: register a named coupling branch (e.g. S1T-paired) that jointly resamples, where AA publishes paired per-task cost and outcome data, the leaf share and the cost-per-task total at task-cluster level for same-execution components; where pairing is not published, print an explicit "quality–cost dependence unmodeled (same execution)" note beside the separability statistics. The workload cross-check section already joint-resamples paired task-level costs and outcomes for 
𝑑
𝑖
𝑏
d
ib
	​

, so the machinery exists.

Separability statistics count same-configuration plan rows as ordinary pairs (E258), while noise bands bundle them (E248). O48 creates one Plan row per configuration–plan; those rows share every scenario draw (one dependency group) and differ only in a deterministic displayed multiple, so they separate in ~100% of scenarios by construction. Counting such pairs apart (E258) mixes structurally separable pairs into the same statistic as evidentially separable pairs whenever adjacent Plan ranks are plans of one configuration — with 51 plan rows over 16 configurations in the AI Coding Daily ranking this is not rare — while E248 simultaneously treats them as one bundle for noise bands. Recommended change: report separability in two columns — restricted to distinct-configuration pairs (the evidentiary claim) and including same-configuration pairs (the table claim), with the restriction rule stated in E258 and the band rule unchanged.

Low:

E268 creates a cross-board cascade: the AI Coding Daily record is chosen by matching the harness of the configuration's Bug Hunt record, and E206's Bug Hunt record switches harness whenever a larger-
𝑁
N run appears on another CLI. A new Bug Hunt run can therefore change the AICD leaf with no new AICD evidence. Recommended change: when E268's match key's harness changes, the build emits a leaf-lineage diff entry (old row → new row → trigger) beside the alternates list, so reviewers can attribute a leaf move to the cascade rather than to fresh evidence.

Bug Hunt's S1T trial count ignores the recorded run count: the SD uses 
𝑛
=
105
n=105 planted bugs even when the record is a mean over 
𝑁
N published runs, overstating the mean's noise. The direction is conservative (widest noise bands, never a label), so severity is low. Recommended change: use 
105
×
𝑁
105×N (or the between-run SD over the E224 cross-harness/run list when 
𝑁
≥
2
N≥2) and keep the wide reading as published sensitivity.

LiveBench 2.0 Overall's SD uses the 2026-10-14 task counts for the 2026-10-23 release, and the "wide reading" counts Reasoning and Data Analysis parts as independent binomial trials. Recommended change: a registry requirement to re-check per-release task counts at each LiveBench capture; when absent, the provisional-SD flag is already implicit — print it explicitly beside the leaf's provenance.

Inconsistent suppression thresholds for rank-correlation diagnostics: the workload cross-check suppresses 
𝜏
𝑏
τ
b
	​

 below 
𝑛
=
8
n=8 matched rows, but the Terminal-Bench cross-source agreement (E229) publishes 
𝜏
𝑏
=
0.74
τ
b
	​

=0.74 on a 5-row panel and "undefined (panel too small)" at 1 row. Recommended change: one suppression rule (panel size, and the rule for "undefined") governing all published 
𝜏
𝑏
τ
b
	​

 statistics.

E181's logistic sensitivity pins 
𝐸
𝐴
=
1600
E
A
	​

=1600 to a named model's rating: like anchors, the pin should be versioned with a re-pinning bridge if AA replaces its scale anchor, otherwise the sensitivity silently tracks a stale reference. Recommended change: store the pin with date and source, treat re-pinning as an anchor-version event.

2. Methodology design recommendations

Prioritised, all implementable from routinely refreshable public data.

Meter-denomination register with conditional O88 grading (highest value per unit effort): one field per plan row in the route registry, populated at each staged-research capture from provider documentation; grading rule 
=
1
[
denomination
∈
{
tokens, credits
}
]
=1[denomination∈{tokens, credits}]. This is a public, stable attribute of plan terms, cheap to refresh, and it fixes the measured-only view's composition.

Direction-consistent uncertain numerators: extend the E74 scalar convention to every un-identified numerator family — scored rows display the conservative end of their admissible interval, with the optimistic end and interval width printed as diagnostics. Formula: displayed multiple 
=
min
⁡
𝑀
admissible
=minM
admissible
	​

 for set-valued evidence (matching E74); the O46 ceiling then lives in the diagnostic column.

Paired quality–cost coupling stream: add S1T-paired to the stream allowlist with target profile restricted to (same-execution leaf, same-execution cost component) pairs, sampling task clusters jointly where AA's published per-task records pair outcome and cost; publish the correlation grid 0 / 0.3 / 0.6 as the conservative reading where pairing is not public (the O42 grid machinery is already built).

Two-column separability and adjacent-rank reporting: separability counts restricted to distinct-configuration pairs on the Plan basis, with same-configuration pairs reported separately and marked "structural".

Bug Hunt effective sample size: 
𝑛
eff
=
105
×
𝑁
runs
n
eff
	​

=105×N
runs
	​

 for the S1T SD of the mean, with the between-run empirical SD preferred once 
≥
2
≥2 same-harness runs are published (the E224 objects already capture the values).

Uniform rank-correlation suppression policy: a single registered rule (minimum panel 8; below it "not estimable (insufficient panel)") applied to E229, E41 and any future 
𝜏
𝑏
τ
b
	​

 diagnostic, declared once and cited.

Versioned sensitivity pins: the E181 anchor 
𝐸
𝐴
E
A
	​

, LiveBench task counts and similar external constants get { value, source, capturedOn, version } records; a change triggers a bridge note rather than a silent move.

3. Questions for the owner

For O88/O87: do you accept denomination-conditioned grading (token/credit meters keep "measured" status across efforts; message/window meters are graded donor-assumptions), or should all cross-effort transport keep its current single grade? The answer determines recommendation 1 of section 2 and the scope of my medium finding on the measured-only view.

For the coupling stream: does AA's published per-task Terminal-Bench/FrontierCode data actually pair per-task cost with per-task outcome in a joinable form? If not, recommendation 3 degrades to the correlation-grid reading plus the "dependence unmodeled" note, and I need to know which you prefer before it enters the allowlist.

4. Verdict

VERDICT: HAS FEEDBACK