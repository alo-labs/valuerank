# ValueRank Methodology

**Version:** v1.5.0
**Updated:** September 6, 2026

## Cohort and source versions

The ranked cohort is the complete **21-model current DeepSWE Best roster**. Each model is represented by the Best-page effort row shown by DeepSWE; all 21 rows have pass@1, uncertainty, average cost, output-token, and agent-step values.

- DeepSWE source: [live leaderboard](https://deepswe.datacurve.ai/), v1.1, 113 tasks, updated September 3, 2026.
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current Artificial Analysis Intelligence Index v4.2.
- AA model values: one first-party model page per DeepSWE family, with the effort-specific URL selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values. The data files are pinned to release commit **62240f848c977d4202c1029191ac663498745f2f**.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with 14 official rows.

The old v1.3.1 and v1.4.0 publications used earlier benchmark identities or source snapshots. They remain historical; their numerical scores must not be compared directly with v1.5.0.

## Primary dimensions

The score retains only dimensions with a genuine value for every one of the 21 ranked models. Values are stored as raw fractions in scores.json, then converted to rank scores.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
| 1 | Cost | 31.65% | lower |
| 2 | Non-Hallucination | 7.59% | higher |
| 3 | DeepSWE | 8.86% | higher |
| 4 | GDPval-AA v2 | 7.59% | higher |
| 5 | τ³-Banking | 6.33% | higher |
| 6 | AA-LCR v1.1 | 5.06% | higher |
| 7 | AA-Omniscience Accuracy | 5.06% | higher |
| 8 | HLE | 5.06% | higher |
| 9 | GPQA Diamond (legacy) | 5.06% | higher |
| 10 | CritPt | 3.80% | higher |
| 11 | AA Intelligence Index | 7.59% | higher |
| 12 | Speed | 6.33% | higher |

The eleven AA source components below correspond to ten current AA evaluations because Omniscience is split into accuracy and non-hallucination reliability:

| AA evaluation/component | Current methodology weight |
|---|---:|
| AA-Briefcase | 15% |
| GDPval-AA v2 | 10% |
| τ³-Banking | 5% |
| Terminal-Bench v2.1 | 10% |
| SciCode | 10% |
| Humanity's Last Exam | 10% |
| GDP.pdf | 10% |
| CritPt | 10% |
| AA-Omniscience Accuracy | 10% |
| AA-Omniscience Non-Hallucination Rate | 5% |
| AA-LCR v1.1 | 5% |

These AA methodology weights describe the source index, not the combined ValueRank weights above. ValueRank adds DeepSWE, cost, and AA Index signals using the explicitly published priority table.

## Zero-gap rule

- A candidate dimension is scored only when all 21 models have a published value.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- No neutral 50, median, model-family, or legacy-version substitution is used.
- In v1.5.0, **Speed is retained in the primary score** because the v4.2 snapshot publishes numeric speed for all 21 selected pages.
- GPQA Diamond remains in the score as an explicitly labelled legacy ValueRank input for continuity; it is not a component of the v4.2 source composite.
- AA total evaluation cost is available for **18/21** models. Since the v4.2 snapshot is incomplete for **GPT-5.5, Claude Opus 4.8, GLM-5.2**, all models use the same DeepSWE-only cost mode; no selective substitution is applied.
- LiveBench Instruction Following is available for **20/21** cohort models, and Terminal-Bench 4.0 is available for **11/21**. Both are retained as null-safe coverage fields and visualized separately; neither is weighted into the primary score until it satisfies the zero-gap rule.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
| Terminal-Bench 4.0 | Kimi K3, GPT-5.5, GLM-5.3 Flash, DeepSeek V4 Pro, Qwen3.8 Max, Muse Spark 1.2, DeepSeek V4 Flash, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | incomplete cohort coverage; values remain null and are not neutral-filled |
| Instruction Following (LiveBench) | GPT-6 Astra | incomplete cohort coverage; values remain null and are not neutral-filled |
| SciCode | GPT-5.5 | incomplete cohort coverage; values remain null and are not neutral-filled |

## Rank normalization

For each retained dimension, models are ranked from best to worst and mapped with:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, rank 21 maps to 0, and exact ties receive the average tied rank. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Cost construction

The intended Cost input combines two independently observed penalties: AA Intelligence Index total evaluation cost and DeepSWE Best average cost per task, each normalized against the highest current cohort cost. The captured v4.2 pages do not publish AA total evaluation cost for **GPT-5.5, Claude Opus 4.8, GLM-5.2**. To preserve a comparable zero-gap dimension, this release uses the DeepSWE penalty alone for every model; available AA costs remain raw data and are not selectively substituted. The resulting costComposite is rank-normalized with lower cost better.

## Quality score and interpretation

Overall Score is the weighted sum of all retained dimensions. Quality Score removes Cost and renormalizes the remaining retained dimensions to 100%. Scores are rank-relative to this cohort, not probabilities and not an absolute model capability scale.

## Supplemental data

Artificial Analysis exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, AutomationBench, EnterpriseOpsGym, ITBench SRE, and other legacy/current fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json. AA-Briefcase and GDP.pdf are v4.2 source components represented in the snapshot; they are not added as separate ValueRank dimensions. GPQA Diamond is explicitly labelled as a legacy ValueRank input. The AA source payload still records its Terminal-Bench v2.1 component for provenance; the standalone current Terminal-Bench publication is TB4.

LiveBench is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the 20 matched cohort rows plus 1 official supplemental model: Claude Fable 5.1.

Terminal-Bench 4.0 is incorporated as the current external terminal-agent source. The standalone page shows all 14 official rows and the current cohort overlap, while the ValueRank score keeps the field coverage-only because 10 of the 21 ranked models are not present in the pinned TB4 table.

## Limitations

- DeepSWE and AA measure different tasks, harnesses, and sampling procedures; this is a transparent synthesis, not a new benchmark.
- Rank normalization discards magnitude differences and should be read with the raw values and uncertainty fields.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Speed is retained in the primary score because all selected v4.2 pages publish numeric values.
- LiveBench and Terminal-Bench have different task suites and release surfaces from the AA source component; their displayed values should not be substituted for one another or read as a continuous version-to-version series.
