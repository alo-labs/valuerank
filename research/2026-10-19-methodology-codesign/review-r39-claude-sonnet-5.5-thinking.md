1. Findings by severity
Critical

None.

High
H1. The normative kernel-assignment rules still specify two different experiments

Issue: E133 distinguishes primitive dependency components from coarser kernel-switch groups and explicitly adopts role-group switching without exhaustively varying independent competitor components. However, the following E121 paragraph still says that kernels are assigned to primitive dependency blocks and that the check enumerates all 
2
𝐵
2
B
 assignments over the resulting non-empty blocks. It also retains the claim “block-exhaustive over candidate, reference and competitors.” Both passages sit inside the Normative definitions, so the general normative-precedence rule cannot resolve their disagreement.
paste.txt

Why it hurts the objective: Two conforming implementations could run different assignment sets, incur very different computational costs, and potentially issue different scenario-supported-cheapest labels. This is not a request to strengthen the adopted robustness standard; it is a remaining ambiguity about which standard actually governs.

Concrete change: Make the E133 switch-group object the sole executable definition:

Build primitive dependency components.

Map each component to exactly one kernel-switch group.

Enumerate assignments over switch groups, not dependency components.

Publish the exact assignment list and its hash.

Authorise the label only after every listed assignment passes E77.

Delete the conflicting E121 enumeration language, or rewrite it using these same objects. Use one label: “supported under all registered role-group kernel checks.”

What is new relative to the ledger: E133 already adopted the component/group distinction. The finding is that the older normative enumeration and label language remain operative alongside it, rather than having been superseded.
paste.txt

Medium
M1. The unreconciled-price-basis branch contradicts the adopted Plan admission table

Issue: The Value Multiple paragraph says that without public token receipts, 
𝑀
𝑊
M
W
	​

 is unidentified and “the displayed Plan score keeps the multiple’s original valuation basis under O16,” flagged “valuation basis differs.” E106 case 4 and E123 instead exclude a measurement whose valuation basis cannot be reconciled with the release price list from the official Plan ranking.
paste.txt

Why it hurts the objective: This can change the official candidate set, selected route, anchor construction and displayed ranking—not merely a disclosure. An implementer following the earlier paragraph could admit evidence that the governing admission table explicitly excludes.

Concrete change: Replace the offending branch with two distinct cases:

No token ledger, but the measurement already uses the release valuation basis: assess workload identification separately; an otherwise eligible workload-unmatched measurement can remain scored under O16.

Different valuation basis with no supported revaluation: diagnostic-only under E106 case 4; it cannot supply an official score or an anchor observation.

Absence of a token ledger should not itself decide price-basis compatibility. Conversely, workload-unmatched display eligibility should not override a price-basis mismatch.

What is new relative to the ledger: This does not reopen O7, O16 or E123. It identifies an unreconciled instruction left after their admission policy was adopted.
paste.txt

Low

None.

2. Methodology design recommendations
Priority 1 — Compile kernel checks from one canonical object

Use a single machine-readable event object, rather than deriving assignments independently from several prose passages:

text
kernel_check:
  event_signature
  dependency_components
  switch_groups
  component_to_switch_group
  assignment_ids
  assignment_set_hash
  required_checks
  completed_checks
  per_assignment_threshold_status
  authorisation_status

Let 
𝐺
G be the number of independently switchable groups with conventional alternatives. For the registered role-group design, enumerate

𝐴
=
{
uniform
,
arcsine
}
𝐺
,
A={uniform,arcsine}
G
,

while preserving evidenced laws for primitives without a conventional alternative. Dependencies within a component remain governed by its declared joint sampling mechanism.

Authorise the label precisely when

Eligible
⁡
(
𝑖
)
  
∧
  
⋀
𝑎
∈
𝐴
[
Completed
⁡
(
𝑎
)
∧
CP
⁡
𝑎
𝐿
≥
0.90
]
.
Eligible(i)∧
a∈A
⋀
	​

[Completed(a)∧CP
a
L
	​

≥0.90].

Here 
CP
⁡
𝑎
𝐿
CP
a
L
	​

 is the sequentially adjusted lower bound already specified by E77. This changes neither the threshold nor the adopted error calculation; it makes the assignment universe unambiguous.
paste.txt

Add one regression fixture that specifically distinguishes E133 from the obsolete reading: several independent competitor dependency components mapped to one competitor switch group. The build must enumerate group assignments without silently expanding into component-wise assignments.

Keep failure states separate:

Check not completed: label withheld.

Sequential interval still crosses 90% at the cap: threshold unresolved.

Primary specification passes but a registered alternative fails: kernel-sensitive.

Every registered specification passes: label authorised.

This also prevents the generic “otherwise … kernel-sensitive” sentence from swallowing resource-limit or unresolved-threshold cases.
paste.txt

Priority 2 — Make admission a single function consumed by every downstream stage

Implement E106 as the only source of admission predicates:

text
classify_measurement(record, release_basis):
    execution_compatibility
    source_evidence_eligibility
    freshness_status
    valuation_compatibility
    target_transport_identification
    official_display_eligibility
    interval_eligibility
    reason_codes

The route comparator, official anchor builder, measured-only view and scenario-panel builder should consume this result rather than reimplementing admission.

For valuation compatibility, distinguish:

Status	Treatment
Already on the release valuation basis	Continue to workload-identification checks
Revalued from a compatible public consumption ledger	Continue using the revalued measurement
Different basis and not revaluable	Diagnostic-only
Valuation basis unknown	Not established as official-display eligible

These are implementation consequences of the existing E106/E123 policy, not new restrictions on workload-unmatched measurements.
paste.txt

Add paired fixtures with the same measured multiple: one already valued on the release basis, the other valued on an unreconcilable older basis. They must not receive identical official-admission outcomes.

Priority 3 — Consolidate governing rules without adding another statistical layer

The next revision should replace superseded passages rather than append another exception paragraph. In particular:

One governing kernel-assignment definition.

One governing Plan admission definition.

Other sections reference those definitions and describe presentation only.

The active-rules manifest identifies the governing rule version used by each consumer.

The draft already has extensive uncertainty, scope and provenance machinery. These findings call for consolidation, not more weights, additional uncertainty distributions or further diagnostics.

I would retain O27’s cost definition unchanged: AA’s public methodology explicitly describes cost and token metrics as pooled per-task-attempt averages, consistent with the draft’s chosen accounting convention. That source does not, by itself, justify inventing a repeatability distribution or replacing the owner’s published-record completeness rule.
artificialanalysis

3. Questions for the owner

None. Both material findings can be resolved by consistently implementing decisions already recorded as adopted.

4. Verdict

VERDICT: HAS FEEDBACK