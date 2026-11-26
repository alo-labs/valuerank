0. Read check

Read all three requested parts to their ends through the GitHub connector, in order, at commit 0aedd96ddfb5c1e86ba1487bc7845bfe301e946d. The first lines are unusually long paragraphs; they are quoted in full below.

Part 10

First line:

Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress. Deletion branches (E146): each registered branch names its removed leaf set R. Displayed-score deletion sensitivity removes R globally and renormalises the remaining observed weights, Q̄i^(−R) = Σ{b∈O_i∖R} w_b z_ib ÷ Σ_{b∈O_i∖R} w_b (a zero denominator leaves the row unevaluable in the branch, listed), keeping the primary workload, selected route, anchors and cost score; a branch whose retained nominal weight Σ_{b∉R} w_b is under 40% is "not identifiable under the coverage rule" (leave-AA-out today: 34% and 22%); rank changes and τ_b use the common panel (E65). *Evidence unavailability* — the full-composite target with the removed observations replaced by their admissible domains, reported as bounds or convention-dependent scenarios — is a distinct, separately named branch and never shares a deletion branch's name. Registered branches: one per leaf of the ranking (leave-one-benchmark-out), one per multi-leaf source (leave-AA-out, and, under E258, every publisher of two or more independently run leaves in the ranking: leave-Vals-out in the max-effort ranking, LiveBench 2.0 Overall being a single-leaf source since O61, so leave-one-benchmark-out covers it) and the basket-scope branch (E178), which removes jointly the leaves whose benchmarks O15 and O137 exclude from the cost basket as knowledge or science recall (AA-Omniscience, HLE-Diamond, CritPt v2; retained nominal weight 86.7%, the same in every ranking because these leaves carry the same weights in each; GDPval-AA and AA-LCR, which left the basket only because v5 no longer publishes their costs, are kept) and is labelled "quality restricted to the cost basket's scope" (O10 and O15 are unchanged: the scored quality vector stays general); a single-leaf source (Bug Hunt Bench; LiveBench 2.0 Overall in the max-effort ranking; AI Coding Daily in its ranking) coincides with its leaf's branch, which carries both labels, and the Bug Hunt branch is the standing Bug Hunt removal. Standing cost-component removal (E64, defined by E149): a cost-deletion object D_cost = (R_C, W∖R_C, anchor policy, route policy, multiple policy, panel rule), separate from quality deletion; R_C names execution components, not quality leaves. The standing column removes AA's Index-run Terminal-Bench 4.0 (the Coding Agent Index also executes Terminal-Bench v4) and publishes two named calculations on the main-workload panel, each compared with the primary ranks on the common panel (E65) with quality held at Q̄_i: (a) *cost-component removal, original anchors* — C_i^(−TB) = C_i,W − C_i,TB scored on the original anchor object A_W, V = 0.25·S_C(C_i^(−TB); A_W) + 0.75·Q̄_i (a sensitivity of the published scoring scale); (b) *alternative workload, recalibrated anchors* — W∖TB scored on anchors rebuilt with the ln 2 padding from every row with a cost on W∖TB, with the new exchange rate published beside the rank changes so cost-composition and recalibration effects can be told apart. On the Plan basis each row keeps its selected route and displayed multiple, labelled "fixed-multiple arithmetic stress (not identified Plan economics for the altered workload)"; basis typing (E152): with A_i the API basket cost, m_i the selected displayed multiple and P_i = A_i / m_i, the removal subtracts the API component cost before dividing — A_i^(−TB) = A_i − A_i,TB is scored only against API anchors and P_i^(−TB) = (A_i − A_i,TB) / m_i only against Plan anchors, in both calculations (fixture: A = 100, A_TB = 20, m = 4 gives P = 25 and P^(−TB) = 20 — never 25 − 20 = 5, never 80 against Plan anchors); API-fallback rows take P_i^(−TB) = A_i^(−TB), as on the primary workload; an M_W identified for W is reused for W∖TB only when its identification mechanism also covers W∖TB. Leave-one-component-out cost family (E172): the same D_cost object, with both named calculations and basis typing, is registered once per admitted basket unit (O15's admission units, E148; the Coding Agent Index is one unit) and published per basis as rank changes on the common panel with each recalibrated exchange rate; with the matched-cost diagnostic (quality-weighted complete passes) and the per-row expenditure shares (E22), it shows how far the ranking depends on AA's task multiplicities, which O15 fixes for the scored workload. No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

Last 12 words:

“the quartile bars on the headline's position or a neighbour; from four configurations the three positions are distinct.”

Correction to the word boundary: the exact last 12 whitespace-delimited words are:

“headline's position or a neighbour; from four configurations the three positions are distinct.”

Part 11

First line:

A frozen level is never a configuration, and a configuration qualifies only when its full-composite bound is at or above the level (Q ≥ H, E156's policy object), so the setter itself, still ranked with every leaf, qualifies weakly at exactly H and is reported as such, never silently excluded; the population-count condition only makes the level well defined. Whether an output compares alternatives depends on R_W. Every bar result therefore publishes possibleQualifierN, the number of R_W configurations that can possibly qualify, and reads "comparison vacuous" below two (E198a).

Last 12 words:

“outputs compare ranked configurations only and names the listed configurations.”

The exact 12-word suffix, including the preceding words, is:

“summary says these outputs compare ranked configurations only and names the listed configurations.”

Part 12

First line:

Interval decision procedure (E40, amended by E43). Interval labels are decided by deterministic, decision-specific feasibility problems over Θ, never from scenario draws. Primitive domains have a box enclosure (per-row input boxes and a box of declared shared factors, e.g. a common price list or a donor multiple shared by several rows); Θ itself is the constrained subset defined by E73, and a product-box representation may replace it only under a decision-specific equivalence proof (E169). Constrained evidence model (E73): the primitive-variable constraint graph Θ = {v : ℓ ≤ v ≤ u, h(v) = 0, g(v) ≤ 0} is authoritative; costs, quality, capacities and multiples are derived quantities of v (an identity such as API-valued capacity = λ × C_API survives uncertainty propagation). A box reduction is used only with a decision-specific equivalence proof; otherwise the box is an outer enclosure for pruning, and every witness is certified against the original constraints (release fixture: an enclosing box containing a favourable state the original constraints exclude must never return a certified possible membership). Separability condition (E89): with no shared factor and no row-local coupling — each row's C and Q depend on disjoint primitives with no joint constraint, so the row's feasible set is the product of its C and Q ranges — each label is decided exactly by monotone extremes (Q is linear in leaf values; basket cost is monotone in component costs; each row's inputs move only its own C and Q): e.g. possible-frontier membership of i is established by setting i to its best corner and every j to its worst. A row-local primitive or constraint that enters both C_i and Q_i is a coupled variable and is branched over like a shared factor; a constraint class the solver does not support returns unresolved (release test: i with C_i = 1 + t, Q_i = t, t ∈; j with C = 1, Q = 0.5; k with C = 1.5, Q = 1 — i is dominated for every t although its box corner (1, 1) is undominated, so the solver must return disproved and never a possible membership). In v1 every row's C and Q come from distinct published records, so the condition holds and is asserted per release. Shared price factors (E276): two rows can still share a cost factor, through one model's price list (two efforts of one model, including a superseded tariff's hull, E183) or one registered pricing omission (O94, O98); such a factor moves the rows' costs together, never against each other. A row carrying one is a blocker that competes and never earns a label (E183, E186, O94), and the factor covers every effort of its model, so a candidate never shares it; the possible-frontier and bar tests set every competitor at one common extreme (all at their worst corners, or all at their best), a state the shared factor permits, and the definite test moves one competitor at a time, so the per-row boxes give the same answers as the joint constraint; the one cross-row factor the Plan basis can create, a donor multiple shared by several configurations, is checked by the build: when two configurations among a decision's Plan candidates rest on one donor multiple identified only as a range, the Plan interval outputs are unresolved, with the shared donor named, and never computed by corners (E273). With shared factors or row-local coupling, labels are decided by certified interval branch-and-bound over the shared-factor box: on each sub-box, interval bounds either certify the condition for every point (witness), refute it for every point (prune), or the sub-box is split, up to a published depth; a sub-box still undecided at that depth returns unresolved. Endpoint search alone is not sufficient (release test: competitors with Q_j = 2t and Q_k = 2(1 − t), C_j = C_k = 0, and i with C_i = 1, Q_i = 1.2: i is a possible-frontier member via the interior witness t = 0.5). Possible-frontier membership solves, in one common θ, for every j ≠ i: C_j(θ) > C_i(θ) ∨ Q_j(θ) < Q_i(θ) ∨ [C_j(θ) = C_i(θ) ∧ Q_j(θ) = Q_i(θ)]; definite membership is disproved by one θ and one dominating j; strict inequalities are decided exactly, never by tolerance alone. Every returned witness is re-checked against the original equations and shared constraints. The monotone-corner shortcut is used only for decisions with a documented corner-reduction proof; dependencies are compiled from the complete decision equations, so a varying reference quality Q_r is a shared variable for every qualification condition even when all row inputs are independent (E50; a frozen bar level is a constant and adds no shared variable, but the rule binds any registered varying reference): bar decisions partition at qualification breakpoints (exact enumeration for affine one-dimensional thresholds) or use the certified branch-and-bound (regression test: i with C = 1, Q = 5; j with C = 0, Q = 4; Q_r ∈ — i ∈ K_r via the interior witness Q_r = 4.5, which neither endpoint shows). Feasible witnesses and infeasibility certificates have separate proof obligations, and numerical bounds may not discard feasible points through floating-point error. Statuses: certified / disproved / unresolved / unevaluable, with solver status, depth and witness (or counterexample) stored; an unresolved solve is never shown as certified. Certification grammar (E108): each decision is compiled into (1) primitive domains and the original constraints, (2) a reduced problem obtained only by documented, equivalence-preserving substitutions (definitional equalities are eliminated by substitution wherever possible) and (3) a certificate checked independently against the original problem. Supported v1 classes: boxes, affine constraints decided in exact rational arithmetic on the published decimal inputs, separable monotone transforms and the documented corner reductions; a nonlinear equality is supported only with a validated existence certificate (e.g. a sign change of a continuous univariate function evaluated exactly at rational endpoints); every other class returns unresolved, and a small numerical residual is never a feasibility certificate (fixtures: x² = 2 with x ∈ is certified feasible without a rational witness; x² = 2 with x ∈ [1, 1.4] is certified infeasible; an approximate point with residual 10⁻⁶ certifies nothing). Feasibility prerequisite (E79): before any decision, the decision's full constraint component (all connected shared variables and identities) must have a certified feasible witness checked against the original constraints; certified infeasible → "inconsistent evidence", no frontier or bar labels for the affected output, release-blocking for that output with the conflicting records listed; feasibility unresolved → "unresolved", no confirmed or definite label (fixtures: individually valid intervals whose shared identity has an empty intersection; a feasible outer box whose original constrained set is empty — neither may produce a confirmed, definite or certified-possible result).
0

Last 12 words:

“or definite result; every cost check reads C_W, never the Index diagnostic.”

1. Findings by severity
Critical

None.

High

None.

Medium

The Omniscience reconstruction gate does not propagate the reporting precision of its inputs. Issue: Part 12 requires the reconstruction

𝐼
=
100
[
𝐴
−
ℎ
(
1
−
𝐴
)
]
I=100[A−h(1−A)]

to match AA’s published index within 0.05 index points, described as half the index’s displayed precision. That accounts for rounding of the published index, but not rounding of the accuracy and conditional hallucination rate used to reconstruct it. These sections otherwise explicitly require published-record rounding intervals and constrained consistency checks. Why it hurts the objective: a perfectly consistent public record can fail this release-blocking check merely because its three displayed statistics were rounded separately. This impedes routine refreshes without identifying a genuine evidence inconsistency. For example, consider a hypothetical underlying record with 
𝐴
=
0.60048
A=0.60048 and 
ℎ
=
0.25
h=0.25. Its index is 
50.06
50.06. If the source displays accuracy and hallucination rate to one decimal percentage point, and the index to one decimal index point, the displayed record is:

Accuracy: 60.0%.

Conditional hallucination rate: 25.0%.

Omniscience Index: 50.1.

Reconstructing from the two displayed rates gives 50.0, so the specified gate fails by 0.1 despite all three figures being mutually compatible. Concrete change: replace the point-residual gate with a joint reporting-precision feasibility test. Keep the 0.05 index interval, but also carry the actual displayed precision of both rates. Fail only when no values inside those three rounding intervals satisfy the identity. If exact counts are available, additionally check the count identity using those counts. What is new relative to the ledger: this is not a challenge to O28’s scoring formula, E209’s cost-reconciliation tolerance, or the adopted Omniscience reconstruction diagnostic. It identifies a false-positive failure mode in the diagnostic’s particular 0.05 point-residual criterion.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the Omniscience gate a precision-aware consistency certificate

Implement this using only the public statistics and their captured display precision:

Record each displayed value as an exact decimal, with its unit and last published digit.

Construct rounding intervals:

𝐴
∈
[
𝐴
𝐿
,
𝐴
𝑈
]
,
ℎ
∈
[
ℎ
𝐿
,
ℎ
𝑈
]
,
𝐼
∈
[
𝐼
𝐿
,
𝐼
𝑈
]
.
A∈[A
L
	​

,A
U
	​

],h∈[h
L
	​

,h
U
	​

],I∈[I
L
	​

,I
U
	​

].

Convert percentage-point precision to proportion units before applying the formula.

Because

𝑓
(
𝐴
,
ℎ
)
=
100
[
𝐴
−
ℎ
(
1
−
𝐴
)
]
f(A,h)=100[A−h(1−A)]

increases with 
𝐴
A and decreases with 
ℎ
h on 
[
0
,
1
]
2
[0,1]
2
, calculate its exact range:

𝐼
r
e
c
o
n
s
t
r
u
c
t
e
d
∈
[
100
{
𝐴
𝐿
−
ℎ
𝑈
(
1
−
𝐴
𝐿
)
}
,
100
{
𝐴
𝑈
−
ℎ
𝐿
(
1
−
𝐴
𝑈
)
}
]
.
I
reconstructed
	​

∈[100{A
L
	​

−h
U
	​

(1−A
L
	​

)},100{A
U
	​

−h
L
	​

(1−A
U
	​

)}].

Pass the rounded-summary check when this range intersects the published index interval. Preserve the point residual as a diagnostic, not as the blocking criterion.

When counts are published, require the count-derived values to lie inside the corresponding displayed intervals. A count disagreement should remain blocking.

Store the source precision, feasible intersection and certificate with the release evidence.

Add regression fixtures for:

Compatible separately rounded figures with a point residual above 0.05.

An incompatible record whose intervals do not intersect.

An exact-count record consistent with all displayed summaries.

Rate displays at different precisions.

This changes no quality weights, cohort membership, exact-variant policy, Plan evidence admission, or published-record uncertainty target. It applies the draft’s existing rounding-and-feasibility architecture consistently to one additional release gate.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK