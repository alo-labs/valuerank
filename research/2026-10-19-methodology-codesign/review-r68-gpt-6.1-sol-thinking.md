0. Read check

Read all 13 parts, in order, through the GitHub connector at commit 82cd76900b7a65971ce4598047315843f854f536, including each part’s end.

Draft’s first line:

ValueRank methodology — draft r150

Last 12 whitespace-delimited words of each part:

> carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py).

> their own subset (the seven Index evaluations), flagged "subset cost" (O17, E254).

> on the Plan basis the workload question is the M_W identification status.

> for other Claude models; the transfers keep their assumption label and caution.

> (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

> value; no epsilon is introduced. Domain validity is separate from evidence completeness.

> Daily on a harness chosen per model) are disclosed as a limitation.

> predictive run-to-run variation, and only interpretations the public evidence supports are published.

> with a displayed quality, ordered by displayed quality ascending, then configuration ID.

> says these outputs compare ranked configurations only and names the listed configurations.

> or definite result; every cost check reads C_W, never the Index diagnostic.

> donor's stage, and a report partition takes its most advanced contributor's stage.

> normative); it is in draft-r150.md in the same folder of the repository.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. O94’s scenario treatment is not reconciled with the executable stream contract

Issue. O94/O98 require pricing-omission rows to compete in interval and scenario outputs over 
[
𝐶
,
𝑓
𝐶
]
[C,fC], or 
[
𝐶
,
∞
)
[C,∞) without a stated factor. However:

Part 8’s stream allowlist restricts S0 to reporting precision and describes S1’s additional inputs without an explicit pricing-omission treatment.

Part 10’s BlockerSafe explanation says scenario draws retain superseded-price rows at their published record.

The eligibility definition subsequently says O94 rows compete in scenario outputs over their cost range.

The draft provides neither an O94 sampling law nor a specific bounds-only scenario procedure connecting these statements.

The superseded-tariff and pricing-omission cases need not have the same treatment, but the specification must distinguish them explicitly.

Why it hurts the objective. A pricing-omission row can affect other rows’ rank, top-k and frontier frequencies even though it cannot receive a label. BlockerSafe protects the cheapest label; it does not resolve those other frequencies. Keeping the omitted cost fixed at 
𝐶
C and allowing it to range over the O94 domain can produce different outputs.

A structural interval alone does not specify a Monte Carlo input law. NIST’s uncertainty-propagation documentation likewise distinguishes specifying an input distribution from merely having a range; its Monte Carlo procedure requires a fully specified joint input distribution.
uncertainty.nist

Concrete change. Add an explicit pricing-omission uncertainty object and stream rule:

Published-record arithmetic may retain 
𝐶
C, clearly named as such.

O94-compliant outputs must propagate the structural cost domain.

Without public evidence supporting a distribution, publish scenario-share bounds or withhold the affected point frequency—not an invented uniform distribution, particularly on 
[
𝐶
,
∞
)
[C,∞).

Keep the existing label-denial and BlockerSafe requirements.

What is new relative to the ledger. This is not a challenge to O94, O98, or their blocker policy. It identifies the unresolved interface between those recently adopted rules and the earlier stream allowlist, fixed-record scenario convention, and frequency outputs.

M2. Relaxed range concordance can admit a pair whose midpoint pool is far outside the concordant evidence

Owner decision challenge — O81’s midpoint pooling in combination with O86.

Issue. O86 tests whether reports can be reconciled within the 20% margin, but O81 then pools their unconstrained arithmetic midpoints geometrically. Those are different operations.

Consider two otherwise eligible, independent, non-provisional reports in one comparable partition:

Report	Reported allowance range	Arithmetic midpoint
A	
[
100
,
110
]
[100,110]	105
B	
[
100
,
1000
]
[100,1000]	550

O86 passes because:

max
⁡
(
ℓ
𝑟
)
=
100
≤
1.20
min
⁡
(
𝑢
𝑟
)
=
132.
max(ℓ
r
	​

)=100≤1.20min(u
r
	​

)=132.

O81 nevertheless produces:

𝑀
pool
=
105
⋅
550
≈
240.3.
M
pool
	​

=
105⋅550
	​

≈240.3.

That pooled allowance is more than twice report A’s upper endpoint. Widening B’s uncertainty upward can increase the official multiple substantially without adding stronger evidence of a larger allowance.

Draft locators: Part 5, “Report admission is computed” and “Report eligibility profile”; Part 4, concordance and geometric pooling.

Why it hurts the objective. Once such a cell replaces a transfer or fallback, its inflated pooled multiple reduces displayed Plan cost and changes the ranking. The cell can be labelled concordant even though its selected midpoint values are not concordant. This is an estimator-design problem, not a request to loosen admission.

Concrete change. Preserve O74’s all-reports requirement and O86’s admission test, but constrain aggregation to values that satisfy the same concordance condition. Publish the feasible pooled range and adopt an explicit conservative displayed-value convention.

What is new relative to the ledger. This is not the rejected robust-core proposal: no report is discarded, no passing subset is selected, and provisional reports still constrain admission. The new argument is a counterexample showing that O86’s existence-based admission and O81’s unconstrained midpoint estimator do not compose safely.

Low
L1. AI Coding Daily’s sampling unit is specified inconsistently

Issue. Part 8’s “Added leaves — Sampling noise” paragraph says AI Coding Daily is read as a binomial share of 60 points. Later in the same part, the operative S1T definition uses six graded projects under E263, with 60 points retained only as the narrow-reading sensitivity.

Why it hurts the objective. These descriptions imply materially different noise bands. The draft itself reports the corresponding change in the AI Coding Daily ranking’s median separation threshold. Although the later governing definition resolves the precedence, an implementer reading the earlier leaf-specific paragraph could implement the wrong primary kernel.

Concrete change. Replace the earlier sentence with:

AI Coding Daily uses six graded projects as the primary S1T sampling unit under E263; the 60-point reading is a separately published sensitivity.

Generate both descriptions from one sampling-unit registry field.

What is new relative to the ledger. This does not challenge E263 or reopen the sampling-unit decision. It identifies a surviving inconsistent statement in r150.

2. Methodology design recommendations
Priority 1 — Give pricing omissions a bounds-only scenario interface

Implement M1 without changing the headline weights, published-cost ranking, or owner-mandated label policy.

For each affected configuration, register:

text
cost_uncertainty_kind: pricing_omission
published_cost: C
structural_cost_domain: [C, f*C] or [C, infinity)
constraint_basis: structural_bound
sampling_status: bounds_only
source_note_id: ...
dependency_id: ...

For an event 
𝐸
E, draw only the other inputs admitted by the stream’s existing law. Within scenario 
𝑠
s, evaluate:

𝑒
𝑠
−
=
inf
⁡
𝑐
∈
𝐶
𝑠
1
{
𝐸
(
𝑠
,
𝑐
)
}
,
𝑒
𝑠
+
=
sup
⁡
𝑐
∈
𝐶
𝑠
1
{
𝐸
(
𝑠
,
𝑐
)
}
,
e
s
−
	​

=
c∈C
s
	​

inf
	​

1{E(s,c)},e
s
+
	​

=
c∈C
s
	​

sup
	​

1{E(s,c)},

where 
𝐶
𝑠
C
s
	​

 preserves every relevant dependency and public constraint. Publish:

[
1
𝑁
∑
𝑠
𝑒
𝑠
−
,
1
𝑁
∑
𝑠
𝑒
𝑠
+
]
.
[
N
1
	​

s
∑
	​

e
s
−
	​

,
N
1
	​

s
∑
	​

e
s
+
	​

].

These are conservative scenario-share envelopes, not a probability distribution over omitted costs. They can be wider than an envelope obtained by treating one unknown cost as fixed across every replicate; state that distinction.

For unsupported decision classes, publish “pricing-omission scenario bounds unresolved.” Do not silently substitute the published-cost point frequency.

Add three release fixtures:

A finite omission range changes a competitor’s possible rank.

An unbounded omission requires no arbitrary distribution or finite truncation.

The published-cost point frequency remains separately reproducible but is never presented as the omission-aware result.

This follows the draft’s existing separation of structural bounds from sampling conventions; it supplies the missing executable interface rather than adding another uncertainty layer. Fully specifying the law for sampled inputs remains necessary for interpreting the resulting Monte Carlo frequencies.
uncertainty.nist

Priority 2 — Make range admission and aggregation use the same feasible evidence set

Subject to owner approval of M2, define the complete-partition feasible set:

𝐹
=
{
𝑥
:
ℓ
𝑟
≤
𝑥
𝑟
≤
𝑢
𝑟
 
∀
𝑟
,
max
⁡
𝑟
𝑥
𝑟
≤
1.20
min
⁡
𝑟
𝑥
𝑟
}
.
F={x:ℓ
r
	​

≤x
r
	​

≤u
r
	​

 ∀r,
r
max
	​

x
r
	​

≤1.20
r
min
	​

x
r
	​

}.

Every eligible report, including provisional reports where current policy requires them, constrains 
𝐹
F. The reports eligible to supply the pooled value remain the non-provisional reports 
𝐴
A.

Then publish:

𝑀
p
o
o
l
𝐿
=
min
⁡
𝑥
∈
𝐹
exp
⁡
 ⁣
(
1
∣
𝐴
∣
∑
𝑟
∈
𝐴
ln
⁡
𝑥
𝑟
)
,
M
pool
L
	​

=
x∈F
min
	​

exp(
∣A∣
1
	​

r∈A
∑
	​

lnx
r
	​

),
𝑀
p
o
o
l
𝑈
=
max
⁡
𝑥
∈
𝐹
exp
⁡
 ⁣
(
1
∣
𝐴
∣
∑
𝑟
∈
𝐴
ln
⁡
𝑥
𝑟
)
.
M
pool
U
	​

=
x∈F
max
	​

exp(
∣A∣
1
	​

r∈A
∑
	​

lnx
r
	​

).

A concrete conservative scoring convention is to use 
𝑀
p
o
o
l
𝐿
M
pool
L
	​

, with the complete range and the original midpoint result disclosed alongside it.

Implementation is small: in log coordinates, report bounds and the concordance constraints are linear, and the objective is linear. It requires only the report ranges and eligibility fields already collected.

Important limitations:

This interval describes aggregation of the reported allowance evidence. It does not identify 
𝑀
𝑊
M
W
	​

.

It does not establish full utilisation, fix workload mismatch, or upgrade evidence grade.

It retains every report; there is no robust-core selection.

Add the counterexample above as a regression fixture, plus a test that widening one report’s uncertainty cannot manufacture a stronger lower-bound allowance claim.

Priority 3 — Compile uncertainty descriptions from the kernel registry

Resolve L1 by making these fields authoritative for every leaf:

text
sampling_unit
primary_n
primary_n_source
alternative_n
alternative_role
kernel_status

Generate the leaf-specific explanation, S1T definition, separability annotation, and active-rules entry from that object. E265 already checks rendered figures; this extends that discipline to the semantic identity of the sampling unit.

No change to the chosen weights, benchmark set, or primary noise approximation is needed.

3. Questions for the owner

None. M2 explicitly identifies the owner decisions that would need amendment; the other recommendations implement or clarify existing policy.

4. Verdict

The remaining material feedback concerns two interfaces: propagating pricing-omission bounds into scenario outputs, and composing range-valued concordance with the selected pooling estimator. Neither requires changing the fixed cohort policy, transferring benchmark evidence between configurations, or obtaining non-public data.

VERDICT: HAS FEEDBACK