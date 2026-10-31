0. Read check

Draft first line:

ValueRank methodology — draft r57

I opened all seven parts through the GitHub connector at commit cb4b8c7f97013f41cbf4f45500dc157558599248 and read each through its end.

Last 12 whitespace-delimited words of each part, in order:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> a bias bound in the identification layer); repetitions are not a bias.

> No analyst-chosen buyer profile is registered: no public source supplies alternative multiplicities.

> candidate's cost upper bound); otherwise "not established", with the omitted competitors listed.

> or definite result; every cost check reads C_W, never the Index diagnostic.

> pending until complete exact-variant cost evidence covers two-thirds of ranked rows jointly

Source locations below refer to these pinned draft parts and their named rules. The connector returned complete text but supplied no citation identifiers; I therefore identify the relevant passages explicitly rather than invent citation tokens.

1. Findings by severity
Critical

None.

High
H1. The superseded-price exemption conflicts with the minimum-anchor release requirement

Issue: E160 requires at least two eligible anchor references and says that, for the main workload, failure to meet that minimum means “freezing fails.” E170 excludes superseded-price rows from anchor derivation while also stating that the release “never holds for this reason.” Those instructions conflict when the valuation-basis gate leaves fewer than two eligible main-workload references at an anchor freeze. The draft does not specify which instruction wins or what gets published. Source: part 3, “Scoring with frozen, per-basis anchors,” E160; part 7, “Valuation-basis gate,” E170.

Why it hurts the objective: This is a publication-boundary failure, not a disagreement with keeping superseded-price rows ranked. A tariff change could make the required ranking impossible to initialise even though O29 explicitly requires publication without holding the release. Different implementations could silently retain prohibited references, withhold the release, or publish incomparable replacement scores.

Concrete change: Add a single precedence rule and publication state covering anchor insufficiency after E170:

Existing valid frozen anchors remain usable; E160 already says that later evidence loss does not rebuild them.

A new anchor freeze must never use E170 outcome-3 rows.

If fewer than two eligible references remain, the system must enter an explicitly specified state rather than improvising anchors or treating the situation as an ordinary release hold.

State whether that condition postpones only the proposed anchor migration, or permits a published release without a new headline value ranking when no prior anchor exists.

What is new relative to the ledger: This is the interaction between E160’s minimum-reference failure and E170/O29’s no-hold requirement. It does not reopen the adopted decision to exclude superseded-price rows from anchors, nor the decision to keep those rows in the ranking.

Medium

None.

Low

None.

2. Methodology design recommendations
Priority 1 — Make anchor availability an explicit publication state

Add a small state machine per basis and workload. It can be implemented entirely from the existing evidence bundle, valuation statuses and frozen anchor objects.

Let

𝐴
𝑏
,
𝑊
,
𝑉
e
l
i
g
i
b
l
e
=
{
𝑖
:
CompleteCostEvidence
⁡
(
𝑖
,
𝑊
)
∧
AnchorValuationEligible
⁡
(
𝑖
,
𝑉
)
}
.
A
b,W,V
eligible
	​

={i:CompleteCostEvidence(i,W)∧AnchorValuationEligible(i,V)}.

The second predicate must implement E170 explicitly, rather than relying on an independently maintained exclusion list.

Condition	Required behaviour
A valid frozen anchor object already governs this workload	Continue using that object. Record current reference eligibility separately; do not reconstruct its frozen costs.
A new freeze is requested and 
∣
𝐴
𝑏
,
𝑊
,
𝑉
e
l
i
g
i
b
l
e
∣
≥
2
∣A
b,W,V
eligible
	​

∣≥2	Apply the existing E160 rule: 
𝑐
𝐿
=
min
⁡
𝐶
𝑖
/
2
c
L
	​

=minC
i
	​

/2, 
𝑐
𝐻
=
2
max
⁡
𝐶
𝑖
c
H
	​

=2maxC
i
	​

.
A new freeze is requested, fewer than two references qualify, and a prior applicable anchor exists	Publish using the prior anchor; record “anchor migration unavailable—insufficient valuation-eligible references.” Apply the ordinary clip gate independently.
No applicable prior anchor exists and fewer than two references qualify	Publish the owner-approved unavailable state; never manufacture anchors, reuse anchors from another workload, or admit superseded-price references.

This preserves the adopted weights, log-cost normalization, exact-variant rules and O29 treatment. It adds no imputation and requires no new external measurement.

Source: part 3, E160’s frozen-anchor and minimum-reference rules; part 7, E170’s anchor exclusion and no-hold requirement.

Priority 2 — Add regression fixtures for the conflicting boundary

Test at least these cases:

Nineteen complete-cost rows exist, but eighteen become E170 outcome 3 before the first freeze: anchor construction must not use those eighteen.

The same transition occurs after a valid anchor has been frozen: the frozen anchor remains unchanged.

API anchors remain available but Plan anchors do not: status and publication behaviour are basis-specific.

A proposed workload migration lacks two eligible references: anchors from the old workload cannot be relabelled as anchors for the new one.

A retained anchor subsequently triggers the clip gate: the output distinguishes that independent gate failure from anchor insufficiency.

Each fixture should assert the anchor ID, eligible-reference count, publication state and reason code. That makes the resolution reproducible under the existing immutable-evidence-bundle contract.

Source: part 1, E159 and workload migration rules; part 3, E160 and the clip gate; part 7, E170.

I have no additional material design recommendations beyond resolving this boundary. In particular, I would not add another uncertainty layer, change the quality weights, or revisit the already-ledgered Plan identification limitations in this review.

3. Questions for the owner

When an initial release or necessary workload migration has fewer than two valuation-eligible anchor references, and no applicable prior anchor exists, which requirement takes precedence?

Publish the release with costs, quality and evidence statuses but no headline value-score ranking for the affected basis/workload; or

Delay that initial ranking/workload migration until two eligible references exist, while continuing any previously valid release.

This answer determines the missing publication state. Neither option requires changing O29’s treatment of individual superseded-price rows.

4. Verdict

The draft is substantially specified and respects its stated claim scope. One material consistency issue remains at the intersection of anchor availability and the superseded-price publication exemption.

VERDICT: HAS FEEDBACK