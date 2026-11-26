0. Read check

Read all four listed files to their ends through the GitHub connector, in order, at commit fe13eb3d27b3cb9f2386f1955752f4052ba7d52e. The quotations below omit Markdown emphasis but preserve the words.

Part 6

First line:

Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V], and for each model × plan cell it ends instead at that cell's latest staged search, so it never claims days nobody searched (owner decision O161, on reviewer 79; a report dated after it is excluded as "dated after the cell's latest staged search", and each cell publishes the date as searchedThrough); compared as UTC calendar dates (date(V) − 30 days ≤ d ≤ date(V), with a timestamped E194 date truncated to its UTC date; reports are recorded by date, not time, so for the report window E213's cutoff is V's UTC date, whole: a report dated that day counts whatever its hour), both end days included, so the window spans 31 calendar dates (a report dated exactly 30 days before the cutoff is in, one dated 31 days before is out), published as the registry's reporting window, which is AGENTS.md's "preceding month".

Final sentence:

Fixtures: two concordant reports 41 days apart, neither admitted earlier, where the older one leaves the partition and the route is diagnostic; a model with a current controlled measurement and a lapsed report pair, where the controlled route stays and the report route is diagnostic; a transfer from a lapsed report donor, which is diagnostic.

Part 7

First line:

Quota schema: the registry stores each plan's limit-schema version: windows (e.g. 5-hour and weekly) with their semantics — session-anchored (starts at first use), fixed reset (calendar or account reset time) or sliding — shared pools across surfaces (e.g. one pool for chat and CLI), pool scope per window (all-models vs per-model), model-specific sub-caps within a shared pool and model-specific consumption (burn) coefficients where measured; how reset balances are treated (counted only if a measurement shows them spendable on the measured workload); and fee decomposition: the primary multiple uses gross cash: M = eligible API-priced usage delivered ÷ (subscription cash fee + any cash required for that usage); usage funded by credits bundled into the fee is counted once in the numerator; separately purchased usage is excluded unless its payment is in the denominator; the denominator must be positive and reconcile to receipts.

Final sentence:

Their selected routes and multiples are printed with the Plan rows (scores.json planRows); GPT-6 Astra (max)'s selected route moved from ChatGPT Plus to a higher plan under O45.

Part 8

First line:

MiMo quota ceiling (owner decision O46): Xiaomi prices MiMo Token Plan credits at parity with its pay-as-you-go API (100M credits = ¥1), and the owner-requested research (Claude's deep-research skill with three researchers, and Perplexity Search with GPT-6.1 Sol, Grok 4.7 and Gemini 3.8 Flash; Silver Bullet's multi-model workflow could not run without provider credentials; record research/2026-10-23-mimo-token-plans/) found no end-user measurement of a MiMo-V2.6 billing period.

Final sentence:

AA Intelligence Index and output speed are diagnostics, not quality.

Part 9

First line:

Leaf sets per ranking (owner decisions O49, O52–O55, O61): AA withdrew DeepSWE v1.1 from its Coding Agent Index, and the owner dropped it in favour of FrontierCode (O49), which left ten common leaves: FrontierCode 25%, Terminal-Bench 4.0 20%, Bug Hunt Bench 15% and the seven leaves outside software engineering.

Final sentence:

Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

Repeated report-admission instructions can be read as overriding their newer, more precise definitions. Issue: Part 6 correctly distinguishes:

Reports entering the range test, including provisional reports only after a logged inference re-check, under O159.

Non-provisional admitting reports determining the value-clipping band, under O176.

Midpoints clipped before geometric pooling, under O115.

Later, the same part says that the range test runs over “every eligible report … provisional ones included,” followed by a value defined as the geometric mean of non-provisional midpoints, without repeating the clipping step. The later wording is not necessarily contradictory when “eligible” incorporates the earlier predicates, but it reads like a second executable specification. Source: part 6, “Report admission is computed,” “Report eligibility profile,” and the paragraph beginning “The split comes first.” Why it hurts the objective: Independent implementations could agree on the evidence records but disagree on admission or the displayed multiple. That is a reproducibility problem rather than a challenge to the adopted admission policy. Concrete change: Replace the later restatement with a reference to one governing admission algorithm, or explicitly say “inference-rechecked provisional reports” and “clipped non-provisional midpoints.” What is new relative to the ledger: This does not ask to adopt O115, O159 or O176 again. It identifies a remaining duplicate-specification ambiguity in the supplied text after those decisions.

2. Methodology design recommendations
Priority 1: Publish one executable report-admission sequence

Consolidate the existing rules into a single ordered specification, referenced everywhere else:

Resolve canonical model and plan identities.

Determine the cell’s new-report window and retain earlier-admitted reports under O127.

Apply measurement-period eligibility, accounting-fault exclusions and partition splits.

Consolidate each observer to one range within the partition.

Form the concordance set from non-provisional reports plus only inference-rechecked provisional reports.

Require at least two independent, non-provisional observers and apply the existing concordance test.

Form the value band from admitting non-provisional reports only.

Clip their midpoints to that band and take their geometric mean.

Apply the existing route precedence, donor propagation and expiry rules.

For report ranges 
[
𝑙
𝑗
,
𝑢
𝑗
]
[l
j
	​

,u
j
	​

], distinguish the concordance set 
𝑇
T from the admitting value set 
𝐴
A:

max
⁡
𝑗
∈
𝑇
𝑙
𝑗
≤
1.20
min
⁡
𝑗
∈
𝑇
𝑢
𝑗
,
j∈T
max
	​

l
j
	​

≤1.20
j∈T
min
	​

u
j
	​

,
𝐵
𝐴
=
[
max
⁡
𝑗
∈
𝐴
𝑙
𝑗
1.20
,
  
1.20
min
⁡
𝑗
∈
𝐴
𝑢
𝑗
]
,
B
A
	​

=[
1.20
max
j∈A
	​

l
j
	​

	​

,1.20
j∈A
min
	​

u
j
	​

],
𝑀
^
=
exp
⁡
(
1
∣
𝐴
∣
∑
𝑗
∈
𝐴
ln
⁡
 ⁣
[
clip
⁡
(
𝑙
𝑗
+
𝑢
𝑗
2
,
𝐵
𝐴
)
]
)
.
M
=exp
	​

∣A∣
1
	​

j∈A
∑
	​

ln[clip(
2
l
j
	​

+u
j
	​

	​

,B
A
	​

)]
	​

.

These formulas express the existing decisions; they introduce no new estimator, threshold, numerator source or policy exception. Source: part 6, O81/O86/O115/O159/O174/O176.

Add one targeted regression fixture: two admitting observers pass, and an inference-rechecked provisional observer participates in concordance but cannot change the value band or pooled value. This tests the interaction behind the textual ambiguity, rather than merely testing each rule separately.

Otherwise, I recommend retaining the designs in these sections. In particular, the separation between displayed Plan evidence and target-workload identification, the explicit accounting-population boundaries, and the consumption-optimal/minimum-cash definition avoid materially different quantities being silently treated as equivalent. Source: part 7, E105/E106/E130.

3. Questions for the owner

None.

4. Verdict

The sectional methodology has no remaining medium-or-higher finding from this review. The remaining feedback is a low-severity reproducibility clarification, not an owner decision challenge or a request to reopen a settled design.

VERDICT: HAS FEEDBACK