0. Read check

Read all seven parts to their ends through the GitHub connector at commit e2f5ce5f663f990a30c1b9e930eddeb66ced8c99. The separate raw-URL fetches failed; this review uses the complete connector reads, not those fetches.

Draft’s first line:

ValueRank methodology — draft r52

Last 12 words of each part, in order:

> cost per task, not AA's 7:2:1 blended price, not total Index cost.

> unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).

> (e.g. Bug Hunt run in vendor CLIs) are disclosed as a limitation.

> not separable" and its S0 result is not described as target-workload support.

> Q. Shared dependencies are kept. Scenario frontier frequencies are a separate output.

> conditional hallucination rate h is tested against AA's published index each release.

> covers two-thirds of ranked rows jointly with the admitted components (E95, E101).

Source references below identify the relevant part and named provision. The GitHub connector returned the file contents without citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The release needs an explicit resolution rule when the applicable tariff and AA’s captured cost valuation diverge

Issue: E141 requires prices applicable at the release’s declared valuation timestamp. Meanwhile, the API numerator remains AA’s published basket cost, AA cost snapshots and price lists may be up to 45 days old, and Plan measurements must either use the release valuation basis or be revalued to it. E157 correctly explains when public demand information cannot support revaluation, but it does not explicitly resolve the release-level choice when AA’s captured cost uses an older tariff and the currently applicable tariff differs.

This is distinct from the already-adopted tariff-band and scheduled-refresh provisions: those identify tariff applicability and valuation sufficiency. The remaining gap is what the build must do when those checks expose incompatible valuation clocks.

Why it hurts the objective: a routinely refreshed release could otherwise compare a historical API basket valuation with a current-price Plan multiple, or different configurations valued at different tariff dates. The resulting change in 
𝐶
𝑊
/
𝑀
C
W
	​

/M would not necessarily represent a change in subscription economics. Reconciliation could also fail for an otherwise valid published cost record merely because the release advanced its price-list timestamp.

Concrete change: add an atomic valuation-basis gate:

Each scored cost observation must name the actual valuation basis used to produce it, not merely the date on which ValueRank retrieved it.

A release claiming a common valuation timestamp must establish that every scored observation is compatible with the tariffs applicable then, or revalue it from sufficient public exact-configuration demand evidence.

If compatibility cannot be established, retain the published observation as diagnostic evidence and explicitly choose either a compatible historical release cutoff or a held current-valuation release. Do not silently mix bases or manufacture token allocations.

Price changes must invalidate affected cost–multiple compatibility checks even when neither source artifact changes.

Source: part 3, “Tariff-aware valuation” and “Valuation compatibility”; part 7, “Freshness” and “Tariff applicability.”

Low
L1. “Best-eligible-route ranking” names an output without giving it a separate executable definition

Issue: the draft precisely defines the official evidence-priority selector and the measured-only selector, but also promises “a best-eligible-route ranking” without specifying whether “best” means the same evidence-priority selection, highest displayed multiple, highest lower-bound target multiple, or highest resulting value score.

What is new: this is not an objection to the adopted route comparator. It concerns an additional promised output whose relationship to that comparator is unspecified.

Why it hurts the objective: the official selector explicitly does not claim to select the lowest-cost route. An undefined “best” alternative could therefore be read as the economic optimum that the official ranking intentionally does not establish—especially when candidates have incomparable measurement workloads.

Concrete change: either delete the phrase as redundant with the published route-selection sensitivity, or define a hashed alternative-view object with:

Candidate admission and identification requirements.

Selection objective and tie rules.

Treatment of workload-unmatched measurements.

Anchor policy and common-panel comparison.

Wording that distinguishes displayed arithmetic from identified target-workload economics.

Source: part 2, “Plan cost input,” particularly E85/E93 and the promise of a “best-eligible-route ranking.”

2. Methodology design recommendations
Priority 1 — Make valuation compatibility an executable join, not a date annotation

Introduce a valuation object:

𝐵
=
(
configuration
,
 serving route
,
 tariff rule
,
 applicability conditions
,
 effective interval
,
 billing support
)
.
B=(configuration, serving route, tariff rule, applicability conditions, effective interval, billing support).

Every API component cost and Plan consumption valuation references such an object. Before computing

𝑃
𝑖
,
𝑊
=
𝐶
𝑖
,
𝑊
𝑀
𝑖
,
P
i,W
	​

=
M
i
	​

C
i,W
	​

	​

,

the build must establish compatibility between the numerator’s basis and the multiple’s API valuation basis.

Permit only three outcomes:

Compatible as captured.

Compatible after evidenced revaluation.

Incompatible or unresolved—no mixed-basis calculation.

For case 2, revaluation uses the billing-sufficient public representation already required by E157: category totals, tariff-stratified totals, or a request ledger, as appropriate. No new inferred demand or provider marketing numerator is needed.

Add two regression fixtures:

A tariff changes between AA’s execution/cost valuation and ValueRank’s release cutoff, while the AA payload remains unchanged.

A Plan measurement is revalued to the new tariff, but the basket cannot be revalued from public evidence.

Both must prevent an apparently current, common-basis 
𝐶
/
𝑀
C/M calculation unless compatibility is established. This completes—not replaces—the existing effective-date and valuation-sufficiency designs.

Priority 2 — Replace “best eligible” with a narrowly named alternative view

The least disruptive implementation is to remove the undefined ranking promise and publish a route-alternative table alongside the existing official and measured-only views.

For each admissible route–measurement pair, show:

Identification class and evidence grade.

Measurement workload and valuation basis.

Displayed multiple and resulting displayed value score.

Official selection tuple and exclusion/dominance reason.

Whether comparison with the selected route is identified on 
𝑊
W, or merely observed-workload arithmetic.

If a separate ranking is retained, name its objective literally—for example, “highest displayed-multiple sensitivity”—and do not call it a lowest-cost target-workload route ranking when 
𝑀
𝑊
M
W
	​

 is unidentified.

Neither recommendation changes the fixed cohort, exact-variant evidence, benchmark weights, headline cost weight, full-utilisation target, or owner-required scoring of workload-unmatched Plan rows.

3. Questions for the owner

When a tariff changes but AA has not published a compatible refreshed cost and public demand evidence cannot support revaluation, should ValueRank hold the current-valuation release or publish at an explicitly compatible historical valuation cutoff? This determines the failure action for M1.

Is “best-eligible-route ranking” intended to mean a distinct economic selector, or simply the already-defined evidence-priority selection plus sensitivity? If it is the latter, L1 needs only a wording correction.

4. Verdict

VERDICT: HAS FEEDBACK