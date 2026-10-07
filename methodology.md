# ValueRank Methodology

**Version:** v1.9.4
**Updated:** October 8, 2026

## Cohort and source versions

The model universe is the **27-model AA-mapped ValueRank comparison roster**. AA's Coding Agent Index v1.5 chart publishes **25 DeepSWE v1.1 configurations** across **113 tasks**. The primary rank contains **13 models** with both an exact chart model-variant result and an eligible Bug Hunt owner result; all other candidates remain visible without a composite rank. Each chart result retains its displayed model variant, agent, and effort.

- DeepSWE v1.1 source: [AA Coding Agent Index v1.5](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1). The published chart says each score averages pass@1 across three attempts per task; the 25 visible configurations and exact-variant mapping decisions are pinned in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json).
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current Artificial Analysis Intelligence Index v4.3.2.
- AA v4.3.2 model values: first-party model pages selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values. The data files are pinned to release commit **7be9f746f36a6f007dd78461f67cb7d06cfe2304**.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with 15 official rows, **11** direct cohort matches, and **1** eligible provider claim.

Earlier publications used different source snapshots, weights, or cohorts. They remain historical; their numerical scores must not be compared directly with v1.9.4.

## Primary dimensions

The score retains only dimensions with a genuine value for every one of the 13 ranked models, including exact owner-published Bug Hunt values. Values are stored as raw fractions in scores.json, then converted to rank scores within this cohort.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
| 1 | Cost | 22.32% | lower |
| 2 | Non-Hallucination | 5.36% | higher |
| 3 | DeepSWE v1.1 | 22.32% | higher |
| 4 | [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 5.36% | higher |
| 5 | [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | 4.46% | higher |
| 6 | [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 3.57% | higher |
| 7 | [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 3.57% | higher |
| 8 | [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 3.57% | higher |
| 9 | [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 3.57% | higher |
| 10 | [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 2.68% | higher |
| 11 | [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 5.36% | higher |
| 12 | [Bug Hunt Bench](https://bughunt.productcompass.pm/) | 17.86% | higher |

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

## Zero-gap rule

- A candidate dimension is scored only when every model has an eligible value from the benchmark owner or an exact-version provider claim.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- No neutral 50, median, or mismatched-version value is used. Provider claims remain source-typed and are eligible only for the stated benchmark version and evaluated model/route.
- AA output speed covers **12/13** selected pages; **Kimi K3** is missing, so Speed is excluded under the zero-gap rule.
- GPQA Diamond remains an explicitly labelled legacy ValueRank input; it is not a component of the v4.3.2 source composite.
- AA total evaluation cost is available for **13/13** ranked models; the cost component uses **AA evaluation cost only** consistently across this cohort.
- LiveBench Instruction Following is available for **12/13** ranked models and is scored. Terminal-Bench 4.0 remains supplemental because it has gaps in this cohort.
- Bug Hunt Bench has **21/27** exact owner results; **13** also have an exact AA DeepSWE model-variant result and enter the primary composite at **17.86%**. 14 candidates without the full overlap are not ranked.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
| Terminal-Bench 4.0 | Kimi K3, Qwen3.8 Max, Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, Grok 4.7 | incomplete coverage within the exact Bug Hunt matched cohort; values remain null and are not neutral-filled |
| Instruction Following (LiveBench) | Claude Opus 5.5 | incomplete coverage within the exact Bug Hunt matched cohort; values remain null and are not neutral-filled |
| GPQA Diamond (legacy) | Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, Grok 4.7 | incomplete coverage within the exact Bug Hunt matched cohort; values remain null and are not neutral-filled |
| Speed | Kimi K3 | incomplete coverage within the exact Bug Hunt matched cohort; values remain null and are not neutral-filled |

## Rank normalization

For each retained dimension, models are ranked from best to worst and mapped with:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, rank 13 maps to 0, and exact ties receive the average tied rank. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Benchmark evaluation cost (score input)

The Cost input uses **AA evaluation cost only** for every one of the 13 ranked models. AA Intelligence Index evaluation cost is normalized into costComposite; lower evaluation cost is better. No DeepSWE leaderboard cost or missing-value fill is used.

## Quality score and interpretation

Overall Score is the weighted sum of all retained dimensions. Quality Score removes Cost and renormalizes the remaining retained dimensions to 100%. Scores are rank-relative to this cohort, not probabilities and not an absolute model capability scale.

## Supplemental data

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, EnterpriseOpsGym, ITBench SRE, and legacy fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json. AA-Briefcase, GDP.pdf, AutomationBench-AA, and AA's Terminal-Bench 4.0 evaluation are v4.3.2 source components, not standalone ValueRank dimensions. GPQA Diamond and the old τ³-Banking/TB2.1 fields are separately labelled legacy data.

[LiveBench](https://livebench.ai/) is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the 24 matched cohort rows plus 1 official supplemental model: Claude Fable 5.1.

[Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) is incorporated as the current external terminal-agent source. The official page shows 15 owner rows; a separate provider-claim row is included for the current DeepSeek V4 Flash API alias and is explicitly labelled. Together they provide 12/27 eligible cohort values, leaving 15 gaps.

## Provider claim policy

When the benchmark owner has not published a result for a model, ValueRank uses a model-provider-published claim when the benchmark version and evaluated model identity match. The claim keeps its source type, direct source link, date, and any alias/variant caveat in the raw data and evidence ledger. A benchmark-owner result supersedes the claim when it becomes available. Claims for different versions or variants remain audit-only.

## Bug Hunt Bench scoring

Bug Hunt Bench reports planted bugs fixed out of **105** across two repositories. The owner scoreboard snapshot is pinned at commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c** and provides **21/27** exact results in the AA-mapped comparison roster. **13** of those also have an exact AA DeepSWE v1.1 model-variant result, so both values enter the main 13-model composite at Bug Hunt priority **20** (**17.86%**).

The companion Bug Hunt emphasis ranking uses the same 13-model exact-overlap cohort and re-ranks the other retained dimensions within those models. It gives Bug Hunt priority **30** out of **122**, or **24.59%**. Ties use average rank, then lower cost and model name. Its scores are a separate weighting view and should not be compared numerically with the primary composite.

The scoreboard tests an agentic model-and-harness configuration. Runs vary in effort, agent CLI, route, and repeat count; those details remain in the table, and single-run rows are noisy. The 14 models without the full AA DeepSWE and Bug Hunt overlap remain unranked; some have only one of those results. No values are inferred or neutral-filled. A provider claim may fill an owner gap only for an exact benchmark version and evaluated model variant, and an owner result supersedes it when published.

## Limitations

- The AA DeepSWE chart and the other AA Index components measure distinct tasks and use different evaluation setups; ValueRank is a transparent synthesis, not a new benchmark.
- Bug Hunt results also depend on the tested agent CLI/harness, effort, and route; they measure the tested stack, not model capability in isolation.
- Rank normalization discards magnitude differences. The AA DeepSWE chart publishes rounded percentage values without uncertainty intervals; read them alongside the exact agent and effort configuration.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Provider claims may use a different harness or sampling procedure than the benchmark owner; displayed claim values are not presented as independent benchmark-owner measurements.
- AA output speed is numeric for **12/13** selected pages; **Kimi K3** has no value, so Speed is excluded under the zero-gap rule.
- LiveBench and Terminal-Bench have different task suites and release surfaces from the AA source component; their displayed values should not be substituted for one another or read as a continuous version-to-version series.
