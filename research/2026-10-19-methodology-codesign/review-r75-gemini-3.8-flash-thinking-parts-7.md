0. Read check

Part 7:

First line: - **Scoring with frozen, per-basis anchors** in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); **anchor object (E20)**, identified by anchor version, basis and workload hash (the hash covers the workload's component set only, so two rankings' workloads with the same components share a hash but are different anchor objects with different references and anchors, and equal hashes imply no comparability across rankings): reference configuration ids and frozen costs, the references chosen by the registered **anchor-panel policy (E160)** — distinct from workload admission even where it coincides: the ranked configurations with complete cost evidence (exact cost, no AA missing- or declined-task marker) on every component of the workload at the freeze cutoff (on the main workload, the admission reference panel), on the Plan basis every plan row of the same configurations at its displayed Plan cost (O48) — measured routes, owner assumptions of every kind and API-cost fallbacks alike, since each is scored in the Plan table (O13, O16) and a narrower panel would clip them; at least two references, otherwise that workload's anchors are unavailable and its configurations get no cost score (the main workload must meet the minimum, or freezing fails); **anchor availability after the valuation gate (E184)**: a reference must also pass the valuation-basis gate (E170 outcome 1 or 2) at its freeze; a frozen anchor object keeps its references when one later fails the gate (as with any evidence lost after freezing), and a new freeze leaves out a row whose AA cost omits a pricing term (O94); a subset workload left with fewer than two eligible references takes the unavailable state above; and a main-workload migration whose new workload would have fewer than two eligible references is deferred — the release publishes on the current anchor version and admitted set, the component that would have been admitted stays pending with the reason "anchor migration unavailable — insufficient valuation-eligible references", and the release is not held (O29), because anchors from the old workload are never relabelled for a new one; a workload migration is atomic across bases — both bases share the workload object and E160's reference configurations (the Plan references are every plan row of the same configurations at its displayed Plan cost, O48), so their availability cannot differ; the shared eligibility is complete cost evidence on every component, an E170 outcome of 1 or 2 for the configuration's AA cost and, from the next freeze, no O94 pricing omission, and the selected Plan evidence's own valuation status (E138) governs Plan interval eligibility, never anchor eligibility, because E160's Plan anchors must cover the displayed Plan table (measured routes, owner assumptions of every kind and API fallbacks alike; the measured-evidence calibration of E164 shows what that choice does); each freeze publishes a row-level anchor-eligibility table (complete evidence, valuation-gate outcome, eligibility and exclusion reason); the first freeze of a new methodology version that cannot anchor its main workload is not released and the previous version's release stays live (a versioned migration completes only with its anchors, O12), while a subset workload takes the unavailable state; fixtures: a superseded row inside a frozen anchor panel leaves the anchor unchanged; a freeze excludes superseded and unverified rows; a deferred migration keeps the prior workload and lists the pending component; a first freeze short of references is refused; IDs and costs stay frozen, evidence lost after freezing never rebuilds an anchor, and any population or rule change is a new anchor version with an old/new bridge (fixtures: reordered input rows give identical anchors; an unresolved component removes a row from the population; a subset workload below the minimum leaves its rows unscored without disturbing the main gates); c_L = min reference cost ÷ 2 and c_H = max reference cost × 2 (a fixed ln 2 log padding, so the reference cohort itself never clips); units; expected clipping (none for the reference cohort). A first-release fixture on the actual reference cohort must pass without re-anchoring. Dollars always displayed; unclipped values kept. **Clip gate (single governing gate)**: per basis and anchor object, hold the release (O12) when more than max(1, 10% of n) rows clip, where n is the number of ranked rows scored on that anchor object (ranked rows on its workload with a positive cost on that basis; a subset workload is gated on its own anchor object), or when any such ranked row lies beyond an anchor by more than a factor of 2. **Listed rows beyond the anchors (O58)**: a listed configuration (E259) is not in the gate's population and never holds a release, because it has no rank and no label; the gate output discloses each listed row whose cost lies outside its workload's anchors, with its basis, side, factor, whether it passes the factor-2 limit, and whether it is a point on AA's rendered frontier (the E197 entrant case, now visible rather than held). Today, in the max-effort ranking, API: none; Plan: Gemini 4 Carbon (high) 4.74 above the high anchor (rendered-frontier point, past the factor-2 limit). In the AI Coding Daily ranking, API: GPT-6 Luna (low) 2.30 below the low anchor (rendered-frontier point, past the factor-2 limit); Claude Opus 5.5 (max) 1.24 above the high anchor; Claude Sonnet 5.5 (max) 1.17 above the high anchor; Gemini 4 Carbon (high) 1.01 above the high anchor (rendered-frontier point); Plan: Gemini 4 Carbon (high) 8.17 above the high anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (low) 2.71 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (low) 2.30 below the low anchor (rendered-frontier point, past the factor-2 limit). **Gate scope (E262)**: every gate runs per ranking on that ranking's own anchor objects and rows; both rankings publish together, so a hold in either holds the release, and the release record names the held rankings (scores.json releaseHold). **A held release (E200)** is still built. Its manifest names each clipped row, including a frontier entrant, with its unclipped cost and score and the flag "off-anchor scale, release held", and the entrant stays in the reconciliation inventory. That output is published with the dual run that clears the hold. **Re-anchoring path (E197)**: the gate's remedy is pre-built. Anchors stay over a ranking's ranked rows (listed rows are disclosed, O58); a newly ranked row beyond them that holds the gate is cleared only by the O12 versioned re-freeze with its dual run, and the gate output names that remedy (owner decision O120, 2026-10-29). The freeze command re-freezes on the release's evidence, and the dual-run command scores that same evidence on the previous and the new anchor objects. It publishes each row's cost score, value and rank under both, and each bar's result under both bar objects (O12), so a cheaper entrant beyond the low anchor can clear the gate within one release cycle as a versioned migration. **Re-freeze at the moved cutoff (owner decision O47, E247, E253)**: AA published FrontierCode results after the 2026-10-21 cutoff, and the owner chose "Move cutoff now": the release cutoff moved to that day's new capture instant, every AA source was re-captured and the anchors were re-frozen. No dual run was possible, because the main workload changed (Coding Agent Index v1 left the basket when AA replaced it with v2.0), so this is a workload migration (E184) and the engine refuses to score on the previous anchors; the previous anchor object is kept as v3-frozen-2026-10-21-before-o47.json. **AA data after the cutoff (owner decision O65, 2026-10-25)**: AA data read after the release cutoff is never merged into a pinned capture; it moves the cutoff, every AA source is re-captured and the anchors are re-frozen. On 2026-10-25 this moved the cutoff from 2026-10-23T06:26:23Z (the safety-refusal counts of O63 had been read later that day) to the new capture instant; the re-capture added Kimi K3.1 Pro as a rendered-frontier vertex. Because the main workload of each ranking did not change, a dual run on the previous and the new anchors was possible and is published (data/v3_dual_run.json, data/v3_dual_run_aicd.json; the previous objects are kept as v3-frozen-2026-10-23-before-o65.json and v3-frozen-aicd-2026-10-23-before-o65.json). **Board re-read (owner decision O68, 2026-10-25)**: with the cutoff moved, every board either ranking uses was re-read (Vals' two boards, AI Coding Daily with its hidden older rows, Bug Hunt Bench's scoreboard and LiveBench 2.0's 2026-10-23 release in full; tbench.ai's Terminal-Bench 4.0 leaderboard and Cognition's FrontierCode board re-read and found unchanged, so their 2026-10-23 captures stand), each kept only when its own last update predates the cutoff's day (O60); every reviewed match is kept, the build stops if a matched row vanished or changed effort, and on 2026-10-25 the only changes were Kimi K3.1 Pro's new rows and LiveBench's new release (research/2026-10-25-board-reread/). **Re-capture under Intelligence Index v5 (owner decision O132, 2026-10-30)**: AA published Intelligence Index v5.0 around 2026-10-27, after the 2026-10-25 cutoff, and the owner chose to re-capture under v5 now: under O65 the cutoff moved to 2026-10-31T04:10:00Z, every AA source was re-captured (the chart at 2026-10-30T22:15:18Z), the leaves were mapped to their v5 successors (O136) and the basket re-decided (O137), and every ranking's anchors were re-frozen on the v5 cohort (anchor versions below). As at O47, the main workload of each ranking changed (GDPval-AA, SciCode and AA-LCR left the basket; FrontierCode 2.0 and Terminal-Bench-Science joined it), so this is a workload migration (E184) with no dual run on the previous anchors; the previous anchor objects are kept in research/2026-10-30-v5-recapture/previous-anchors/, and the published dual-run files still describe the O65 move of 2026-10-25. Every board was re-read on 2026-10-30 (O68; research/2026-10-30-v5-recapture/third-party/): LiveBench had withdrawn its 2026-10-23 release, so its 2026-10-25 release is pinned (O139); Vals, Bug Hunt and AI Coding Daily added GPT-6.1 Terra rows (Vals also Gemini 4 Carbon) and changed no other cohort value; tbench.ai was unchanged; and no board row is dated after the v5 chart capture. E247's freeze at O47 over the 29-configuration cohort (anchor version v3-2026-10-23, API 4.19 to 12,078 USD on 27 references at O47) was replaced before any release by one frozen object per ranking (E253): the max-effort ranking's version string is v3-2026-10-31 and the AI Coding Daily ranking's is v3-2026-10-31-aicd, each padded (c_L = cheapest reference ÷ 2, c_H = dearest × 2) per workload and basis, with every anchor object's references and anchors in scores.json workloads. Today a cost doubling is worth 3.11 value points (offset by 4.14 quality points) on the max-effort API basis and 3.19 (4.26) on its Plan basis, and 3.02 (4.03) and 2.88 (3.84) in the AI Coding Daily ranking.

Last 12 words: value for 10 of 19 cohort rows in the 2026-10-17 snapshot) |

Part 8:

First line: - **GDPval temporal estimand (E90, owner decision O70, 2026-10-25)**: the leaf is the GDPval-AA v2.1 Elo that AA's model page displays at the release's capture, the leaderboard value, which AA refits as models join.

Last 12 words: bias bound in the identification layer); repetitions are not a bias.

Part 9:

First line: ## Uncertainty (three separate layers, one scenario engine)

Last 12 words: not separable" and its S0 result is not described as target-workload support.

All parts were read in full to their end.

1. Findings by severity
Critical

Internal contradiction between MiMo-V2.6-Flash thinking-mode matching and Bug Hunt E206 selection rule

Issue: Part 8 explicitly asserts under MiMo-V2.6-Flash with thinking enabled (owner decisions O135 and O140) that: "Bug Hunt's OpenRouter default-route run and Vals' records, which state no reasoning setting, stay unmatched (O140)." However, the very next subsection under Bug Hunt record selection (E206) states: "a model AA lists with one unlabelled reasoning mode matches a documented equivalent setting recorded with its evidence, or a record that is itself unlabelled (the same single mode); today the equivalents are MiMo-V2.6-Flash at enabled or high (O54, O66, O135, O140)."

Why it hurts the objective: This is a direct internal contradiction. Under E206, an unlabelled Bug Hunt run matches MiMo-V2.6-Flash, which would admit Bug Hunt and enable the model to meet O36/O38 completeness gates; under O140, the unlabelled Bug Hunt run remains unmatched, leaving MiMo-V2.6-Flash listed rather than ranked. Automated build harnesses and validation gates will fail or produce nondeterministic cohort rosters when two adjacent paragraphs give conflicting matching rules for the same benchmark and model.

Concrete recommendation: Reconcile Part 8 with owner decision O140. Remove the clause "or a record that is itself unlabelled (the same single mode); today the equivalents are MiMo-V2.6-Flash at enabled or high" from E206, and explicitly specify that because Xiaomi's API documents thinking enabled as an active reasoning mode, Bug Hunt records without explicit thinking-enabled/high telemetry do not match.

High

Clipping bias and mass concentration at boundaries in S1T normal draws

Issue: In Part 9, S1T draws each observed leaf score from a Gaussian distribution 
𝑁
(
𝜇
,
𝜎
2
)
N(μ,σ
2
) with plug-in standard error 
100
𝑝
~
(
1
−
𝑝
~
)
/
𝑛
100
p
~
	​

(1−
p
~
	​

)/n
	​

, and then enforces domain validity by hard clipping: "clipped to 0–100".

Why it hurts the objective: Hard-clipping an unbounded Gaussian distribution generates asymmetric truncation bias for frontier models scoring near the boundary (e.g. 90–98% on FrontierCode, HLE, or Omniscience). Draws exceeding 100 are forced to 100 while draws below remain unconstrained, causing the expected drawn score 
𝐸
[
𝑧
clipped
]
E[z
clipped
	​

] to fall strictly below the observed point estimate 
𝜇
μ. Furthermore, it produces an artificial point mass (atom) at exactly 100.0, distorting scenario frequencies, rank-separability metrics, and cheapest-above-bar qualifiers.

Concrete recommendation: Replace Gaussian sampling plus clipping with exact conjugate Beta posterior sampling under the Jeffreys prior already adopted in E241: draw 
𝑝
∗
∼
Beta
(
𝑘
+
0.5
,
 
𝑛
−
𝑘
+
0.5
)
p
∗
∼Beta(k+0.5,n−k+0.5) and set 
𝑧
=
100
⋅
𝑝
∗
z=100⋅p
∗
. This strictly bounds all draws within 
[
0
,
100
]
[0,100] without clipping bias, preserves the mean, and eliminates boundary atoms.

Sample-size dominance over harness comparability in Bug Hunt record selection

Issue: In Part 8, E206 specifies: "Among the owner's published results for the key's name and effort, over every harness and route, the record is the largest-sample mean ('mean of N')."

Why it hurts the objective: Unlike Terminal-Bench 4.0, which enforces a pre-registered agent hierarchy (Terminus 2 
→
→ mini-SWE-agent 
→
→ OpenHands 
→
→ vendor CLIs), Bug Hunt chooses solely by sample size 
𝑁
N. If a third party publishes 
𝑁
=
3
N=3 runs using an unoptimized CLI wrapper and the model provider publishes 
𝑁
=
1
N=1 run on their native vendor CLI, the build automatically switches the benchmark record to the wrapper CLI. As E224 notes, cross-harness variation is substantial (e.g. Gemini 4 Argon scored 40.7 vs 33.0 across harnesses). Selecting purely on 
𝑁
N introduces uncalibrated harness noise into the headline quality score.

Concrete recommendation: Establish an explicit harness precedence order for Bug Hunt (e.g. Native Vendor CLI 
>
> Reference Bench CLI 
>
> Third-Party Wrapper) before using 
𝑁
N as a tiebreaker, matching the rigorous agent registration pattern established for Terminal-Bench.

Medium

Micro-task category sampling noise in LiveBench 2.0 Overall under S1T

Issue: In Part 8 and Part 9, LiveBench 2.0 Overall's standard deviation in S1T is computed from its seven category binomial shares, where Reasoning has 
𝑛
=
4
n=4 tasks and Data Analysis has 
𝑛
=
3
n=3 tasks ("Reasoning and Data Analysis count their parts... wide reading; E264").

Why it hurts the objective: With 
𝑛
=
3
n=3, a Jeffreys proportion yields a category standard error exceeding 27 percentage points. Because LiveBench 2.0 Overall carries 15% of the total quality score in the max-effort ranking (tying FrontierCode 2.0 as the largest single leaf), this extreme binomial variance from 7 macro-prompts dominates the S1T quality composite spread, artificially depressing ordinal rank separability across the entire ranking.

Concrete recommendation: Pin the task count 
𝑛
𝑐
n
c
	​

 in LiveBench categories to the evaluated sub-question or unit-test count (the narrow reading) rather than top-level prompt counts, or cap the minimum category effective sample size to prevent small task counts from inflating uncertainty in a 15% leaf.

Cohort-dependent anchor span distorts the nominal cost-quality exchange rate

Issue: In Part 7, cost anchors are padded from the reference cohort: 
𝑐
𝐿
=
min
⁡
(
𝑐
)
/
2
c
L
	​

=min(c)/2 and 
𝑐
𝐻
=
max
⁡
(
𝑐
)
×
2
c
H
	​

=max(c)×2. As a consequence, the value impact of a cost doubling is inversely proportional to the log-span 
ln
⁡
(
𝑐
𝐻
/
𝑐
𝐿
)
ln(c
H
	​

/c
L
	​

). As documented, a cost doubling is worth 3.11 value points in max-effort API, but only 2.88 value points in AI Coding Daily.

Why it hurts the objective: The headline metric purports to maintain a fixed 25% cost / 75% quality balance (O2). However, when the cohort expands to include extreme low-cost or high-cost references, 
ln
⁡
(
𝑐
𝐻
/
𝑐
𝐿
)
ln(c
H
	​

/c
L
	​

) widens, which automatically compresses 
𝑆
𝐶
S
C
	​

 and dilutes the real-world economic significance of cost across all models.

Concrete recommendation: Decouple the anchor log-span from cohort extremes by registering a standardized span 
Δ
ln
⁡
𝑐
=
ln
⁡
(
1000
)
≈
6.908
Δlnc=ln(1000)≈6.908 (a 3-order-of-magnitude ratio) centered at the cohort geometric mean, guaranteeing an invariant exchange rate across rankings and releases.

Low

Notation collision for hallucination rate h across Parts 7 and 9

Issue: Part 7 defines h as the conditional hallucination rate ("incorrect ÷ non-correct"), while Part 9 redefines h as the unconditional incorrect rate ("h = its hallucination rate × (1 − a)").

Why it hurts the objective: While the variance derivation in Part 9 is mathematically correct, reusing the scalar symbol h with conflicting definitions creates confusion for auditors.

Concrete recommendation: Adopt distinct notation in Part 9 (e.g. let 
𝑤
=
ℎ
⋅
(
1
−
𝑎
)
w=h⋅(1−a) represent the unconditional incorrect rate).

Redundant specification of AA-LCR under drift flag exclusions

Issue: Part 7 states: "non-discriminating leaves excluded from B*: AA-LCR v1.1 and AA-LCR v1.1 respectively".