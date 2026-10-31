1. Findings by severity
Critical

The cost source and cohort chart no longer match AA’s current published metric.

Issue: The draft specifies total suite dollars and an Intelligence-vs-total-cost frontier. AA currently labels its rendered frontier “Intelligence Index vs. Cost per Task,” where cost is a weighted average per Intelligence Index task. Its methodology also incorporates cache-hit measurements and cache-token pricing. That contradicts both the draft’s source-field definition and its assertion that caching is not modelled.
artificialanalysis
+1

Why it hurts the objective: Substituting weighted cost per task for suite-total cost silently changes units, potentially changes the selected families, and invalidates dollar anchors. Refreshes could therefore change the meaning of the ranking without a method change.

Concrete change: Before release, pin an actual public AA chart/export and its exact field, units, suite version and accounting rules. If the owner intends the current rendered frontier, implement the fixed cohort policy on that chart and explicitly version the migration. If a historical total-cost field is intended, archive that snapshot and do not silently replace it.

What is new relative to the ledger: This is not another request to document the field; it is an observed mismatch between the adopted specification and the current source.

High

Dividing expenditure by AA Intelligence reintroduces a second, differently weighted quality measure.

Issue: With 
𝑐
=
𝐶
/
𝐼
A
A
c=C/I
AA
	​

, the unclipped cost score contains

𝑆
𝐶
=
100
ln
⁡
(
𝑐
𝐻
/
𝑐
𝐿
)
(
ln
⁡
𝑐
𝐻
−
ln
⁡
𝐶
+
ln
⁡
𝐼
A
A
)
.
S
C
	​

=
ln(c
H
	​

/c
L
	​

)
100
	​

(lnc
H
	​

−lnC+lnI
AA
	​

).

Thus AA intelligence still increases the headline score independently of ValueRank quality. AA’s current weights differ substantially from ValueRank’s, including 30% general capability and 20% scientific reasoning.
artificialanalysis

Why it hurts the objective: Two models with identical expenditure and identical ValueRank quality can receive different value scores solely because AA prefers one on another capability mix. Removing AA Intelligence from the quality table did not remove this indirect contribution.

Concrete change: Keep the owner’s 25/75 headline, but score cost from the pinned AA expenditure metric before dividing by intelligence. Retain USD per AA Index point as a diagnostic. Likewise, use expenditure—not expenditure divided by another quality index—for the buyer-facing frontier and cheapest-above-quality-bar views.

What is new: This is an algebraic consequence of the retained denominator, not a repetition of the adopted removal of AA Intelligence from quality.

Renormalised quality is being used as though every row measured the same construct.

Issue: A row missing engineering evidence can receive a high quality score mainly from general benchmarks. The existing provisional flag does not prevent that score from determining “cheapest above 70” or appearing on the frontier.

Why it hurts the objective: A buyer can receive a confident purchasing recommendation from a model that has not demonstrated the required capability mix. Reporting bounds beside that recommendation does not resolve the contradiction.

Concrete change: Retain all cohort rows, missing values and renormalised point scores. Make decision outputs bound-aware: distinguish confirmed versus possible threshold qualification, and definite versus possible frontier membership. Do not name a uniquely cheapest qualifying model unless both qualification and the relevant cost comparison are established.

What is new: The ledger adopted bounds and flags, but not rules governing how uncertainty changes purchasing recommendations.

The Plan multiplier lacks a common valuation basis and model-attributable numerator.

Issue: An accepted end-user report can still value usage using different API prices, cache treatment or dates from the AA cost being divided. It can also report a whole plan’s mixed-model usage rather than capacity delivered by the selected model.

Why it hurts the objective: API price changes can move Plan rankings even when subscription fees and delivered capacity have not changed. Mixed-model usage can incorrectly credit one model with another model’s allowance.

Concrete change: Require each multiplier to identify its fee period, workload, selected model/effort, token categories, valuation prices, and any shared usage pools. Where public token receipts exist, reprice numerator and AA workload consistently. Where they do not, preserve the report’s original valuation basis and mark the resulting transfer as an assumption rather than a matched measurement.

What is new: This does not change permitted evidence sources, remove owner-authorised assumptions, or introduce monthly-demand scenarios. It specifies when accepted evidence measures the quantity used in the formula.

“Highest eligible multiple” does not yet identify a purchasable, evidence-compatible route.

Issue: The draft allows effort mismatches to be flagged rather than resolving whether the selected configuration is actually available. It also mixes API fallbacks into a ranking for native-subscription buyers.

Why it hurts the objective: The apparent Plan winner may require an unavailable effort, a different app/harness, a restricted account tier, or API access rather than a subscription route. Separately taking the best quality evidence and best multiplier can produce a combination no buyer can obtain.

Concrete change: Calculate Plan results first at model–plan–surface–configuration level. Select the best compatible route only after joining its access conditions, evidence and multiplier. Preserve authorised mismatched transfers as explicitly assumed routes. Keep API fallback rows visible, but exclude them from native-Plan winner and frontier claims.

Bug Hunt’s 20% weight gives two repositories excessive influence over a broad software-engineering claim.

Issue: Bug Hunt contains 105 bugs but only two production TypeScript codebases; each run fixes multiple bugs in one repository-level session. Its public results also show repeat-run variation and different harness/serving routes.
github

Why it hurts the objective: Counting 105 bugs can suggest much broader independent evidence than two environments provide. At full coverage, this narrow test controls 15% of the entire headline score; missing-data renormalisation can increase its influence further.

Concrete change: Reduce Bug Hunt to 10% of quality while retaining the 60% engineering group. Allocate the released 10% to broader repository-level engineering evidence, with a published alternative-weight sensitivity. Bootstrap whole runs, not 105 supposedly independent Bernoulli trials.

What is new: The concern is repository concentration and the unit of inference, not merely the already acknowledged model+harness limitation.

Medium

Several scored quantities remain insufficiently specified for reproducible implementation.

Issue: “Accuracy-weighted reliability” supplies no formula. GDPval’s bounded transform is unspecified, and the four-test science sub-basket does not say how missing children affect its weight. AA publishes Omniscience accuracy and non-hallucination separately and uses an explicit frozen GDPval transform.
artificialanalysis

Why it hurts the objective: Implementers can produce materially different ranks from the same evidence.

Concrete change: Publish executable equations for every leaf and group, including missing-child propagation. For Omniscience, use a declared weighted arithmetic combination rather than an undefined product or conditional metric.

Rank bands conflate fundamentally different uncertainties.

Issue: Sampling intervals, missing-data bounds, multiplier ranges and leave-one-source-out results answer different questions.

Why it hurts the objective: A single band can imply statistical confidence where there is only a stress test or an unidentified quantity.

Concrete change: Publish separate measurement, identification and methodological-sensitivity outputs. Preserve shared dependencies: one plan multiplier, price update or benchmark version must move all affected rows together.

What is new: The ledger adopted the ingredients; this specifies their interpretation and joint propagation.

The stated market claim exceeds the selection and measurement scope.

Issue: An AA-selected configuration is not necessarily the configuration best suited to ValueRank’s engineering-heavy objective. The suite is also primarily text-based and English-language.
artificialanalysis

Why it hurts the objective: “Actually lowest cost in practice” can be read as a market-wide optimum across configurations and workloads that the fixed cohort cannot establish.

Concrete change: State the claim as “value among AA-selected frontier and near-frontier configurations, under the published benchmark mix.” Do not broaden the cohort or transfer evidence.

Low

None.

2. Methodology design recommendations

Establish a versioned source contract before calculating scores. Publish one machine-readable registry containing:

AA chart identity, selected filters and snapshot timestamp.

Cost field name, unit and accounting treatment.

Exact model/version, effort, fallback, serving route and benchmark-specific stack.

Benchmark version, raw metric, evaluated population, attempts and aggregation.

Source revision or commit, observation date and retrieval date.

Explicit missingness reason: not evaluated, incompatible variant, unavailable public evidence, or withdrawn result.

AA’s current public methodology and Bug Hunt’s public JSON/CSV receipts provide practical starting points. Do not reconstruct hidden suite totals from weighted cost-per-task figures.
artificialanalysis
+1

Separate expenditure from quality in all decision calculations. After resolving the source contract, let 
𝐶
𝑖
C
i
	​

 be the pinned AA expenditure metric and 
𝑀
𝑖
𝑟
M
ir
	​

 the eligible multiplier for route 
𝑟
r:

𝑐
𝑖
,
A
P
I
=
𝐶
𝑖
,
𝑐
𝑖
𝑟
,
P
l
a
n
=
𝐶
𝑖
𝑀
𝑖
𝑟
,
c
i,API
	​

=C
i
	​

,c
ir,Plan
	​

=
M
ir
	​

C
i
	​

	​

,
𝑉
𝑖
𝑏
=
0.25
𝑆
𝐶
(
𝑐
𝑖
𝑏
)
+
0.75
𝑄
𝑖
.
V
ib
	​

=0.25S
C
	​

(c
ib
	​

)+0.75Q
i
	​

.

Keep the frozen logarithmic cost transform, but set its anchors in the actual expenditure unit. The illustrative “$1–$300 per point” anchors cannot carry over unchanged. This preserves O2 and O3. It does not claim dollars per successful engineering task, which remains deferred.

Make incomplete evidence actionable without imputing it. For fixed leaf weights 
𝑤
𝑗
w
j
	​

, observed set 
𝑂
𝑖
O
i
	​

, and transformed evidence intervals 
[
ℓ
𝑖
𝑗
,
𝑢
𝑖
𝑗
]
[ℓ
ij
	​

,u
ij
	​

]:

𝑄
𝑖
−
=
∑
𝑗
∈
𝑂
𝑖
𝑤
𝑗
ℓ
𝑖
𝑗
,
𝑄
𝑖
+
=
∑
𝑗
∈
𝑂
𝑖
𝑤
𝑗
𝑢
𝑖
𝑗
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
−
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

ℓ
ij
	​

,Q
i
+
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

u
ij
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

Missing endpoints represent identification limits, not filled-in observations. For a quality bar 
𝑡
t:

Confirmed qualifying: 
𝑄
𝑖
−
≥
𝑡
Q
i
−
	​

≥t.

Possibly qualifying: 
𝑄
𝑖
−
<
𝑡
≤
𝑄
𝑖
+
Q
i
−
	​

<t≤Q
i
+
	​

.

Not qualifying: 
𝑄
𝑖
+
<
𝑡
Q
i
+
	​

<t.

With cost interval 
[
𝑐
𝑖
−
,
𝑐
𝑖
+
]
[c
i
−
	​

,c
i
+
	​

], model 
𝑗
j definitely dominates 
𝑖
i if

𝑐
𝑗
+
≤
𝑐
𝑖
−
,
𝑄
𝑗
−
≥
𝑄
𝑖
+
,
c
j
+
	​

≤c
i
−
	​

,Q
j
−
	​

≥Q
i
+
	​

,

with at least one strict inequality. Otherwise distinguish possible dominance from established dominance. A uniquely cheapest confirmed recommendation additionally requires its worst-case cost to beat every other possibly qualifying candidate’s best-case cost. When that cannot be established, publish a candidate set.

Define Plan multipliers as auditable route-level measurements. Where public receipts support it, calculate

𝑀
𝑖
𝑟
=
∑
𝑘
𝑛
𝑖
𝑟
𝑘
𝑝
𝑖
𝑘
𝐹
𝑟
,
M
ir
	​

=
F
r
	​

∑
k
	​

n
irk
	​

p
ik
	​

	​

,

where 
𝑛
𝑖
𝑟
𝑘
n
irk
	​

 counts delivered input, cache-read, cache-write, reasoning and answer tokens over the stated fee period; 
𝑝
𝑖
𝑘
p
ik
	​

 uses the same valuation convention as 
𝐶
𝑖
C
i
	​

; and 
𝐹
𝑟
F
r
	​

 is the fee for that period. Record whether capacity was actually exhausted and which rate-limit windows constrained it. Do not extrapolate a short burst to a billing period unless the allowed controlled measurement establishes that extrapolation. For 
𝑀
∈
[
𝑀
−
,
𝑀
+
]
M∈[M
−
,M
+
]:

𝑐
P
l
a
n
∈
[
𝐶
−
𝑀
+
,
𝐶
+
𝑀
−
]
.
c
Plan
	​

∈[
M
+
C
−
	​

,
M
−
C
+
	​

].

Select the best eligible route within each joint scenario, rather than selecting the largest point estimate and ignoring route-selection uncertainty. Preserve O4’s authorised assumptions, but identify their donor measurement and transfer explicitly.

Adopt a more diversified engineering allocation and fully specify leaf formulas. A concrete proposed quality allocation is:
Engineering benchmark	Share of total quality
DeepSWE v1.1	30%
Bug Hunt	10%
Terminal-Bench 4.0	10%
FrontierCode 1.1	10%
FrontierCode evaluates code changes to open-source repositories using tests and rubric grading, with blocking failures scoring zero. That supplies a different engineering task structure from unrestricted bug hunting. Use only publicly reported exact-variant evidence; absent matches remain missing.
artificialanalysis
 For other leaves:

GDPval-AA v2.1: adopt and freeze 
𝑧
=
100
 
c
l
i
p
(
(
𝐸
−
500
)
/
2000
,
0
,
1
)
z=100clip((E−500)/2000,0,1), explicitly matching AA’s published integration transform.
artificialanalysis

Omniscience: a transparent starting policy is 
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
z=(2A+N)/3, where 
𝐴
A and 
𝑁
N are percentage accuracy and non-hallucination. This preserves AA’s published 2:1 relative emphasis while keeping one ValueRank leaf.
artificialanalysis

Science sub-basket: assign each of its four children 1.25% of total quality. Keep those as fixed leaf weights when calculating coverage and bounds.

Publish three uncertainty layers, not one blended confidence band.

Measurement: published intervals, rounding and appropriately clustered resampling.

Identification: missing benchmark evidence and unmeasured Plan quantities.

Specification: benchmark weights, source omission and authorised transfer assumptions.

For Bug Hunt, public per-run/per-repository data support repeat-run sensitivity conditional on those repositories. They do not establish generalisation across the universe of software repositories.
github
 Publish robust pairwise ordering only when it survives the declared joint scenarios. Do not turn overlapping intervals into transitive “tie groups”: overlap between A–B and B–C does not establish equivalence between A–C.

3. Questions for the owner

Is the intended AA cohort source the current rendered cost-per-task frontier, or an archived total-suite-cost frontier? Which public snapshot/export establishes the intended units?

Is dividing cost by AA Intelligence itself an owner requirement, beyond the fixed 25/75 headline? If so, the ranking should explicitly disclose AA Intelligence as a second quality contribution rather than claim it has been removed.

Does the authorised Plan-assumption policy cover only named model-to-model transfers, or also effort, surface, workload and price-basis transfers? That determines which route results can remain official assumptions versus unmatched evidence.

Can the engineering leaf weights change within the adopted 60% group? If not, the repository-concentration finding should remain a prominently quantified limitation rather than trigger reallocation.

4. Verdict

VERDICT: HAS FEEDBACK