1. Findings by severity
Critical

None.

High

Cost-completeness certification conflates task support with attempt-level aggregation. Issue: E47 treats 
𝑇
=
𝑛
𝜇
T=nμ as a certificate that all 
𝑛
n tasks have cost evidence. But AA’s current methodology describes efficiency metrics as pooled per-task-attempt averages, excluding missing telemetry; performance instead averages attempts within tasks before averaging tasks. Those are different aggregation operators when observed attempt counts vary by task. The public methodology does not establish the draft’s premise that 
𝜇
μ is an average over cost-observed tasks.
paste.txt
artificialanalysis
 Why it hurts the objective: This can misclassify cost completeness and can make the priced workload differ across configurations. For illustration, suppose two tasks have observed mean costs of USD 10 and USD 100, with one and three observed attempts respectively. Their equal-task deployment-pass cost is USD 110, whereas twice their pooled attempt mean is USD 155. Both tasks have telemetry: unequal repetition coverage, not missing task support, causes the difference. Concrete change: Require an aggregation contract for both pinned fields: their observation unit, denominator, repetition treatment, and task weighting. Permit 
𝑇
=
𝑛
𝜇
T=nμ certification only when public evidence establishes the necessary task-level aggregation—or balanced attempt coverage plus a documented conversion. Otherwise mark completeness unresolved. Preserve E53: incomplete repetition coverage alone must not disqualify a component. What is new: This does not repeat the rejected attempt-level eligibility gate. It identifies an aggregation problem in the certificate used to establish task-level completeness.

Absence of a declined-task marker is insufficient evidence of complete cost telemetry. Issue: E47 separately allows chart components to be “confirmed complete” merely because AA’s declined-task marker is absent. Yet refusal status, execution coverage, and cost-telemetry coverage are different properties. AA explicitly states that missing efficiency telemetry is excluded from averages; its refusal methodology separately distinguishes blocked attempts and fallbacks. Absence of a refusal marker therefore does not, by itself, establish telemetry completeness.
paste.txt
artificialanalysis
 Why it hurts the objective: Frontier and cheapest-above-bar outputs require FullCost. A negative check for one exclusion reason cannot certify that every required task contributes cost, particularly when chart totals are rounded and cannot independently establish support. Concrete change: Treat the marker as one-way evidence: its presence triggers investigation or an incompleteness status under the documented source semantics; its absence provides no completeness certificate. Require an explicit coverage count, task-level support, or a public source contract guaranteeing complete support for that aggregate. Otherwise use “completeness unresolved,” while retaining the displayed score under the existing policy. What is new: E37 already requires completeness. This finding concerns the unsupported chart-specific exception that bypasses that requirement.

Medium

Rank-change diagnostics do not explicitly hold the comparison panel constant. Issue: E13 requires numerical ranks only within evaluable branches, but does not explicitly require baseline and branch ranks to use the same competitors. E64’s “maximum rank change” can therefore mix a score effect with competitors disappearing from a branch.
paste.txt
 Why it hurts the objective: A model can apparently improve several places without its relative ordering against any retained competitor changing. Readers could interpret this as robustness to benchmark removal or workload changes when it is merely a panel-composition effect. Concrete change: Compute every baseline-versus-branch rank difference on their common evaluable panel. Publish panel size and excluded rows beside it. If release-wide ranks are also shown, label their change separately as including composition effects. What is new: This tightens the comparison underlying E13/E64; it does not repeat their already-adopted requirement to avoid ranking unevaluable rows.

E62 does not specify a uniquely reproducible independent-source comparison. Issue: “A ranking computed from the independently executed leaves only” could mean independent-only quality or a new value score retaining the original cost input. These answer different questions. If it means quality alone, comparing it with displayed value confounds benchmark-source disagreement with the intentionally included cost term.
paste.txt
 Why it hurts the objective: A low correlation could incorrectly look like evidence against AA dependence when the disagreement actually comes from cost. Conversely, retaining AA-derived cost in both rankings can generate agreement that is not independent validation of the complete ranking. Concrete change: Define two named checks on the same exact-configuration panel:

Quality agreement: full observed-quality ranking versus independent-only quality ranking.

Quality-substitution value agreement: original value ranking versus value recomputed with independent-only quality, keeping cost, anchors, basis and route fixed.

Explicitly state that the second check substitutes quality evidence only; it does not independently validate costs or Plan multiples. What is new: This specifies the estimands of the newly adopted E62 rather than asking again for an independent-source check.

Low

“Bounded” and “identified” Plan statuses lack an explicit relationship. Issue: E61 presents “identified / bounded / unidentified” as statuses, while the capacity definition permits a structurally established interval 
[
𝐿
,
𝑈
]
[L,U] to enter Θ and says Plan interval outputs require an “identified” 
𝑀
𝑊
M
W
	​

. It is unclear whether “bounded” means eligible partial identification or an ineligible status.
paste.txt
 Why it hurts the objective: Different implementations could produce different Plan evaluable sets and different “fewer than half identified” headline labels from identical evidence. Concrete change: Separate identification status from representation: point-identified, set-identified, unidentified; then record finite interval, one-sided bound, or full domain separately. Specify eligibility and identification-yield counting explicitly.

2. Methodology design recommendations
Priority 1 — Make the cost aggregation contract executable

For task 
𝑡
t, let 
𝐴
𝑖
𝑡
o
b
s
A
it
obs
	​

 be its cost-observed evaluation repetitions. The equal-task, deployment-equivalent record cost is:

𝑃
𝑖
=
∑
𝑡
∈
𝑇
1
∣
𝐴
𝑖
𝑡
o
b
s
∣
∑
𝑟
∈
𝐴
𝑖
𝑡
o
b
s
𝑐
𝑖
𝑡
𝑟
.
P
i
	​

=
t∈T
∑
	​

∣A
it
obs
	​

∣
1
	​

r∈A
it
obs
	​

∑
	​

c
itr
	​

.

This expression requires at least one observed cost per required task. It does not require complete repetition coverage, and it does not estimate or fill missing repetitions.

By contrast, a pooled attempt mean is:

𝜇
𝑖
p
o
o
l
=
∑
𝑡
∑
𝑟
∈
𝐴
𝑖
𝑡
o
b
s
𝑐
𝑖
𝑡
𝑟
∑
𝑡
∣
𝐴
𝑖
𝑡
o
b
s
∣
.
μ
i
pool
	​

=
∑
t
	​

∣A
it
obs
	​

∣
∑
t
	​

∑
r∈A
it
obs
	​

	​

c
itr
	​

	​

.

Multiplying this by the task count reproduces 
𝑃
𝑖
P
i
	​

 under balanced observed repetition counts, but not generally. AA’s public description makes this distinction material.
artificialanalysis

Add these fields to the registry:

aggregation_unit: task / attempt.

aggregation_operator: sum / pooled mean / mean of task means.

observed_task_count and observed_attempt_count.

repetition_conversion_rule.

support_certificate_type and its public evidence.

Keep the existing pinned total for displayed scoring unless its documented semantics require a versioned correction. Do not reconstruct a replacement from insufficient public data. Where the aggregation contract cannot be verified, publish the total but leave the relevant eligibility status unresolved.

Add regression fixtures for balanced repetitions, unequal repetitions with full task support, and a genuinely missing task. This operationalises E47/E53 without imposing the rejected attempt-completeness gate.

Priority 2 — Require positive support evidence for FullCost

Implement completeness as:

CompleteCostEvidence
⁡
(
𝑖
,
𝑒
)
=
SupportEstablished
⁡
(
𝑖
,
𝑒
)
∧
AggregationCompatible
⁡
(
𝑖
,
𝑒
)
.
CompleteCostEvidence(i,e)=SupportEstablished(i,e)∧AggregationCompatible(i,e).

Accept public task-level records, explicit matching counts, or a documented aggregate contract establishing both predicates. Marker absence alone satisfies neither.

This is routinely refreshable: it changes the interpretation of available evidence, not the requirement to obtain private telemetry. Unavailable evidence remains unresolved, as the existing missing-evidence policy intends.

Priority 3 — Standardise paired-panel sensitivity reporting

For baseline 
0
0 and branch 
𝑏
b, define:

𝐼
𝑏
=
𝐸
0
∩
𝐸
𝑏
,
Δ
𝑟
𝑖
𝑏
=
𝑟
𝑖
(
𝑏
;
𝐼
𝑏
)
−
𝑟
𝑖
(
0
;
𝐼
𝑏
)
.
I
b
	​

=E
0
	​

∩E
b
	​

,Δr
ib
	​

=r
i
(b;I
b
	​

)
	​

−r
i
(0;I
b
	​

)
	​

.

Both ranks use exactly 
𝐼
𝑏
I
b
	​

. Report:

Δ
𝑟
𝑖
𝑏
Δr
ib
	​

, with ties handled by one declared convention.

Baseline and branch scores.

Retained quality weight and workload hash.

Common-panel size and excluded competitors.

For a maximum across branches, identify the responsible branch and its panel. If panels differ substantially, also publish a fixed-panel summary over their intersection, when that intersection is informative. No weights or owner-required headline rankings need change.

Priority 4 — Split E62 into two explicit diagnostic estimands

On rows with both independent leaves, define:

𝑄
𝑖
i
n
d
=
0.10
𝑧
𝑖
,
B
u
g
H
u
n
t
+
0.10
𝑧
𝑖
,
T
B
0.20
,
Q
i
ind
	​

=
0.20
0.10z
i,BugHunt
	​

+0.10z
i,TB
	​

	​

,

and:

𝑉
𝑖
i
n
d
Q
=
0.25
𝑆
𝐶
(
𝑐
𝑖
)
+
0.75
𝑄
𝑖
i
n
d
.
V
i
indQ
	​

=0.25S
C
	​

(c
i
	​

)+0.75Q
i
ind
	​

.

Publish separately:

𝜏
𝑏
 ⁣
(
rank
⁡
𝑄
ˉ
,
rank
⁡
𝑄
i
n
d
)
,
τ
b
	​

(rank
Q
ˉ
	​

,rankQ
ind
),
𝜏
𝑏
 ⁣
(
rank
⁡
𝑉
,
rank
⁡
𝑉
i
n
d
Q
)
.
τ
b
	​

(rankV,rankV
indQ
).

Use the same matched rows for each pair. Retain the adopted model-row bootstrap, labelled as matched-panel sensitivity rather than benchmark measurement uncertainty. Define an explicit “undefined” result for panels with insufficient rank variation.

These checks supplement—not replace—the adopted leave-AA-out evaluability rule.

Priority 5 — Normalise the Plan identification taxonomy

Use:

Status	Meaning	Plan interval eligibility
Point-identified	Compatible evidence establishes a single published-record 
𝑀
𝑊
M
W
	​

	Eligible, subject to other gates
Set-identified	Compatible evidence establishes a strictly positive, finite interval 
[
𝐿
,
𝑈
]
[L,U]	Eligible, carrying the interval through Θ
Unidentified	No qualifying target-workload constraint is established	Ineligible

Handle one-sided or zero-inclusive bounds explicitly rather than silently assigning finite log-cost scores.

For E61, count point-identified and eligible set-identified rows as target-workload identified, but print their counts separately. Retain the existing exploratory headline rule; simply make its denominator and numerator executable.

3. Questions for the owner

Do the archived sums.costUsd and mean.costUsd objects document task-normalised aggregation, or are they derived from pooled attempt-level telemetry? This determines whether the remedy is a documentation correction, a completeness-status correction, or a versioned cost correction.

Is E62 intended primarily to test dependence of quality estimates on AA, or agreement of the complete purchasing ranking with independent evidence? The former supports the proposed quality-only check; the latter requires retaining the quality-substitution value check while explicitly disclosing shared cost evidence.

4. Verdict

The material remaining issues concern evidence certification and diagnostic comparability, not the fixed cohort, exact-variant policy, owner-selected weights, or permission to retain flagged scores. The first two findings should be resolved before relying on FullCost-based interval labels.

VERDICT: HAS FEEDBACK