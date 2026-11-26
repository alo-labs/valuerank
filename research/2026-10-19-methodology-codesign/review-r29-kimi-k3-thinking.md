1. Findings by severity
Critical

None.

High

None.

Medium

Plan numerator eligibility does not clearly distinguish an unsuccessful task from an unsuccessful request.

Issue: E75 includes delivered execution and policy-permitted retries, but excludes “failed or rejected requests.” It does not explicitly state whether a successfully delivered response that fails a benchmark task remains eligible consumption. That distinction matters because the API basket measures expenditure on attempted work, not expenditure exclusively on successful outcomes. AA describes its Coding Agent Index cost as average API cost per task across the benchmark executions, rather than cost conditional on solving the task.
paste.txt
artificialanalysis

Why it hurts the objective: If Plan eligibility excludes model execution because the task was unsuccessful, while the API basket includes its token expenditure, the two bases use different accounting supports. Quality already captures task success; filtering consumption by success can penalise it again through the Plan multiple.

Concrete change: Introduce separate fields for request-delivery status and task outcome. State explicitly that successfully delivered, deployment-policy-permitted execution remains eligible whether the task passes or fails. Distinguish transport errors, pre-execution rejection, model-generated refusal, and ordinary task failure; document how each reconciles with the API basket. This clarifies E75 rather than relaxing the fixed evidence rules.

Headline rank events need an explicit common-panel and tie contract.

Issue: E65 defines common panels and a declared tie convention for baseline-versus-branch rank differences. The draft does not give an equally explicit definition for headline rank, “rank ≤ 3” scenario shares, or pairwise ordering shares when rows tie or a branch excludes configurations. E13 requires branch evaluability disclosures, but does not completely define those events.
paste.txt

Why it hurts the objective: A configuration can acquire a stronger-looking top-three share because competitors disappear from the branch, rather than because its relative value improves. Equal scores also permit materially different top-three shares under different rank conventions.

Concrete change: Define a frozen eligible panel for every published rank-frequency series, prohibit scenario-dependent silent panel changes, and publish a tie convention. For branch comparisons, extend E65 to top-
𝑘
k and pairwise frequencies—not just numerical rank differences. Report pairwise win, tie and loss separately.

The cost-component admission rule leaves reference-panel construction insufficiently specified.

Issue: The rule requires exact costs for every configuration in a frozen reference panel containing at least two-thirds of ranked rows. However, it does not specify how that panel is selected, when selection occurs, or whether different components may use different admission panels. Depending on that interpretation, individually admissible components can produce an admitted basket with much lower joint full-basket coverage. Existing readiness and completeness disclosures would reveal the result, but do not resolve the construction ambiguity.
paste.txt

Why it hurts the objective: Basket construction determines which configurations receive common-workload costs and which remain on incomparable subset workloads. An underspecified selection procedure weakens reproducibility and can unintentionally favour well-documented configurations.

Concrete change: Specify one workload-level admission panel, its deterministic selection procedure, and the point at which it is frozen. If component-specific panels are intended instead, say so explicitly and publish the intersection of complete configurations before admitting the basket. This does not require changing the two-thirds threshold or imputing costs.

Low

The stated ±20% concordance shorthand does not match the intuitive interpretation of its executable rule.

Issue: O11 describes reports as “concordant within ±20%,” while E33 implements 
max
⁡
𝑥
𝑘
/
min
⁡
𝑥
𝑘
≤
1.20
maxx
k
	​

/minx
k
	​

≤1.20. Reports at 80 and 120 are both within ±20% of 100, but fail that ratio rule. Normative precedence resolves implementation, but not reader interpretation.
paste.txt

Why it hurts the objective: Contributors may collect or describe qualifying Plan evidence using a different tolerance from the one the release actually applies.

Concrete change: Preserve the adopted ratio rule and replace the shorthand everywhere with “largest report no more than 20% above the smallest report.” This is a wording correction, not a proposal to loosen O11.

Single-leaf quality groups need an explicit deterministic within-group weight rule.

Issue: S2 prescribes within-group Dirichlet draws, while Reliability currently contains only Omniscience. The intended result is clear, but an executable specification should state that a one-leaf group has within-group weight exactly one. Dirichlet weights live on a simplex; for a single component, that simplex contains only the value one.
paste.txt
wikipedia

Why it hurts the objective: This is a small implementation-portability issue, particularly when benchmark retirement changes the number of leaves in a group.

Concrete change: Add a singleton-group fixture and bypass the distribution sampler for that group.

2. Methodology design recommendations

The priority is to close a few executable-contract gaps, not to add another uncertainty layer or reopen the adopted owner decisions.

Priority 1 — Align Plan eligibility with the API execution support

For each measured execution record 
𝑟
r, store:

request_delivery_status

task_outcome

deployment_policy_role

token_observability

api_basket_treatment

plan_numerator_treatment

eligibility_reason

Define the numerator as

𝑈
=
∑
𝑟
𝑒
𝑟
 
𝑝
⊤
𝑡
𝑟
,
U=
r
∑
	​

e
r
	​

p
⊤
t
r
	​

,

where 
𝑒
𝑟
e
r
	​

 expresses eligibility under the declared deployment policy and execution accounting—not whether the task succeeded.

Add these fixtures:

Delivered execution, task passes: included.

Delivered execution, task fails: included under the same deployment policy.

Policy-permitted retry after an unsuccessful attempt: both delivered executions included.

Request rejected before model execution, with no delivered consumption: excluded.

Execution or consumption cannot be separated from excluded overhead: supported bounds or unidentified transport, as already required by E75.

The important addition is an accounting reconciliation between eligible measured consumption and the execution support underlying 
𝐶
𝑖
,
𝑊
C
i,W
	​

. AA’s public cost description supports treating API expenditure and task performance as distinct quantities.
artificialanalysis

Priority 2 — Define ranking events mathematically

For each stratum and branch, publish a fixed panel 
𝐼
I. One implementable tie convention is competition rank:

𝑟
𝑖
(
𝑠
)
=
1
+
∑
𝑗
∈
𝐼
∖
{
𝑖
}
1
{
𝑉
𝑗
(
𝑠
)
>
𝑉
𝑖
(
𝑠
)
}
.
r
i
	​

(s)=1+
j∈I∖{i}
∑
	​

1{V
j
	​

(s)>V
i
	​

(s)}.

Then define

𝑓
𝑖
,
𝑘
=
1
𝑁
∑
𝑠
=
1
𝑁
1
{
𝑟
𝑖
(
𝑠
)
≤
𝑘
}
.
f
i,k
	​

=
N
1
	​

s=1
∑
N
	​

1{r
i
	​

(s)≤k}.

Disclose that ties can make more than 
𝑘
k configurations qualify for “rank ≤ 
𝑘
k.” Alternatively, choose another convention, but make it normative.

For pairwise results, publish the three frequencies

𝑓
𝑖
𝑗
>
,
𝑓
𝑖
𝑗
=
,
𝑓
𝑖
𝑗
<
,
f
ij
>
	​

,f
ij
=
	​

,f
ij
<
	​

,

rather than leaving equality treatment implicit.

Additional release rules:

A branch-level exclusion changes the declared panel; it never silently changes the denominator scenario by scenario.

A top-
𝑘
k frequency computed among 
𝑛
n configurations names 
𝑛
n.

Baseline-versus-branch frequency changes use the same common panel on both sides.

Frequencies from different workload objects remain labelled as cross-workload ordering not identified, consistent with O17.

This extends the existing paired-panel principle to the headline events without changing the score or cohort policy.
paste.txt

Priority 3 — Make admission-panel construction reproducible

Use a machine-readable object such as:

text
admission_panel:
  workload_version
  selection_rule
  selection_timestamp
  configuration_ids
  ranked_cohort_size_at_admission
  required_panel_size
  admitted_components
  complete_all_components_ids

A straightforward implementation is:

Freeze one named workload-level panel before score and rank inspection.

Apply the existing exact-cost requirement to every proposed component on that panel.

Publish both marginal component coverage and joint full-basket coverage.

Preserve the adopted persistence rule after admission.

If the intended policy instead allows different panels for different components, encode that alternative explicitly. In that case, joint full-basket coverage becomes a particularly important release statistic; it must not be inferred from separate component percentages.

This recommendation specifies the existing admission mechanism rather than replacing its threshold or exact-variant evidence requirement.
paste.txt

Priority 4 — Add small specification fixtures

Add two inexpensive tests:

Concordance boundary: reports 100 and 120 pass; reports 100 and any value strictly above 120 fail. Replace “±20%” with the ratio-based wording.

Singleton weight: a group with one active leaf always assigns that leaf within-group weight one; only the group-level draw changes its overall weight.

Neither requires new public data or alters an adopted substantive decision.
paste.txt

3. Questions for the owner

Does “failed request” in E75 mean failure to deliver model execution, or does it also include delivered execution that fails the task? The answer determines whether the numerator rule needs substantive correction or only clearer wording.

Is the admission reference panel intended to be one common panel for workload version 
𝑊
W, or may each component use a different panel? The answer changes the appropriate admission-panel specification.

Should tied configurations all receive the best occupied rank for headline top-
𝑘
k shares, even when that means more than 
𝑘
k configurations qualify? The answer determines the normative rank-event formula.

4. Verdict

The draft is substantively well developed. Its remaining material gaps concern execution-accounting interpretation, rank-event definitions and admission-panel construction—not the fixed cohort, exact-variant evidence policy or Value Multiple evidence rules. These can be resolved with small, testable specification changes rather than another methodological redesign.
paste.txt

VERDICT: HAS FEEDBACK