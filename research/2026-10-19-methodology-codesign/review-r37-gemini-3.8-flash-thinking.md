1. Findings by severity
Critical

None.

High
H1. The demand registry does not explicitly separate Intelligence Index accounting support from Coding Agent Index accounting support

Issue: E124 describes constructing the admitted basket’s feasible demand region using per-component costs and output tokens together with Intelligence Index-wide category totals. However, basket v1 also contains the separately executed Coding Agent Index. The Intelligence Index totals cannot constrain that additional execution’s consumption, even where benchmark families overlap. Conversely, the seven admitted Intelligence Index evaluations cannot be equated to the whole Index totals without retaining residual variables for the three excluded evaluations. AA documents the Coding Agent Index as its own suite with pooled per-task-attempt telemetry, rather than as part of the Intelligence Index accounting population.
paste.txt
artificialanalysis
+1

Why it hurts the objective: An incorrectly scoped conservation constraint can produce an empty demand region or an artificially narrow one. The latter could falsely identify Plan capacity and effective cost—the central quantity distinguishing the Plan ranking from the API ranking. The existing demand–cost reconciliation test would not necessarily catch this: dollar identities can hold while category totals are allocated across the wrong execution populations.

Concrete change: Partition the registry into separately conserved accounting populations. Constrain the ten Intelligence Index executions against their own totals, retain the excluded evaluations as non-scored residual demand, and give the Coding Agent Index its own demand variables and telemetry constraints. Combine only the seven selected Index components and the Coding Agent component when deriving the scored workload vector.

What is new: E84 checks aggregation and dollar reconciliation, while E124 adds the demand registry. Neither explicitly states the cross-suite conservation equations or requires excluded-component residuals. This is an accounting-support correction, not a challenge to O27 or a request for imputation.

Medium
M1. The token-category contract needs an executable distinction between total output and answer-only output

Issue: The draft lists “reasoning” and “output” as separate demand coordinates while also importing published “output tokens per task.” AA describes output tokens as including reasoning and answer tokens, and its cost breakdown distinguishes reasoning from answer tokens. Thus a published output field cannot automatically become an additive coordinate alongside reasoning.
paste.txt
artificialanalysis
+2

Why it hurts the objective: A direct mapping can double-count reasoning tokens. Even where cost reconciliation prevents that particular mistake, inconsistent category definitions can invalidate the comparison with a plan measurement or burn-coefficient model. Equal reasoning and answer prices can also make a dollar check insufficient to detect a category-allocation error.

Concrete change: Require a field-level token ontology and conversion expression. Use mutually exclusive canonical coordinates such as uncached input, cache read, cache write, reasoning, and answer-only output. Record whether each source field is inclusive, exclusive, or unresolved. Permit subtraction of reasoning from total output only when their execution, aggregation, and telemetry supports match.

What is new: E44 already requires category definitions and E84 requires compatible supports. The missing implementation detail is the explicit inclusive-to-exclusive mapping for the AA output fields actually named in E124.

M2. The eight kernel assignments are not well-defined when candidate, reference, and competitors share primitives

Issue: E121 defines three kernel blocks by decision role—candidate, reference, and competitors—and requires all eight uniform/arcsine assignments while keeping shared primitives shared. These roles need not partition the primitive variables. The candidate can be the reference itself; the reference can also be a competitor; and shared measurement or price primitives can affect multiple roles. The draft does not specify which kernel applies when one primitive receives conflicting role assignments.
paste.txt

Why it hurts the objective: Different implementations could generate different kernel checks, withhold different labels, or inadvertently duplicate a shared primitive. This affects the reproducibility of “scenario-supported cheapest,” despite the otherwise strong decision-target and dependency contracts.

Concrete change: Assign kernels to primitive dependency blocks first, then map decision roles onto those blocks. Never give one primitive two kernel laws within an assignment. Enumerate the resulting distinct assignments when feasible; otherwise publish a pre-registered restricted assignment set and describe its actual coverage. Handle candidate-equals-reference explicitly so that self-qualification remains an identity under every draw.

What is new: E83 preserves shared primitives and E121 adds role-block checks. The unresolved issue is their interaction when roles overlap, not the already-adopted choice of uniform versus arcsine kernels.

Low

None.

2. Methodology design recommendations
Priority 1 — Make demand conservation execution-population-specific

For configuration 
𝑖
i, let:

𝐽
J be the ten Intelligence Index execution components.

𝑆
⊂
𝐽
S⊂J be the seven admitted SDLC Index components.

𝐴
A be the separately accounted Coding Agent Index component.

𝑑
𝑖
𝑒
d
ie
	​

 be the deployment-equivalent demand vector for execution component 
𝑒
e.

Where the published Index category totals have compatible accounting support, impose:

∑
𝑒
∈
𝐽
𝑑
𝑖
𝑒
=
𝑇
𝑖
I
n
d
e
x
.
e∈J
∑
	​

d
ie
	​

=T
i
Index
	​

.

Then derive the scored workload demand as:

𝑑
𝑖
𝑊
=
∑
𝑒
∈
𝑆
𝑑
𝑖
𝑒
+
𝑑
𝑖
𝐴
.
d
iW
	​

=
e∈S
∑
	​

d
ie
	​

+d
iA
	​

.

The excluded evaluations remain in the first equation but not the second. Coding Agent Index demand never consumes the Intelligence Index total. Where a published total covers only some token categories, impose conservation only on those coordinates.

For the Coding Agent component, use:

𝑑
𝑖
𝐴
=
303
 
𝑡
‾
𝑖
𝐴
d
iA
	​

=303
t
iA
	​


only when the category means have the required pooled aggregation and compatible telemetry support. AA explicitly excludes missing telemetry separately from a metric’s average, so compatibility across cost and token metrics must be checked rather than presumed. Failure leaves this transport mechanism unidentified; it does not alter O27’s displayed cost or completeness policy.
paste.txt
artificialanalysis

Add these registry fields:

accounting_population_id

execution_component_id

conservation_total_id

conservation_support

excluded_component_residual_ids

aggregation_support_compatibility

Add three regression fixtures:

Changing Coding Agent demand cannot change the Intelligence Index conservation residual.

Excluded Index evaluations can retain positive demand without adding it to 
𝑊
W.

Two executions of the same benchmark family remain separate demand populations.

This design uses public telemetry and feasible domains only; it does not estimate missing category shares.

Priority 2 — Make token conversion machine-checkable before constructing the feasible region

Adopt a mutually exclusive canonical vector:

𝑑
=
(
𝑑
i
n
p
u
t
,
u
n
c
a
c
h
e
d
,
𝑑
c
a
c
h
e
,
r
e
a
d
,
𝑑
c
a
c
h
e
,
w
r
i
t
e
,
𝑑
r
e
a
s
o
n
i
n
g
,
𝑑
a
n
s
w
e
r
)
.
d=(d
input,uncached
	​

,d
cache,read
	​

,d
cache,write
	​

,d
reasoning
	​

,d
answer
	​

).

Every imported token field should specify its canonical mapping and support. For example:

𝑑
a
n
s
w
e
r
=
𝑑
o
u
t
p
u
t
,
t
o
t
a
l
−
𝑑
r
e
a
s
o
n
i
n
g
d
answer
	​

=d
output,total
	​

−d
reasoning
	​


is admissible only when the source establishes that total output includes reasoning and both quantities use compatible supports. Otherwise retain the available identity as a partial constraint rather than manufacturing a split. AA’s public presentation distinguishes total output from its reasoning and answer breakdown, making this a practical ingestion requirement.
artificialanalysis
+2

Require three independent validations:

Category conservation.

Price–demand reconciliation.

Matching execution and telemetry support.

Include a fixture with equal reasoning and answer prices. It should demonstrate that a wrong category mapping can pass a dollar reconciliation while failing the token ontology check.

No quality weights, cost weights, or normalization rules need to change for these corrections.

Priority 3 — Define kernel coverage over dependencies, not overlapping roles

For each cheapest-above-bar event:

Compile its primitive dependency graph.

Identify blocks that must share a joint sampling mechanism.

Attach candidate/reference/competitor role tags to those blocks.

Register admissible kernel alternatives for each block.

Enumerate distinct assignments without assigning conflicting laws to a shared primitive.

With 
𝐵
B independently assignable binary kernel blocks, the exhaustive set contains 
2
𝐵
2
B
 assignments—not necessarily eight. If full enumeration is too expensive, retain a smaller, frozen check set, but report it as restricted coverage rather than block-exhaustive coverage.

Preserve E77’s sequential threshold test for each checked event specification. A label should identify the assignment-set version that authorized it.

Required fixtures:

Candidate equals the reference.

Reference is also a competing configuration.

One primitive affects candidate and competitors.

A primitive has no conventional kernel alternative and remains governed by its evidenced sampling law.

This changes neither the selected kernel families nor the substantive 90% threshold. It makes their application reproducible.

3. Questions for the owner

Does the intended E124 implementation already maintain separate conservation populations for the Intelligence Index and Coding Agent Index, including residual demand for the three excluded Index evaluations? If so, H1 becomes a documentation and regression-test correction rather than a solver redesign.

For E121, is the intended priority exactly eight role-based checks, or exhaustive checks over non-overlapping dependency blocks? When roles share primitives, those requirements cannot generally both hold. The answer determines whether to revise the assignment construction or narrow the published coverage claim.

4. Verdict

The remaining feedback concerns reproducibility of Plan demand accounting and scenario-label checks, not the fixed cohort, exact-variant policy, evidence admission rules, or headline weights. The draft already addresses the major conceptual limitations; these changes would close specific gaps between its stated contracts and an executable implementation.
paste.txt

VERDICT: HAS FEEDBACK