0. Read check

Read all three listed files to their ends through the GitHub connector, in order, at commit 2ca6c729a3f1a11bd08f5d669f5977875b087381. This review concerns only parts 10–12. References below identify the part and normative rule; the connector returned no citation identifiers.

Part 10

First line:

Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress. Deletion branches (E146): each registered branch names its removed leaf set R. Displayed-score deletion sensitivity removes R globally and renormalises the remaining observed weights, Q̄i^(−R) = Σ{b∈O_i∖R} w_b z_ib ÷ Σ_{b∈O_i∖R} w_b (a zero denominator leaves the row unevaluable in the branch, listed), keeping the primary workload, selected route, anchors and cost score; a branch whose retained nominal weight Σ_{b∉R} w_b is under 40% is "not identifiable under the coverage rule" (leave-AA-out today: 34% and 22%); rank changes and τ_b use the common panel (E65). *Evidence unavailability* — the full-composite target with the removed observations replaced by their admissible domains, reported as bounds or convention-dependent scenarios — is a distinct, separately named branch and never shares a deletion branch's name. Registered branches: one per leaf of the ranking (leave-one-benchmark-out), one per multi-leaf source (leave-AA-out, and, under E258, every publisher of two or more independently run leaves in the ranking: leave-Vals-out in the max-effort ranking, LiveBench 2.0 Overall being a single-leaf source since O61, so leave-one-benchmark-out covers it) and the basket-scope branch (E178), which removes jointly the leaves whose benchmarks O15 and O137 exclude from the cost basket as knowledge or science recall (AA-Omniscience, HLE-Diamond, CritPt v2; retained nominal weight 86.7%, the same in every ranking because these leaves carry the same weights in each; GDPval-AA and AA-LCR, which left the basket only because v5 no longer publishes their costs, are kept) and is labelled "quality restricted to the cost basket's scope" (O10 and O15 are unchanged: the scored quality vector stays general); a single-leaf source (Bug Hunt Bench; LiveBench 2.0 Overall in the max-effort ranking; AI Coding Daily in its ranking) coincides with its leaf's branch, which carries both labels, and the Bug Hunt branch is the standing Bug Hunt removal. Standing cost-component removal (E64, defined by E149): a cost-deletion object D_cost = (R_C, W∖R_C, anchor policy, route policy, multiple policy, panel rule), separate from quality deletion; R_C names execution components, not quality leaves. The standing column removes AA's Index-run Terminal-Bench 4.0 (the Coding Agent Index also executes Terminal-Bench v4) and publishes two named calculations on the main-workload panel, each compared with the primary ranks on the common panel (E65) with quality held at Q̄_i: (a) *cost-component removal, original anchors* — C_i^(−TB) = C_i,W − C_i,TB scored on the original anchor object A_W, V = 0.25·S_C(C_i^(−TB); A_W) + 0.75·Q̄_i (a sensitivity of the published scoring scale); (b) *alternative workload, recalibrated anchors* — W∖TB scored on anchors rebuilt with the ln 2 padding from the registered anchor population on W∖TB (E160 and E184's eligibility evaluated on the reduced workload; on the Plan basis its measured rows only, O157), its reference and excluded ids published, and the calculation reported unavailable when fewer than two references qualify (E317, on reviewer 84), with the new exchange rate published beside the rank changes so cost-composition and recalibration effects can be told apart. On the Plan basis each row keeps its selected route and displayed multiple, labelled "fixed-multiple arithmetic stress (not identified Plan economics for the altered workload)"; basis typing (E152): with A_i the API basket cost, m_i the selected displayed multiple and P_i = A_i / m_i, the removal subtracts the API component cost before dividing — A_i^(−TB) = A_i − A_i,TB is scored only against API anchors and P_i^(−TB) = (A_i − A_i,TB) / m_i only against Plan anchors, in both calculations (fixture: A = 100, A_TB = 20, m = 4 gives P = 25 and P^(−TB) = 20 — never 25 − 20 = 5, never 80 against Plan anchors); API-fallback rows take P_i^(−TB) = A_i^(−TB), as on the primary workload; an M_W identified for W is reused for W∖TB only when its identification mechanism also covers W∖TB. Leave-one-component-out cost family (E172): the same D_cost object, with both named calculations and basis typing, is registered once per admitted basket unit (O15's admission units, E148; the Coding Agent Index is one unit) and published per basis as rank changes on the common panel with each recalibrated exchange rate; with the matched-cost diagnostic (quality-weighted complete passes) and the per-row expenditure shares (E22), it shows how far the ranking depends on AA's task multiplicities, which O15 fixes for the scored workload. No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

Last 12 words:

position or a neighbour; from four configurations the three positions are distinct.

Part 11

First line:

A frozen level is never a configuration, and a configuration qualifies only when its full-composite bound is at or above the level (Q ≥ H, E156's policy object), so the setter itself, still ranked with every leaf, qualifies weakly at exactly H and is reported as such, never silently excluded; the population-count condition only makes the level well defined. Whether an output compares alternatives depends on U_W = R_W ∪ B_W. Every bar result therefore publishes possibleQualifierN, the number of R_W configurations that can possibly qualify, and possibleBlockerQualifierN, the blockers that can possibly qualify (they compete but earn no label), and reads "comparison vacuous" only when the two together are below two (E198a, amended by E315 on reviewer 83: one eligible qualifier against a qualifying blocker is a substantive comparison).

Last 12 words:

says these outputs compare ranked configurations only and names the listed configurations.

Part 12

First line:

Interval decision procedure (E40, amended by E43). Interval labels are decided by deterministic, decision-specific feasibility problems over Θ, never from scenario draws. Primitive domains have a box enclosure (per-row input boxes and a box of declared shared factors, e.g. a common price list or a donor multiple shared by several rows); Θ itself is the constrained subset defined by E73, and a product-box representation may replace it only under a decision-specific equivalence proof (E169). Constrained evidence model (E73): the primitive-variable constraint graph Θ = {v : ℓ ≤ v ≤ u, h(v) = 0, g(v) ≤ 0} is authoritative; costs, quality, capacities and multiples are derived quantities of v (an identity such as API-valued capacity = λ × C_API survives uncertainty propagation). A box reduction is used only with a decision-specific equivalence proof; otherwise the box is an outer enclosure for pruning, and every witness is certified against the original constraints (release fixture: an enclosing box containing a favourable state the original constraints exclude must never return a certified possible membership). Separability condition (E89): with no shared factor and no row-local coupling — each row's C and Q depend on disjoint primitives with no joint constraint, so the row's feasible set is the product of its C and Q ranges — each label is decided exactly by monotone extremes (Q is linear in leaf values; basket cost is monotone in component costs; each row's inputs move only its own C and Q): e.g. possible-frontier membership of i is established by setting i to its best corner and every j to its worst. A row-local primitive or constraint that enters both C_i and Q_i is a coupled variable and is branched over like a shared factor; a constraint class the solver does not support returns unresolved (release test: i with C_i = 1 + t, Q_i = t, t ∈; j with C = 1, Q = 0.5; k with C = 1.5, Q = 1 — i is dominated for every t although its box corner (1, 1) is undominated, so the solver must return disproved and never a possible membership). In v1 every row's C and Q come from distinct published records, so the condition holds and is asserted per release. Shared price factors (E276): two rows can still share a cost factor, through one model's price list (two efforts of one model, including a superseded tariff's hull, E183) or one registered pricing omission (O94, O98); such a factor moves the rows' costs together, never against each other. A row carrying one is a blocker that competes and never earns a label (E183, E186, O94), and the factor covers every effort of its model, so a candidate never shares it; the possible-frontier and bar tests set every competitor at one common extreme (all at their worst corners, or all at their best), a state the shared factor permits, and the definite test moves one competitor at a time, so the per-row boxes give the same answers as the joint constraint; the one cross-row factor the Plan basis can create, a donor multiple shared by several configurations, is checked by the build: when two configurations among the rows a decision reads (its Plan candidates, competitors and the blockers B_W of U_W = R_W ∪ B_W, E313 on reviewer 83) rest on one donor multiple identified only as a range, the Plan interval outputs are unresolved, with the shared donor named, and never computed by corners (E273). With shared factors or row-local coupling, labels are decided by certified interval branch-and-bound over the shared-factor box: on each sub-box, interval bounds either certify the condition for every point (witness), refute it for every point (prune), or the sub-box is split, up to a published depth; a sub-box still undecided at that depth returns unresolved. Endpoint search alone is not sufficient (release test: competitors with Q_j = 2t and Q_k = 2(1 − t), C_j = C_k = 0, and i with C_i = 1, Q_i = 1.2: i is a possible-frontier member via the interior witness t = 0.5). Possible-frontier membership solves, in one common θ, for every j ≠ i: C_j(θ) > C_i(θ) ∨ Q_j(θ) < Q_i(θ) ∨ [C_j(θ) = C_i(θ) ∧ Q_j(θ) = Q_i(θ)]; definite membership is disproved by one θ and one dominating j; strict inequalities are decided exactly, never by tolerance alone. Every returned witness is re-checked against the original equations and shared constraints. The monotone-corner shortcut is used only for decisions with a documented corner-reduction proof; dependencies are compiled from the complete decision equations, so a varying reference quality Q_r is a shared variable for every qualification condition even when all row inputs are independent (E50; a frozen bar level is a constant and adds no shared variable, but the rule binds any registered varying reference): bar decisions partition at qualification breakpoints (exact enumeration for affine one-dimensional thresholds) or use the certified branch-and-bound (regression test: i with C = 1, Q = 5; j with C = 0, Q = 4; Q_r ∈ — i ∈ K_r via the interior witness Q_r = 4.5, which neither endpoint shows). Feasible witnesses and infeasibility certificates have separate proof obligations, and numerical bounds may not discard feasible points through floating-point error. Statuses: certified / disproved / unresolved / unevaluable, with solver status, depth and witness (or counterexample) stored; an unresolved solve is never shown as certified. Certification grammar (E108): each decision is compiled into (1) primitive domains and the original constraints, (2) a reduced problem obtained only by documented, equivalence-preserving substitutions (definitional equalities are eliminated by substitution wherever possible) and (3) a certificate checked independently against the original problem. Supported v1 classes: boxes, affine constraints decided in exact rational arithmetic on the published decimal inputs, separable monotone transforms and the documented corner reductions; a nonlinear equality is supported only with a validated existence certificate (e.g. a sign change of a continuous univariate function evaluated exactly at rational endpoints); every other class returns unresolved, and a small numerical residual is never a feasibility certificate (fixtures: x² = 2 with x ∈ is certified feasible without a rational witness; x² = 2 with x ∈ [1, 1.4] is certified infeasible; an approximate point with residual 10⁻⁶ certifies nothing). Feasibility prerequisite (E79): before any decision, the decision's full constraint component (all connected shared variables and identities) must have a certified feasible witness checked against the original constraints; certified infeasible → "inconsistent evidence", no frontier or bar labels for the affected output, release-blocking for that output with the conflicting records listed; feasibility unresolved → "unresolved", no confirmed or definite label (fixtures: individually valid intervals whose shared identity has an empty intersection; a feasible outer box whose original constrained set is empty — neither may produce a confirmed, definite or certified-possible result).
0

Last 12 words:

or definite result; every cost check reads C_W, never the Index diagnostic.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The executable definition of 
𝑅
𝑊
R
W
	​

 does not explicitly exclude blockers, although subsequent formulas require that partition

Issue: Part 10 defines 
𝑅
𝑊
R
W
	​

 as cohort rows with FullCost and, for Plan, identified 
𝑀
𝑊
M
W
	​

. It then defines 
𝐵
𝑊
B
W
	​

 as rows that “would otherwise belong to 
𝑅
𝑊
R
W
	​

” and says blockers earn no memberships or labels. However, the displayed set definition of 
𝑅
𝑊
R
W
	​

 never expressly subtracts blockers. The frontier predicates subsequently require only 
𝑖
∈
𝑅
𝑊
i∈R
W
	​

, without an explicit non-blocker condition. Part 11’s possible-cheapest set likewise requires 
𝑖
∈
𝑅
𝑊
i∈R
W
	​

.

The intended policy is clear from the surrounding prose, including part 11’s description of 
𝑅
𝑊
R
W
	​

 as rows “that are not blockers.” The remaining defect is in the executable mathematical definition, not the owner’s blocker policy.

Why it hurts the objective: An implementation following the initial set definition literally could:

award frontier membership to a blocker;

admit a blocker into the certified possible-cheapest candidate set;

double-count a qualifying blocker in possibleQualifierN + possibleBlockerQualifierN;

report a substantive comparison where only one distinct configuration exists.

Concrete change: Define an eligibility set first, then a disjoint partition:

𝐸
𝑊
=
{
𝑖
:
ranking row, FullCost, and basis-specific interval eligibility
}
,
E
W
	​

={i:ranking row, FullCost, and basis-specific interval eligibility},
𝐵
𝑊
=
{
𝑖
∈
𝐸
𝑊
:
blocker
⁡
(
𝑖
)
}
,
𝑅
𝑊
=
{
𝑖
∈
𝐸
𝑊
:
¬
blocker
⁡
(
𝑖
)
}
,
𝑈
𝑊
=
𝑅
𝑊
∪˙
𝐵
𝑊
.
B
W
	​

={i∈E
W
	​

:blocker(i)},R
W
	​

={i∈E
W
	​

:¬blocker(i)},U
W
	​

=R
W
	​

∪
˙
B
W
	​

.

Apply O155’s excluded-route rule before constructing 
𝐸
𝑊
E
W
	​

. Add assertions that 
𝑅
𝑊
∩
𝐵
𝑊
=
∅
R
W
	​

∩B
W
	​

=∅, every candidate belongs to 
𝑅
𝑊
R
W
	​

, and qualifier counts count distinct IDs.

New argument relative to the ledger: E279 and E313 already address which blocker kinds and dependencies must be included. This finding concerns the missing explicit set subtraction and its effect on candidate membership and qualifier counting—not reopening blocker inclusion policy.

Low
L1. “The only open row at a bar is its setter” is not guaranteed by complete benchmark coverage

Issue: Part 11, E221, says:

“While no ranked row has a missing leaf (O36), the only open row at a bar is its setter, on reporting precision only.”

Complete coverage removes missing-leaf uncertainty, but it does not prevent another configuration’s reporting-precision interval from crossing the same frozen bar. Equal displayed qualities, or sufficiently close displayed qualities, can produce multiple open rows. E201b’s softer wording—“typically the bar’s own configuration”—does not have this problem.

Why it hurts the objective: This overstates what O36 guarantees and could encourage a UI or test to attribute every unresolved qualification to the setter rather than to the actual interval calculation.

Concrete change: Replace it with:

“While every ranked row has every leaf, any open qualification is due to reporting precision rather than missing leaves. The setter is normally open when its interval straddles the frozen level; other rows may also be open.”

If only the setter is open in the current release, render that as a checked release-specific observation, not a general methodological consequence.

New argument relative to the ledger: This does not challenge O34’s frozen bars, O25’s published-record target, or E201’s disclosure. It distinguishes a current-data observation from a universal implication of complete coverage.

2. Methodology design recommendations
1. Make competitor classification a single executable partition

Prioritise M1. Produce one decision-population object per ranking, basis and workload, containing:

eligible candidate IDs, 
𝑅
𝑊
R
W
	​

;

blocker IDs, 
𝐵
𝑊
B
W
	​

, with all applicable reasons;

excluded IDs and exclusion reasons;

the union 
𝑈
𝑊
U
W
	​

;

a hash consumed by every frontier, bar, scenario-label and qualifier-count calculation.

Use that object rather than independently reconstructing membership inside individual outputs.

Add a minimal regression fixture: one fully costed, fully benchmarked configuration with a provider-claimed leaf and no other configurations. It belongs to 
𝐵
𝑊
B
W
	​

, receives no candidate membership or label, contributes zero to possibleQualifierN, contributes at most one to possibleBlockerQualifierN, and leaves the comparison vacuous. This tests the set partition without changing any evidence-admission policy.

2. Generate statements about open qualification from interval results

For each bar, derive:

Open
⁡
𝐻
=
{
𝑖
∈
𝑅
𝑊
:
𝑄
𝑖
𝐿
<
𝐻
≤
𝑄
𝑖
𝑈
}
.
Open
H
	​

={i∈R
W
	​

:Q
i
L
	​

<H≤Q
i
U
	​

}.

Report each open row with an uncertainty-source classification, such as reporting precision or missing evidence. Do not infer this set from coverage or setter identity.

Add two fixtures:

Two complete configurations have equal displayed quality at 
𝐻
H, and both intervals straddle 
𝐻
H.

A non-setter’s displayed quality is slightly above 
𝐻
H, but its reporting-precision lower bound is below 
𝐻
H.

Both must be reported as open. This is implementable entirely from the draft’s existing public-record inputs and interval machinery; no additional data collection or probabilistic model is required.

I recommend no changes here to the owner-fixed cohort rule, exact-variant matching, 25/75 weighting, full-utilisation Plan target, or numerator-evidence policy. The reviewed sections already distinguish reporting precision, missing-evidence identification, task-sampling scenarios and specification stress with considerable care.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK