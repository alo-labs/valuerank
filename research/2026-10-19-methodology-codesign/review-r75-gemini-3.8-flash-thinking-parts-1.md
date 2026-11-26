0. Read check
Part 1

First line: # ValueRank methodology — draft r157

Last 12 words: carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py).

Part 2

First line: - **Full benchmark set (owner decisions O36, O38)**: a cohort configuration is ranked in a ranking only when it has every leaf of that ranking for the exact configuration, so every row of a ranking is scored on the same benchmarks at that ranking's owner-set weights (O55, as amended for the max-effort ranking by O61).

Last 12 words: or provider declined some tasks on safety grounds\") also flags \"partial component\".

Part 3

First line: - **Capture status (per ranking, E254).** Coding share (E200): the published summary prints, beside the basket label, the share of basket cost carried by coding and terminal tasks (the Coding Agent Index where admitted, Terminal-Bench 4.0 and FrontierCode 2.0), with its median and range over the full-basket configurations (scores.json diagnostics.basketReadiness for each); it is far higher in a ranking that admits the Coding Agent Index.

Last 12 words: on the Plan basis the workload question is the M_W identification status.

1. Findings by severity
Critical

None

High

Issue: Under E209 and E37, CompleteCostEvidence requires that the sum of AA's nine published v5 evaluation costs reconstructs AA's published total Index cost at a relative error tolerance of at most 
10
−
6
10
−6
. Because all three Claude Opus 5.5 rows miss this exact sum by 0.03%–0.04% (3 to 4 basis points), all six of their Index SDLC components are marked "unresolved", stripping FullCost status and locking Claude Opus 5.5 out of interval outputs and anchor reference panels.

Why it hurts the objective: ValueRank exists to determine which frontier model delivers the lowest cost for practical value. In the leading max-effort ranking, there are only 5 cohort configurations. Disqualifying a premier frontier configuration like Claude Opus 5.5 (max) from interval claims (frontier membership and cheapest-above-bar status) due to a 0.03% discrepancy—worth less than 0.01 value points—undermines the validity of the published frontier. Web-scraped aggregations across 5,156 tasks naturally carry minor floating-point or intermediate display rounding.

Concrete change: Amend E209 to set the relative error threshold for Index total reconstruction to 
5
×
10
−
4
5×10
−4
 (0.05%), or classify a residual under 0.1% as "reconciled with minor precision residual," preserving CompleteCostEvidence and FullCost while adding the 
±
0.04
%
±0.04% residual interval to the row's cost envelope in interval checks.

Issue: Following the retirement of O116 (FrontierCode chart total stand-in) under O137, the AI Coding Daily ranking admits only the six general Index SDLC evaluations (Briefcase, AutomationBench, GDP.pdf, Terminal-Bench, FrontierCode 2.0, Terminal-Bench-Science) because Coding Agent Index v2.0 is priced on only 5 of 15 configurations and misses the two-thirds threshold.

Why it hurts the objective: AI Coding Daily weights software engineering at 60% of quality, but its cost workload contains no multi-turn agentic coding benchmark. The cost basket is dominated by general office, PDF, and QA tasks (AutomationBench, Briefcase, GDP.pdf), resulting in a severe inverted value-variance cost allocation of -99% on API. The ranking measures coding on quality while pricing office administration on cost.

Concrete change: Permit a versioned coding-agent proxy stand-in for rankings where Coding Agent Index v2.0 is pending, or establish a dedicated coding-cost companion index that reports value scores on coding-only workloads alongside the general basket.

Medium

Issue: In the max-effort ranking (5 configurations), the frozen quality bars sit at 63.7 (lower quartile), 65.2 (headline median), and 66.2 (upper quartile), giving an interquartile range of only 2.5 points. Under O44, each bar requires a noise-margin companion cleared by a fixed 4.5 quality points.

Why it hurts the objective: The fixed 4.5-point noise margin exceeds the entire interquartile spread of the cohort. To qualify for the headline companion, a configuration must reach 
65.2
+
4.5
=
69.7
65.2+4.5=69.7, and for the upper quartile 
66.2
+
4.5
=
70.7
66.2+4.5=70.7, both of which exceed the maximum displayed quality across the entire cohort. The companion label collapses to unachievable by construction.

Concrete change: Scale the noise margin dynamically to the ranking's analytic quality standard error (e.g., 
1.96
×
SE
𝑄
1.96×SE
Q
	​

), or specify that when a bar level plus the margin exceeds the cohort maximum, the companion field explicitly publishes "unachievable in current cohort" rather than evaluating empty sets.

Issue (Owner decision challenge): Under O123, vendor agent tokens from the Coding Agent Index are charged to model API cost without measuring agent quality contributions, and the S2 stress model 
log
⁡
𝐶
(
𝑚
,
𝑎
)
=
𝛼
𝑚
+
ℎ
𝑎
logC(m,a)=α
m
	​

+h
a
	​

 is mathematically unidentifiable because no model is evaluated across multiple vendor agents.

Why it hurts the objective: Models evaluated in heavier scaffolding (such as Claude Code or Codex) absorb structural cost penalties that are not separated from model efficiency. Because the diagnostic stress is permanently collinear and unevaluable, the methodology acknowledges an uncorrected cost distortion.

Concrete change: Condition the inclusion of agent-scaffolded costs on identical harness baselines, or bound the agent token overhead using public prompt/completion ratios before pooling into 
𝐶
𝑖
,
𝑊
C
i,W
	​

.

Low

Issue: In Part 3 under "Matched-cost diagnostic", the text states: "B may include any leaf with exact-variant per-task cost (AA per-evaluation costs, FrontierCode, Terminal-Bench)", but the canonical family set is formally defined as 
𝐺
G (
𝐶
𝑖
match
=
∑
𝑔
∈
𝐺
𝜔
𝑔
𝑃
𝑖
𝑔
C
i
match
	​

=∑
g∈G
	​

ω
g
	​

P
ig
	​

) and the diagnostic object is 
𝐷
=
(
𝐺
,
…
 
)
D=(G,…).

Why it hurts the objective: The symbol 
𝐵
B is an undefined orphan notation left from an earlier revision, creating ambiguity in diagnostic specification.

Concrete change: Replace "B may include..." with "The execution family set G may include...".

Issue: In Part 1 under "Cohort and configuration", the text reads: "Today 1 configurations are in both (GPT-6 Luna (max)), so 19 of the 27 are ranked at least once."

Why it hurts the objective: Grammatical singular-plural disagreement in normative text.

Concrete change: Change "Today 1 configurations" to "Today 1 configuration".

2. Methodology design recommendations

Reconciliation tolerance calibration for upstream totals (E209): Replace the absolute 
10
−
6
10
−6
 relative error bound with a tiered check:

Relative Error
=
∣
∑
𝑒
𝐶
𝑖
𝑒
−
𝐶
𝑖
,
Index
∣
𝐶
𝑖
,
Index
Relative Error=
C
i,Index
	​

∣∑
e
	​

C
ie
	​

−C
i,Index
	​

∣
	​


If 
Relative Error
≤
10
−
6
Relative Error≤10
−6
, classify as confirmed complete. If 
10
−
6
<
Relative Error
≤
10
−
3
10
−6
<Relative Error≤10
−3
 (0.1%), classify as confirmed complete with precision residual, logging the residual 
Δ
𝐶
ΔC and incorporating 
[
𝐶
𝑖
,
𝑊
−
Δ
𝐶
,
𝐶
𝑖
,
𝑊
+
Δ
𝐶
]
[C
i,W
	​

−ΔC,C
i,W
	​

+ΔC] into interval outputs. This prevents trivial upstream rounding from disqualifying primary frontier models from FullCost status.

Adaptive noise margin for small cohorts (O44): Rather than pinning a static 4.5-point noise margin across all rankings, define the noise margin companion threshold as:

𝐻
𝑘
∗
=
𝐻
𝑘
+
max
⁡
(
1.96
⋅
median
(
SD
𝑄
)
,
min
⁡
(
4.5
,
IQR
𝑄
)
)
H
k
∗
	​

=H
k
	​

+max(1.96⋅median(SD
Q
	​

),min(4.5,IQR
Q
	​

))

In dense or compressed top-tier rankings like max-effort, this ensures the companion bar reflects genuine statistical separability without overshooting the empirical maximum of the cohort.

Harmonized software engineering cost weighting: For rankings where Coding Agent Index v2.0 is pending capture under E254 (such as AI Coding Daily), provide an explicit subset cost bridge or coding-only diagnostic value score that pairs the 60% coding quality group with the coding-specific subset (FrontierCode 2.0 and Terminal-Bench 4.0), preventing non-coding office tasks from dictating the cost rank.

3. Questions for the owner

Was the exclusion of Claude Opus 5.5 from FullCost and interval outputs intended as an explicit penalty for Artificial Analysis's 0.03% total discrepancy, or would you support relaxing the E209 reconciliation threshold to 0.05%?

For AI Coding Daily, where Coding Agent Index v2.0 is pending capture, should ValueRank publish a primary coding-cost view rather than scoring value against a general office and document processing basket?

4. Verdict

VERDICT: HAS FEEDBACK