1. Findings by severity
Critical

The confirmed-cheapest definition compares a candidate against itself. Issue: The definition requires candidate 
𝑖
i to be strictly cheaper than “every 
𝑗
j that can possibly qualify,” without excluding 
𝑗
=
𝑖
j=i. A confirmed-qualified candidate necessarily possibly qualifies, so the test includes

max
⁡
𝜃
[
𝑐
𝑖
(
𝜃
)
−
𝑐
𝑖
(
𝜃
)
]
<
0
,
θ
max
	​

[c
i
	​

(θ)−c
i
	​

(θ)]<0,

which is impossible. The scenario-supported-cheapest wording has the same self-comparison ambiguity.
paste.txt
 Why it hurts the objective: One of the three principal outputs can never certify a cheapest model under the literal executable specification. Change: Explicitly quantify over 
𝑗
∈
𝑅
𝑊
∖
{
𝑖
}
j∈R
W
	​

∖{i} in both definitions. Specify separately whether equal-cost competitors produce co-cheapest labels or prevent a unique-cheapest label. Add fixtures for a singleton cohort, a uniquely cheapest candidate, and two equal-cost qualifiers.

High

A component with missing cost telemetry can appear to be a full-workload component. Issue: The Coding Agent Index total covers the tasks with cost telemetry; unrecorded tasks are omitted and the component is flagged “partial.” But the draft does not explicitly require such a component to fail the full-workload-cost eligibility test. The workload object, meanwhile, freezes task multiplicities. A reported total over fewer tasks is not the cost of that frozen execution workload.
paste.txt
 Why it hurts the objective: A model can appear cheaper because less of its evaluation was priced, and a “partial component” flag alone does not prevent that cost from entering frontier or cheapest calculations. Change: Distinguish task outcome from accounting completeness:

Attempted task with missing telemetry: cost is missing, not zero.

Measured refusal or early termination: retain its actual cost and corresponding outcome.

Unexecuted task: record its execution status explicitly.

Require exact task-support coverage for full-
𝑊
W eligibility. Otherwise use O17’s subset machinery on an explicitly named execution subset, or report the component as unavailable if public aggregate data cannot isolate a comparable subset. New relative to E28: This is not a request to impute omitted tasks or reject AA’s total. It addresses whether a partial published total satisfies the separate full-workload eligibility predicate.

Certification scope does not explicitly account for excluded competitors. Issue: Frontier and bar outputs operate over 
𝑅
𝑊
R
W
	​

, excluding subset-cost, API-fallback and Plan-unidentified rows. That restriction is mathematically clear, but the headline claim concerns the AA-selected cohort. A “confirmed cheapest” among evaluable rows need not be cheapest among all selected configurations. The additional test that “removing competitor evidence cannot strengthen a confirmed result” conflicts with simply dropping a competitor from 
𝑅
𝑊
R
W
	​

.
paste.txt
 Why it hurts the objective: Losing evidence can remove a potentially competitive model and manufacture an apparently stronger result. Change: Publish the certification universe beside each result: “among these 
𝑛
n full-workload, identified configurations.” Separately report whether the claim extends to the complete selected cohort. Unevaluable competitors must prevent a cohort-wide certification unless available structural bounds rule them out. New relative to E11/E21/E36: The issue is the relationship between the eligible-set definition, public label scope and the existing evidence-removal invariant—not another request to remove flagged rows from the headline table.

The capacity program does not yet specify an executable treatment of session starts. Issue: E30 correctly distinguishes session-anchored, fixed-reset and sliding windows. However, a session beginning at first use makes its start time dependent on the consumption schedule. Merely naming a “small time-indexed linear program” does not specify how that dependency is enforced. The simple 
min
⁡
𝑤
𝜆
𝑤
min
w
	​

λ
w
	​

 expression also requires a feasible allocation, not just independently attainable budgets.
paste.txt
 Why it hurts the objective: Capacity can be overestimated if the optimizer chooses incompatible window phases or treats session boundaries as freely available resets. This matters operationally: Anthropic documents both session and weekly limits, shared across Claude and Claude Code.
support.claude
 Change: Add an executable window-scheduling contract:

Fixed phases: ordinary time-indexed constraints.

Endogenous session starts: explicit session-start variables and logic, or enumeration of admissible schedules.

Insufficient public semantics: a documented feasible conservative schedule, not an unconstrained optimum.

Publish discretization, boundary treatment and a feasible consumption schedule supporting every identified capacity result. New relative to E30: This concerns implementing the adopted session semantics, not replacing them with sliding windows.

Medium

Formal interval outputs lack a decision procedure and numerical certification contract. Issue: Definite and possible frontier membership are joint quantified statements. The 10,000-scenario engine cannot establish those statements: not observing a dominating scenario does not prove none exists. The draft separates scenario frequencies from interval outputs, but does not specify how the latter are computed.
paste.txt
 Why it hurts the objective: Two implementations can produce different certified labels despite reading the same registry, especially with shared dependencies and strict inequalities. Change: Specify a deterministic optimization or feasibility procedure for each interval label. Record solver status, tolerance and a witness or certificate. An unresolved solve must return “not certified,” not a scenario-derived definite or impossible label. New relative to E21/E25: The quantifiers and draw kernels are already adopted; the missing piece is their executable separation.

“Low agreement” in the mandatory workload cross-check is undefined. Issue: The draft specifies Kendall 
𝜏
𝑏
τ
b
	​

, a minimum panel size and resampling rules, but says only that “low agreement” triggers a headline warning. It supplies no threshold or rule for uncertain estimates.
paste.txt
 Why it hurts the objective: A mandatory warning remains editorially discretionary after results are observed. Change: Pre-register a descriptive threshold and a separate uncertainty status. For example: trigger the warning at point-estimate 
𝜏
𝑏
<
0.5
τ
b
	​

<0.5; report “uncertain agreement” when the sensitivity interval spans the threshold. Treat 0.5 as an explicit policy choice, not a statistical fact. Publish the exact matched configuration panel alongside the statistic.

Low

Component expenditure concentration does not capture the disclosed Terminal-Bench overlap. Issue: HHI over accounting components can conceal task-family concentration because one Terminal-Bench execution sits inside the indivisible Coding Agent Index total while another appears separately.
paste.txt
 Why it hurts the objective: The diagnostic can appear diversified even though expenditure includes repeated exposure to the same task family. Change: Keep the adopted component HHI, but add a task-family overlap matrix and mark family-level expenditure concentration “unidentified” where aggregate costs cannot be separated. New relative to O24/E22: This retains both priced executions; it improves interpretation of the concentration diagnostic rather than revisiting inclusion.

2. Methodology design recommendations
Priority 1: Make eligibility and claim scope executable

Introduce separate predicates rather than allowing a generic “partial” flag to carry several meanings:

FullCost
⁡
(
𝑖
,
𝑊
)
=
⋀
𝑒
∈
𝑊
CompleteCostEvidence
⁡
(
𝑖
,
𝑒
)
.
FullCost(i,W)=
e∈W
⋀
	​

CompleteCostEvidence(i,e).

For Plan interval outputs, additionally require identified 
𝑀
𝑖
,
𝑊
M
i,W
	​

, as already adopted. Store:

Component identity and exact task-support identity.

Required, executed and cost-observed task counts.

Completeness status and exclusion reason.

Eligible-set membership for each output.

A task count alone is insufficient when different rows could cover different tasks. These fields operationalize the existing frozen-workload and no-imputation policies without changing them.
paste.txt

For every certified label, publish two scope fields:

Certified within the named evaluable set.

Extension to the selected cohort: established / not established, with omitted competitors listed.

Priority 2: Correct and test the cheapest predicates

Use the corrected definition:

ConfirmedUniqueCheapest
⁡
(
𝑖
)
  
⟺
  
	
ConfirmedQualified
⁡
(
𝑖
)
∧
¬
Provisional
⁡
(
𝑖
)


	
∧
∀
𝑗
∈
𝑅
𝑊
∖
{
𝑖
}
 with possible qualification
,


	
sup
⁡
𝜃
∈
Θ
:
 
𝑄
𝑗
(
𝜃
)
≥
𝑄
𝑟
(
𝜃
)
[
𝐶
𝑖
(
𝜃
)
−
𝐶
𝑗
(
𝜃
)
]
<
0.
ConfirmedUniqueCheapest(i)⟺
	​

ConfirmedQualified(i)∧¬Provisional(i)
∧∀j∈R
W
	​

∖{i} with possible qualification,
θ∈Θ:Q
j
	​

(θ)≥Q
r
	​

(θ)
sup
	​

[C
i
	​

(θ)−C
j
	​

(θ)]<0.
	​


The scenario event must likewise exclude 
𝑖
i from its competitor set. Use a distinct label for co-cheapest results if ties are to be supported.

Test evidence loss in two stages: the eligible-set result may change, but evidence loss must not create a stronger selected-cohort claim.

Priority 3: Separate simulation from certification in the implementation

Use the scenario engine for frequencies and sensitivity. Use deterministic feasibility checks for interval labels:

To disprove definite-frontier membership, find an admissible scenario and competitor that dominates.

To establish possible-frontier membership, find one admissible scenario where no competitor dominates.

To certify unique cheapest, solve the conditional pairwise cost maximizations in the corrected definition.

Return at least four implementation statuses: certified / disproved / unresolved / unevaluable. Save counterexample scenarios where available. Do not convert Monte Carlo non-observation into certification. This preserves E21’s joint-dependence definitions.
paste.txt

Priority 4: Require constructive Plan-capacity evidence

Every identified capacity result should include either:

A feasible schedule achieving the stated capacity; or

A lower-bound feasible schedule and an upper bound, yielding an interval for 
𝑀
𝑊
M
W
	​

.

Use publicly measured budgets and consumption coefficients only. Provider documentation can establish window structure, but should continue to supply neither the Value Multiple numerator nor an invented burn rate. Anthropic’s documentation illustrates why shared pools and simultaneous limits need explicit treatment.
support.claude
+1

Priority 5: Finish the diagnostic specification without expanding the ranking

Keep the adopted weights, normalization and benchmark mix unchanged in this revision. Complete the missing warning threshold, task-support checks and overlap annotations first.

For routine refreshes, derive these outputs from the same versioned registry rather than adding another evidence collection process. AA already distinguishes token-price inputs, task costs and suite costs; preserve those distinctions in ingestion and accounting tests rather than inferring one field from another.
artificialanalysis
+1

3. Questions for the owner

Should “confirmed cheapest” mean uniquely cheapest only, or should equal-cost qualifying models receive a separate co-cheapest label? This determines the tie predicate and release fixtures.

Must frontier and cheapest labels make claims about the entire AA-selected cohort, or may they explicitly certify only the named evaluable subset? This determines whether excluded competitors block certification or instead limit its scope.

4. Verdict

VERDICT: HAS FEEDBACK