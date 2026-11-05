1. Findings by severity
Critical

None.

High

Unknown window semantics need an upper bound across admissible semantics, not merely a conservative scheduling convention.

Issue: E30 substitutes sliding-window constraints when semantics are unknown. E39/E56 then permit capacity identification from feasible lower and relaxed upper bounds under the recorded semantics. These are not equivalent safeguards: a sliding-window model can establish a conservative achievable capacity, but an upper bound for that model need not upper-bound capacity under other plausible reset semantics. Two bursts straddling a fixed reset can be feasible even when the same bursts violate a sliding-window constraint. Consequently, matching lower and upper bounds under the substituted sliding model does not establish point identification of the actual route’s capacity.
paste.txt

Why it hurts the objective: An unresolved quota mechanism can become an apparently identified 
𝑀
𝑊
M
W
	​

, affecting route selection, Plan cost, and interval eligibility. The issue concerns identification of the target, not numerical precision.

Concrete change: Represent unknown semantics as a discrete structural uncertainty object. Compute a feasible lower bound valid for the actual unknown mechanism and an upper bound covering every publicly plausible mechanism. If that covering upper bound cannot be established, retain the conservative capacity as a diagnostic or one-sided bound and leave 
𝑀
𝑊
M
W
	​

 unidentified.

What is new relative to E30/E39/E56: Those decisions address conservative scheduling and numerical optimality bounds. This finding distinguishes optimality conditional on an assumed mechanism from identification across unresolved mechanisms.

Medium

The route–measurement comparator lacks a final measurement-object tie-break.

Issue: E111 expands candidates from routes to route–measurement pairs, but E85’s last comparison key remains route ID. Two measurement objects belonging to the same route can tie on identification class, grade, comparison multiple, gross cash and route ID. The selector is therefore not a total order over its actual candidate domain.
paste.txt

Why it hurts the objective: Tied candidates can carry different dates, identification objects, dependencies or uncertainty ranges. Choosing whichever happens to appear first can change scenarios and certificates without changing any declared comparator key.

Concrete change: Append a stable measurement-object ID as the final key, and publish the complete selected pair ID.

What is new relative to E85/E111: E111 changed the candidate domain; the existing terminal tie-break was not extended with it.

The workday diagnostic does not fully specify its fee-period calendar.

Issue: E15 specifies an eight-hour, five-day, 40-hour week, but the primary capacity problem uses a measured fee period with account-specific reset phases and billing boundaries. The draft does not explicitly define how the weekly availability pattern maps onto that same fee period: timezone, weekday selection, daily start time, partial weeks and phase relative to resets.
paste.txt

Why it hurts the objective: Different valid implementations can produce different 
𝑀
workday
/
𝑀
full
M
workday
	​

/M
full
	​

 ratios. That weakens the diagnostic intended to help buyers interpret full-utilisation economics.

Concrete change: Make the availability calendar a versioned input to the existing capacity program. Use identical fee-period boundaries, initial balances, purchase policy and quota semantics for both solves.

What is new relative to E15: The recommendation completes the calendar and horizon contract; it does not replace full-utilisation scoring or introduce monthly-demand scoring.

Low

Zero observed quality coverage has no explicit display rule.

Issue: The displayed quality equation divides by 
𝑝
𝑖
p
i
	​

, but no governing rule specifies the outcome when 
𝑝
𝑖
=
0
p
i
	​

=0. The provisional rule flags inadequate evidence but does not resolve division by zero. Exact-variant evidence restrictions and future evidence withdrawal make this a relevant registry edge case.
paste.txt

Why it hurts the objective: Implementations could diverge between a missing score, zero score, or an accidental numeric result.

Concrete change: Define 
𝑝
𝑖
=
0
p
i
	​

=0 as “quality not scoreable — no observed leaves,” with no displayed quality or value score. Keep the row in the cohort and retain any evaluable full-domain interval analysis.

What is new relative to E109: E109 validates costs, anchors and multiples; it does not cover the observed-quality denominator.

2. Methodology design recommendations
Priority 1 — Make quota semantics part of the identification set

Extend the existing primitive constraint graph rather than introducing another solver framework.

For route 
𝑟
r, record a semantics set

𝑆
𝑟
=
{
publicly admissible window/reset mechanisms
}
.
S
r
	​

={publicly admissible window/reset mechanisms}.

For evidence state 
𝑣
v and semantics 
𝑠
s, let the existing capacity program produce the consumption-optimal, minimum-cash multiple 
𝑀
𝑟
∗
(
𝑣
,
𝑠
)
M
r
∗
	​

(v,s). Certify bounds satisfying

𝐿
𝑟
≤
inf
⁡
𝑠
∈
𝑆
𝑟
,
  
𝑣
∈
𝑉
𝑟
(
𝑠
)
𝑀
𝑟
∗
(
𝑣
,
𝑠
)
,
𝑈
𝑟
≥
sup
⁡
𝑠
∈
𝑆
𝑟
,
  
𝑣
∈
𝑉
𝑟
(
𝑠
)
𝑀
𝑟
∗
(
𝑣
,
𝑠
)
.
L
r
	​

≤
s∈S
r
	​

,v∈V
r
	​

(s)
inf
	​

M
r
∗
	​

(v,s),U
r
	​

≥
s∈S
r
	​

,v∈V
r
	​

(s)
sup
	​

M
r
∗
	​

(v,s).

This preserves E105’s payment treatment: optimise consumption first, apply the minimum-cash tie-break, and then bound the resulting multiple. Do not independently combine capacity and cash extrema unless their combination is a valid conservative enclosure.
paste.txt

Implementable registry additions:

semantics_status: established / unresolved.

admissible_semantics and supporting public evidence.

lower_bound_scope and upper_bound_scope.

capacity_identified_across_semantics.

Explicit initial-balance and reset-phase domains.

Public provider documentation may establish mechanism structure under the existing rules; controlled measurements and eligible reports remain the evidence for delivered consumption. No marketing quota becomes a numerator.
paste.txt

Add two release fixtures:

Sliding and fixed-reset mechanisms are both admissible and yield different capacities: no point-identification result.

The mechanisms yield the same certified capacity because an independently established bottleneck binds: point identification is permitted.

If publicly plausible mechanisms cannot be bounded, publish “semantics unresolved; conservative achievable capacity only.” This is more informative than treating a conditional optimum as the route’s identified optimum.

Priority 2 — Complete the selector’s identity contract

Define the terminal comparison keys as

(
…
,
  
route ID
,
  
measurement-object ID
)
.
(…,route ID,measurement-object ID).

Construct the measurement-object ID from a canonical representation of route ID, partition/report IDs, measurement dates, workload, valuation basis and identification-object version.

Add a permutation-invariance fixture: shuffling the admissible-candidate file must not change the selected pair, selected uncertainty object or scenario dependencies.

This preserves the existing evidence-priority comparator. It changes neither the owner’s highest-eligible-multiple rule nor the declared preference ordering.
paste.txt

Priority 3 — Specify the workday diagnostic as a paired restriction

Define both capacity solves over the same recorded fee period 
𝑇
𝑟
T
r
	​

. Add an availability indicator 
𝐴
𝑟
(
𝑡
)
A
r
	​

(t) only to the workday solve:

𝑦
𝑡
=
0
whenever 
𝐴
𝑟
(
𝑡
)
=
0.
y
t
	​

=0whenever A
r
	​

(t)=0.

Publish:

IANA timezone and daylight-saving treatment.

Local weekdays and daily operating hours.

Exact fee-period start and end.

Treatment of partial days and weeks.

Identical initial balances, funding policy and reset-phase evidence in both solves.

The workday feasible set must be a subset of the full-utilisation feasible set. As a regression test, its maximum eligible consumption cannot exceed the full-utilisation maximum. With consumption-dependent payments, do not additionally assume that the resulting multiple ratio must be at most one: that would require a separate property of the payment function.

This makes the diagnostic reproducible without changing O3’s scored estimand.
paste.txt

Priority 4 — Finish numerical totality without changing missing-data policy

Add one explicit branch before displayed-quality calculation:

𝑝
𝑖
=
0
  
⟹
  
𝑄
ˉ
𝑖
 undefined
,
𝑉
𝑖
display
 undefined
.
p
i
	​

=0⟹
Q
ˉ
	​

i
	​

 undefined,V
i
display
	​

 undefined.

Do not assign zero, renormalise an empty set, or infer quality from another variant.

Keep display eligibility separate from interval evaluability: a configuration with no observed quality leaves can still have a full-composite expression over missing-leaf domains, subject to the existing completeness and feasibility gates.
paste.txt

These recommendations require no change to the nominal quality weights, 25% cost weight, cohort rule or exact-variant policy. The remaining work is chiefly to make assumptions and implementation boundaries executable. That focus is consistent with OECD/JRC guidance to distinguish uncertainty arising from data, normalisation, weights and aggregation rather than treating a composite ranking as assumption-free.
oecd

3. Questions for the owner

When quota-window semantics remain publicly unresolved, should a certified conservative capacity be allowed to supply the displayed multiple through the existing lower-bound convention, while the route remains unidentified and interval-ineligible? Or should it remain diagnostic-only, with the observed multiple continuing to supply the displayed score? The answer determines the display treatment, not the identification requirement.

4. Verdict

The draft is close to implementation-ready within its declared scope. The principal remaining issue is the boundary between a conservative scheduling assumption and identification of actual Plan capacity; the other findings complete deterministic selection, diagnostic reproducibility and numerical-domain handling.
paste.txt

VERDICT: HAS FEEDBACK