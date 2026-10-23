1. Findings by severity
Critical

The specification-weight kernel substantially changes the objective instead of perturbing it. Issue: With 13 leaves, 
𝛼
𝑖
=
max
⁡
(
50
𝑤
𝑖
,
10
)
α
i
	​

=max(50w
i
	​

,10) gives DeepSWE 
𝛼
=
15
α=15 and every other leaf 
𝛼
=
10
α=10. Since a Dirichlet component has mean 
𝛼
𝑖
/
∑
𝑗
𝛼
𝑗
α
i
	​

/∑
j
	​

α
j
	​

, the expected group weights become:
Group	Headline weight	Expected S2 weight
Software engineering	60%	33.3%
General professional work	20%	14.8%
Reliability and instruction following	10%	14.8%
Long context and science	10%	37.0%
The Dirichlet mean identity establishes this directly.
wikipedia
 Why it hurts: The requirement to lead in a majority of S2 scenarios can reject a strong software-engineering value leader because it fails a substantially science-reweighted objective. Publishing realised CVs does not fix the shifted means. Change: Preserve nominal means with 
𝛼
𝑖
=
𝜅
𝑤
𝑖
α
i
	​

=κw
i
	​

, or use a hierarchical distribution that preserves both group and within-group means. This is a new argument against the adopted kernel: its problem is not merely excessive or insufficient dispersion, but systematic recentering.

High

The Plan credit convention permits economically incomparable multiples. Issue: One branch divides by fee minus bundled credits at list value; another divides by gross fee depending on whether credits were spent. Consequently, the same subscription can receive different denominators because of accounting treatment rather than delivered usage. The net denominator can also approach zero or become non-positive. Why it hurts: Since Plan score uses 
𝐶
A
P
I
/
𝑀
C
API
	​

/M, denominator artefacts can become large apparent value advantages. Change: Use gross cash fee for the primary multiple:

𝑀
=
eligible API-priced usage delivered
subscription cash fee
+
required usage payments
.
M=
subscription cash fee+required usage payments
eligible API-priced usage delivered
	​

.

Include usage funded by credits bundled into that fee once; exclude separately purchased usage unless its payment is included. Retain net-credit accounting only as a diagnostic. New relative to the ledger: This identifies a denominator-consistency failure in the adopted credit-netting rule, not a request to remove credit accounting or change the full-utilisation objective.

Scenario sampling does not establish identification-bound claims. Issue: The draft combines missing-leaf bounds, parametric ranges and finite draws, but does not specify an exhaustive calculation for “lead holds on its identification bounds.” Sampling 10,000 interior points cannot establish a worst-case statement over the allowed set. Why it hurts: A “recommended” label could appear robust because adverse boundary combinations were never drawn. Conversely, the result can depend on arbitrary triangular or uniform kernels for quantities that have bounds but no estimated distribution. Change: Compute identification claims separately through interval arithmetic or constrained optimisation. Keep scenario frequencies as a secondary sensitivity output. Define shared constraints explicitly so worst-case comparisons respect common multiples, prices and missing benchmark values. New relative to the ledger: The adopted bounds and simulation are appropriate outputs; the missing element is the algorithm connecting them to the certification language.

The workload cross-check does not define a comparable target across its matched rows. Issue: Membership allows either DeepSWE or Terminal-Bench evidence. The draft does not say whether models are compared on the same benchmark, the same task population, or a pooled score. It also refers to divergence from “total-cost rank,” whereas the matched-cost diagnostic refers to a different, reweighted cost ranking. Why it hurts: Comparing one model’s dollars per DeepSWE solve with another’s dollars per Terminal-Bench solve measures different units of useful work. Yet a greater-than-three-place divergence can block recommendation. Terminal-Bench itself reports model, agent, resolution rate and cost separately, making stack-specific matching important.
tbench
 Change: Define separate, common-panel comparisons for each benchmark and exact stack. Calculate both rank positions within the same matched subset. Distinguish:

total cost versus matched cost;

total cost versus cost per solved task.

Only the explicitly designated comparison should trigger the recommendation block. New relative to the ledger: This addresses incompatible denominators and rank universes in the adopted cross-check, not whether the cross-check should exist.

S2 leader conditioning is underspecified and potentially inoperable. Issue: S2 draws source-drop flags, but their frequencies are unspecified. Meanwhile, approximately 25% of nominal quality weight is independent of AA, so the draft’s 40% suppression rule makes leave-AA-out unavailable on its own stated source allocation. Why it hurts: The majority-S2 leader rule can change with arbitrary source-drop frequencies or with whether suppressed scenarios count as losses, disappear from the denominator, or are renormalised. The promised headline leave-AA-out column will ordinarily contain no substantive result. Change: Publish source removal as separate stress-test strata, not randomly weighted events. Define the S2-majority requirement over a specified, evaluable core stratum. Mark leave-AA-out “not identifiable under coverage rule,” and exclude it from that denominator. New relative to the ledger: This is an incompatibility between the adopted source allocation, suppression threshold and leader rule—not another request to add source sensitivity.

Medium

The attempts-reconciliation rule can manufacture a bias where none exists. Issue: A mean of three pass@1 attempts estimates single-attempt performance. It is not the performance of a three-attempt retry strategy. A cost representing one attempt is therefore not automatically mismatched with that quality estimate. AA describes its evaluations as generally using pass@1 scoring.
artificialanalysis
 Why it hurts: Automatically adding an “attempts bias” draw can penalise repeated measurement rather than a genuine difference in deployment policy. Change: Record two separate fields: evaluation repetitions and deployment attempts per task. Repetitions affect precision; retries, best-of-
𝑘
k, selection and verifier policies affect both quality and cost. Apply reconciliation only to the latter. New relative to the ledger: The correction concerns the interpretation of repeats, not the need to reconcile genuinely different attempt policies.

Route selection and eligibility are not rerun inside uncertainty scenarios. Issue: The route is selected using its multiple’s lower bound, but the scenario description only draws the selected multiple. It does not specify whether alternative eligible tiers remain available during comparisons, or whether measured and assumed routes compete in the same selection step. Why it hurts: A model can receive a poor conservative route despite having another route that is preferable across much of the admissible evidence. Recommendation robustness then partly reflects an undocumented route-selection policy. Change: Preserve every admissible route in the release data. Make the displayed route a deterministic policy choice, but publish route-selection sensitivity and distinguish a fixed-route ranking from a best-eligible-route ranking. Do not silently switch tiers within scenarios.

Quality-bar references lack an uncertainty rule. Issue: “The median definite-frontier model” can change when frontier membership changes, and the reference model’s quality is itself uncertain. The draft does not specify whether the bar is a point, interval or jointly drawn value. Why it hurts: “Confirmed qualifying” can mean either genuinely at least as capable as the reference or merely above its reported point estimate. These are different claims. Change: Pin a named reference configuration for each release and compare candidates with its jointly modelled quality. Publish the stronger interval-certified relation separately from scenario qualification.

Low

The recommendation-blocking rank threshold is sensitive to cohort composition. Issue: A three-place displacement becomes easier or harder to trigger when closely spaced models enter the matched subset, even if existing models’ costs and capabilities do not change. Why it hurts: A recommendation can disappear because several near-tied alternatives were added rather than because the model’s practical economics changed. Change: Retain the adopted rank flag, but accompany it with a material cost-ratio threshold and attribute changes caused solely by matched-set membership. Use the economic discrepancy, not rank movement alone, to explain the warning.

2. Methodology design recommendations
Priority 1 — Correct the scenario architecture before implementation

Preserve the headline’s nominal weights:

𝑤
(
𝑠
)
∼
Dirichlet
⁡
(
𝜅
𝑤
)
.
w
(s)
∼Dirichlet(κw).

For this distribution,

CV
⁡
(
𝑤
𝑖
(
𝑠
)
)
=
1
−
𝑤
𝑖
𝑤
𝑖
(
𝜅
+
1
)
.
CV(w
i
(s)
	​

)=
w
i
	​

(κ+1)
1−w
i
	​

	​

	​

.

Thus preserving a 1.25% leaf’s mean while limiting its CV to approximately 30% requires 
𝜅
κ around 877 or higher. A single Dirichlet cannot independently give every leaf the same relative perturbation while retaining arbitrary nominal means.
wikipedia

A more interpretable alternative is hierarchical sensitivity:

Perturb group weights around 
60
/
20
/
10
/
10
60/20/10/10.

Perturb within-group weights around their nominal proportions.

Publish concentrations separately.

Treat source removal, alternative GDPval mappings and transfer assumptions as named stress-test branches rather than assigning them arbitrary occurrence frequencies.

Use S2-majority eligibility only within a fully specified core branch. Publish the remaining branches alongside it, with explicit reasons for any unevaluable branch.

Priority 2 — Add deterministic certification alongside scenario frequencies

For each model, retain the no-imputation headline:

𝑄
𝑖
o
b
s
=
∑
𝑗
∈
𝑂
𝑖
𝑤
𝑗
𝑧
𝑖
𝑗
∑
𝑗
∈
𝑂
𝑖
𝑤
𝑗
.
Q
i
obs
	​

=
∑
j∈O
i
	​

	​

w
j
	​

∑
j∈O
i
	​

	​

w
j
	​

z
ij
	​

	​

.

Separately calculate complete-objective identification bounds:

𝑄
𝑖
𝐿
=
∑
𝑗
∈
𝑂
𝑖
𝑤
𝑗
𝑧
𝑖
𝑗
𝐿
,
𝑄
𝑖
𝑈
=
∑
𝑗
∈
𝑂
𝑖
𝑤
𝑗
𝑧
𝑖
𝑗
𝑈
+
100
∑
𝑗
∉
𝑂
𝑖
𝑤
𝑗
.
Q
i
L
	​

=
j∈O
i
	​

∑
	​

w
j
	​

z
ij
L
	​

,Q
i
U
	​

=
j∈O
i
	​

∑
	​

w
j
	​

z
ij
U
	​

+100
j∈
/
O
i
	​

∑
	​

w
j
	​

.

These are bounding calculations, not filled-in benchmark observations.

With cost interval 
[
𝐶
𝑖
𝐿
,
𝐶
𝑖
𝑈
]
[C
i
L
	​

,C
i
U
	​

], monotonicity gives:

𝑉
𝑖
𝐿
=
0.25
𝑆
𝐶
(
𝐶
𝑖
𝑈
)
+
0.75
𝑄
𝑖
𝐿
,
𝑉
𝑖
𝑈
=
0.25
𝑆
𝐶
(
𝐶
𝑖
𝐿
)
+
0.75
𝑄
𝑖
𝑈
.
V
i
L
	​

=0.25S
C
	​

(C
i
U
	​

)+0.75Q
i
L
	​

,V
i
U
	​

=0.25S
C
	​

(C
i
L
	​

)+0.75Q
i
U
	​

.

A sufficient conservative certificate is 
𝑉
𝑖
𝐿
>
max
⁡
𝑘
≠
𝑖
𝑉
𝑘
𝑈
V
i
L
	​

>max
k

=i
	​

V
k
U
	​

. Where shared dependencies make this too conservative, minimise each pairwise difference over the joint admissible set:

min
⁡
𝜃
∈
Θ
[
𝑉
𝑖
(
𝜃
)
−
𝑉
𝑘
(
𝜃
)
]
>
0.
θ∈Θ
min
	​

[V
i
	​

(θ)−V
k
	​

(θ)]>0.

Publish “interval-certified,” “scenario-supported” and “not identified” as distinct outcomes. Do not let a scenario-frequency threshold substitute for the certificate.

Priority 3 — Standardise Plan accounting and preserve route alternatives

For every route, publish:

actual cash subscription fee;

additional cash required for included usage;

included credits and whether they were consumed;

eligible API-valued consumption;

excluded consumption and its funding source.

Use one gross-cash convention for the primary multiple. Require a positive denominator and explicit reconciliation from receipts to numerator.

Keep the owner’s lower-bound route selection, but specify its application precisely: maximise the eligible multiple’s lower bound, use a declared tie-breaker, and freeze the selected route for the primary ranking. Publish other eligible tiers as route sensitivity, without transferring evidence across configurations.

Priority 4 — Make matched-cost diagnostics benchmark-specific

For each benchmark 
𝑏
b, define a common exact-configuration panel 
𝐼
𝑏
I
b
	​

. For each model:

𝑑
𝑖
𝑏
=
mean cost per attempted task
resolved fraction
.
d
ib
	​

=
resolved fraction
mean cost per attempted task
	​

.

Set 
𝑑
𝑖
𝑏
=
∞
d
ib
	​

=∞ when the resolved fraction is zero; report uncertainty near zero rather than suppressing the problem.

Calculate Kendall 
𝜏
𝑏
τ
b
	​

 between total-cost rank and 
𝑑
𝑖
𝑏
d
ib
	​

 rank within 
𝐼
𝑏
I
b
	​

, separately for DeepSWE and Terminal-Bench. Where public task-level results exist, resample the same task clusters across models. If only aggregates exist, label a model-row bootstrap as sensitivity to the matched model set—not measurement uncertainty.

Do not pool raw dollars per solve across benchmarks. AA’s published methodology supplies token-category cost accounting, while the independent Terminal-Bench table supplies stack-specific cost and resolution fields; both still require exact field and denominator matching.
tbench
+1

Priority 5 — Pin thresholds and distinguish replication from retries

For a named reference model 
𝑟
r:

Interval-certified qualification:

𝑄
𝑖
𝐿
≥
𝑄
𝑟
𝑈
.
Q
i
L
	​

≥Q
r
U
	​

.

Possible qualification: there exists a jointly admissible state with 
𝑄
𝑖
≥
𝑄
𝑟
Q
i
	​

≥Q
r
	​

.

Scenario qualification: the share of specified scenarios satisfying 
𝑄
𝑖
(
𝑠
)
≥
𝑄
𝑟
(
𝑠
)
Q
i
(s)
	​

≥Q
r
(s)
	​

.

Choose and freeze the reference identity at release time. A cohort-relative reference can remain a descriptive view, but should not silently replace that identity during uncertainty propagation.

For attempts, add machine-readable fields for:

number of independent evaluation repetitions;

attempts permitted per deployment task;

selection or retry policy;

cost coverage of those attempts.

This makes the reconciliation implementable without collecting new private data or treating repeated pass@1 measurement as multi-attempt deployment.

3. Questions for the owner

Should S2 test modest uncertainty around the stated 60/20/10/10 objective, or intentionally test substantially different buyer preferences? The present kernel does the latter despite stating the former.

Does the “recommended” label require universal identification-bound superiority, or only superiority in a high share of declared scenarios? The draft currently invokes both; the distinction determines whether certification must use optimisation or only simulation.

Are subscription credits inseparable entitlements included in the fee, optional purchases, or both across current routes? This changes which usage and payments belong in the primary gross-cash multiple.

Which adopted cross-check is intended to block recommendation: reweighted matched cost, benchmark-specific cost per solved task, or either? These can disagree for legitimate reasons and need separate definitions.

4. Verdict

VERDICT: HAS FEEDBACK