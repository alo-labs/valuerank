0. Read check

Part 7:

First line: - **Scoring with frozen, per-basis anchors** in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); **anchor object (E20)**, identified by anchor version, basis and workload hash (the hash covers the workload's component set only, so two rankings' workloads with the same components share a hash but are different anchor objects with different references and anchors, and equal hashes imply no comparability across rankings): reference configuration ids and frozen costs, the references chosen by the registered **anchor-panel policy (E160)** — distinct from workload admission even where it coincides: the ranked configurations with complete cost evidence (exact cost, no AA missing- or declined-task marker) on every component of the workload at the freeze cutoff (on the main workload, the admission reference panel), on the Plan basis the plan rows of the same configurations whose displayed Plan cost is measured (a controlled measurement or concordant reports; owner decision O157, 2026-11-01, on reviewer 78, amending E160 and E253): owner assumptions and API-cost fallbacks are scored on those anchors and flagged (O13, O16) but are outside the Plan clip-gate population (scores.json gates.clip.plan[].outsideGate), because API fallbacks cost an order of magnitude more than plan routes and, as references, had stretched the Plan anchor range until every measured row sat in a narrow band of cost scores (at r160 the max-effort Plan high anchor was twice one API fallback; the O12 dual run against the r160 anchors is published in data/v3_dual_run*.json, anchor version v3-2026-11-01-a3); at least two references, otherwise that workload's anchors are unavailable and its configurations get no cost score (the main workload must meet the minimum, or freezing fails); **anchor availability after the valuation gate (E184)**: a reference must also pass the valuation-basis gate (E170 outcome 1 or 2) at its freeze; a frozen anchor object keeps its references when one later fails the gate (as with any evidence lost after freezing), and a new freeze leaves out a row whose AA cost omits a pricing term (O94); a subset workload left with fewer than two eligible references takes the unavailable state above; and a main-workload migration whose new workload would have fewer than two eligible references is deferred — the release publishes on the current anchor version and admitted set, the component that would have been admitted stays pending with the reason "anchor migration unavailable — insufficient valuation-eligible references", and the release is not held (O29), because anchors from the old workload are never relabelled for a new one; a workload migration is atomic across bases — both bases share the workload object and E160's reference configurations (the Plan references are the measured plan rows of the same configurations, O48, O157); because O157 needs at least two measured plan rows, the two bases' availability can differ, so the migration requires both, at least two complete-evidence API references and at least two measured Plan references on the main workload, and otherwise the freeze stops and the previous anchor objects stay in force for both bases (E304, on reviewer 80; fixtures: two API references with one measured Plan reference, and with none, each stopping the freeze); the shared eligibility is complete cost evidence on every component, an E170 outcome of 1 or 2 for the configuration's AA cost and, from the next freeze, no O94 pricing omission, and the selected Plan evidence's own valuation status (E138) governs Plan interval eligibility, never anchor eligibility, because E160's Plan anchors are the measured plan rows (O157), and the rows they do not cover are scored on them, flagged and outside the clip gate; each freeze publishes a row-level anchor-eligibility table (complete evidence, valuation-gate outcome, eligibility and exclusion reason); the first freeze of a new methodology version that cannot anchor its main workload is not released and the previous version's release stays live (a versioned migration completes only with its anchors, O12), while a subset workload takes the unavailable state; fixtures: a superseded row inside a frozen anchor panel leaves the anchor unchanged; a freeze excludes superseded and unverified rows; a deferred migration keeps the prior workload and lists the pending component; a first freeze short of references is refused; IDs and costs stay frozen, evidence lost after freezing never rebuilds an anchor, and any population or rule change is a new anchor version with an old/new bridge (fixtures: reordered input rows give identical anchors; an unresolved component removes a row from the population; a subset workload below the minimum leaves its rows unscored without disturbing the main gates); c_L = min reference cost ÷ 2 and c_H = max reference cost × 2 (a fixed ln 2 log padding, so the reference cohort itself never clips); units; expected clipping (none for the reference cohort). A first-release fixture on the actual reference cohort must pass without re-anchoring. Dollars always displayed; unclipped values kept. **Clip gate (single governing gate)**: per basis and anchor object, hold the release (O12) when more than max(1, 10% of n) rows clip, where n is the number of ranked rows scored on that anchor object (ranked rows on its workload with a positive cost on that basis; a subset workload is gated on its own anchor object), or when any such ranked row lies beyond an anchor by more than a factor of 2. **Listed rows beyond the anchors (O58)**: a listed configuration (E259) is not in the gate's population and never holds a release, because it has no rank and no label; the gate output discloses each listed row whose cost lies outside its workload's anchors, with its basis, side, factor, whether it passes the factor-2 limit, and whether it is a point on AA's rendered frontier (the E197 entrant case, now visible rather than held). Today, in the max-effort ranking, API: GPT-6 Luna (low) 7.10 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (medium) 1.54 below the low anchor (rendered-frontier point); Claude Haiku 5.5 (low) 1.53 below the low anchor (rendered-frontier point); Plan: Claude Haiku 5.5 (low) 70.65 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (low) 59.81 below the low anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (medium) 38.91 below the low anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (high) 24.11 below the low anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (xhigh) 15.85 below the low anchor (past the factor-2 limit); GPT-6 Luna (medium) 13.01 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (high) 8.36 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (xhigh) 6.22 below the low anchor (past the factor-2 limit); Gemini 4 Carbon (high) 4.74 above the high anchor (rendered-frontier point, past the factor-2 limit); GPT-6.1 Terra (low) 4.27 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6.1 Terra (medium) 2.40 below the low anchor (rendered-frontier point, past the factor-2 limit); Kimi K3.1 Pro (max) 2.24 above the high anchor (past the factor-2 limit); GPT-6.1 Sol (low) 2.13 below the low anchor (past the factor-2 limit); GPT-6.1 Terra (high) 1.76 below the low anchor (rendered-frontier point); Claude Opus 5.5 (medium) 1.39 below the low anchor; GPT-6.1 Sol (medium) 1.32 below the low anchor (rendered-frontier point); GPT-6.1 Terra (xhigh) 1.31 below the low anchor; Claude Opus 5.5 (high) 1.05 below the low anchor. In the AI Coding Daily ranking, API: GPT-6 Luna (low) 2.30 below the low anchor (rendered-frontier point, past the factor-2 limit); Plan: Claude Haiku 5.5 (low) 16.58 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (low) 14.03 below the low anchor (rendered-frontier point, past the factor-2 limit); Gemini 4 Carbon (high) 8.17 above the high anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (xhigh) 3.72 below the low anchor (past the factor-2 limit); Claude Haiku 5.5 (max) 2.25 below the low anchor (past the factor-2 limit); GPT-6.1 Terra (low) 1.06 below the low anchor (rendered-frontier point). **Gate scope (E262)**: every gate runs per ranking on that ranking's own anchor objects and rows; both rankings publish together, so a hold in either holds the release, and the release record names the held rankings (scores.json releaseHold). **A held release (E200)** is still built. Its manifest names each clipped row, including a frontier entrant, with its unclipped cost and score and the flag "off-anchor scale, release held", and the entrant stays in the reconciliation inventory. That output is published with the dual run that clears the hold. **Re-anchoring path (E197)**: the gate's remedy is pre-built. Anchors stay over a ranking's ranked rows (listed rows are disclosed, O58); a newly ranked row beyond them that holds the gate is cleared only by the O12 versioned re-freeze with its dual run, and the gate output names that remedy (owner decision O120, 2026-10-29). The freeze command re-freezes on the release's evidence, and the dual-run command scores that same evidence on the previous and the new anchor objects. It publishes each row's cost score, value and rank under both, and each bar's result under both bar objects (O12), so a cheaper entrant beyond the low anchor can clear the gate within one release cycle as a versioned migration. **Re-freeze at the moved cutoff (owner decision O47, E247, E253)**: AA published FrontierCode results after the 2026-10-21 cutoff, and the owner chose "Move cutoff now": the release cutoff moved to that day's new capture instant, every AA source was re-captured and the anchors were re-frozen. No dual run was possible, because the main workload changed (Coding Agent Index v1 left the basket when AA replaced it with v2.0), so this is a workload migration (E184) and the engine refuses to score on the previous anchors; the previous anchor object is kept as v3-frozen-2026-10-21-before-o47.json. **AA data after the cutoff (owner decision O65, 2026-10-25)**: AA data read after the release cutoff is never merged into a pinned capture; it moves the cutoff, every AA source is re-captured and the anchors are re-frozen. On 2026-10-25 this moved the cutoff from 2026-10-23T06:26:23Z (the safety-refusal counts of O63 had been read later that day) to the new capture instant; the re-capture added Kimi K3.1 Pro as a rendered-frontier vertex. Because the main workload of each ranking did not change, a dual run on the previous and the new anchors was possible and is published (data/v3_dual_run.json, data/v3_dual_run_aicd.json; the previous objects are kept as v3-frozen-2026-10-23-before-o65.json and v3-frozen-aicd-2026-10-23-before-o65.json). **Board re-read (owner decision O68, 2026-10-25)**: with the cutoff moved, every board either ranking uses was re-read (Vals' two boards, AI Coding Daily with its hidden older rows, Bug Hunt Bench's scoreboard and LiveBench 2.0's 2026-10-23 release in full; tbench.ai's Terminal-Bench 4.0 leaderboard and Cognition's FrontierCode board re-read and found unchanged, so their 2026-10-23 captures stand), each kept only when its own last update predates the cutoff's day (O60); every reviewed match is kept, the build stops if a matched row vanished or changed effort, and on 2026-10-25 the only changes were Kimi K3.1 Pro's new rows and LiveBench's new release (research/2026-10-25-board-reread/). **Re-capture under Intelligence Index v5 (owner decision O132, 2026-10-30)**: AA published Intelligence Index v5.0 around 2026-10-27, after the 2026-10-25 cutoff, and the owner chose to re-capture under v5 now: under O65 the cutoff moved to 2026-11-01T06:10:00Z, every AA source was re-captured (the chart at 2026-11-01T05:53:05Z), the leaves were mapped to their v5 successors (O136) and the basket re-decided (O137), and every ranking's anchors were re-frozen on the v5 cohort (anchor versions below). As at O47, the main workload of each ranking changed (GDPval-AA, SciCode and AA-LCR left the basket; FrontierCode 2.0 and Terminal-Bench-Science joined it), so this is a workload migration (E184) with no dual run on the previous anchors; the previous anchor objects are kept in research/2026-10-30-v5-recapture/previous-anchors/, and the published dual-run files still describe the O65 move of 2026-10-25. Every board was re-read on 2026-11-01 for the 37-configuration cohort (O68, O145; research/2026-11-01-recapture/third-party/), and earlier on 2026-10-30 (research/2026-10-30-v5-recapture/third-party/): LiveBench had withdrawn its 2026-10-23 release, so its 2026-10-25 release is pinned (O139); Vals, Bug Hunt and AI Coding Daily added GPT-6.1 Terra rows (Vals also Gemini 4 Carbon) and changed no other cohort value; tbench.ai was unchanged; and no board row is dated after the v5 chart capture. E247's freeze at O47 over the 29-configuration cohort (anchor version v3-2026-10-23, API 4.19 to 12,078 USD on 27 references at O47) was replaced before any release by one frozen object per ranking (E253): the max-effort ranking's version string is v3-2026-11-01-a3 and the AI Coding Daily ranking's is v3-2026-11-01-a3-aicd, each padded (c_L = cheapest reference ÷ 2, c_H = dearest × 2) per workload and basis, with every anchor object's references and anchors in scores.json workloads`. Today a cost doubling is worth 3.11 value points (offset by 4.14 quality points) on the max-effort API basis and 5.31 (7.08) on its Plan basis, and 2.71 (3.61) on the AI Coding Daily API basis and 4.11 (5.48) on its Plan basis.

Last 12 words: AI Coding Daily (judged code quality on existing Laravel and React-TS repositories plus edge-case testing over six graded projects; the 10-point bug-finding column is excluded because it overlaps Bug Hunt; harness chosen per model and named on each record: Claude Code, Codex CLI, OpenCode, Devin or DeepSeek's harness; a configuration the board lists twice takes the row selected as in the added-leaves bullet) | — | 10% | — | points of 60; z = 100 × points / 60 |

Part 8:

First line: | General professional work (20%) | GDPval-AA v2.1 (Elo as displayed on AA's model page at the capture; E90, O70) | 10% | 10% | 10% | z = 100 × clip((E − 500)/2000, 0, 1) (AA's published integration transform "clamp((Elo − 500) / 2000)", artificialanalysis.ai/methodology/intelligence-benchmarking, verified 2026-10-19 (E129)); specification-layer sensitivity (E181): logistic win probability against AA's pinned scale anchor, z = 100 / (1 + 10^((E_A − E)/400)) with E_A = 1600 (DeepSeek V4.1 Flash (max), AA's anchor, pinned on 2026-10-19 from AA's methodology page; a change of AA's anchor is a versioned re-pinning, not a silent move) and the conventional Elo scale of 400 points per tenfold odds (AA does not state its scale factor), published as rank changes on the common panel with every other input fixed |

Last 12 words: bounds in the identification layer); repetitions are not a bias.

Part 9:

First line: ## Uncertainty (three separate layers, one scenario engine)

Last 12 words: result is not described as target-workload support.

All listed parts were successfully read to their end via the GitHub connector.

1. Findings by severity
Critical

None

High

None

Medium

M1. Bug Hunt Bench unbounded z score introduces unstandardized leverage into the quality composite

Issue: In Part 7, under O163 and E302, Bug Hunt Bench is evaluated as 
𝑥
=
planted fixed (out of 105)
+
genuine unplanted fixed
x=planted fixed (out of 105)+genuine unplanted fixed, and normalized as 
𝑧
=
𝑥
z=x directly with no scaling factor and no upper ceiling (anchors 
0
0 to 
∞
∞, with sample fixtures reaching 
109.6
109.6). In contrast, all other quality leaves are strictly normalized to a 
0
–
100
0–100 scale (
𝑧
∈
[
0
,
100
]
z∈[0,100]).

Why it hurts the objective: ValueRank's composite quality score relies on pre-allocated weights totaling 100 points (
𝑄
=
∑
𝑤
𝑖
𝑧
𝑖
Q=∑w
i
	​

z
i
	​

). When one leaf has an open-ended support 
[
0
,
∞
)
[0,∞) where 
𝑧
z can exceed 100 by an arbitrary amount depending on repository bug density, its nominal weight (8% in max-effort, 12% in AI Coding Daily, 15% in common-leaf) no longer represents its maximum contribution to 
𝑄
Q. A model finding 100 unplanted bugs alongside 40 planted bugs would contribute 
140
×
0.15
=
21.0
140×0.15=21.0 points from a 15% leaf, distorting the intended 60/20/10/10 domain weighting and inflating the realized influence of Bug Hunt relative to bounded leaves like FrontierCode or Terminal-Bench.

Concrete change: Rescale 
𝑧
z by dividing 
𝑥
x by a stable reference denominator or upper benchmark capacity (e.g., 
𝑧
=
100
×
planted
+
unplanted
105
+
𝑢
ˉ
max
⁡
z=100×
105+
u
ˉ
max
	​

planted+unplanted
	​

 or capping at 100 with clipping audit disclosure), or map unplanted bugs via a saturating concave function so that exceptional open-ended bug counts cannot expand a leaf's effective nominal share beyond its assigned budget.

M2. Asymmetric error propagation in S1T Jeffreys Beta sampling for partial and judged scoring leaves

Issue: In Part 9, S1T uses a plug-in binomial Jeffreys Beta posterior 
Beta
(
𝑘
+
1
/
2
,
𝑛
−
𝑘
+
1
/
2
)
Beta(k+1/2,n−k+1/2) for leaves whose per-task scores are continuous or partial in 
[
0
,
1
]
[0,1] (e.g., AutomationBench partial scores, FrontierCode rubric/tests, and AI Coding Daily judged points with 
𝑛
=
6
n=6), justifying this because 
𝑝
(
1
−
𝑝
)
p(1−p) is an upper bound on variance. However, treating a mean of non-binary bounded random variables as a pseudo-binomial count 
𝑘
=
𝑛
⋅
𝑝
k=n⋅p and sampling from a Beta distribution imposes artificial skewness near boundaries (0% and 100%) that does not match the actual sum of continuous partial scores or project rubrics.

Why it hurts the objective: On AI Coding Daily with 
𝑛
=
6
n=6 projects, drawing 
Beta
(
6
𝑝
+
0.5
,
6
(
1
−
𝑝
)
+
0.5
)
Beta(6p+0.5,6(1−p)+0.5) induces massive variance and substantial mean-shifts near the endpoints (as acknowledged in E303), distorting separability thresholds and ranking noise bands.

Concrete change: For non-binary bounded task scores where individual task variance 
𝜎
2
≤
𝑝
(
1
−
𝑝
)
σ
2
≤p(1−p), use a truncated/clipped normal or a scaled logit-normal with mean-matching and conservative variance scaling, rather than imposing a discrete binomial Beta conjugate posterior that structurally shifts the mean.

Low

L1. Ambiguity in AI Coding Daily tie-breaking when Bug Hunt harness name is absent or unmatched

Issue: In Part 8 (E268), when AI Coding Daily lists a model multiple times, the rule selects the row whose harness matches Bug Hunt's harness; if none matches or multiple match, it selects the row with the latest test date, and stops the build if a tie remains. For newer models evaluated on custom harnesses or third-party wrappers, Bug Hunt and AI Coding Daily harnesses frequently share no common naming scheme (e.g., vendor CLI vs. OpenCode/Devin).

Why it hurts the objective: While the rule includes a fallback to the latest test date, it relies on exact case-insensitive string matching of harness names before route delimiters, which may fail on trivial formatting discrepancies (e.g., claude-code vs Claude Code CLI).

Concrete change: Require an explicit normalized harness alias table in data/swe_tracks.json rather than ad-hoc string equality before falling back to test date.

2. Methodology design recommendations

Standardize Bug Hunt composite normalization

Design: Define Bug Hunt's normalization as:

𝑧
=
100
×
𝑥
planted
+
𝑥
unplanted
𝑁
planted
z=100×
N
planted
	​

x
planted
	​

+x
unplanted
	​

	​


with an explicit soft saturation or standard anchor 
𝑎
high
=
105
+
𝑢
anchor
a
high
	​

=105+u
anchor
	​

 (where 
𝑢
anchor
u
anchor
	​

 is frozen across the methodology version, similar to cost anchors). This guarantees that Bug Hunt conforms to the standard anchor framework (
𝑎
low
=
0
,
𝑎
high
a
low
	​

=0,a
high
	​

 documented), preventing variance explosion and preserving the nominal 60% software-engineering domain budget.

Refine S1T project-level uncertainty for AI Coding Daily

Design: Until per-project points are captured directly (as noted in Part 9), replace the 
𝑛
=
6
n=6 pseudo-binomial Beta draw with a moment-matched truncated normal draw:

𝑧
∼
𝑁
(
𝑧
0
,
𝑧
0
(
100
−
𝑧
0
)
𝑛
eff
)
clipped to 
[
0
,
100
]
z∼N(z
0
	​

,
n
eff
	​

z
0
	​

(100−z
0
	​

)
	​

)clipped to [0,100]

where 
𝑛
eff
∈
[
6
,
60
]
n
eff
	​

∈[6,60] is calibrated against the empirical variance observed on comparable multi-project evaluation suites (such as Vals or RepoBench).

3. Questions for the owner

None

4. Verdict

VERDICT: HAS FEEDBACK