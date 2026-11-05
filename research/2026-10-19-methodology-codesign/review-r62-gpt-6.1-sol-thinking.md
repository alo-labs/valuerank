0. Read check

First line, exactly:

ValueRank methodology — draft r56

Last 12 whitespace-delimited words of each part, in order:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> a bias bound in the identification layer); repetitions are not a bias.

> No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

> candidate's cost upper bound); otherwise "not established", with the omitted competitors listed.

> or definite result; every cost check reads C_W, never the Index diagnostic.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

All seven parts were read through their ends through the GitHub connector at the specified commit. The review below uses those complete reads, not the repository’s indexed description. The public repository is listed under Ālo Labs.
github

1. Findings by severity
Critical

None.

High

E170’s “block but never enable” exception is not integrated into the governing interval decision definitions.

Issue: Part 7 says a superseded-price row earns no interval label but competes against other rows using the hull of its published-record and current-tariff costs. However, Part 5 defines frontier and bar competitors through 
𝑅
𝑊
R
W
	​

, and the formal predicates quantify only over that set. There is no separate blocker population or complete rule specifying which cost domain the solver uses for these exceptional competitors. The selected-cohort extension addresses omitted competitors, but it does not explicitly implement E170 inside the within-evaluable-set decisions.

Why it hurts the objective: Two implementations could disagree materially: one might remove the stale-price row entirely and award another configuration a definite-frontier or confirmed-cheapest label; another might retain it as a blocker. The latter is what E170 intends. This ambiguity affects actionable lowest-cost claims, not merely diagnostics.

Concrete change: Separate label candidates from potential blockers in the normative equations. Compile E170 competitors into every relevant frontier and bar decision, with an explicit published-record/current-tariff hull and the original dependency constraints. Specify how they enter possible-frontier and possible-cheapest membership as well as confirmed labels.

What is new relative to E170: This does not challenge O29 or request another tariff flag. It identifies an incomplete connection between the adopted exception and the executable quantifiers that must enforce it.

Medium

E182 does not specify a sampling law when the published point coincides with a confidence-interval endpoint.

Issue: Part 4 requires half the kernel mass on each side of an asymmetric or clipped interval’s published point. If the point is the lower endpoint, the left side has zero length; if it is the upper endpoint, the right side does. Neither “uniform on each side” nor the rescaled arcsine alternative defines the zero-length case explicitly. A point interval presents the same problem twice.

Why it hurts the objective: The scenario build requires executable kernel parameters and reproducible draws. Different implementations could introduce an atom, discard the empty side, or fail. Those choices produce different S1M frequencies precisely for configurations near a score boundary.

Concrete change: Define a zero-length side as a point mass at the published point; define a fully degenerate interval as a point mass with probability one. Validate that the point lies inside the captured interval after the registered transformation.

What is new relative to E182: E182 resolves unequal nonzero side lengths. This finding concerns its remaining zero-length boundary cases, not the adopted median-preserving design.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the E170 blocker population executable

Introduce three explicit sets per basis and workload:

𝐸
𝑊
E
W
	​

: ordinary interval-evaluable rows.

𝐿
𝑊
⊆
𝐸
𝑊
L
W
	​

⊆E
W
	​

: rows eligible to receive the particular label.

𝐵
𝑊
B
W
	​

: E170 superseded-price rows retained only as competitors.

Use the competitor universe 
𝑈
𝑊
=
𝐸
𝑊
∪
𝐵
𝑊
U
W
	​

=E
W
	​

∪B
W
	​

, while awarding labels only to eligible candidates.

For a blocker 
𝑏
b, define its cost domain by:

𝐶
𝑏
b
l
o
c
k
=
hull
⁡
(
𝐶
𝑏
p
u
b
l
i
s
h
e
d
,
𝐶
𝑏
c
u
r
r
e
n
t
)
.
C
b
block
	​

=hull(C
b
published
	​

,C
b
current
	​

).

This is an outer admissible domain, not a sampling distribution. Preserve all evidenced shared constraints; do not independently draw its endpoints.

For example, definite-frontier membership becomes:

𝑖
∈
𝐿
𝑊
∧
∀
𝜃
∈
Θ
†
,
 
∄
𝑗
∈
𝑈
𝑊
∖
{
𝑖
}
:
𝑗
≻
𝜃
𝑖
.
i∈L
W
	​

∧∀θ∈Θ
†
, ∄j∈U
W
	​

∖{i}:j≻
θ
	​

i.

Apply the same competitor universe consistently to confirmed-cheapest and possible-cheapest decisions. A blocker’s own membership or label remains unavailable under O29.

Add regression fixtures:

A stale-price row dominates a candidate at its published cost but not its current-tariff cost: the candidate cannot be definite.

The reverse situation: the candidate still cannot be definite.

A potentially qualifying, cheaper stale-price row blocks confirmed-cheapest.

The blocker itself receives no interval label.

Adding the blocker cannot strengthen another row’s label.

A basis-incompatible or unidentified Plan multiple does not become identified merely because the row is a blocker.

If a blocker’s required domain cannot be constructed, return an explicit unresolved result for the affected claim rather than silently removing that competitor. This changes no scoring weights, cohort policy, or owner-required displayed ranking.

Priority 2 — Complete the two-sided kernel contract

For transformed interval 
[
𝐿
,
𝑈
]
[L,U] and published point 
𝑚
m, require 
𝐿
≤
𝑚
≤
𝑈
L≤m≤U. Define:

𝐾
=
1
2
𝐾
[
𝐿
,
𝑚
]
+
1
2
𝐾
[
𝑚
,
𝑈
]
,
K=
2
1
	​

K
[L,m]
	​

+
2
1
	​

K
[m,U]
	​

,

where each nondegenerate side uses its registered uniform or arcsine law, and:

𝐾
[
𝑎
,
𝑎
]
=
𝛿
𝑎
.
K
[a,a]
	​

=δ
a
	​

.

Consequences:

𝐿
=
𝑚
<
𝑈
L=m<U: half the mass is an atom at 
𝑚
m.

𝐿
<
𝑚
=
𝑈
L<m=U: half the mass is an atom at 
𝑚
m.

𝐿
=
𝑚
=
𝑈
L=m=U: all mass is at 
𝑚
m.

Publish these atoms in the kernel object. Add fixtures for both endpoint cases, a point interval, and an ordinary asymmetric interval. Keep the existing S1M interpretation and tail limitations unchanged.

These two recommendations are implementation completions. Neither requires additional private evidence, new benchmark collection, imputation, or a change to an owner decision.

3. Questions for the owner

None.

4. Verdict

The remaining material issue is the gap between E170’s intended competitor treatment and the normative interval equations. The other finding completes a reproducibility boundary case. Neither requires reopening the fixed cohort, exact-variant evidence, Value Multiple numerator rules, or headline weights. The draft needs these targeted corrections rather than another expansion of its diagnostic framework.

VERDICT: HAS FEEDBACK