0. Read check

Read all three requested files to their ends, in order, at commit 8cbc853b5cf9f5665ee354d68fae165ab1566856. This review is limited to those files. Rules incorporated by reference are treated as defined, not missing.

Part 10

First line:

Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress. Deletion branches (E146): each registered branch names its removed leaf set R. Displayed-score deletion sensitivity removes R globally and renormalises the remaining observed weights, Q̄i^(−R) = Σ{b∈O_i∖R} w_b z_ib ÷ Σ_{b∈O_i∖R} w_b (a zero denominator leaves the row unevaluable in the branch, listed), keeping the primary workload, selected route, anchors and cost score; a branch whose retained nominal weight Σ_{b∉R} w_b is under 40% is "not identifiable under the coverage rule" (leave-AA-out today: 34% and 22%); rank changes and τ_b use the common panel (E65). *Evidence unavailability* — the full-composite target with the removed observations replaced by their admissible domains, reported as bounds or convention-dependent scenarios — is a distinct, separately named branch and never shares a deletion branch's name. Registered branches: one per leaf of the ranking (leave-one-benchmark-out), one per multi-leaf source (leave-AA-out, and, under E258, every publisher of two or more independently run leaves in the ranking: leave-Vals-out in the max-effort ranking, LiveBench 2.0 Overall being a single-leaf source since O61, so leave-one-benchmark-out covers it) and the basket-scope branch (E178), which removes jointly the leaves whose benchmarks O15 and O137 exclude from the cost basket as knowledge or science recall (AA-Omniscience, HLE-Diamond, CritPt v2; retained nominal weight 86.7%, the same in every ranking because these leaves carry the same weights in each; GDPval-AA and AA-LCR, which left the basket only because v5 no longer publishes their costs, are kept) and is labelled "quality restricted to the cost basket's scope" (O10 and O15 are unchanged: the scored quality vector stays general); a single-leaf source (Bug Hunt Bench; LiveBench 2.0 Overall in the max-effort ranking; AI Coding Daily in its ranking) coincides with its leaf's branch, which carries both labels, and the Bug Hunt branch is the standing Bug Hunt removal. Standing cost-component removal (E64, defined by E149): a cost-deletion object D_cost = (R_C, W∖R_C, anchor policy, route policy, multiple policy, panel rule), separate from quality deletion; R_C names execution components, not quality leaves. The standing column removes AA's Index-run Terminal-Bench 4.0 (the Coding Agent Index also executes Terminal-Bench v4) and publishes two named calculations on the main-workload panel, each compared with the primary ranks on the common panel (E65) with quality held at Q̄_i: (a) *cost-component removal, original anchors* — C_i^(−TB) = C_i,W − C_i,TB scored on the original anchor object A_W, V = 0.25·S_C(C_i^(−TB); A_W) + 0.75·Q̄_i (a sensitivity of the published scoring scale); (b) *alternative workload, recalibrated anchors* — W∖TB scored on anchors rebuilt with the ln 2 padding from every row with a cost on W∖TB, with the new exchange rate published beside the rank changes so cost-composition and recalibration effects can be told apart. On the Plan basis each row keeps its selected route and displayed multiple, labelled "fixed-multiple arithmetic stress (not identified Plan economics for the altered workload)"; basis typing (E152): with A_i the API basket cost, m_i the selected displayed multiple and P_i = A_i / m_i, the removal subtracts the API component cost before dividing — A_i^(−TB) = A_i − A_i,TB is scored only against API anchors and P_i^(−TB) = (A_i − A_i,TB) / m_i only against Plan anchors, in both calculations (fixture: A = 100, A_TB = 20, m = 4 gives P = 25 and P^(−TB) = 20 — never 25 − 20 = 5, never 80 against Plan anchors); API-fallback rows take P_i^(−TB) = A_i^(−TB), as on the primary workload; an M_W identified for W is reused for W∖TB only when its identification mechanism also covers W∖TB. Leave-one-component-out cost family (E172): the same D_cost object, with both named calculations and basis typing, is registered once per admitted basket unit (O15's admission units, E148; the Coding Agent Index is one unit) and published per basis as rank changes on the common panel with each recalibrated exchange rate; with the matched-cost diagnostic (quality-weighted complete passes) and the per-row expenditure shares (E22), it shows how far the ranking depends on AA's task multiplicities, which O15 fixes for the scored workload. No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

Last 12 words:

“population pin bar?”

Correction: the exact last 12 words are:

“puts the quartile bars on the headline's position or a neighbour; from four configurations the three positions are distinct.”

That quoted ending contains more than 12 words; the exact 12-word suffix is:

“or a neighbour; from four configurations the three positions are distinct.”

Part 11

First line:

A frozen level is never a configuration, and a configuration qualifies only when its full-composite bound is at or above the level (Q ≥ H, E156's policy object), so the setter itself, still ranked with every leaf, qualifies weakly at exactly H and is reported as such, never silently excluded; the population-count condition only makes the level well defined. Whether an output compares alternatives depends on R_W. Every bar result therefore publishes possibleQualifierN, the number of R_W configurations that can possibly qualify, and reads "comparison vacuous" below two (E198a).

Last 12 words:

“says these outputs compare ranked configurations only and names the listed configurations.”

Part 12

First line:

Interval decision procedure (E40, amended by E43). Interval labels are decided by deterministic, decision-specific feasibility problems over Θ, never from scenario draws. Primitive domains have a box enclosure (per-row input boxes and a box of declared shared factors, e.g. a common price list or a donor multiple shared by several rows); Θ itself is the constrained subset defined by E73, and a product-box representation may replace it only under a decision-specific equivalence proof (E169). Constrained evidence model (E73): the primitive-variable constraint graph Θ = {v : ℓ ≤ v ≤ u, h(v) = 0, g(v) ≤ 0} is authoritative; costs, quality, capacities and multiples are derived quantities of v (an identity such as API-valued capacity = λ × C_API survives uncertainty propagation). A box reduction is used only with a decision-specific equivalence proof; otherwise the box is an outer enclosure for pruning, and every witness is certified against the original constraints (release fixture: an enclosing box containing a favourable state the original constraints exclude must never return a certified possible membership). Separability condition (E89): with no shared factor and no row-local coupling — each row's C and Q depend on disjoint primitives with no joint constraint, so the row's feasible set is the product of its C and Q ranges — each label is decided exactly by monotone extremes (Q is linear in leaf values; basket cost is monotone in component costs; each row's inputs move only its own C and Q): e.g. possible-frontier membership of i is established by setting i to its best corner and every j to its worst. A row-local primitive or constraint that enters both C_i and Q_i is a coupled variable and is branched over like a shared factor; a constraint class the solver does not support returns unresolved (release test: i with C_i = 1 + t, Q_i = t, t ∈; j with C = 1, Q = 0.5; k with C = 1.5, Q = 1 — i is dominated for every t although its box corner (1, 1) is undominated, so the solver must return disproved and never a possible membership). In v1 every row's C and Q come from distinct published records, so the condition holds and is asserted per release. Shared price factors (E276): two rows can still share a cost factor, through one model's price list (two efforts of one model, including a superseded tariff's hull, E183) or one registered pricing omission (O94, O98); such a factor moves the rows' costs together, never against each other. A row carrying one is a blocker that competes and never earns a label (E183, E186, O94), and the factor covers every effort of its model, so a candidate never shares it; the possible-frontier and bar tests set every competitor at one common extreme (all at their worst corners, or all at their best), a state the shared factor permits, and the definite test moves one competitor at a time, so the per-row boxes give the same answers as the joint constraint; the one cross-row factor the Plan basis can create, a donor multiple shared by several configurations, is checked by the build: when two configurations among a decision's Plan candidates rest on one donor multiple identified only as a range, the Plan interval outputs are unresolved, with the shared donor named, and never computed by corners (E273). With shared factors or row-local coupling, labels are decided by certified interval branch-and-bound over the shared-factor box: on each sub-box, interval bounds either certify the condition for every point (witness), refute it for every point (prune), or the sub-box is split, up to a published depth; a sub-box still undecided at that depth returns unresolved. Endpoint search alone is not sufficient (release test: competitors with Q_j = 2t and Q_k = 2(1 − t), C_j = C_k = 0, and i with C_i = 1, Q_i = 1.2: i is a possible-frontier member via the interior witness t = 0.5). Possible-frontier membership solves, in one common θ, for every j ≠ i: C_j(θ) > C_i(θ) ∨ Q_j(θ) < Q_i(θ) ∨ [C_j(θ) = C_i(θ) ∧ Q_j(θ) = Q_i(θ)]; definite membership is disproved by one θ and one dominating j; strict inequalities are decided exactly, never by tolerance alone. Every returned witness is re-checked against the original equations and shared constraints. The monotone-corner shortcut is used only for decisions with a documented corner-reduction proof; dependencies are compiled from the complete decision equations, so a varying reference quality Q_r is a shared variable for every qualification condition even when all row inputs are independent (E50; a frozen bar level is a constant and adds no shared variable, but the rule binds any registered varying reference): bar decisions partition at qualification breakpoints (exact enumeration for affine one-dimensional thresholds) or use the certified branch-and-bound (regression test: i with C = 1, Q = 5; j with C = 0, Q = 4; Q_r ∈ — i ∈ K_r via the interior witness Q_r = 4.5, which neither endpoint shows). Feasible witnesses and infeasibility certificates have separate proof obligations, and numerical bounds may not discard feasible points through floating-point error. Statuses: certified / disproved / unresolved / unevaluable, with solver status, depth and witness (or counterexample) stored; an unresolved solve is never shown as certified. Certification grammar (E108): each decision is compiled into (1) primitive domains and the original constraints, (2) a reduced problem obtained only by documented, equivalence-preserving substitutions (definitional equalities are eliminated by substitution wherever possible) and (3) a certificate checked independently against the original problem. Supported v1 classes: boxes, affine constraints decided in exact rational arithmetic on the published decimal inputs, separable monotone transforms and the documented corner reductions; a nonlinear equality is supported only with a validated existence certificate (e.g. a sign change of a continuous univariate function evaluated exactly at rational endpoints); every other class returns unresolved, and a small numerical residual is never a feasibility certificate (fixtures: x² = 2 with x ∈ is certified feasible without a rational witness; x² = 2 with x ∈ [1, 1.4] is certified infeasible; an approximate point with residual 10⁻⁶ certifies nothing). Feasibility prerequisite (E79): before any decision, the decision's full constraint component (all connected shared variables and identities) must have a certified feasible witness checked against the original constraints; certified infeasible → "inconsistent evidence", no frontier or bar labels for the affected output, release-blocking for that output with the conflicting records listed; feasibility unresolved → "unresolved", no confirmed or definite label (fixtures: individually valid intervals whose shared identity has an empty intersection; a feasible outer box whose original constrained set is empty — neither may produce a confirmed, definite or certified-possible result).
0

Last 12 words:

“or definite result; every cost check reads C_W, never the Index diagnostic.”

Source locations for the sectional review: part 10, part 11, part 12.

1. Findings by severity
Critical

None.

High

None.

Medium

E273’s shared-donor guard should explicitly cover blockers, not just “Plan candidates.” Issue: Part 12 says Plan interval outputs become unresolved when “two configurations among a decision’s Plan candidates” share a donor multiple identified only as a range. However, the actual decision universe includes blockers, 
𝑈
𝑊
=
𝑅
𝑊
∪
𝐵
𝑊
U
W
	​

=R
W
	​

∪B
W
	​

, and BlockerSafe also compares candidates with blockers. A blocker can have an otherwise eligible Plan route; its blocker status does not necessarily remove a shared donor dependency. The broader constrained-model rules already require correct handling, but the narrower build-check wording leaves an avoidable implementation ambiguity. Part 10, E183; part 11, E186; part 12, E273/E276. Why it hurts the objective: Independent cost corners can invent a candidate–blocker ordering that no common donor value permits. For example, with 
𝑀
∈
[
1
,
2
]
M∈[1,2], 
𝐶
𝑖
=
100
/
𝑀
C
i
	​

=100/M and 
𝐶
𝑏
=
90
/
𝑀
C
b
	​

=90/M, blocker 
𝑏
b is always cheaper. Treating the intervals independently admits the impossible comparison 
𝐶
𝑖
=
50
<
𝐶
𝑏
=
90
C
i
	​

=50<C
b
	​

=90. That can contaminate possible-cheapest or possible-frontier membership unless the general dependency machinery overrides the shortcut. Concrete change: Define the guard over all rows and derived quantities appearing in the compiled decision, including 
𝐵
𝑊
B
W
	​

 and BlockerSafe. Require either a decision-specific joint reduction proof or the existing certified solver/unresolved outcome. What is new relative to the ledger: This is not a request to adopt shared-donor handling again; E273 already does that. It is the candidate–blocker boundary case absent from the quoted guard and fixtures.

Low

“Comparison vacuous” counts potential label recipients, not the full competitor universe. Issue: E198a requires “comparison vacuous” when fewer than two rows in 
𝑅
𝑊
R
W
	​

 can qualify. But a qualifying blocker in 
𝐵
𝑊
B
W
	​

 can make the comparison substantive and deny the sole eligible candidate a label. Thus one eligible qualifier plus one decisive blocker is not a vacuous comparison, although the specified message says it is. Part 11, E198a and the confirmed-cheapest/BlockerSafe definitions. Why it hurts the objective: The user-facing explanation can imply that no meaningful alternative was tested when the result was actually constrained by an adverse-evidence competitor. Concrete change: Retain possibleQualifierN for continuity, but rename its displayed interpretation to “potentially qualifying label-eligible rows,” separately count potentially qualifying blockers, and reserve “comparison vacuous” for fewer than two potentially qualifying competitors across 
𝑈
𝑊
U
W
	​

, with unresolved blocker qualification reported separately. What is new relative to the ledger: E198/E201 establish qualifier counts; E279 later broadens the blocker universe. This finding concerns their interaction, not the already-adopted requirement to publish counts.

2. Methodology design recommendations

Prioritise a decision-universe dependency assertion. For each interval decision 
𝑑
d, construct:

𝐽
𝑑
=
{
all rows whose costs or qualities occur in 
𝑑
}
,
J
d
	​

={all rows whose costs or qualities occur in d},

including candidate rows, competitors, blockers and any derived route quantities. For each uncertain primitive 
𝑣
v, record:

𝑆
𝑣
,
𝑑
=
{
𝑖
∈
𝐽
𝑑
:
 
𝐶
𝑖
 or 
𝑄
𝑖
 depends on 
𝑣
}
.
S
v,d
	​

={i∈J
d
	​

: C
i
	​

 or Q
i
	​

 depends on v}.

If 
∣
𝑆
𝑣
,
𝑑
∣
>
1
∣S
v,d
	​

∣>1, independent-row corners are allowed only with the already-required decision-specific equivalence proof. Otherwise use the supported joint solver or return unresolved. This is a precise extension of the existing E73/E108/E147 machinery, not a new uncertainty model. Add a regression fixture with a qualifying candidate and qualifying blocker sharing 
𝑀
∈
[
1
,
2
]
M∈[1,2], using 
100
/
𝑀
100/M and 
90
/
𝑀
90/M. Assert that the candidate cannot become cheapest through incompatible donor endpoints. Add a second fixture with two blockers sharing that donor, to exercise possible-membership decisions involving all competitors simultaneously.

Separate eligibility counts from competition counts. Publish, per bar:

possibleEligibleQualifierN: potentially qualifying rows in 
𝑅
𝑊
R
W
	​

.

possibleBlockerQualifierN: potentially qualifying rows in 
𝐵
𝑊
B
W
	​

.

unresolvedBlockerQualifierN: blockers whose qualification cannot be decided.

competitionStatus: substantive / vacuous / unresolved.

Preserve the existing count fields as aliases if needed. Define “vacuous” only when the full decision universe is resolved and contains fewer than two potentially qualifying competitors. When there is one eligible qualifier and a qualifying blocker, say “one eligible qualifier; blocker competition present.”

Both recommendations use the draft’s existing captured evidence and compiled decision objects. Neither requires additional private data, provider marketing quotas, cross-variant imputation, changed weights or an owner-policy reversal.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK