Part 10 read. Now reading part 11.
Part 11 read. Now reading part 12.
0. Read check

Read all three requested parts to their ends at commit 954f80eb52607a5c820ae8025c76915f0c6038d8. This review is limited to those parts.

Part 10

First line:

Uncertainty (three separate layers, one scenario engine)

Last 12 words:

not separable" and its S0 result is not described as target-workload support.

Source: Part 10.

Part 11

First line:

Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress. Deletion branches (E146): each registered branch names its removed leaf set R. Displayed-score deletion sensitivity removes R globally and renormalises the remaining observed weights, Q̄i^(−R) = Σ{b∈O_i∖R} w_b z_ib ÷ Σ_{b∈O_i∖R} w_b (a zero denominator leaves the row unevaluable in the branch, listed), keeping the primary workload, selected route, anchors and cost score; a branch whose retained nominal weight Σ_{b∉R} w_b is under 40% is "not identifiable under the coverage rule" (leave-AA-out today: 34% and 22%); rank changes and τ_b use the common panel (E65). *Evidence unavailability* — the full-composite target with the removed observations replaced by their admissible domains, reported as bounds or convention-dependent scenarios — is a distinct, separately named branch and never shares a deletion branch's name. Registered branches: one per leaf of the ranking (leave-one-benchmark-out), one per multi-leaf source (leave-AA-out, and, under E258, every publisher of two or more independently run leaves in the ranking: leave-Vals-out in the max-effort ranking, LiveBench 2.0 Overall being a single-leaf source since O61, so leave-one-benchmark-out covers it) and the basket-scope branch (E178), which removes jointly the leaves whose benchmarks O15 and O137 exclude from the cost basket as knowledge or science recall (AA-Omniscience, HLE-Diamond, CritPt v2; retained nominal weight 86.7%, the same in every ranking because these leaves carry the same weights in each; GDPval-AA and AA-LCR, which left the basket only because v5 no longer publishes their costs, are kept) and is labelled "recall/science-leaf removal sensitivity": it is not an execution-matched quality–cost comparison, which is the matched-cost diagnostic's question (E327, on reviewer 88; O10 and O15 are unchanged: the scored quality vector stays general); a single-leaf source (Bug Hunt Bench; LiveBench 2.0 Overall in the max-effort ranking; AI Coding Daily in its ranking) coincides with its leaf's branch, which carries both labels, and the Bug Hunt branch is the standing Bug Hunt removal. Standing cost-component removal (E64, defined by E149): a cost-deletion object D_cost = (R_C, W∖R_C, anchor policy, route policy, multiple policy, panel rule), separate from quality deletion; R_C names execution components, not quality leaves. The standing column removes AA's Index-run Terminal-Bench 4.0 (the Coding Agent Index also executes Terminal-Bench v4) and publishes two named calculations on the main-workload panel, each compared with the primary ranks on the common panel (E65) with quality held at Q̄_i: (a) *cost-component removal, original anchors* — C_i^(−TB) = C_i,W − C_i,TB scored on the original anchor object A_W, V = 0.25·S_C(C_i^(−TB); A_W) + 0.75·Q̄_i (a sensitivity of the published scoring scale); (b) *alternative workload, recalibrated anchors* — W∖TB scored on anchors rebuilt with the ln 2 padding from the registered anchor population on W∖TB (E160 and E184's eligibility evaluated on the reduced workload; on the Plan basis its measured rows only, O157), its reference and excluded ids published, and the calculation reported unavailable when fewer than two references qualify (E317, on reviewer 84), with the new exchange rate published beside the rank changes so cost-composition and recalibration effects can be told apart. On the Plan basis each row keeps its selected route and displayed multiple, labelled "fixed-multiple arithmetic stress (not identified Plan economics for the altered workload)"; basis typing (E152): with A_i the API basket cost, m_i the selected displayed multiple and P_i = A_i / m_i, the removal subtracts the API component cost before dividing — A_i^(−TB) = A_i − A_i,TB is scored only against API anchors and P_i^(−TB) = (A_i − A_i,TB) / m_i only against Plan anchors, in both calculations (fixture: A = 100, A_TB = 20, m = 4 gives P = 25 and P^(−TB) = 20 — never 25 − 20 = 5, never 80 against Plan anchors); API-fallback rows take P_i^(−TB) = A_i^(−TB), as on the primary workload; an M_W identified for W is reused for W∖TB only when its identification mechanism also covers W∖TB. Leave-one-component-out cost family (E172): the same D_cost object, with both named calculations and basis typing, is registered once per admitted basket unit (O15's admission units, E148; the Coding Agent Index is one unit) and published per basis as rank changes on the common panel with each recalibrated exchange rate; with the matched-cost diagnostic (quality-weighted complete passes) and the per-row expenditure shares (E22), it shows how far the ranking depends on AA's task multiplicities, which O15 fixes for the scored workload. No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

Last 12 words:

on quality). The current ladders are in Output 3 and scores.json barCurrency.

Source: Part 11.

Part 12

First line:

Fewer than two population configurations pin no bar: all three bars, and every output that reads them, are published as unavailable. Ladder minimum (E215): with two or three, only the headline bar is pinned, because floor((n − 1)k/4) puts the quartile bars on the headline's position or a neighbour; from four configurations the three positions are distinct.

Last 12 words:

says these outputs compare ranked configurations only and names the listed configurations.

Source: Part 12.

1. Findings by severity
Critical

None.

High

None.

Medium

M1 — The new noise companion tests individual margins but describes a joint purchasing conclusion.

Issue: O171 calls an answer “noise-separated” when its own standardized margin exceeds 1.96 and every cheaper row’s margin is below −1.96. It introduces this as whether the answer is “clear of benchmark noise.” These are separate, pointwise comparisons—not a calibrated joint assessment that the answer qualifies while all cheaper alternatives fail. Furthermore, comparisons share the same noisy bar setter, so their dependence matters. The existing S1T interpretation already acknowledges a mixed-target dispersion stress, rather than one coherent estimation-uncertainty model. Part 12, O171 · Part 10, S1T

Why it hurts the objective: the companion sits beside the cheapest-above-bar answer, precisely where readers need to distinguish record stability from performance robustness. “Clear of benchmark noise” can overstate what this conjunction of approximate marginal tests establishes. This finding does not assert that the current winners change.

Concrete change: retain O171’s calculation, but call it “passes the pointwise noise-margin screen,” explicitly stating “not a simultaneous confidence statement.” If a joint noise-robustness diagnostic is desired, publish a separately named joint-event stress frequency using the existing public-data kernels.

New argument relative to the ledger: this concerns the newly added O171 companion’s joint interpretation, not the already adopted disclosure that S1T mixes targets, and not an attempt to replace O128’s fixed margin.

Low

L1 — E221’s attainability guarantee fails when observed-score rounding matters.

Issue: E221 says a possibly-but-not-certainly qualifying row must have an attainable point-value threshold 
𝑢
∗
u
∗
 between 0 and 100. But qualification uses observed-score rounding intervals, while 
𝑢
∗
u
∗
 fixes those observations at their point values. The guarantee therefore does not follow. Part 12, E221

For example, let observed leaves carry 90 weight points and have displayed score 90 with admissible interval 
[
89.5
,
90.5
]
[89.5,90.5]; one missing leaf carries 10 points. At 
𝐻
=
91.2
H=91.2, qualification is possible because the upper composite is 
0.9
(
90.5
)
+
0.1
(
100
)
=
91.45
0.9(90.5)+0.1(100)=91.45. Nevertheless, the point-value formula gives 
𝑢
∗
=
102
u
∗
=102. Conversely, at 
𝐻
=
80.8
H=80.8, it gives 
𝑢
∗
=
−
2
u
∗
=−2, although confirmed qualification fails because the lower composite is 80.55.

Why it hurts the objective: the proposed explanation of “what would settle a row” can contradict the interval solver. This is currently dormant under O36’s complete-leaf rule, so it is not a present ranking defect. Part 12, E221

Concrete change: remove the unconditional attainability assertion. Preserve out-of-domain point thresholds and explain that qualification requires favorable observed-score rounding, or that adverse rounding prevents confirmation.

New argument relative to the ledger: this is a counterexample to the reviewer-93 clarification, not a renewed objection to displayed-quality bars.

2. Methodology design recommendations

Prioritize precise noise-companion wording. Keep the O171 categories and thresholds if desired, but describe them as a pointwise screen under the declared analytic approximation. Include the comparison-panel size, bar-setter identity, and S1T mixed-target caveat in the generated output. No new benchmark collection or change to official labels is required. Part 12, O171

Optionally add a joint noise diagnostic, without another certification system. For the displayed winner 
𝑖
i, hold the displayed-cost comparison panel fixed and evaluate

𝐸
𝑖
(
𝑠
)
=
1
 ⁣
[
𝑄
~
𝑖
(
𝑠
)
≥
𝐻
~
(
𝑠
)
 
∧
 
∀
𝑗
:
𝐶
𝑗
<
𝐶
𝑖
,
 
𝑄
~
𝑗
(
𝑠
)
<
𝐻
~
(
𝑠
)
]
.
E
i
(s)
	​

=1[
Q
	​

i
(s)
	​

≥
H
(s)
 ∧ ∀j:C
j
	​

<C
i
	​

, 
Q
	​

j
(s)
	​

<
H
(s)
].

Use one shared bar-setter draw 
𝐻
~
(
𝑠
)
H
(s)
 per replicate, preserving identity when a compared row is the setter. Publish the resulting frequency as a “joint noise-stress frequency,” not a probability or official label. Keep the official frozen 
𝐻
H unchanged; this is a separate diagnostic target consistent with O171’s treatment of setter noise. Existing S1T kernels supply the inputs, subject to their existing limitations. Part 10, scenario engine and S1T · Part 12, O171 and E52

Make E221’s threshold rounding-aware. With missing weight 
𝑚
=
∑
missing
𝑤
𝑏
m=∑
missing
	​

w
b
	​

, define the observed contribution 
𝐴
(
𝜃
)
=
∑
observed
𝑤
𝑏
𝑧
𝑏
(
𝜃
)
A(θ)=∑
observed
	​

w
b
	​

z
b
	​

(θ). Alongside the point threshold, publish

𝑢
favorable
=
100
𝐻
−
max
⁡
𝜃
∈
Θ
𝐴
(
𝜃
)
𝑚
,
𝑢
robust
=
100
𝐻
−
min
⁡
𝜃
∈
Θ
𝐴
(
𝜃
)
𝑚
.
u
favorable
	​

=
m
100H−max
θ∈Θ
	​

A(θ)
	​

,u
robust
	​

=
m
100H−min
θ∈Θ
	​

A(θ)
	​

.

Use the constrained 
Θ
Θ, not independent endpoint substitutions where dependencies exist. Preserve thresholds outside 
[
0
,
100
]
[0,100] and attach an explanatory status rather than clipping them. Add the two counterexamples above as regression fixtures. This uses the rounding domains and solver already specified in these parts. Part 11, joint admissible set · Part 12, E221

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK