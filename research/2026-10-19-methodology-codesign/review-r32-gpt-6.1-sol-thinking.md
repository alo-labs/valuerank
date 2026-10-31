1. Findings by severity
Critical

None.

High
H1. Plan-report comparability is specified, but report selection and conflicting-report handling remain underdetermined

Issue: E102 establishes whether reports can be pooled, and E98 tests concordance before pooling. Neither establishes a reproducible rule for selecting the reports to test when more than two comparable reports exist. For example, comparable reports of 100, 110 and 150 contain an admissible-looking pair, although the complete set fails concordance. The current specification does not explicitly prohibit choosing the pair and admitting the route. This finding concerns evidence-set construction, not the already-adopted comparability or concordance tests.
paste.txt

Why it hurts the objective: Two implementations could select different reports, admit different routes and publish different Plan rankings while each claims to satisfy the two-report rule. A contrary report could also disappear into a separate measurement object without a documented reason.

Concrete change: Before testing concordance, construct a versioned report set using a preregistered discovery window, public-source search procedure and inclusion/exclusion rules. Test every eligible, comparable report in that set together. Do not search for a passing subset. Where public evidence establishes a limit-schema change, partition reports using that change; otherwise record the disagreement and apply the diagnostic-only outcome for failed concordance. Publish excluded reports and their exclusion reasons.

Medium
M1. The constrained solver needs an explicit mechanism for certifying feasibility on equality-constrained sets

Issue: E73 correctly makes the original constrained set authoritative, and E79 requires a certified feasible witness. However, the executable procedure principally describes interval subdivision and checking candidate witnesses. It does not specify how feasibility is certified when the feasible set lies on an equality manifold, particularly with nonlinear identities or capacity-optimality conditions. This is a remaining implementation gap, not a request to repeat E73 or E79.
paste.txt

Why it hurts the objective: A numerical approximation to a feasible point is not necessarily an exact feasible witness. Conversely, requiring an entire positive-width box to satisfy an equality can leave an otherwise straightforward problem permanently unresolved. Rigorous interval optimization treats equality-feasibility verification as a separate problem, using methods such as interval Newton verification rather than ordinary approximate substitution alone.
interval.louisiana

Concrete change: Publish a supported constraint grammar and certification backend:

Eliminate definitional equalities by substitution wherever possible.

Use exact rational feasibility for affine constraints and published decimal inputs.

For supported nonlinear equalities, require a validated existence certificate.

Return unresolved for unsupported classes without attempting approximate certification.

Add a fixture with a feasible non-rational solution, such as 
𝑥
2
=
2
,
 
𝑥
∈
[
1
,
2
]
x
2
=2, x∈[1,2], and a nearby inconsistent system. The implementation must distinguish validated existence from a small numerical residual.

M2. Cost and capacity domain requirements are not complete at the scoring boundary

Issue: Cost scoring requires 
ln
⁡
𝑐
lnc, while Plan scoring requires division by the displayed multiple. The draft explicitly requires strictly positive finite bounds for set-identified multiples, but does not state a corresponding universal input-domain contract for point-identified multiples, observed multiples, component costs, workload totals and anchor endpoints. Zero-cost or zero-delivery observations therefore lack a complete scoring rule.
paste.txt

Why it hurts the objective: A legitimate zero-dollar observation, an unavailable price encoded as zero, and a zero-consumption measurement must not produce the same computational treatment. Otherwise implementations can generate infinities, silently cap values or mistake missing evidence for unusually good value.

Concrete change: Validate domains before route comparison and anchor construction:

Component costs must be finite and nonnegative; missing costs remain missing.

Positive-cost log scoring requires 
0
<
𝑐
𝐿
<
𝑐
𝐻
<
∞
0<c
L
	​

<c
H
	​

<∞.

Every multiple used as a divisor must be finite and strictly positive.

Zero eligible consumption does not supply a usable positive-multiple score.

Define a documented zero-workload-cost extension, or classify that scoring case as unsupported. Do not introduce an arbitrary epsilon.

Low
L1. Quality clipping lacks a parallel observability contract

Issue: Quality retains unclipped values, but the active-rules manifest does not explicitly require a per-leaf clipping count or distinguish valid saturation from an input outside the metric’s documented domain. Cost clipping receives much more explicit treatment. This does not challenge frozen quality anchors or request automatic re-anchoring.
paste.txt

Why it hurts the objective: A legitimate GDPval value beyond its scoring anchor and an invalid percentage above 100 can both become a clipped score of 100, despite requiring different responses. Silent saturation can also hide lost discrimination.

Concrete change: Publish per leaf the count and identities of clipped rows, their raw values and clipping reasons. Treat valid anchor saturation as a disclosure; treat violation of a documented metric domain as a data-validation error. Add these outcomes to the active-rules manifest.

2. Methodology design recommendations
Priority 1 — Freeze the Plan evidence set before evaluating concordance

Add an evidence-selection object:

𝐸
𝑟
,
𝑡
=
{
𝑘
:
report 
𝑘
 satisfies the preregistered inclusion rules for route 
𝑟
 at release 
𝑡
}
.
E
r,t
	​

={k:report k satisfies the preregistered inclusion rules for route r at release t}.

Apply E102 comparability partitions to 
𝐸
𝑟
,
𝑡
E
r,t
	​

, then apply E98 to every eligible report within each partition. Source count must count distinct independent measurement objects, not posts or citations.

Publish:

Discovery procedure and cutoff date.

Included report IDs and observation periods.

Excluded report IDs and reason codes.

Schema-partition evidence.

Concordance outcome for the complete eligible partition.

Which reports determine the displayed measurement and its uncertainty.

This preserves O11 and the fixed numerator rules. Its new contribution is preventing evidence-subset selection from becoming an undocumented ranking parameter. The existing geometric-mean pooling rule can remain unchanged after this gate.
paste.txt

Priority 2 — Separate constraint semantics from the numerical solver

Compile each decision into three objects:

Primitive domains and original constraints.

A reduced problem obtained through documented, equivalence-preserving substitutions.

A certificate checked independently against the original problem.

A minimal routinely maintainable v1 can support affine constraints with exact arithmetic, separable monotone transforms and the existing certified corner reductions. More elaborate nonlinear classes can remain unresolved until a validated backend exists.

For nonlinear equality constraints, distinguish a verified root enclosure from an approximate point with a small residual. Interval feasibility literature explicitly identifies this distinction as necessary for rigorous bounds.
interval.louisiana

This recommendation does not change the frontier or bar definitions. It makes their existing certification promises operational.

Priority 3 — Add a shared numerical-domain validator

Use one validator across displayed scores, anchors, scenarios and interval outputs:

PositiveCostScoreable
⁡
(
𝑐
)
  
⟺
  
𝑐
∈
𝑅
,
0
<
𝑐
<
∞
,
PositiveCostScoreable(c)⟺c∈R,0<c<∞,
DivisorEligible
⁡
(
𝑀
)
  
⟺
  
𝑀
∈
𝑅
,
0
<
𝑀
<
∞
.
DivisorEligible(M)⟺M∈R,0<M<∞.

Keep domain validity separate from evidence completeness: a published zero is not missing, but it may require a special scoring branch. Likewise, a positive numeric value is not evidence of completeness.

For genuine zero workload cost, the natural right-limit extension is:

𝑆
𝐶
(
0
)
=
100.
S
C
	​

(0)=100.

If adopted, identify zero separately in dollar displays, exclude it from logarithmic anchor construction, and show the corresponding unclipped logarithmic diagnostic as undefined or 
+
∞
+∞, not as an epsilon-based finite number. Freeze this extension as a methodology rule rather than deciding it per release. The existing log formula otherwise remains unchanged.
paste.txt

Priority 4 — Expose quality saturation without changing quality weights

Add a small quality-normalization audit:

Field	Meaning
Raw-domain validity	Whether the observation satisfies the source metric’s documented domain
Anchor position	Below, inside or above the frozen scoring anchors
Clipping amount	Difference between unclipped and clipped normalized score
Affected weight	Nominal quality weight subject to saturation
Action	Accept and disclose, or reject as invalid input

No new benchmark, imputation, weight change or additional uncertainty kernel is needed. The audit uses values already required by the registry.
paste.txt

3. Questions for the owner

When a third eligible, comparable Plan report makes the complete report set fail concordance, should the route become diagnostic-only, or is there an intended public rule for determining that the report belongs to a different measurement regime? This determines whether H1 needs only implementation detail or an additional adjudication policy.

Is a genuine zero-dollar workload cost within ValueRank’s intended scope? If yes, adopt an explicit zero-cost scoring extension; if no, declare the supported positive-cost domain rather than leaving the case implicit.

4. Verdict

VERDICT: HAS FEEDBACK