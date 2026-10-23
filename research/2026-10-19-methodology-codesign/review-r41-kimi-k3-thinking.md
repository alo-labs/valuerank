1. Findings by severity
Critical

None.

High

None.

Medium
M1. Price freshness is specified by observation date, but not by tariff validity

Issue: The registry records price-list dates, maximum snapshot age and change-triggered refreshes, but does not explicitly distinguish when a price was observed from when it applies. That matters for introductory discounts and already-announced tariff changes. AA currently identifies Gemini 4 Argon’s pricing as a 50% launch discount and reports materially different costs at standard pricing. This is an actual pricing condition, not merely a hypothetical stress test.
paste.txt
artificialanalysis

Why it hurts the objective: A recently captured price can nevertheless be inapplicable to the release date. A scheduled transition can also occur without a new page edit, so page-diff detection alone does not guarantee correct pricing. Conversely, treating an undated promotion as permanent can make the headline look more durable than the evidence supports.

Concrete change: Add effective-date and promotion-status fields to the price registry. Schedule refreshes at known effective boundaries, independently of page diffs. Where a discount’s end date is unknown, keep the currently applicable price in the primary ranking, flag it as promotional and publish a named standard-tariff sensitivity only when that tariff is publicly documented.

What is new relative to the ledger: This is a tariff-applicability requirement, not another proposal for the already-adopted first-party-versus-cross-provider price branch or general price sensitivity.

M2. Expiry and route selection have an unresolved ordering conflict

Issue: The methodology selects among admissible route–measurement pairs, but the expiry paragraph says that an expired route becomes diagnostic-only and “the model falls back to API cost.” It does not explicitly condition that fallback on there being no other eligible route–measurement pair. One configuration can have several such pairs under E111.
paste.txt

Why it hurts the objective: Two implementations could produce different results: one reruns the selector and chooses a surviving measured route; another immediately inserts API fallback when the previously selected route expires. The latter could create cross-estimand ordering unnecessarily.

Concrete change: State the release-time order explicitly: classify every measurement object for eligibility and expiry, discard diagnostic-only candidates from official selection, apply the dominance filter, rerun the comparator, and use API fallback only if no official-display-eligible candidate survives. Freeze the resulting selection within that release’s scenarios.

What is new relative to the ledger: E111 resolves selection among multiple measurement objects; this finding concerns the interaction between that selection and O13’s fallback trigger. It does not challenge expiry or the owner-required fallback.

M3. E58’s scenario-target separation is not yet an executable output contract

Issue: E58 requires expected-performance uncertainty to remain separate from predictive run-to-run variation, but the named strata and event signatures do not identify which target-specific simulation is being reported. The general instruction to draw leaf values from their measurement intervals could therefore produce an S0 or S1 stream combining different targets without an explicit composite interpretation.
paste.txt

Why it hurts the objective: Reporting precision, uncertainty about expected benchmark performance and variation in a future deployment run answer different questions. Merely storing a target on each primitive does not establish what a rank-frequency event means when those primitives are combined. The issue is particularly relevant because the sources include both pooled evaluation averages and leaderboard confidence intervals; those source descriptions alone do not establish one interchangeable sampling target.
tbench
+1

Concrete change: Add a scenario-target profile to every stream and output signature. Require the build to validate either a coherent shared target or an explicitly defined mixed-target construction. Unsupported combinations should produce separate target-specific outputs, bounds-only results, or an unavailable frequency—not an unqualified “measurement” frequency.

What is new relative to the ledger: The conceptual separation is already adopted in E58. The missing piece is an executable stream-level compatibility check and an output identifier that prevents implementations from collapsing that separation.

Low

None.

2. Methodology design recommendations
Priority 1 — Make route lifecycle processing a deterministic release operation

Specify one governing pipeline:

𝐴
𝑖
,
𝑡
=
{
(
𝑟
,
𝑚
)
:
OfficialDisplayEligible
⁡
(
𝑖
,
𝑟
,
𝑚
,
𝑡
)
}
.
A
i,t
	​

={(r,m):OfficialDisplayEligible(i,r,m,t)}.

Then define:

Selected
⁡
𝑖
,
𝑡
=
{
Comparator
⁡
 ⁣
(
DominanceFilter
⁡
(
𝐴
𝑖
,
𝑡
)
)
,
	
𝐴
𝑖
,
𝑡
≠
∅
,


APIFallback
⁡
𝑖
,
𝑡
,
	
𝐴
𝑖
,
𝑡
=
∅
.
Selected
i,t
	​

={
Comparator(DominanceFilter(A
i,t
	​

)),
APIFallback
i,t
	​

,
	​

A
i,t
	​


=∅,
A
i,t
	​

=∅.
	​


This preserves the existing comparator, owner-authorised transfers and expiry policy; it makes their order unambiguous.
paste.txt

Add regression fixtures:

The selected measurement expires, but another measurement of the same route remains eligible.

Every measurement of the selected route expires, but another route remains eligible.

Only an authorised transfer remains eligible.

No official candidate remains, triggering API fallback.

An older release is rebuilt using its original cutoff and reproduces its original selection.

Publish an eligibility-transition reason separately from the existing comparator-selection reason. That distinguishes “the evidence expired” from “the comparator preferred a different candidate.”

Priority 2 — Version prices as effective-dated tariff records

Extend each price observation with:

Field	Purpose
observed_at	When the source was captured
effective_from	When the tariff becomes applicable
effective_until	Publicly established end, if any
tariff_status	Standard / promotional / grandfathered
applicability_conditions	Public conditions governing eligibility
scheduled_refresh_at	Next known effective boundary
source_evidence_id	Archived public support

A primary release must select prices applicable at its declared valuation timestamp, not simply the most recently observed prices. Unknown effective boundaries should remain unknown rather than receive an analyst-assumed date.

For a documented standard tariff behind a temporary promotion, publish a named S2 branch that reprices the evidenced consumption under that tariff. Preserve the existing demand–cost reconciliation and Plan valuation-compatibility requirements; where the public consumption ledger cannot support repricing, mark that result unavailable. AA’s documented Argon promotion is a concrete case for this design.
paste.txt
artificialanalysis

Priority 3 — Add target profiles to scenario streams and decision signatures

Extend E100 with:

text
scenario_target_profile_id
target_compatibility_status
composite_target_definition

Use distinct profiles for:

Published-record reporting precision.

Expected-performance estimation, where the source evidence supports it.

Future-run prediction, where public run-level or task-level evidence supports that target.

Explicitly conventional identification scenarios.

S0/S1/S2 should continue to identify uncertainty layers; the target profile should identify what quantity the stream concerns. These are separate dimensions.

For each stream, validate that:

Every primitive has the required target and sampling-level metadata.

Each derived quantity has a declared interpretation consistent with its inputs.

Expected-performance and future-run outputs are not silently substituted for one another.

An explicitly mixed-target stream receives a descriptive label and cannot inherit a stronger interpretation from one of its inputs.

Kernel alternatives change the sampling convention, not the target being evaluated.

This implements E58 without changing the nominal weights, evidence policies or published-record interval estimand. It also avoids inventing uncertainty distributions when public evidence does not support them.
paste.txt

3. Questions for the owner

When the selected Plan measurement expires but another official-display-eligible route–measurement pair survives, should the comparator select the surviving pair before API fallback? I recommend yes. If fallback is intentionally unconditional, that should be stated as an owner decision because it changes the lifecycle recommendation.

4. Verdict

VERDICT: HAS FEEDBACK