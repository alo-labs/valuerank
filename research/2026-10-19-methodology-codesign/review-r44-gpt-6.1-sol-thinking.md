1. Findings by severity
Critical

None.

High

E77 confuses the confidence level with the error allocation, leaving the executable stopping rule materially ambiguous. Issue: E77 calls for a Clopper–Pearson interval “at level α/16 with α = 0.05.” The intended Bonferroni construction requires an error allocation of 
0.05
/
16
0.05/16, hence a confidence level of 
1
−
0.05
/
16
=
0.996875
1−0.05/16=0.996875. These are opposite arguments in common implementations: SciPy accepts confidence_level, whereas statsmodels accepts alpha.
paste.txt
scipy
+1
 Why it hurts the objective: Passing 
0.05
/
16
0.05/16 as the confidence level would produce a dramatically narrower interval than intended and could prematurely authorise a scenario-supported-cheapest label. The draft presents E77 as executable specification, so this should not depend on an implementer inferring the intended convention. Concrete change: Replace “at level α/16” with:

At each look, compute a two-sided Clopper–Pearson interval with per-look error allocation 
𝛿
=
0.05
/
16
δ=0.05/16, confidence level 
1
−
𝛿
=
0.996875
1−δ=0.996875, and equal tail allocations 
𝛿
/
2
δ/2.

Publish the API argument convention and regression-test the interval endpoints. What is new relative to the ledger: This does not challenge E77/E127’s adopted repeated-look correction. It identifies a parameterisation ambiguity in its operative wording.

Medium

Pooled Plan measurement objects lack an explicit evidence-clock aggregation rule. Issue: E107 freezes report sets; E111 makes a concordant partition a measurement object; E144 carefully prevents a transfer from restarting its donor’s clock. However, the draft does not specify how a pooled partition’s observation date, expiry stage and change-detection status derive from its constituent reports. “The measurement window’s end” does not uniquely resolve a partition containing multiple measurement windows.
paste.txt
 Why it hurts the objective: An implementation could use the latest report date for the entire partition. That would allow a fresh report to renew older consumption observations still contributing to the geometric mean. Alternatively, an implementation could discard the entire partition when its earliest report expires. Those choices can produce different eligible routes, multiples and ranks. Concrete change: Apply freshness and scoped-change classification to each contributing report before finalising the official partition. Only individually surviving reports may contribute to its official pooled multiple. Recheck source count, independence and concordance after that filtering. Publish the resulting contributor IDs and a conservative partition freshness summary. Do not remove an otherwise eligible discordant report merely to recover a passing subset; the existing complete-partition rule must continue to apply. What is new relative to the ledger: E142 resolves expiry before route reselection, and E144 resolves donor-clock inheritance. Neither explicitly resolves freshness inheritance within a multi-report measurement object.

E149 leaves the Plan cost-removal calculation insufficiently explicit about the API-cost numerator and the effective Plan cost. Issue: The standing removal formula defines

𝐶
𝑖
(
−
𝑇
𝐵
)
=
𝐶
𝑖
,
𝑊
−
𝐶
𝑖
,
𝑇
𝐵
C
i
(−TB)
	​

=C
i,W
	​

−C
i,TB
	​


and then scores it on the original anchors. Elsewhere, 
𝐶
𝑖
,
𝑊
C
i,W
	​

 is the API basket sum, while the Plan cost input is that sum divided by the selected multiple. E149’s subsequent instruction to retain the displayed multiple suggests the intended Plan calculation, but does not actually write it.
paste.txt
 Why it hurts the objective: A literal implementation could subtract an API-dollar component from an already divided Plan-dollar cost, or score the undivided API numerator against Plan anchors. Both would invalidate the standing cross-basis sensitivity column. Concrete change: Define separate symbols and equations:

𝐴
𝑖
=
API basket cost
,
𝑚
𝑖
=
selected displayed multiple
,
𝑃
𝑖
=
𝐴
𝑖
/
𝑚
𝑖
.
A
i
	​

=API basket cost,m
i
	​

=selected displayed multiple,P
i
	​

=A
i
	​

/m
i
	​

.

Then, for the fixed-multiple arithmetic stress,

𝐴
𝑖
(
−
𝑇
𝐵
)
=
𝐴
𝑖
−
𝐴
𝑖
,
𝑇
𝐵
,
𝑃
𝑖
(
−
𝑇
𝐵
)
=
𝐴
𝑖
−
𝐴
𝑖
,
𝑇
𝐵
𝑚
𝑖
.
A
i
(−TB)
	​

=A
i
	​

−A
i,TB
	​

,P
i
(−TB)
	​

=
m
i
	​

A
i
	​

−A
i,TB
	​

	​

.

Score 
𝐴
𝑖
(
−
𝑇
𝐵
)
A
i
(−TB)
	​

 against API anchors and 
𝑃
𝑖
(
−
𝑇
𝐵
)
P
i
(−TB)
	​

 against Plan anchors. Explicitly state how API-fallback rows participate, if at all. What is new relative to the ledger: This does not repeat the adopted request to add cost removal or distinguish original from recalibrated anchors. It closes a basis-specific arithmetic ambiguity in E149.

Low

The normalised weighted-spread and drift statistics omit a zero-total-spread outcome. Issue: E114 defines

𝐷
𝑔
=
∑
𝑏
∈
𝑔
∩
𝐵
∗
𝑤
𝑏
 
𝑆
𝐷
(
𝑧
𝑏
)
∑
𝑏
∈
𝐵
∗
𝑤
𝑏
 
𝑆
𝐷
(
𝑧
𝑏
)
.
D
g
	​

=
∑
b∈B
∗
	​

w
b
	​

SD(z
b
	​

)
∑
b∈g∩B
∗
	​

w
b
	​

SD(z
b
	​

)
	​

.

The draft handles insufficient panels, but not an empty 
𝐵
∗
B
∗
 or a zero denominator. The separately reported normalised weighted-spread statistic has the same boundary case. This is possible if every observed leaf is marked non-discriminating.
paste.txt
 Why it hurts the objective: Different implementations could emit NaN, zero shares or misleading drift flags despite there being no eligible dispersion to allocate. Concrete change: Return undefined — no eligible quality dispersion, issue no group drift flags, and publish the excluded leaves. Add fixtures for an empty eligible-leaf set and a constant-score panel.

2. Methodology design recommendations

Make the E77 confidence construction fully executable. Retain the existing 16 looks, per-event guarantee and threshold logic. Define

𝛿
=
0.05
16
.
δ=
16
0.05
	​

.

For 
𝑘
k successful scenarios out of 
𝑛
n, use

𝐿
=
{
0
,
	
𝑘
=
0
,


Beta
⁡
−
1
(
𝛿
/
2
;
𝑘
,
𝑛
−
𝑘
+
1
)
,
	
𝑘
>
0
,
L={
0,
Beta
−1
(δ/2;k,n−k+1),
	​

k=0,
k>0,
	​

𝑈
=
{
1
,
	
𝑘
=
𝑛
,


Beta
⁡
−
1
(
1
−
𝛿
/
2
;
𝑘
+
1
,
𝑛
−
𝑘
)
,
	
𝑘
<
𝑛
.
U={
1,
Beta
−1
(1−δ/2;k+1,n−k),
	​

k=n,
k<n.
	​


This is the equal-tailed Clopper–Pearson construction with confidence 
1
−
𝛿
1−δ.
metricgate
 Record per_look_error, confidence_level, tail_allocation, 
𝑘
k, 
𝑛
n, 
𝐿
L and 
𝑈
U in the certificate. In SciPy, the corresponding argument is confidence_level=1-0.05/16, not 0.05/16.
scipy

Give pooled Plan evidence a constituent-level freshness pipeline. Use the following deterministic order:

Discover and freeze the report set under E107.

Establish comparability partitions under E102.

Classify each report’s expiry and scoped-change status at the release cutoff.

Form each official partition from all surviving eligible reports.

Recheck independent-source count and complete-partition concordance.

Compute the geometric mean only if the partition passes.

Construct the route–measurement candidate and run the existing selector.

Preserve excluded reports and their reasons in the release data. A report leaving through expiry is an eligibility transition, not permission to cherry-pick among still-eligible reports. This extends the existing frozen-evidence and expiry-before-selection contracts without changing the numerator evidence policy.
paste.txt
 Recommended fields:

contributing_report_ids

report_observation_end

report_expiry_stage

report_change_detection_status

next_contributor_eligibility_boundary

partition_recomputed_at

These require only the report dates and provenance already contemplated by the draft.

Add a basis-typed cost-removal fixture. For a synthetic configuration with API basket cost 100, Index-run Terminal-Bench cost 20 and selected displayed multiple 4:

Primary effective Plan cost: 
100
/
4
=
25
100/4=25.

Correct fixed-multiple removal cost: 
(
100
−
20
)
/
4
=
20
(100−20)/4=20.

Explicitly reject 
25
−
20
=
5
25−20=5.

Explicitly reject scoring 80 against Plan-dollar anchors.

Apply the same basis typing to both original-anchor and recalibrated-anchor calculations. Keep E149’s existing warning that this is arithmetic stress, not identified economics for the altered workload.
paste.txt

Complete the diagnostic numerical-domain contract. Add one governing helper for normalised dispersion shares:

Share
⁡
𝑔
=
{
𝑑
𝑔
/
∑
ℎ
𝑑
ℎ
,
	
∑
ℎ
𝑑
ℎ
>
0
,


undefined
,
	
otherwise
.
Share
g
	​

={
d
g
	​

/∑
h
	​

d
h
	​

,
undefined,
	​

∑
h
	​

d
h
	​

>0,
otherwise.
	​


Distinguish insufficient panel, no eligible leaves and zero eligible dispersion in the data release. None should trigger a substantive group-drift flag.

No changes to the cohort policy, exact-variant rule, weights or Value Multiple numerator evidence rules are needed to implement these recommendations.

3. Questions for the owner

None.

4. Verdict

The remaining material findings concern implementation rather than a redesign of the ranking: disambiguate the confidence parameter, make pooled-evidence clocks explicit, and type the Plan sensitivity arithmetic. The other identified boundary case is a small diagnostic completeness fix.

VERDICT: HAS FEEDBACK