1. Findings by severity
Critical

Mathematical contradiction between log-cost ratio scoring and pairwise cert margin

The issue: In the prose and headline definition, cost is scored logarithmically:

𝑆
𝐶
=
100
⋅
clip
⁡
(
ln
⁡
𝑐
𝐻
−
ln
⁡
𝑐
ln
⁡
𝑐
𝐻
−
ln
⁡
𝑐
𝐿
,
0
,
1
)
S
C
	​

=100⋅clip(
lnc
H
	​

−lnc
L
	​

lnc
H
	​

−lnc
	​

,0,1)

where a cost doubling changes the cost score by 
100
ln
⁡
2
/
(
ln
⁡
𝑐
𝐻
−
ln
⁡
𝑐
𝐿
)
100ln2/(lnc
H
	​

−lnc
L
	​

). However, in the pairwise certificate specification governing certification, the draft states:

Δ
𝑖
𝑗
=
0.25
⋅
(
𝑆
𝐶
(
𝐶
𝑖
,
𝑊
)
−
𝑆
𝐶
(
𝐶
𝑗
,
𝑊
)
)
+
0.75
⋅
(
𝑄
𝑖
∣
𝑖
𝑗
−
𝑄
𝑗
∣
𝑖
𝑗
)
Δ
ij
	​

=0.25⋅(S
C
	​

(C
i,W
	​

)−S
C
	​

(C
j,W
	​

))+0.75⋅(Q
i∣ij
	​

−Q
j∣ij
	​

)

while simultaneously defining the "implied exchange rate" across releases as 
Δ
𝑉
=
0.25
Δ
𝑆
𝐶
+
0.75
Δ
𝑄
ΔV=0.25ΔS
C
	​

+0.75ΔQ with subset calibration contract E10 defining subset-specific anchors 
(
𝑐
𝐿
,
𝑆
,
𝑐
𝐻
,
𝑆
)
(c
L,S
	​

,c
H,S
	​

). Because 
𝑆
𝐶
(
𝑐
𝑖
)
−
𝑆
𝐶
(
𝑐
𝑗
)
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
ln
⁡
(
𝑐
𝑗
/
𝑐
𝑖
)
S
C
	​

(c
i
	​

)−S
C
	​

(c
j
	​

)=
ln(c
H
	​

/c
L
	​

)
100
	​

ln(c
j
	​

/c
i
	​

), the pairwise cost difference depends strictly on the cohort anchor spread 
ln
⁡
(
𝑐
𝐻
/
𝑐
𝐿
)
ln(c
H
	​

/c
L
	​

). If candidate 
𝑖
i is evaluated on subset workload 
𝑊
𝑆
W
S
	​

 and candidate 
𝑗
j on full basket 
𝑊
W, their anchors 
(
𝑐
𝐿
,
𝑆
,
𝑐
𝐻
,
𝑆
)
(c
L,S
	​

,c
H,S
	​

) versus 
(
𝑐
𝐿
,
𝑊
,
𝑐
𝐻
,
𝑊
)
(c
L,W
	​

,c
H,W
	​

) differ. Subtracting raw 
𝑆
𝐶
S
C
	​

 across different workloads or when dropping leaves with leaf-cost dependencies produces an uncalibrated exchange rate.

Why it hurts the objective: ValueRank's primary claim is to tell buyers which frontier model is actually lowest cost for value delivered in practice. If the cost anchor scale changes depending on whether a model is evaluated on a subset or full basket, the trade-off exchange rate (dollars to quality points) fluctuates arbitrarily between model pairs, rendering certification mathematically inconsistent.

Concrete change recommended: Enforce in the normative pairwise certificate that 
Δ
𝑖
𝑗
Δ
ij
	​

 evaluates cost using the exact common-support basket 
𝑊
𝑖
𝑗
W
ij
	​

 and its dedicated versioned anchor pair 
(
𝑐
𝐿
,
𝑖
𝑗
,
𝑐
𝐻
,
𝑖
𝑗
)
(c
L,ij
	​

,c
H,ij
	​

), or define the cost component in 
Δ
𝑖
𝑗
Δ
ij
	​

 invariant to subset scaling via a fixed global elasticity constant 
𝜅
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
κ=
ln(c
H
	​

/c
L
	​

)
100
	​

 registered per release across all common-support slices.

Non-monotonic collapse of time-indexed LP for multi-pool subscription quotas under unobserved burst arrival

The issue: The draft mandates a time-indexed linear program:

max
⁡
∑
𝑡
𝑦
𝑡
subject to
∑
𝑡
∈
𝑊
𝑎
𝑤
𝑡
𝑦
𝑡
≤
𝐵
𝑤
max
t
∑
	​

y
t
	​

subject to
t∈W
∑
	​

a
wt
	​

y
t
	​

≤B
w
	​


as the sole governing Plan capacity calculation over rolling windows (e.g., 5-hour and weekly caps). However, real-world subscription CLI/coding workloads (such as Claude Code or Codex) do not submit perfectly flat, deterministic workloads across arbitrary 5-hour blocks 24/7 over 30 days. Real developer usage exhibits diurnal clustering and burst windows. Under the LP formulation, a model with a tiny 5-hour window and a loose weekly window is assigned an unrealistic theoretical maximum that requires perfectly scheduled 24/7 utilization.

Why it hurts the objective: Buyers relying on the Plan ranking are misinformed: a plan that mathematically admits high theoretical throughput under an unconstrained 24/7 linear program can be completely unusable during an 8-hour workday due to aggressive short-window throttling (e.g., hitting the 5-hour limit 2 hours into a session).

Concrete change recommended: Bound the time-indexed LP by an empirical diurnal duty cycle parameter 
𝐷
∈
[
0
,
1
]
D∈[0,1] (e.g., active developer work-window constraint of 8–10 hours/day, or pre-registered 40-hour work week vs 168-hour continuous saturation), and publish both the 168-hour maximum saturation multiple and the realistic 40-hour burst-constrained multiple.

High

Inconsistency between pairwise common-support certification and 70% threshold gating on missing SWE leaves

The issue: Under the normative definitions, pairwise edge certification drops leaves missing for either row to form common support 
𝐵
𝑖
𝑗
B
ij
	​

, requiring retained common-support weight 
𝑝
𝑖
𝑗
≥
0.70
p
ij
	​

≥0.70 and SWE gates met. However, DeepSWE v1.1 alone carries 30% of total quality weight (50% of the SWE group). If model 
𝑖
i has DeepSWE and Bug Hunt (40% SWE weight) and model 
𝑗
j has FrontierCode, Terminal-Bench 4.0, and Bug Hunt (30% SWE weight), their common SWE support is only Bug Hunt (10%), which fails the rule requiring at least 2 common SWE leaves and 40% observed SWE weight.

Why it hurts the objective: Because non-AA independent benchmarks (Bug Hunt, Terminal-Bench) are only partially refreshed across models while proprietary provider suites drop certain benchmarks, pairwise certification will frequently evaluate to "unevaluable" across major frontier contenders, neutralizing the headline "recommended" certification.

Concrete change recommended: Formally define the common-support SWE gate at the pair level 
𝐵
𝑖
𝑗
B
ij
	​

: require 
𝑝
𝑖
𝑗
,
SWE
≥
0.30
p
ij,SWE
	​

≥0.30 (rather than 0.40) and at least 1 common anchor SWE benchmark whenever both models independently meet the individual row provisional threshold (coverage 
≥
0.70
≥0.70 and observed SWE 
≥
0.40
≥0.40).

Conflation of task retries and multi-attempt variance in the matched-cost API cost-shape check

The issue: The matched-cost blocker compares 
𝐶
𝑖
,
match
=
∑
𝑏
∈
𝐵
𝑤
𝑏
′
𝑐
𝑖
𝑏
C
i,match
	​

=∑
b∈B
	​

w
b
′
	​

c
ib
	​

 to basket cost 
𝐶
𝑖
,
𝑊
C
i,W
	​

. The draft states that 
𝑐
𝑖
𝑏
c
ib
	​

 must divide out evaluation repetitions but include deployment retries. However, benchmark providers (including Artificial Analysis and SWE-bench variants) do not publish uniform accounting of token expenditures on failed intermediate steps versus execution environment setup and verifier passes.

Why it hurts the objective: A model running in a scaffold that logs retries as separate runs will fail the 1.5 ratio / 3-rank blocker against a model whose provider reported only the final successful execution pass tokens, creating false-positive certification disqualifications based on harness telemetry rather than true model inference efficiency.

Concrete change recommended: Standardize 
𝑐
𝑖
𝑏
c
ib
	​

 in the registry strictly to net API token counts (input, reasoning, output, cache-read) multiplied by the primary price list, removing non-inference harness charges from the matched-cost panel.

Medium

Omniscience formula non-monotonicity at zero attempt boundaries

The issue: The formula for AA-Omniscience quality uses:

𝐴
=
100
⋅
𝑐
𝑐
+
𝑝
+
𝑖
+
𝑎
,
𝑁
=
100
⋅
(
1
−
𝑖
𝑖
+
𝑝
+
𝑎
)
,
𝑧
=
2
𝐴
+
𝑁
3
A=100⋅
c+p+i+a
c
	​

,N=100⋅(1−
i+p+a
i
	​

),z=
3
2A+N
	​


with the exception rule "
𝑁
=
100
N=100 when 
𝑖
+
𝑝
+
𝑎
=
0
i+p+a=0". If a model answers all questions correctly (
𝑐
=
100
,
𝑝
=
0
,
𝑖
=
0
,
𝑎
=
0
c=100,p=0,i=0,a=0), 
𝑖
+
𝑝
+
𝑎
=
0
i+p+a=0, yielding 
𝐴
=
100
,
𝑁
=
100
,
𝑧
=
100
A=100,N=100,z=100. But if a model attempts all questions and gets 99 correct, 1 partial, and 0 incorrect, 
𝑐
=
99
,
𝑝
=
1
,
𝑖
=
0
,
𝑎
=
0
c=99,p=1,i=0,a=0; then 
𝑖
/
(
𝑖
+
𝑝
+
𝑎
)
=
0
/
1
=
0
i/(i+p+a)=0/1=0, giving 
𝑁
=
100
N=100, whereas if it had 1 unattempted (
𝑎
=
1
,
𝑖
=
0
a=1,i=0), 
𝑁
N is still 100. Conversely, if a cautious model skips difficult questions (
𝑎
a is high, 
𝑖
i is low), 
𝑁
N remains high despite low accuracy 
𝐴
A, creating perverse incentives where abstention is over-rewarded relative to wrong guesses.

Why it hurts the objective: Reliability and instruction following in coding workflows should penalize silent failures and hallucinations, but should not arbitrarily reward models that decline tasks over models that attempt them with high partial success.

Concrete change recommended: Redefine 
𝑁
N as a direct fraction of total questions: 
𝑁
=
100
⋅
(
1
−
𝑖
𝑐
+
𝑝
+
𝑖
+
𝑎
)
N=100⋅(1−
c+p+i+a
i
	​

), so that hallucination/error rate is normalized against the total test set rather than the non-correct subset.

Ambiguity in 30-day soft expiry triggers for minor pricing tier revisions

The issue: The draft specifies that a plan limit-schema version diff or web page diff triggers a 30-day soft expiry and flags the route as "possibly superseded." Web pages for Claude, ChatGPT, and Grok frequently update unrelated marketing copy, enterprise disclaimers, or auxiliary feature text weekly.

Why it hurts the objective: Automated diff scrapers will perpetually mark valid saturation measurements as "possibly superseded," eroding user confidence in the freshness badges of stable plans.

Concrete change recommended: Restrict the change-detection diff trigger to scoped DOM selectors covering pricing tables, rate-limit documentation sections, and model availability matrices, rather than full-page diffs.

Low

Dirichlet perturbation skew on sparse within-group weights

The issue: The scenario engine draws hierarchical weights with within-group weights 
Dirichlet
⁡
(
50
×
proportions
)
Dirichlet(50×proportions). For the Long Context & Science group (total weight 10%), individual leaves (HLE, GPQA Diamond, SciCode, CritPt) each have nominal weights of 1.25% (group share 12.5%). A concentration parameter of 
50
×
0.125
=
6.25
50×0.125=6.25 yields a variance that can distort these minor leaves by over 40% across draws, exceeding the intended "modest perturbation."

Why it hurts the objective: Random scenario instability in minor benchmarks can inject artificial variance into S2 rank change outputs.

Concrete change recommended: Scale the Dirichlet precision parameter inversely to group weight: use 
𝛼
=
200
×
𝑤
⃗
nominal
α=200×
w
nominal
	​

 for within-group draws to maintain a uniform coefficient of variation across all leaves.

2. Methodology design recommendations

Formalize a Dual-Workload Capacity Profile for Plan Buyers (Workday Burst vs. Continuous Saturation)

Design: Augment the linear program for Plan capacity to compute two distinct metrics:

𝑀
cont
M
cont
	​

: 24/7 continuous saturation (the theoretical upper bound currently defined).

𝑀
burst
M
burst
	​

: Workday-feasible throughput, adding the constraint that tokens must be consumed within an 8-hour daily window over 5 working days per week (40 hours/week).

Implementation: Solvable with the existing time-indexed LP engine by simply setting the consumption indicator vector 
1
active
(
𝑡
)
=
0
1
active
	​

(t)=0 outside business hours. This requires no new provider data—only an explicit scenario parameter.

Automated Cross-Validation of Exact-Variant Harness Divergence

Design: For the SWE category where Bug Hunt runs on vendor CLIs while DeepSWE and Terminal-Bench run in controlled sandboxes, introduce an explicit "Harness Mismatch Penalty Bound" 
[
𝛿
𝐿
,
𝛿
𝑈
]
[δ
L
	​

,δ
U
	​

] in the S1 identification layer.

Implementation: Estimate 
[
𝛿
𝐿
,
𝛿
𝑈
]
[δ
L
	​

,δ
U
	​

] from the empirical score divergence observed when running the same model across different CLI/agent harnesses on Terminal-Bench 4.0. Pre-register this empirical interval in the registry to prevent vendor-tailored CLIs from gaining an unhedged advantage in certification.

Robust Common-Support Proration in Pairwise Value Margin

Design: In the normative pairwise certificate:

Δ
𝑖
𝑗
=
0.25
⋅
𝜅
⋅
ln
⁡
(
𝐶
𝑗
,
𝑊
𝑖
𝑗
𝐶
𝑖
,
𝑊
𝑖
𝑗
)
+
0.75
⋅
(
𝑄
𝑖
∣
𝑖
𝑗
−
𝑄
𝑗
∣
𝑖
𝑗
)
Δ
ij
	​

=0.25⋅κ⋅ln(
C
i,W
ij
	​

	​

C
j,W
ij
	​

	​

	​

)+0.75⋅(Q
i∣ij
	​

−Q
j∣ij
	​

)

use a fixed cohort elasticity constant 
𝜅
=
100
/
ln
⁡
(
𝑐
𝐻
/
𝑐
𝐿
)
κ=100/ln(c
H
	​

/c
L
	​

) derived once per release from the full cohort reference anchor points, and recompute 
𝐶
𝑖
,
𝑊
𝑖
𝑗
C
i,W
ij
	​

	​

 strictly over the subset of benchmarks present in both rows. This ensures that the dollar-to-quality exchange rate remains identical across all pairwise edges.

3. Questions for the owner

When a provider changes fair-use throttling thresholds without updating published documentation (a common practice among subscription LLM providers), do you intend to rely on user concordance reports to trigger a route soft-expiry, or must soft-expiry wait for a detected text diff on the provider's domain?

If pairwise common support drops DeepSWE (e.g., because a newly released frontier model only has Terminal-Bench and Bug Hunt at launch), is it your policy to hold that model in "provisional" status indefinitely until an exact-variant DeepSWE run is published, regardless of its score margin on remaining leaves?

4. Verdict

VERDICT HAS FEEDBACK