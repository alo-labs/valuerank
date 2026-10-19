1. Findings by severity
Critical

None.

High

E40’s extreme-point procedure is not sufficient for possible-frontier certification.

Issue: The joint-set definitions are sound, but their proposed implementation does not generally follow from monotonicity of individual scores. “There exists a scenario with no dominator” is a simultaneous, disjunctive feasibility problem—not simply an extremum of a monotone function. Extreme points relevant to a constrained optimisation problem belong to its feasible region, not necessarily to the original uncertainty box.
paste.txt
math.mit

Counterexample: Let 
𝑡
∈
[
0
,
1
]
t∈[0,1]. Configuration 
𝑖
i has cost 1 and quality 1.2. Two competitors have cost 0, with qualities 
𝑄
𝑗
=
2
𝑡
Q
j
	​

=2t and 
𝑄
𝑘
=
2
(
1
−
𝑡
)
Q
k
	​

=2(1−t). At either endpoint, one competitor dominates 
𝑖
i. At 
𝑡
=
0.5
t=0.5, neither does. Thus 
𝑖
i is a possible-frontier member, but checking only the shared factor’s endpoints misses its witness.

Why it hurts the objective: A solver could incorrectly exclude a genuinely possible low-cost/high-quality option, despite the published definitions being correct.

Change: Replace the blanket extreme-point prescription with a decision-specific feasibility formulation. Use LP/MILP where the declared functions permit it, and certified interval branch-and-bound otherwise. Preserve “unresolved” when certification fails.

New relative to E40: This challenges the adequacy of the newly adopted algorithm, not the already-adopted requirement for deterministic certification.

E37’s aggregate-ratio completeness test can confuse numerical precision with missing tasks.

Issue: For aggregates, total ÷ mean = required count within 10⁻⁶ is treated as equivalent to complete telemetry. But if either published quantity is rounded, complete telemetry need not satisfy that equality. Conversely, a matching ratio alone does not establish that the same required task support underlies both fields. The draft already reports non-integer ratios for two configurations, but does not establish whether these are rounding effects, aggregation differences, or genuinely missing telemetry.
paste.txt

Why it hurts the objective: This determines membership of 
𝑅
𝑊
R
W
	​

, so a numerical presentation detail can remove competitors from frontier and bar results.

Change: Establish task-support completeness from explicit public counts or task-level records where available. Otherwise perform an interval compatibility test using the source fields’ published precision, and distinguish “compatible with complete telemetry” from “confirmed complete.”

New relative to E37: Retain the complete-cost requirement and prohibition on imputation. Correct the proposed operational equivalence between completeness and a point-valued ratio.

Plan transport does not explicitly require evidence for the workload’s token-demand vector.

Issue: The governing capacity formula requires 
𝑥
𝑘
x
k
	​

, the category-specific tokens per unit of 
𝑊
W. Yet the cost-basket contract principally requires public dollar totals. A scalar dollar cost does not uniquely determine input, cache, reasoning and output token quantities. Consequently, admitting a cost component does not establish that its contribution to 
𝑥
𝑘
x
k
	​

 is publicly recoverable.
paste.txt

Why it hurts the objective: A route could appear to have an identified target-workload multiple because its quota coefficients and measured capacity are known, while the workload demand inserted into that capacity model is underdetermined. Category mix is also not automatically sufficient: Claude’s documentation identifies conversation complexity, tools, model and effort as factors affecting usage limits. This is structural evidence, not a permissible Value Multiple numerator.
support.claude

Change: Add a separate workload-demand evidence object. Require exact-configuration category vectors—or public bounds covering all compatible vectors—before additive-capacity transport can identify 
𝑀
𝑊
M
W
	​

. Where this is unavailable, retain the displayed score under O16 but mark this transport mechanism unidentified.

New relative to E30/E32/E39: Those decisions address quota semantics, repricing and schedule feasibility. This addresses the missing evidence contract for the demand side of the same program.

Medium

The cheapest-above-bar candidate set is not executable.

Issue: E38 specifies confirmed and scenario-supported cheapest labels, but only says that ties appear in a “candidate set,” which is “published otherwise.” It does not define whether this means every possible qualifier, every potentially cheapest qualifier, or only tied point-estimate winners.
paste.txt

Why it hurts the objective: These sets answer materially different buyer questions. Including every possible qualifier could retain a configuration that can never be cheapest.

Change: Define a possible-cheapest set using simultaneous qualification and cost comparisons in one admissible scenario. Publish “possible” and “certified possible” separately if solver status requires it.

New relative to E38: Preserve its self-comparison, tie and scope fixes; supply the missing mathematical definition of its fallback output.

Full-domain uncertainty lacks a declared inference target.

Issue: The draft distinguishes observed means, repeated runs, published intervals and full score domains, but does not consistently state whether a leaf’s uncertainty concerns the fixed published benchmark result, expected performance on repeated executions, or generalisation to new tasks. For example, a single-run Bug Hunt row receives 
[
0
,
100
]
[0,100], while the general rule accepts public repeated runs without prescribing what quantity their spread bounds.
paste.txt

Why it hurts the objective: Two implementations could treat an observed run range as either a sensitivity range or an identified bound on expected future performance, producing different “definite” results from the same public evidence.

Change: Require estimand, randomness_unit and constraint_target fields for every uncertainty object. An observed minimum/maximum should retain its meaning as an observed range unless a documented method supports a broader inference.

New relative to E11/E25/O19: This does not request narrower uncertainty or analyst allowances. It makes the target of the accepted evidence types consistent across leaves.

Low

The singleton cheapest fixture omits the provisional-status condition.

Issue: The fixture says a singleton evaluable set’s qualifying row is confirmed cheapest, but the governing definition additionally requires that row not be provisional. A singleton provisional row is a counterexample to the fixture as written.
paste.txt

Why it hurts the objective: Conflicting acceptance tests can silently override the intended qualification safeguards.

Change: Specify “singleton, confirmed-qualified, non-provisional row → confirmed cheapest,” and add a separate provisional singleton fixture that receives no confirmed-cheapest label.

2. Methodology design recommendations
Priority 1 — Implement decision-specific certification

Keep the mathematical definitions, but replace E40’s generic search instruction with explicit solver contracts.

For possible-frontier membership of 
𝑖
i, seek one common 
𝜃
θ satisfying, for every competitor 
𝑗
j,

𝐶
𝑗
(
𝜃
)
>
𝐶
𝑖
(
𝜃
)
∨
𝑄
𝑗
(
𝜃
)
<
𝑄
𝑖
(
𝜃
)
∨
[
𝐶
𝑗
(
𝜃
)
=
𝐶
𝑖
(
𝜃
)
∧
𝑄
𝑗
(
𝜃
)
=
𝑄
𝑖
(
𝜃
)
]
.
C
j
	​

(θ)>C
i
	​

(θ)∨Q
j
	​

(θ)<Q
i
	​

(θ)∨[C
j
	​

(θ)=C
i
	​

(θ)∧Q
j
	​

(θ)=Q
i
	​

(θ)].

This expresses “
𝑗
j does not dominate 
𝑖
i” and retains exact ties.

Implementation:

Use disjunctive LP/MILP formulations for bounded affine inputs and declared piecewise-linear functions.

For nonlinear Plan ratios or capacity-derived functions, use certified interval subdivision or another solver with validated bounds.

Treat strict inequalities explicitly. A floating-point tolerance alone must not establish strict superiority.

Validate every returned witness against the original equations and shared constraints.

Add the interior-witness counterexample above to release tests.

The distinction between a box’s corners and the vertices of the actual constrained feasible region matters even in linear optimisation.
math.mit

Priority 2 — Separate telemetry completeness from arithmetic reconciliation

For public total 
𝑇
T, public mean 
𝜇
μ, and required count 
𝑛
n, represent source precision as intervals:

𝑇
∈
[
𝑇
𝐿
,
𝑇
𝑈
]
,
𝜇
∈
[
𝜇
𝐿
,
𝜇
𝑈
]
.
T∈[T
L
	​

,T
U
	​

],μ∈[μ
L
	​

,μ
U
	​

].

A necessary aggregate consistency condition is

[
𝑇
𝐿
,
𝑇
𝑈
]
∩
[
𝑛
𝜇
𝐿
,
𝑛
𝜇
𝑈
]
≠
∅
.
[T
L
	​

,T
U
	​

]∩[nμ
L
	​

,nμ
U
	​

]

=∅.

Use three statuses:

Status	Public evidence	Interval-output treatment
Confirmed complete	Explicit matching support/count, or complete task-level records	Eligible under E37
Completeness unresolved	Aggregate intervals are consistent, but support is not established	Unevaluable
Confirmed incomplete/inconsistent	Explicit missing telemetry, or incompatible aggregate identities	Unevaluable; publish reason

This preserves the owner’s no-imputation policy. Do not infer fractional missing-task counts from rounded ratios.

Priority 3 — Add a workload-demand transport contract

For each configuration and workload version, publish:

𝑥
𝑖
𝑊
𝑘
=
∑
𝑒
𝑛
𝑒
𝑥
𝑖
𝑒
𝑘
,
x
iWk
	​

=
e
∑
	​

n
e
	​

x
iek
	​

,

where 
𝑥
𝑖
𝑒
𝑘
x
iek
	​

 is category-
𝑘
k token consumption per deployment-equivalent task.

The object should include:

Exact configuration, execution stack and task support.

Token-category definitions and source-field precision.

Cache-policy compatibility.

Joint feasible bounds where only partial token information exists.

Evidence that the capacity mechanism covers the relevant context lengths, tool use and effort—or conservative bounds covering those differences.

Where several demand vectors are compatible with public evidence, optimise capacity over that feasible set rather than selecting an arbitrary vector:

𝑀
𝑊
𝐿
=
inf
⁡
𝑥
∈
𝑋
𝑖
𝑊
,
 
𝑎
,
𝐵
∈
𝐴
𝑀
(
𝑥
,
𝑎
,
𝐵
)
,
𝑀
𝑊
𝑈
=
sup
⁡
𝑥
∈
𝑋
𝑖
𝑊
,
 
𝑎
,
𝐵
∈
𝐴
𝑀
(
𝑥
,
𝑎
,
𝐵
)
.
M
W
L
	​

=
x∈X
iW
	​

,a,B∈A
inf
	​

M(x,a,B),M
W
U
	​

=
x∈X
iW
	​

,a,B∈A
sup
	​

M(x,a,B).

Here 
𝐴
A contains the publicly evidenced capacity constraints, with dependencies preserved. A feasible schedule certifies attainability conditional on its demand and quota inputs; it does not independently validate those inputs.

Priority 4 — Define the fallback candidate set

A useful possible-cheapest definition is:

𝑖
∈
𝐾
𝑟
  
⟺
  
∃
𝜃
∈
Θ
:
𝑄
𝑖
(
𝜃
)
≥
𝑄
𝑟
(
𝜃
)
∧
∀
𝑗
≠
𝑖
,
  
[
𝑄
𝑗
(
𝜃
)
<
𝑄
𝑟
(
𝜃
)
∨
𝐶
𝑖
(
𝜃
)
≤
𝐶
𝑗
(
𝜃
)
]
.
i∈K
r
	​

⟺∃θ∈Θ:Q
i
	​

(θ)≥Q
r
	​

(θ)∧∀j

=i,[Q
j
	​

(θ)<Q
r
	​

(θ)∨C
i
	​

(θ)≤C
j
	​

(θ)].

This permits tied cheapest qualifiers and excludes configurations that can never be cheapest in any common admissible scenario.

Publish:

Confirmed unique cheapest, if established.

Certified possible-cheapest members.

Unresolved membership.

Provisional status beside each candidate.

Keep the existing 
𝑅
𝑊
R
W
	​

 universe and selected-cohort extension labels. This completes E38 rather than replacing it.

Priority 5 — Make uncertainty meaning machine-checkable

Extend each uncertainty object with:

text
estimand
randomness_unit
constraint_target
coverage_claim
supporting_public_evidence

Examples:

A rounding interval bounds an underlying reported numerical value.

A run-level range describes observed executions.

A published confidence interval targets the quantity specified by its source.

A full score domain expresses lack of a narrower admissible constraint.

Then reject any transformation that silently converts one target into another. Keep scenario kernels separate from the evidence supporting the admissible set, as E25 already requires.
paste.txt

No weight changes are necessary to implement these recommendations. They primarily make the existing policy executable without changing its buyer definitions, cohort, exact-variant rule or evidence restrictions.

3. Questions for the owner

Do AA’s captured source records expose unrounded totals and means, explicit cost-observed counts, and matching task-support identifiers? If so, the completeness fix can rely on those fields rather than aggregate interval checks.

Is the intended uncertainty target fixed-suite performance, expected performance on repeated runs of those tasks, or generalisation to new tasks? This changes which constraints public run-level data can support.

Are category-level token vectors publicly recoverable for every admitted workload component? If not, which existing Plan routes identify 
𝑀
𝑊
M
W
	​

 through direct compatible-workload measurement rather than additive-capacity transport?

Does the proposed E40 implementation already search dominance-boundary intersections or solve the full disjunctive feasibility problem? If so, its implementation may be adequate, but the normative description still needs correction.

4. Verdict

VERDICT: HAS FEEDBACK