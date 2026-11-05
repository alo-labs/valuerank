0. Read check

First line:

ValueRank methodology — draft r55

Last 12 words by part:

Part 1: cost per task, not AA's 7:2:1 blended price, not total Index cost.

Part 2: unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

Part 3: a bias bound in the identification layer); repetitions are not a bias.

Part 4: No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

Part 5: candidate's cost upper bound); otherwise "not established", with the omitted competitors listed.

Part 6: or definite result; every cost check reads C_W, never the Index diagnostic.

Part 7: covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

All seven parts were read to their end.

1. Findings by severity
Critical

None

High

Issue: Undefined degrees of freedom for cohort and leaf dispersion statistics across gates. In Part 1 and Part 3, the within-cohort influence flag uses 
0.25
⋅
SD
(
𝑆
𝐶
)
0.25⋅SD(S
C
	​

) versus 
0.75
⋅
SD
(
𝑆
𝑄
)
0.75⋅SD(S
Q
	​

), and leaf discrimination uses a 3-point threshold on cohort 
SD
(
𝑧
)
SD(z), without specifying whether 
SD
SD is the sample estimator with 
𝑁
−
1
N−1 degrees of freedom or population estimator with 
𝑁
N.
Why it hurts the objective: The cohort is small (19 configurations total, and subset-workload panels can have 2 or 3 rows). On small panels, sample and population standard deviations differ by 5% to 41%, which can arbitrarily flip the 3-point non-discriminating boundary or the 10%/90% influence flags.
Recommended change: Normatively standardize all cohort standard deviation and variance calculations to the unbiased sample estimator (
𝑁
−
1
N−1 degrees of freedom), with an explicit rule returning "undefined (insufficient panel)" whenever a panel has fewer than 2 rows.

Issue: Undefined score-swing gate behavior for cohort admission and retirement. In Part 7, the release gate holds the release if any score swing exceeds 5 points without being attributed by the replay bridge under E177. However, the gate does not define the attribution predicate for a newly admitted configuration (whose prior score 
𝑉
𝑡
−
1
V
t−1
	​

 does not exist) or a demoted configuration.
Why it hurts the objective: An unhandled null score comparison can either fail closed and improperly block routine releases that introduce new frontier models, or silently pass unvalidated score jumps in existing models.
Recommended change: Formally specify that the score-swing attribution gate applies strictly to the intersection cohort ranked in both release 
𝑡
−
1
t−1 and release 
𝑡
t. Explicitly classify new entrants as "cohort admission (prior score undefined; replay check bypassed)" and departing rows as "cohort exit".

Medium

Issue: Clashing classification of the leave-AA-out sensitivity. Part 4 refers to leave-AA-out as a "headline robustness column," while Part 4 and Part 7 simultaneously mandate under E146 that any deletion branch with under 40% retained quality weight is "not identifiable under the coverage rule" and suppressed from ranking (today independent leaves retain only 20%).
Why it hurts the objective: This creates a direct contradiction between the narrative description of the headline table and the normative ranking engine.
Recommended change: Harmonize Part 4 with E146 and E62 by clarifying that leave-AA-out is a registered deletion branch that is non-evaluable for headline rank columns under v1 evidence weights, and that independent-source robustness is officially supplied by the matched-panel diagnostics in E62.

Issue: Missing executable specification for GDPval-AA logistic win-probability sensitivity. Part 3 registers a specification-layer sensitivity using "logistic win-probability vs the pinned anchor model" for GDPval-AA, but omits the logistic scale denominator and the explicit formula.
Why it hurts the objective: Without specifying whether the logistic conversion uses standard base-10 Elo with a 400 divisor or base-
𝑒
e, independent implementations cannot reproduce the specification-stress branch.
Recommended change: Specify the formula explicitly: 
𝑧
logit
,
𝑖
=
100
/
(
1
+
10
(
𝐸
𝑟
−
𝐸
𝑖
)
/
400
)
z
logit,i
	​

=100/(1+10
(E
r
	​

−E
i
	​

)/400
), where 
𝐸
𝑟
E
r
	​

 is the rating of the pinned bar reference model.

Issue: Unhandled boundary condition in the unanswered-or-partial share formula for Omniscience. Part 3 gives the formula 
(
1
−
𝐴
)
(
1
−
ℎ
)
(1−A)(1−h) where 
ℎ
=
incorrect
/
(
all questions
−
correct
)
h=incorrect/(all questions−correct). If a future configuration achieves 100% accuracy (
𝐴
=
1
A=1), the denominator of 
ℎ
h is zero, rendering 
ℎ
h undefined.
Why it hurts the objective: Direct evaluation in automated pipelines triggers a division-by-zero runtime error on perfect runs.
Recommended change: Formally define unanswered-or-partial share directly from counts as 
(
𝑝
+
𝑎
)
/
𝑇
(p+a)/T when counts are available, or add the guard condition: 
0
0 when 
𝐴
=
1
A=1.

Low

Issue: Unspecified leave-selected-out state for singleton Plan routes in E179. Part 2 defines the leave-selected-out summary as the route selected when the primary route is removed, but does not define the output for a model with exactly one admissible route.
Why it hurts the objective: An implementation without an explicit rule for empty candidate sets could crash or display undefined values.
Recommended change: Specify that when a configuration has only one admissible route, the leave-selected-out field reports "none (singleton route; API fallback)" and displays the API-fallback value score.

Issue: Asymmetric confidence interval handling in the S1M stream. Part 4 notes that S1M draws uniformly or via arcsine inside source-documented intervals. For asymmetric intervals (e.g., binomial intervals near boundaries), a uniform draw shifts the expected value away from the published point estimate.
Why it hurts the objective: This introduces an unintentional mean shift in conventional sensitivity draws.
Recommended change: Specify that when a source interval is asymmetric around the reported point estimate, the kernel should use a piecewise-uniform distribution split at the mode to preserve the point estimate as the median.

2. Methodology design recommendations

Standardize numerical dispersion operators:
Formally define 
Var
(
𝑥
)
=
1
𝑛
−
1
∑
𝑖
=
1
𝑛
(
𝑥
𝑖
−
𝑥
ˉ
)
2
Var(x)=
n−1
1
	​

∑
i=1
n
	​

(x
i
	​

−
x
ˉ
)
2
 and 
SD
(
𝑥
)
=
Var
(
𝑥
)
SD(x)=
Var(x)
	​

 across all cohort metrics, including within-cohort influence, drift flags, and the 3-point discrimination threshold. Require 
𝑛
≥
2
n≥2 for evaluation; return "undefined (insufficient panel)" otherwise.

Formalize release gate cohort domain transitions:
In the E177 replay contract, define the evaluation set for score swings strictly as 
𝐶
𝑡
−
1
∩
𝐶
𝑡
C
t−1
	​

∩C
t
	​

. For elements in 
𝐶
𝑡
∖
𝐶
𝑡
−
1
C
t
	​

∖C
t−1
	​

, assign status NEW_ROW_ATTRIBUTED_TO_ADMISSION. For elements in 
𝐶
𝑡
−
1
∖
𝐶
𝑡
C
t−1
	​

∖C
t
	​

, assign status RETIRED_ROW.

Reconcile headline robustness terminology:
Update Section 4 to state: "leave-one-source-out (leave-AA-out is a registered deletion branch, currently reported as not identifiable under E146 due to 20% independent weight; independent robustness is provided by the E62 matched-panel diagnostics)."

Complete the GDPval-AA logistic transform definition:
Add the closed-form equation to the specification layer:

𝑧
logit
,
𝑖
=
100
1
+
10
(
𝐸
𝑟
−
𝐸
𝑖
)
/
400
z
logit,i
	​

=
1+10
(E
r
	​

−E
i
	​

)/400
100
	​


where 
𝐸
𝑖
E
i
	​

 is configuration 
𝑖
i's Elo rating and 
𝐸
𝑟
E
r
	​

 is the rating of the pinned bar reference configuration.

Guard the Omniscience unanswered share calculation:
Replace the algebraic expression with a piecewise definition:

share
unanswered
=
{
0
,
	
if 
𝐴
=
1


(
1
−
𝐴
)
(
1
−
ℎ
)
,
	
if 
𝐴
<
1
 and counts absent


𝑝
+
𝑎
𝑇
,
	
if counts published
share
unanswered
	​

=
⎩
⎨
⎧
	​

0,
(1−A)(1−h),
T
p+a
	​

,
	​

if A=1
if A<1 and counts absent
if counts published
	​

3. Questions for the owner

For the GDPval-AA specification-layer sensitivity, should the logistic win probability be evaluated against the pinned bar reference model 
𝑟
r, or against the fixed Elo anchor model (e.g., the model corresponding to Elo 1500)?

4. Verdict

VERDICT: HAS FEEDBACK