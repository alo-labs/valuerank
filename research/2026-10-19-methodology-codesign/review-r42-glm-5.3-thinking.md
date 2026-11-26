1. Findings by severity
Critical

None.

High

Transfer freshness is not explicitly inherited from the donor measurement. Issue: Owner-named transfers must identify a donor measurement, but the expiry rules do not explicitly require that donor to remain eligible. E142 even includes an “only an owner-named transfer survives” fixture without distinguishing a transfer supported by a current donor from one whose donor has expired. This leaves an implementation path where an expired measurement stops supporting its original configuration but continues affecting another configuration through a transfer.
paste.txt
 Why it hurts the objective: The Plan ranking could retain stale economic evidence after the methodology’s freshness policy has otherwise removed it. Merely refreshing the transfer record could perpetuate an obsolete multiple. Concrete change: Make transfer eligibility depend on a versioned provenance graph. A transfer must reference an immutable donor measurement ID and inherit its observation dates, valuation compatibility, capacity status and relevant expiry/change flags. Creating or editing a transfer must not restart the donor’s evidence clock. If the donor becomes diagnostic-only, the transfer becomes diagnostic-only unless a separate, currently eligible donor supports it. What is new: This does not challenge the authorised transfers or repeat the transfer-identification objection. It closes the interaction between O4/O7 and the newly explicit expiry-before-reselection procedure in E142.

Medium

The v1 scenario target profile and the general S0 instructions still prescribe different input sets. Issue: E143 says v1 S0 is reporting precision only. Elsewhere, S0 includes measurement draws, and the engine is instructed to draw published measurement intervals and supported task/run resamples. Those instructions are not interchangeable: the draft itself distinguishes reporting precision, expected-performance uncertainty and future-run variation. A source’s fitted-rating confidence interval, for example, is not automatically uncertainty about the published decimal record.
paste.txt
 Why it hurts the objective: Two implementations can produce different rank frequencies while both claiming to implement “S0.” Target-profile metadata identifies the disagreement but does not, by itself, choose which inputs belong in the stream. Concrete change: Give the scenario target profile operational precedence over the generic sampling instructions. For v1:

S0 draws only published-record rounding.

S1 adds the declared conventional identification draws.

S2 adds the declared specification changes.

Public confidence intervals and repeated-run data enter separately named streams only when their documented estimand supports those streams.

What is new: E143 adopted target profiles; this finding concerns completing their execution semantics and removing the remaining competing instructions, not introducing another uncertainty taxonomy.

Source-removal branches lack a governing quality equation. Issue: The draft requires leave-one-benchmark-out, leave-one-source-out and standing Bug Hunt-removal diagnostics. It specifies common panels, retained weight and rank-comparison rules, but does not expressly determine whether a removed leaf is deleted and the remaining weights renormalised, converted into a missing full-composite variable, or removed only from rows that originally observed it. These choices generate different results.
paste.txt
 Why it hurts the objective: A source-removal diagnostic should answer a reproducible question about dependence on that evidence. Otherwise its rank changes can reflect different missingness treatments rather than the removal itself. Concrete change: Register each deletion branch with an explicit equation and affected leaf set. For the displayed-score sensitivity, remove the nominated leaves globally and renormalise the remaining observed weights. Keep any “treat this source as unavailable evidence” full-composite analysis as a distinct branch, with its identification domains and kernels disclosed. What is new: E13/E65 already govern panels and interpretation. The missing piece is the transformation that produces the branch’s quality scores.

Low

The draft uses “no shared primitives in v1” as a fact without scoping it to a compiled stream. Issue: The kernel-check definition states that each row forms its own dependency component in v1 because rows share no primitives. Other provisions allow shared prices, donor measurements, quota pools and jointly fitted evidence. Whether any of those actually vary depends on the target profile and branch. The certification grammar already calls for dependencies to be compiled from complete decision equations.
paste.txt
 Why it hurts the objective: A stale v1 assertion could incorrectly determine kernel-switch groups or permit a separability shortcut after the evidence model changes. Concrete change: Replace the unconditional statement with a release assertion: “For this stream and decision, the compiled dependency graph has these components.” Publish its hash and fail the build when the graph differs from the registered kernel-check object. What is new: This operationalises the existing dependency rules; it does not ask for exhaustive component-wise kernel switching, which the ledger has already narrowed to registered role groups.

2. Methodology design recommendations
Priority 1 — Make freshness propagate through evidence dependencies

Represent every measured or transferred multiple as an evidence node with immutable parent IDs:

CurrentSupport
⁡
(
𝑡
)
=
TransferAuthorised
⁡
(
𝑡
)
∧
⋀
𝑚
∈
RequiredDonors
⁡
(
𝑡
)
CurrentSupport
⁡
(
𝑚
)
.
CurrentSupport(t)=TransferAuthorised(t)∧
m∈RequiredDonors(t)
⋀
	​

CurrentSupport(m).

Keep provenance eligibility separate from target identification: an authorised, current transfer can remain display-eligible while still never identifying 
𝑀
𝑊
M
W
	​

, as required by existing policy.
paste.txt

Implement with public evidence already required by the registry:

Donor measurement ID and original measurement period.

Applicable route and limit-schema IDs.

Valuation-basis compatibility.

Expiry stage and demotion date.

Transfer creation date, recorded only as an editorial event—not a new observation.

Add fixtures for a current donor, an expired donor, a donor superseded by a schema change, and replacement by a newly eligible donor. Rerun E142 after propagating these statuses.

Priority 2 — Compile scenario streams from an explicit allowlist

Use one executable stream object:

𝑇
=
(
target profile
,
layer
,
primitive IDs
,
sampling laws
,
dependency graph
,
panel
,
event
)
.
T=(target profile,layer,primitive IDs,sampling laws,dependency graph,panel,event).

A primitive enters a stream only if the stream explicitly authorises its target and sampling level. Make the published frequency label a derived field of this object, not free text.

For the declared v1 design:

Stream	Permitted varying inputs	Interpretation
S0 record precision	Rounding of published records	Reporting-precision scenario frequency
S1 record plus identification	S0 plus registered missing-evidence and transport conventions	Convention-dependent identification scenario frequency
S2 weight stress	S1 plus hierarchical weight perturbations	Specification-stress scenario frequency
Separately supported measurement stream	Source-supported parameter or repeatability evidence	Named according to the supported estimand

This resolves the conflicting S0 instructions without discarding public uncertainty evidence or changing O25’s published-record interval target.
paste.txt

Add negative tests: a fitted-rating confidence interval cannot enter record-precision S0; a run range cannot enter an expected-performance stream without a supported mapping; an analyst token-use range cannot enter S0.

Priority 3 — Define deletion branches algebraically

For a globally removed leaf set 
𝑅
R, define displayed-score deletion sensitivity as:

𝑄
ˉ
𝑖
(
−
𝑅
)
=
∑
𝑏
∈
𝑂
𝑖
∖
𝑅
𝑤
𝑏
𝑧
𝑖
𝑏
∑
𝑏
∈
𝑂
𝑖
∖
𝑅
𝑤
𝑏
.
Q
ˉ
	​

i
(−R)
	​

=
∑
b∈O
i
	​

∖R
	​

w
b
	​

∑
b∈O
i
	​

∖R
	​

w
b
	​

z
ib
	​

	​

.

If the denominator is zero, the branch is unevaluable. Apply the existing branch coverage rules and common-panel comparison contract; retain the primary cost workload, selected route and anchors unless the branch explicitly changes them.
paste.txt

Distinguish:

Evidence deletion: omit 
𝑅
R, renormalise and measure displayed-score sensitivity.

Evidence unavailability: retain the full-composite target, replace unavailable observations with their admissible domains, and report bounds or convention-dependent scenarios.

The first tests dependence on the chosen evidence mix; the second tests what can be established without that evidence. They should not share a branch name.

Priority 4 — Derive dependency and shortcut eligibility from the actual equations

Compile the primitive graph separately for each decision and stream. From that graph, derive:

Dependency components.

Role-group merges for kernel checks.

Whether row-local cost–quality separability holds.

Whether shared-reference handling is required.

Whether a registered corner reduction is applicable.

For interval decisions, include every nonconstant domain variable; for scenario streams, include the variables actually sampled. This prevents a fixed shared quantity from being confused with a sampled shared factor while preserving the existing role-group kernel policy. The draft already requires enough registry information to implement this routinely without collecting additional private data.
paste.txt

3. Questions for the owner

When a donor measurement reaches diagnostic-only status, should its authorised transfers also become diagnostic-only, or is continued use intended as a separate owner-authorised assumption? The latter would need its own explicit freshness exception rather than inheriting the measured donor’s former status.

Is v1 S0 intended to be strictly reporting precision, as E143 states, or should it also contain source-supported uncertainty about expected benchmark performance? This determines whether the general measurement-draw instructions should be narrowed or assigned to additional named streams.
paste.txt

4. Verdict

The remaining material gaps concern execution, rather than the ranking’s chosen policy: donor-expiry propagation, authoritative scenario-stream membership and exact deletion-branch semantics. These can be resolved using the existing public registry and release machinery, without changing the fixed cohort, exact-variant evidence policy, basket policy or authorised Plan assumptions.
paste.txt

VERDICT: HAS FEEDBACK