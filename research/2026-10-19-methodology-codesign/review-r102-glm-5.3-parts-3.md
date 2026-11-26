0. Read check

Both listed parts were opened through the GitHub connector at commit 5c2ab13991d61e5a15c418407e9c9e95db001918 and read to their ends. This review covers only those two parts.

Part 3

First line:

Configuration rule (E188, amended by E193 and E251): a family is AA's model identity, the plotted model name without its effort and fallback qualifiers; it must equal the selected catalog model's display name, and MiMo-V2.6-Pro and MiMo-V2.6-Flash are separate families. Every plotted on/near configuration is its own row (O51): each effort AA plots on the rendered frontier or within the near gap is a cohort row, ranked in every ranking whose full set it has; nothing is chosen among a family's efforts, and a configuration is never replaced by another effort. Family primary (E193, E251): the family rule only chooses each family's primary configuration, which the reconciliation gate checks and the one-row-per-family diagnostics use. A frontier family's primary is its highest point on the rendered frontier; along the strictly rising rendered line (E195) that point is also the dearest of the family's rendered-frontier points, so a rounded-Index tie never decides it (a near point of the family can cost more; today Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max), GPT-6 Luna (xhigh), GPT-6.1 Terra (max) and GPT-6.1 Terra (xhigh)). A near family (one with no point on the rendered frontier) has as its primary its plotted near point with the smallest Index gap to the rendered frontier at its cost, then the lower total cost, then the name (today Claude Sonnet 5.5 (max) at gap 3); a near family's other near points (today none) are cohort rows, not primaries. A frontier family's near points (today Claude Opus 5.5 (high), Claude Opus 5.5 (max), GPT-6 Astra (max), GPT-6 Luna (max), GPT-6 Luna (xhigh), GPT-6.1 Sol (low), GPT-6.1 Terra (max) and GPT-6.1 Terra (xhigh)) are cohort rows like any other plotted effort, never primaries; together these are the 9 near points. The reconciliation gate checks a family with both frontier and near points under both rules; the one-row-per-family diagnostics take its frontier point. O30's evidence-first choice for a near family (its effort with exact DeepSWE and Bug Hunt results) has no object since O49 dropped DeepSWE and O51 ranks every plotted near effort, so E251 uses E193's rule. Selection precedes the benchmark check (O36, O38): a primary is selected by these rules alone; when it then lacks a leaf of every ranking after the logged search it is listed under O38, never replaced by another effort, and the reconciliation gate accepts it without a roster decision because it is in the roster. Every row carries the tier of its own plotted point. The specification names a row "Family (effort)"; the published tables use the roster's display name, which names every configuration of a family with several cohort configurations with its effort (e.g. GPT-6 Luna (max)) and keeps the bare family name for a family with one (e.g. Claude Sonnet 5.5, MiMo-V2.6-Flash), and the build requires display names to be unique. Fallback (E214): the "with fallback" qualifier names AA's serving setting rather than a second configuration. Today AA plots Claude Opus 5.5 and Claude Sonnet 5.5 only "with fallback" and every other cohort family without it; the build reads this from the capture and prints it with the cohort (scores.json aaPlottedNames, which also lists the families plotted with no effort, today MiMo-V2.6-Flash), so the statement cannot go stale; a third-party record (Bug Hunt, tbench.ai, Vals, LiveBench, AI Coding Daily) that states no fallback matches by model and effort; a record whose explicit fallback state differs from AA's ("without fallback" for a model AA plots only with it, or "with fallback" for one AA plots only without it) does not match until a dated matching decision says it does, in either direction. The build fails if AA ever plots the same model and effort both with and without fallback, until a dated matching decision says which configuration such a record belongs to (otherwise the leaf would be missing for the fallback-qualified one), and row names then carry the fallback token. The build fails when a cohort configuration is missing from the roster. A family's plotted configurations outside the frontier and the near gap stay in the reconciliation inventory with their AA Index and total cost, unscored; manifest records model/version, effort, fallback, and per-benchmark harness/tool limits. Exact-variant evidence only; harness differences shown as separate stack evidence. Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

Final sentence:

Both priced executions stay in the basket as the owner listed them; the overlap is disclosed.

Part 4

First line:

Admission and persistence (E26). A component is admitted to workload version W when exact-configuration cost exists for every configuration in W's frozen, named reference panel, published with W and containing at least two-thirds of the cohort rows at admission; until admitted it is listed as "pending capture". Panel construction (E95, selection by E140): one panel per workload version, built deterministically before scores or ranks are inspected. With P(S) = the cohort rows with complete cost evidence (CompleteCostEvidence, E37 as set by O27: exact cost and no AA missing- or declined-task marker) on every component of S (E101), the admitted set is chosen by enumerating every subset S of the target components (2ⁿ subsets of the n targets; admission units, E148: the units are exactly the named targets of O15 as amended by O50 and O137, eight since the v5 basket (the six Index SDLC evaluations, the Coding Agent Index v2.0 and ITBench-AA; O137 retired O116's FrontierCode stand-in), each counted once whatever its accounting representation — the Coding Agent Index is one unit, not its three sub-benchmarks; a unit's complete evidence enters only at unit level, as an accepted aggregate or a complete compatible decomposition first composed by the accounting tree, so K_iu is identical under either representation; raw accounting children never enter admission and the build rejects any component outside the unit registry; adding a unit is a basket-version migration; fixture: N = 6, unit A complete on rows 1–4, units B and C on rows 3–6 — B + C is admitted, and A presented as its sub-benchmarks is rejected rather than counted as three units) with |P(S)| ≥ ⌈2N/3⌉ and maximising, lexicographically, the number of admitted components (O15 lists them without priorities), then |P(S)|, then the earliest components in the published target order; P(S) of the selected set is the reference panel, and the selected subset, its objective tuple and the feasible alternatives are published (fixture: components A on rows 1–5 and B and C each on rows 1, 2, 3, 6 with N = 6 — a greedy coverage order admits only A, enumeration admits B and C). This replaces E95's greedy coverage order; the 2026-10-19 outcome was eight components on a 16-row panel and the 2026-10-21 outcome the same eight on a 29-row panel (cohort of 32). Per-ranking admission (E254, applying E140 under O53; owner decision O57): admission is decided within each ranking's cohort rows, so N, the reference panel, the admitted set and the workload are each ranking's own. Today the max-effort ranking admits 7 components (the six Index SDLC evaluations and the Coding Agent Index v2.0, priced for 8 of its 9 rows against a threshold of 6) on a reference panel of 8 rows, with 127 feasible alternatives; the AI Coding Daily ranking admits 6 on a reference panel of 20 rows (threshold 14), with 63 feasible alternatives, and the Coding Agent Index v2.0 (7 of 20) stays pending, so the O50 migration is deferred there, not forced (E184). Two public matrices are published per release, A_ie = exact compatible cost available and K_ie = CompleteCostEvidence(i, e), with both joint panels P_A(W) and P_K(W); only P_K is called complete. One status scale (E209): each (row, component) cost has exactly one status — confirmed complete (K_ie = 1), unresolved (published, but the Index reconstruction fails), confirmed incomplete (AA's missing- or declined-task marker) or missing (A_ie = 0). Only confirmed complete enters K_ie, P_K and the admission panel. Admission is decided at a freeze and is otherwise frozen (owner decision O169, 2026-11-01, on reviewer 92, replacing E333's between-freeze test): an admitted component stays in W until the next re-freeze whatever its coverage does meanwhile, whether entrants lack its cost or an incumbent's reconstruction starts failing, so no between-freeze denominator exists and the order in which records are processed cannot matter; a component's published-but-unresolved or confirmed-incomplete cost stays in the row's displayed W cost with W's anchors (the row loses FullCost and interval eligibility, E209), and only a missing published cost makes the row a subset row (O17); a frozen component below the two-thirds threshold at a refresh is published (scores.json frozenBelowThreshold, manifest rule "frozen admission (O169)") and its coverage is re-tested at the next freeze; only a newly admissible component whose workload can be anchored is a migration (E184). Anchor eligibility is K on every admitted component and an E170 outcome of 1 or 2, two separate tests; a row can fail either; a row whose AA cost omits a pricing term (O94) is eligible until the next freeze, which leaves it out, so the diagnostics that rebuild anchors by this rule (E187, E205) keep it until then (E64 and E172 rebuild anchors from this population recomputed on the reduced workload, measured rows only on Plan, E317, so they keep it too) and their effects stay separable. Since O175 the Claude Opus 5.5 rows, whose Index reconstruction misses AA's total by at most 0.04%, are complete, so in each ranking the main workload's admission panel holds 8 of 8 and 20 of 20 main-workload rows; the frozen a4 anchor references were set while those rows were unresolved, so they stay out of the anchor references until the next versioned re-freeze (on reviewer 98). Scored on W (E209): a row is scored on W, with W's anchors, when every admitted component has a published cost, whatever its status; FullCost additionally needs every component confirmed complete. A row with an unresolved or confirmed-incomplete component is flagged "partial component" (E37), is counted in that anchor object's clip-gate n and in the common-workload panel, and stays out of R_W, P_K and the anchor references. Today none (max-effort ranking) and none (AI Coding Daily ranking) are in that state. The admission object (workload version, selection rule, timestamp, configuration IDs, ranked cohort size, required panel size, admitted components, complete-on-all-components IDs) is published, with marginal coverage per component and joint full-basket coverage side by side (fixtures: two components that each pass alone but not together — the higher-coverage one is admitted, the other stays pending; two-thirds of rows with exact costs, some carrying AA's declined-task marker — the component is admitted only if the unmarked rows reach two-thirds). Once admitted, membership is frozen for W. Later missingness (a new cohort row, withdrawn evidence) invokes O17/E10 subset scoring for that row without changing W or its hash, and an unresolved published cost keeps the row on W (E209); adding cohort rows never invalidates an admission (O169). The target-basket readiness table (E22) is published each release. Total Index cost and USD per Index point remain diagnostics.

Final sentence:

These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status.

Source note: The GitHub connector returned the complete file texts and file SHAs, but no citation identifiers. Section and rule references below identify the reviewed passages without inventing citation tokens.

1. Findings by severity
Critical

None.

High

None.

Medium

The fallback re-pricing sensitivity silently substitutes attempt share for expenditure share. Issue: Part 3, “Accounting identities,” describes O158 as moving “the Coding Agent Index cost's fallback share, taken by attempts” from fallback-model prices to the ranked model’s prices. The available attempt counts identify the fraction of attempts involving fallback, not the fraction of the pooled dollar cost attributable to those attempts. The calculation therefore introduces an equal-average-cost-per-attempt assumption without stating it. Why it hurts the objective: This diagnostic is intended to show whether fallback execution materially affects a model’s apparent API value. Its reported movement can be understated or overstated if fallback attempts have a different average cost from other attempts. Showing the lower and higher price-ratio results does not address that separate allocation uncertainty. Concrete change: Keep the adopted O158 sensitivity, but label it “attempt-share allocation proxy; assumes equal average observed cost per attempt.” Publish the attempt share separately from the unknown expenditure share. Do not describe its two endpoints as bounding the fallback adjustment. What is new relative to the ledger: This is not a renewed challenge to keeping fallback costs or labels under O63/O134, nor a request to replace O158. It identifies an unstated assumption inside the already-adopted diagnostic. Part 3 already applies the corresponding distinction correctly to SWE-Atlas QnA: its task fraction is an equal-cost reading, not an expenditure-share bound. Apply that same standard here.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the fallback sensitivity’s allocation assumption explicit

Use the following decomposition for the existing diagnostic:

𝐴
𝑖
A
i
	​

: published Coding Agent Index cost.

𝐵
𝑖
=
𝐶
𝑖
,
𝑊
−
𝐴
𝑖
B
i
	​

=C
i,W
	​

−A
i
	​

: other admitted basket costs.

𝑓
𝑖
f
i
	​

: observed fallback-attempt fraction.

𝑞
𝑖
q
i
	​

: fallback expenditure share, unidentified unless suitable public cost telemetry exists.

𝑟
𝑖
r
i
	​

: the selected target-to-fallback price ratio under the existing re-pricing convention.

The allocation-based sensitivity is:

𝐶
𝑖
′
(
𝑞
𝑖
,
𝑟
𝑖
)
=
𝐵
𝑖
+
𝐴
𝑖
[
(
1
−
𝑞
𝑖
)
+
𝑞
𝑖
𝑟
𝑖
]
.
C
i
′
	​

(q
i
	​

,r
i
	​

)=B
i
	​

+A
i
	​

[(1−q
i
	​

)+q
i
	​

r
i
	​

].

The current attempt-share proxy sets 
𝑞
𝑖
=
𝑓
𝑖
q
i
	​

=f
i
	​

. State that substitution explicitly in the output and its methodology record.

For example, the diagnostic record should distinguish:

Field	Meaning
fallbackAttemptShare	Observed fraction from AA’s attempt counts
fallbackExpenditureShare	Unidentified, unless publicly evidenced
allocationAssumption	Equal average observed dollars per attempt
proxyExpenditureShare	Set equal to the attempt share for this sensitivity only
interpretation	Conditional re-pricing sensitivity, not an identified cost correction or bound

This requires no additional private data, no cross-configuration evidence transfer and no change to official scores.

Priority 2 — Add an expenditure-allocation stress beside the proxy

Where expenditure share remains unidentified, evaluate the same formula over 
𝑞
𝑖
∈
[
0
,
1
]
q
i
	​

∈[0,1], alongside—not instead of—the existing 
𝑞
𝑖
=
𝑓
𝑖
q
i
	​

=f
i
	​

 result.

For a single fallback model and fixed price ratio:

𝐶
𝑖
′
∈
[
𝐵
𝑖
+
𝐴
𝑖
min
⁡
(
1
,
𝑟
𝑖
)
,
  
𝐵
𝑖
+
𝐴
𝑖
max
⁡
(
1
,
𝑟
𝑖
)
]
.
C
i
′
	​

∈[B
i
	​

+A
i
	​

min(1,r
i
	​

),B
i
	​

+A
i
	​

max(1,r
i
	​

)].

Carry those costs through the existing clipped cost-score function before reporting value or rank effects. Where there are several fallback models, use nonnegative expenditure shares whose sum is at most one, with the remaining share assigned to non-fallback execution.

Interpret this carefully:

It addresses uncertainty about allocation of the observed pooled cost.

It remains conditional on holding the relevant token quantities and execution behaviour fixed.

It is not a bound on the cost of rerunning the tasks with the target model.

It does not enter official scores, O25 interval outputs or evidence admission.

This would distinguish “small movement under the attempt-share proxy” from “small movement across every possible expenditure allocation.” That is a useful difference when the Coding Agent Index accounts for the substantial basket-cost shares reported in part 3.

3. Questions for the owner

None.

4. Verdict

The reviewed sections provide a coherent, implementable separation between published costs, completeness, admission, frozen workloads, subset scoring and comparable interval outputs. I found one material diagnostic-interpretation issue: the fallback re-pricing calculation needs to disclose—and preferably stress—its attempt-to-expenditure allocation assumption. No change to the binding cohort, ranking, fallback-retention or Value Multiple policies is needed.

VERDICT: HAS FEEDBACK