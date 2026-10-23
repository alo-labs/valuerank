1. Findings by severity
Critical

None.

High

The Plan admission rules do not clearly distinguish measured consumption from demonstrated full-utilisation capacity on the measurement workload. Issue: The controlled-measurement path expressly requires saturation, but the end-user-report path requires independence, comparability and concordance without an equally explicit saturation prerequisite. The registry records whether capacity was exhausted, but the admission table does not specify what happens when it was not. Consequently, two comparable, concordant reports of unsaturated usage can apparently supply an official multiple that the surrounding methodology describes as full-utilisation economics.
paste.txt
 Why it hurts the objective: Agreement between two usage observations does not establish that either observation measured capacity. This problem arises before transport to the SDLC basket: even the capacity of the original measurement workload remains unestablished. The draft already addresses unidentified target-workload transport; the new argument is that measurement-workload saturation needs its own status rather than being absorbed into transport uncertainty. Concrete change: Add a mandatory measurement_capacity_status field, distinguishing:

capacity established under the recorded constraints;

eligible delivered consumption observed, capacity not established;

saturation status unverified.

Keep otherwise eligible observations scored under O16, but describe the latter two as “observed-usage multiple; full utilisation not established.” Concordance must not upgrade these statuses. Where justified, treat observed consumption as an attainable-consumption bound—not automatically as a bound on the multiple at the consumption-optimal solution, because E105 already establishes that consumption-dependent cash payments can invalidate that inference.
paste.txt

Medium

The greedy component-admission algorithm can exclude a larger jointly supportable basket. Issue: E95 admits components in descending marginal coverage, retaining each earlier choice permanently. This is reproducible, but it need not identify the largest jointly feasible subset of the target basket.
paste.txt
 For example, with six configurations and a four-configuration admission threshold:
Component	Complete-evidence configurations
A	1, 2, 3, 4, 5
B	1, 2, 3, 6
C	1, 2, 3, 6
The greedy rule admits A and rejects B and C because each intersection with A contains only three configurations. Yet B and C together support a four-configuration panel. Why it hurts the objective: The active basket can omit more of the intended SDLC coverage than public evidence requires. This is not a request to repeat the already-adopted joint-coverage safeguard; the new issue is the optimality of the selection procedure after that safeguard is applied. Concrete change: At workload creation or migration, enumerate feasible component subsets and apply a predeclared selection objective. Keep membership frozen between migrations. This does not affect the current admission outcome: the draft reports FrontierCode and ITBench-AA below the individual two-thirds threshold already.
paste.txt

Low

None.

2. Methodology design recommendations
Priority 1 — Separate measurement capacity from workload transport

Extend each measurement object with:

text
measurement_capacity_status
saturation_evidence_ids
measurement_workload_id
binding_constraint_evidence
fee_period_coverage
initial_and_terminal_balance_evidence
attainable_consumption_bound
capacity_multiple_identification_status

Use two distinct questions:

Did the measurement establish capacity on its own workload?

Does public evidence identify capacity on the scored workload W?

A route can fail either question independently. Publish both statuses beside its multiple.

Implement the following reporting rules:

Evidence	Published interpretation
Controlled or report-based evidence establishes capacity on the measurement workload	“Measurement-workload capacity established”
Eligible consumption observed without capacity certification	“Observed usage; full utilisation not established”
Capacity established, but transport to W unidentified	“Measurement-workload capacity established; target workload unmatched”
Capacity and transport both identified	Publish the identified 
𝑀
𝑊
M
W
	​

, retaining point/set identification

For fixed positive gross cash, verified attainable consumption 
𝑈
a
t
t
U
att
	​

 supports 
𝑈
∗
≥
𝑈
a
t
t
U
∗
≥U
att
	​

, and therefore a lower bound 
𝑀
∗
≥
𝑈
a
t
t
/
𝐹
0
M
∗
≥U
att
	​

/F
0
	​

. For consumption-dependent payments, use E105’s joint optimisation requirements instead; do not promote 
𝑈
a
t
t
/
𝐹
a
t
t
U
att
	​

/F
att
	​

 to a capacity-multiple bound. This extends the draft’s existing payment certification rather than replacing it.
paste.txt

These fields require no provider marketing quota as a numerator. They classify what receipts, delivered-consumption evidence and public measurements actually establish.

Priority 2 — Optimise basket admission explicitly

For candidate component set 
𝐸
E, complete-evidence matrix 
𝐾
K, cohort size 
𝑁
N, and threshold 
𝑘
=
⌈
2
𝑁
/
3
⌉
k=⌈2N/3⌉, define:

𝑃
(
𝑆
)
=
{
𝑖
:
𝐾
𝑖
𝑒
=
1
 for every 
𝑒
∈
𝑆
}
.
P(S)={i:K
ie
	​

=1 for every e∈S}.

Choose only subsets satisfying:

∣
𝑃
(
𝑆
)
∣
≥
𝑘
.
∣P(S)∣≥k.

A practical default is the following lexicographic objective:

maximise the number of admitted target components;

maximise complete-panel size;

break remaining ties by the published target-component order.

With ten target components, exhaustive enumeration requires only 
2
10
=
1,024
2
10
=1,024 subsets. Publish the selected subset, panel, objective tuple and rejected alternatives. No imputation or relaxation of exact-variant evidence is required.

Component count is appropriate only if the owner regards the ten listed components as the admission units of equal priority. If not, replace the first objective with predeclared component priorities or workflow-coverage priorities—not weights chosen after examining rankings.

This change leaves O15’s cost definition intact: costs remain sums of the admitted execution components, not AA’s weighted Index cost or a newly quality-weighted primary basket. AA separately documents benchmark aggregation and provider-reported token accounting, reinforcing the importance of keeping admission, cost accounting and quality aggregation distinct.
artificialanalysis

3. Questions for the owner

Should an otherwise eligible but demonstrably unsaturated end-user report remain an official scored observation under O16 with an “observed usage” label, or is evidence of measurement-workload saturation intended as an additional admission requirement? The current wording leaves that distinction unresolved.

At workload creation or migration, should admission prioritise the largest number of target components, explicitly weighted workflow coverage, or the existing preference for the highest-coverage component first? This determines the appropriate optimisation objective.

4. Verdict

VERDICT: HAS FEEDBACK