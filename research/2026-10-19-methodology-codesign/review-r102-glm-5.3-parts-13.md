0. Read check

Both listed parts were read to their ends through the GitHub connector at commit 5c2ab13991d61e5a15c418407e9c9e95db001918, in the requested order. This review covers only those parts.

Part 13

First line:

Ladder positions (O34): with the population's n displayed qualities in ascending order, bar level H_k (k = 1, 2, 3; H = H_2, the headline bar; renamed from Q̄ in r70 so it is not confused with a row's displayed quality Q̄_i) is the value at zero-based position floor((n − 1)k/4), an element of the order, never an interpolated percentile. k = 2 is the headline bar H, which is the ⌈n/2⌉-th value for odd and even n; k = 1 and k = 3 are the lower and upper quartile bars. The policy object records order = ascending and position = floor((n − 1)k/4) for each bar, and the bars are published in the order k = 2, 1, 3. All three are frozen together, from the same population, with the anchor version. Fixtures: n = 32 gives the 8th, 16th and 24th ascending values (zero-based 7, 15 and 23); n = 9 gives zero-based 2, 4 and 6, and n = 15 gives 3, 7 and 10. At the 2026-10-21 pre-release re-freezes (O30, O31, O34, O33 and O36 changed the cohort or the policy), the population has 32 configurations and the ladder is 47.36 (GPT-6 Luna), 55.31 (Claude Sonnet 5.5 (high), headline) and 59.56 (GPT-6.1 Sol (high)). O30, O31, O34 and O36 left the anchor values unchanged. O33 added cheaper efforts, which lowered the low anchors (API $66.43 to $35.76, Plan $2.48 to $0.61; 29 references at O36); the high anchors were unchanged. All dual runs are kept in the research record. No release had been published, so the anchor version string stayed v3-2026-10-21. At the 2026-10-23 re-freezes at O53 (O47, E247, then one object per ranking, E253) E247's ladder over the 27 ranked configurations before O53 (32.26, 48.92 with GPT-6.1 Sol (medium) as headline, 54.99) was replaced before any release by one ladder per ranking; O61 then changed the max-effort ranking's leaves and re-froze its bars on the same anchor version (its cost anchors are unchanged, because they do not depend on quality). The current ladders are in Output 3 and scores.json barCurrency.

Final sentence:

Ranked configurations only (owner decision O43): a family listed under O38 with an indicative value (O41) is not a competitor in any frontier or bar output; each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

Part 14

First line:

Interval decision procedure (E40, amended by E43). Interval labels are decided by deterministic, decision-specific feasibility problems over Θ, never from scenario draws. Primitive domains have a box enclosure (per-row input boxes and a box of declared shared factors, e.g. a common price list or a donor multiple shared by several rows); Θ itself is the constrained subset defined by E73, and a product-box representation may replace it only under a decision-specific equivalence proof (E169). Constrained evidence model (E73): the primitive-variable constraint graph Θ = {v : ℓ ≤ v ≤ u, h(v) = 0, g(v) ≤ 0} is authoritative; costs, quality, capacities and multiples are derived quantities of v (an identity such as API-valued capacity = λ × C_API survives uncertainty propagation). A box reduction is used only with a decision-specific equivalence proof; otherwise the box is an outer enclosure for pruning, and every witness is certified against the original constraints (release fixture: an enclosing box containing a favourable state the original constraints exclude must never return a certified possible membership). Separability condition (E89): with no shared factor and no row-local coupling — each row's C and Q depend on disjoint primitives with no joint constraint, so the row's feasible set is the product of its C and Q ranges — each label is decided exactly by monotone extremes (Q is linear in leaf values; basket cost is monotone in component costs; each row's inputs move only its own C and Q): e.g. possible-frontier membership of i is established by setting i to its best corner and every j to its worst. A row-local primitive or constraint that enters both C_i and Q_i is a coupled variable and is branched over like a shared factor; a constraint class the solver does not support returns unresolved (release test: i with C_i = 1 + t, Q_i = t, t ∈; j with C = 1, Q = 0.5; k with C = 1.5, Q = 1 — i is dominated for every t although its box corner (1, 1) is undominated, so the solver must return disproved and never a possible membership). In v1 every row's C and Q come from distinct published records, so the condition holds and is asserted per release. Shared price factors (E276): two rows can still share an uncertain cost factor, through a superseded tariff's hull on one model's price list (two efforts of one model, E183) or one registered pricing omission (O94, O98) — tariffs in force are published constants, not uncertain factors; such a factor moves the rows' costs together, never against each other. A row carrying one is a blocker that competes and never earns a label (E183, E186, O94), and the factor covers every effort of its model, so a candidate never shares it; the possible-frontier and bar tests set every competitor at one common extreme (all at their worst corners, or all at their best), a state the shared factor permits, and the definite test moves one competitor at a time, so the per-row boxes give the same answers as the joint constraint; the one cross-row factor the Plan basis can create, a donor multiple shared by several configurations, is checked by the build: when two configurations among the rows a decision reads (its Plan candidates, competitors and the blockers B_W of U_W = R_W ∪ B_W, E313 on reviewer 83) rest on one donor multiple identified only as a range, the Plan interval outputs are unresolved, with the shared donor named, and never computed by corners (E273). With shared factors or row-local coupling, labels are decided by certified interval branch-and-bound over the shared-factor box: on each sub-box, interval bounds either certify the condition for every point (witness), refute it for every point (prune), or the sub-box is split, up to a published depth; a sub-box still undecided at that depth returns unresolved. Endpoint search alone is not sufficient (release test: competitors with Q_j = 2t and Q_k = 2(1 − t), C_j = C_k = 0, and i with C_i = 1, Q_i = 1.2: i is a possible-frontier member via the interior witness t = 0.5). Possible-frontier membership solves, in one common θ, for every j ≠ i: C_j(θ) > C_i(θ) ∨ Q_j(θ) < Q_i(θ) ∨ [C_j(θ) = C_i(θ) ∧ Q_j(θ) = Q_i(θ)]; definite membership is disproved by one θ and one dominating j; strict inequalities are decided exactly, never by tolerance alone. Every returned witness is re-checked against the original equations and shared constraints. The monotone-corner shortcut is used only for decisions with a documented corner-reduction proof; dependencies are compiled from the complete decision equations, so a varying reference quality Q_r is a shared variable for every qualification condition even when all row inputs are independent (E50; a frozen bar level is a constant and adds no shared variable, but the rule binds any registered varying reference): bar decisions partition at qualification breakpoints (exact enumeration for affine one-dimensional thresholds) or use the certified branch-and-bound (regression test: i with C = 1, Q = 5; j with C = 0, Q = 4; Q_r ∈ — i ∈ K_r via the interior witness Q_r = 4.5, which neither endpoint shows). Feasible witnesses and infeasibility certificates have separate proof obligations, and numerical bounds may not discard feasible points through floating-point error. Statuses: certified / disproved / unresolved / unevaluable, with solver status, depth and witness (or counterexample) stored; an unresolved solve is never shown as certified. Certification grammar (E108): each decision is compiled into (1) primitive domains and the original constraints, (2) a reduced problem obtained only by documented, equivalence-preserving substitutions (definitional equalities are eliminated by substitution wherever possible) and (3) a certificate checked independently against the original problem. Supported v1 classes: boxes, affine constraints decided in exact rational arithmetic on the published decimal inputs, separable monotone transforms and the documented corner reductions; a nonlinear equality is supported only with a validated existence certificate (e.g. a sign change of a continuous univariate function evaluated exactly at rational endpoints); every other class returns unresolved, and a small numerical residual is never a feasibility certificate (fixtures: x² = 2 with x ∈ is certified feasible without a rational witness; x² = 2 with x ∈ [1, 1.4] is certified infeasible; an approximate point with residual 10⁻⁶ certifies nothing). Feasibility prerequisite (E79): before any decision, the decision's full constraint component (all connected shared variables and identities) must have a certified feasible witness checked against the original constraints; certified infeasible → "inconsistent evidence", no frontier or bar labels for the affected output, release-blocking for that output with the conflicting records listed; feasibility unresolved → "unresolved", no confirmed or definite label (fixtures: individually valid intervals whose shared identity has an empty intersection; a feasible outer box whose original constrained set is empty — neither may produce a confirmed, definite or certified-possible result).
0

Final sentence:

A new observed price under an unchanged price rule is a data refresh; changing a rule is a methodology migration; a benchmark-version change triggers a comparability review with dual-run where feasible.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

None.

No new material finding in these two parts survives the stated owner decisions and decision ledger. In particular:

Part 13 explicitly distinguishes stability under published-record reporting precision from benchmark-noise robustness. E337 and E342 also prevent the pointwise noise screen from being represented as either a simultaneous confidence statement or the same target as S1T.

Part 14 makes the constrained evidence set authoritative, requires decision-specific proofs before using box reductions, and prevents unsupported or unresolved feasibility problems from producing certified labels.

The Plan capacity rules distinguish an achievable schedule from an upper bound and a grid optimum from the target optimum. Unidentified reset semantics cannot silently produce an identified workload multiple.

Comparisons disclose their ranked universe, omitted configurations and unevaluated cheaper siblings. The common-leaf headline companion is explicitly diagnostic under the owner’s policy, rather than being presented as equivalent evidence for the leading rankings.

These observations concern the written rules in parts 13–14, not verification that the implementation or rendered outputs satisfy them.

2. Methodology design recommendations

None beyond the designs already adopted and specified in these parts.

I do not recommend reopening the frozen-bar policy, full-utilisation Plan estimand, exact-configuration evidence rule, or separation of reporting precision from benchmark noise. The limitations relevant to this sectional review are already handled through explicit estimands, restricted claim language, diagnostic companions, dependency-aware decision procedures and unresolved statuses.

3. Questions for the owner

None.

4. Verdict

VERDICT: NO FURTHER FEEDBACK