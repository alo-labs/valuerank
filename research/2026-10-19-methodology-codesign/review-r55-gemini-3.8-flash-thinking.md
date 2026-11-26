0. Read check

Read all seven parts through the GitHub connector at commit 9a89e37a50f504e9cc025548826ee4a301e3ad8e, including each part’s end.

First line:

ValueRank methodology — draft r49

Last 12 words of each part, in order:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> (e.g. Bug Hunt run in vendor CLIs) are disclosed as a limitation.

> is reused for W∖TB only when its identification mechanism also covers W∖TB.

> Q. Shared dependencies are kept. Scenario frontier frequencies are a separate output.

> conditional hallucination rate h is tested against AA's published index each release.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

Source references below identify parts, section names and rule IDs from those seven connector reads; the connector did not supply citation IDs.

1. Findings by severity
Critical

None.

High

None.

Medium

The required Plan fit disclosure can mislabel observed consumption as full-utilisation capacity. Issue: Governance requires every Plan row to publish “full-utilisation capacity M × F in API-priced USD so light users can judge fit.” But E139 explicitly admits measurements for which capacity was not established, and E106 permits displayed multiples based on observed workloads or owner-authorised transfers. Consequently, multiplying the displayed multiple by its denominator does not universally produce an evidenced capacity. There is also a denominator ambiguity: Governance calls F the “fee”, while the governing multiple uses gross cash, including any additional cash required for the measured consumption. Using subscription cash alone would fail to reconstruct the numerator when additional cash was paid. Why it hurts the objective: This is the disclosure intended to help a buyer interpret the full-utilisation ranking. Calling an observed-usage figure “capacity” can make an exploratory Plan score appear supported by a measured ceiling, particularly for the light users this disclosure addresses. Concrete change: Generate the amount’s name and interpretation from the selected measurement object:

Capacity established on the measurement workload: “Measured-workload capacity, API-priced USD per recorded fee period.”

Delivered consumption observed, capacity not established: “Observed eligible consumption, API-priced USD per recorded fee period; capacity not established.”

Owner-authorised transfer: “Assumed API-equivalent consumption,” identifying the donor and transfer.

API fallback: no Plan-consumption amount.

Identified target-workload capacity: publish that separately, explicitly bound to W.

Define the reconstructing denominator as F_gross, not an unqualified F. What is new relative to the ledger: E139 already adopts the capacity-status distinction. This finding concerns its incomplete propagation into a mandatory downstream disclosure, not a request to revisit O11 or stop scoring observed-usage multiples. Source: Part 2, “Measurement capacity status (E139)” and “Quota schema”; Part 3, “Plan admission decision table (E106)”; Part 7, Governance.

Low

The transfers-off scenario branch needs a fully explicit scalar-score transition. Issue: The draft defines the S2 core branch as “transfers off”, freezes the selected route for primary scenarios, and explicitly prohibits silently replacing a transfer with API cost in interval outputs. It also supplies a measured-only view that reruns selection. However, the corresponding transition for scalar Plan scores in the transfers-off scenario branch is not stated equally explicitly: does a transfer-dependent row become unevaluable, or does the branch rerun the selector over non-transfer candidates? Why it hurts the objective: These are different sensitivity questions. One tests dependence on the selected evidence; the other tests the best available non-transfer evidence. They can produce different panels, costs and rank changes even when both obey the common-panel rules. Concrete change: Define the standing transfers-off branch as selected-evidence removal: keep the primary selected pair fixed; if it depends on a transfer, mark that row unevaluable, with no replacement. Use the already-defined measured-only view for non-transfer reselection. Publish distinct branch IDs and exclusion reasons. What is new relative to the ledger: This does not repeat the adopted no-fallback rule for interval outputs or the measured-only view. It closes the remaining operational ambiguity between those contracts and scalar scenario-rank sensitivity. Source: Part 4, Uncertainty and “Rank events (E96)”; Part 5, “Joint admissible set Θ”; Part 3, “Measured-only Plan view (E113)”.

2. Methodology design recommendations
Priority 1 — Type every displayed Plan amount by what it actually measures

Retain the existing ranking policies, weights, routes and evidence admission. Add a small output contract that prevents a displayed multiple from acquiring a stronger interpretation downstream.

For selected measurement object 
𝑚
m, define:

𝑈
d
i
s
p
l
a
y
,
𝑚
=
𝑀
d
i
s
p
l
a
y
,
𝑚
 
𝐹
g
r
o
s
s
,
𝑚
.
U
display,m
	​

=M
display,m
	​

F
gross,m
	​

.

This is a reconstruction of the selected displayed multiple’s numerator or scoring convention—not automatically a capacity estimate.

Require the output record to contain:

Field	Required meaning
amount_kind	Observed consumption / established measured-workload capacity / identified target-workload capacity / transferred assumption
workload_id	Measurement workload or target W, as applicable
fee_period	Exact recorded period
subscription_cash	Subscription payment for that period
additional_cash	Other payment included in the multiple’s denominator
gross_cash	Sum of the two, reconciled to the measurement
capacity_status	Existing E139 status
valuation_status	Existing E138 status
interpretation_label	Generated from those fields, not independently authored

For an identified target-workload multiple under fixed positive gross cash:

𝑈
𝑊
∈
[
𝐿
𝑊
𝐹
g
r
o
s
s
,
𝑈
𝑊
𝑀
𝐹
g
r
o
s
s
]
,
U
W
	​

∈[L
W
	​

F
gross
	​

,U
W
M
	​

F
gross
	​

],

where 
𝑈
𝑊
𝑀
U
W
M
	​

 denotes the multiple’s upper bound, avoiding reuse of the same symbol for consumption and multiple. For consumption-dependent payments, retain E105’s joint optimum-and-payment treatment rather than multiplying unrelated marginal endpoints.

Add fixtures covering additional cash, unsaturated reports, transfers and API fallbacks. This requires no new public evidence: it uses information the methodology already requires.

Source basis: Parts 2–3, E105, E138, E139 and E106; Part 7, Governance.

Priority 2 — Separate transfer removal from route reselection in the branch registry

Register two different operations:

selected-transfer-removal

Freeze the primary selected measurement pair.

Remove support supplied by owner-authorised transfers.

Mark affected rows unevaluable.

Do not select another route or introduce API fallback.

Calculate baseline-versus-branch rank changes only on the common surviving panel.

measured-route-reselection

Use E113’s measured-only candidate set and selector.

Retain the official anchors for its primary comparison.

Keep E164’s measured-evidence calibration as the separate calibration diagnostic already specified.

This makes the distinction visible:

Removal asks, “How dependent is this published result on its selected assumption?”

Reselection asks, “What result can the remaining measured evidence support?”

Neither operation changes the owner’s official ranking policy. Both are routinely refreshable from the existing admissible-route file.

Source basis: Part 3, E113 and E164; Part 4, E96; Part 6, E65.

I recommend no changes to the headline weights, cohort policy, exact-variant requirements, basket admission, Omniscience transform or published-record interval target. The two changes above are output-contract and executable-branch clarifications, not alternative ranking methodologies.

3. Questions for the owner

None.

4. Verdict

The draft is substantially sound against its explicitly bounded objective. Its separation of published-record intervals, conventional scenario sensitivity, target-workload identification and observed Plan consumption is particularly important. The remaining feedback concerns ensuring that downstream displays and branch operations preserve those distinctions.

VERDICT: HAS FEEDBACK