0. Read check

Read parts 7–9 through their ends at commit 2ca6c729a3f1a11bd08f5d669f5977875b087381. This review covers only those parts.

Part 7

First line:

One Plan row per configuration and plan (owner decision O48, E245): asked whether "per model, per plan" meant the Plan ranking itself, the owner chose "Rank every plan". A plan row is a configuration on one plan whose route is the official comparator's choice among that plan's candidates (E85, E88); every plan with an eligible (non-diagnostic) route for the configuration has a row, and a configuration with no eligible route keeps one API-cost row, flagged (O13). Rows of one configuration share its quality and API cost and differ only by the plan's multiple. The Plan anchors, clip gate, cost influence, identification yield, interval outputs, displayed cheapest rows, separability, bands and scenario shares range over plan rows; one configuration's plan rows share every scenario draw (one dependency group) and are counted inseparable only by value: in the scenario shares they separate whenever their values differ (the separability statistics leave such pairs out and report their number separately, E258), and a noise band that starts at one of them extends over its configuration's other plan rows (E248). A configuration's own Plan figures (the README table, model pages, and the Plan diagnostics that rebuild anchors or move evidence) are those of its representative row, the plan row of its selected route (the route the comparator selects over the candidates of all its plans together, so the representative row is the plan whose winning route the comparator's keys rank first); the README and site list every plan row. Today the max-effort ranking has 27 plan rows for 9 configurations and the AI Coding Daily ranking 67 for 20. Measured-evidence calibration over plan rows (E249): the official Plan anchors are set over plan rows, so E164 reads each anchor setter's evidence from its plan row. Which plan rows set the official anchors, the measured anchors and their ratio, and the pairwise reversals and largest value change are published for each ranking (scores.json measuredOnlyPlanView), which says when the calibration is unavailable because fewer than two reference rows have complete cost evidence on measured routes (E164).

Last 12 words:

"harness-mixed" (today, max-effort ranking: none; AI Coding Daily ranking: none) |

Part 8

First line:

| | Bug Hunt Bench (2 TypeScript repos, 105 planted bugs, one round per run, vendor CLIs; model+harness) | 8% | 12% | 15% | owner decision O163, 2026-11-01: x = planted bugs fixed (of 105, the board's own score) + genuine unplanted bugs fixed (the board's "extras", real defects the model fixed that nobody planted, verified by its blind judge; partial and claimed-only fixes not counted), each the mean over the published runs for the exact model and effort, harness and route chosen by E206 and recorded (run count recorded); z = x, a plain sum with no rescaling and no ceiling, so the leaf can exceed 100 (fixture: 44.3 planted + 65.3 unplanted → 109.6) |

Last 12 words:

a bias bound in the identification layer); repetitions are not a bias.

Part 9

The first line is blank. Its first nonblank line is:

Uncertainty (three separate layers, one scenario engine)

Last 12 words:

not separable" and its S0 result is not described as target-workload support.

Source identification: the three GitHub connector file reads above, at the specified commit. The connector returned their complete text but supplied no citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. Bug Hunt’s sampling kernel does not distinguish a published multi-run mean from a single-run count

Issue: Part 8 defines the scored Bug Hunt result as the mean across the selected record’s published runs. It also says independent evaluation repetitions affect precision. Part 9 nevertheless assigns its sampling SD using only the planted score and mean unplanted count:

𝜎
B
H
=
105
𝑝
~
(
1
−
𝑝
~
)
+
max
⁡
(
𝑢
,
0.5
)
.
σ
BH
	​

=
105
p
~
	​

(1−
p
~
	​

)+max(u,0.5)
	​

.

The number of published runs does not enter that formula. The text expressly says that captured Bug Hunt run values are unused by v1 streams. Consequently, the specified kernel gives the same spread to identical published means whether they represent one run or several. These rules appear in parts 8’s “Bug Hunt record selection” and “Attempts reconciliation,” and part 9’s S1T definition.

Why it hurts the objective: S1T feeds the reported rank separability, noise bands and noise-margin companions. Its Bug Hunt component does not clearly target either uncertainty in the selected published mean or variation in a future single evaluation. Those are different quantities. Selecting the largest-sample record while ignoring its repetitions in the noise model also disconnects record selection from the precision interpretation.

Concrete change: distinguish two outputs:

Published-mean uncertainty: use public paired per-run planted and unplanted counts where available, with the sampling unit explicitly recorded.

Single-run dispersion stress: retain the present count-based kernel as a separately named approximation, without interpreting it as uncertainty in the published multi-run mean.

Do not automatically divide the current variance by the run count: that would additionally assume independent repetitions and would not resolve shared task or repository effects.

What is new relative to the ledger: E301 and E309 address the planted-plus-unplanted count model and covariance between its two components. This finding concerns the different estimand created by averaging multiple published runs, not that within-run covariance. It does not ask to change O163’s scored leaf.

Low
L1. The GDPval temporal-estimand paragraph overstates what the current capture comparison demonstrates

Issue: Part 8 says that “the captures point the other way” when discussing whether the displayed GDPval Elo equals AA’s integrated Index input. Its accompanying comparison reports zero Elo changes and zero Index-total changes across all 27 overlapping pages.

Why it hurts the objective: An unchanged-versus-unchanged comparison does not distinguish frozen integration from contemporaneous integration. The source-methodology statement and the capture comparison have different evidential roles, but the paragraph presents them as mutually reinforcing evidence of divergence.

Concrete change: retain O70 unchanged and replace that inference with:

AA’s methodology describes a rating frozen at configuration addition. ValueRank instead uses the currently displayed Elo. The current capture comparison shows no movement and therefore provides no empirical test of whether those two values differ.

If historical divergent movement is available in an already captured artifact, identify that particular comparison rather than attributing the inference to the current zero-movement comparison.

What is new relative to the ledger: this is not a challenge to O70 or E90. It concerns the logical interpretation of the newly rendered capture comparison.

2. Methodology design recommendations
Priority 1: Type Bug Hunt noise by the statistic actually published

Keep the official leaf unchanged:

𝑧
𝑖
=
𝑃
ˉ
𝑖
+
𝑈
ˉ
𝑖
.
z
i
	​

=
P
ˉ
i
	​

+
U
ˉ
i
	​

.

Add these fields to its sampling object:

published_statistic: single run or mean of 
𝑟
𝑖
r
i
	​

 runs;

run_count;

available_sampling_units;

sampling_target: published mean, future run, or count-model stress;

repeat_dependence_status.

Where paired public run values are available, form

𝑋
𝑖
𝑟
=
𝑃
𝑖
𝑟
+
𝑈
𝑖
𝑟
.
X
ir
	​

=P
ir
	​

+U
ir
	​

.

If independent repetitions are justified, estimate the published mean’s standard error as

S
E
^
(
𝑋
ˉ
𝑖
)
=
𝑠
(
𝑋
𝑖
)
𝑟
𝑖
.
SE
(
X
ˉ
i
	​

)=
r
i
	​

	​

s(X
i
	​

)
	​

.

Alternatively, resample paired runs under an explicitly conventional empirical-bootstrap branch. Resample the planted and unplanted counts together, not separately: pairing preserves their observed covariance.

Where independence is unsupported or repetitions are too sparse, publish the available run dispersion descriptively and mark published-mean uncertainty “not identified from captured evidence.” Keep the present kernel as the count-model stress rather than silently treating it as a sampling distribution for the mean.

This design uses the run values part 9 says are already captured where published, requires no cross-version transfer, and changes neither scores nor official interval outputs.

Priority 2: Report whether the Bug Hunt estimand choice changes the existing noise conclusions

Use the existing scenario and separability machinery rather than adding another headline ranking. On an identical workload, panel and set of other draws, compare:

the current count-model stress;

a published-mean branch where public repetitions support one.

Publish the changes in:

adjacent-pair separability;

noise-band membership;

noise-margin bar companions.

For rows without sufficient public repetition evidence, report the comparison as unavailable instead of imputing repetition precision. This isolates whether M1 is consequential without claiming that either branch measures deployment reliability.

Priority 3: Separate documentary evidence from movement diagnostics

For the existing GDPval movement diagnostic, add a small rendered status:

no movement observed;

movement observed but integration relationship unresolved;

observed movement distinguishes the candidate integration interpretations.

Derive that status from the captured comparison, while keeping AA’s documented integration policy in a separate field. For this release, the stated zero/zero comparison warrants the first status only.

3. Questions for the owner

None. The recommendations preserve the fixed scoring, cohort, evidence and ranking policies; the Bug Hunt clarification can be implemented within the existing distinction between sampling targets and named stress branches.

4. Verdict

VERDICT: HAS FEEDBACK