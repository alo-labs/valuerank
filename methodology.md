# ValueRank Methodology

**Version:** v1.7.0
**Updated:** September 29, 2026

## Cohort and source versions

The ranked cohort is the complete **21-model current DeepSWE Best roster**. Each model is represented by the Best-page effort row shown by DeepSWE; all 21 rows have pass@1, uncertainty, average cost, output-token, and agent-step values.

- DeepSWE source: [live leaderboard](https://deepswe.datacurve.ai/), v1.1, 113 tasks, updated September 22, 2026.
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current Artificial Analysis Intelligence Index v4.3.2.
- AA model values: one first-party model page per DeepSWE family, with the effort-specific URL selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values. The data files are pinned to release commit **7be9f746f36a6f007dd78461f67cb7d06cfe2304**.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with 15 official rows, **11** direct cohort matches, and **1** eligible provider claim.

The v1.3.1 through v1.6.0 publications used earlier benchmark identities or source snapshots. They remain historical; their numerical scores must not be compared directly with v1.7.0.

## Primary dimensions

The score retains only dimensions with a genuine value for every one of the 21 ranked models. Values are stored as raw fractions in scores.json, then converted to rank scores.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
| 1 | Cost | 32.05% | lower |
| 2 | Non-Hallucination | 7.69% | higher |
| 3 | Instruction Following (LiveBench) | 6.41% | higher |
| 4 | DeepSWE | 8.97% | higher |
| 5 | [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 7.69% | higher |
| 6 | [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 5.13% | higher |
| 7 | [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 5.13% | higher |
| 8 | [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 5.13% | higher |
| 9 | [GPQA Diamond (legacy)](https://artificialanalysis.ai/evaluations/gpqa-diamond) | 5.13% | higher |
| 10 | [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 5.13% | higher |
| 11 | [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 3.85% | higher |
| 12 | [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 7.69% | higher |

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

These AA methodology weights describe the source index, not the combined ValueRank weights above. ValueRank adds DeepSWE, cost, and AA Index signals using the explicitly published priority table. The AA Index value for Gemini 3.7 Flash is the benchmark owner’s estimate pending independent evaluation.

## Zero-gap rule

- A candidate dimension is scored only when every model has an eligible value from the benchmark owner or an exact-version provider claim.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- No neutral 50, median, or mismatched-version value is used. Provider claims remain source-typed and are eligible only for the stated benchmark version and evaluated model/route.
- AA output speed covers **20/21** selected pages; **Kimi K3** is missing, so Speed is excluded under the zero-gap rule.
- GPQA Diamond remains an explicitly labelled legacy ValueRank input; it is not a component of the v4.3.2 source composite.
- AA total evaluation cost is available for **20/21** models. Since v4.3.2 cost coverage is incomplete for **Gemini 3.7 Flash**, all models use the same DeepSWE-only cost mode.
- LiveBench Instruction Following is available for **21/21** cohort models and is scored. Terminal-Bench 4.0 has **11** benchmark-owner results and **1** provider claim (**12/21 eligible values**); remaining gaps keep it out of the primary score.
- Bug Hunt Bench has **16/21** exact eligible results and is scored only in a separate matched-cohort emphasis ranking. It does not change the full-cohort primary score.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
| Terminal-Bench 4.0 | Kimi K3, GPT-5.5, GLM-5.3 Flash, DeepSeek V4 Pro, Qwen3.8 Max, Muse Spark 1.2, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | incomplete cohort coverage; values remain null and are not neutral-filled |
| AutomationBench-AA | Gemini 3.7 Flash | incomplete cohort coverage; values remain null and are not neutral-filled |
| Speed | Kimi K3 | incomplete cohort coverage; values remain null and are not neutral-filled |

## Rank normalization

For each retained dimension, models are ranked from best to worst and mapped with:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, rank 21 maps to 0, and exact ties receive the average tied rank. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Cost construction

The intended Cost input combines two independently observed penalties: AA Intelligence Index total evaluation cost and DeepSWE Best average cost per task, each normalized against the highest current cohort cost. The captured v4.3.2 pages do not publish AA total evaluation cost for **Gemini 3.7 Flash**. To preserve a comparable zero-gap dimension, this release uses the DeepSWE penalty alone for every model; available AA costs remain raw data and are not selectively substituted. The resulting costComposite is rank-normalized with lower cost better.

## Quality score and interpretation

Overall Score is the weighted sum of all retained dimensions. Quality Score removes Cost and renormalizes the remaining retained dimensions to 100%. Scores are rank-relative to this cohort, not probabilities and not an absolute model capability scale.

## Supplemental data

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, EnterpriseOpsGym, ITBench SRE, and legacy fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json. AA-Briefcase, GDP.pdf, AutomationBench-AA, and AA's Terminal-Bench 4.0 evaluation are v4.3.2 source components, not standalone ValueRank dimensions. GPQA Diamond and the old τ³-Banking/TB2.1 fields are separately labelled legacy data.

[LiveBench](https://livebench.ai/) is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the 21 matched cohort rows plus 1 official supplemental model: Claude Fable 5.1.

[Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) is incorporated as the current external terminal-agent source. The official page shows 15 owner rows; a separate provider-claim row is included for the current DeepSeek V4 Flash API alias and is explicitly labelled. Together they provide 12/21 eligible cohort values, leaving 9 gaps.

## Provider claim policy

When the benchmark owner has not published a result for a model, ValueRank uses a model-provider-published claim when the benchmark version and evaluated model identity match. The claim keeps its source type, direct source link, date, and any alias/variant caveat in the raw data and evidence ledger. A benchmark-owner result supersedes the claim when it becomes available. Claims for different versions or variants remain audit-only.

## Bug Hunt Bench emphasis ranking

The Bug Hunt owner publishes planted bugs fixed out of **105** across two repositories. This refresh pins the [combined scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv) and [run notes](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/run-notes.md) to commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c**. The result matches **16/21** models at the exact evaluated variant/route selected for this cohort. Unmatched rows remain null and are excluded from this view.

For this alternate ranking, each existing retained ValueRank dimension is re-ranked within the same 16-model subset. The Bug Hunt result is rank-normalized in that subset and receives priority **20** against the existing retained priority sum of **78**: **20/98 = 20.41%**. Each other retained dimension keeps its existing priority relative to the new total. Ties receive average rank; final composite ties use lower cost and then model name. This score is relative to the matched subset and cannot be compared numerically with the primary 21-model ranking.

The benchmark evaluates an agentic stack. The scoreboard includes different agent CLIs, reasoning efforts, routes, and repeat counts; those details remain with each row in [raw-data.md](raw-data.md). Most configurations have a single run, so close score differences may be noise. A focused provider-source check found no matching provider-published Bug Hunt score for the five uncovered models. If a future exact-version provider claim fills an owner gap, it must stay labelled as a provider claim; the benchmark owner’s result supersedes it when published.

## Limitations

- DeepSWE and AA measure different tasks, harnesses, and sampling procedures; this is a transparent synthesis, not a new benchmark.
- Bug Hunt results depend on the tested agent CLI/harness, effort, and route; they measure the tested stack, not model capability in isolation.
- Rank normalization discards magnitude differences and should be read with the raw values and uncertainty fields.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Provider claims may use a different harness or sampling procedure than the benchmark owner; displayed claim values are not presented as independent benchmark-owner measurements.
- AA output speed is numeric for **20/21** selected pages; **Kimi K3** has no value, so Speed is excluded under the zero-gap rule.
- LiveBench and Terminal-Bench have different task suites and release surfaces from the AA source component; their displayed values should not be substituted for one another or read as a continuous version-to-version series.
