This review evaluates parts 10, 11, and 12 of methodology draft draft-r157.md at commit 0ca7ef5f2a8bafc77b219947fba5723248d9f1c6.

0. Read check
Part 10

First line: - **Specification**: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress. **Deletion branches (E146)**: each registered branch names its removed leaf set R. *Displayed-score deletion sensitivity* removes R globally and renormalises the remaining observed weights, Q̄_i^(−R) = Σ_{b∈O_i∖R} w_b z_ib ÷ Σ_{b∈O_i∖R} w_b (a zero denominator leaves the row unevaluable in the branch, listed), keeping the primary workload, selected route, anchors and cost score; a branch whose retained nominal weight Σ_{b∉R} w_b is under 40% is "not identifiable under the coverage rule" (leave-AA-out today: 34% and 22%); rank changes and τ_b use the common panel (E65). *Evidence unavailability* — the full-composite target with the removed observations replaced by their admissible domains, reported as bounds or convention-dependent scenarios — is a distinct, separately named branch and never shares a deletion branch's name. Registered branches: one per leaf of the ranking (leave-one-benchmark-out), one per multi-leaf source (leave-AA-out, and, under E258, every publisher of two or more independently run leaves in the ranking: leave-Vals-out in the max-effort ranking, LiveBench 2.0 Overall being a single-leaf source since O61, so leave-one-benchmark-out covers it) and the **basket-scope branch (E178)**, which removes jointly the leaves whose benchmarks O15 and O137 exclude from the cost basket as knowledge or science recall (AA-Omniscience, HLE-Diamond, CritPt v2; retained nominal weight 86.7%; GDPval-AA and AA-LCR, which left the basket only because v5 no longer publishes their costs, are kept) and is labelled "quality restricted to the cost basket's scope" (O10 and O15 are unchanged: the scored quality vector stays general); a single-leaf source (Bug Hunt Bench; LiveBench 2.0 Overall in the max-effort ranking; AI Coding Daily in its ranking) coincides with its leaf's branch, which carries both labels, and the Bug Hunt branch is the standing Bug Hunt removal. **Standing cost-component removal (E64, defined by E149)**: a cost-deletion object D_cost = (R_C, W∖R_C, anchor policy, route policy, multiple policy, panel rule), separate from quality deletion; R_C names execution components, not quality leaves. The standing column removes AA's Index-run Terminal-Bench 4.0 (the Coding Agent Index also executes Terminal-Bench v4) and publishes two named calculations on the main-workload panel, each compared with the primary ranks on the common panel (E65) with quality held at Q̄_i: (a) *cost-component removal, original anchors* — C_i^(−TB) = C_i,W − C_i,TB scored on the original anchor object A_W, V = 0.25·S_C(C_i^(−TB); A_W) + 0.75·Q̄_i (a sensitivity of the published scoring scale); (b) *alternative workload, recalibrated anchors* — W∖TB scored on anchors rebuilt with the ln 2 padding from every row with a cost on W∖TB, with the new exchange rate published beside the rank changes so cost-composition and recalibration effects can be told apart. On the Plan basis each row keeps its selected route and displayed multiple, labelled "fixed-multiple arithmetic stress (not identified Plan economics for the altered workload)"; **basis typing (E152)**: with A_i the API basket cost, m_i the selected displayed multiple and P_i = A_i / m_i, the removal subtracts the API component cost before dividing — A_i^(−TB) = A_i − A_i,TB is scored only against API anchors and P_i^(−TB) = (A_i − A_i,TB) / m_i only against Plan anchors, in both calculations (fixture: A = 100, A_TB = 20, m = 4 gives P = 25 and P^(−TB) = 20 — never 25 − 20 = 5, never 80 against Plan anchors); API-fallback rows take P_i^(−TB) = A_i^(−TB), as on the primary workload; an M_W identified for W is reused for W∖TB only when its identification mechanism also covers W∖TB. **Leave-one-component-out cost family (E172)**: the same D_cost object, with both named calculations and basis typing, is registered once per admitted basket unit (O15's admission units, E148; the Coding Agent Index is one unit) and published per basis as rank changes on the common panel with each recalibrated exchange rate; with the matched-cost diagnostic (quality-weighted complete passes) and the per-row expenditure shares (E22), it shows how far the ranking depends on AA's task multiplicities, which O15 fixes for the scored workload. No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

Last 12 words: of both rankings has a cost, so the two ladders are equal.

Part 11

First line: - **Noise-margin companion (owner decision O44, kept over a per-candidate margin as O128, 2026-10-30)**: because each bar is a configuration's own displayed quality (O34), the cheapest row at a bar can be its setter, an answer a 0.01-point move could change. Beside each bar's displayed-record result the summary therefore names the cheapest configuration whose displayed quality clears the bar by at least the quality noise margin (or says none, when no configuration clears the bar by that much), 1.96 × √2 × the median, over the ranking's configurations (one value each, the same on both bases), of the analytic quality SD (the same per-row SD, before the 0.75 scaling, that the separability threshold uses). The margin is today 3.5 quality points in the max-effort ranking and 5.6 in the AI Coding Daily ranking; it is on the quality scale, so it is about 1/0.75 times the separability threshold, which is on the value scale where quality carries 75%. The companions are printed beside the bar results (scores.json displayedCheapest.<basis>.bars[].margin). The frozen bars are unchanged. A result whose cheapest row changes when the gap fills are removed or lowered (E234) is marked fill-sensitive beside it. **Displayed-record cheapest (E203)**: for each bar and basis, the published summary also names the lowest-cost scored, non-provisional main-workload row whose displayed quality reaches the bar, with ties listed and the number of rows that reach it, labelled "displayed record on the headline scale, not a claim". It adds no evidence and never replaces the interval and scenario labels, which remain the claim. Each release prints these results with the cheapest row's cost and the number of rows that reach the bar (scores.json displayedCheapest). Their reach counts main-workload rows only, so in a ranking with a subset workload they can be lower than bar currency's (E207).

Last 12 words: Bug Hunt and AI Coding Daily name the harness on each record).

Part 12

First line: - **Target-basket readiness (E22, diagnostic).** Per target component: inclusion status, missing configurations, task multiplicity, cost availability, priced quality weight. Per scored model: expenditure share s_ie = n_e c_ie / C_i,W per component and concentration HHI_i = Σ_e s_ie². A **task-family overlap matrix** (E42) accompanies it (e.g. Terminal-Bench inside both the Index run and the Coding Agent Index); family-level concentration is "unidentified" where aggregate costs cannot be separated. No single unlabelled coverage percentage.

Last 12 words: or definite result; every cost check reads C_W, never the Index diagnostic.

1. Findings by severity
Critical

None

High

Frontier eligibility contradiction between Part 10 and Part 11

Issue: Part 10 defines 
𝑅
𝑊
R
W
	​

 as cohort rows with FullCost and restricts 
𝐵
𝑊
B
W
	​

 strictly to superseded-price rows (O29) and pricing-omission rows (O94), stating that frontier labels are awarded over 
𝑅
𝑊
R
W
	​

. However, Part 11 establishes a unified eligibility predicate UniqueLabelEligible(i) = i is a bar competitor ∧ ¬provisional(i) ∧ ¬blocker(i), which explicitly defines blockers to include unverified valuation bases (E222), provider-claimed leaves (E233), and superseded Plan routes (E228). Part 11 states this predicate is used for frontier labels as well. Under Part 10's verbatim formula, a configuration with a provider-claimed leaf (such as MiMo-V2.6-Pro under E233) or unverified basis (E222) that has FullCost remains in 
𝑅
𝑊
R
W
	​

 and would receive a Definite or Possible Frontier label.

Why it hurts the objective: Directly violates the owner decision and decision ledger policy (E233, E222) that provider-claimed and unverified-basis configurations can block other models but must never earn official frontier labels.

Concrete change: Align Part 10's formal frontier definitions with Part 11 by defining 
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

 where 
𝐵
𝑊
B
W
	​

 holds all rows matching blocker(i), and explicitly condition both DefiniteFrontier(i) and PossibleFrontier(i) on 
𝑖
∈
𝑅
𝑊
∖
𝐵
𝑊
i∈R
W
	​

∖B
W
	​

 (or 
𝑖
∈
𝑅
𝑊
∧
¬
blocker
(
𝑖
)
i∈R
W
	​

∧¬blocker(i)).

Medium

Inconsistent bar population and reach figures for the max-effort ranking in Part 10

Issue: Part 10 states under Bar currency (E207) that "Today 4, 3 and 2 of the max-effort ranking's 5 rows reach its lower, headline and upper bars", while the max-effort ranking contains 9 ranked configurations and the ladder fixture in the same section explicitly establishes 
𝑛
=
9
n=9 (yielding zero-based positions 2, 4, and 6). E243 specifically dictates that the bar population keeps all full-benchmark configurations regardless of cost completeness because cost is not a quality fact. If the bar population was 
𝑛
=
5
n=5, the quartile positions would evaluate to 1, 2, and 3 (yielding the 4, 3, 2 reach counts), which conflicts with 
𝑛
=
9
n=9 (where reach would be 7, 5, 3).

Why it hurts the objective: Conflates the quality-only bar population with 
𝑅
𝑊
R
W
	​

 cost-complete subsets, misstates the current reach of frozen bars, and obscures whether configurations were improperly omitted from the quartile ladder.

Concrete change: Reconcile the text in Part 10 to reflect the true bar population 
𝑛
=
9
n=9 for the max-effort ranking with positions 2, 4, 6 and reach 7, 5, 3; or explicitly document the 4 excluded configurations if they were classified as provisional.

Stale static retained weight in the basket-scope quality branch (E178) in Part 10

Issue: Part 10 specifies a single retained nominal weight of 86.7% for the basket-scope branch (E178), which jointly removes AA-Omniscience, HLE-Diamond, and CritPt v2. While leave-AA-out correctly publishes separate figures for both rankings (34% and 22%), E178 presents a single legacy figure from before the dual-ranking architecture (O53) and subsequent weight recalibrations (O55, O61, O136).

Why it hurts the objective: The two active rankings have completely different leaf tables and weights (max-effort has 60% coding across six leaves; AI Coding Daily has 60% across four leaves). A single static 86.7% figure is mathematically impossible for both and misleads users evaluating non-SDLC recall sensitivity.

Concrete change: Update Part 10 to specify the retained nominal quality weight dynamically or list both distinct values per ranking (e.g. max-effort and AI Coding Daily) alongside the leave-AA-out disclosures.

Low

Extrapolation of Terminal-Bench cross-agent spread to Bug Hunt in Part 11

Issue: Part 11 states that the S2 harness-mismatch band applied to Bug Hunt is estimated from same-model cross-agent spreads on the tbench.ai leaderboard, despite Bug Hunt having actual published cross-harness evaluation data (e.g. Gemini 4 Argon scoring 40.7 vs 33.0, documented in E224).

Why it hurts the objective: Software-engineering agent scaffolding variance from Terminal-Bench does not reflect the mechanics or error distribution of Bug Hunt's direct CLI test-debugging harness.

Concrete change: Parameterize Bug Hunt's harness stress branch using the empirical cross-harness spread documented in E224 instead of borrowing tbench.ai agent distributions.

Ambiguous BlockerSafe solver status reporting in Part 11

Issue: Part 11 states that when BlockerSafe fails, "otherwise the frequency is published with the reading 'scenario frequency passes; blocker unresolved' (whichever blocker kind it is) and no label".

Why it hurts the objective: Conflates an inconclusive solve (e.g. search depth timeout or missing price tariff) with a certified counterexample where a blocker is proven to qualify and undercut the candidate.

Concrete change: Distinguish between "denied by blocker" (when the solver certifies a blocker witness state) and "blocker unresolved" (reserved for timeouts, incomplete domains, or unpriced categories).

Missing default time zone in Plan workday calendar specification in Part 11

Issue: Part 11 specifies a 40-hour week from a versioned calendar with IANA time zone handling, but does not define the governing reference time zone.

Why it hurts the objective: Plans with fixed-reset cycles (such as weekly reset phases) intersect differently with a 40-hour working window depending on whether the calendar evaluates in UTC or US Pacific time.

Concrete change: Explicitly record the governing time zone convention in the calendar specification (e.g. defaulting to provider billing reset time zone or UTC).

2. Methodology design recommendations

Explicit blocker set in competitor compilation
Define 
𝐵
𝑊
B
W
	​

 universally across Part 10 and Part 11 as the set of all cohort rows satisfying blocker(i) under E92, E183, E222, E228, and E233. Update the candidate sets for interval outputs such that any label candidate 
𝑖
i must satisfy 
𝑖
∈
𝑅
𝑊
∖
𝐵
𝑊
i∈R
W
	​

∖B
W
	​

, while competitors range over 
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

. This cleanly prevents provider-claimed, unverified-tariff, or superseded-route rows from receiving frontier or cheapest-above-bar labels while preserving their full capacity to block invalid claims.

Per-ranking dynamic branch metadata
Replace static textual percentages in sensitivity branch definitions with a formal tuple (nominal_retained_weight, observed_panel_size, rank_tau) computed and rendered per ranking. In particular, the basket-scope branch (E178) and leave-one-source-out branches should publish distinct metadata objects