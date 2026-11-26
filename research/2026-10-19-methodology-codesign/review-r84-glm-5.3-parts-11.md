0. Read check

Read both listed parts to their ends through the GitHub connector, in order, at commit 8e532e4891e1759c825d0fed89e1ae32fbc9eea1. This review is limited to those two parts.

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

Source references below identify the part and governing rule directly. The connector returned the complete file contents but did not provide citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The cheaper-sibling disclosure uses a different cost object from the answer it qualifies

Issue: E201c and O143 identify unevaluated cheaper siblings using AA’s total Index cost. However, the cheapest-above-bar answers use the ranking’s admitted workload cost, and Plan answers additionally depend on the selected plan route. Part 12 explicitly ends with the requirement that “every cost check reads C_W, never the Index diagnostic,” while the sibling disclosure expressly uses total Index cost. These are different comparisons.
Source: part 11, “Unevaluated cheaper siblings (E201c)” and O143; part 12, “Release tests.”

Why it hurts the objective: The disclosure can omit precisely the unevaluated alternative relevant to the buyer’s cost basis. For example, an unranked sibling could have higher total Index cost but lower cost on the admitted SDLC basket. The existing filter would not name it. Conversely, a lower-total-Index sibling need not be cheaper on the basket or on the selected Plan basis. This does not invalidate the explicitly bounded ranking claim, but it makes the adjacent limitation notice an unreliable guide to where a cheaper alternative might exist.

This is a logical possibility, not a claim that a particular current sibling exhibits the reversal.

Concrete change: Keep the adopted Index-based disclosure, but label its comparison object explicitly and add a workload- and basis-aligned check wherever exact public cost evidence permits:

“Lower AA total Index cost; workload-cost ordering unverified.”

“Lower API cost on this ranking’s workload.”

“Lower Plan cost on this plan and workload.”

“Cost comparison unavailable.”

Do not infer any missing cost, transfer quality evidence, rank the sibling, or extend the claim to it.

What is new relative to the ledger: This does not repeat the already adopted request to name cheaper siblings. It identifies a mismatch between the cost criterion selecting those names and the cost criterion used by the answer they qualify.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the sibling caveat cost-object aware

Extend uncheckedCheaperSiblings and the O143 headline companion with a small typed comparison record:

Field	Purpose
comparison_basis	API or a named Plan
cost_workload_hash	Identifies the exact admitted workload being compared
index_cost_relation	Preserves the existing AA total Index comparison
workload_cost_relation	Cheaper / tied / dearer / unidentified
cost_evidence_status	Exact public evidence, incomplete, or unavailable
ranking_exclusion_reason	Missing required quality leaf, outside ranking population, or another recorded reason
claim_scope	Always “unevaluated alternative; no qualification claim”

For an API answer 
𝑖
i, a same-family unranked sibling 
𝑗
j should receive the workload-cheaper marker only when the same workload is publicly priced for both:

𝐶
𝑗
,
𝑊
<
𝐶
𝑖
,
𝑊
.
C
j,W
	​

<C
i,W
	​

.

If costs are bounded rather than point-identified, distinguish:

definitely cheaper:
sup
⁡
𝜃
∈
Θ
(
𝐶
𝑗
,
𝑊
(
𝜃
)
−
𝐶
𝑖
,
𝑊
(
𝜃
)
)
<
0
,
definitely cheaper:
θ∈Θ
sup
	​

(C
j,W
	​

(θ)−C
i,W
	​

(θ))<0,

from:

possibly cheaper:
∃
𝜃
∈
Θ
:
𝐶
𝑗
,
𝑊
(
𝜃
)
<
𝐶
𝑖
,
𝑊
(
𝜃
)
.
possibly cheaper:∃θ∈Θ:C
j,W
	​

(θ)<C
i,W
	​

(θ).

Use the existing certified solver and its unresolved status; do not substitute independent corners when the existing dependency rules prohibit them. For Plan comparisons, require the same named plan and the already-defined admissible route evidence. Otherwise report the comparison as unidentified.

This reuses the draft’s existing workload hashes, basis typing, evidence statuses and interval machinery rather than introducing a new ranking or measurement programme.
Source: part 11, E100’s decision-target signature and E201c/O143; part 12, E40/E73/E108.

Priority 2 — Add cost-reversal fixtures for the disclosure

Add three release fixtures:

A same-family sibling has higher total Index cost but lower complete 
𝐶
𝑊
C
W
	​

: it appears as a workload-cheaper unevaluated alternative.

A sibling has lower total Index cost but higher 
𝐶
𝑊
C
W
	​

: it remains in the Index-based disclosure, but is not described as cheaper for the headline workload.

A sibling has lower total Index cost but lacks exact workload costs: it is marked “workload-cost ordering unverified,” without imputation.

For Plan outputs, add a fourth fixture in which API and Plan cost orderings differ; each disclosure must retain its own basis.

These fixtures extend the existing requirement that cost decisions use the correct workload object, without changing the cohort, exact-variant evidence policy, Plan numerator rules, or claim universe.
Source: part 12, “Release tests”; part 11, E38/O43’s scope contract.

3. Questions for the owner

None.

4. Verdict

The two reviewed parts provide careful separation of published-record interval claims, scenario frequencies, sensitivity outputs and unevaluated configurations. I found one material presentation-design gap: the cheaper-sibling limitation notice is selected using a different cost object from the buyer-facing answer. Fixing that disclosure requires neither a policy reversal nor additional private data.

VERDICT: HAS FEEDBACK