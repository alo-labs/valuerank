0. Read check

Read all seven parts to their ends through the GitHub connector at commit 6b5bd054c67595a0b36952cd6c90aa3f7603fc6d.

Draft’s first line:

ValueRank methodology — draft r50

Last 12 whitespace-delimited words of each part, preserving their wording and punctuation:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> (e.g. Bug Hunt run in vendor CLIs) are disclosed as a limitation.

> not separable" and its S0 result is not described as target-workload support.

> Q. Shared dependencies are kept. Scenario frontier frequencies are a separate output.

> conditional hallucination rate h is tested against AA's published index each release.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

1. Findings by severity
Critical

None.

High
H1. E166 can label a hybrid of target-workload economics and measured-workload cash as identified capacity

Issue. E105 correctly defines the target multiple under consumption-dependent payment as

𝑀
𝑊
(
𝑣
)
=
𝑈
𝑊
∗
(
𝑣
)
𝐹
𝑊
∗
(
𝑣
)
,
M
W
	​

(v)=
F
W
∗
	​

(v)
U
W
∗
	​

(v)
	​

,

where 
𝐹
𝑊
∗
F
W
∗
	​

 is cash at the target workload’s consumption-optimal, minimum-cash solution. However, Governance then instructs every Plan row to publish “the cash paid” and “the selected multiple’s API-priced amount 
𝑀
×
𝐹
g
r
o
s
s
M×F
gross
	​

,” with an amount kind that can be “identified target-workload capacity.” The selected multiple can be 
𝑀
𝑊
M
W
	​

, while the cash paid belongs to the original measurement. The draft does not explicitly require those cash quantities to coincide. Its measurement and transport objects deliberately distinguish the two workloads.
Source locations: Part 2, “Multiple certification (E105)”; Part 3, “Plan admission decision table (E106)”; Part 7, Governance, E166.

Why it hurts the objective. When payments depend on consumption, multiplying a target-workload multiple by measured-workload cash need not recover either workload’s delivered consumption or capacity. The result could mislead the light users whom E166 explicitly intends to help judge subscription fit.

For example, suppose an eligible measurement records consumption of 60 and gross cash of 20. An identified target-workload solution under the declared purchase policy instead establishes 
𝑈
𝑊
∗
=
100
U
W
∗
	​

=100, 
𝐹
𝑊
∗
=
50
F
W
∗
	​

=50, and therefore 
𝑀
𝑊
=
2
M
W
	​

=2. Multiplying the displayed target multiple by the measurement’s cash produces 40—not the measured consumption of 60 and not the target capacity of 100. This is an illustrative arithmetic counterexample, not a claim about an actual plan.

Concrete change. Publish measured consumption and target capacity as separate, typed quantities. Derive target capacity from the capacity solver’s 
𝑈
𝑊
∗
U
W
∗
	​

 output, not by multiplying the displayed multiple by cash from another object. Permit the multiplication only when an explicit identity establishes that the cash belongs to the same target solution.

What is new relative to the ledger. E105 already adopts the correct joint treatment of consumption and payment. E166 already adopts amount typing. This finding concerns their interaction: correct types for the amount’s label do not prevent incompatible provenance in its operands. It does not challenge either adopted decision.

Medium

None.

Low

None.

2. Methodology design recommendations
Priority 1 — Give every published Plan amount an explicit numerator and denominator lineage

Extend E166’s amount record with:

Field	Required meaning
amount_target	Measured-workload consumption, measured-workload capacity, assumed consumption, or target-workload capacity
workload_id	The workload to which the amount belongs
measurement_object_id	The originating measurement, where applicable
capacity_solution_id	The identified target solution or bound object, where applicable
cash_object_id	The cash quantity used in the amount–multiple identity
purchase_policy_id	The policy governing that cash and consumption
derivation	Direct observation, solver projection, authorised assumption, or valid multiplication

Use the following distinct outputs:

Measurement record: 
𝑈
o
b
s
=
𝑀
o
b
s
𝐹
o
b
s
U
obs
	​

=M
obs
	​

F
obs
	​

, on its recorded valuation basis.

Point-identified target solution: publish 
𝑈
𝑊
∗
U
W
∗
	​

, 
𝐹
𝑊
∗
F
W
∗
	​

, and 
𝑀
𝑊
=
𝑈
𝑊
∗
/
𝐹
𝑊
∗
M
W
	​

=U
W
∗
	​

/F
W
∗
	​

 together.

Set-identified target solution: publish separate projections of the joint target solution set for consumption, cash, and multiple.

Owner-named transfer: retain the assumed-consumption label, with the fee and transfer convention explicitly attached; do not imply an identified target-capacity identity.

This implements E105’s existing distinction between fixed-cash and consumption-dependent-payment routes without changing the evidence rules, route selector, scoring convention, or owner-required Plan ranking.
Source locations: Part 2, E105; Part 3, E106 and E144; Part 7, E166.

Priority 2 — Do not reconstruct capacity bounds from separately projected multiple and cash bounds

For an admissible evidence state 
𝑣
v, retain the joint relationship

𝑈
𝑊
∗
(
𝑣
)
=
𝑀
𝑊
(
𝑣
)
𝐹
𝑊
∗
(
𝑣
)
.
U
W
∗
	​

(v)=M
W
	​

(v)F
W
∗
	​

(v).

Publish target-capacity bounds directly as

𝑈
𝑊
𝐿
=
inf
⁡
𝑣
∈
𝑉
𝑈
𝑊
∗
(
𝑣
)
,
𝑈
𝑊
𝑈
=
sup
⁡
𝑣
∈
𝑉
𝑈
𝑊
∗
(
𝑣
)
.
U
W
L
	​

=
v∈V
inf
	​

U
W
∗
	​

(v),U
W
U
	​

=
v∈V
sup
	​

U
W
∗
	​

(v).

The lower-bound displayed multiple 
𝐿
𝑊
L
W
	​

 is a scoring convention, not necessarily the multiple at the state attaining minimum consumption. Consequently, neither 
𝐿
𝑊
𝐹
o
b
s
L
W
	​

F
obs
	​

 nor a product of separately reported endpoints should receive an exact identified-capacity label.

Add release fixtures for:

Fixed cash: multiplication reproduces target capacity.

Consumption-dependent cash: measured cash differs from target-optimal cash; cross-object multiplication is rejected.

Set identification: capacity is obtained by projection of the original joint solution set.

Missing target cash lineage: the measured amount remains publishable, but no target-capacity amount is manufactured.

These fixtures extend the draft’s existing primitive-dependency and joint-bound contracts rather than introduce another uncertainty framework.
Source locations: Part 4, “Primitive sampling (E83)”; Part 5, “Constrained evidence model” references and Plan measurement versus transport; Part 6, E73; Part 2, E105.

3. Questions for the owner

None. This can be resolved as an implementation clarification consistent with the existing owner decisions.

4. Verdict

VERDICT: HAS FEEDBACK