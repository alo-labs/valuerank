0. Read check
Part 7: research/2026-10-19-methodology-codesign/perplexity/parts-r175/draft-r175-part-7-of-14.md

First line: - **MiMo quota ceiling (owner decision O46)**: Xiaomi prices MiMo Token Plan credits at parity with its pay-as-you-go API (100M credits = ¥1), and the owner-requested research (Claude's deep-research skill with three researchers, and Perplexity Search with GPT-6.1 Sol, Grok 4.7 and Gemini 3.8 Flash; Silver Bullet's multi-model workflow could not run without provider credentials; record research/2026-10-23-mimo-token-plans/) found no end-user measurement of a MiMo-V2.6 billing period.

Last 12 words: marked **non-discriminating** (still scored and reported, excluded from drift-flag counting). AA Intelligence Index and output speed are diagnostics, not quality.

Part 8: research/2026-10-19-methodology-codesign/perplexity/parts-r175/draft-r175-part-8-of-14.md

First line: **Leaf sets per ranking (owner decisions O49, O52–O55, O61)**: AA withdrew DeepSWE v1.1 from its Coding Agent Index, and the owner dropped it in favour of FrontierCode (O49), which left ten common leaves: FrontierCode 25%, Terminal-Bench 4.0 20%, Bug Hunt Bench 15% and the seven leaves outside software engineering.

Last 12 words: reconciled (as a bias bound in the identification layer); repetitions are not a bias.

Part 9: research/2026-10-19-methodology-codesign/perplexity/parts-r175/draft-r175-part-9-of-14.md

First line: ## Uncertainty (three separate layers, one scenario engine)

Last 12 words: separable\" and its S0 result is not described as target-workload support.

1. Findings by severity
Critical

None.

High
H-1: Bug Hunt unscaled metric creates unconstrained composite distortion

Issue: Under O163 and the quality leaf table in Part 8, Bug Hunt Bench is defined as 
𝑥
=
planted
+
genuine unplanted fixes
x=planted+genuine unplanted fixes, with 
𝑧
=
𝑥
z=x directly without rescaling or upper ceiling, explicitly allowing 
𝑧
>
100
z>100 (e.g., fixture notes 
44.3
+
65.3
→
109.6
44.3+65.3→109.6). Meanwhile, all other 10 to 12 leaves are normalized via 
𝑧
=
100
×
clip
(
(
𝑥
−
𝑎
low
)
/
(
𝑎
high
−
𝑎
low
)
,
0
,
1
)
z=100×clip((x−a
low
	​

)/(a
high
	​

−a
low
	​

),0,1) strictly to 
[
0
,
100
]
[0,100].

Why it hurts the objective: Quality 
𝑄
Q is defined as a convex combination 
∑
𝑤
𝑖
𝑧
𝑖
∑w
i
	​

z
i
	​

 with nominal weights summing to 100%. When a single leaf can scale well past 100 without an upper bound, its effective marginal contribution to 
𝑄
Q exceeds its nominal weight allocation (8%, 12%, or 15%), diluting the owner's explicit 60/20/10/10 domain weighting and violating the cardinal interpretability of the composite score 
𝑄
∈
[
0
,
100
]
Q∈[0,100]. Models that encounter noisy "unplanted" bug opportunities gain an unbounded point bonus compared to fixed-task benchmarks.

Recommended change: Rescale Bug Hunt to 
[
0
,
100
]
[0,100] using a documented empirical saturation anchor (e.g., 
𝑎
high
=
105
+
𝑢
max
⁡
a
high
	​

=105+u
max
	​

 or setting 
𝑎
high
=
150
a
high
	​

=150 frozen as a methodology version parameter, with soft clipping or ceiling tracking), or standardize its normalization alongside all other leaves.

Medium
M-1: Bug Hunt single-run noise kernel injects variance into multi-run means in S1T

Issue: In Part 9, S1T models Bug Hunt Bench variance using a single-run dispersion formula: 
SD
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
𝑢
SD=
105
p
~
	​

(1−
p
~
	​

)+u
	​

, where 
𝑢
u is treated as a Poisson count floored at 0.5. The text explicitly states: "this is a single-run dispersion approximation, not the uncertainty of the published multi-run mean, which would need the board's per-run paired counts and is not divided by the run count, since repeated runs share their tasks and repositories (E326)".

Why it hurts the objective: The published score used in the composite is the mean of 
𝑁
N runs (where 
𝑁
N is documented and tracked, E206). Treating the estimator's sampling error as a single-run dispersion without dividing by 
𝑁
N
	​

 (or an empirical clustered effective sample size) heavily overstates the estimation variance of models with large sample sizes relative to single-run benchmarks. This artificially expands S1T noise bands and depresses rank separability.

Recommended change: While shared tasks and repositories introduce intraclass correlation (
𝜌
>
0
ρ>0), assuming complete zero variance reduction (
𝜌
=
1
ρ=1) is an overly conservative extreme. Model the variance of the published mean using an effective sample size divisor:

Var
(
𝑥
ˉ
)
=
𝜎
single
2
𝑁
eff
,
where 
𝑁
eff
=
𝑁
1
+
(
𝑁
−
1
)
𝜌
repo
Var(
x
ˉ
)=
N
eff
	​

σ
single
2
	​

	​

,where N
eff
	​

=
1+(N−1)ρ
repo
	​

N
	​


Set 
𝜌
repo
=
0.5
ρ
repo
	​

=0.5 as a registered default or publish the empirical per-run standard error when individual run logs are captured.

M-2: Missing continuity mechanism between AA Intelligence Index v4 and v5 migrations

Issue: Part 7 notes that when AA released Intelligence Index v5.0, GDPval-AA, SciCode, and AA-LCR left the basket, while FrontierCode 2.0 and Terminal-Bench-Science joined. Because the main workload changed, E184 triggered a workload migration where dual runs on previous anchors were refused. The text notes: "anchor versions below... As at O47, the main workload of each ranking changed... with no dual run on the previous anchors... and the published dual-run files still describe the O65 move of 2026-10-25".

Why it hurts the objective: ValueRank aims to track public frontier AI models with defensible longitudinal stability. Refusing a bridge or dual run during major benchmark version shifts prevents consumers from distinguishing genuine frontier efficiency improvements from benchmark basket re-basing.

Recommended change: Require a synthetic bridge artifact whenever a workload changes: score the intersection cohort on both the retiring basket (using frozen pre-migration anchors) and the new basket (using newly frozen anchors) at the transition instant, publishing an empirical level-shift diagnostic 
Δ
𝑉
=
𝑉
new
−
𝑉
old
ΔV=V
new
	​

−V
old
	​

.

Low
L-1: Clopper–Pearson sequential looks do not form a true martingale confidence sequence

Issue: In Part 9 (E77), sequential Monte Carlo looks evaluate an exact Clopper–Pearson interval with per-look Bonferroni error allocation 
𝛿
=
0.05
/
16
δ=0.05/16 across 16 fixed batch looks (
𝑁
=
10
,
000
…
160
,
000
N=10,000…160,000). The text acknowledges this is "not an anytime-valid confidence sequence".

Why it hurts the objective: While union-bounding across a pre-registered grid of 16 discrete sample sizes is mathematically valid for that discrete grid, it incurs conservative efficiency loss compared to modern anytime-valid confidence sequences (e.g., betting or mixture martingales) and leaves interim inspections vulnerable to misinterpretation.

Recommended change: Adopt a standard mixture martingale or Robbins-type anytime-valid boundary for the sequential Monte Carlo gate, which guarantees valid sequential stopping at any 
𝑁
N without arbitrary look-count caps.

2. Methodology design recommendations

Bug Hunt Normalization and Noise Standardization:

Anchor Bug Hunt with a frozen baseline:

𝑧
BH
=
100
×
clip
(
𝑥
planted
+
𝑥
unplanted
𝑎
high
,
0
,
1
)
z
BH
	​

=100×clip(
a
high
	​

x
planted
	​

+x
unplanted
	​

	​

,0,1)

where 
𝑎
high
=
105
+
𝑢
ˉ
95
a
high
	​

=105+
u
ˉ
95
	​

 (e.g., 150 points). This prevents unplanted defect discovery from distorting the 60% software engineering budget.

Adjust the S1T variance by accounting for the published run count 
𝑁
N:

SD
(
𝑥
ˉ
)
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
𝑢
max
⁡
(
1
,
𝑁
)
SD(
x
ˉ
)=
max(1,N)
105
p
~
	​

(1−
p
~
	​

)+u
	​

	​


accompanied by the correlation stress test already implemented in E309.

Workload Transition Continuity Protocol:

In Part 7, whenever AA upgrades its suite (e.g., v4 
→
→ v5), mandate an automated "bridge snapshot":

Evaluate the transition cohort simultaneously on the legacy basket 
𝑊
𝑡
−
1
W
t−1
	​

 and the successor basket 
𝑊
𝑡
W
t
	​

.

Calculate the rank concordance (
𝜏
𝑏
τ
b
	​

) and average value delta (
𝐸
[
𝑉
𝑡
−
𝑉
𝑡
−
1
]
E[V
t
	​

−V
t−1
	​

]).

Publish this in data/migrations/ so external users can track price-performance trendlines across benchmark generations.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK