1. Findings by severity
Critical

None.

High

Cost completeness is inferred at the wrong observational unit. Issue: E47 treats 
𝑇
=
𝑛
𝜇
T=nμ, with 
𝑛
=
303
n=303, as sufficient to establish complete task support. However, AA describes its efficiency metrics as pooled per-task-attempt averages, excludes missing telemetry from those averages, and runs three attempts per task. Consequently, establishing that all task identities appear is not equivalent to establishing that all attempts contributing to their published deployment-equivalent means have cost telemetry. The draft requires attempt counts to be published but does not make their completeness part of the predicate.
paste.txt
artificialanalysis
 Why it hurts the objective: Missing expensive attempts can lower published cost while a task remains represented. Such a row could enter 
𝑅
𝑊
R
W
	​

 and receive an interval label despite its cost omitting part of the deployment policy represented by its quality score. A fractional 
𝑇
/
𝜇
T/μ also does not, by itself, identify a number of missing tasks. Concrete change: Define completeness over the required task–attempt support and the source’s aggregation operator. Permit aggregate-based certification only when a documented identity establishes that support—not merely the number of task equivalents. Otherwise use “completeness unresolved.” Re-audit the stated 13 complete rows against this stronger predicate. New relative to E37/E47: This is not another request to add completeness checks; it identifies a mismatch between their existing unit of certification and AA’s documented averaging unit.

The LiveBench instruction-following leaf has no demonstrated current source. Issue: The draft allocates 5% of quality to “LiveBench Instruction Following” and counts it toward approximately 25% independent quality weight. The current LiveBench 2.0 page, released October 13, lists Agentic, Reasoning, Coding, Browser Use, Data Analysis, Research and Design—not an instruction-following suite. This does not prove that no archived instruction-following evidence exists, but the current source does not substantiate the leaf specified in r19.
paste.txt
livebench
 Why it hurts the objective: An unavailable or obsolete leaf changes coverage, renormalised weights and the claimed independent evidence share. Substituting a current suite would silently change the construct being measured. Concrete change: Before release, pin an actual instruction-following artifact, dataset version, score field and exact-configuration support. If none exists for a row, mark that leaf missing. If the leaf is retired or replaced, make that a quality-version migration with an overlap comparison; do not substitute LiveBench Overall, Agentic or Reasoning. New relative to the ledger: This is a source-availability finding for a leaf still present in r19, analogous in consequence—but not identical—to the already resolved GPQA retirement.

Plan capacity can be counted twice when gross cash includes usage-dependent purchases. Issue: The fee contract allows additional purchased usage when its payment enters the denominator. The capacity contract, however, defines spendable budgets 
𝐵
𝑤
B
w
	​

 without explicitly separating subscription entitlement, bundled credits and separately purchased capacity. These can obey different constraints. In particular, included credits can either fund consumption within an existing limit or unlock additional consumption; those are different mechanisms.
paste.txt
 Why it hurts the objective: A capacity implementation could count purchased consumption in an observed numerator and also treat it as subscription capacity, or scale a measured purchase amount as though it were a recurring entitlement. Both distort 
𝑀
𝑊
M
W
	​

, even when the cash receipt reconciles. Concrete change: Add funding-source capacity variables and a purchase policy to the route object. State whether additional cash is fixed at the measured amount or varies with consumption. Each consumed unit must use exactly one funding source, while all applicable shared rate limits still apply. Where public evidence cannot establish these relationships, retain the observed multiple but leave target-workload transport unidentified. New relative to the existing gross-cash rule: The denominator already addresses payment accounting; the missing contract concerns how those payments generate feasible capacity in the optimiser.

Medium

The matched-cost split/merge invariant conflicts with its formula. Issue: The diagnostic is

𝐶
𝑖
𝑚
𝑎
𝑡
𝑐
ℎ
=
∑
𝑏
𝑤
𝑏
′
𝑃
𝑖
𝑏
.
C
i
match
	​

=
b
∑
	​

w
b
′
	​

P
ib
	​

.

If a leaf of weight 
𝑤
w and pass cost 
𝑃
=
𝑃
1
+
𝑃
2
P=P
1
	​

+P
2
	​

 is split into two leaves with weights 
𝑤
/
2
,
𝑤
/
2
w/2,w/2, its contribution changes from 
𝑤
𝑃
wP to 
𝑤
(
𝑃
1
+
𝑃
2
)
/
2
w(P
1
	​

+P
2
	​

)/2, before the common panel normalisation. Thus preserving total quality weight and total execution workload does not preserve this diagnostic, contrary to the release test.
paste.txt
 Why it hurts the objective: A benchmark’s accounting representation can change matched-cost ranks and warnings without changing any underlying execution or outcome. Concrete change: Separate execution accounting from quality-leaf weighting. Freeze diagnostic pass weights on canonical execution families, and make quality subleaves inherit their parent’s execution reference without creating additional pass-weight terms. Alternatively, narrow the invariant explicitly to duplicate reporting of the same complete execution—not partitioning it into disjoint costs. New relative to E24: The finding is an algebraic contradiction in the adopted invariant, not a renewed argument about complete-pass versus per-task pricing.

The quota optimiser certifies a grid problem, not necessarily full attainable capacity. Issue: E39 specifies a default 15-minute grid and feasible schedules, but does not distinguish optimality on that grid from optimality under the underlying quota semantics. Session starts and resets need not align with the grid.
paste.txt
 Why it hurts the objective: A grid-feasible schedule is a valid lower bound if its boundary treatment is conservative. It is not automatically an upper bound on full-utilisation capacity. A discretisation loss could therefore be presented as a plan’s capacity difference. Concrete change: Publish separate feasible_lower_bound, relaxed_upper_bound, grid_resolution and optimality_scope fields. Use an event-aligned grid where public reset times permit it. Certify a point capacity only when the bounds coincide under the recorded semantics; otherwise transport an interval into 
𝑀
𝑊
M
W
	​

. New relative to E39: Feasible scheduling is already required. The missing distinction is between a grid optimum and the target capacity optimum.

The uncertainty layers do not fully specify how source intervals become scenario frequencies. Issue: Draw-kernel objects specify distributions, but the draft allows published confidence intervals, repeated-run ranges and “token-use variance” to feed scenario outputs without consistently stating whether the sampled variable is a latent mean, a future run, or the published statistic. These are different targets. O25 clarifies the interval-output target, but does not resolve this scenario-target ambiguity.
paste.txt
 Why it hurts the objective: Two implementations can use the same public interval and kernel family yet produce materially different ranking frequencies because they simulate different quantities. Concrete change: Require scenario_target and sampling_level for every stochastic input. Separate uncertainty about expected benchmark performance from predictive run-to-run variation. Where public evidence supports only one, publish only that interpretation; do not manufacture the other. New relative to E25/E49: Kernel completeness and interval-target compatibility are already adopted. This adds the missing target contract for the scenario engine itself.

Low

Quality-source exposure is not yet an executable quantity. Issue: The draft lists “share of quality weight by data source,” while its provenance contract separately records dataset authors, executors, harnesses and graders. Those categories need not coincide. The approximately 75%/25% split is therefore ambiguous unless “source” is explicitly defined.
paste.txt
 Why it hurts the objective: Readers can mistake execution independence for dataset or grading independence, overstating diversification. Concrete change: Publish separate exposure vectors for execution organisation, dataset origin, harness and grader. Keep “leave-AA-out” explicitly defined as removal by execution organisation, and recompute the percentages from actual admitted evidence rather than a static list. New relative to the existing provenance requirement: The metadata already exists; what is missing is a deterministic aggregation rule connecting it to the displayed exposure figures.

2. Methodology design recommendations
Priority 1 — Correct the completeness contract before certifying interval outputs

For each configuration 
𝑖
i and execution component 
𝑒
e, store:

Required task identities.

Required evaluation-attempt identities.

Which attempts contribute to the published statistic.

Cost-observed attempt identities.

The exact aggregation operator.

Any documented exclusions or retry replacements.

Define:

CompleteCostEvidence
⁡
(
𝑖
,
𝑒
)
  
⟺
  
every required contributing attempt has cost evidence,
CompleteCostEvidence(i,e)⟺every required contributing attempt has cost evidence,

or a publicly documented aggregate identity establishes the equivalent support.

Keep evaluation repetitions averaged rather than multiplied into deployment cost. The change is about completeness of that average, not charging for all three repetitions. AA explicitly distinguishes three-attempt task scoring from pooled task-attempt efficiency metrics, making this distinction necessary.
artificialanalysis

Add two fixtures:

All 303 tasks appear, but one contributing attempt lacks cost telemetry: not confirmed complete.

A documented aggregate identity certifies complete contributing support: confirmed complete without requiring unpublished raw records.

Do not infer missing-task counts from fractional total-to-mean ratios.

Priority 2 — Add a source-existence preflight for every quality leaf

Before scoring, validate the tuple:

(
artifact
,
version
,
field
,
configuration
,
effort
,
stack
,
task support
)
.
(artifact,version,field,configuration,effort,stack,task support).

The immediate application is LiveBench: its current published suites differ from the instruction-following leaf specified in r19.
livebench

Produce a release diff showing:

Evidence newly admitted or withdrawn.

Coverage changes by row.

Changes in row-specific effective weights.

Changes in evaluator-independent observed weight.

This requires no imputation and preserves the fixed exact-variant policy.

Priority 3 — Make Plan capacity funding-aware

Represent consumption using non-overlapping funding flows, for example:

𝑦
𝑡
=
𝑦
𝑡
𝑠
𝑢
𝑏
𝑠
𝑐
𝑟
𝑖
𝑝
𝑡
𝑖
𝑜
𝑛
+
𝑦
𝑡
𝑏
𝑢
𝑛
𝑑
𝑙
𝑒
𝑑
+
𝑦
𝑡
𝑝
𝑢
𝑟
𝑐
ℎ
𝑎
𝑠
𝑒
𝑑
.
y
t
	​

=y
t
subscription
	​

+y
t
bundled
	​

+y
t
purchased
	​

.

Apply shared quota constraints to the relevant combined flows, and funding-specific balances to the relevant individual flows. Where public evidence establishes a different mechanism, encode that mechanism instead.

Define the purchase policy explicitly:

No additional purchases.

Fixed measured additional cash.

A publicly evidenced consumption-dependent payment rule.

Then compute:

𝑀
𝑊
=
API-priced feasible target-workload consumption
subscription cash
+
purchase cash under the stated policy
.
M
W
	​

=
subscription cash+purchase cash under the stated policy
API-priced feasible target-workload consumption
	​

.

This is an implementation clarification of the existing gross-cash decision, not a proposal to use provider marketing quotas.

Priority 4 — Repair matched-cost representation invariance

Use canonical execution families 
𝑔
g, with frozen diagnostic weights 
𝛼
𝑔
α
g
	​

:

𝐶
𝑖
𝑚
𝑎
𝑡
𝑐
ℎ
=
∑
𝑔
𝛼
𝑔
𝑃
𝑖
𝑔
,
∑
𝑔
𝛼
𝑔
=
1.
C
i
match
	​

=
g
∑
	​

α
g
	​

P
ig
	​

,
g
∑
	​

α
g
	​

=1.

Execution-family membership and 
𝛼
𝑔
α
g
	​

 should be fixed before ranks are examined. Partitioning 
𝑃
𝑖
𝑔
P
ig
	​

 into accounting subcomponents must leave the parent cost unchanged:

𝑃
𝑖
𝑔
=
∑
𝑒
∈
𝑔
𝑃
𝑖
𝑒
.
P
ig
	​

=
e∈g
∑
	​

P
ie
	​

.

Splitting a quality reporting leaf must not automatically split or duplicate an execution-family weight. Retain the priced-quality coverage diagnostic separately; do not make accounting representation determine diagnostic workload weights.

Priority 5 — Publish capacity bounds and scenario targets explicitly

For Plan scheduling, require:

𝜆
feasible
≤
𝜆
true
≤
𝜆
relaxed
,
λ
feasible
	​

≤λ
true
	​

≤λ
relaxed
	​

,

where the first bound comes from a verified feasible schedule and the second from a valid relaxation of the same public quota semantics. Convert both to multiple bounds. A solver’s grid optimality certificate alone should not establish equality.

For stochastic outputs, add these registry fields:

Field	Required distinction
scenario_target	Expected benchmark performance / future deployment run / reporting precision / specification convention
sampling_level	Task / repository / run / fitted parameter / shared factor
supported_by_public_evidence	The evidence supporting that target and sampling level
interpretation_label	The wording permitted beside the resulting scenario share

Do not change the fixed weights or cost anchors as part of these repairs. None of these findings establishes a better replacement weight vector; the immediate need is to make the existing design internally executable and its output interpretations consistent.

3. Questions for the owner

For routes with separately purchased usage, is the intended full-utilisation estimand conditional on the measured additional cash amount, or may the capacity optimiser vary purchases? This determines the funding constraints and potentially whether the optimisation remains linear.

Is there a pinned public LiveBench instruction-following artifact with exact-version and effort evidence for this cohort? If so, its identity determines whether the remedy is source repair or a quality-version migration.

Do the captured Coding Agent Index fields document complete task–attempt support, or only aggregate totals and pooled means? This determines which currently “complete” rows can retain interval eligibility.

4. Verdict

VERDICT: HAS FEEDBACK