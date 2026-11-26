1. Findings by severity
Critical

None.

High

The interval solver’s “no shared factor” shortcut does not cover uncertain reference bars. Issue: E40/E43 says that, without shared factors, each interval label can be decided exactly by monotone extremes. That is not generally true for cheapest-above-a-bar decisions: the uncertain reference quality 
𝑄
𝑟
Q
r
	​

 becomes a common threshold across every qualification condition, even when all primitive uncertainty objects are row-independent. A counterexample using independent row boxes:
Configuration	Cost	Quality
Candidate 
𝑖
i	1	5
Competitor 
𝑗
j	0	4
Reference 
𝑟
r	2	
[
0
,
10
]
[0,10]
At 
𝑄
𝑟
=
0
Q
r
	​

=0, 
𝑗
j qualifies and undercuts 
𝑖
i. At 
𝑄
𝑟
=
10
Q
r
	​

=10, 
𝑖
i does not qualify. But at 
𝑄
𝑟
=
4.5
Q
r
	​

=4.5, 
𝑖
i qualifies, 
𝑗
j does not, and 
𝑖
i is cheapest. Thus 
𝑖
∈
𝐾
𝑟
i∈K
r
	​

, with an interior witness that neither endpoint establishes. Why it hurts: A valid possible-cheapest candidate could be excluded by the proposed shortcut. Concrete change: Restrict the monotone-corner shortcut to decisions with a proved corner reduction. For bar decisions, treat uncertain reference quality as a derived shared variable; partition at qualification breakpoints or use the certified feasibility solver. New relative to E43/E45: The existing interior-witness fixture concerns an explicit shared factor in frontier membership. This failure arises from the endogenous reference bar even without a declared shared-factor input.
paste.txt

E46 records estimand mismatches but does not yet prevent them from narrowing 
Θ
Θ. Issue: The target is expected performance over repeated executions of a fixed suite. However, the draft allows rounding intervals and observed run ranges into 
Θ
Θ, while correctly acknowledging that they constrain a reported result or observed executions—not necessarily that expectation. Preserving an interval’s interpretation in metadata does not make it a valid constraint on another estimand. Confidence-interval coverage likewise depends on the interval-producing procedure and its target.
paste.txt
stats.ox.ac
 Why it hurts: A solver can certify the equations perfectly while its input set excludes plausible values of the declared target. This would make “definite” and “confirmed” stronger than the evidence supports. Concrete change: Add an executable target-compatibility gate. An interval narrows a variable only when its documented target matches that variable, or a public, justified transformation connects them. Otherwise retain the observation for displayed scores and descriptive scenarios, but use the full admissible domain for the expected-performance variable. New relative to E46/O19: This is not a request for analyst repeatability bands. It is a missing enforcement rule between the newly declared constraint target and the variable actually constrained.

Medium

“Certified” conflates computational validity with evidential coverage. Issue: 
Θ
Θ can combine confidence intervals, observed ranges and structural bounds. A deterministic certificate establishes a result conditional on that set; it does not turn the set into a simultaneous confidence region. Individual interval coverage does not itself specify joint coverage across the complete ranking.
paste.txt
stats.ox.ac
 Why it hurts: Readers could interpret “confirmed cheapest” as either an unconditional guarantee or a ranking-level confidence statement. Concrete change: Keep the adopted labels, but attach two distinct fields:

Solver certificate: certified / disproved / unresolved.

Evidence-set coverage: structural / documented simultaneous coverage / joint coverage unspecified.

Display “confirmed within the declared evidence set” where joint coverage is unspecified. Do not invent a joint confidence percentage. New relative to E46: Per-input coverage metadata is already adopted; the missing element is an output-level rule describing what the combined certificate establishes.

A pinned reference can leave the evaluable set without a defined bar policy. Issue: A reference identity is frozen at release, but subsequent missing cost evidence or unidentified Plan transport can exclude it from 
𝑅
𝑊
R
W
	​

. The bar equations still require its quality, while the draft does not explicitly distinguish a reference used only as a threshold from a reference eligible to compete.
paste.txt
 Why it hurts: Implementations could suppress a valid quality threshold unnecessarily, silently substitute a new reference, or treat an ineligible reference as a priced competitor. Concrete change: Give each bar a separate reference-quality object. Require evaluable quality constraints for 
𝑟
r, not necessarily cost or Plan eligibility. Include 
𝑟
r as a competitor only if it independently belongs to 
𝑅
𝑊
R
W
	​

. If reference quality cannot be evaluated, mark the bar unevaluable; never substitute another reference silently. New relative to E38: This concerns threshold availability, not the already-adopted treatment of omitted competitors.

Cost uncertainty lacks the quality side’s explicit estimand discipline. Issue: Quality targets expected repeated-execution performance, but cost draws include resampling or parametric ranges without an equally explicit governing target. The cost being bounded could therefore mean the published benchmark bill, expected cost of repeating the fixed workload, or realised cost of a future pass. These are different quantities.
paste.txt
 Why it hurts: Frontier and cheapest comparisons can combine expected quality with differently interpreted cost bounds, despite appearing to describe one purchasing decision. Concrete change: Declare expected deployment-equivalent cost of the fixed workload as the primary interval estimand. Keep published observed expenditure as the displayed input. Require cost constraints to pass the same target-compatibility gate as quality; publish future-pass expenditure variability separately. New relative to E25/E46: Kernel documentation and general uncertainty metadata exist; the unresolved point is which cost quantity the governing equations represent.

Low

None.

2. Methodology design recommendations
Priority 1 — Compile a decision dependency graph before selecting the solver

Build dependencies from the complete decision equations, not only registry dependency_id fields.

For a bar, define

𝑔
𝑖
(
𝜃
)
=
𝑄
𝑖
(
𝜃
)
−
𝑄
𝑟
(
𝜃
)
.
g
i
	​

(θ)=Q
i
	​

(θ)−Q
r
	​

(θ).

Every 
𝑔
𝑖
g
i
	​

 depends on the reference-quality variables. Mark those dependencies as shared for this decision, even when the underlying row inputs are independent.

Implement:

A documented corner-reduction proof for each supported shortcut.

Exact breakpoint enumeration for affine, one-dimensional reference thresholds where applicable.

Certified branch-and-bound for remaining problems.

The three-row example above as a mandatory regression test.

Keep separate proof obligations for feasible witnesses and infeasibility certificates. Reliable interval optimisation requires numerical bounds that cannot discard feasible solutions through floating-point error; equality-constrained feasibility also needs explicit verification machinery.
link.springer
+1

Priority 2 — Separate observations from target parameters

For every quality and cost object, store:

text
observed_statistic
observed_statistic_constraint
target_parameter
target_parameter_constraint
target_mapping
mapping_evidence

Only target_parameter_constraint enters the primary 
Θ
Θ.

Examples:

A rounded benchmark result constrains the reported statistic.

An observed run range describes the observed executions.

An applicable repeated-run confidence interval may constrain expected fixed-suite performance, retaining its documented coverage.

Without a valid mapping, the expected-performance variable retains its full score domain.

For nonnegative expected cost without a finite evidenced upper bound, allow an unbounded domain or return unevaluable where the solver cannot support it. Do not manufacture a finite primary bound from a parametric sensitivity range.

This implements O19 and E46 rather than relaxing them.
paste.txt

Priority 3 — Publish a compact claim contract beside each interval result

Use a machine-readable and visible summary:

Field	Example
Decision	Possible cheapest above reference 
𝑟
r
Target	Expected fixed-suite quality and cost
Universe	Named evaluable configurations
Evidence-set coverage	Joint coverage unspecified
Solver status	Certified
Selected-cohort extension	Not established
Certificate	Witness or exclusion certificate

This separates three questions: whether the input constraints fit the estimand, whether the solver established the mathematical claim, and whether the result extends beyond the evaluable subset. The draft already addresses much of the third; this design connects all three without changing owner policy.
paste.txt

Priority 4 — Separate bar references from ranked competitors

Define

BarEvaluable
⁡
(
𝑟
)
  
⟺
  
the reference-quality expression and its constraints are evaluable
.
BarEvaluable(r)⟺the reference-quality expression and its constraints are evaluable.

Then:

Evaluate qualification against 
𝑟
r whenever this predicate holds.

Construct the competitor set independently using 
𝑅
𝑊
R
W
	​

.

Preserve the pinned identity through cost-evidence loss.

Report separately whether the reference is itself an eligible competitor.

Add fixtures for a reference with valid quality but missing API cost, and a reference with valid quality but unidentified Plan transport.

No changes to the fixed cohort, exact-variant evidence policy, nominal weights, or Value Multiple admission rules are needed for these recommendations.

3. Questions for the owner

For interval outputs, should cost mean expected cost over repeated executions of the fixed workload, or the cost of one future deployment-equivalent pass? The answer changes which public cost intervals are applicable.

May a pinned reference remain a quality threshold after losing cost or Plan eligibility? I recommend yes, provided its quality constraints remain evaluable.

4. Verdict

VERDICT: HAS FEEDBACK