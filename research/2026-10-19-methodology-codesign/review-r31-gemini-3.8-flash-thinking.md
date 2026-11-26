1. Findings by severity
Critical

None.

High
H1. Capacity bounds do not automatically bound the Value Multiple when gross cash depends on consumption

Issue. E80 correctly defines the endogenous-payment target: maximise eligible consumption, then minimise gross cash among consumption-maximising solutions. E56 separately requires a feasible capacity lower bound and a relaxed capacity upper bound, and the schedule contract says the resulting interval is carried into the bound on 
𝑀
𝑊
M
W
	​

. That conversion is valid with fixed gross cash, but not generally with consumption-dependent payments. The draft does not specify the additional proof obligation for this case.
paste.txt

A counterexample illustrates the gap:

A verified feasible schedule delivers API-valued consumption 
𝑈
=
10
U=10 for gross cash 
𝐹
=
1
F=1, giving 
𝑀
=
10
M=10.

The consumption-maximising schedule delivers 
𝑈
=
20
U=20 for gross cash 
𝐹
=
10
F=10, giving the scored target 
𝑀
=
2
M=2.

The feasible schedule certifies a lower bound on attainable consumption, but its multiple, 10, is not a lower bound on the target multiple, 2. Optimising consumption and evaluating a ratio at that optimum are different operations; ratio objectives require explicit treatment of their denominators.
seas.ucla

Why it hurts the objective. An incorrectly certified 
𝑀
𝑊
M
W
	​

 interval can affect Plan cost, route dominance, route selection, and frontier or cheapest-above-bar claims. Primitive sampling and identity checks alone would not catch this: both schedules can satisfy every accounting identity.

Concrete change. Add an endogenous-payment certification contract that bounds the multiple evaluated at consumption-optimal, minimum-cash solutions—not at arbitrary feasible schedules. Until such a certificate exists, publish capacity bounds but leave target-workload 
𝑀
𝑊
M
W
	​

 unidentified.

What is new relative to the ledger. This does not repeat the adopted requests for funding-aware capacity, endogenous payments, or feasible/relaxed scheduling bounds. It addresses their interaction: E80’s lexicographic target changes what E56 must certify.

Medium
M1. The official Plan admission rules still give contradictory instructions for workload and valuation-basis mismatches

Issue. The Assumptions paragraph says that any other mismatch, expressly including workload and price basis, is excluded from the official Plan ranking. Elsewhere, O16 and its implementing provisions retain measured routes with unidentified 
𝑀
𝑊
M
W
	​

, including routes whose original valuation basis cannot be repriced, in that same ranking with flags. The comparator also explicitly supports unidentified routes on different valuation bases. These are operationally different admission instructions, not merely different descriptions of uncertainty.
paste.txt

Why it hurts the objective. Two implementations can use the same public evidence and produce different official Plan tables before any scoring occurs. This also undermines the claim that route selection is reproducible from the admissible-route file alone.

Concrete change. Replace the broad mismatch sentence with an explicit admission decision table that distinguishes:

Exact execution-identity incompatibility.

An owner-authorised transfer.

A valid exact-route measurement whose target-workload transport is unidentified.

A valid exact-route measurement whose valuation basis cannot be reconciled.

Evidence failing the source-count, comparability, concordance, or expiry rules.

Consistent with O16, cases 3 and 4 should remain displayed and scored where otherwise admissible, but remain excluded from Plan interval outputs. Unsupported execution-identity mismatches should not enter as exact-route measurements.

What is new relative to the ledger. This is not another request to remove unmatched or assumed multiples. It is a request to reconcile the residual exclusion sentence with O16, E85/E93, and the explicit original-valuation-basis display rule.
paste.txt

Low

None.

2. Methodology design recommendations
Priority 1: Certify the endogenous-payment estimand explicitly

For each admissible evidence state 
𝑣
v, let 
𝑌
(
𝑣
)
Y(v) be the feasible schedules and funding flows under the recorded purchase policy. Define:

𝑈
∗
(
𝑣
)
=
max
⁡
𝑦
∈
𝑌
(
𝑣
)
𝑈
(
𝑦
,
𝑣
)
,
U
∗
(v)=
y∈Y(v)
max
	​

U(y,v),
𝐹
∗
(
𝑣
)
=
min
⁡
𝑦
∈
𝑌
(
𝑣
)


𝑈
(
𝑦
,
𝑣
)
=
𝑈
∗
(
𝑣
)
𝐹
(
𝑦
,
𝑣
)
,
F
∗
(v)=
y∈Y(v)
U(y,v)=U
∗
(v)
	​

min
	​

F(y,v),
𝑀
∗
(
𝑣
)
=
𝑈
∗
(
𝑣
)
𝐹
∗
(
𝑣
)
.
M
∗
(v)=
F
∗
(v)
U
∗
(v)
	​

.

This implements E80 without substituting multiple-maximisation for consumption-maximisation. The identified interval must enclose:

𝑀
𝑊
𝐿
=
inf
⁡
𝑣
∈
𝑉
𝑀
∗
(
𝑣
)
,
𝑀
𝑊
𝑈
=
sup
⁡
𝑣
∈
𝑉
𝑀
∗
(
𝑣
)
,
M
W
L
	​

=
v∈V
inf
	​

M
∗
(v),M
W
U
	​

=
v∈V
sup
	​

M
∗
(v),

where 
𝑉
V contains only publicly supported parameter states and structural bounds. It must not be obtained simply by converting two schedules’ consumption values into multiples. The mathematical distinction follows from the dependence of a ratio on both numerator and denominator.
seas.ucla

An implementable certification hierarchy is:

Payment case	Certification rule
Fixed positive gross cash 
𝐹
0
F
0
	​

	Convert consumption bounds directly: 
[
𝑈
𝐿
/
𝐹
0
,
 
𝑈
𝑈
/
𝐹
0
]
[U
L
	​

/F
0
	​

, U
U
	​

/F
0
	​

].
Public deterministic payment function 
𝐹
=
𝑓
(
𝑈
)
F=f(U)	Bound 
𝑈
/
𝑓
(
𝑈
)
U/f(U) over the certified domain containing 
𝑈
∗
U
∗
; do not assume monotonicity without establishing it.
Schedule- or funding-dependent payment	Certify the consumption optimum and minimum-cash tie-break, or derive conservative joint bounds covering all admissible optimal solutions.
Insufficient public payment evidence	Keep the observed multiple for permitted display; target-workload 
𝑀
𝑊
M
W
	​

 remains unidentified.

Add these machine-readable fields:

capacity_optimum_bounds

cash_at_capacity_optimum_bounds

multiple_target

multiple_bounds_derivation

payment_monotonicity_certificate

lexicographic_optimality_status

Add a regression fixture using the 
𝑈
=
10
,
𝐹
=
1
U=10,F=1 versus 
𝑈
=
20
,
𝐹
=
10
U=20,F=10 example. The first schedule must never certify 
𝑀
𝑊
≥
10
M
W
	​

≥10 when the scored target is 2.

This recommendation requires no new private data. Where public evidence cannot support certification, it uses the draft’s existing unidentified status rather than an analyst-created allowance.
paste.txt

Priority 2: Separate Plan display admission, transport identification, and interval eligibility

Compile one executable decision table with separate outputs:

Predicate	Purpose
OfficialDisplayEligible(route)	Determines whether the route may supply a displayed Plan score under the owner’s evidence and transfer policies.
TargetTransportIdentified(route, W)	Determines whether public evidence identifies a point or strictly positive finite interval for 
𝑀
𝑊
M
W
	​

.
PlanIntervalEligible(route, W)	Requires the applicable identification, full-cost, funding, and other interval-output conditions.

A displayed score should then use the already-adopted scalar conventions:

𝑀
d
i
s
p
l
a
y
=
{
𝑀
𝑊
,
	
point-identified
,


𝐿
𝑊
,
	
set-identified
,


𝑀
o
b
s
e
r
v
e
d
 or authorised transfer
,
	
unidentified but display-eligible
.
M
display
	​

=
⎩
⎨
⎧
	​

M
W
	​

,
L
W
	​

,
M
observed
	​

 or authorised transfer,
	​

point-identified,
set-identified,
unidentified but display-eligible.
	​


The important change is not the formula—it is making the admission predicate unambiguous before the comparator runs. Existing O16 and E74 already establish the intended distinction between a displayed scalar and an identified target-workload multiple.
paste.txt

Add fixtures for:

Exact-route measured usage with unknown workload transport: displayed, interval-ineligible.

Exact-route measured usage with an unreconciled valuation basis: displayed with the specified flag, interval-ineligible.

Unsupported effort mismatch: rejected as exact-route evidence.

Owner-authorised transfer: handled only through its explicitly authorised assumption path.

Failed report comparability: not pooled into an otherwise qualifying measurement object.

Have every prose section reference this decision table rather than restating admission rules independently.

3. Questions for the owner

None. Both recommendations preserve the binding owner decisions and can be implemented as clarification and certification work.

4. Verdict

VERDICT: HAS FEEDBACK