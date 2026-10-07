# ValueRank Methodology

**Version:** v1.9.6
**Updated:** October 8, 2026

## Cohort and source versions

The selected catalog is reconciled against AA's current Pareto frontier of Intelligence Index score versus total USD benchmark-run cost and includes every represented frontier model. AA's Coding Agent Index v1.5 chart publishes **31 DeepSWE v1.1 configurations** across **113 tasks**, observed **2026-10-08**. The primary rank includes every selected model with at least one eligible exact-version non-cost quality metric; a model does not need complete benchmark overlap. Models without an observed quality metric remain unranked. Each chart result retains its displayed model variant, agent, and effort.

- DeepSWE v1.1 source: [AA Coding Agent Index v1.5](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1). The published chart says each score averages pass@1 across three attempts per task; the complete 31-configuration inventory and exact-variant mapping decisions are pinned in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json).
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current Artificial Analysis Intelligence Index v4.3.2.
- AA Intelligence Index percentile comparisons use whole-point precision for every model because fresh public labels are rounded while older captures retain finer raw precision. Raw source inputs remain unchanged; sub-point differences should not be read as a reliable ordering.
- AA v4.3.2 model values: first-party model pages selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values. The data files are pinned to release commit **7be9f746f36a6f007dd78461f67cb7d06cfe2304**.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with 14 official rows, **11** direct cohort matches, and **1** eligible provider claim.

Earlier publications used different source snapshots, weights, or cohorts. They remain historical; their numerical scores must not be compared directly with v1.9.6.

## Primary dimensions

The retained dimension set is selected from eligible current source coverage and the published priority policy. For each dimension, only models with a genuine exact-version value are ranked; scores remain missing for other rows. Each model's available dimension priorities are then renormalized to 100%, and its `availablePriority / totalPriority` coverage and missing metrics are published with the score. Raw benchmark values remain in scores.json; normalized rank scores are calculated from available values only.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
| 1 | Cost | 18.94% | lower |
| 2 | Non-Hallucination | 4.55% | higher |
| 3 | [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) | 4.55% | higher |
| 4 | Instruction Following (LiveBench) | 3.79% | higher |
| 5 | DeepSWE v1.1 | 18.94% | higher |
| 6 | [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 4.55% | higher |
| 7 | [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | 3.79% | higher |
| 8 | [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 3.03% | higher |
| 9 | [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 3.03% | higher |
| 10 | [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 3.03% | higher |
| 11 | [GPQA Diamond (legacy)](https://artificialanalysis.ai/evaluations/gpqa-diamond) | 3.03% | higher |
| 12 | [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 3.03% | higher |
| 13 | [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 2.27% | higher |
| 14 | [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 4.55% | higher |
| 15 | Speed | 3.79% | higher |
| 16 | [Bug Hunt Bench](https://bughunt.productcompass.pm/) | 15.15% | higher |

The eleven AA source components below correspond to ten current AA evaluations because Omniscience is split into accuracy and non-hallucination reliability:

| AA evaluation/component | Current methodology weight |
|---|---:|
| [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase) | 15% |
| [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 10% |
| [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | 5% |
| [Terminal-Bench 4.0 (AA evaluation)](https://artificialanalysis.ai/evaluations/terminalbench-4-0) | 10% |
| [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 10% |
| [Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 10% |
| [GDP.pdf](https://artificialanalysis.ai/evaluations/gdp-pdf) | 10% |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 10% |
| [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 10% |
| [AA-Omniscience Non-Hallucination Rate](https://artificialanalysis.ai/evaluations/omniscience) | 5% |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 5% |

These AA methodology weights describe the source index, not the combined ValueRank weights above. ValueRank adds DeepSWE, cost, and AA Index signals using the explicitly published priority table. The AA Index value for none is the benchmark owner’s estimate pending independent evaluation.

## API Costs and Plan Costs

The default API Costs basis uses each model's AA total evaluation cost in USD. Plan Costs divides that same value by the model's highest eligible subscription Value Multiple. Lower cost ranks better in both views; the site switcher recalculates the primary composite when the cost basis changes.

## Missing-metric handling

- A retained dimension contributes to a model only when that model has an eligible value from the benchmark owner or an exact-version provider claim. Ranking within each dimension uses only models with eligible values.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- Each row's retained priorities are renormalized over that model's available values. Coverage is available priority divided by total retained priority; missing metric names accompany the percentage.
- No zero, neutral 50, median, or mismatched-version value is used. Provider claims remain source-typed and are eligible only for the stated benchmark version and evaluated model/route.
- AA output speed covers **15/16** selected pages; **Kimi K3** is missing. If retained, Speed contributes only where a value exists and the gap is included in row coverage.
- GPQA Diamond remains an explicitly labelled legacy ValueRank input; it is not a component of the v4.3.2 source composite.
- AA total evaluation cost is available for **16/16** ranked models; the cost component uses **AA evaluation cost only** consistently across this cohort.
- LiveBench Instruction Following is available for **12/16** ranked models and is scored where present. Terminal-Bench 4.0 is supplemental in this release under the published dimension-selection policy.
- Bug Hunt Bench has **22/28** exact owner results. Eligible exact-variant results contribute where present at the published Bug Hunt priority; the separate emphasis view includes **14** rows with eligible results.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
| None | — | All candidate dimensions have complete coverage. |

## Rank normalization

For each retained dimension, models with an eligible value are ranked from best to worst and mapped using that dimension's available sample size:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, the worst observed rank maps to 0, and exact ties receive the average tied rank. The sample size is the number of models with a value for that dimension. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Benchmark evaluation cost (score input)

The Cost input uses **AA evaluation cost only** where an AA Intelligence Index total evaluation cost is available; lower evaluation cost is better. Plan Costs divides that same total benchmark cost by the model's highest eligible subscription Value Multiple. A missing cost remains null and the row's other available priorities are renormalized; no DeepSWE leaderboard cost or missing-value fill is used.

## Quality score and interpretation

Overall Score is the weighted sum of a model's available retained dimensions, with that row's available priorities renormalized to 100%. Quality Score removes Cost and renormalizes the available non-cost dimensions to 100%. Scores are rank-relative to the values available for this release, not probabilities and not an absolute model capability scale; row coverage is displayed beside each score.

## Supplemental data

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, EnterpriseOpsGym, ITBench SRE, and legacy fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json. AA-Briefcase, GDP.pdf, AutomationBench-AA, and AA's Terminal-Bench 4.0 evaluation are v4.3.2 source components, not standalone ValueRank dimensions. GPQA Diamond and the old τ³-Banking/TB2.1 fields are separately labelled legacy data.

[LiveBench](https://livebench.ai/) is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the 24 matched cohort rows plus 1 official supplemental model: Claude Fable 5.1.

[Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) is incorporated as the current external terminal-agent source. The official page shows 14 owner rows; a separate provider-claim row is included for the current DeepSeek V4 Flash API alias and is explicitly labelled. Together they provide 12/28 eligible cohort values, leaving 16 gaps.

## Provider claim policy

When the benchmark owner has not published a result for a model, ValueRank uses a model-provider-published claim when the benchmark version and evaluated model identity match. The claim keeps its source type, direct source link, date, and any alias/variant caveat in the raw data and evidence ledger. A benchmark-owner result supersedes the claim when it becomes available. Claims for different versions or variants remain audit-only.

## Bug Hunt Bench scoring

Bug Hunt Bench reports planted bugs fixed out of **105** across two repositories. The owner scoreboard snapshot is pinned at commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c** and provides **22/28** exact results in the AA-mapped comparison roster. Each eligible exact-variant owner value contributes to that model's primary score at Bug Hunt priority **20** (**15.15%** before row-level renormalization).

The companion Bug Hunt emphasis ranking uses **14** eligible owner-result rows and re-ranks the other available dimensions within that subset. It gives Bug Hunt priority **30** out of **142**, or **21.13%** before row-level renormalization. Ties use average rank, then lower cost and model name. Its scores are a separate weighting view and should not be compared numerically with the primary composite.

The scoreboard tests an agentic model-and-harness configuration. Runs vary in effort, agent CLI, route, and repeat count; those details remain in the table, and single-run rows are noisy. Models remain visible when one or more retained metrics are missing, with their available-priority coverage shown. A model with no rankable primary metric remains unranked. No values are inferred or neutral-filled. A provider claim may fill an owner gap only for an exact benchmark version and evaluated model variant, and an owner result supersedes it when published.

## Limitations

- The AA DeepSWE chart and the other AA Index components measure distinct tasks and use different evaluation setups; ValueRank is a transparent synthesis, not a new benchmark.
- Bug Hunt results also depend on the tested agent CLI/harness, effort, and route; they measure the tested stack, not model capability in isolation.
- Rank normalization discards magnitude differences. The AA DeepSWE chart publishes rounded percentage values without uncertainty intervals; read them alongside the exact agent and effort configuration.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Provider claims may use a different harness or sampling procedure than the benchmark owner; displayed claim values are not presented as independent benchmark-owner measurements.
- AA output speed is numeric for **15/16** selected pages; **Kimi K3** has no value. When retained, Speed affects only rows with a value and the per-row coverage makes that difference visible.
- LiveBench and Terminal-Bench have different task suites and release surfaces from the AA source component; their displayed values should not be substituted for one another or read as a continuous version-to-version series.


## Subscription evidence policy

Plan route evidence as of 2026-10-08. Effective Plan evaluation cost is AA API evaluation cost divided by the highest eligible Value Multiple. The candidate comparison includes unranked source candidates; a Plan route does not establish a primary composite rank or ValueRank quality frontier membership. For Anthropic and Codex, the user-selected SemiAnalysis analysis supplies controlled subscription-account measurements with workload projections; its allocation regime, workload and evaluated model remain in the route evidence. The common ChatGPT multiples (Plus 8.1×; Pro $100 10.55×; Pro $200 10.42×; Pro $500 10.772×) are a provisional cross-model application: the source projections evaluate Astra for Plus and Sol for the Pro tiers, and do not establish the same allowance for every GPT variant. The highest eligible common GPT route is Pro $500 at 10.772×. MiMo Pro and MiMo Flash use a provisional user assumption of 1.5×; their subscription fee is not established and their API equivalent dollar numerator is not measured. For other providers, eligible measured routes require actual end-user API-priced usage, exact variants, plan tier and report date in the preceding month. Mixed or unidentified model usage remains provider/plan evidence and does not enter a model route. Provider allowance, quota and marketing figures cannot supply a measured numerator.
