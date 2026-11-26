1. Findings by severity
Critical

None.

High

The interval solver still contains an invalid “no shared factors” shortcut for row-local coupled constraints. Issue: E73 correctly makes the constrained primitive-variable graph authoritative, but the decision procedure still says that, without shared factors, labels are decided exactly by monotone extremes. Independence across configurations does not imply that a configuration’s lowest cost and highest quality are jointly attainable. E83’s primitive-derived quantities make this distinction especially important.
paste.txt
 A counterexample, using arbitrary cost and quality units:

Configuration 
𝑖
i: one local primitive 
𝑡
∈
[
0
,
1
]
t∈[0,1], with 
𝐶
𝑖
=
1
+
𝑡
C
i
	​

=1+t and 
𝑄
𝑖
=
𝑡
Q
i
	​

=t.

Configuration 
𝑗
j: 
𝐶
𝑗
=
1
,
 
𝑄
𝑗
=
0.5
C
j
	​

=1, Q
j
	​

=0.5.

Configuration 
𝑘
k: 
𝐶
𝑘
=
1.5
,
 
𝑄
𝑘
=
1
C
k
	​

=1.5, Q
k
	​

=1.

For 
𝑡
≤
0.5
t≤0.5, 
𝑗
j dominates 
𝑖
i. For 
𝑡
≥
0.5
t≥0.5, 
𝑘
k dominates 
𝑖
i. Thus 
𝑖
i is never on the frontier. But the unattainable componentwise “best corner” 
(
𝐶
𝑖
,
𝑄
𝑖
)
=
(
1
,
1
)
(C
i
	​

,Q
i
	​

)=(1,1) is undominated. Why it hurts the objective: An implementation following the unconditional shortcut can certify a configuration as a possible frontier member when no admissible execution state supports that result. An implementation following the proof requirement instead remains safe, but the draft does not specify its general solution path for this case. Concrete change: Replace “no shared factor” with a decision-specific separability condition. When local constraints couple cost and quality, branch over the relevant local primitives as well as shared factors, or use a certified row-feasible-set reduction. Unsupported constraint classes must return unresolved. What is new: This does not repeat the request for E73’s constrained model or E79’s feasibility prerequisite. The example has a nonempty feasible set and no cross-row shared factor; it exposes a remaining mismatch between those adopted rules and the shortcut’s stated applicability.

Medium

The route comparator can select a route that is strictly worse in target-workload cost under every admissible state. Issue: E85 prioritises point identification over set identification before comparing multiples. Consider two equally graded, otherwise eligible routes for the same configuration, workload and valuation basis:

Route A: point-identified 
𝑀
𝑊
=
2
M
W
	​

=2.

Route B: set-identified 
𝑀
𝑊
∈
[
10
,
11
]
M
W
	​

∈[10,11].

E85 selects A, although B’s effective cost is lower throughout its identified interval:

𝐶
𝑊
/
10
<
𝐶
𝑊
/
2.
C
W
	​

/10<C
W
	​

/2.

The same discontinuity occurs if an interval changes from 
[
10
,
10
]
[10,10] to 
[
10
,
10
+
𝜀
]
[10,10+ε]: an arbitrarily small loss of point identification can trigger a large deterioration in the selected economics. The existing best-eligible-route sensitivity exposes the consequence but does not prevent the official selection.
paste.txt
 Why it hurts the objective: The official route can be demonstrably more expensive for the same configuration and workload, rather than merely more conservative under overlapping evidence. Concrete change: Before applying E85, remove routes robustly dominated in effective workload cost by another route with at least equal evidence grade. Preserve the existing comparator for the remaining routes. What is new: This is a challenge to editor decision E85 based on robust dominance and a discontinuity fixture—not a request to choose the largest reported multiple regardless of evidence.

GDPval needs an explicit live-rating versus frozen-integration estimand. Issue: AA documents both fitted GDPval-AA ratings and scores frozen at the time a configuration enters the Intelligence Index. The draft specifies the normalization and requires pinned fields, but does not explicitly say which temporal rating object ValueRank’s quality leaf must use. AA also documents that the fitted ratings depend on pairwise comparisons and a pinned reference configuration.
artificialanalysis
 Why it hurts the objective: Two refresh implementations could use the same benchmark version, model configuration and normalization yet produce different quality scores: one from the current fitted leaderboard and another from the frozen Index integration value. A live refit can also change a row without a new task execution, which does not fit cleanly into the draft’s price/token-use/method/cohort attribution categories.
paste.txt
artificialanalysis
 Concrete change: Declare the primary temporal estimand explicitly. Record rating_snapshot_id, fit_revision, integration_freeze_status and task_execution_revision separately. Attribute rating-only changes as “benchmark refit/regrading,” not token-use or model-performance changes. What is new: The registry already pins fields and benchmark versions. The additional issue is that current fitted performance and frozen Index contribution are distinct published records within the same benchmark version.

Per-row cost anchors are disclosed, but cohort-level cost influence still pools incomparable scoring transformations. Issue: E86 correctly gives subset rows their own workload, anchor object and exchange rate. However, the headline within-cohort influence statistic still computes one 
𝑆
𝐷
(
𝑆
𝐶
)
SD(S
C
	​

) across ranked rows, including scores produced by different workloads and anchor transformations. The release flag can therefore change because a row moves between full-basket and subset calibration—not because cost has become more or less influential on a common workload.
paste.txt
 Why it hurts the objective: The “cost influence below 10%” flag can describe a mixture of calibration effects and actual cost dispersion. A reader cannot interpret it as the effective cost contribution among comparable configurations. Concrete change: Keep the mixed-table statistic only as “displayed-table dispersion.” Compute the headline influence statistic on a declared common-workload panel using one anchor object and the same rows for 
𝑆
𝐷
(
𝑆
𝐶
)
SD(S
C
	​

) and 
𝑆
𝐷
(
𝑆
𝑄
)
SD(S
Q
	​

). Publish separate workload-stratum statistics for subset rows. What is new: E86 solves row-level anchor applicability. It does not resolve the interpretation of a cohort statistic pooling those different anchor objects. This recommendation leaves O17’s displayed scores and table positions unchanged.

Low

None.

2. Methodology design recommendations

Make solver eligibility depend on constraint geometry, not merely shared-factor presence. Add an executable decision classification:
Constraint class	Permitted solution method
Decision-specific corner reduction proved	Exact corner evaluation
Affine constraints and supported disjunctions	Exact or certified linear/disjunctive feasibility
Supported nonlinear primitive constraints	Certified branch-and-bound over all relevant primitives
Unsupported constraint class	Unresolved; no certified label
A feasibility witness establishes that the evidence set is nonempty; it does not establish that separately optimized cost and quality endpoints can coexist. Add the three-configuration example above as a regression test alongside the existing shared-factor interior-witness test.

Add a conservative route-dominance filter before E85. For routes 
𝑎
,
𝑏
a,b serving the same exact configuration and workload, define:

𝑎
≺
𝑏
⟺
max
⁡
𝜃
∈
Θ
𝑎
𝑏
[
𝐶
𝑊
(
𝜃
)
𝑀
𝑊
,
𝑎
(
𝜃
)
−
𝐶
𝑊
(
𝜃
)
𝑀
𝑊
,
𝑏
(
𝜃
)
]
<
0.
a≺b⟺
θ∈Θ
ab
	​

max
	​

[
M
W,a
	​

(θ)
C
W
	​

(θ)
	​

−
M
W,b
	​

(θ)
C
W
	​

(θ)
	​

]<0.

Apply the filter only when:

Both routes have identified target-workload multiples.

The workload, valuation basis and deployment policy are compatible.

Route 
𝑎
a’s evidence grade is at least route 
𝑏
b’s.

The dominance result is certified under their joint constraints.

With simple independent positive intervals, the sufficient condition 
𝐿
𝑎
>
𝑈
𝑏
L
a
	​

>U
b
	​

 avoids another nonlinear solve. Retain every route in the release data and publish the dominance reason. No new private measurements or provider-marketing numerators are required.

Specify GDPval’s temporal record and refresh policy. For the stated practical-capability objective, I would use the current published fitted GDPval-AA v2.1 rating at the release snapshot, while retaining the frozen Intelligence Index contribution as a diagnostic. AA’s methodology distinguishes the fitted Elo process from its frozen Index integration.
artificialanalysis
 This choice should be explicit rather than inferred from a field name. Publish a refresh decomposition:

Δ
𝑄
=
Δ
𝑄
new executions
+
Δ
𝑄
refit/regrading
+
Δ
𝑄
method
+
Δ
𝑄
coverage
,
ΔQ=ΔQ
new executions
	​

+ΔQ
refit/regrading
	​

+ΔQ
method
	​

+ΔQ
coverage
	​

,

using a declared sequential bridge where these effects interact. Where public evidence cannot separate execution changes from refitting, label that component “benchmark-record update—decomposition unavailable.”

Compute influence on comparable panels. For a declared panel 
𝐼
𝑊
I
W
	​

 whose rows share workload 
𝑊
W and anchor object 
𝐴
𝑊
A
W
	​

, publish:

𝜙
𝐶
,
𝑊
=
0.25
 
𝑆
𝐷
𝑖
∈
𝐼
𝑊
(
𝑆
𝐶
,
𝑖
)
0.25
 
𝑆
𝐷
𝑖
∈
𝐼
𝑊
(
𝑆
𝐶
,
𝑖
)
+
0.75
 
𝑆
𝐷
𝑖
∈
𝐼
𝑊
(
𝑆
𝑄
,
𝑖
)
.
ϕ
C,W
	​

=
0.25SD
i∈I
W
	​

	​

(S
C,i
	​

)+0.75SD
i∈I
W
	​

	​

(S
Q,i
	​

)
0.25SD
i∈I
W
	​

	​

(S
C,i
	​

)
	​

.

Use the same panel for both standard deviations. Show the panel size and excluded rows beside the statistic. Return “undefined—no composite dispersion” when the denominator is zero. Keep the existing mixed-table calculation if useful, but do not use it as the sole basis for a common-workload cost-influence claim. This changes neither the fixed 25% cost weight nor subset-row scoring.

3. Questions for the owner

Is evidence-class priority intended to override even certified economic dominance between eligible routes? If yes, retain E85 unchanged, but describe the official route as “evidence-priority selected,” not as the configuration’s lowest-cost eligible subscription route.

Should ValueRank’s GDPval leaf represent the current fitted benchmark record or the frozen contribution used when AA admitted the configuration to its Intelligence Index? This determines both the primary field and the treatment of rating-only refreshes.

4. Verdict

VERDICT: HAS FEEDBACK