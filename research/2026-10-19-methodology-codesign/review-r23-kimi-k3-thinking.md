1. Findings by severity
Critical

None.

High
H1. The mandatory cost-per-solved-task cross-check lacks an explicit same-execution contract

Issue: The cross-check defines 
𝑑
𝑖
𝑏
d
ib
	​

 as mean cost per attempted task divided by resolved fraction, but does not explicitly require those two quantities to come from the same execution stack, task support and deployment policy. This matters particularly for Terminal-Bench: the draft distinguishes an independently executed quality leaf from two AA-priced executions and prohibits joining tbench.ai cost columns elsewhere. Exact model-and-effort matching alone does not establish that a cost and success rate describe the same deployment.
paste.txt

Why it hurts the objective: A synthetic cost-per-success ratio could diagnose disagreement that comes from mixing harnesses rather than from the SDLC basket’s relevance. AA itself describes coding-agent results as configuration-specific and notes that model, settings and execution configuration materially affect outcomes.
artificialanalysis

Concrete change: Define the cross-check’s observation key as:

(
model, effort, fallback, harness/version, task support, deployment policy
)
.
(model, effort, fallback, harness/version, task support, deployment policy).

Require numerator and denominator to share that key. For Terminal-Bench, use the success rate of the corresponding AA-priced execution where publicly available—not the independently executed quality score. Otherwise mark that row unpriced for this diagnostic.

New relative to the ledger: E55 establishes execution-family accounting for the matched-cost diagnostic, but the separate mandatory 
𝑑
𝑖
𝑏
d
ib
	​

 cross-check does not explicitly inherit an equivalent same-execution requirement.

H2. Aggregate token-demand transport needs an explicit divisible-workload assumption

Issue: The Plan capacity program transports a workload using category-token demand per unit of 
𝑊
W. Even with correctly evidenced token totals and quota coefficients, an average demand vector need not establish that actual tasks can be completed within individual windows. The schedule contract constrains aggregate consumption, but does not explicitly preserve task boundaries, task ordering or non-preemptible execution.
paste.txt

Why it hurts the objective: The solver can certify attainable token consumption without certifying an attainable pass through the scored workload. Consider two task types with consumption vectors 
(
2
,
0
)
(2,0) and 
(
0
,
2
)
(0,2), and a window budget 
(
1
,
1
)
(1,1). Their average demand is 
(
1
,
1
)
(1,1), so a divisible-flow model permits one average task-equivalent. If tasks must finish within that window and cannot be split across resets, neither actual task fits. This is a counterexample to task-capacity identification, not evidence about any particular provider.

Concrete change: Add a workload-execution field:

divisible, interruptible demand;

task-level demand with resumable execution;

task-level demand with non-preemptible execution;

unknown.

Use the existing aggregate program as an upper relaxation unless public evidence supports its attainability interpretation. Derive the lower bound from a feasible task schedule where public task-level records exist. Otherwise label the result “token-equivalent capacity”; do not let it identify completed-workload capacity without a justified mapping.

New relative to E39/E44/E56: Those decisions address quota-window scheduling, demand evidence and certified optimization bounds. They do not explicitly distinguish scheduling consumption from scheduling executable tasks.

Medium
M1. The two independent-source agreement statistics contain built-in self-agreement

Issue: Both statistics compare a composite containing Bug Hunt and Terminal-Bench against a composite made from those same leaves. Consequently, positive agreement is partly mechanical. The value-substitution check also retains the same cost term in both rankings. E66 appropriately limits what that statistic validates, but does not quantify these overlapping contributions.
paste.txt

Why it hurts the objective: Readers can mistake agreement with partly reused evidence for corroboration by independent evidence.

Concrete change: Keep E66’s two statistics, but add a disjoint-evidence comparison:

𝜏
disjoint
=
𝜏
𝑏
 ⁣
(
𝑄
AA-only
,
𝑄
independent-only
)
τ
disjoint
	​

=τ
b
	​

(Q
AA-only
	​

,Q
independent-only
	​

)

on the same common exact-configuration panel. Publish retained weights and panel composition. If the comparison is descriptive and below the main coverage threshold, label it explicitly as a restricted evidence comparison, not an alternative eligible ranking.

New relative to E62/E66: This does not request another version of the adopted substitution check; it removes the shared quality inputs that make that check partly self-confirming.

M2. A fixed 10,000 scenarios does not specify numerical reliability near the 90% decision threshold

Issue: The draft fixes 
𝑁
=
10,000
N=10,000 and defines a “scenario-supported cheapest” label at a scenario frequency of at least 90%, but does not specify Monte Carlo error handling. A published seed guarantees reproducibility, not stability of the estimated frequency around the threshold.
paste.txt

Why it hurts the objective: A label can depend on simulation noise rather than a material difference in the declared scenario model.

Concrete change: Publish Monte Carlo standard errors separately from measurement, identification and specification uncertainty. For independently generated scenario draws:

S
E
^
M
C
=
𝑝
^
(
1
−
𝑝
^
)
𝑁
.
SE
MC
	​

=
N
p
^
	​

(1−
p
^
	​

)
	​

	​

.

Pre-register sequential sample expansion for threshold-adjacent results and a maximum simulation budget. If numerical precision remains insufficient, report “scenario threshold unresolved” rather than choosing a side.

This is an uncertainty-of-computation issue, not another uncertainty stratum or a probability interpretation for the scenario model.

Low
L1. “Every simultaneous limit window is saturated” conflicts with the governing bottleneck formula

Issue: The prose defines full utilisation as saturating every simultaneous limit window. The governing minimum-capacity formula and its weekly-binding fixture correctly allow a non-binding window to remain unsaturated.
paste.txt

Why it hurts the objective: The plain-language description misstates what the Plan result represents.

Concrete change: Replace it with: “maximum eligible API-equivalent usage attainable over the fee period, subject to all evidenced limits and the recorded purchase policy.” Identify the binding constraints separately.

This is a wording correction, not an Owner decision challenge to full-utilisation scoring.

2. Methodology design recommendations
Priority 1 — Make cost-per-success observations execution-matched

For each benchmark execution 
ℎ
h, define:

𝑑
𝑖
ℎ
=
𝑐
ˉ
𝑖
ℎ
𝑟
^
𝑖
ℎ
,
d
ih
	​

=
r
^
ih
	​

c
ˉ
ih
	​

	​

,

where both quantities use the same task support and attempt policy.

Store at least:

execution identifier and harness version;

model, effort and fallback configuration;

task-set identifier;

cost aggregation operator;

success-rate aggregation operator;

treatment of missing cost telemetry;

deployment retry policy, separately from evaluation repetitions.

If the public record exposes paired task-level costs and outcomes, resample those records jointly. If only matching aggregates exist, publish the aggregate ratio with its limitations. If the executions do not match, do not construct the ratio.

This is implementable using existing public benchmark records and the registry already required by r22. AA publishes component scores, cost information and configuration-specific execution descriptions; availability should determine diagnostic coverage rather than justify joining unmatched records.
artificialanalysis

Priority 2 — Distinguish capacity of token flows from capacity of completed work

Introduce two explicit targets:

𝑀
𝑊
flow
and
𝑀
𝑊
completed-work
.
M
W
flow
	​

andM
W
completed-work
	​

.

They may coincide, but only under documented execution assumptions.

For completed-work capacity, use:

𝐿
𝑊
=
capacity achieved by a verified feasible task schedule
,
L
W
	​

=capacity achieved by a verified feasible task schedule,
𝑈
𝑊
=
capacity allowed by a valid aggregate-flow relaxation
.
U
W
	​

=capacity allowed by a valid aggregate-flow relaxation.

Then carry:

𝑀
𝑊
completed-work
∈
[
𝐿
𝑊
,
𝑈
𝑊
]
.
M
W
completed-work
	​

∈[L
W
	​

,U
W
	​

].

Where only aggregate demand is public:

retain any valid flow-capacity calculation;

state whether it is an upper bound, a divisible-workload estimand or an observed-compatible capacity;

identify completed-work capacity only if a public argument connects the two.

This preserves E56’s lower/upper-bound architecture while correcting what the bounds certify. It requires no provider marketing quota numerator and no transferred exact-variant evidence.

Priority 3 — Add one genuinely disjoint quality-agreement diagnostic

On the common panel 
𝐼
I, compute:

𝑄
𝑖
A
A
=
∑
𝑏
∈
𝐴
𝑖
𝑤
𝑏
𝑧
𝑖
𝑏
∑
𝑏
∈
𝐴
𝑖
𝑤
𝑏
,
Q
i
AA
	​

=
∑
b∈A
i
	​

	​

w
b
	​

∑
b∈A
i
	​

	​

w
b
	​

z
ib
	​

	​

,
𝑄
𝑖
i
n
d
=
∑
𝑏
∈
𝐷
𝑖
𝑤
𝑏
𝑧
𝑖
𝑏
∑
𝑏
∈
𝐷
𝑖
𝑤
𝑏
,
Q
i
ind
	​

=
∑
b∈D
i
	​

	​

w
b
	​

∑
b∈D
i
	​

	​

w
b
	​

z
ib
	​

	​

,

where 
𝐴
𝑖
A
i
	​

 and 
𝐷
𝑖
D
i
	​

 contain disjoint execution-organisation groups.

Publish 
𝜏
𝑏
(
𝑄
A
A
,
𝑄
i
n
d
)
τ
b
	​

(Q
AA
,Q
ind
), panel size, excluded configurations, retained leaves and the existing matched-panel sensitivity interval.

Keep E66’s statistics, but name their roles distinctly:

existing quality agreement: alignment with the independent subset;

existing value-substitution agreement: effect of substituting quality evidence while retaining costs;

new disjoint agreement: agreement between non-overlapping quality evidence.

None establishes external validity by itself.

Priority 4 — Give scenario thresholds an executable numerical stopping rule

Use 10,000 scenarios as the initial batch rather than the complete precision contract.

A practical rule is:

Calculate the scenario frequency and its Monte Carlo error interval.

If that interval crosses 90%, expand the simulation using a pre-registered batch schedule.

Stop when the interval lies entirely on one side of 90% or the maximum budget is reached.

At the maximum budget, retain an unresolved threshold status if necessary.

Use an anytime-valid interval if stopping depends on repeatedly checking the result. Apply comparable precision reporting to other headline scenario frequencies, but do not turn small Monte Carlo differences into extra ranking distinctions.

This changes neither the 90% threshold nor the declared scenario kernels. It separates numerical approximation from substantive uncertainty.

Priority 5 — Align the full-utilisation definition with the existing solver

Use one canonical definition in the headline, route registry and capacity section:

Full utilisation is the maximum eligible API-equivalent consumption attainable during the measured fee period under all evidenced quota, funding, throughput and execution constraints.

Publish binding limits and unused non-binding capacity as diagnostics. No formula or owner decision needs to change.

3. Questions for the owner

Is the identified Plan-capacity target divisible token-equivalent throughput, or completed passes through the fixed workload? The answer determines whether aggregate demand alone can be sufficient or task-execution feasibility must also be established.

For the mandatory Terminal-Bench cost-per-solved-task cross-check, is the intended resolved fraction from the AA-priced execution or from the independent tbench.ai quality leaf? If the former is already required operationally, H1 becomes a specification clarification rather than a substantive implementation change.

4. Verdict

VERDICT: HAS FEEDBACK