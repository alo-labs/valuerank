0. Read check

Part 12 (research/2026-10-19-methodology-codesign/perplexity/parts-r151/draft-r151-part-12-of-13.md):
First line: ## Governance
Last 12 words: donor's stage, and a report partition takes its most advanced contributor's stage.

Part 13 (research/2026-10-19-methodology-codesign/perplexity/parts-r151/draft-r151-part-13-of-13.md):
First line: | Stage | Trigger | Official Plan score | Route comparison | Interval eligibility | Published label |
Last 12 words: normative); it is in draft-r151.md in the same folder of the repository.

Both parts were read completely to their ends via the GitHub connector.

1. Findings by severity
Critical

None

High

Issue: In the Part 13 lifecycle table, the "Expired, in grace" row sets interval eligibility to unchanged.
Impact: When a route reaches 91–120 days old without an explicit limit or price change trigger, inheriting the Current interval eligibility allows an officially expired measurement to earn confirmed certification labels (such as confirmed cheapest-above-bar). This compromises certification integrity by validating frontier claims on obsolete telemetry.
Recommendation: Update the "Expired, in grace" interval eligibility cell in Part 13 to state explicitly that the route is label-denied and competes only as a blocker under E228 during its 30-day grace period.

Medium

Issue: Acknowledged accounting-fault measurements retain active interval eligibility without label denial. Part 13 notes that a measurement in an acknowledged accounting-fault window keeps its stage, score, and comparison, flagged only by text until replaced under O93.
Impact: If a controlled measurement was captured within 30 days of the release cutoff but falls inside a provider-acknowledged metering fault window, it retains Current status and can receive confirmed value labels despite acknowledged data distortion.
Recommendation: Clarify in Part 13 that while point scores and official comparator choices persist pending replacement, routes flagged with an acknowledged accounting fault are label-denied and compete strictly as blockers in interval outputs.

Issue: Syntactic ambiguity in cutoff-day row timestamp bounding. Part 12 defines the upper bound for ages displayed as "N hours ago" as "read instant minus N − ½ hours".
Impact: Without explicit grouping parentheses, automated verification and lint parsers could evaluate the expression as 
(
𝑡
read
−
𝑁
)
−
0.5
=
𝑡
read
−
(
𝑁
+
0.5
)
(t
read
	​

−N)−0.5=t
read
	​

−(N+0.5) rather than the intended upper bound 
𝑡
read
−
(
𝑁
−
0.5
)
t
read
	​

−(N−0.5), introducing edge-case timestamp rejections on cutoff day.
Recommendation: Rewrite the text in Part 12 as 
𝑡
read
−
(
𝑁
−
0.5
)
 hours
t
read
	​

−(N−0.5) hours.

Low

Issue: Structural enum asymmetry between amount_kind and amount_target in Part 12. amount_kind defines six categories (including O88 same-model routes), whereas amount_target defines only five closed targets.
Impact: While O90 establishes that O88 routes represent measured evidence, the missing explicit mapping in the lineage specification risks validator failures in automated JSON schema checks.
Recommendation: Add an explicit sentence in Part 12 stating that O88 and O90 same-model routes set amount_target to measured-workload consumption.

Issue: Vestigial 45-day snapshot freshness threshold under O65. Part 12 retains the rule that the Model-Page snapshot must be at most 45 days old at the cutoff, while noting that O65 defines the cutoff at the snapshot instant.
Impact: Stating a 45-day limit alongside an identity where snapshot age is zero by definition creates confusion for external auditors regarding which freshness rule actively binds.
Recommendation: Clarify in Part 12 that the 45-day snapshot age rule is satisfied identically under O65, serving as a fallback constraint if the valuation cutoff is ever decoupled from the snapshot timestamp.

2. Methodology design recommendations

Formalize label denial across all degraded Plan evidence stages.
Standardize the interval eligibility column in Part 13 so that any route carrying a validity impairment (detected limit or price change, acknowledged accounting-fault window, or expiration past 90 days) is marked label-denied. These routes should remain capable of acting as blockers to protect published records under O25, but should never be granted confirmed frontier or cheapest-above-bar certifications.

Define Plan-specific replay steps for swing attribution.
Clarify in Part 12 whether E177 swing attribution thresholds apply to Plan value scores in addition to API scores. Because plan expirations past grace trigger abrupt transitions to API-cost fallbacks that can swing a plan score by more than 5 points, explicitly register route eligibility demotions and comparator selections as named steps in the declared bridge sequence to prevent false-positive release holds under O12.

Normalize independent check weighting to reflect ranking design.
In Part 12, independent-source check (a) currently evaluates 
𝑄
ind
Q
ind
	​

 as an unweighted mean of independent leaves. Calculating 
𝑄
ind
Q
ind
	​

 with the independent leaves re-weighted proportionally to their ranking weights (e.g., LiveBench Overall at 15 versus Vals Vibe Code at 5 in max-effort) alongside the unweighted diagnostic would prevent artificial rank divergence caused strictly by weighting differences rather than evidence disagreement.

3. Questions for the owner

Under O13 and E228, is a route in the 30-day grace period (91–120 days old) intended to remain eligible for confirmed interval labels if no provider change was detected, or should all expired routes be restricted to blocker-only status?

4. Verdict

VERDICT: HAS FEEDBACK