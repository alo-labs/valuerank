1. Findings by severity
Critical

O15 changes the scored workload, but the Plan transport target has not been migrated.

Issue: API cost now means the phased SDLC basket, while Plan identification and certification still target 
𝑀
AA-mix
M
AA-mix
	​

, defined for AA’s suite workload. The draft then computes basket cost divided by that suite-targeted multiple. A multiple identified for the former workload is not automatically identified for the new one. This is a new consequence of O15, not a repetition of reviewer 9’s already-adopted transport finding.
paste.txt

Why it hurts the objective: A Plan route could satisfy the written certification gate while its effective cost for the scored SDLC workload remains unidentified. Removing knowledge-heavy evaluations and adding coding evaluations can change token-category shares and consumption against binding quota pools.

Concrete change: Define a versioned target workload 
𝑊
𝑣
W
v
	​

 containing the exact scored basket, task multiplicities, configuration and deployment policies. Replace the governing target with 
𝑀
𝑊
𝑣
M
W
v
	​

	​

, and compute 
𝐶
Plan
,
𝑖
=
𝐶
𝑊
𝑣
,
𝑖
/
𝑀
𝑊
𝑣
,
𝑖
C
Plan,i
	​

=C
W
v
	​

,i
	​

/M
W
v
	​

,i
	​

. Existing AA-suite transport evidence qualifies only if its public capacity model or conservative transport bound also covers 
𝑊
𝑣
W
v
	​

. O16 can remain: unidentified routes stay scored and flagged, but cannot be certified for the basket.

High

The executable certificate still has two incompatible quality estimands.

Issue: Reviewer 10 adopted common-support certification with no missing-leaf fills, but the normative certificate still defines 
𝑉
𝑖
V
i
	​

 using the full-composite 
𝑄
𝑖
(
𝜃
)
Q
i
	​

(θ), and still lists missing-leaf bounds inside 
Θ
cert
Θ
cert
	​

. The draft does not give the replacement pair-specific quality formula or say whether retained weights are renormalised.
paste.txt

Why it hurts the objective: Two compliant implementations can produce different certificates. Renormalisation also changes the trade-off: at 70% common coverage, dividing by 0.70 amplifies the retained quality contribution relative to cost.

Concrete change: Specify 
𝐵
𝑖
𝑗
B
ij
	​

, its total weight 
𝑝
𝑖
𝑗
p
ij
	​

, the exact pairwise score formula, and pair-specific gates. Keep full-composite bounds for frontier and threshold outputs explicitly separate. Add a release test that certification results match between the prose-level and executable definitions.

What is new: The issue is not whether to adopt common support—that was decided—but that the governing executable specification has not implemented that decision.

The Omniscience denominator is substantively wrong.

Issue: The draft defines non-hallucination as 
1
−
𝑖
/
(
𝑐
+
𝑝
+
𝑖
)
1−i/(c+p+i), conditioned on non-abstentions. AA currently defines hallucination as incorrect divided by incorrect + partial + not attempted, so the corresponding non-hallucination denominator is 
𝑖
+
𝑝
+
𝑎
i+p+a, not 
𝑐
+
𝑝
+
𝑖
c+p+i. AA’s accuracy denominator is all questions.
paste.txt
artificialanalysis

Why it hurts the objective: The draft rewards a different behaviour from the source metric, changing reliability scores and potentially rankings. Merely pinning the field name does not resolve the conflict because the explicit count formula governs.

Concrete change: Use 
𝐴
=
100
𝑐
/
(
𝑐
+
𝑝
+
𝑖
+
𝑎
)
A=100c/(c+p+i+a) and 
𝑁
=
100
[
1
−
𝑖
/
(
𝑖
+
𝑝
+
𝑎
)
]
N=100[1−i/(i+p+a)], retaining ValueRank’s chosen 
𝑧
=
(
2
𝐴
+
𝑁
)
/
3
z=(2A+N)/3. Specify the zero-denominator convention and test reconstructed values against AA’s published fields.

What is new: This is a verified source-definition mismatch, not another objection to the already-decided 2:1 weighting.

The “common basket” can change the economic yardstick when cohort membership or capture availability changes.

Issue: An evaluation enters only when every ranked row has exact-configuration cost. The draft specifies entry but not what happens when a later near-frontier entrant lacks an already-admitted evaluation, or a source withdraws one row. It also treats some benchmark changes as comparability reviews without explicitly governing cost-basket composition changes.
paste.txt

Why it hurts the objective: Either the basket silently shrinks, the refresh becomes impossible, or one row lacks cost. Shrinking changes every model’s workload, Plan transport target and potentially rank even when its evidence is unchanged.

Concrete change: Freeze basket membership within a workload version. An unavailable exact cost stays missing; the row remains listed without a value score, consistent with the existing no-cost rule. Adding or removing basket components requires an explicit workload migration, overlap comparison and Plan-transport revalidation.

What is new: This concerns O15’s newly introduced all-row admission dependency, not the rejected demand for a mandatory common quality panel.

Basket accounting does not yet rule out aggregate/component double counting or inconsistent repetition exposure.

Issue: “Coding Agent Index benchmarks (incl. DeepSWE)” appears beside named evaluations, but the accounting contract does not explicitly forbid adding an aggregate run cost and its constituent costs, or counting overlapping components twice. Nor does it define one consistent exposure unit when published costs include repeated evaluation runs.
paste.txt

Why it hurts the objective: The price of the basket can depend on how a source packages its benchmark results rather than on the intended workload.

Concrete change: Represent the basket as unique execution components, with explicit task multiplicities and repetition treatment. Aggregate costs must be either a reconciliation check or an exclusive substitute for their components—never additive to them. Publish a machine-checkable accounting tree.

What is new: Attempts reconciliation is already adopted for quality/cost compatibility; the additional requirement here is accounting integrity for O15’s expanded scored basket.

Medium

Pair-specific certificates need a different presentation from a single scalar ranking.

Issue: A candidate is compared against different opponents using different common leaf sets. The draft appropriately avoids transitive tie groups, but does not explicitly prevent readers from interpreting a common-support certificate as proof that the candidate’s displayed headline score is globally highest.
paste.txt

Why it hurts the objective: Pairwise statements can be valid individually without defining one shared scalar ordering. Cycles can arise when different comparisons retain different leaves; this is an algebraic consequence of changing the comparison function, not measurement uncertainty.

Concrete change: Publish a directed certification matrix with each pair’s retained weight, dropped leaves and margin. Describe an undefeated candidate as “certified against each listed competitor on pair-specific common evidence.” Explicitly allow cycles, no undefeated candidate, and a displayed-score leader that differs from the certified candidate.

What is new: This is not a request to reverse common-support certification; it addresses the interpretation introduced by that adopted design.

The matched-cost blocker contains stale variable names and unresolved precedence.

Issue: The normative formula still uses 
𝐶
total
C
total
, while O15 makes the basket the scored input. The prose adds a pairwise cost-order reversal blocker, but the normative blocker only specifies the median-relative ratio/rank rule. Earlier prose also restricts source joins differently from the later permissive priced-leaf definition.
paste.txt

Why it hurts the objective: Implementers can block recommendations using different reference costs and different tests.

Concrete change: Define 
𝐶
basket
C
basket
 separately from diagnostic 
𝐶
Index
C
Index
. Specify whether certification fails on either blocker, and define the reversal rule in equations, including ties and uncertain cost intervals. Give each permitted priced-leaf source a registry-level compatibility rule.

Printed cost/quality exchange rates will become stale after re-anchoring.

Issue: The headline retains approximately −2.9 API and −2.3 Plan value points per cost doubling, while O15 requires new basket-unit anchors. Those numbers are not invariant to the anchor ratio.
paste.txt

Why it hurts the objective: The explanation of the owner’s 25:75 trade-off may contradict the implemented score.

Concrete change: Generate the displayed exchange rate from the actual anchor version. Explain that the constant trade-off applies only in the unclipped region; crossing or remaining beyond an anchor changes the realised score movement.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the scored workload a first-class versioned object

Define the workload using unique execution components:

𝑊
𝑣
=
{
(
𝑒
,
𝑛
𝑒
,
𝑑
𝑒
)
}
,
𝐶
𝑖
,
𝑊
𝑣
=
∑
𝑒
∈
𝑊
𝑣
𝑛
𝑒
 
𝑐
ˉ
𝑖
𝑒
(
𝑑
𝑒
)
,
W
v
	​

={(e,n
e
	​

,d
e
	​

)},C
i,W
v
	​

	​

=
e∈W
v
	​

∑
	​

n
e
	​

c
ˉ
ie
(d
e
	​

)
	​

,

where:

𝑒
e identifies a benchmark execution component and version;

𝑛
𝑒
n
e
	​

 is its frozen workload multiplicity;

𝑑
𝑒
d
e
	​

 identifies deployment attempts, retry policy and stack;

𝑐
ˉ
𝑖
𝑒
(
𝑑
𝑒
)
c
ˉ
ie
(d
e
	​

)
	​

 is cost per workload task, excluding extra evaluation repetitions unless deliberately included in the workload.

Use the existing public per-evaluation sources and captured charts; do not require private telemetry or infer unavailable exact-variant costs. AA exposes category-level evaluation cost breakdowns, which can support the accounting and transport records where published.
artificialanalysis

For Plan rows:

𝐶
Plan
,
𝑖
,
𝑊
𝑣
=
𝐶
𝑖
,
𝑊
𝑣
𝑀
𝑖
,
𝑊
𝑣
.
C
Plan,i,W
v
	​

	​

=
M
i,W
v
	​

	​

C
i,W
v
	​

	​

	​

.

Bind every transport result to the workload hash, price-list version and quota-schema version. If public receipts or a public capacity model cannot identify 
𝑀
𝑖
,
𝑊
𝑣
M
i,W
v
	​

	​

, preserve O16’s flagged score but mark certification unavailable. Do not let an old workload label supply identification for a new basket.

Priority 2 — Implement common-support certification as a separate function

For each pair:

𝐵
𝑖
𝑗
=
𝑂
𝑖
∩
𝑂
𝑗
,
𝑝
𝑖
𝑗
=
∑
𝑏
∈
𝐵
𝑖
𝑗
𝑤
𝑏
.
B
ij
	​

=O
i
	​

∩O
j
	​

,p
ij
	​

=
b∈B
ij
	​

∑
	​

w
b
	​

.

My recommended implementation is a renormalised common-support comparison:

𝑄
𝑖
(
𝑖
𝑗
)
(
𝜃
)
=
∑
𝑏
∈
𝐵
𝑖
𝑗
𝑤
𝑏
𝑧
𝑖
𝑏
(
𝜃
)
𝑝
𝑖
𝑗
,
Q
i
(ij)
	​

(θ)=
p
ij
	​

∑
b∈B
ij
	​

	​

w
b
	​

z
ib
	​

(θ)
	​

,
Δ
𝑖
𝑗
(
𝜃
)
=
0.25
[
𝑆
𝐶
(
𝑐
𝑖
(
𝜃
)
)
−
𝑆
𝐶
(
𝑐
𝑗
(
𝜃
)
)
]
+
0.75
[
𝑄
𝑖
(
𝑖
𝑗
)
(
𝜃
)
−
𝑄
𝑗
(
𝑖
𝑗
)
(
𝜃
)
]
.
Δ
ij
	​

(θ)=0.25[S
C
	​

(c
i
	​

(θ))−S
C
	​

(c
j
	​

(θ))]+0.75[Q
i
(ij)
	​

(θ)−Q
j
(ij)
	​

(θ)].

Certify the directed edge 
𝑖
→
𝑗
i→j only when:

Pair-specific coverage and SWE gates pass.

Required cost-shape and Plan-identification checks pass.

No qualifying unidentified observed input remains unbounded.

inf
⁡
𝜃
∈
Θ
𝑖
𝑗
Δ
𝑖
𝑗
(
𝜃
)
>
0
inf
θ∈Θ
ij
	​

	​

Δ
ij
	​

(θ)>0.

Here 
Θ
𝑖
𝑗
Θ
ij
	​

 contains uncertainties for retained evidence and relevant costs, not values for dropped leaves. Use exactly this estimand for S0 scenario support.

This preserves the adopted common-support policy while making the 25:75 comparison explicit. Publish the renormalisation factor 
1
/
𝑝
𝑖
𝑗
1/p
ij
	​

, because it reveals how far the comparison departs from the nominal full benchmark mix. Keep full-composite missing-data bounds for the separate outputs that require them. The draft already distinguishes those outputs conceptually; the implementation should enforce that separation.
paste.txt

Priority 3 — Add targeted executable tests, not more modelling layers

Add these tests to the existing suite:

Omniscience denominator: with 
𝑐
=
60
,
𝑝
=
0
,
𝑖
=
10
,
𝑎
=
30
c=60,p=0,i=10,a=30, verify 
𝐴
=
60
A=60, 
𝑁
=
75
N=75, and 
𝑧
=
65
z=65. The incorrect draft denominator produces a different result. The corrected denominator follows AA’s current public definition.
artificialanalysis

Aggregate/component exclusivity: replacing an aggregate with an exactly reconciled component decomposition leaves basket cost unchanged.

Evaluation repetition invariance: averaging additional independent evaluation repetitions does not multiply workload cost.

Workload migration: changing basket composition changes the workload identifier and invalidates unreviewed Plan transport.

Certificate isolation: changing a leaf dropped from 
𝐵
𝑖
𝑗
B
ij
	​

 cannot change that pair’s certificate.

Cyclic comparison handling: a synthetic three-model cycle produces no global certificate, rather than a forced winner.

Reference-cost consistency: every matched-cost blocker reads the intended basket cost, never the legacy Index diagnostic.

Priority 4 — Make exchange rates and release accounting computed outputs

With 
𝛽
=
0.25
β=0.25 and 
𝑅
=
𝑐
𝐻
/
𝑐
𝐿
R=c
H
	​

/c
L
	​

, an unclipped cost doubling changes value by

Δ
𝑉
×
2
=
−
100
𝛽
ln
⁡
2
ln
⁡
𝑅
.
ΔV
×2
	​

=−
lnR
100βln2
	​

.

The compensating increase in quality is

Δ
𝑄
×
2
=
100
𝛽
ln
⁡
2
(
1
−
𝛽
)
ln
⁡
𝑅
.
ΔQ
×2
	​

=
(1−β)lnR
100βln2
	​

.

Generate these directly from each basis’s anchors.

For every workload migration, publish an overlap bridge: old and new basket costs, scores and ranks for configurations evidenced under both versions. Attribute basket-composition changes separately from prices, token use and cohort changes. This extends the adopted decomposition specifically to O15’s new workload object rather than reopening the owner’s cost-basket decision.
paste.txt

3. Questions for the owner

Is common-support quality intended to be renormalised to 100% within each pair, preserving a 25:75 trade-off on retained evidence, or left in original-weight units, reducing quality’s possible contribution as support shrinks? This changes the governing certificate formula.

Is the SDLC basket intended to price one deployment-equivalent pass through each included task, or the evaluator’s full experimental execution including repeated runs? This determines repetition accounting and the workload transported into Plan capacity.

When a newly eligible cohort configuration lacks cost for an established basket component, should it remain in the table without a value score, or should the entire release be held? I recommend the former; either is implementable without imputation or changing the fixed cohort policy.

4. Verdict

VERDICT: HAS FEEDBACK