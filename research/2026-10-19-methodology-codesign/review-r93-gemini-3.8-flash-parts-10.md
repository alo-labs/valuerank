0. Read check
Part 10

First line: - **Specification**: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress. **Deletion branches (E146)**: each registered branch names its removed leaf set R. *Displayed-score deletion sensitivity* removes R globally and renormalises the remaining observed weights, Q̄_i^(−R) = Σ_{b∈O_i∖R} w_b z_ib ÷ Σ_{b∈O_i∖R} w_b (a zero denominator leaves the row unevaluable in the branch, listed), keeping the primary workload, selected route, anchors and cost score; a branch whose retained nominal weight Σ_{b∉R} w_b is under 40% is "not identifiable under the coverage rule" (leave-AA-out today: 34% and 22%); rank changes and τ_b use the common panel (E65). *Evidence unavailability* — the full-composite target with the removed observations replaced by their admissible domains, reported as bounds or convention-dependent scenarios — is a distinct, separately named branch and never shares a deletion branch's name. Registered branches: one per leaf of the ranking (leave-one-benchmark-out), one per multi-leaf source (leave-AA-out, and, under E258, every publisher of two or more independently run leaves in the ranking: leave-Vals-out in the max-effort ranking, LiveBench 2.0 Overall being a single-leaf source since O61, so leave-one-benchmark-out covers it) and the **basket-scope branch (E178)**, which removes jointly the leaves whose benchmarks O15 and O137 exclude from the cost basket as knowledge or science recall (AA-Omniscience, HLE-Diamond, CritPt v2; retained nominal weight 86.7%, the same in every ranking because these leaves carry the same weights in each; GDPval-AA and AA-LCR, which left the basket only because v5 no longer publishes their costs, are kept) and is labelled "recall/science-leaf removal sensitivity": it is not an execution-matched quality–cost comparison, which is the matched-cost diagnostic's question (E327, on reviewer 88; O10 and O15 are unchanged: the scored quality vector stays general); a single-leaf source (Bug Hunt Bench; LiveBench 2.0 Overall in the max-effort ranking; AI Coding Daily in its ranking) coincides with its leaf's branch, which carries both labels, and the Bug Hunt branch is the standing Bug Hunt removal. **Standing cost-component removal (E64, defined by E149)**: a cost-deletion object D_cost = (R_C, W∖R_C, anchor policy, route policy, multiple policy, panel rule), separate from quality deletion; R_C names execution components, not quality leaves. The standing column removes AA's Index-run Terminal-Bench 4.0 (the Coding Agent Index also executes Terminal-Bench v4) and publishes two named calculations on the main-workload panel, each compared with the primary ranks on the common panel (E65) with quality held at Q̄_i: (a) *cost-component removal, original anchors* — C_i^(−TB) = C_i,W − C_i,TB scored on the original anchor object A_W, V = 0.25·S_C(C_i^(−TB); A_W) + 0.75·Q̄_i (a sensitivity of the published scoring scale); (b) *alternative workload, recalibrated anchors* — W∖TB scored on anchors rebuilt with the ln 2 padding from the registered anchor population on W∖TB (E160 and E184's eligibility evaluated on the reduced workload; on the Plan basis its measured rows only, O157), its reference and excluded ids published, and the calculation reported unavailable when fewer than two references qualify (E317, on reviewer 84), with the new exchange rate published beside the rank changes so cost-composition and recalibration effects can be told apart. On the Plan basis each row keeps its selected route and displayed multiple, labelled "fixed-multiple arithmetic stress (not identified Plan economics for the altered workload)"; **basis typing (E152)**: with A_i the API basket cost, m_i the selected displayed multiple and P_i = A_i / m_i, the removal subtracts the API component cost before dividing — A_i^(−TB) = A_i − A_i,TB is scored only against API anchors and P_i^(−TB) = (A_i − A_i,TB) / m_i only against Plan anchors, in both calculations (fixture: A = 100, A_TB = 20, m = 4 gives P = 25 and P^(−TB) = 20 — never 25 − 20 = 5, never 80 against Plan anchors); API-fallback rows take P_i^(−TB) = A_i^(−TB), as on the primary workload; an M_W identified for W is reused for W∖TB only when its identification mechanism also covers W∖TB. **Leave-one-component-out cost family (E172)**: the same D_cost object, with both named calculations and basis typing, is registered once per admitted basket unit (O15's admission units, E148; the Coding Agent Index is one unit) and published per basis as rank changes on the common panel with each recalibrated exchange rate; with the matched-cost diagnostic (quality-weighted complete passes) and the per-row expenditure shares (E22), it shows how far the ranking depends on AA's task multiplicities, which O15 fixes for the scored workload. No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

Last 12 words: ordered by displayed quality ascending, then configuration ID.

Part 11

First line: - **Ladder positions (O34)**: with the population's n displayed qualities in ascending order, bar level H_k (k = 1, 2, 3; H = H_2, the headline bar; renamed from Q̄ in r70 so it is not confused with a row's displayed quality Q̄_i) is the value at zero-based position floor((n − 1)k/4), an element of the order, never an interpolated percentile. k = 2 is the headline bar H, which is the ⌈n/2⌉-th value for odd and even n; k = 1 and k = 3 are the lower and upper quartile bars. The policy object records order = ascending and position = floor((n − 1)k/4) for each bar, and the bars are published in the order k = 2, 1, 3. All three are frozen together, from the same population, with the anchor version. Fixtures: n = 32 gives the 8th, 16th and 24th ascending values (zero-based 7, 15 and 23); n = 9 gives zero-based 2, 4 and 6, and n = 15 gives 3, 7 and 10. At the 2026-10-21 pre-release re-freezes (O30, O31, O34, O33 and O36 changed the cohort or the policy), the population has 32 configurations and the ladder is 47.36 (GPT-6 Luna), 55.31 (Claude Sonnet 5.5 (high), headline) and 59.56 (GPT-6.1 Sol (high)). O30, O31, O34 and O36 left the anchor values unchanged. O33 added cheaper efforts, which lowered the low anchors (API $66.43 to $35.76, Plan $2.48 to $0.61; 29 references at O36); the high anchors were unchanged. All dual runs are kept in the research record. No release had been published, so the anchor version string stayed v3-2026-10-21. At the 2026-10-23 re-freezes at O53 (O47, E247, then one object per ranking, E253) E247's ladder over the 27 ranked configurations before O53 (32.26, 48.92 with GPT-6.1 Sol (medium) as headline, 54.99) was replaced before any release by one ladder per ranking; O61 then changed the max-effort ranking's leaves and re-froze its bars on the same anchor version (its cost anchors are unchanged, because they do not depend on quality). The current ladders are in Output 3 and scores.json barCurrency.

Last 12 words: compare ranked configurations only and names the listed configurations.

Part 12

First line: - **Interval decision procedure (E40, amended by E43).** Interval labels are decided by deterministic, decision-specific feasibility problems over Θ, never from scenario draws. Primitive domains have a box enclosure (per-row input boxes and a box of declared shared factors, e.g. a common price list or a donor multiple shared by several rows); Θ itself is the constrained subset defined by E73, and a product-box representation may replace it only under a decision-specific equivalence proof (E169). **Constrained evidence model (E73)**: the primitive-variable constraint graph Θ = {v : ℓ ≤ v ≤ u, h(v) = 0, g(v) ≤ 0} is authoritative; costs, quality, capacities and multiples are derived quantities of v (an identity such as API-valued capacity = λ × C_API survives uncertainty propagation). A box reduction is used only with a decision-specific equivalence proof; otherwise the box is an outer enclosure for pruning, and every witness is certified against the original constraints (release fixture: an enclosing box containing a favourable state the original constraints exclude must never return a certified possible membership). **Separability condition (E89)**: with no shared factor **and no row-local coupling** — each row's C and Q depend on disjoint primitives with no joint constraint, so the row's feasible set is the product of its C and Q ranges — each label is decided exactly by monotone extremes (Q is linear in leaf values; basket cost is monotone in component costs; each row's inputs move only its own C and Q): e.g. possible-frontier membership of i is established by setting i to its best corner and every j to its worst. A row-local primitive or constraint that enters both C_i and Q_i is a coupled variable and is branched over like a shared factor; a constraint class the solver does not support returns unresolved (release test: i with C_i = 1 + t, Q_i = t, t ∈ [0, 1]; j with C = 1, Q = 0.5; k with C = 1.5, Q = 1 — i is dominated for every t although its box corner (1, 1) is undominated, so the solver must return disproved and never a possible membership). In v1 every row's C and Q come from distinct published records, so the condition holds and is asserted per release. **Shared price factors (E276)**: two rows can still share a cost factor, through one model's price list (two efforts of one model, including a superseded tariff's hull, E183) or one registered pricing omission (O94, O98); such a factor moves the rows' costs together, never against each other. A row carrying one is a blocker that competes and never earns a label (E183, E186, O94), and the factor covers every effort of its model, so a candidate never shares it; the possible-frontier and bar tests set every competitor at one common extreme (all at their worst corners, or all at their best), a state the shared factor permits, and the definite test moves one competitor at a time, so the per-row boxes give the same answers as the joint constraint; the one cross-row factor the Plan basis can create, a donor multiple shared by several configurations, is checked by the build: when two configurations among the rows a decision reads (its Plan candidates, competitors and the blockers B_W of U_W = R_W ∪ B_W, E313 on reviewer 83) rest on one donor multiple identified only as a range, the Plan interval outputs are unresolved, with the shared donor named, and never computed by corners (E273). With shared factors or row-local coupling, labels are decided by **certified interval branch-and-bound** over the shared-factor box: on each sub-box, interval bounds either certify the condition for every point (witness), refute it for every point (prune), or the sub-box is split, up to a published depth; a sub-box still undecided at that depth returns **unresolved**. Endpoint search alone is not sufficient (release test: competitors with Q_j = 2t and Q_k = 2(1 − t), C_j = C_k = 0, and i with C_i = 1, Q_i = 1.2: i is a possible-frontier member via the interior witness t = 0.5). Possible-frontier membership solves, in one common θ, for every j ≠ i: C_j(θ) > C_i(θ) ∨ Q_j(θ) < Q_i(θ) ∨ [C_j(θ) = C_i(θ) ∧ Q_j(θ) = Q_i(θ)]; definite membership is disproved by one θ and one dominating j; strict inequalities are decided exactly, never by tolerance alone. Every returned witness is re-checked against the original equations and shared constraints. The monotone-corner shortcut is used only for decisions with a documented corner-reduction proof; dependencies are compiled from the complete decision equations, so a varying reference quality Q_r is a shared variable for every qualification condition even when all row inputs are independent (E50; a frozen bar level is a constant and adds no shared variable, but the rule binds any registered varying reference): bar decisions partition at qualification breakpoints (exact enumeration for affine one-dimensional thresholds) or use the certified branch-and-bound (regression test: i with C = 1, Q = 5; j with C = 0, Q = 4; Q_r ∈ [0, 10] — i ∈ K_r via the interior witness Q_r = 4.5, which neither endpoint shows). Feasible witnesses and infeasibility certificates have separate proof obligations, and numerical bounds may not discard feasible points through floating-point error. Statuses: certified / disproved / unresolved / unevaluable, with solver status, depth and witness (or counterexample) stored; an unresolved solve is never shown as certified. **Certification grammar (E108)**: each decision is compiled into (1) primitive domains and the original constraints, (2) a reduced problem obtained only by documented, equivalence-preserving substitutions (definitional equalities are eliminated by substitution wherever possible) and (3) a certificate checked independently against the original problem. Supported v1 classes: boxes, affine constraints decided in exact rational arithmetic on the published decimal inputs, separable monotone transforms and the documented corner reductions; a nonlinear equality is supported only with a validated existence certificate (e.g. a sign change of a continuous univariate function evaluated exactly at rational endpoints); every other class returns unresolved, and a small numerical residual is never a feasibility certificate (fixtures: x² = 2 with x ∈ [1, 2] is certified feasible without a rational witness; x² = 2 with x ∈ [1, 1.4] is certified infeasible; an approximate point with residual 10⁻⁶ certifies nothing). **Feasibility prerequisite (E79)**: before any decision, the decision's full constraint component (all connected shared variables and identities) must have a certified feasible witness checked against the original constraints; certified infeasible → "inconsistent evidence", no frontier or bar labels for the affected output, release-blocking for that output with the conflicting records listed; feasibility unresolved → "unresolved", no confirmed or definite label (fixtures: individually valid intervals whose shared identity has an empty intersection; a feasible outer box whose original constrained set is empty — neither may produce a confirmed, definite or certified-possible result).

Last 12 words: widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic.

1. Findings by severity
Critical

None.

High

None.

Medium

Inconsistent missing-leaf composite upper bound text under unbounded Bug Hunt z-score

Issue: In Part 10 under Coverage and scores, the draft states: "The weights are therefore coefficients, not maximum contributions, and a composite can exceed 100 (with every leaf missing, its formal upper bound is 100 + w_BugHunt × 1.1)." Under E302, Bug Hunt's missing-evidence domain $u$ is explicitly registered as $$ ($105 \text{ planted} + 105 \text{ unplanted}$). With weights expressed in percentage points summing to 100 and scaled by $1/100$, if every other leaf is at 100 and Bug Hunt is at 210, the maximum possible composite score is:[0][210]

∑
𝑏
≠
BH
𝑤
𝑏
×
100
+
𝑤
BH
×
210
100
=
(
100
−
𝑤
BH
)
×
100
+
𝑤
BH
×
210
100
=
100
+
𝑤
BH
×
1.10
100
∑
b

=BH
	​

w
b
	​

×100+w
BH
	​

×210
	​

=
100
(100−w
BH
	​

)×100+w
BH
	​

×210
	​

=100+w
BH
	​

×1.10
However, the text parenthetical writes "with every leaf missing, its formal upper bound is $100 + w_{\text{BugHunt}} \times 1.1$". If every leaf were missing and evaluated at its lower bound (or if missing leaves are bounded on $$), this expression represents the maximal theoretical upper bound when all ordinary leaves achieve 100 and Bug Hunt reaches 210, not when "every leaf is missing" (which at $u=0$ would be 0).[0][100]

Why it hurts the objective: In an executable normative specification, stating that the upper bound with "every leaf missing" is $100 + w_{\text{BugHunt}} \times 1.1$ creates an ambiguity between the maximal theoretical composite bound over all valid states versus the bound where missing leaves take zero or their full intervals.

Recommended change: Amend the parenthetical to clarify: "(the formal maximum upper bound across all leaves at their maximal domain points is $100 + w_{\text{BugHunt}} \times 1.1$)".

Missing edge-case specification for what would settle a row ($u^$) when Bug Hunt is among missing leaves

Issue: In Part 11 under What would settle a row (E221), the formula is given as $u^* = (100 \cdot H - \Sigma_{\text{observed}} w \cdot z) / \Sigma_{\text{missing}} w$. The draft specifies that $u^*$ represents the mean score the missing leaves would need. However, because ordinary leaves are bounded in $$ while Bug Hunt can attain up to 210 (E302), a required mean score $u^* \in (100, 210]$ is attainable only if Bug Hunt is in the missing set, whereas if Bug Hunt is already observed and ordinary leaves are missing, any $u^* > 100$ is structurally unattainable.[0][100]

Why it hurts the objective: An automated report reader or auditor interpreting $u^*$ as a feasible required average score could encounter values above 100 without knowing whether the missing subset can mathematically attain that average.

Recommended change: In E221, specify that when $u^* > 100$, the summary flags whether the missing set contains Bug Hunt (making $u^* \le 100 + w_{\text{BugHunt}} \times 1.1 / \Sigma_{\text{missing}} w$ feasible) or whether $H$ is structurally unattainable given the observed leaves.

Low

Implicit ceiling in $u^$ notation when weights are fractional

Issue: In Part 11, the formula $u^* = (100 \cdot H - \Sigma_{\text{observed}} w \cdot z) / \Sigma_{\text{missing}} w$ explicitly assumes weights $w$ sum to 100. The alternative general form $u^* = (H \cdot \Sigma_{\text{all}} w - \Sigma_{\text{observed}} w \cdot z) / \Sigma_{\text{missing}} w$ is noted. When $u^* < 0$, the row already qualifies at zero performance on missing leaves.

Why it hurts the objective: Minor clarity gap; an automated parser could display a negative required score $u^*$ for a candidate whose observed leaves already guarantee clearing $H$.

Recommended change: Explicitly clamp or note: "for rows where observed leaves already guarantee qualification, $u^*$ is reported as 0 (or 'already qualified')".

2. Methodology design recommendations

Explicit Feasibility Check for $u^$ in E221:

For any row open on missing leaves, compute both the scalar $u^$ and the indicator $\text{isFeasible}(u^) = [u^* \le \max_{b \in \text{missing}} \text{dom}(u_b)]$. When Bug Hunt is observed, the maximum attainable average of missing leaves is strictly 100.

Harmonise Upper Bound Formulation in Normative Definitions:

Rephrase Part 10's composite score upper bound text to strictly delineate the maximum domain bound ($Q_i^U \le 100 + 1.10 \cdot w_{\text{BH}}$) from missing-leaf scenario defaults.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK