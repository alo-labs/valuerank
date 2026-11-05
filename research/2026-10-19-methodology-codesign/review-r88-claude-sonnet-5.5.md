0. Read check

Read all 14 parts, in order, through the GitHub connector at commit fedb331f25983db7bec2a174e324bcaa667d2052. Every response reached the end of its part. The parts sometimes end at paragraph or clause boundaries rather than sentence boundaries; those endings are preserved below.

Draft’s first line:

ValueRank methodology — draft r170

Final sentence or terminal text of each part:

Part 1:

Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

Part 2:

Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

Part 3:

Release assertion: the scored field is the basket sum, not cost per task, not AA's 7:2:1 blended price, not total Index cost.

Part 4:

Fable 5.1 is not a donor-error gauge (owner decision O35, 2026-10-21): Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

Part 5:

Fixtures: two concordant reports 41 days apart, neither admitted earlier, where the older one leaves the partition and the route is diagnostic; a model with a current controlled measurement and a lapsed report pair, where the controlled route stays and the report route is diagnostic; a transfer from a lapsed report donor, which is diagnostic.

Part 6:

Their selected routes and multiples are printed with the Plan rows (scores.json planRows); GPT-6 Astra (max)'s selected route moved from ChatGPT Plus to a higher plan under O45.

Part 7:

AA Intelligence Index and output speed are diagnostics, not quality.

Part 8:

Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

Part 9:

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

Part 10:

The current ladders are in Output 3 and scores.json barCurrency.

Part 11:

Ranked configurations only (owner decision O43): a family listed under O38 with an indicative value (O41) is not a competitor in any frontier or bar output; each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

Part 12 — the concluding release-test sentence:

Omniscience vector above; Bug Hunt vector above; Index reconciliation (C_6 + C_HLE-Diamond + C_Omniscience + C_CritPt v2 reproduces AA's total within the E209 tolerance, the task counts taken from the registered v5 evaluations; the residual never enters C_W); Coding Agent Index fixtures (E82): the scored cost equals AA's pooled per-task-attempt mean × 290 (v2.0, O50); the raw telemetry sum and sum ÷ mean are preserved as diagnostics without requiring equality to 290 (fixture with unequal telemetry coverage, where mean × 290 differs from the sum and the row still scores and passes completeness); completeness has two predicates: a Coding Agent Index cost is complete when AA's missing- or declined-task markers are absent (O27), and an Index SDLC component cost also needs its row's Index reconstruction to pass (E209); aggregate/component exclusivity (an exactly reconciled decomposition leaves basket cost unchanged); repetition invariance (averaging extra evaluation repetitions does not multiply workload cost); workload migration changes W's hash and invalidates unreviewed Plan transport; basket persistence (a new cohort row with missing costs does not change W's hash); single clip predicate (all gate consumers call one function, with integer-boundary fixtures for several cohort sizes); split invariance (partitioning an execution family into accounting subcomponents leaves its pass cost and C^match unchanged; splitting a quality reporting leaf never creates or duplicates an execution-family weight — E55); kernel completeness (every stochastic input has executable parameters); price tests (E23): uniform price scaling cancels in Plan cost; arbitrary category-price changes cancel when measured consumption is proportional to the target-workload token vector; otherwise category repricing changes Plan cost by (p·x / p·u) and triggers a transport identification recheck (two-category fixture with different measured and target mixes); restoring a missing leaf moves correctly from S0 to S1; transfers-off never silently becomes API fallback in an interval output or a scenario panel (E167); a tighter quota cannot increase computed capacity; window-semantics fixtures above; adding an unrelated row cannot change common-panel diagnostics except via declared cohort-dependent quantities; a frozen bar does not force its setter as the answer (at freeze at least two population configurations reach H on displayed quality; E192), and each bar result publishes its count of R_W configurations that can qualify (E198a); cheapest fixtures (non-provisional and provisional singletons, unique cheapest, equal-cost tie → both in K_r; no self-comparison); interior-witness possible-frontier fixture (E43); completeness statuses (an AA declined- or missing-task marker → confirmed incomplete; an Index reconstruction that misses AA's total → unresolved; otherwise confirmed complete; the Coding Agent Index cost equals the per-task metric × 290); completeness (an AA-marked incomplete component fails FullCost and removes the row from R_W without changing its displayed score); session-start fixture (a schedule whose second burst starts a new session after the first session ends is feasible; capacity results carry a feasible schedule); interval decision statuses (an unresolved solve is never certified); widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic.

Part 13 — terminal sentence fragment, continued in part 14:

One AA state (E217): the model-page snapshot, the chart capture, the Coding Agent Index capture and the cost-chart capture are each at most 7 days from the snapshot, the build tests each of the last three against the release cutoff and the snapshot itself defines it (O65), and the build fails otherwise, and capture proximity alone does not show one AA revision, so the chart is also reconciled with the model pages on the fields both publish: each chart point linked to a captured page must carry that page's total Index cost (within 1%) and its displayed Index (the page's unrounded Index within half a display unit), and a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);

Part 14:

Revision history: omitted from this review copy (not normative); it is in draft-r170.md in the same folder of the repository.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low
L1. The basket-scope sensitivity’s name now overstates what the branch aligns

Issue: E178 calls its deletion branch “quality restricted to the cost basket’s scope.” Under the current v5 design, that branch retains GDPval-AA and AA-LCR even though their costs have left the basket. It also retains the whole LiveBench Overall leaf. The draft explains the GDPval-AA/LCR exception, but the short label still sounds like an execution-matched quality–cost comparison. This is visible in part 10’s specification-branch definition, read alongside parts 3 and 8.

Why it hurts the objective: readers trying to determine whether a configuration is cheap for the capability being rewarded can mistake this branch for the matched-cost diagnostic. It is actually a narrower intervention: removal of three specified recall/science leaves, not matching quality to all—and only—the costed executions.

Concrete change: rename the branch “recall/science-leaf removal sensitivity,” retaining its exact existing leaf set and calculations. Add one sentence: “This is not an execution-matched quality–cost comparison; see the matched-cost diagnostic for that question.”

What is new relative to the ledger: this does not reopen E178’s adopted removal set or O10/O15. It addresses the label after O137 removed additional quality-bearing evaluations from the basket while explicitly keeping them in this branch.

L2. The retention narrative mixes plotted exits with actual cohort exits

Issue: part 14 says ten configurations “left it” in its cohort-change narrative, while parts 1, 2 and 12 correctly keep those configurations in the current cohort through O145. Part 14 even clarifies this distinction elsewhere for MiniMax-M3.1-Flash. The executable rule is clear; the narrative terminology is not.

Why it hurts the objective: cohort composition determines which alternatives a ranking considers. Calling retained configurations cohort exits makes the release’s coverage and comparison scope harder to interpret, particularly when some retained configurations still rank.

Concrete change: render three separately named diffs:

plotted-set entrants and exits;

retained-set entrants and expirations;

final-cohort entrants and exits.

Replace the offending prose with “left the plotted frontier/near set and remain in this release’s cohort under O145.”

What is new relative to the ledger: E306/E310 already resolve membership correctly. This finding concerns an inconsistent current-release description, not a request to change retention or add another membership rule.

2. Methodology design recommendations
Priority 1: Give each sensitivity branch an explicit comparison contract

Keep the existing formulas, weights, admission rules and evidence policies. Add a compact, generated contract beside each sensitivity result:

Field	Meaning
Intervention	Precisely which inputs or rules change
Held fixed	Quality, workload, routes, multiples, anchors and panel, as applicable
Comparison target	Displayed-score arithmetic, alternative workload, evidence removal, or identified economics
Interpretation limit	What the result does not establish

For E178, for example:

Intervention: remove AA-Omniscience, HLE-Diamond and CritPt v2 from quality.

Held fixed: basket, selected routes, displayed multiples, anchors and common panel.

Comparison target: displayed-score sensitivity to these three quality leaves.

Interpretation limit: not full quality–cost execution matching.

This is a presentation consolidation of existing contracts, not a new uncertainty layer or a new gate. The draft already distinguishes these targets carefully across E103, E146, E149/E152, E172 and E178; generating the same short contract wherever results appear would make those distinctions usable without requiring readers to reconstruct them from several sections.

Priority 2: Generate the release’s membership explanation from the retention state machine

Use the already defined sets:

𝑇
𝑡
=
𝑃
𝑡
−
1
∖
𝑃
𝑡
,
𝐶
𝑡
=
𝑃
𝑡
∪
𝑇
𝑡
.
T
t
	​

=P
t−1
	​

∖P
t
	​

,C
t
	​

=P
t
	​

∪T
t
	​

.

Publish separately:

Plotted exits
=
𝑃
𝑡
−
1
∖
𝑃
𝑡
,
Plotted exits=P
t−1
	​

∖P
t
	​

,
Final-cohort exits
=
𝐶
𝑡
−
1
∖
𝐶
𝑡
.
Final-cohort exits=C
t−1
	​

∖C
t
	​

.

Generate the prose directly from these sets and assert that no retained ID is described as a final-cohort exit. This needs no new public data and preserves O145, E306 and E310.

I recommend no additional scored leaf, changed weight, altered normalization, expanded uncertainty model or new release gate in this round. Those would require a material new argument beyond the adopted and rejected decisions; I did not find one after reading the full draft.

3. Questions for the owner

None.

4. Verdict

The draft’s current methodology is coherent against its explicitly narrowed objective: ranking evidenced configurations within each ranking’s declared benchmark mix, workload and buyer basis—not identifying a market-wide practical optimum. In particular, it does not promote unidentified Plan transport into a frontier/bar claim, and it distinguishes published-record stability from benchmark-noise sensitivity.

The remaining feedback is low-severity terminology and generated-release clarity. Neither finding requires reopening an owner decision or changing a score. Under O56, this is a clean round, although it is not a no-feedback round.

VERDICT: HAS FEEDBACK