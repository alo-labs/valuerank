0. Read check

Read all seven parts through the GitHub connector at commit 04005dde2e32bdf68d349d8cc664223253504ec6, including each part’s end.

Draft’s first line:

ValueRank methodology — draft r48

Last 12 words of each part, in order:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> analysis, not imputation). A row without a cost gets no value score.

> scenario convention (with one published alternative), never evidence; formal bounds are distribution-free.

> candidate's cost upper bound); otherwise "not established", with the omitted competitors listed.

> or definite result; every cost check reads C_W, never the Index diagnostic.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

The review below concerns the complete draft, not the truncated full-ledger retrieval. I used the supplied decision ledger to distinguish settled decisions from the new arguments identified below.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. S1M needs to distinguish CI-range sensitivity from source-supported expected-performance uncertainty

Issue: E162 introduces S1M as “expected-performance uncertainty, one leaf,” but constructs its draws by assigning uniform or arcsine density entirely inside Terminal-Bench’s published 95% confidence interval. The draft correctly calls interval-only kernels conventional and avoids assuming normality. Nevertheless, a confidence interval does not supply a distribution over the parameter, nor does its confidence level establish that the parameter has no support outside its endpoints. Its coverage statement concerns repeated application of the interval-construction procedure.
itl.nist
+1

Terminal-Bench confirms that its whiskers represent a 95% confidence interval, and its submission schema exposes accuracy_ci95_half_width and n_trials. Those facts establish the existence of an interval, but do not by themselves establish the sampling unit, treatment of repeated trials on the same task, or an expected-performance sampling law suitable for ValueRank.
tbench
+1

Why it hurts the objective: A reader comparing configurations may interpret S1M as the empirical uncertainty counterpart to S1. In fact, its ordering frequencies are conditional on an additional convention: putting all simulated mass inside the reported CI. Changing between uniform and arcsine kernels explores density within that range, not uncertainty about the range’s construction or its excluded tails.

Concrete change:

Keep the public CI and the additional stream.

Name the default stream “S1 plus conventional Terminal-Bench CI-range sensitivity.”

Record source_interval_method, source_estimand, sampling_unit, repeated_task_treatment, and distribution_derivation_status.

Permit the stronger expected-performance interpretation only when the source’s interval method or public underlying observations justify the corresponding sampling construction.

Otherwise publish the uniform/arcsine results explicitly as endpoint-conditioned sensitivity, without inferring a tail model.

What is new: This addresses the new E162 stream’s inferential interpretation. It does not reopen O25, request confidence intervals in deterministic outputs, or repeat the already-adopted requirement to declare alternative kernels.

M2. Assumptions can change measured-only Plan rankings indirectly through the official anchor scale

Issue: E113 appropriately removes transfers from the measured-only route candidates, but retains the official Plan anchor object. E160 permits transferred and API-fallback observations to determine that object. Consequently, an assumed multiple can affect the measured-only ranking even after its route and configuration are absent from that view.

This is a scoring-scale effect, not merely a change of panel. In the unclipped region, for two measured configurations 
𝑖
,
𝑗
i,j,

𝑉
𝑖
−
𝑉
𝑗
=
25
ln
⁡
(
𝐶
𝑗
/
𝐶
𝑖
)
𝐷
+
0.75
(
𝑄
𝑖
−
𝑄
𝑗
)
,
𝐷
=
ln
⁡
(
𝑐
𝐻
/
𝑐
𝐿
)
.
V
i
	​

−V
j
	​

=25
D
ln(C
j
	​

/C
i
	​

)
	​

+0.75(Q
i
	​

−Q
j
	​

),D=ln(c
H
	​

/c
L
	​

).

If 
𝑖
i is cheaper but has lower quality, changing 
𝐷
D can reverse their order while their measured routes, costs, quality and competitor panel remain unchanged. An assumption-supported anchor extreme can therefore influence a supposedly measured-only comparison through the exchange rate.

Why it hurts the objective: The measured-only view usefully answers “what happens when only measured route evidence supplies the rows?” It does not independently answer “what ordering is supported without assumed Plan economics?” The existing common-panel comparison separates route-selection and composition effects, but leaves this calibration channel fixed and therefore invisible.

Concrete change: Keep the official anchors and existing measured-only view. Add one supplementary, common-panel calibration diagnostic:

Existing measured-only scores on official Plan anchors.

The same rows, routes, costs and quality scored on a separately frozen measured-evidence anchor object.

Pairwise reversals, rank shifts and both cost-doubling exchange rates.

Anchor-extreme provenance identifying measured, transfer-supported and fallback observations.

Where fewer than two eligible measured references exist, report “measured-evidence calibration unavailable.” Preserve the distinction between measured consumption and identified target-workload economics.

What is new: E160 settles which observations enter the official anchors. This recommendation does not replace that policy. The new argument is the specific indirect path from assumptions to ordering within the transfer-excluded view; the proposed diagnostic isolates that path.

Low

None.

2. Methodology design recommendations
Priority 1 — Give S1M an executable interpretation contract

Retain the current weights, deterministic interval target and stream separation. Add a small interpretation object to E162:

Field	Implementable rule
source_interval	Capture the published endpoints, confidence level and exact submission identity.
source_estimand	Record the documented target; otherwise not established from captured documentation.
source_interval_method	Pin the documented procedure or public implementation commit; otherwise unknown.
sampling_unit	Distinguish task, trial, task cluster and fitted parameter.
kernel_status	source-derived or conventional-within-CI.
tail_treatment	For the present conventional stream, outside-CI values not explored; do not invent tail mass.
permitted_label	Derive the label from these fields rather than allowing free-text “expected-performance uncertainty.”

For the conventional stream, define explicitly:

𝑍
𝑖
,
T
B
(
𝑠
)
∼
𝐾
 ⁣
(
[
𝐿
𝑖
,
𝑈
𝑖
]
∩
[
0
,
100
]
)
,
Z
i,TB
(s)
	​

∼K([L
i
	​

,U
i
	​

]∩[0,100]),

where 
𝐾
K is the registered uniform or arcsine convention and 
𝐿
𝑖
,
𝑈
𝑖
L
i
	​

,U
i
	​

 are the source interval transformed onto the leaf scale. State that the resulting frequencies describe this construction, not a source-estimated parameter distribution.

This preserves the useful information Terminal-Bench publishes without assigning its interval an unsupported probabilistic interpretation.
itl.nist
+1

Priority 2 — Add an anchor-provenance calibration diagnostic, not another primary ranking

Create a versioned object containing:

The existing measured-only common panel.

Its frozen route–measurement pairs and displayed costs.

The official Plan anchor ID.

A supplementary measured-evidence anchor ID, constructed using the same min/2 and max×2 rule.

Reference eligibility and provenance.

Both exchange rates and the resulting rank comparison.

Hold everything except calibration fixed:

Δ
𝑖
c
a
l
=
𝑉
𝑖
(
𝐴
m
e
a
s
u
r
e
d
)
−
𝑉
𝑖
(
𝐴
o
f
f
i
c
i
a
l
)
.
Δ
i
cal
	​

=V
i
	​

(A
measured
	​

)−V
i
	​

(A
official
	​

).

Report:

Maximum absolute score and rank changes.

Pairwise reversals.

Which official anchor extremes are supported by assumptions or fallback costs.

Whether each measured reference is target-workload identified or unmatched.

Do not interpret this supplementary calibration as validation of unidentified 
𝑀
𝑊
M
W
	​

. Its purpose is narrower: expose how much of the ordering comes from measured observations versus the exchange rate induced by the broader official table.

Neither recommendation changes the fixed cohort, transfers evidence between variants, imputes missing evidence, uses provider quota marketing as a numerator, or requires a new private measurement programme.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK