1. Findings by severity
Critical

None.

High

Anchor freezing is specified more completely than anchor-panel selection. Issue: E20 defines the anchor arithmetic and requires frozen reference IDs and costs, but the draft does not unambiguously identify the initial reference population for each basis and workload. The admission reference panel is explicitly constructed by E140, while the scoring sections refer more generally to “reference configurations evidenced on” a workload. It remains unclear whether API anchors must use that admission panel, whether Plan anchors use the same IDs or a separate display-eligible panel, and how subset-workload reference populations are selected. These choices matter because the Plan table can contain measured routes, authorised transfers and API-cost fallbacks.
paste.txt
 Why it hurts the objective: The reference population determines the log-cost span and therefore the quality gain needed to offset a cost doubling. Two implementations can use identical observations, weights and freezing arithmetic yet produce different value scores and rankings by choosing different reference populations. Publishing the selected IDs makes an implementation reproducible after the choice; it does not make the selection rule deterministic. Concrete change: Add a versioned anchor-panel policy specifying population construction, eligibility, selection cutoff, minimum population, treatment of Plan fallbacks and assumptions, and re-freeze conditions. Explicitly distinguish the workload-admission panel from the anchor panel—even if the policy deliberately makes them identical. What is new relative to E20/E86/E95/E140: This is not another request to freeze anchors, disclose their exchange rate or enumerate workload admission. It concerns the upstream rule selecting which observations establish each scoring scale.

Medium

Scenario frontier events need an explicit quality-equation contract, especially for S0. Issue: The deterministic frontier uses full-composite quality. S0 instead uses observed-only, row-renormalised quality, while S1/S2 use the full composite. The draft requests frontier scenario frequencies by stratum but does not explicitly define whether the S0 frontier event uses S0’s observed-only quality or a full-composite expression. The bar section resolves the analogous distinction for S0 qualifying-and-cheapest frequencies; the frontier section does not.
paste.txt
 Why it hurts the objective: With unequal coverage, an observed-only frontier and a full-composite frontier answer different questions. An S0-to-S1 frequency change could reflect both a changed quality equation and added missing-evidence variation—not merely an additional uncertainty layer. Generic “scenario frontier frequency” wording would conceal that distinction. Concrete change: Define the frontier event separately for each stream and require its event manifest to record the quality equation. Label S0 results “observed-only score frontier frequency,” and S1 results “full-composite frontier frequency under conventional missing-evidence draws.” Do not describe their difference as an uncertainty-only change. What is new relative to E96/E100/E143/E155: Those decisions establish panels, signatures, target profiles and uncertainty descriptions. This recommendation supplies the missing stream-specific frontier event definition and extends the explicit S0/full-composite distinction already implemented for bar events.

Low

None.

2. Methodology design recommendations
Priority 1 — Make anchor-panel construction executable

Introduce an anchor-policy object:

text
anchor_policy_id
basis
workload_hash
selection_cutoff
source_population_rule
eligibility_predicate
minimum_reference_count
fallback_and_assumption_policy
reference_cost_convention
refreeze_trigger

A concrete default consistent with the existing policies would be:

API main workload: use the frozen workload-admission panel, subject to positive, finite scoreable costs at anchor creation.

API subset workload: use all selected-cohort configurations with complete, positive, finite costs on that exact subset at the anchor-creation cutoff.

Plan workload: use an explicitly declared display-eligible population on that workload. State whether authorised transfers and API fallbacks enter calibration; do not leave this to implementation discretion.

If fewer than two eligible references remain: report the anchor as unavailable rather than selecting a replacement population implicitly.

After creation: retain the existing frozen costs and IDs. Any change to the population or its eligibility rule creates a new anchor version and an old/new bridge.

The current arithmetic can remain unchanged:

𝑐
𝐿
=
min
⁡
𝑖
∈
𝑃
𝐴
𝑐
𝑖
2
,
𝑐
𝐻
=
2
max
⁡
𝑖
∈
𝑃
𝐴
𝑐
𝑖
,
c
L
	​

=
2
min
i∈P
A
	​

	​

c
i
	​

	​

,c
H
	​

=2
i∈P
A
	​

max
	​

c
i
	​

,

where 
𝑃
𝐴
P
A
	​

 is the deterministically selected anchor panel. This preserves E20 rather than introducing a new normalisation.
paste.txt

Add three fixtures:

Shuffling input rows leaves panel membership and anchors unchanged.

Losing reference evidence after freezing does not silently rebuild the anchor.

Switching a Plan row between a measured route, authorised transfer and API fallback follows the declared anchor policy without an implicit re-freeze.

Priority 2 — Compile scenario frontier events from explicit score targets

For each stream 
𝑠
s, define:

𝐹
𝑖
(
𝑠
)
(
𝑣
)
=
1
 ⁣
[
∄
𝑗
≠
𝑖
:
𝐶
𝑗
(
𝑣
)
≤
𝐶
𝑖
(
𝑣
)
∧
𝑄
𝑗
(
𝑠
)
(
𝑣
)
≥
𝑄
𝑖
(
𝑠
)
(
𝑣
)
 with at least one strict inequality
]
.
F
i
(s)
	​

(v)=1[∄j

=i:C
j
	​

(v)≤C
i
	​

(v)∧Q
j
(s)
	​

(v)≥Q
i
(s)
	​

(v) with at least one strict inequality].

Specify:

S0: 
𝑄
𝑖
(
0
)
=
𝑄
ˉ
𝑖
Q
i
(0)
	​

=
Q
ˉ
	​

i
	​

, the observed-only renormalised expression.

S1: 
𝑄
𝑖
(
1
)
=
𝑄
𝑖
Q
i
(1)
	​

=Q
i
	​

, the nominal-weight full composite.

S2: use the branch-declared full-composite expression and weight specification.

Continue to use fixed panels, joint primitive draws and the existing Monte Carlo procedure. Those mechanisms are already specified; the required addition is the event’s score target.
paste.txt

Every frequency artifact should carry:

text
event_definition_id
quality_equation_id
cost_workload_hash
competitor_panel_id
route_selection_version
scenario_target_profile_id
kernel_assignment_id

For comparisons:

Compare frequencies directly only when the event target and panel match.

Otherwise identify the changed target explicitly.

When useful, rerun a common-target comparison rather than attributing the whole S0/S1 difference to missing-evidence uncertainty.

A regression fixture should contain two configurations with different coverage whose observed-only quality order differs from an admissible full-composite order. The output must distinguish the corresponding frontier events.

3. Questions for the owner

Should Plan anchor calibration include API-cost fallback rows and authorised-transfer rows, or should those rows merely be scored against anchors established by a narrower reference population? This changes the specific anchor-panel policy I recommend; it does not require removing any owner-required row from the table.

4. Verdict

VERDICT: HAS FEEDBACK