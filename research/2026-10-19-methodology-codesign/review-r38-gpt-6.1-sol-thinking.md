1. Findings by severity
Critical

None.

High

E132 does not unambiguously define the kernel assignments that authorise a scenario-supported label.

Issue: E132 first defines blocks by primitive dependencies, but subsequently describes eight assignments when candidate, reference and competitor role blocks are distinct. Those are different partitions. With independent missing leaves across several competitors, dependency-based blocking can produce substantially more than three blocks. Conversely, putting all competitor primitives into one role block forces their kernel choices to move together even when they are independent. The current wording does not determine which assignment set an implementation must enumerate.
paste.txt

Why it hurts the objective: Two conforming implementations could authorise different cheapest-above-bar labels. This is particularly material because E132 is intended to close the remaining kernel-sensitivity loophole, not merely provide another descriptive diagnostic.

Concrete change: Specify two distinct objects: primitive dependency components and the coarser kernel-switch groups used for the registered checks. Publish their mapping and the exact assignment list. If switching is role-grouped, say explicitly that independently varying competitor kernels are not exhaustively checked. If switching is dependency-component-exhaustive, remove the general eight-assignment illustration and publish the actual 
𝐵
B, assignment count and computational budget.

What is new: This is not another request to add kernel robustness; E112/E121 already adopted that. It concerns an ambiguity introduced by E132’s dependency-based revision.

The fallback for cost uncertainty can place unsupported analyst variation into the measurement stratum.

Issue: The uncertainty section says token-use variance is drawn using public clustered resampling “otherwise a declared parametric range.” E122, however, restricts S0 to reporting precision or supported measurement variation. A declared range without supporting exact-configuration evidence does not satisfy that restriction. Recording its kernel parameters makes the simulation reproducible, but does not establish that it measures uncertainty in expected performance, reporting precision or a future deployment run.
paste.txt

Why it hurts the objective: S0 can acquire invented cost dispersion, while S1 core inherits that dispersion and can use it to authorise a cheapest label. A conventional kernel over a justified domain and an analyst-invented domain are materially different assumptions.

Concrete change: Replace the fallback with an explicit rule:

Public rounding supports reporting-precision draws.

Applicable exact-configuration observations support measurement or predictive draws at their evidenced sampling level.

An analyst-selected token-variation range belongs only in a named S2 stress branch.

Without supporting observations, repeatability uncertainty is “not quantified,” not zero. Publish a reporting-precision-only result where possible, but do not describe it as covering token-use variability.

What is new: E58 and E122 already require target and layer metadata. The remaining problem is the operative fallback sentence, which authorises a range without specifying the evidence needed to place it in S0.

Medium

The binomial Monte Carlo certification rule needs an explicit across-scenario sampling contract.

Issue: E72/E77 specify the standard error and Clopper–Pearson stopping intervals, but do not explicitly require independent, identically distributed scenario replicates within an event–kernel specification. Shared variables within one scenario are correctly required to move together; independence across scenario replicates is a different requirement. The binomial model underlying Clopper–Pearson assumes independent Bernoulli trials with a common success probability.
paste.txt
wikipedia
+1

Why it hurts the objective: A later implementation could use correlated MCMC draws, stratified batches or another variance-reduction method while retaining the stated “exact binomial” guarantee. This becomes more likely if sampling from the constrained evidence model grows computationally difficult.

Concrete change: Require IID replicates for every frequency using E77. Allow dependence within each replicate and reuse of random numbers across alternative specifications, but prohibit adaptation of the sampling law within a certified event stream. Other sampling designs must supply a matching error calculation or publish descriptive frequencies without E77 certification.

What is new: This does not challenge the already-adopted repeated-look correction or request simultaneous coverage across all published events. It supplies a missing prerequisite for the existing per-event guarantee.

Low

“Each row’s own normalised weighted spread” is not operationally defined.

Issue: The quality section defines weighted spread using variation across configurations, while governance additionally requires each row’s “own normalised weighted spread.” A single configuration does not have a cross-configuration standard deviation without a specified comparison panel. Row-specific missingness also changes the coefficients and available leaves.
paste.txt

Why it hurts the objective: Implementations can produce inconsistent exposure diagnostics, or readers can mistake cross-sectional discrimination for uncertainty in one configuration.

Concrete change: Either remove this additional statistic or define its panel and formula explicitly. Keep it visibly separate from the already well-defined row-level scenario-dispersion decomposition.

2. Methodology design recommendations
Priority 1 — Make the kernel-check object executable and auditable

Retain the adopted kernel-robustness policy, but replace the current prose with a versioned object containing:

Field	Required content
Primitive dependency components	Components induced by shared primitives and joint sampling mechanisms
Kernel-switch groups	The sets whose conventional kernels change together
Dependency-to-switch mapping	Explicit mapping; no dependency component may receive incompatible laws
Roles touched	Candidate, reference and competitor identities affected by each group
Assignment set	Exact assignments tested, not merely a verbal description
Coverage	Dependency-component-exhaustive or restricted
Execution status	Completed, threshold unresolved, or withheld because the registered checks were not completed

For 
𝐵
B binary-switch groups, the full assignment count is 
2
𝐵
2
B
. Pre-register a resource limit. If the complete registered check cannot be executed, withhold the label rather than silently combining groups after observing results.

Use the narrower wording appropriate to the implemented design:

“Supported under all registered role-group kernel checks”; or

“Supported under all uniform/arcsine assignments across the declared dependency components.”

Neither wording implies robustness to distributions outside the registered family.

This is an implementation clarification of E112–E132, not a proposal to reopen the adopted kernel policy.
paste.txt

Priority 2 — Compile scenario eligibility from evidence, rather than from the presence of a range

Add a mandatory uncertainty-admission table:

Evidence available	Permitted treatment
Published decimal precision	Rounding draws, with reporting-precision interpretation
Public paired task/run observations	Resampling at the supported level
Estimate and applicable documented standard error	Declared approximation for the supported estimand
Supported identification interval	S1 conventional kernel or bounds-only treatment
Analyst-selected token-variation range	Named S2 stress branch only
No evidence for repeatability variation	“Not quantified”; no invented distribution

For example, AA documents its coding-agent cost as a pooled per-task-attempt average and excludes missing telemetry from that metric. Those facts establish how to reproduce the published statistic; they do not by themselves provide a sampling distribution for the missing telemetry or future-run cost variation. Preserve O27’s cost and completeness rules unchanged.
artificialanalysis

The build should reject any S0 primitive whose parameter_derivation points only to an analyst convention rather than supporting measurement evidence. That gives E122 an executable enforcement mechanism.

Priority 3 — Add a sampling-validity certificate to each threshold event

For each event and kernel assignment, publish:

𝑝
^
=
1
𝑁
∑
𝑠
=
1
𝑁
1
{
𝐸
(
𝑣
𝑠
)
}
.
p
	​

=
N
1
	​

s=1
∑
N
	​

1{E(v
s
	​

)}.

The accompanying certificate should state:

The 
𝑣
𝑠
v
s
	​

 are IID draws from the declared scenario law.

All dependence required by the evidence model is retained within 
𝑣
𝑠
v
s
	​

.

The sampling law remains fixed across sequential batches.

The event definition, competitor panel and assignment identity remain fixed.

Any coupling across alternative specifications does not alter the within-specification IID requirement.

Then retain E77’s existing sequential rule. Its Clopper–Pearson calculation is appropriate to a binomial event count; the amendment makes that prerequisite explicit.
wikipedia
+1

No new benchmark data or private measurements are needed for these checks.

Priority 4 — Resolve the row-specific spread diagnostic without adding another uncertainty measure

If the statistic is retained, define it using a named panel 
𝐼
I. For row 
𝑖
i, let its observed-leaf coefficients be

𝑎
𝑖
𝑏
=
{
𝑤
𝑏
/
𝑝
𝑖
,
	
𝑏
∈
𝑂
𝑖
,


0
,
	
𝑏
∉
𝑂
𝑖
.
a
ib
	​

={
w
b
	​

/p
i
	​

,
0,
	​

b∈O
i
	​

,
b∈
/
O
i
	​

.
	​


A possible descriptive allocation is

𝐷
𝑖
𝑏
(
𝐼
)
=
𝑎
𝑖
𝑏
SD
⁡
𝑗
∈
𝐼
(
𝑧
𝑗
𝑏
)
∑
𝑘
∈
𝑂
𝑖
𝑎
𝑖
𝑘
SD
⁡
𝑗
∈
𝐼
(
𝑧
𝑗
𝑘
)
.
D
ib
(I)
	​

=
∑
k∈O
i
	​

	​

a
ik
	​

SD
j∈I
	​

(z
jk
	​

)
a
ib
	​

SD
j∈I
	​

(z
jb
	​

)
	​

.

Require complete observations on the relevant leaves within 
𝐼
I, report its size, and return “not estimable” when the denominator or panel is inadequate. Name this “cross-sectional discrimination under this row’s scoring coefficients,” not row uncertainty.

The simpler option is to omit it: the existing common-panel weighted-spread diagnostic and row-level scenario-variance decomposition already answer the two distinct questions more clearly.
paste.txt

3. Questions for the owner

Should the authorising kernel check vary kernels independently across primitive dependency components, or deliberately switch all competitor components together? The former requires potentially many more assignments; the latter supports a narrower robustness claim.

What exact-configuration evidence is intended to support the fallback “declared parametric range” for token-use variance? If no such evidence exists, should it be moved entirely to S2, leaving S0 explicitly reporting-precision-only for those costs?

4. Verdict

The draft is close to a defensible executable methodology within its deliberately restricted claim scope. The remaining material issues concern reproducibility of the authorising kernel checks and the evidential meaning of scenario variation—not the fixed cohort, exact-variant rule, O27 cost accounting or the already-disclosed lack of identified Plan transport. Those policies need not change to address these findings.
paste.txt

VERDICT: HAS FEEDBACK