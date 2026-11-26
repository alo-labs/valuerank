1. Findings by severity
Critical

A target-mix Plan cost can be unidentified while its interval certificate remains artificially precise. Issue: The normative capacity definition correctly says that, without an established additive budget, an observed-mix multiple does not identify target-mix capacity. But the certification set varies “evidenced multiple ranges” without explicitly requiring a bound on the difference between the measured workload and AA’s workload. Consequently, a narrow measurement interval around an observed-mix multiple can produce a narrow Plan cost interval even when the quantity being ranked is expressly unidentified. The L1 mix flag does not resolve this.
paste.txt
 Why it hurts the objective: A certificate could establish numerical dominance for the wrong workload rather than establish lower full-utilisation cost for the declared workload. Concrete change: Distinguish 
𝑀
𝑜
𝑏
𝑠
𝑒
𝑟
𝑣
𝑒
𝑑
M
observed
 from 
𝑀
𝐴
𝐴
-
𝑚
𝑖
𝑥
M
AA-mix
. Certification must use the latter. Permit certification only when public evidence establishes either direct workload compatibility, an identified capacity model, or an evidenced transfer bound. Otherwise retain the row and observed-mix score, but mark target-mix cost unidentified and prohibit its certification. This does not require removing mix-unmatched rows from the official table. What is new: Earlier decisions preserved mix-unmatched rows and introduced the capacity-identification distinction. The remaining problem is that this distinction has not been connected explicitly to the certification gate.

High

The treatment of unevaluable competitors leaves the scope of a Plan certificate ambiguous. Issue: A transfer-dependent route is unevaluable with transfers off, while certification requires beating “every competitor.” The draft does not say whether such competitors invalidate a cohort-wide certificate or disappear from its comparison domain. API-fallback exclusions are explicit; this separate competitor issue is not.
paste.txt
 Why it hurts the objective: Dropping an unevaluable competitor can turn “best among routes we can evaluate without transfers” into an apparent recommendation across the full official Plan ranking. Concrete change: Publish the certificate comparison set and its exclusions. Distinguish:

Certified among identified, directly evidenced routes.

Certified across all eligible native Plan routes in the cohort.

The second label requires valid comparisons against every eligible competitor, including assumption-dependent competitors through conservative bounds. Where those bounds are unavailable, the broader result is not identified. What is new: E2 resolves the candidate’s own transfer-dependent route. This finding concerns what happens when that route belongs to a competitor.

The matched-cost blocker has no executable Plan-basis definition. Issue: The normative blocker uses 
𝐶
𝑖
𝑚
𝑎
𝑡
𝑐
ℎ
/
𝐶
𝑖
𝑡
𝑜
𝑡
𝑎
𝑙
C
i
match
	​

/C
i
total
	​

, but neither expression includes a Plan multiple. Elsewhere, certification and matched-cost divergence are described “per basis.”
paste.txt
 Why it hurts the objective: An API-only check cannot by itself establish that the Plan cost transformation behaves reasonably. Conversely, dividing both matched and total cost by the same scalar multiple leaves their ratio unchanged, making that component of a Plan check algebraically redundant. Concrete change: Define separate purposes:

API check: the existing reweighted API-cost diagnostic.

Plan check: a workload-compatibility test of the effective-cost transformation, using evidenced workload-specific capacity where available.

If no Plan-matched capacity is identified, report “API cost-shape check passed; Plan workload check unidentified.” Do not imply that the former validates the latter. What is new: Earlier reviews established the matched-cost blocker; they did not resolve its transformation across the two buyer bases.

The 40% matched-panel requirement creates a strong, currently undisclosed certification bottleneck. Issue: The draft reports only 43.75% total priced quality weight, against a 40% common-panel minimum. On the stated leaf inventory, Terminal-Bench, GDPval, and AutomationBench each contribute 10 priced percentage points. Losing any one leaves at most 33.75%, making certification impossible regardless of the remaining evidence. The statement that 17 of 19 rows have matched DeepSWE or Terminal-Bench evidence does not establish feasibility of this substantially broader panel.
paste.txt
 Why it hurts the objective: The practical certification gate becomes exact-configuration cost availability on three particular benchmarks, not simply broad matched-cost coverage. That may be defensible, but readers and implementers need to know that it is the effective policy. Concrete change: Publish a certification-feasibility matrix before implementing the recommendation layer: row × priced leaf, exact-variant compatibility, stack compatibility, available cost, and resulting common-panel weight. Define how the common model panel is selected without outcome-dependent discretion. What is new: This is the arithmetic consequence of E3 interacting with the stated priced inventory—not a repetition of the recommendation to introduce E3.

Medium

Certification endpoints need a more explicit evidence-status contract. Issue: The registry distinguishes rounding ranges, published confidence intervals, observed ranges, identification bounds, and analyst stress ranges. Nevertheless, certification treats them as one admissible set without a rule specifying which endpoints are mandatory and how unmeasured repeatability enters. The Bug Hunt normative definition expressly separates published evidence uncertainty from a repeatability stress allowance.
paste.txt
 Why it hurts the objective: Two implementers can produce different certificates from the same registry simply by including or excluding the stress allowance. “Under the declared evidence bounds” is appropriately limited wording, but the declaration must be executable. Concrete change: Add a per-input certificate_role field: included constraint, specification-only stress, or unidentified quantity. Require every uncertain scored input to have an explicit role and rationale. Missing repeatability evidence must not silently become zero uncertainty. What is new: The distinction between evidence uncertainty and stress allowances is adopted; their exact membership in the certificate remains unspecified.

Fee-period capacity needs reset-phase handling, not only aggregate window totals. Issue: The multi-pool formula is valid if each 
𝐵
𝑤
B
w
	​

 is an attainable spendable capacity over the fee period. The draft does not explicitly require this attainability check when billing periods and quota windows have different boundaries. Anthropic documents weekly resets at an account-specific fixed time, independent of when a subscription starts.
paste.txt
claude
 Why it hurts the objective: Counting reset allowances that intersect a fee period can overstate usable capacity if short partial windows cannot actually be consumed under the other simultaneous limits. Concrete change: Record billing boundaries, reset phase, carryover, and any evidenced throughput restriction. When necessary, calculate capacity with a small time-indexed linear program. Use observed consumption or a conservative bound when public evidence cannot establish scheduling feasibility. What is new: Earlier changes addressed simultaneous pools and minimum binding limits; this concerns attainability when their reset schedules intersect a fee period.

Low

Superseded prose still conflicts with the normative specification. Issue: The earlier Bug Hunt formula treats repository differences as a measurement interval and widens single-run rows using cohort repeat spread; the normative definition explicitly rejects those interpretations. The uncertainty overview also mandates a shared serving-snapshot coupling, while the normative dependence rule allows joint resampling only with paired public observations.
paste.txt
 Why it hurts the objective: A public methodology should not require readers to infer which contradictory paragraph wins. Concrete change: Replace the superseded passages rather than retaining both. State that executable definitions govern, and add specification tests that reject inconsistent field interpretations. What is new: The substantive corrections were adopted; this is a document-to-implementation consistency defect.

2. Methodology design recommendations
Priority 1 — Make identification status part of every recommendation

For each row and basis, release:

Displayed score and its estimand.

Target-workload cost identification status.

Certification eligibility and failed gates.

Certificate comparison set.

Unevaluable competitors and the reason each comparison is unavailable.

For candidate 
𝑖
i, calculate the pairwise margin only where the required quantities are identified:

𝑚
𝑖
𝑗
=
inf
⁡
𝜃
∈
Θ
c
e
r
t
[
𝑉
𝑖
(
𝜃
)
−
𝑉
𝑗
(
𝜃
)
]
.
m
ij
	​

=
θ∈Θ
cert
	​

inf
	​

[V
i
	​

(θ)−V
j
	​

(θ)].

A broad certificate requires every relevant 
𝑚
𝑖
𝑗
>
0
m
ij
	​

>0. An undefined comparison is not a positive margin. A restricted certificate can still be useful, but its comparison domain belongs in the label.

Keep the adopted 25/75 weights and frozen anchors; none of these corrections requires changing them.
paste.txt

Priority 2 — Split Plan measurement from Plan transport

Use distinct registry objects:

𝑀
𝑖
𝑜
𝑏
𝑠
𝑒
𝑟
𝑣
𝑒
𝑑
=
eligible API-valued measured consumption
gross cash paid
,
M
i
observed
	​

=
gross cash paid
eligible API-valued measured consumption
	​

,
𝑀
𝑖
𝐴
𝐴
-
𝑚
𝑖
𝑥
∈
[
𝐿
𝑖
,
𝑈
𝑖
]
,
𝑐
𝑖
𝑃
𝑙
𝑎
𝑛
=
𝑐
𝑖
𝐴
𝑃
𝐼
𝑀
𝑖
𝐴
𝐴
-
𝑚
𝑖
𝑥
.
M
i
AA-mix
	​

∈[L
i
	​

,U
i
	​

],c
i
Plan
	​

=
M
i
AA-mix
	​

c
i
API
	​

	​

.

Record the identification mechanism for the second quantity:

Direct compatible-workload measurement.

Publicly evidenced additive capacity model.

Evidenced transport bound.

Unidentified.

Do not use cohort spread or an arbitrary percentage band to turn category 4 into category 3. Preserve owner-authorised transfers in the official ranking, as required, while keeping their assumption status separate from empirical identification.
paste.txt

Priority 3 — Publish a common-panel feasibility report

Before each release, generate the row-by-leaf matrix described above. Fix the panel-selection rule before examining resulting ranks.

Terminal-Bench publicly exposes model, agent, resolution rate, cost, and token columns, making it a useful source for this audit. Those columns still need exact-configuration and accounting checks; leaderboard presence alone does not establish compatibility.
tbench

Publish:

Maximum feasible priced weight per row.

The selected shared panel and its weight.

Rows outside that panel.

Whether any comparison is certifiable under the current 40% requirement.

If no useful panel exists, publish that outcome rather than silently relaxing exact-variant evidence or the editor’s threshold.

Priority 4 — Add temporal capacity only where it is needed

For time slices 
𝑡
t, let 
ℓ
𝑡
ℓ
t
	​

 denote AA-suite-equivalent work delivered. Maximise

𝜆
=
∑
𝑡
ℓ
𝑡
λ=
t
∑
	​

ℓ
t
	​


subject to each evidenced quota-window constraint:

∑
𝑡
∈
𝑊
𝑎
𝑤
𝑡
ℓ
𝑡
≤
𝐵
𝑤
𝑊
.
t∈W
∑
	​

a
wt
	​

ℓ
t
	​

≤B
wW
	​

.

The coefficients represent evidenced resource consumption, including any documented temporal variation. Derive

𝑀
𝐴
𝐴
-
𝑚
𝑖
𝑥
=
𝜆
𝐶
𝐴
𝑃
𝐼
𝐹
g
r
o
s
s
.
M
AA-mix
=
F
gross
	​

λC
API
	​

	​

.

Use this only when public measurements identify the coefficients and capacities. Provider documentation may establish reset structure, but must not supply the consumption numerator—preserving the fixed evidence policy. Claude’s documented five-hour and weekly limits illustrate why the time dimension can matter.
claude
+1

Priority 5 — Make certificate construction auditable

For every uncertain input, publish:

Interval endpoints and their meaning.

Whether the interval enters certification.

Scenario sampling law, separately.

Dependency identifier.

Evidence supporting any joint constraint.

Release pairwise certificate margins alongside the winning label. Add tests showing that widening an admissible uncertainty set cannot create a previously absent certificate, and that removing competitor evidence cannot silently strengthen an unrestricted recommendation.

3. Questions for the owner

When a transfer-dependent Plan competitor is unevaluable with transfers off, should it block a cohort-wide certificate, or should certification explicitly cover only directly evidenced routes?

Is the intended Plan matched-cost blocker merely the API cost-shape check applied to Plan rows, or must it also validate the subscription workload transformation?

Is the effective requirement for exact-compatible priced Terminal-Bench, GDPval, and AutomationBench evidence intentional, given the current 43.75% priced inventory and 40% threshold?
paste.txt

4. Verdict

The draft has a strong separation between scenario support and certification. The remaining material issues concern whether the certified quantities are actually identified, which competitors the claim covers, and whether the public evidence can satisfy the declared gates. These can be addressed without changing the fixed cohort, exact-variant policy, owner-selected headline weights, or Value Multiple evidence rules.

VERDICT: HAS FEEDBACK