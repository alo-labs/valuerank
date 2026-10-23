0. Read check

First line:

ValueRank methodology — draft r59

Last 12 whitespace-separated words of each part, in order:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> analysis, not imputation). A row without a cost gets no value score.

> No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

> candidate's cost upper bound); otherwise "not established", with the omitted competitors listed.

> or definite result; every cost check reads C_W, never the Index diagnostic.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

All seven parts were read through their ends at the specified commit. References below identify the relevant part and rule directly; the connector supplied no citation identifiers.

1. Findings by severity
Critical

None.

High
H1. The scenario-supported cheapest label does not incorporate the superseded-price blocker rule

Issue: E183 correctly expands interval competitors to 
𝑈
𝑊
=
𝑅
𝑊
∪
𝐵
𝑊
U
W
	​

=R
W
	​

∪B
W
	​

, so a superseded-price row can block another row without receiving a label. However, the normative scenario-supported cheapest event still compares the candidate only with 
𝑗
∈
𝑅
𝑊
j∈R
W
	​

. E170 separately says a superseded-price row “can block but never enable another row's label.” These instructions are not reconciled for the scenario-supported label.
Source: Part 5, “Frontier” and “Cheapest above a bar”; Part 7, E170.

Why it hurts the objective: a cheaper, qualifying configuration can leave 
𝑅
𝑊
R
W
	​

 solely because its tariff changed. Its disappearance from the scenario event can then elevate another configuration above the 90% threshold, although no evidence established that the candidate became cheaper. The generic selected-cohort scope disclosure does not enforce E170’s explicit prohibition on enabling labels.

Concrete change: retain the existing scenario frequency over its declared panel, but add a deterministic blocker veto to label issuance. A candidate receives the scenario-supported label only if every 
𝑏
∈
𝐵
𝑊
b∈B
W
	​

 is structurally ruled out as a qualifying, no-dearer alternative over the blocker’s joint domain. If that cannot be established, publish the frequency but withhold the label.

What is new relative to the ledger: this does not repeat E183’s adopted interval fix. It identifies the remaining path through the separately defined scenario-supported label.

Medium
M1. The current-tariff bound omits the harmless zero-to-zero price case

Issue: E185 requires a strictly positive applied price for every category or band that can carry demand. It specifies zero-to-positive and positive-to-zero changes, but not a category that is free under both the applied tariff and the current tariff. For such a category, 
𝑟
𝑘
=
0
/
0
r
k
	​

=0/0 is undefined even though its contribution to both valuations is exactly zero.
Source: Part 7, E170 and E185.

Why it hurts the objective: a refresh implementation following the positivity condition literally can mark an otherwise valid tariff bound unavailable, making affected claims unresolved for an accounting reason rather than an evidence limitation.

Concrete change: partition tariff coordinates before constructing ratios:

Applied price positive: include the coordinate in the ratio bounds.

Applied and current prices both zero: retain its demand constraints, but omit it from the monetary ratio calculation.

Applied price zero and current price positive: require a public bound on its demand; otherwise retain E185’s unavailable status.

For Plan bounds, apply this partition to both target-demand and measured-consumption support, preserving their respective accounting constraints.

What is new relative to the ledger: E185 handles newly priced and newly free categories; this adds the distinct unchanged-free case without weakening either safeguard.

M2. Cross-basis anchor availability is asserted rather than operationally resolved

Issue: E184 states that workload migration is atomic across API and Plan, that the bases share reference configurations, and therefore that “their availability cannot differ.” But E138 permits a Plan measurement with an unrecorded valuation basis to remain displayed while never becoming interval-eligible, and E170 requires Plan measurement valuation compatibility to be assessed separately. API basket valuation eligibility therefore does not itself establish Plan valuation eligibility for the same configuration.
Source: Part 2, E138; Part 3, E160 and E184; Part 7, E170.

Why it hurts the objective: two plausible implementations can produce different reference panels:

Select references using API cost eligibility and admit their displayed Plan costs.

Require each reference to pass both API and Plan valuation checks.

The first can calibrate the Plan exchange rate using an unverified valuation basis. The second can leave fewer than two joint references even when each basis separately has enough. E184’s atomic migration policy needs an explicit rule for this case.

Concrete change: define the shared eligible reference set as an explicit intersection of basis-specific predicates, including the selected Plan evidence’s valuation status. Freeze both bases from that same intersection. If fewer than two remain, apply E184’s existing deferral or first-freeze refusal rule.

What is new relative to the ledger: this accepts E184’s atomic migration decision and supplies the missing cross-basis eligibility operation; it does not propose separate reference panels.

Low

None.

2. Methodology design recommendations
Priority 1 — Separate scenario estimation from blocker-safe label issuance

Keep the scenario event and its frequency transparent:

𝐸
𝑖
(
𝑠
)
=
1
 ⁣
[
𝑄
𝑖
(
𝑠
)
≥
𝑄
𝑟
(
𝑠
)
  
∧
  
∀
𝑗
∈
𝑅
𝑊
∖
{
𝑖
}
,
 
𝑄
𝑗
(
𝑠
)
<
𝑄
𝑟
(
𝑠
)
 
∨
 
𝐶
𝑖
(
𝑠
)
<
𝐶
𝑗
(
𝑠
)
]
.
E
i
	​

(s)=1[Q
i
	​

(s)≥Q
r
	​

(s)∧∀j∈R
W
	​

∖{i}, Q
j
	​

(s)<Q
r
	​

(s) ∨ C
i
	​

(s)<C
j
	​

(s)].

Then define, separately, the blocker-safety condition:

BlockerSafe
⁡
(
𝑖
)
  
⟺
  
∀
𝑏
∈
𝐵
𝑊
,
 
∄
𝜃
∈
Θ
:
𝑄
𝑏
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
𝐶
𝑏
(
𝜃
)
≤
𝐶
𝑖
(
𝜃
)
.
BlockerSafe(i)⟺∀b∈B
W
	​

, ∄θ∈Θ:Q
b
	​

(θ)≥Q
r
	​

(θ)∧C
b
	​

(θ)≤C
i
	​

(θ).

Issue the label only when:

The candidate meets UniqueLabelEligible.

Every registered kernel assignment passes the existing E77 threshold procedure.

BlockerSafe is certified.

This requires no invented distribution over the current-tariff hull and uses the existing deterministic solver framework. Publish “scenario frequency passes; superseded-price blocker unresolved” when the first two conditions pass but the third does not. The frequency remains informative without contradicting E170.
Basis: Part 5, E100, E112–E137 and E183; Part 6, E40/E108; Part 7, E170.

Add a regression fixture: a qualifying configuration becomes a superseded-price blocker while its published cost and quality remain unchanged. Removing it from the sampled panel must not, by itself, create a label for another row.

Priority 2 — Make tariff support preprocessing an executable accounting step

Before evaluating E170’s ratio bounds, create three coordinate sets:

𝐾
+
=
{
𝑘
:
𝑝
𝑘
o
l
d
>
0
}
,
K
+
	​

={k:p
k
old
	​

>0},
𝐾
00
=
{
𝑘
:
𝑝
𝑘
o
l
d
=
𝑝
𝑘
n
e
w
=
0
}
,
K
00
	​

={k:p
k
old
	​

=p
k
new
	​

=0},
𝐾
0
+
=
{
𝑘
:
𝑝
𝑘
o
l
d
=
0
,
 
𝑝
𝑘
n
e
w
>
0
}
.
K
0+
	​

={k:p
k
old
	​

=0, p
k
new
	​

>0}.

Coordinates publicly established to have zero relevant demand can be removed before this partition.

When 
𝐾
0
+
K
0+
	​

 is empty and the original total is positive, calculate the monetary ratio envelope using 
𝐾
+
K
+
	​

; coordinates in 
𝐾
00
K
00
	​

 contribute zero to both valuations and require no ratio. Preserve all other demand, quota and conservation constraints.

If 
𝐾
0
+
K
0+
	​

 is nonempty and demand is not publicly bounded, retain the unavailable outcome. Do not infer zero demand from zero expenditure.
Basis: Part 3, E130/E157; Part 7, E170/E185.

Add fixtures for:

An unchanged-free category with positive demand.

An unchanged-free category alongside a positive-price change.

A newly priced category with unknown demand.

A newly free category that makes the conservative Plan upper bound unbounded.

Priority 3 — Compile one shared anchor-eligibility table

For workload 
𝑊
W and freeze cutoff 
𝑉
V, publish a row-level eligibility table containing:

CompleteCostEvidence on every component of 
𝑊
W.

API valuation-gate outcome.

Selected Plan pair or API-fallback identity.

Selected Plan valuation status.

API anchor eligibility.

Plan anchor eligibility.

Shared-reference eligibility and exclusion reason.

Define:

𝑃
s
h
a
r
e
d
(
𝑊
,
𝑉
)
=
𝑃
c
o
m
p
l
e
t
e
(
𝑊
,
𝑉
)
∩
𝑃
A
P
I
 
v
a
l
u
a
t
i
o
n
(
𝑊
,
𝑉
)
∩
𝑃
P
l
a
n
 
v
a
l
u
a
t
i
o
n
(
𝑊
,
𝑉
)
.
P
shared
	​

(W,V)=P
complete
	​

(W,V)∩P
API valuation
	​

(W,V)∩P
Plan valuation
	​

(W,V).

Use the same configuration IDs in both anchor objects, valued at their respective displayed costs. Owner-authorised transfers and API fallbacks remain admissible under E160, but their applicable valuation checks must be explicit; target-workload identification is not an additional anchor requirement.

Freeze only when 
∣
𝑃
s
h
a
r
e
d
∣
≥
2
∣P
shared
	​

∣≥2. Otherwise follow E184’s existing migration outcome. This operationalises the policy without changing the owner’s ranking weights, transfer policy or exploratory Plan scoring.
Basis: Part 3, E160/E184; Part 7, E170.

3. Questions for the owner

None. These recommendations resolve executable-contract gaps without requiring a change to the stated owner decisions.

4. Verdict

The draft now carefully distinguishes displayed arithmetic, identified economics, published-record bounds and conventional scenario sensitivity. My remaining feedback concerns three narrower implementation gaps: scenario labels bypassing tariff blockers, unchanged-free tariff coordinates, and cross-basis anchor eligibility. None requires changing the fixed cohort, exact-variant evidence rules, Value Multiple numerator policy or headline weights.

VERDICT: HAS FEEDBACK