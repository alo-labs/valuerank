1. Findings by severity
Critical

None.

High
H1. The Plan report rules do not uniquely determine which measurement supplies a route’s multiple

Issue: E107 correctly freezes discovery and requires concordance across every comparable report in a partition. But E102 can produce multiple comparability partitions for the same route—for example, measurements on different workloads that cannot be reconciled. The draft requires publishing “which reports determine the displayed measurement” without specifying a deterministic rule for choosing that partition. E85 selects between routes, not between competing measurement objects within one route. Likewise, the controlled-measurement override explicitly replaces owner-named transfers, but does not fully resolve competition between a controlled measurement and an independently eligible report partition for the same route.
paste.txt

Why it hurts the objective: Two implementations can admit the same evidence, satisfy the complete-partition concordance rule, and still select different Plan multiples and ranks. This leaves a selection opportunity upstream of the reproducible route comparator. E107 prevents choosing a favourable report subset within a partition; it does not prevent choosing a favourable partition.

Concrete change: Add a measurement-selection stage before E85. Either:

Give distinct measurement objects explicit candidate identities and extend the comparator to select among route–measurement pairs; or

Define a deterministic within-route selector, including identification status, evidence grade, applicability dates, compatible-workload status and a stable final tie-break.

Never use the magnitude of a multiple to choose among incomparable measurement objects without explicitly authorising and labelling that rule. Publish the alternatives and the resulting rank sensitivity.

H2. The scenario-supported cheapest label can be authorised by one arbitrary missing-data convention despite failing under its mandatory alternative

Issue: E25 requires an alternative kernel for endpoint-only intervals, and wholly missing quality leaves explicitly receive conventional—not evidential—sampling laws. E100 nevertheless authorises “scenario-supported cheapest” from the primary-kernel S1 branch alone. The draft does not require that the label survive the already-required alternative kernel.
paste.txt

Why it hurts the objective: The issue is not the full-composite-versus-observed-only error already addressed by E100. The new problem is that the full-composite label can still be determined by an arbitrary distribution assigned to missing evidence.

Consider a non-provisional candidate with 70% observed quality weight, all observed scores equal to 100, and one missing 10%-weight leaf in each of three groups. Let a more expensive, fully observed reference score 75. If the missing leaves are sampled independently and uniformly, the candidate qualifies when 
𝑈
1
+
𝑈
2
+
𝑈
3
≥
50
U
1
	​

+U
2
	​

+U
3
	​

≥50, which occurs in 
47
/
48
47/48, approximately 97.9%, of scenarios. Under independent endpoint-heavy alternatives placing equal mass at 0 and 100, qualification occurs in only 
7
/
8
=
87.5
%
7/8=87.5%. If it is strictly cheaper whenever qualified, the candidate receives the label under the primary kernel but fails it under the alternative—with identical public evidence.

Concrete change: Require the authorising threshold to pass under every pre-registered kernel alternative affecting the event, with Monte Carlo threshold resolution for each. Otherwise publish “primary-kernel frequency ≥90%; kernel-sensitive” without the unqualified scenario-supported label. Formal interval labels should remain unchanged.

Medium
M1. “Measured-only” does not yet have an executable estimand or route-selection contract

Issue: The draft promises a measured-only Plan view but does not define whether it:

Filters the officially selected routes to remove transfers;

Removes transfers first and reruns the route comparator;

Includes eligible exact-route measurements whose target-workload transport is unidentified; or

Includes single-source or expired measurements currently restricted to diagnostics.

These alternatives can produce different rows and selected routes. E106 defines official display and interval admission, but not membership in this particular view.
paste.txt

Why it hurts the objective: The measured-only view is the main way readers distinguish observed subscription evidence from owner-authorised transfers. Without a predicate and selection order, its name can suggest stronger workload identification than it actually provides, and independent implementations need not reproduce it.

Concrete change: Define a named view object with:

An explicit evidence-admission predicate;

A rule for whether selection is rerun after filtering;

Its workload and valuation-basis requirements;

Its fallback policy;

Its anchor policy and comparison panel.

A practical definition is: remove transfer-dependent and diagnostic-only candidates, rerun the same selector among remaining officially eligible measurement candidates, retain workload-unmatched flags, and use the official anchor object for directly comparable score differences.

M2. A signed covariance allocation is defined, but the older “effective weight” drift flag remains ambiguous

Issue: The quality section replaces “effective weights” with two distinct diagnostics: normalised weighted spread and signed covariance allocation. The next sentence still flags a group whose “effective weight” differs from nominal by more than ±50%, without naming which diagnostic governs, how leaf values aggregate to groups, or which common panel supplies the calculation.
paste.txt

Why it hurts the objective: These diagnostics answer different questions and can disagree materially, especially with correlated leaves. A release can therefore fire or suppress the same public warning depending on an implementer’s interpretation.

Concrete change: Name one governing drift statistic and provide its equation. Keep the covariance allocation separately labelled, including its potential negative values. Specify the panel, group aggregation, treatment of non-discriminating leaves and undefined cases.

Low

None.

2. Methodology design recommendations
Priority 1 — Make measurement selection a first-class, versioned object

Extend the existing evidence and route objects with:

𝑚
=
(
route ID
,
partition ID
,
report IDs
,
measurement workload
,
valuation basis
,
measurement dates
,
identification object
)
.
m=(route ID,partition ID,report IDs,measurement workload,valuation basis,measurement dates,identification object).

Build eligible measurement candidates from the complete frozen partitions. Apply a documented selector before route selection, or select directly over route–measurement pairs.

For candidates at equal identification class and evidence grade, prefer the latest completed eligible measurement period, then use a stable ID. This avoids implicitly treating a larger, incomparable observed multiple as better evidence. Where a controlled measurement overrides lower-grade evidence, state that explicitly.

Publish fixtures for:

Two passing but incomparable workload partitions for one route;

A controlled measurement plus a passing end-user partition;

An older target-identified measurement versus a newer unmatched measurement;

Conflicting partitions with and without public evidence of a schema change.

This completes the selection chain without changing E107’s no-subset-search rule or weakening the owner’s numerator evidence restrictions.
paste.txt

Priority 2 — Separate scenario frequency from kernel-robust scenario labelling

For candidate 
𝑖
i, reference 
𝑟
r, and the pre-registered set of admissible conventional kernel specifications 
𝐾
K, define:

𝑓
𝑖
𝑟
min
⁡
=
min
⁡
𝑘
∈
𝐾
𝑓
𝑖
𝑟
,
𝑘
qualifying and strictly cheapest
.
f
ir
min
	​

=
k∈K
min
	​

f
ir,k
qualifying and strictly cheapest
	​

.

Issue the scenario-supported label only if every required kernel’s sequential lower confidence bound is at least 0.90. Report the frequency range across those kernels, rather than presenting the minimum as a probability.

To keep this routinely implementable:

Evaluate the already-required primary and alternative kernels first.

Freeze the kernel set before examining labels.

State whether the robustness check covers complete named specifications or a larger combination set.

If some required specification is unevaluable, withhold the kernel-robust label rather than silently dropping that specification.

This uses the existing engine and E77 threshold machinery. It does not introduce imputation, alter formal published-record bounds, or require new private data.
paste.txt

Priority 3 — Turn the measured-only view into a reproducible sensitivity object

Publish a hashed view specification:

𝐷
m
e
a
s
u
r
e
d
=
(
admission predicate
,
selection rule
,
anchor policy
,
panel policy
,
fallback policy
)
.
D
measured
	​

=(admission predicate,selection rule,anchor policy,panel policy,fallback policy).

Use “measured, target-workload identified” and “measured, target-workload unmatched” as distinct statuses within the view. “Measured” should describe the provenance of the consumption observation, not imply that 
𝑀
𝑊
M
W
	​

 is identified.

Compare official and measured-only ranks on their common panel, following E65, and attribute differences to route selection separately from panel composition. The draft already has the evidence metadata needed to implement this.
paste.txt

Priority 4 — Finish the executable definition of the quality drift flag

If normalised weighted spread is intended to govern, define, on one declared common complete panel 
𝐼
I:

𝑑
𝑏
=
𝑤
𝑏
 
SD
⁡
𝑖
∈
𝐼
(
𝑧
𝑖
𝑏
)
,
𝐷
𝑔
=
∑
𝑏
∈
𝑔
𝑑
𝑏
∑
𝑏
𝑑
𝑏
.
d
b
	​

=w
b
	​

SD
i∈I
	​

(z
ib
	​

),D
g
	​

=
∑
b
	​

d
b
	​

∑
b∈g
	​

d
b
	​

	​

.

Then flag a group when:

𝐷
𝑔
<
0.5
𝑊
𝑔
or
𝐷
𝑔
>
1.5
𝑊
𝑔
,
D
g
	​

<0.5W
g
	​

orD
g
	​

>1.5W
g
	​

,

where 
𝑊
𝑔
W
g
	​

 is its nominal quality share.

For the existing exclusion of non-discriminating leaves from drift-flag counting, specify an eligible leaf set 
𝐵
∗
B
∗
, and renormalise both observed spread shares and nominal comparison shares over that same set. Otherwise the flag compares quantities with different denominators.

Keep

𝐴
𝑔
=
Cov
⁡
 ⁣
(
∑
𝑏
∈
𝑔
𝑤
𝑏
𝑧
𝑏
,
𝑄
)
Var
⁡
(
𝑄
)
A
g
	​

=
Var(Q)
Cov(∑
b∈g
	​

w
b
	​

z
b
	​

,Q)
	​


as the separately named signed covariance allocation. If the complete panel is insufficient, return “not estimable”; do not combine row-specific renormalised coefficients. This completes E81 rather than proposing another influence diagnostic.
paste.txt

3. Questions for the owner

When one Plan route has several eligible but incomparable measurement partitions, should selection prioritise target-workload identification, measurement recency, or the highest observed multiple? This determines the missing within-route selection rule.

Should “scenario-supported cheapest” mean support under the primary declared convention only, or support robust to the mandatory alternative conventions? If primary-only is intentional, I recommend making that limitation part of the label itself.

Should the measured-only view rerun route selection after removing transfers, and should it retain officially eligible measurements whose 
𝑀
𝑊
M
W
	​

 remains unidentified?

4. Verdict

The draft’s remaining material weaknesses concern selection and interpretation rather than the already-settled cohort, cost-record or interval-certification policies. The most important fixes are to close the within-route measurement-selection gap and prevent a unique-cheapest label from depending silently on one arbitrary missing-evidence kernel.
paste.txt

VERDICT: HAS FEEDBACK