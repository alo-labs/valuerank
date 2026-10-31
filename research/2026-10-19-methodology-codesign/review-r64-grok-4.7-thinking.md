0. Read check

Read all seven parts, in order, through the GitHub connector at commit 53a0319b9a99c1e838612963c199f3b21a2878f2, including each part’s end.

Draft’s first line:

ValueRank methodology — draft r58

Last 12 words of each part, counting whitespace-separated words:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> a bias bound in the identification layer); repetitions are not a bias.

> one multiple, price update or benchmark version affects all its rows jointly).

> candidate's cost upper bound); otherwise "not established", with the omitted competitors listed.

> or definite result; every cost check reads C_W, never the Index diagnostic.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

Source locators below identify the part and governing rule; the connector returned file contents without citation IDs.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The current-tariff bound needs an explicit zero-price and newly priced-category branch

Issue. E170 defines category/band ratios 
𝑟
=
𝑝
c
u
r
r
e
n
t
/
𝑝
a
p
p
l
i
e
d
r=p
current
	​

/p
applied
	​

, followed by:

𝐶
′
∈
[
𝐶
min
⁡
𝑟
,
  
𝐶
max
⁡
𝑟
]
C
′
∈[Cminr,Cmaxr]

and

𝑃
′
∈
[
𝑃
min
⁡
𝑟
max
⁡
𝑟
,
𝑃
max
⁡
𝑟
min
⁡
𝑟
]
.
P
′
∈[P
maxr
minr
	​

,P
minr
maxr
	​

].

The numerical-domain rules require positive aggregate workload costs and multiples, but do not require every category’s old and current price to be strictly positive. Consequently:

A category with positive consumption and zero applied price makes its ratio undefined.

A current zero price can make 
min
⁡
𝑟
=
0
minr=0, making the Plan upper-bound expression undefined.

A previously free category becoming chargeable cannot be bounded by multiplying the old aggregate cost by finite price ratios.

The stated weighted-mean justification therefore needs a positivity condition on the relevant applied prices. This is a boundary of the E170 formulas, not a challenge to O29.
Source: part 7, E170; part 3, E109.

Why it hurts the objective. E183 uses these bounds to prevent superseded-price rows from improperly enabling another row’s interval label. An undefined ratio must not silently remove such a blocker or produce an apparently finite bound. That would undermine the published-record protection specifically added in r57.
Source: part 5, E183.

Concrete change. Add a tariff-bound dispatcher:

Use the ratio formulas only when their denominators are strictly positive and all ratios required by the formula are defined.

Otherwise optimize the current valuation over the public demand/consumption constraints already registered under E124/E157.

If those constraints do not establish a finite enclosing bound, publish the bound as unavailable or one-sided and mark affected blocker-dependent decisions unresolved, as E183 already requires.

Route an exactly repriced aggregate zero cost through E109’s existing “cost not scoreable (zero)” state.

What is new. E157 already handles tariff sufficiency, and E183 already handles an unconstructible blocker domain. The missing connection is an explicit domain check and dispatch from E170’s ratio formulas to those existing mechanisms.

Low
L1. E184 does not specify the bootstrap case or the cross-basis consequence of anchor unavailability

Issue. E184 says that a main-workload migration with insufficient valuation-eligible references is deferred and that publication continues on the current workload and anchor version. That recovery path presupposes an existing version. It does not explicitly define:

Initial publication when no prior anchor exists.

Whether an unavailable Plan freeze defers an otherwise available API workload migration, or only the Plan output.

The draft says availability is reported per basis, while W is also a versioned workload object used across the methodology. A builder should not have to infer the intended transition.
Source: part 3, E160/E184 and the workload/anchor definitions; part 1, workload object W.

Why it hurts the objective. This is unlikely to change today’s reported data, but it leaves a release-state ambiguity precisely when evidence becomes thin. Two implementations could make different publication decisions from the same bundle.

Concrete change. Add a short transition table covering initial freeze versus migration, separately for API and Plan. For initial publication without adequate references, report the affected ranking as unavailable rather than invoking a nonexistent previous anchor. State explicitly whether workload migration is atomic across bases.

What is new. This addresses E184’s bootstrap and cross-basis transition semantics, not its already adopted decision to preserve frozen anchors or defer an under-supported migration.

2. Methodology design recommendations
1. Make tariff-bound construction a typed operation

Retain the current score, weights, basket and O29 policy. Introduce one deterministic object for each revaluation bound:

text
valuation_bound_method:
  exact_revaluation
  positive_price_ratio_enclosure
  constrained_demand_optimization
  bound_unavailable

Record:

Applied and current tariff IDs.

Relevant categories/bands.

Positivity and ratio-definedness checks.

Demand or consumption constraint-object IDs.

Bound endpoints, including an explicit unbounded endpoint where appropriate.

Downstream blocker decisions affected.

For the constrained branch, compute:

𝐶
′
𝐿
=
inf
⁡
𝑑
∈
𝐷
𝑇
c
u
r
r
e
n
t
(
𝑑
)
,
𝐶
′
𝑈
=
sup
⁡
𝑑
∈
𝐷
𝑇
c
u
r
r
e
n
t
(
𝑑
)
,
C
′L
=
d∈D
inf
	​

T
current
	​

(d),C
′U
=
d∈D
sup
	​

T
current
	​

(d),

where 
𝐷
D is the existing public-evidence demand region and 
𝑇
T is the applicable tariff function. For Plan revaluation, preserve the joint workload-demand and measured-consumption lineage rather than independently multiplying marginal bounds.

This extends the existing E124/E157/E170 machinery; it requires no inferred token mix, transferred evidence or new nonpublic data.
Source: part 3, E124/E157; part 7, E168/E170.

Add regression fixtures for:

Zero applied category price becoming positive.

Positive category price becoming zero.

Public demand bounds sufficient to recover a finite bound.

Insufficient demand evidence, producing an unresolved blocker-dependent result.

Exactly repriced aggregate zero cost.

2. Add an explicit anchor-release state machine

Define the release state by:

(
basis
,
workload version
,
prior anchor exists
,
eligible reference count
)
.
(basis,workload version,prior anchor exists,eligible reference count).

A minimal transition table should distinguish:

Situation	Required outcome
Initial freeze; at least two eligible references	Freeze and publish
Initial freeze; fewer than two	Affected cost/value ranking unavailable; no previous-anchor fallback
Existing workload; frozen reference later fails the valuation gate	Preserve frozen anchor, as E184 already requires
Proposed migration; fewer than two eligible references	Defer according to the declared cross-basis migration policy

Publish the transition reason in the active-rules manifest and add fixtures for API-available/Plan-unavailable and the reverse. This makes E184 operational without reopening its adopted anchor policy.
Source: part 3, E184; part 7, E63.

No changes to the 25%/75% weights, exact-variant rule, cohort policy or Value Multiple evidence rules are recommended.

3. Questions for the owner

When a proposed workload migration has enough valuation-eligible API anchor references but insufficient Plan references, should both bases stay on the previous workload, or may the API basis migrate while the Plan basis remains on its explicitly labelled previous workload? This determines the cross-basis transition recommended in L1.

4. Verdict

VERDICT: HAS FEEDBACK