0. Read check

research/2026-10-19-methodology-codesign/perplexity/parts-r175/draft-r175-part-1-of-14.md

First line: # ValueRank methodology — draft r175

Last 12 words: moved the release cutoff (O65) and re-captured every source.

research/2026-10-19-methodology-codesign/perplexity/parts-r175/draft-r175-part-2-of-14.md

First line: - **Two rankings (owner decisions O52, O53, O54)**: ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52).

Last 12 words: Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

research/2026-10-19-methodology-codesign/perplexity/parts-r175/draft-r175-part-3-of-14.md

First line: ## Cost (25% of the value score)

Last 12 words: cost per task, not AA's 7:2:1 blended price, not total Index cost.

1. Findings by severity
Critical

None

High
H1. Cohort definition contradiction between O51/O145 prose and the formal definition of cohort row

Issue: Under Cohort and configuration in Part 1, O51 and O145 define the cohort as all configurations plotted on or within the near gap of Artificial Analysis's (AA) rendered frontier, plus those retained for one release (totaling 37 configurations). Part 2 then explicitly defines: "a cohort row of a ranking is a cohort configuration ranked in it". Later in Part 2, the text states: "The cohort size 
𝑁
N of a ranking, counting every cohort row of it whether or not it carries a cost, is the denominator of its admission threshold 
⌈
2
𝑁
/
3
⌉
⌈2N/3⌉ (today 6 and 14)". For the max-effort ranking, there are 9 ranked configurations, and 
⌈
2
×
9
/
3
⌉
=
6
⌈2×9/3⌉=6. For AI Coding Daily, there are 20 ranked configurations, and 
⌈
2
×
20
/
3
⌉
=
14
⌈2×20/3⌉=14. However, in Part 1 and Part 2 prose, "cohort configurations" frequently refers to the global pool of 37 configurations, and Part 2 elsewhere says: "Today the max-effort ranking has 9 cohort rows, 9 scored rows and a bar population of 9..." while referring to excluded configurations as "cohort configurations without that ranking's full set (today 28 beside the max-effort ranking...)".

Why it hurts the objective: Calling both the global 37-configuration set and the ranking-specific ranked subset "cohort rows" introduces ambiguity into automated gates, audit scripts, and denominator checks for admission thresholds.

Recommended change: Strictly standardize terminology: define the global 37 configurations as Cohort Configurations (or Tracked Cohort), and define the ranking-specific set as Ranking Cohort Rows (or Ranked Candidates). Explicitly state in the Counts, defined once section that 
𝑁
N in 
⌈
2
𝑁
/
3
⌉
⌈2N/3⌉ refers to 
𝑁
ranked, track
N
ranked, track
	​

 (the number of cohort configurations possessing that ranking's full benchmark set), not the total tracked cohort of 37.

Medium
M1. Asymmetric treatment of vendor agent overheads between cost and quality

Issue: In Part 3 under Coding agent (owner decision O123), the Coding Agent Index v2.0 cost is measured using vendor agents (such as Claude Code and Codex), where agent orchestration and scaffold token overheads inflate the measured API token cost. However, the quality evaluations for FrontierCode 2.0 and Terminal-Bench 4.0 are measured on bare model runs by AA.

Why it hurts the objective: Models evaluated with token-heavy scaffolds in the Coding Agent Index suffer cost inflation without receiving credit for agent-enabled scaffold capabilities on the quality leaves. While O123 acknowledges this and registers an 
𝑆
2
S2 log-linear harness stress (log C(m, a) = α_m + h_a), the draft notes this stress is currently unevaluable because no model is listed under multiple agents.

Recommended change: Until multi-agent data exists to fit 
ℎ
𝑎
h
a
	​

, provide a bounded diagnostic sensitivity: compute headline cost and ranks when the Coding Agent Index component is re-weighted by the ratio of bare-model execution tokens to agent-execution tokens (or report ranks with Coding Agent Index excluded under E172 leave-one-component-out) to bound the scaffold distortion on the headline table.

M2. Ambiguity in the directional tolerance formula for clipped cost anchors

Issue: In Part 1 under Transfer tolerance (E242 / E272 / E305), the draft states: "an assumption row whose cost score is clipped at an anchor has zero slope there, but a large enough error in its multiple moves its cost back across the anchor, so its tolerance is directional: the factor by which the multiple must move in the one direction that can change its value... before the value moves by the median threshold". For a row already clipped at 
𝑐
𝐻
c
H
	​

 or 
𝑐
𝐿
c
L
	​

, any perturbation within the clipped zone causes 
Δ
𝑉
=
0
ΔV=0. The multiple must first shift cost from 
𝑐
𝑖
c
i
	​

 to the anchor 
𝑐
anchor
c
anchor
	​

, and then traverse an additional distance to induce 
Δ
𝑉
=
threshold
ΔV=threshold. The draft states the factor is 
2
threshold
/
exchange rate
2
threshold/exchange rate
 on the unclipped scale, but does not provide the exact closed-form boundary equation for the clipped regime.

Why it hurts the objective: Without the explicit formula incorporating 
ln
⁡
(
𝑐
𝑖
/
𝑐
anchor
)
ln(c
i
	​

/c
anchor
	​

), implementations cannot deterministically replicate diagnostics.rankSeparability.plan.clippedTolerance.

Recommended change: Provide the exact piecewise formula for directional tolerance:

Factor
clip
=
𝑐
anchor
𝑐
𝑖
×
2
threshold
points per doubling
Factor
clip
	​

=
c
i
	​

c
anchor
	​

	​

×2
points per doubling
threshold
	​


specifying the boundary conditions when 
𝑐
𝑖
≥
𝑐
𝐻
c
i
	​

≥c
H
	​

 versus 
𝑐
𝑖
≤
𝑐
𝐿
c
i
	​

≤c
L
	​

.

Low
L1. Potential circularity in open-web discovery date check

Issue: In Part 2 under Open-web discovery (E240), candidates found via open-web search must be resolved by a dated registry addition or a dated rejection. One rejection reason is "published after the cutoff". However, under O65, when new AA data is read after the cutoff, it moves the cutoff date itself.

Why it hurts the objective: If open-web discovery uncovers benchmark results published between the initial cutoff and the revised cutoff, the validity window shifts, potentially requiring re-evaluating previously rejected candidates.

Recommended change: Clarify in E240 that candidate rejection timestamps are evaluated strictly against the final, frozen publication cutoff timestamp 
𝑉
V established after all O65 recapture triggers have completed.

2. Methodology design recommendations

Formalize Piecewise Clipped Transfer Tolerance Formula (High Priority)
To eliminate implementation variance across independent runners, specify the exact piecewise directional tolerance factor for plan multiples 
𝑀
M when cost 
𝑐
𝑖
c
i
	​

 is clipped:

For an upper-clipped row (
𝑐
𝑖
>
𝑐
𝐻
c
i
	​

>c
H
	​

):

Tol
down
=
𝑐
𝑖
𝑐
𝐻
⋅
2
Δ
𝑉
med
points per doubling
Tol
down
	​

=
c
H
	​

c
i
	​

	​

⋅2
points per doubling
ΔV
med
	​

	​


representing the downward factor required to move value by the median separability threshold 
Δ
𝑉
med
ΔV
med
	​

.

For a lower-clipped row (
𝑐
𝑖
<
𝑐
𝐿
c
i
	​

<c
L
	​

):

Tol
up
=
𝑐
𝐿
𝑐
𝑖
⋅
2
Δ
𝑉
med
points per doubling
Tol
up
	​

=
c
i
	​

c
L
	​

	​

⋅2
points per doubling
ΔV
med
	​

	​


Decouple "Cohort" Nomenclature Across Pipeline Stages (Medium Priority)
Adopt explicit hierarchical labels in the definitions:

Tracked Catalog Cohort (
𝑁
catalog
=
37
N
catalog
	​

=37): Plotted frontier, near-gap, and O145-retained configurations.

Ranking Workload Cohort (
𝑁
rank
=
9
N
rank
	​

=9 or 
20
20): Configurations possessing 100% of the required leaves for that ranking.

Admitted Reference Panel (
∣
𝑃
𝐾
(
𝑊
)
∣
=
7
∣P
K
	​

(W)∣=7 or 
18
18): FullCost-verified subset used for anchor freezing.

3. Questions for the owner

For a Plan row whose cost is clipped at an anchor boundary (
𝑐
𝑖
>
𝑐
𝐻
c
i
	​

>c
H
	​

 or 
𝑐
𝑖
<
𝑐
𝐿
c
i
	​

<c
L
	​

), does the directional tolerance in scores.json measure the factor required to move the multiple from its current value until total value changes by the median threshold (absorbing the flat clipped zone first), or does it measure the distance starting strictly from the anchor boundary?

4. Verdict

VERDICT: HAS FEEDBACK