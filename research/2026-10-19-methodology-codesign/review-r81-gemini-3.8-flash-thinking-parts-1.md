0. Read check

Read all three requested files to their ends through the GitHub connector, in order, at commit 0aedd96ddfb5c1e86ba1487bc7845bfe301e946d. This review covers only those sections; cited rules defined elsewhere are treated as defined.

Part 1

First line:

ValueRank methodology — draft r163

Last 12 words:

configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

Part 2

The first line is the entire opening bullet, reproduced below:

Two rankings (owner decisions O52, O53, O54): ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52). No benchmark outside AA covers the cohort at exact effort (research/2026-10-23-swe-benchmarks/reports/SWE benchmark candidates.md), so ValueRank publishes two rankings, each over the cohort configurations that have its complete leaf set (Quality): the max-effort ranking (no rule limits it to one effort per family; it holds one configuration per family at the vendor's top effort only because LiveBench 2.0 and Vals run each model once, at its top effort, O54; today 9 configurations from 9 of the 15 cohort families, plotted and retained), which leads on the site and in the README (O54), and the AI Coding Daily ranking (mostly high and medium efforts; today 20). Configurations in both rankings today: 4 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Luna (max), Gemini 4 Argon (high) and MiMo-V2.6-Pro), so 25 of the 37 are ranked at least once. Each ranking has its own leaf table and weights (O55), frozen anchors, quality bars, scenario run, basket admission and diagnostics, scored by the same engine (E253, E254); values compare within a ranking only. Common-leaf diagnostic ranking (owner decision O121, 2026-10-29): because the two leading rankings cannot rank the cheaper efforts that LiveBench, Vals and AI Coding Daily never run, a third ranking scores every cohort configuration with AA's leaves and Bug Hunt, at any effort, on the ten leaves the leading rankings share, at the weights O121 set for its ten leaves, O55's before O61's amendment (FrontierCode 25, Terminal-Bench 20, Bug Hunt 15 and the seven leaves outside software engineering). Today it ranks 33 configurations, 8 of them ranked in neither leading ranking: Claude Haiku 5.5 (low), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh) and GPT-6.1 Terra (low). It has its own frozen anchors, quality bars, basket admission and scenario run, but it is diagnostic: it earns no interval or scenario label, its gates are disclosed but never hold the release, a configuration ranked only there stays listed (not ranked) in ValueRank, and a model page never makes it its home. For each bar position and basis it publishes its displayed-record cheapest row beside each leading ranking's answer at the same position (each ranking's bar levels are its own), with whether they differ (scores.json v3Tracks.common.leadingComparison). Admission per ranking (owner decision O57, implementing E254): O15 and E140 admit a component when its exact cost covers two-thirds of "the cohort"; with two rankings this is two-thirds of the ranking's own cohort rows, because each ranking is scored on its own rows and anchors. The choice changes the result: today the Coding Agent Index v2.0 is priced for 8 of the max-effort ranking's 9 rows, so it is admitted there, while under a whole-cohort reading it would have stayed pending (the counts at the decision are in the ledger, O57). Per-ranking full set (E255): a cohort configuration is ranked in every ranking whose full set it has, and it is excluded from ValueRank, listed under O38 with its searches, only when it lacks both leading rankings' sets (the common-leaf diagnostic ranking may still rank it; today 12: Claude Haiku 5.5 (low), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (low), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (low), Gemini 4 Carbon (high), MiMo-V2.6-Flash and MiniMax-M3.1-Flash (max)). Each ranking also lists the cohort configurations without its own set, with their missing leaves (today 28 beside the max-effort ranking and 17 beside the AI Coding Daily ranking). Every missing (configuration, added leaf) pair carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py).

Last 12 words:

configuration missing a leaf after the search is listed, not ranked (O36).

Part 3

The literal first line is blank. Its first nonblank line is:

Cost (25% of the value score)

Last 12 words:

on the Plan basis the workload question is the M_W identification status.

1. Findings by severity

Critical

None.

High

None.

Medium

M1. The clipping-aware transfer tolerance mistakes local insensitivity for unlimited robustness

Issue: Part 1, “Transfer tolerance (E242),” states:

an assumption row whose cost score is clipped at an anchor moves no value whatever its multiple, so it has no finite tolerance

Clipping makes the score locally constant while the effective cost remains beyond that anchor. It does not make it constant for every possible multiple. A sufficiently large change in the opposite direction moves effective cost back into the unclipped region and can change value materially.

Why it hurts the objective: A reader can interpret toleranceUnbounded as evidence that even an arbitrarily wrong transfer cannot alter the row’s value. That is stronger than the score function supports and particularly consequential for a Plan ranking explicitly described as exploratory.

Concrete change: Replace the categorical clipped/unbounded rule with a directional, exact inversion of the clipped score. Report separately:

The factor needed to change value by the stated threshold when the multiple increases.

The factor needed when it decreases.

“Threshold unreachable in this direction” only when the remaining score headroom is insufficient.

What is new relative to E272: This does not request the already-adopted clipping disclosure. It identifies a mathematical error in its present implementation contract: zero local slope does not imply an infinite finite-change tolerance.

Source: Part 1, Outputs → Transfer tolerance.

M2. The cohort wording can accidentally re-retain a configuration indefinitely

Issue: Part 1 defines O145 using:

a configuration of the previous release's cohort that has left the rendered frontier and the near gap stays a cohort row for one more release

But a retained configuration is itself a member of that previous release’s cohort. The surrounding “never retained twice” restriction prevents indefinite retention only if the implementation distinguishes previous plotted membership from previous retained membership. The prose also does not clearly specify whether a configuration that genuinely re-enters the plotted cohort and later exits can receive another one-release retention.

Why it hurts the objective: The cohort is a fixed-policy selection mechanism. Ambiguity in its state transitions can change membership, benchmark searches, ranking coverage, admission denominators and frozen-bar populations without a substantive owner decision.

Concrete change: Express O145 as a state machine based on consecutive release identities, distinguishing plotted, retained, and out. Define whether “never retained twice” means once per exit episode or once over the configuration’s lifetime.

What is new relative to O145/E282: This is not a challenge to retention or a request for its already-adopted disclosure. It concerns the recursive definition of “previous release’s cohort” and the unresolved re-entry transition.

Source: Part 1, Cohort and configuration → One-release retention; Part 2, counts and admission denominators.

Low

L1. Two current-state statements contradict the section’s own population records

Issue:

Part 3’s “Subset-workload interval outputs” says:

every ranked row of each leading ranking is priced on its main workload

Yet Parts 2 and 3 explicitly identify MiMo-V2.6-Pro as a max-effort subset-workload row.

Part 3’s “Scored on W” current-state example lists only Claude Opus 5.5 (high) for AI Coding Daily, whereas Part 2 identifies both its high and medium configurations as outside that ranking’s complete-cost admission panel. Part 3 also says the three Opus rows have failed reconstruction.

Why it hurts the objective: These statements obscure which rows support the main-workload comparisons and which fail FullCost. The underlying rules may be sound, but readers cannot reconcile the prose with the published populations.

Concrete change: Render these assertions from the same membership arrays used for mainWorkload, subsetWorkload, and failed-completeness populations. Replace the first statement with a distinction between unavailable main-workload cost and the narrower population actually displayed in a subset stratum.

What is new relative to E265: The ledger already requires generated current figures. This finding identifies two surviving contradictory assertions, rather than requesting generation as a new general policy.

Sources: Part 2, “Counts, defined once”; Part 3, “Scored on W” and “Subset-workload interval outputs.”

2. Methodology design recommendations
Priority 1: Compute transfer tolerance against the actual clipped score

Retain the owner-set weights, anchors and Plan arithmetic. Change only the diagnostic.

For current selected multiple 
𝑀
0
M
0
	​

, let 
𝐶
0
C
0
	​

 be its effective cost and let

𝑆
𝐶
(
𝐶
)
=
100
 
clip
⁡
(
ln
⁡
𝑐
𝐻
−
ln
⁡
𝐶
ln
⁡
(
𝑐
𝐻
/
𝑐
𝐿
)
,
 
0
,
 
1
)
.
S
C
	​

(C)=100clip(
ln(c
H
	​

/c
L
	​

)
lnc
H
	​

−lnC
	​

,0,1).

For a multiplicative change 
𝑟
r in the selected multiple, evaluate

𝑉
(
𝑟
)
=
0.75
𝑄
+
0.25
𝑆
𝐶
(
𝐶
0
/
𝑟
)
.
V(r)=0.75Q+0.25S
C
	​

(C
0
	​

/r).

For the published value threshold 
𝑡
t, calculate

𝑟
↑
=
inf
⁡
{
𝑟
≥
1
:
𝑉
(
𝑟
)
−
𝑉
(
1
)
≥
𝑡
}
,
r
↑
	​

=inf{r≥1:V(r)−V(1)≥t},

and

𝑟
↓
=
inf
⁡
{
𝑟
≥
1
:
𝑉
(
1
)
−
𝑉
(
1
/
𝑟
)
≥
𝑡
}
.
r
↓
	​

=inf{r≥1:V(1)−V(1/r)≥t}.

This incorporates both the distance required to leave a clipped plateau and the subsequent movement through the scoring region. Return an unreachable status only when the relevant set is empty.

Implementation requires no new external evidence: the release already contains 
𝐶
0
C
0
	​

, 
𝑄
Q, the applicable anchors and the separability threshold. Use each subset row’s own anchor object, as E86 already requires. This corrects M1 without estimating transfer error or adding assumptions to interval outputs.

Priority 2: Make retention a deterministic transition table

If O145 is intended to allow one retained release per exit episode, use:

Previous state	Currently on/near AA frontier?	New state
Any	Yes	plotted
plotted	No	retained
retained	No	out
out	No	out

Store the previous release identifier and previous inclusion state. A retained row cannot create another retained row merely by remaining in the previous cohort.

Add fixtures for:

First exit.

Continued absence.

Re-entry.

A second exit after re-entry.

A retained configuration that loses benchmark coverage.

If the owner instead intends lifetime-only retention, add a persistent everRetained field and state that policy explicitly. Either design is routinely refreshable from the existing public captures and release history; neither changes the fixed frontier/near-frontier rule.

Priority 3: Validate prose membership, not just numerical totals

Extend the existing generated-current-figure checks with assertions that:

Every named subset row belongs to the subset population.

Every row described as main-workload-priced has all admitted cost records.

Every named unresolved row equals the build’s unresolved-row set.

Main-workload and subset populations partition the scored rows at the intended level.

A sentence claiming “every” or “none” is generated from the corresponding predicate.

This is a targeted repair for L1, not a proposal for another certification layer or release framework.

3. Questions for the owner

Does O145 permit a fresh one-release retention after a configuration genuinely re-enters the plotted frontier/near cohort and subsequently exits again, or is retention available only once in that configuration’s lifetime? The answer determines the retention state machine and whether it needs persistent lifetime history.

4. Verdict

The reviewed sections carefully limit claim scope, preserve exact-configuration evidence, distinguish API from Plan buyers, and disclose the present absence of supported Plan frontier/bar claims. I found no new reason here to reopen the fixed cohort, weighting, subset-ranking or Plan-evidence policies. The remaining material feedback concerns the transfer-tolerance mathematics and retention-state precision, plus two current-state prose defects.

VERDICT: HAS FEEDBACK