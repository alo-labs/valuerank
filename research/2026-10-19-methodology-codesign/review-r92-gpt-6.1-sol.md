0. Read check

Read all 14 parts, in order, through the GitHub connector at commit f0435ada639013013e0a3b7da34c9433c34166b1. Every part was returned through its end.

First line:

ValueRank methodology — draft r174

Final sentence of each part, in order:

1.

Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

2.

Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

3.

Release assertion: the scored field is the basket sum, not cost per task, not AA's 7:2:1 blended price, not total Index cost.

4.

Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

5.

Fixtures: two concordant reports 41 days apart, neither admitted earlier, where the older one leaves the partition and the route is diagnostic; a model with a current controlled measurement and a lapsed report pair, where the controlled route stays and the report route is diagnostic; a transfer from a lapsed report donor, which is diagnostic.

6.

Their selected routes and multiples are printed with the Plan rows (scores.json planRows); GPT-6 Astra (max)'s selected route moved from ChatGPT Plus to a higher plan under O45.

7.

AA Intelligence Index and output speed are diagnostics, not quality.

8.

Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

9.

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

10.

The population is the non-provisional cohort rows with a displayed quality, ordered by displayed quality ascending, then configuration ID.

11.

No published claim extends to them.

12.

every cost check reads C_W, never the Index diagnostic.

13.

One AA state (E217): the model-page snapshot, the chart capture, the Coding Agent Index capture and the cost-chart capture are each at most 7 days from the snapshot, the build tests each of the last three against the release cutoff and the snapshot itself defines it (O65), and the build fails otherwise, and capture proximity alone does not show one AA revision, so the chart is also reconciled with the model pages on the fields both publish: each chart point linked to a captured page must carry that page's total Index cost (within 1%) and its displayed Index (the page's unrounded Index within half a display unit), and a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);

14.

Revision history: omitted from this review copy (not normative); it is in draft-r174.md in the same folder of the repository.

Part 12 ends with the final semicolon-delimited clause quoted above; part 13 ends mid-sentence, which continues in part 14. Neither connector response was truncated.

1. Findings by severity
Critical

None.

High

None.

Medium

The between-freeze admission rule does not distinguish evidence deterioration from cohort-denominator changes. Issue: In “Admission and persistence,” E333 says that between freezes the build stops when reconstruction failures leave a component below the two-thirds admission threshold. The same paragraph later says:

adding cohort rows never invalidates an admission.

Those rules can produce different answers in a mixed refresh. Suppose an admitted component is complete on 6 of 9 configurations. Three configurations enter without that component, and one incumbent’s reconstruction begins failing. Coverage becomes 5 of 12. Against the frozen population, the incumbent failure changes coverage to 5 of 9; against the current population, the three entrants had already reduced coverage below two-thirds before the failure. The draft does not specify which population and denominator E333 tests, or how departures interact with that test. Why it hurts the objective: Whether ValueRank publishes a refreshed ranking or holds a workload migration should not depend on an implementation’s choice of denominator or update order. This matters especially with O145’s retained rows and two independently populated rankings. Concrete change: Define a separate, frozen admission-maintenance population and threshold, or explicitly define an entrant/departure-adjusted test. Publish its member IDs and denominator separately from current coverage. State that the check is evaluated on the final release state, not sequentially as records are processed. New argument relative to the ledger: This does not challenge frozen admission, E333, or the two-thirds policy. It identifies an unspecified interaction between E333’s deterioration gate and the existing rule protecting admission against cohort growth.

Low

E333 sends unresolved costs toward subset treatment, contradicting the explicit scored-on-W contract. Issue: E333 says reconstruction failures make costs unresolved and rows “move to the subset or unevaluable treatment.” But E209 explicitly says a row remains scored on W whenever every admitted component has a published cost, whatever its status. An unresolved published component therefore does not create a subset workload. Why it hurts the objective: Applying subset scoring would change the cost sum, anchors and exchange rate, rather than merely withdrawing interval eligibility. This is a small wording defect with potentially material implementation consequences. Concrete change: Replace that phrase with:

Published but unresolved or confirmed-incomplete components remain in the displayed W cost and retain W’s anchors; the row loses FullCost and interval eligibility. Only a missing published component invokes subset scoring.

This is not a request to reconsider O17/O117 or E209; it is a consistency correction.

The “newly admitted report is at most 30 calendar days old” statement is false under the draft’s empty-window case. Issue: The pooled-evidence-clock paragraph says a newly admitted report reaches no age stage “while it is in its admission window.” The report-window section correctly allows an empty window when the latest staged search predates the release envelope. These statements are individually manageable, but the earlier paragraph describes O32 admission as if every release has a nonempty window and does not explicitly distinguish admission at a previous release from pooling at the present release. Why it hurts the objective: This is not a present numerical defect, but it makes the already complicated relationship between admission, retained reports and partition ageing harder to implement consistently. Concrete change: State the invariant directly: a report first admitted at release t must fall in that release’s nonempty cell window; subsequently it is retained under O127 and ages independently of later windows. An empty window admits nothing, including reports found in an earlier search but never admitted.

2. Methodology design recommendations

Prioritise a deterministic admission-maintenance state machine. Keep the existing score, cohort and basket policies. Add a small versioned object for each ranking and workload:

text
admissionMaintenance:
  policyVersion
  freezePopulationIds
  requiredCompleteCount
  departurePolicy
  entrantPolicy
  currentCompleteIds
  failedIncumbentIds
  maintenanceStatus
  migrationReason

A minimal implementation consistent with frozen admission would test deterioration against the frozen admission population:

𝑁
0
=
∣
𝐶
f
r
e
e
z
e
∣
,
𝐾
𝑡
(
𝑆
)
=
∑
𝑖
∈
𝐶
f
r
e
e
z
e
1
[
complete evidence at 
𝑡
 for every 
𝑒
∈
𝑆
]
.
N
0
	​

=∣C
freeze
	​

∣,K
t
	​

(S)=
i∈C
freeze
	​

∑
	​

1[complete evidence at t for every e∈S].

The maintenance gate would compare 
𝐾
𝑡
(
𝑆
)
K
t
	​

(S) with 
⌈
2
𝑁
0
/
3
⌉
⌈2N
0
	​

/3⌉, while current-cohort coverage remains a separately published diagnostic. This formula requires an explicit departure policy: either maintain captures for departed references until the next freeze, or define how departures adjust the maintenance population. Do not silently treat departure as evidence failure. The exact choice is less important than making it deterministic and independent of processing order.

Add three mixed-refresh regression fixtures. Existing fixtures are extensive, but the following combinations resolve the outstanding admission ambiguity:

Entrants without costs, with no incumbent evidence loss: admission persists.

Entrants without costs plus an incumbent reconstruction failure: one specified maintenance denominator decides the result.

An incumbent departs while another loses completeness: the departure policy and evidence-loss policy produce the same result regardless of processing order.

Each fixture should assert the workload hash, displayed workload per row, reference-panel membership, interval eligibility and release-hold status—not only the admitted component list.

Consolidate row transitions into one executable table. The necessary distinctions already exist; no new evidence or scoring policy is needed:
Component state	Displayed cost treatment	Anchor object used for scoring	FullCost
Published, confirmed complete	Include component	W	May pass
Published, unresolved	Include component; flag	W	Fails
Published, confirmed incomplete	Include component; flag	W	Fails
Missing	Score available subset under O17	W_S	Evaluate separately on W_S
Generate the prose references to these transitions from the same table. This would close the E333/E209 inconsistency without reopening any adopted owner decision.

Keep the remaining methodological architecture unchanged for this revision. I have no new material argument against the fixed cohort policy, exact-variant matching, separate API and Plan rankings, published-record interval target, or the existing disclosures around unidentified Plan transport. In particular, I am not recommending another layer of uncertainty machinery, another benchmark, or another diagnostic ranking. The useful next improvement is determinism in the refresh rules, not additional methodological breadth.

3. Questions for the owner

For E333’s between-freeze deterioration gate, should the two-thirds threshold use the frozen admission population or the current ranking population? If it uses the frozen population, should a configuration’s departure remove it from the maintenance denominator, or should its frozen reference evidence continue to be maintained until re-freeze?

4. Verdict

The draft’s principal limitations are now explicit, and its claims are substantially narrower than its exploratory displayed rankings. I found no new critical or high-severity methodological problem. One refresh-governance ambiguity remains material because it can change whether a release is held; the other findings are consistency edits rather than challenges to owner policy.

VERDICT: HAS FEEDBACK