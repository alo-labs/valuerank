0. Read check

Read all seven parts to their ends through the GitHub connector at commit 442b9e5e11bd08f39e279d0d52cb08ad272aab7c.

First line:

ValueRank methodology — draft r51

Last 12 whitespace-delimited words of each part, in order:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> (e.g. Bug Hunt run in vendor CLIs) are disclosed as a limitation.

> not separable" and its S0 result is not described as target-workload support.

> i. Shared dependencies are kept. Scenario frontier frequencies are a separate output.

> conditional hallucination rate h is tested against AA's published index each release.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

Source references below identify sections and rule IDs in the seven connector-read artifacts; the connector returned no citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

Issue: the normative decision procedure retains an unconditional box-factorisation statement that its authoritative constrained-evidence definition immediately qualifies. “Interval decision procedure” first states:

Θ = per-row input boxes (independent across rows) × a box of declared shared factors

E73 then defines the authoritative set using equalities and inequalities, explicitly allowing constraints that invalidate that product representation. E89 correctly requires a proof before using separable extremes. Why it hurts the objective: this is not an unresolved mathematical design problem—the subsequent rules handle it—but it leaves two different descriptions of the executable uncertainty object in the governing section. An implementer extracting the opening definition could incorrectly admit favourable states excluded by accounting or capacity constraints. Concrete change: replace the opening equality with:

Primitive domains have a box enclosure. The admissible set Θ is the constrained subset defined by E73; a product-box representation may replace it only under a decision-specific equivalence proof.

What is new relative to the ledger: this does not request another constraint model, solver or certification mechanism. Those are already adopted. It removes a surviving contradictory statement from the normative specification.
Source: part 6, “Interval decision procedure,” E73, E89 and E108.

Issue: the uncertainty section retains a generic measurement-layer description broader than the active v1 stream contract. Its concluding layer list describes “Measurement” as including published intervals and task- or run-clustered resampling. Elsewhere, E145 and E155 correctly restrict S0 to reporting precision and require separately named streams for other targets; E165 correctly limits the interpretation of S1M. Why it hurts the objective: readers can reasonably mistake the general layer summary for the uncertainty actually quantified beside the ranking. That matters because most benchmark repeatability remains unquantified in v1. Concrete change: distinguish the general taxonomy from active implementation in the layer summary itself:

Measurement taxonomy: reporting precision, source-supported estimation uncertainty and repeatability are distinct targets. Active v1 streams quantify reporting precision in S0 and conventional Terminal-Bench CI-range sensitivity in S1M; other estimation uncertainty and repeatability are not quantified.

What is new relative to the ledger: no additional uncertainty stream or stronger interpretation is proposed. The change makes the surviving summary agree with the adopted allowlists rather than relying on readers to reconcile them.
Sources: part 4, “Uncertainty,” its concluding “Layers” list and E145/E165; part 5, E155.

2. Methodology design recommendations

Prioritise a normative-text consistency pass, not another methodological expansion. Implement the two corrections above. Then enforce a simple documentation rule: each executable concept has one governing definition; explanatory summaries link to it and state their scope. In particular:

Θ always denotes the constrained admissible set, not its box enclosure.

Stream names describe only targets admitted by their active profiles.

“Measured,” “capacity established,” “target-workload identified” and “valuation compatible” remain separate statuses.

Plan amounts always retain the measurement, cash and capacity-solution lineage required by E168.

The draft already contains the substantive designs needed for these distinctions. The priority is preventing compressed summaries from undoing them. Sources: parts 3–7, E106, E138–E139, E145, E155 and E168.

Keep the current mathematical design unchanged on the evidence reviewed. I found no new material argument for changing the 25/75 score, quality weights, normalisation, basket-admission algorithm, exact-variant rules, missing-evidence domains or Plan identification requirements. In particular, r51’s amount-lineage contract appropriately distinguishes:

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


from target capacity obtained by projecting the joint capacity solution. It also avoids manufacturing target-capacity bounds by multiplying separately projected cash and multiple endpoints. That resolves the relevant amount-publication issue without changing owner-required Plan scoring. Source: part 7, “Governance,” E168. Adding further kernels, quota models or benchmark substitutions without newly available public evidence would not improve the objective enough to justify additional complexity.

3. Questions for the owner

None.

4. Verdict

The draft is methodologically sound within its expressly limited claim scope. My remaining feedback is confined to two low-severity consistency edits; neither requires reopening an owner decision or adding a new methodological mechanism.

VERDICT: HAS FEEDBACK