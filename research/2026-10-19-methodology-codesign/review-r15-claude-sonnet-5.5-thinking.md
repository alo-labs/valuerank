1. Findings by severity
Critical

None.

High

The matched-workload certification check does not specify a valid Plan-basis cost. Issue: The governing check defines 
Δ
𝑖
𝑗
,
a
l
t
Δ
ij,alt
	​

 using 
𝐶
𝑖
,
a
l
t
C
i,alt
	​

, but it does not say whether a Plan comparison uses API charges or Plan-effective costs. The surrounding text calls this an API cost-shape check, while also requiring its positive value margin for certification. These interpretations produce different recommendations. Identification of 
𝑀
𝑊
M
W
	​

 for the primary basket does not establish 
𝑀
a
l
t
M
alt
	​

 for a differently weighted workload.
paste.txt
 Why it hurts the objective: A Plan route can have strong economics on the primary workload and weak economics on the alternative workload—or vice versa. Applying 
𝑀
𝑊
M
W
	​

 to both silently assumes workload transport; using API costs instead tests a different buyer’s economics. Concrete change: Define the check explicitly by basis:

API: use API charges on both workloads.

Plan: retain the API alternative-workload check as a separately named diagnostic, or calculate the alternative Plan margin using an independently identified 
𝑀
a
l
t
M
alt
	​

.

If O18 requires a Plan-basis alternative-workload margin, an unidentified 
𝑀
a
l
t
M
alt
	​

 must make that check unevaluable—not become 
𝑀
𝑊
M
W
	​

 by default.

What is new: E5/E17 separate API cost shape from Plan identification, and O18 introduces a value-margin blocker. Their combination still leaves the cost estimand of the Plan alternative-workload margin unspecified.

The alternative-workload weighting convention can make the certification blocker depend on arbitrary benchmark packaging. Issue: The draft permits frozen task quantities and a “weighting convention,” while its matched-cost diagnostic averages per-task costs using quality weights. It does not fully define how those quantities construct 
𝑊
a
l
t
W
alt
	​

. If one benchmark is split into two leaves, or a task is subdivided into several smaller tasks, quality-weighted dollars per task can change without any change in the underlying work. Separate anchors do not remove model-specific changes caused by that repackaging.
paste.txt
 Why it hurts the objective: A supposedly practical workload check can reject or certify a recommendation because of benchmark task granularity rather than a meaningful change in workload economics. Concrete change: Publish one executable construction of 
𝑊
a
l
t
W
alt
	​

, including:

The execution unit for every component.

Exact task multiplicities.

Whether weighting allocates task counts, whole benchmark passes, or another explicitly named unit.

A split/merge invariance test for bookkeeping-only changes.

A feasible default is quality-weighted complete benchmark passes, implemented through per-task multiplicities, rather than an unexplained average of heterogeneous task prices. What is new: E9 and the accounting tree prevent aggregate/component double counting. This finding concerns invariance to task granularity and leaf packaging, not double counting.

Comparison-set construction can change the meaning of “recommended,” but the draft does not prohibit outcome-dependent set selection. Issue: The draft requires disclosure of comparison sets and exclusions, but does not fully prescribe when and how the directly evidenced recommendation set 
𝐽
J is selected. It also permits selected priced-leaf/model panels, subject to preregistration before examining ranks. That leaves room for a candidate-specific or evidence-convenient recommendation scope.
paste.txt
 Why it hurts the objective: An outgoing-edge certificate is rigorous only for its declared set. A narrow set can yield “recommended” even when a commercially relevant, directly evidenced rival is excluded because of a failed comparison gate. Disclosure alone does not establish that two releases—or two candidates—face the same recommendation contest. Concrete change:

Determine route eligibility and 
𝐽
J using a published algorithm before calculating margins.

Use the same 
𝐽
J for every candidate seeking the same headline label.

Keep a route that passes set-level eligibility but fails a pair-level gate inside 
𝐽
J; that comparison is unevaluable and prevents a certificate.

Publish a second, explicitly restricted-panel certificate when needed, without giving it the unrestricted headline wording.

What is new: E7 and E11–E16 define edge validity and certificate scope. This adds a rule governing selection of the contest itself.

Medium

S0 scenario shares are not reproducible from the specified interval-to-draw rules. Issue: The draft specifies uniform draws for rounding ranges, clustered resampling for raw runs, and triangular draws for observed-run ranges. It does not supply a governing draw rule for a published confidence interval when the underlying observations or likelihood are unavailable. A triangular distribution additionally requires a mode. These gaps matter because S0 frequencies determine the “scenario-supported” label.
paste.txt
 Public source formats make this consequential: Terminal-Bench publishes 95% confidence intervals, while AA describes GDPval-AA ratings fitted from pairwise comparisons with sandwich-estimator confidence intervals. Those intervals have different statistical constructions; neither supplies a complete scenario distribution by itself.
tbench
+1
 Why it hurts the objective: Two implementations can consume the same public evidence and produce different leadership frequencies while both appearing compliant. Concrete change: Require a complete, versioned draw-kernel object for every sampled input: distribution, parameters, truncation, mode where relevant, and derivation. When only interval endpoints exist, label the resulting distribution an interval-conditioned scenario convention and publish a second kernel sensitivity. An unspecified kernel makes the affected scenario output unavailable, not implicitly deterministic. What is new: The ledger adopts interval provenance and dependence handling, but does not resolve the mapping from published confidence intervals to executable draws.

Basket admission and subset scoring have conflicting operational rules. Issue: The phasing rule says a component enters only when exact-configuration cost is captured for every ranked row. O17 and E10 then provide official subset scoring for rows missing basket components. The draft does not distinguish an initial component-admission requirement from missingness caused by later cohort additions, evidence withdrawal, or refresh failures.
paste.txt
 Why it hurts the objective: A new configuration could either delay useful basket expansion indefinitely or force a component’s removal for everyone. Alternatively, implementers could admit incomplete components immediately under O17. Those policies produce different workload versions and headline scores. Concrete change: Specify the state transitions:

Admission completeness is tested against a frozen, named reference panel.

Once admitted, membership stays frozen for that workload version.

Later missingness invokes O17/E10 without shrinking the full workload.

Adding a new cohort member does not retroactively invalidate component admission.

What is new: This resolves the interaction between the adopted phasing and subset policies; it does not challenge either policy.

Low

The clip gate still has two incompatible executable thresholds. Issue: E20 calls its threshold the single governing gate, but the Cost section subsequently says, “fail if ≥ 2 rows clip on either basis.” These differ for sufficiently large cohorts. The normative-precedence statement does not cleanly resolve two rules appearing in the same Cost section.
paste.txt
 Why it hurts the objective: Different implementations can hold different releases using identical data. Concrete change: Delete the legacy two-row threshold and implement the E20 rule once, with integer-boundary fixtures for several cohort sizes. What is new: E20 already adopted the intended rule; the remaining finding is a contradictory implementation instruction still present in r14.

2. Methodology design recommendations
Priority 1 — Make the certification object fully typed

Extend each pairwise certificate record with:

text
buyer_basis
primary_workload_hash
alternative_workload_hash
comparison_set_id
cost_estimand_primary
cost_estimand_alternative
multiple_primary_id
multiple_alternative_id
alternative_check_role

For API comparisons:

𝐶
𝑖
,
𝑊
A
P
I
=
∑
𝑒
𝑛
𝑒
𝑐
𝑖
𝑒
.
C
i,W
API
	​

=
e
∑
	​

n
e
	​

c
ie
	​

.

For Plan comparisons:

𝐶
𝑖
,
𝑊
P
l
a
n
=
𝐶
𝑖
,
𝑊
A
P
I
𝑀
𝑖
,
𝑊
,
𝐶
𝑖
,
𝑊
a
l
t
P
l
a
n
=
𝐶
𝑖
,
𝑊
a
l
t
A
P
I
𝑀
𝑖
,
𝑊
a
l
t
.
C
i,W
Plan
	​

=
M
i,W
	​

C
i,W
API
	​

	​

,C
i,W
alt
	​

Plan
	​

=
M
i,W
alt
	​

	​

C
i,W
alt
	​

API
	​

	​

.

Never populate the second multiple from the first merely because the model and subscription tier match. This implements the draft’s existing workload-hash transport discipline consistently across both certification margins.
paste.txt

The owner must choose whether the alternative check is an API diagnostic or a Plan-basis certification requirement; the implementation should not make that choice implicitly.

Priority 2 — Give the alternative workload an execution-unit contract

A concrete, routinely refreshable construction is:

𝑛
𝑏
a
l
t
=
𝐾
 
𝑤
𝑏
′
 
𝑁
𝑏
,
𝐶
𝑖
,
a
l
t
=
∑
𝑏
∈
𝐵
𝑛
𝑏
a
l
t
𝑐
𝑖
𝑏
,
n
b
alt
	​

=Kw
b
′
	​

N
b
	​

,C
i,alt
	​

=
b∈B
∑
	​

n
b
alt
	​

c
ib
	​

,

where:

𝑁
𝑏
N
b
	​

 is the published number of tasks in a complete benchmark pass.

𝑤
𝑏
′
w
b
′
	​

 is the selected panel’s normalized quality weight.

𝐾
K is a fixed scale constant.

Fractional multiplicities represent a workload mixture, not a literal execution schedule.

This represents quality-weighted complete benchmark passes. It does not claim that one terminal task equals one repository task.

Add two fixtures:

Splitting one execution component into accounting subcomponents leaves total cost unchanged.

Splitting a quality leaf while preserving its total weight and underlying execution workload leaves 
𝐶
𝑖
,
a
l
t
C
i,alt
	​

, anchors, and certification margins unchanged.

This complements—not replaces—the adopted aggregate/component exclusivity and repetition-invariance tests.
paste.txt

Priority 3 — Freeze the recommendation contest independently of its outcome

Publish three separate objects:

Route eligibility set: routes satisfying the evidence-admission rules.

Headline comparison set: generated from eligibility and declared scope, before margins are evaluated.

Evaluation graph: all pairwise outcomes within that set, including unevaluable edges.

A useful governing rule is:

Pairwise evaluation failure cannot remove a competitor from an already frozen headline comparison set.

Restricted-panel results may still be useful, but should use wording such as “certified within the named evaluation panel.” This preserves the adopted outgoing-edge logic while preventing scope selection from doing the work of certification.
paste.txt

Priority 4 — Specify scenario kernels as data, not prose

For each input, require:

text
interval_interpretation
kernel_family
kernel_parameters
support
parameter_derivation
dependency_id
alternative_kernel_id

Recommended hierarchy:

Public paired observations: the specified clustered resampling.

Rounding interval: uniform, as already adopted.

Published estimate with documented standard error and applicable approximation: a declared approximate distribution using those parameters.

Interval endpoints only: an explicitly conventional kernel, paired with an alternative such as endpoint-heavy sampling.

No defensible sampling convention: bounds-only output; no scenario leadership claim dependent on that input.

Do not infer a normal distribution merely from the phrase “95% interval.” AA’s documented fitted-rating intervals and Terminal-Bench’s displayed intervals should retain their respective source interpretations.
tbench
+1

Keep the existing separation between scenario frequencies and confidence guarantees.
paste.txt

Priority 5 — Add a small set of governing integration tests

Beyond the existing unit tests, add:

Plan alternative-workload isolation: changing 
𝑀
𝑊
M
W
	​

 cannot change an alternative-workload Plan cost unless a recorded capacity model links the two workloads.

Contest stability: a pair-level gate failure does not remove the rival from the frozen recommendation set.

Kernel completeness: every stochastic input has executable parameters; an unspecified kernel fails the scenario build.

Basket persistence: a newly admitted cohort row with missing costs does not silently change the full workload hash.

Single clip predicate: all release-gate consumers call the same function.

These target interactions among adopted decisions rather than reopening the fixed cohort, exact-variant evidence, weighting, or Value Multiple policies.
paste.txt

3. Questions for the owner

For Plan certification, should O18’s alternative-workload margin use Plan-effective costs, or is it intentionally an API-economics check? If it uses Plan costs, must 
𝑀
a
l
t
M
alt
	​

 be independently identified?

Should the alternative workload represent quality-weighted complete benchmark passes, quality-weighted individual tasks, or another fixed execution mixture? These are different workloads, not interchangeable normalizations.

May a route that passes direct-evidence admission be excluded from the headline comparison set solely because its pairwise common-support or matched-cost check is unevaluable? The answer determines whether the proposed contest-stability rule matches the intended recommendation scope.

4. Verdict

The draft is close to an implementable evidence system, but the Plan alternative-workload estimand, recommendation-set construction, and scenario kernels still permit materially different outputs from the same public inputs. These are integration gaps between adopted rules, not reasons to reopen the fixed owner policies. The most important next step is consistency across the executable objects and release tests.
paste.txt

VERDICT: HAS FEEDBACK