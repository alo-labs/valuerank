All seven parts have been read in full. Before writing the review, I'll verify the draft's stated numerical fixtures computationally and run targeted web checks on the external factual claims the draft leans on.
All numerical fixtures in the draft verify exactly (uniform 91.45% vs arcsine 86.75%; Clopper–Pearson closed forms; E88/E152 arithmetic; Bug Hunt 49.52; O28 vectors; token identity 37,901,142; 303 tasks). The web checks confirm the Terminal-Bench whisker claim and AA's GDPval methodology. One more check on the LiveBench retirement (O26) before I write the review:
0. Read check

All seven parts were opened through the GitHub connector at commit 715bfc51c8f311b00410b3fca9f37f823b0c56e4 and each was read to its end; no part is missing or truncated.

First line of the draft, quoted exactly:

# ValueRank methodology — draft r54

Last 12 words of each part, in order:

"cost per task, not AA's 7:2:1 blended price, not total Index cost."

"unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements)."

"analysis, not imputation). A row without a cost gets no value score."

"No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities."

"candidate's cost upper bound); otherwise "not established", with the omitted competitors listed."

"or definite result; every cost check reads C_W, never the Index diagnostic."

"cost evidence covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."

Verification preamble for Section 1: I executed every stated numerical fixture that is executable from the draft. All check exactly — the E137 kernel fixture (uniform 91.45% vs arcsine 86.75% for the three-missing-leaf qualification event), the E77 Clopper–Pearson closed-form endpoints at δ = 0.05/16, the E88 dominance and E152 basis-typing fixtures, the Bug Hunt vector (52/105 → 49.52), the O28 Omniscience vectors, the token-ontology identity (13,409,872 + 24,491,270 = 37,901,142), and the 303-task Coding Agent Index decomposition. External checks confirm the draft's claims that Terminal-Bench's whiskers "span the 95% confidence interval", that LiveBench 2.0's seven suites (Agentic, Reasoning, Coding, Browser Use, Data Analysis, Research, Design) contain no instruction-following suite, and AA's GDPval methodology (Crowd-BT maximum-likelihood fit, sandwich-estimator intervals, named anchor model). One external check surfaces a finding against E174, below.
tbench
+2

1. Findings by severity

Critical

None.

High

None. The normative layer is internally consistent: the exchange-rate algebra in Outputs is exact; the comparator, dominance filter and admission enumeration are total and reproducible; O29's current-tariff bound [C·min r, C·max r] is correct as a demand-weighted mean; E167/E166/E168 close the transfer and amount-lineage loops; and the fixture set I executed all passes.

Medium

E174's registry statement on GDPval-AA intervals understates the public documentation. The draft records the per-configuration "CI" as an interval of unstated level because "the leaderboard does not state the interval's level." But AA's methodology page — the same page the draft already pins for the GDPval transform — states that the 95% confidence intervals are computed with the sandwich estimator on the Crowd-BT maximum-likelihood fit, with ties counted as half-wins and balanced task exposure per model, corroborated by third-party summaries. This hurts the objective twice: the registry misstates the evidence state (a documentation-accuracy defect in a methodology whose credibility rests on the registry), and it leaves S1M with a single leaf when a second leaf's interval is publicly documented at a stated level, needlessly narrowing the only stream that touches published benchmark uncertainty. Concrete change: reword the registry entry to "level documented on AA's methodology page (95%, sandwich estimator on Crowd-BT MLE); payload not captured," prioritise the capture task, and pre-fill the E165 interpretation contract's fields (source_estimand, source_interval_method, repeated_task_treatment) from that page; the remaining gate is sampling unit. If the contract is satisfied on capture, GDPval-AA joins Terminal-Bench in S1M; if not, publish it beside the leaf as a documented-level interval rather than "unstated level."
artificialanalysis
+1

No joint sensitivity for the unpriced-quality share — a scope mismatch between the quality vector and the cost basket. O15 excludes HLE, AA-Omniscience and CritPt from the cost basket, while O10's single quality vector retains ≈13.3% of quality weight on exactly those leaves (Omniscience 10%, HLE and CritPt 5/3% each). The headline value score therefore ranks on quality shifts that have no cost counterpart anywhere in the scored pipeline. Leave-one-benchmark-out exists per leaf (E146) and priced-mix coverage is published, but no registered branch removes the unpriced set jointly, so a buyer cannot see how much of the ordering rests on capability the cost side never prices. Concrete change: register a named S2 specification branch (E146 displayed-score deletion machinery, E65 common panel, τ_b and rank changes) deleting {AA-Omniscience, HLE, CritPt} jointly. Labelled Owner decision challenge (O15/O10 combination): the SDLC-only basket is the right scored choice for the stated buyer, but since the quality vector is deliberately general-capability-inclusive, the paired-scope view should be visible, not only inferable from per-leaf branches.

Selection bias in comparator key 3 for unidentified routes. Among unidentified routes the comparator selects the largest observed multiple (the owner's highest-eligible rule), and unidentified routes are never filtered by E88 — so a model with many admissible unidentified route–measurement pairs gets more draws at a favorable multiple. Selecting the maximum over noisy estimates is downward-biased (winner's curse): Plan costs look systematically cheaper for multi-route models than for single-route models, a distortion unrelated to any buyer-relevant economics. The existing route-selection sensitivity (lower-bound-only choice) and the E171 route-alternative table do not expose this. Concrete change, without touching the owner's rule: publish per row the count of admissible unidentified route–measurement pairs ("selection intensity") beside the Plan table, and register a jackknife selection-sensitivity that re-runs the comparator with each admissible unidentified route dropped in turn, publishing the min/max/selected spread of the displayed multiple per row and how often the selected multiple is the maximum of its candidate set.

Low

Notation "5/3% each" in the quality table for HLE/SciCode/CritPt is mathematically exact (1⅔% each) but reads as "5 or 3 percent" at a glance. Write "1.67% each (5% split across the three leaves)."

Known limitations omits non-workload subscription value. The value multiple values only the measured workload's consumption, but plan fees typically buy surfaces outside the scored workload (chat, image generation, shared pools across surfaces — the quota schema tracks the pools, not the value). A Plan buyer reading the headline has no statement that the multiple is workload-scoped value, not total subscription value. Add one line to Known limitations and one to the Plan outputs; E166 types the amount's target, not the fee's unmeasured side.

2. Methodology design recommendations

Prioritised; all implementable from public data refreshable on the monthly cadence.

Reclassify and capture the GDPval-AA intervals (from Medium 1). Amend E174's registry wording, schedule the capture, and pre-populate the E165 contract from AA's documented method (Crowd-BT MLE, sandwich 95% CI, ties as half-wins, balanced task exposure). This is the cheapest available widening of S1M from one leaf to two, and it strengthens the O25 boundary by moving a published interval from "beside the leaf" into a governed stream.
artificialanalysis

Register the joint unpriced-quality deletion branch (from Medium 2). Reuse E146's deletion machinery verbatim: remove R = {AA-Omniscience, HLE, CritPt} globally, renormalise observed weights, keep workload, route, anchors and cost score fixed, publish rank changes and τ_b on the E65 common panel, and report the retained nominal weight (86.7%). Optional companion diagnostic: a value score computed against the total Index cost (already a captured diagnostic) with the same quality vector, labelled as the opposite-scope view, so both scope mismatches (cost narrower than quality; cost wider than the SDLC buyer) are visible.

Selection-intensity and jackknife diagnostics for route selection (from Medium 3). Two published columns on the Plan table (candidate count; multiple spread under leave-one-route-out) plus a flag when the selected multiple is the maximum of more than three candidates. No change to the comparator, the owner's rule, or interval eligibility.

Roadmap the independent-evidence share. Leave-AA-out is "not identifiable under the coverage rule" at ≈20% independent weight — the structural concentration risk of the whole quality vector. The E26 admission machinery (≥ 2/3 exact-variant cohort coverage, versioned admission) is already built; apply it to candidate independent SWE leaves with public per-configuration results (e.g. SWE-bench Verified official leaderboards, which are public and model-versioned ) as they achieve coverage. This is the only structural fix for the leave-AA-out non-identifiability and directly serves the objective's "in practice" clause; it is a versioned quality migration, not a v1 change.
swebench

Editorial fixes (from Low findings): the "5/3% each" notation and the Known-limitations line on non-workload subscription value.

3. Questions for the owner

For E174/E165: does documentation on the source's methodology page (rather than the leaderboard payload itself) count as the documentation that fixes an interval's level and method for the interpretation contract? AA's methodology page states the 95% sandwich-estimator level; your answer determines whether GDPval-AA enters S1M immediately on capture or is published beside the leaf, and how the registry statement is worded.
artificialanalysis

Is the ≈13.3% unpriced quality share an accepted permanent feature of the O10/O15 pairing, or a gap you intend to shrink as priced evidence arrives? The answer sets the priority of recommendation 2 versus recommendation 4.

4. Verdict

The draft is sound at its core — every executable fixture verifies, the governance and identification machinery is coherent, and the external claims I checked (Terminal-Bench whiskers, LiveBench 2.0's suite set, AA's GDPval methodology ) hold. The remaining material findings are the E174 registry statement, the missing joint unpriced-quality sensitivity, and the key-3 selection-bias exposure.
tbench
+2

VERDICT: HAS FEEDBACK