I'll review the draft against ValueRank's stated objective and check how the cited benchmarks, plan quotas, and cost fields actually work.
The cost-field definition looks inconsistent with current Artificial Analysis pages. I'll read those pages before treating that as a finding.
The draft does not yet answer its own objective. The headline still prices a different workload from the one it scores, and that gap is large enough to change who wins.

1. Findings by severity

Critical

The ranking cost is not the cost of the value being scored. The pinned input is AA’s total USD to run the Intelligence Index, and the cohort span of about $110–$8,700 matches that field: the comparison tool shows Claude Opus 5.5 (Max, Default Fallback) at $8,708 to run the index and GPT-6 Astra (Max) at $5,324. AA separately publishes weighted cost per Intelligence Index task — $5.98 and $3.26 for those same two configurations — and the live Pareto chart is “Intelligence Index vs. Cost per Task,” not total suite cost. Those series are not a rescaling. The implied task-equivalents are 8,708 / 5.98 ≈ 1,456 versus 5,324 / 3.26 ≈ 1,633, and the cost ratios differ (1.64× on the total bill, 1.83× per task). Total cost also excludes repeats. This is not a restatement of the rejected “the chart flipped” claim. Both fields exist. The 2026-10-17 capture can be real and still be the wrong price of the quality mix.
artificialanalysis
+2

It fails the objective because quality is 60% software engineering, of which DeepSWE (30%), FrontierCode (10%), and Bug Hunt (10%) are not Intelligence Index components. Index v4.3.2 is AA-Briefcase 15%, GDPval-AA 10%, AutomationBench-AA 5%, Terminal-Bench 4.0 10%, SciCode 10%, AA-LCR 5%, AA-Omniscience 15%, GDP.pdf 10%, HLE 10%, and CritPt 10%. The buyer is ranked on the token bill of a suite dominated by knowledge, science, and agent evals, including two expensive leaves (Briefcase, GDP.pdf) that ValueRank does not score. The Spearman cross-check only warns. It does not stop a mismatched cost from naming the winner.
artificialanalysis

Owner decision challenge (O5). Keep total suite USD as a versioned diagnostic. Make the ranking cost a quality-weighted mean of public per-evaluation cost per attempted task, same configuration, same price-list date. If O5 stands, still refuse a unique winner when the total-cost rank and the matched-cost rank differ by more than 3 places.

High

One quality vector cannot serve both buyers. Bug Hunt is one round on two TypeScript repos, 105 planted bugs, graded on the diff, in each vendor’s own CLI. That is the Plan product. It is not what an API buyer using a third-party agent gets. Terminal-Bench 4.0, as run by AA, is mini-swe-agent, pass@1 averaged over three repeats, with cost per task published. Putting that leaf in the “≈25% independent” bucket is false if the score is AA’s run, and the same number cannot be both an API-harness score and a Plan-stack score. A native-CLI gap can move 10% of quality against the buyer who never uses that CLI.
artificialanalysis
+2

Concrete change: split the quality weight vector by basis. API quality uses common-harness public scores only. Plan quality may keep Bug Hunt. Recalculate coverage per basis. Do not change O6’s 10% inside the Plan vector.

The Plan multiple is a scalar from the wrong meter. SemiAnalysis measures a separate subscription rate per plan, model, and token type, because credit-to-API ratios are not API price ratios and change with the model and the workload. Claude Code usage is also two stacked windows, a rolling five-hour limit and a weekly cap, shared across surfaces. Dividing an Intelligence Index bill by a Claude Code blended multiple prices a different token mix and can credit a weekly cap the five-hour window never lets the buyer reach. The draft records windows and categories, then still scores one multiple.
superblocks
+2

Concrete change, compatible with O3 and O7: a route is matched only if category-specific rates exist, or the measurement’s token-category mix is within a predeclared distance of the cost being divided. Full utilisation is the minimum API-equivalent value achievable when every simultaneous window is saturated over the fee period, not the largest single cap. Unmatched mixes stay out of the official Plan ranking.

The headline can name a model the other outputs already know is not a recommendation. Provisional rows stay in the table, which matches cohort policy, but nothing stops a provisional, transfer-dependent, or strictly dominated row from being rank 1 on the weighted score. The 90% scenario bar also mixes measurement noise with a Dirichlet weight draw, a source-drop flag, and a transfer on/off flag. A 90% share of that mixture is not “this winner survives the evidence.” The transfer flag’s probability is unspecified, so an authorised assumption can still produce a unique Plan winner.

Concrete change: the named leader, on either basis, must be non-provisional, not strictly inside the definite frontier, and first in at least 90% of measurement scenarios conditional on transfers off and AA sources included. Publish transfer-on and leave-AA-out as separate columns. Dominated and provisional rows remain in the table, flagged, and ineligible for that name.

Coverage can drop the leaf the objective cares about and still look official. Missing DeepSWE leaves coverage at 70% if every other leaf is present, with at least two SWE leaves, so the row is not provisional, and renormalisation spreads that 30% over the remaining leaves. The joint engine, as written, draws measurement intervals and does not draw the identification bounds. The 90% bar then ignores the largest hole in the score.

Concrete change: any missing leaf with nominal weight at least 20%, or observed SWE weight under 40% of quality, forces provisional. Unique claims must also hold on the identification bounds, not only on the renormalised point.

Medium

The source map is stale relative to the suite being priced. Terminal-Bench 4.0 is an Index component, so leave-AA-out is not an independent-source test if that score is AA’s. DeepSWE and FrontierCode are AA-run extras, not Index leaves. GPQA Diamond is outside the current Index. Briefcase and GDP.pdf are in the bill and absent from quality. GDPval-AA v2.1’s integration map is still clamp((Elo − 500) / 2000), but the scale is now pinned to DeepSeek V4.1 Flash (max) at 1600, and Elos are frozen at addition. A refresh that mixes anchors is a silent version break. AA also reprices cost with a representative cache-hit rate rather than the evaluation run’s own cache accounting, and open-weight prices may be a median across providers rather than a first-party list price.
artificialanalysis
+2

Concrete change: the registry stores, per row, chart field name, repeat-inclusion, cache-rate date, price rule, Elo anchor identity, and judge-panel version. Decompose score moves into price, cache-rate, token-use, method, and cohort. Reclassify the source-share table from the score’s actual runner. Suppress leave-AA-out when the remaining identified weight is under 40%.

A few leaf definitions will not survive a routine refresh. The prose sets anchors at chance, but the table sets GPQA to 0–100; chance on that multiple-choice set is 25%. FrontierCode is not a pass rate: a failed blocker scores 0, and a passing attempt scores 70–100%. Bug Hunt’s “whole-run bootstrap” is one round and two repos. A bug-level bootstrap treats dependent bugs as independent and invents precision. The printed exchange rate is API-only. On the Plan anchors, doubling cost is about −2.3 value points, or about 3.0 quality points, not −2.9 and 3.9. The fee in a multiple must be the amount paid for the measured period. An annual discount converted to a monthly equivalent overstates the multiple.
artificialanalysis
+2

Concrete change: GPQA uses a_low = 25. Pin FrontierCode to AA’s headline field and record the blocker pass rate beside it. Bug Hunt’s measurement interval is the two-repo range, not a bug bootstrap. Print the exchange rate per basis, plus each release’s within-cohort share 0.25 × SD(S_C) versus 0.75 × SD(S_Q).

Low

“Dirichlet concentration ≈ 50” can mean sum of alphas or alpha per leaf. Define α_i = 50 × nominal w_i. AA’s Index FAQ says four categories at 25%, while the methodology table says 30/20/20/30. Pin the table, not the FAQ. The near-Pareto band should use the unrounded Index stored in the registry, not the displayed integer, so a score sitting on a rounding boundary does not enter and leave the cohort between refreshes.
artificialanalysis
+1

2. Methodology design recommendations

Matched API cost. For each leaf with a public per-attempt USD cost c_i on that exact variant, set the ranking cost to the quality-weighted attempt cost

𝑐
API
=
∑
𝑖
∈
𝐿
𝑤
𝑖
′
𝑐
𝑖
,
𝑤
𝑖
′
=
𝑤
𝑖
∑
𝑗
∈
𝐿
𝑤
𝑗
.
c
API
	​

=
i∈L
∑
	​

w
i
′
	​

c
i
	​

,w
i
′
	​

=
∑
j∈L
	​

w
j
	​

w
i
	​

	​

.

Use AA’s per-evaluation cost where it publishes one, including Terminal-Bench’s average cost per task. Keep total suite USD, cost per Index point, and cost per solved task (c_i / pass rate) as diagnostics. If the matched leaves cover under 70% of quality weight, the cost is provisional and cannot name a unique winner. This is the O5 challenge. If O5 is retained, this column still gates unique claims when it disagrees with the total-cost rank by more than 3 places.
artificialanalysis
+1

Plan cost from category rates. Let t_k be the share of c_API coming from token category k, and m_k the measured API-dollar multiple for that category on that route. The route multiple is

𝑀
=
(
∑
𝑘
𝑡
𝑘
𝑚
𝑘
)
−
1
.
M=(
k
∑
	​

m
k
	​

t
k
	​

	​

)
−1
.

Plan cost is c_API / M, using the lower-bound m_k both to select the route and to compute the headline score. A blended multiple is allowed only when the measurement’s category shares are within the declared tolerance of t_k. The numerator is the minimum across binding windows under continuous use for the stated fee period, with shared pools attributed to the measured surface.
superblocks
+1

Claim rule, not a second table. Keep every cohort family in the primary table. The named leader must clear non-provisional coverage, definite-frontier non-dominance, transfers-off, and the identification bounds. Print scenario shares by stratum. Do not average those strata into one 90% figure.

Basis-specific quality. Same leaf formulas. API drops native-CLI leaves and renormalises the published weights. Plan keeps them. Coverage, provisional status, and the leader rule are computed per basis. Add AA-Briefcase to the professional group only by splitting the existing 20%, using the same (Elo − 500) / 2000 map, and only with its anchor identity recorded. Do not import it by raising the group weight.
artificialanalysis

Registry fields required before the next refresh. Chart field, total-cost and cost-per-task side by side, repeat-inclusion, cache-rate date, first-party versus median price, fallback-token treatment, Elo anchor, judge panel, and grader version. A change in any of these is a migration, not a data refresh.

3. Questions for the owner

If a public per-evaluation cost vector exists, may that vector replace total-suite USD as the ranking cost, with total-suite USD kept as a diagnostic? If not, the matched-cost column can only gate claims, not define the score.

Should native-CLI evidence count in API quality, Plan quality, or both? That choice determines whether Bug Hunt stays in one weight vector or two.

4. Verdict

VERDICT: HAS FEEDBACK