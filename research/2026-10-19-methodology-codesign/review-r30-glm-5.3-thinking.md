1. Findings by severity
Critical

None.

High

The scenario-supported-cheapest label does not specify which quality estimand can authorize it. Issue: S0 uses observed-only, renormalized quality, whereas S1/S2 use the full composite, including missing-leaf identification uncertainty. The normative definition of “scenario-supported cheapest” does not restrict the label to a named stratum or require the full-composite equation. Publishing results separately by stratum does not itself resolve that authorization ambiguity.
paste.txt
 Why it hurts the objective: An eligible, non-provisional configuration can receive a cheapest-above-bar label because missing evidence was removed from its denominator, rather than because it meets the declared full-composite quality bar. For example, consider a non-provisional configuration with 70% quality coverage, sufficient SWE coverage, and observed leaves all scoring 100. Its S0 quality is 100. If its missing leaves score zero in an admissible full-composite state, its quality is 70. Against a fully observed reference scoring 80, S0 qualification can be certain even though full-composite qualification is not confirmed. This is a constructed counterexample, not a claim about the current cohort. Concrete change: Authorize the unqualified scenario-supported-cheapest label only under a pre-registered, explicitly named full-composite stratum and branch. Publish the corresponding S0 statistic as an “observed-leaves qualifying-and-cheapest frequency,” without that label. Keep the existing provisional predicate and simultaneous-event requirement. What is new relative to the ledger: E92 aligns candidate eligibility across the two unique-cheapest labels; E96 fixes panels and ties. Neither fixes the mismatch between the S0 and full-composite qualification targets.

The admission panel is described as complete, but its construction tests exact-cost availability rather than cost completeness. Issue: E95 admits components using the intersection of rows with exact costs, calls the resulting set the “complete-row set,” and publishes “complete-on-all-components IDs.” Separately, O27/E37 allow an exact published cost to exist while the component is confirmed incomplete because AA marks missing or declined tasks. Consequently, exact-cost coverage and FullCost coverage need not coincide.
paste.txt
 Why it hurts the objective: A workload can pass the two-thirds admission rule yet have fewer than two-thirds of rows eligible for its interval outputs. More importantly, the admission object can certify “complete” rows that fail the methodology’s own completeness predicate. Concrete change: Make the distinction executable:

ExactCostAvailable(i,e): a compatible published cost exists.

CompleteCostEvidence(i,e): the existing O27/E37 predicate.

Publish both joint intersections.

Prefer constructing the admission reference panel from the second predicate. If admission is intentionally based only on exact-cost availability, retain that policy but rename the panel “exact-cost reference panel,” remove its completeness claims, and report the smaller FullCost panel separately. What is new relative to the ledger: This is not another attempt-level completeness gate or a challenge to O27. It is an interaction between E95’s new joint-panel construction and the already adopted AA-marker-based completeness rule.

Medium

Report concordance needs a comparability gate before its ratio test. Issue: E98 precisely defines numerical concordance, but O11 does not expressly require the unpooled reports to measure a common observed-workload estimand before that test. Route identity captures plan, schema, surface, model and effort, but not the measurement workload. The draft separately recognizes that workload mix, valuation basis, funding policy and saturation constraints affect the multiple.
paste.txt
 Why it hurts the objective: Two numerically similar multiples can agree accidentally while measuring materially different consumption opportunities. Conversely, reports of equivalent consumption can appear discordant because they use different API valuation prices. A geometric mean does not resolve either problem. Concrete change: Before applying max/min ≤ 1.20, require a report-comparability record covering:

Fee-period definition and gross-cash accounting.

Route and limit-schema identity.

Eligible-consumption treatment.

Valuation basis, repriced where public receipts permit.

Measurement-workload compatibility and saturation target.

Where workload differences cannot be publicly reconciled, retain separate measurement objects rather than pool them. They may still support separate workload-unmatched diagnostics under existing policy. What is new relative to the ledger: E33/E98 specify when and how to test the unpooled numbers. E32 addresses target-workload valuation compatibility. This recommendation addresses whether the reports being pooled estimate the same measurement quantity in the first place.

A component’s basket admission needs an explicit freeze/rebase rule for the matched-cost diagnostic weights. Issue: The matched-cost diagnostic freezes execution-family weights derived from quality leaves, while the quality basket, priced-leaf availability and workload membership can migrate independently. The draft versions these objects, but does not fully specify when a changed leaf-to-family mapping or newly priced family creates a new diagnostic estimand rather than merely a refreshed diagnostic value.
paste.txt
 Why it hurts the objective: A reversal warning or more-than-three-place discrepancy could appear or disappear because the diagnostic’s weighted execution mix changed, not because a configuration’s relative costs changed. The existing workload bridge does not necessarily isolate that diagnostic-composition effect. Concrete change: Give the matched-cost diagnostic its own versioned object containing the family set, leaf-to-family mapping, weights, price rule and admissible panel. On a mapping or weight change, publish an old/new diagnostic bridge on the common evidenced panel, separating cost-data changes from diagnostic-composition changes. What is new relative to the ledger: E55 establishes split invariance within an execution family; E65 establishes common comparison panels. Neither explicitly freezes or bridges changes to the diagnostic’s execution-family composition.

Low

None.

2. Methodology design recommendations

Make every decision label carry an executable target signature. This is the highest-priority change. Extend the existing claim contract rather than add another uncertainty layer:

text
decision_target = {
  quality_equation,
  cost_workload_hash,
  basis,
  reference_object_id,
  scenario_stratum,
  specification_branch,
  route_selection_version,
  candidate_panel_id,
  kernel_version
}

For the scenario-supported-cheapest label, require:

text
quality_equation = full_composite
scenario_stratum ∈ {S1, S2}
specification_branch = explicitly named

Use the existing sequential Monte Carlo rule for the selected event. Other strata remain informative diagnostics; they do not silently authorize the same label under a different quality target. Add the 70%-coverage counterexample above as a release fixture: S0 may report 100% observed-leaves qualification while the full-composite label remains unsupported. This preserves the owner’s displayed-score policy without conflating its estimand with the full-composite decision. The draft already distinguishes those equations; this recommendation closes their label-level interface.
paste.txt

Implement admission through two public Boolean matrices. For each release, construct:

𝐴
𝑖
𝑒
=
1
{
exact compatible cost available
}
,
𝐾
𝑖
𝑒
=
1
{
CompleteCostEvidence
(
𝑖
,
𝑒
)
}
.
A
ie
	​

=1{exact compatible cost available},K
ie
	​

=1{CompleteCostEvidence(i,e)}.

For admitted component set 
𝐸
𝑊
E
W
	​

, publish:

𝑃
𝐴
(
𝑊
)
=
{
𝑖
:
∏
𝑒
∈
𝐸
𝑊
𝐴
𝑖
𝑒
=
1
}
,
𝑃
𝐾
(
𝑊
)
=
{
𝑖
:
∏
𝑒
∈
𝐸
𝑊
𝐾
𝑖
𝑒
=
1
}
.
P
A
	​

(W)={i:
e∈E
W
	​

∏
	​

A
ie
	​

=1},P
K
	​

(W)={i:
e∈E
W
	​

∏
	​

K
ie
	​

=1}.

My preferred design uses 
𝑃
𝐾
P
K
	​

 for E95’s two-thirds test. If the intended admission policy uses 
𝑃
𝐴
P
A
	​

, keep it but distinguish the panels everywhere. Add an adversarial fixture in which two-thirds of configurations have published exact costs, but some have an explicit AA declined-task marker. Admission and output-eligibility records must not report the same panel as complete unless that is actually true. This uses only the public fields and markers already required by the draft; it introduces no telemetry-based eligibility requirement.
paste.txt

Separate report comparability, concordance and pooling into three operations. Use this order:

Establish a common measurement target from public evidence.

Revalue eligible usage to a common price basis where possible.

Apply the existing unpooled ratio test, then geometric pooling.

For publicly reconcilable reports, let:

𝑥
𝑘
∗
=
eligible usage valued on the common price list
gross cash for the recorded period
.
x
k
∗
	​

=
gross cash for the recorded period
eligible usage valued on the common price list
	​

.

Then retain the owner’s rule:

max
⁡
𝑘
𝑥
𝑘
∗
min
⁡
𝑘
𝑥
𝑘
∗
≤
1.20.
min
k
	​

x
k
∗
	​

max
k
	​

x
k
∗
	​

	​

≤1.20.

Do not manufacture workload adjustments when public receipts or a supported transport mechanism are unavailable. Different workload objects should remain separate unless compatibility is evidenced. Also publish the contributing report IDs and comparability failures, so the admission result can be refreshed mechanically.

Version the matched-cost diagnostic independently of the scored workload. Define a diagnostic object:

𝐷
=
(
𝐺
,
{
𝜔
𝑔
}
,
leaf-family map
,
price rule
,
panel rule
)
,
D=(G,{ω
g
	​

},leaf-family map,price rule,panel rule),

and write its output as:

𝐶
𝑖
m
a
t
c
h
,
𝐷
=
∑
𝑔
∈
𝐺
𝜔
𝑔
𝑃
𝑖
𝑔
.
C
i
match,D
	​

=
g∈G
∑
	​

ω
g
	​

P
ig
	​

.

A new cost observation under unchanged 
𝐷
D is a data refresh. A changed family set, mapping or weight vector creates a new 
𝐷
D, with a common-panel bridge before comparing reversal warnings across releases. This is consistent with the broader composite-indicator principle that normalization, weighting and sensitivity choices are part of the indicator’s construction, not merely incidental presentation details. The OECD/JRC handbook provides the relevant general framework; the specific versioning design here is my recommendation.
oecd

I would not add new benchmarks, change the 25/75 weights, loosen exact-variant evidence, or reopen the Plan identification requirements in this revision. The material remaining work is making the existing objects compose without changing their meanings.

3. Questions for the owner

Should the scenario-supported-cheapest label be authorized by one designated full-composite branch, or separately issued with a mandatory stratum-and-branch qualifier? Either is implementable; an unqualified label should not be authorized by S0.

Does the two-thirds admission threshold intentionally mean exact published-cost availability, including AA-marked incomplete executions, or complete published-record cost evidence? That determines whether E95 needs a predicate change or only a panel-name and disclosure correction.

4. Verdict

The draft is close: its remaining material weaknesses are interface problems between adopted rules, rather than missing methodological machinery. Resolve the scenario-label target and admission-panel semantics before treating the specification as implementation-ready.
paste.txt

VERDICT: HAS FEEDBACK