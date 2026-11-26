All five parts were read to their ends through the GitHub connector. The review below is confined to what parts 1–5 state; rules they cite from later parts are treated as defined there.

0. Read check

Part 1 — first line: # ValueRank methodology — draft r177. Last 12 words: "configurations; applying O145 moved the release cutoff (O65) and re-captured every source."

Part 2 — first line: - **Two rankings (owner decisions O52, O53, O54)**: ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52). Last 12 words: "configuration missing a leaf after the search is listed, not ranked (O36)."

Part 3 — first line: ## Cost (25% of the value score). Last 12 words: "cost per task, not AA's 7:2:1 blended price, not total Index cost."

Part 4 — first line: - **Matched-cost diagnostic (diagnostic only).** C_i^match = Σ_{g∈G} ω_g P_ig over canonical execution families g (E55; …. Last 12 words: "weight whose leaves are priced in the basket) is published each release."

Part 5 — first line: - **Admission rule for the official Plan ranking (O11)**: a measured route enters only via a controlled saturation measurement with receipts (e.g. SemiAnalysis, …. Last 12 words: "for its plan and model (the build compares observers, not report values);"

1. Findings by severity

Critical

None.

High

Separability, bands and the E242 transfer tolerance use quality sampling noise only; cost is never drawn. The separability threshold is built from 
1.96
𝑆
𝐷
𝑖
2
+
𝑆
𝐷
𝑗
2
−
2
𝜌
𝑆
𝐷
𝑖
𝑆
𝐷
𝑗
1.96
SD
i
2
	​

+SD
j
2
	​

−2ρSD
i
	​

SD
j
	​

	​

 with SD_i = 0.75 × the analytic quality SD, and the draft itself concedes "cost is not drawn" while AA runs a single cost pass per configuration. Unlike the correlation direction (genuinely unsettled and disclosed), omitting cost noise has a known-sign effect: it can only widen the threshold, so the printed separable counts (2 of 6, 0 of 19) and the band boundaries are optimistic, and the E242 "factor by which a transfer can be wrong before value moves by the median threshold" is computed against an under-wide threshold, making transferred Plan rows look more robust than they are. This is not a repeat of the rejected "precision-aware weight shrinkage": nothing here asks to change scores, O25's scenario layer, or O39's stream; it asks that the standing display objects (bands, separable counts, tolerance) print a noise-complete variant, because those objects are what a reader uses to decide whether one configuration is "actually lower cost for the value" than its neighbour — the draft's stated question. Concrete change: beside each existing figure, print a second separable count, band set and median threshold computed with a cost-noise term: where AA publishes per-task costs (the Coding Agent Index per-task-attempt distribution, per-evaluation task costs), a plug-in SD of the cost score on the log scale; where it does not, a stated conservative coefficient-of-variation grid (e.g. 5/10/20%), exactly parallel to the existing correlation grid 0/0.3/0.6. All inputs are public and refresh routinely.

Owner decision challenge — O170's live whole-board Bug Hunt denominator. 
𝑧
=
100
⋅
(
planted+unplanted
)
/
(
board max planted + board max unplanted
)
z=100⋅(planted+unplanted)/(board max planted + board max unplanted) is recomputed "live each release" against a board whose max can be set by a non-cohort configuration. The new argument (not in the ledger's record of this decision): the denominator's live behaviour collides with two pinned commitments in these parts — frozen bars/anchors (O34/E192) and E177 swing attribution with named causes. A new board leader changes every incumbent's Bug Hunt z, hence every Q̄_i, between releases with zero change in any ranked row's evidence; bar crossings and rank swings then appear that E177 can only attribute to an off-cohort entrant's denominator field, and the "published record protected" posture of O25 applies to the record, not to the comparability of two releases' quality composites. The failure mode is a headline that silently re-floors every model because a hobbyist submission topped the Bug Hunt board. Concrete change: freeze the denominator (board maxima) with the anchor version, exactly like the bars; re-freeze it only on the versioned re-freeze cadence O120 already defines; keep the live-denominator value as a printed diagnostic (as the E199 frontier-families bar is printed beside the frozen one).

Medium

Basket admission maximises coverage, not SDLC representativeness, and the headline presents the result as "the" SDLC cost. E140's enumeration maximises (1) number of admitted components, (2) panel size |P(S)|, (3) target order. A priced-but-marginal component therefore always beats an unpriced-but-central one, and the final tie-break (target order) is reached only after the coverage criteria. The readiness table (E22) discloses this, but the headline's E59 basket label reads as a designed workload. The objective cares because the cost half of value is then whatever AA happened to price, priced-task mix drifting release to release. Concrete change: keep the enumeration (it is deterministic and public), but add a published "representativeness gap" line beside E59 naming each target component left unadmitted with its role (e.g. ITBench-AA's DevOps/IT remit) and its median expenditure share among evidenced rows (E173 already computes this machinery); and where two feasible sets tie on |S|, prefer the one whose target-order priority set is lexicographically smaller by target position before panel size — this still never trades a component for coverage, it only orders equal-cardinality sets by owner-listed priority.

All measured Plan evidence for two providers rests on one paywalled SemiAnalysis article, with alternatives frozen until owner re-selection. E238 fails the build if any Claude/ChatGPT route does not cite the one selected analysis; O130's monthly re-read guards the transcription but no second controlled measurement can displace or corroborate the selection except by owner act, and end-user report pairs are graded below it (comparator key 2). Today every SemiAnalysis route is change-flagged, so the entire measured Plan layer for the two largest providers is a single graded-down, flagged object. Concrete change: register the controlled-saturation-measurement source class (O11 already defines it generically) with the same E239-style registry the gap fills use, so a second qualifying controlled measurement enters the comparator automatically rather than awaiting re-selection; publish a single-source-concentration line in the summary naming how many selected routes trace to one measurement object.

Low

The E95/E140 "reference panel frozen with W" and "today" population counts are hard-coded in prose. These parts carry many "today N=…" figures that E265 renders from the build, but several population sentences (e.g. the 7-of-8 and 18-of-20 admission-panel counts, the six-class partition of the excluded set) read as assertions. Concrete change: emit each remaining hand-typed count from the same build object it describes (the pattern E265 already uses), so a wording drift cannot survive a cohort change.

2. Methodology design recommendations

Prioritised, all implementable from public, routinely refreshable data:

Noise-complete separability set (highest priority; backs finding 1). Threshold 
𝑇
𝑖
𝑗
=
1.96
 
(
0.75
 
𝑆
𝐷
𝑄
,
𝑖
)
2
+
(
0.25
 
𝑆
𝐷
𝐶
,
𝑖
)
2
+
(
0.75
 
𝑆
𝐷
𝑄
,
𝑗
)
2
+
(
0.25
 
𝑆
𝐷
𝐶
,
𝑗
)
2
−
2
𝜌
(
⋅
)
T
ij
	​

=1.96
(0.75SD
Q,i
	​

)
2
+(0.25SD
C,i
	​

)
2
+(0.75SD
Q,j
	​

)
2
+(0.25SD
C,j
	​

)
2
−2ρ(⋅)
	​

, with SD_C,i the cost-score SD on the log scale: plug-in from per-task cost dispersion where AA publishes it, else a printed CV grid. Publish alongside, never replacing, the O39 figures; print both band sets.

Rewarded-cost sensitivity beside the headline (backs the E203 asymmetry without touching O15). Compute a displayed-only 
𝑉
′
=
0.25
 
𝑆
𝐶
(
𝑊
∖
{
Briefcase, GDP.pdf, unrewarded SWE-Atlas share
}
)
+
0.75
 
𝑄
ˉ
V
′
=0.25S
C
	​

(W∖{Briefcase, GDP.pdf, unrewarded SWE-Atlas share})+0.75
Q
ˉ
	​

 renormalised over leaves whose executions are priced in the basket, plus the rank bridge against the headline. This quantifies, per release, how much of the ranking is driven by spend the quality side never credits (today's disclosed baseline spans a 15% unrewarded share plus SWE-Atlas QnA inside the pooled index cost), without any owner-policy change.

Versioned Bug Hunt denominator (backs finding 2). Freeze maxima at each re-freeze; the live-board z stays as a diagnostic delta printed beside E177's swing table.

Equal-cardinality admission tie-break by target-order priority (backs finding 3). One-line change to E140's lexicographic tuple; both the chosen and the runner-up set's rank bridge are already produced by the E177 replay machinery.

Pair-wise cost-outcome diagnostic for near ties. Since most adjacent ranks are inseparable, add per adjacent pair the probability (from the existing scenario streams) that the order flips, next to the band table — directly answers "which is actually lower cost" for the comparisons readers will make.

3. Questions for the owner

Does AA publish per-task cost rows (not only pooled means) for the Coding Agent Index and the six Index SDLC evaluations? If yes, recommendation 1's plug-in cost SD is exact; if no, it falls back to the CV grid.

Are quality scores for AA-Briefcase and GDP.pdf publicly available at exact configuration? If yes, the preferred fix for the unrewarded-share asymmetry is adding them as leaves on a workload migration, which is stronger than recommendation 2's displayed-only sensitivity.

Is the headline's intended reader output the ordinal rank or the band set? If bands are intended to carry the claim, finding 1's second band set becomes release-gating rather than beside-the-table.

4. Verdict

VERDICT: HAS FEEDBACK