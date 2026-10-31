1. Findings by severity
Critical

None.

High

The interval certificate lacks a fully specified admissible set. Issue: “Worst admissible joint state” does not say whether certification holds nominal weights fixed, includes the full support of the Dirichlet draws, or permits alternative price policies and GDPval mappings. It also does not define how a transferred Plan route is represented when transfers are off. If Dirichlet support is included, arbitrarily extreme weight allocations remain admissible despite the intended modest perturbations. Why it hurts the objective: Different implementations could produce different “recommended” labels from identical evidence. A certificate is only meaningful relative to an explicit set of allowed states. Concrete change: Publish a deterministic certification set separately from the scenario distributions. Fix nominal weights, the primary price policy, selected route and primary GDPval mapping for the main certificate; include measurement intervals and identification bounds. Publish specification robustness separately. With transfers off, mark transfer-dependent Plan routes unevaluable rather than silently substituting API cost. New relative to the ledger: This does not revisit deterministic certification; it identifies missing definitions needed to implement the adopted certificate.

The category-specific harmonic multiple requires a shared-budget assumption that the quota schema does not establish. Issue: 
𝑀
=
(
∑
𝑘
𝑡
𝑘
/
𝑚
𝑘
)
−
1
M=(∑
k
	​

t
k
	​

/m
k
	​

)
−1
 is valid when category consumption is additive against one common budget. With several windows, category-specific charging, or separate pools, independently derived category multiples need not combine this way. Taking the minimum across windows after collapsing them into one multiple can also lose which constraint binds for the target mix. Why it hurts the objective: The resulting Plan cost can imply that a workload fits within a subscription when its actual combination of token categories exhausts a different pool first. Concrete change: Calculate target-mix capacity separately for every evidenced pool/window, then apply their intersection. Use the harmonic formula only where the source establishes a common additive budget. Otherwise retain the observed-mix multiple and its existing mix-unmatched flag without presenting it as a category-adjusted estimate. New relative to the ledger: Simultaneous limits and category-specific multiples were adopted separately; their mathematical compatibility has not been specified.

The matched-cost certification blocker is not reproducible across incomplete cost panels. Issue: The draft specifies leaf weighting but not a fixed common priced-leaf set, minimum priced-weight coverage, or exact construction of the matched/total ratio. Different rows could therefore represent different weighted task baskets. Moreover, a missing diagnostic could let a poorly evidenced row escape a blocker that a better-evidenced row triggers. Why it hurts the objective: Eligibility for “recommended” can depend on cost-data availability rather than demonstrated value. Concrete change: Define one published common cost panel for each certification comparison, normalize its weights once, and compare both matched-cost and total-cost ranks on precisely the same model panel. Publish priced-weight coverage and the ratio reference population. An unavailable comparison should be “cross-check unidentified,” not “passed”; a recommendation dependent on that comparison should remain uncertified. New relative to the ledger: This concerns missing-data and denominator rules for the adopted blocker, not replacing AA total cost.

The uncertainty engine invents a quality–cost dependency unless paired observations support it. Issue: A shared “serving snapshot” draw does not itself define a joint distribution. When only aggregate benchmark scores and parametric token-cost ranges exist, there is no observed pairing from which to infer whether higher cost accompanies better or worse performance. Why it hurts the objective: An arbitrary coupling can materially change scenario leadership, cost per solve and robustness labels while appearing evidence-backed. Concrete change: Use paired task/run resampling only when corresponding cost and outcome observations are public. Otherwise distinguish known shared factors—such as the same price list—from unknown statistical dependence. Publish independent, positively associated and negatively associated dependence stress branches; use conservative joint bounds for certification. New relative to the ledger: Drawing cost and quality jointly was adopted; this finding addresses how that joint dependence is identified.

Medium

Missing-leaf simulation does not specify how to transition from the renormalized score to the full composite. Issue: S0 uses an observed-only renormalized composite, while S1 adds missing-leaf draws. The text does not explicitly require restoring the original weights before adding those leaves. Its kernels also do not specify how completely unidentified missing leaves are drawn. Why it hurts the objective: Implementations could double-count observed evidence or make scenario rankings depend on an undeclared distribution over missing performance. Concrete change: Define separate equations for S0 and the full-composite S1/S2 score. State that any missing-leaf sampling law is a scenario convention, not evidence; keep the formal 0–100 bounds distribution-free. New relative to the ledger: This is an implementation gap in the adopted cumulative strata, not a request for imputation.

Bug Hunt’s measurement interval mixes incompatible units and imports uncertainty from other configurations. Issue: “Range across the two repos” is not directly an interval for a pooled fixed/105 score unless repository denominators and weighting are specified. Widening single-run rows by the cohort’s repeat spread also imports a variability assumption from other configurations despite exact-variant evidence policy. Why it hurts the objective: A 10%-weight leaf can receive misleadingly narrow or broad intervals, affecting certification. Concrete change: Calculate each complete run’s pooled fixed/105 result. Treat repository differences as repository sensitivity, not repeated measurements of that pooled result. For 
𝑛
=
1
n=1, distinguish published evidence uncertainty from a labelled repeatability stress allowance. Do not use a borrowed cohort spread as exact-variant measurement evidence. New relative to the ledger: The adopted run-count and range rules still need a common estimand and a policy-consistent treatment of borrowed variability.

“Unique cheapest” has two potentially conflicting publication rules. Issue: The Outputs section requires worst-case cost superiority against every possibly qualifying candidate; the Uncertainty section says a unique cheapest is named only at ≥90% of scenarios. It is unclear whether scenario support alone can authorize that wording. The first rule also compares separate extrema even where shared uncertainties make them jointly impossible. Why it hurts the objective: Buyers may confuse a scenario-supported choice with an interval-certified cheapest choice, or the method may unnecessarily fail to identify a genuine robust winner. Concrete change: Use distinct labels: “interval-certified cheapest,” “scenario-supported cheapest,” and “candidate set.” For certification, optimize pairwise cost differences conditional on each competitor qualifying in the same admissible state. New relative to the ledger: This reconciles the earlier scenario rule with the subsequently adopted interval and joint-state rules.

The source accounting does not distinguish evaluator independence from task independence. Issue: Terminal-Bench is independently run for quality but also appears inside AA’s priced suite. Counting its quality weight as independent is reasonable for execution provenance, but does not establish independence of task content or benchmark failure modes. AA explicitly lists Terminal-Bench 4.0 within its Intelligence Index; the official Terminal-Bench board separately reports model, agent, resolution rate, cost and tokens.
tbench
+1
 Why it hurts the objective: “25% independent” can be read as broader independent validation than the evidence establishes. Concrete change: Publish separate provenance fields for dataset author, execution organization, harness and grader. Report evaluator-independent quality weight and task-overlap exposure separately. Do not change nominal weights automatically. New relative to the ledger: Source-weight disclosure and correlations were adopted; this adds a distinction those summaries cannot express.

Low

The registry treats ordinary data refreshes as methodology migrations. Issue: “A change in any of these” includes price-list dates, cache assumptions and other fields that also appear in routine score-change decomposition. Why it hurts the objective: Monthly refreshes become procedurally indistinguishable from actual changes in methodology, obscuring why rankings moved. Concrete change: Separate methodology version, benchmark/evidence version and release snapshot. A new observed price under an unchanged price rule is a data refresh; changing the price rule is a methodology migration. A benchmark-version change should trigger a comparability review and dual-run where feasible. New relative to the ledger: This resolves conflicting versioning instructions rather than questioning the adopted audit trail.

2. Methodology design recommendations
Priority 1 — Publish an executable scoring and certification specification

Retain the owner’s headline weights, cohort and exact-variant rules. Make the following definitions normative.

For observed leaves 
𝑂
𝑖
O
i
	​

, coverage is

𝑝
𝑖
=
∑
𝑏
∈
𝑂
𝑖
𝑤
𝑏
.
p
i
	​

=
b∈O
i
	​

∑
	​

w
b
	​

.

The displayed observed-only score is

𝑄
𝑖
o
b
s
=
∑
𝑏
∈
𝑂
𝑖
𝑤
𝑏
𝑧
𝑖
𝑏
𝑝
𝑖
.
Q
i
obs
	​

=
p
i
	​

∑
b∈O
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

.

The full-composite identification score is instead

𝑄
𝑖
(
𝜃
)
=
∑
𝑏
∈
𝑂
𝑖
𝑤
𝑏
𝑧
𝑖
𝑏
(
𝜃
)
+
∑
𝑏
∉
𝑂
𝑖
𝑤
𝑏
𝑢
𝑖
𝑏
,
𝑢
𝑖
𝑏
∈
[
0
,
100
]
.
Q
i
	​

(θ)=
b∈O
i
	​

∑
	​

w
b
	​

z
ib
	​

(θ)+
b∈
/
O
i
	​

∑
	​

w
b
	​

u
ib
	​

,u
ib
	​

∈[0,100].

Thus, with point-valued observed leaves,

𝑄
𝑖
𝐿
=
𝑝
𝑖
𝑄
𝑖
o
b
s
,
𝑄
𝑖
𝑈
=
𝑝
𝑖
𝑄
𝑖
o
b
s
+
100
(
1
−
𝑝
𝑖
)
.
Q
i
L
	​

=p
i
	​

Q
i
obs
	​

,Q
i
U
	​

=p
i
	​

Q
i
obs
	​

+100(1−p
i
	​

).

Measurement intervals extend these bounds in the same original-weight space. S1 and S2 must use that full-composite equation, not append missing contributions to 
𝑄
𝑖
o
b
s
Q
i
obs
	​

.

For the primary certificate, define

𝑉
𝑖
(
𝜃
)
=
0.25
𝑆
𝐶
(
𝑐
𝑖
(
𝜃
)
)
+
0.75
𝑄
𝑖
(
𝜃
)
,
V
i
	​

(θ)=0.25S
C
	​

(c
i
	​

(θ))+0.75Q
i
	​

(θ),

and publish each pairwise margin

Δ
𝑖
𝑗
min
⁡
=
inf
⁡
𝜃
∈
Θ
c
e
r
t
[
𝑉
𝑖
(
𝜃
)
−
𝑉
𝑗
(
𝜃
)
]
.
Δ
ij
min
	​

=
θ∈Θ
cert
	​

inf
	​

[V
i
	​

(θ)−V
j
	​

(θ)].

Require 
Δ
𝑖
𝑗
min
⁡
>
0
Δ
ij
min
	​

>0 for every relevant competitor, alongside the existing eligibility gates.

The certification manifest should explicitly enumerate:

Fixed choices: nominal weights, route, price rule and primary quality mapping.

Variable evidence: measurement intervals, missing-leaf bounds, evidenced multiple ranges and deployment-policy bias bounds.

Shared constraints: prices, donor measurements, task/run observations and quota pools.

Unevaluable comparisons and their consequences.

Call the result “interval-certified under the declared evidence bounds,” not a confidence guarantee.

Priority 2 — Compute Plan capacity from evidenced constraints

Where public controlled measurements identify additive budget consumption, let 
𝑥
𝑘
x
k
	​

 be required tokens of category 
𝑘
k per AA-suite-equivalent workload. Let 
𝑎
𝑤
𝑘
a
wk
	​

 be measured consumption of budget 
𝑤
w per token, and 
𝐵
𝑤
B
w
	​

 its measured spendable capacity over the fee period.

Then

𝜆
max
⁡
=
min
⁡
𝑤
𝐵
𝑤
∑
𝑘
𝑎
𝑤
𝑘
𝑥
𝑘
,
λ
max
	​

=
w
min
	​

∑
k
	​

a
wk
	​

x
k
	​

B
w
	​

	​

,
𝑀
t
a
r
g
e
t
=
𝜆
max
⁡
𝐶
A
A
𝐹
g
r
o
s
s
,
𝑐
P
l
a
n
=
𝐹
g
r
o
s
s
𝜆
max
⁡
.
M
target
	​

=
F
gross
	​

λ
max
	​

C
AA
	​

	​

,c
Plan
	​

=
λ
max
	​

F
gross
	​

	​

.

This expresses the existing full-utilisation policy without introducing monthly-demand scenarios.

Apply it only when the public evidence supports the budget structure and fee-period conversion. If not, retain the admitted observed-mix measurement; report that target-mix capacity is unidentified. Provider quota descriptions may document structure, but must not supply the numerator.

Priority 3 — Make the matched-cost blocker a defined test

For a published common model panel 
𝐼
I and common priced-leaf panel 
𝐵
∗
B
∗
, define

𝑤
~
𝑏
=
𝑤
𝑏
∑
ℎ
∈
𝐵
∗
𝑤
ℎ
,
𝐶
𝑖
m
a
t
c
h
=
∑
𝑏
∈
𝐵
∗
𝑤
~
𝑏
 
𝑐
𝑖
𝑏
.
w
b
	​

=
∑
h∈B
∗
	​

w
h
	​

w
b
	​

	​

,C
i
match
	​

=
b∈B
∗
∑
	​

w
b
	​

c
ib
	​

.

Here 
𝑐
𝑖
𝑏
c
ib
	​

 must consistently mean cost per attempted task, with evaluation repetitions divided out and deployment retries included. AA publicly describes per-task costs and token-category breakdowns for GDPval-AA; Terminal-Bench exposes cost and token columns, but each ingested cost field still needs its own aggregation contract.
tbench
+1

Define

𝑅
𝑖
=
𝐶
𝑖
m
a
t
c
h
/
𝐶
𝑖
t
o
t
a
l
median
⁡
𝑗
∈
𝐼
(
𝐶
𝑗
m
a
t
c
h
/
𝐶
𝑗
t
o
t
a
l
)
.
R
i
	​

=
median
j∈I
	​

(C
j
match
	​

/C
j
total
	​

)
C
i
match
	​

/C
i
total
	​

	​

.

Make “differs by more than 1.5×” explicitly mean

𝑅
𝑖
>
1.5
or
𝑅
𝑖
<
1
/
1.5.
R
i
	​

>1.5orR
i
	​

<1/1.5.

Apply the existing >3-place condition using ranks calculated on 
𝐼
I for both measures. Publish 
∑
𝑏
∈
𝐵
∗
𝑤
𝑏
∑
b∈B
∗
	​

w
b
	​

, exact stack compatibility and a pass/flag/unidentified result. Set the minimum acceptable priced-weight coverage before inspecting the resulting winners.

Priority 4 — Separate evidence intervals, dependence assumptions and scenario conventions

Add three registry fields for every uncertain input:

Interval meaning: rounding, published confidence interval, observed range, identification bound or analyst stress range.

Sampling law and justification.

Dependency identifier and supporting paired evidence.

When paired observations exist, resample their costs and outcomes together. Otherwise retain known shared factors but show dependence sensitivity instead of implying an observed covariance structure.

For wholly missing leaves, publish the sampling convention and at least one alternative convention. Scenario-supported leadership should be described as conditional on that convention. Formal certificates should not depend on it.

Priority 5 — Unify threshold recommendations using conditional joint comparisons

For candidate 
𝑖
i, require robust qualification:

inf
⁡
𝜃
∈
Θ
[
𝑄
𝑖
(
𝜃
)
−
𝑄
𝑟
(
𝜃
)
]
≥
0.
θ∈Θ
inf
	​

[Q
i
	​

(θ)−Q
r
	​

(θ)]≥0.

For each competitor 
𝑗
j that can qualify, test

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
𝑐
𝑖
(
𝜃
)
−
𝑐
𝑗
(
𝜃
)
]
<
0.
θ∈Θ:Q
j
	​

(θ)≥Q
r
	​

(θ)
sup
	​

[c
i
	​

(θ)−c
j
	​

(θ)]<0.

This respects shared uncertainties and avoids comparing mutually incompatible extrema. If the constraints cannot establish uniqueness, publish the candidate set. Keep the ≥90% scenario result as a separately named, weaker output.

Priority 6 — Add targeted implementation tests

Before release, require tests demonstrating that:

Shared price changes cancel from relevant Plan calculations when both the multiple numerator and AA cost use that same price basis.

Restoring a missing leaf transitions correctly from renormalized S0 to original-weight S1.

Transfers-off never silently becomes API fallback within a Plan certificate.

A tighter quota cannot increase computed full-utilisation capacity.

Adding an unrelated cohort row cannot change the common-panel diagnostic except through explicitly cohort-dependent quantities.

The reference configuration always qualifies against itself in every joint scenario.

These are inexpensive deterministic checks against errors in the methodology’s most consequential joins and formulas.

3. Questions for the owner

Should the interval certificate hold nominal weights and the primary price rule fixed, or also certify against specification alternatives? This determines the admissible set and the meaning of “recommended.”

When a Plan route depends entirely on an owner-authorized transfer, should transfers-off make that route unevaluable, or is another directly measured route permitted for the certification comparison? The present frozen-route language does not settle this.

What minimum common priced-quality weight must the matched-cost diagnostic cover before it can authorize certification? Without this decision, a very narrow panel could control the recommendation label.

4. Verdict

The draft’s remaining weaknesses are primarily operational: its adopted safeguards need precise estimands, joint constraints and missing-evidence behavior before independent implementations can reliably reproduce its recommendation labels. None of the changes above requires relaxing the fixed cohort, transferring exact-variant benchmark evidence, or using marketing quotas as delivered value.

VERDICT: HAS FEEDBACK