# ValueRank Methodology

**Version:** v1.4.0
**Updated:** September 5, 2026

## Cohort and source versions

The ranked cohort is the complete **21-model current DeepSWE Best roster**. Each model is represented by the Best-page effort row shown by DeepSWE; all 21 rows have pass@1, uncertainty, average cost, output-token, and agent-step values.

- DeepSWE source: [live leaderboard](https://deepswe.datacurve.ai/), v1.1, 113 tasks, updated September 3, 2026.
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current Artificial Analysis Intelligence Index v4.1.1.
- AA model values: one first-party model page per DeepSWE family, with the effort-specific URL selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.
- LiveBench source: [livebench.ai](https://livebench.ai/), pinned release **2026-06-25** with seven categories, including the four-task Instruction Following category and published Cost Per Successful Task values.
- Terminal-Bench source: [tbench.ai](https://www.tbench.ai/), current **4.0** rendered leaderboard snapshot with 14 official rows.

The old v1.3.1 publication used an earlier cohort and older AA benchmark identities. It remains historical; its numerical scores must not be compared directly with v1.4.0.

## Primary dimensions

The score retains only dimensions with a genuine value for every one of the 21 ranked models. Values are stored as raw fractions in scores.json, then converted to rank scores.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
| 1 | Cost | 32.05% | lower |
| 2 | Non-Hallucination | 7.69% | higher |
| 3 | DeepSWE | 8.97% | higher |
| 4 | GDPval-AA v2 | 7.69% | higher |
| 5 | τ³-Banking | 6.41% | higher |
| 6 | AA-LCR | 5.13% | higher |
| 7 | AA-Omniscience Accuracy | 5.13% | higher |
| 8 | HLE | 5.13% | higher |
| 9 | GPQA Diamond | 5.13% | higher |
| 10 | SciCode | 5.13% | higher |
| 11 | CritPt | 3.85% | higher |
| 12 | AA Intelligence Index | 7.69% | higher |

The ten AA component entries below correspond to the nine current AA evaluations because Omniscience is split into accuracy and non-hallucination reliability:

| AA evaluation/component | Current methodology weight |
|---|---:|
| GDPval-AA v2 | 20% |
| τ³-Banking | 14% |
| AA source Terminal-Bench v2.1 | 16% |
| SciCode | 8% |
| AA-LCR | 6% |
| Humanity's Last Exam | 12% |
| GPQA Diamond | 6% |
| CritPt | 6% |
| AA-Omniscience Accuracy | 8% |
| AA-Omniscience Non-Hallucination Rate | 4% |

These AA methodology weights describe the source index, not the combined ValueRank weights above. ValueRank adds DeepSWE, cost, and AA Index signals using the explicitly published priority table.

## Zero-gap rule

- A candidate dimension is scored only when all 21 models have a published value.
- Missing values remain null in aa_metrics.json and are listed in coverage_matrix.json.
- No neutral 50, median, model-family, or legacy-version substitution is used.
- In v1.4.0, **Speed is dropped from the primary score** because the selected GPT-6 Astra AA page reports N/A. Numeric speed values for the other 20 models remain in raw data and the coverage matrix.
- LiveBench Instruction Following is available for **20/21** cohort models, and Terminal-Bench 4.0 is available for **11/21**. Both are retained as null-safe coverage fields and visualized separately; neither is weighted into the primary score until it satisfies the zero-gap rule.

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
| Terminal-Bench 4.0 | Kimi K3, GPT-5.5, GLM-5.3 Flash, DeepSeek V4 Pro, Qwen3.8 Max, Muse Spark 1.2, DeepSeek V4 Flash, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | incomplete cohort coverage; values remain null and are not neutral-filled |
| Instruction Following (LiveBench) | GPT-6 Astra | incomplete cohort coverage; values remain null and are not neutral-filled |
| Speed | GPT-6 Astra | incomplete cohort coverage; values remain null and are not neutral-filled |

## Rank normalization

For each retained dimension, models are ranked from best to worst and mapped with:

((n - rank) / (n - 1)) × 100

Rank 1 maps to 100, rank 21 maps to 0, and exact ties receive the average tied rank. Lower-is-better dimensions, including composite Cost, reverse the ordering before normalization.

## Cost construction

The Cost input is an average of two independently observed penalties:

1. AA Intelligence Index total evaluation cost, normalized against the highest current cohort cost.
2. DeepSWE Best average cost per task, normalized against the highest current cohort cost.
3. The two 0–100 penalties are averaged into costComposite.
4. costComposite is rank-normalized with lower cost better.

This avoids treating a single vendor's price surface as the whole production-cost story while keeping the two source quantities visible in every score row.

## Quality score and interpretation

Overall Score is the weighted sum of all retained dimensions. Quality Score removes Cost and renormalizes the remaining retained dimensions to 100%. Scores are rank-relative to this cohort, not probabilities and not an absolute model capability scale.

## Supplemental data

Artificial Analysis exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, AutomationBench, EnterpriseOpsGym, ITBench SRE, Briefcase, and other legacy/current fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json, but they are not added to the primary score when incomplete or outside the current v4.1.1 index definition. The AA source payload still records its own v2.1 component for provenance; the standalone current Terminal-Bench publication is TB4.

LiveBench is incorporated as the current external Instruction Following source. Its four official task values—paraphrase, simplify, story_generation, and summarize—are averaged into the published Instruction Following value; LiveBench Overall is the mean of its seven category means. The LiveBench chart uses the official Overall Score against the official Cost Per Successful Task for the 20 matched cohort rows.

Terminal-Bench 4.0 is incorporated as the current external terminal-agent source. The standalone page shows all 14 official rows and the current cohort overlap, while the ValueRank score keeps the field coverage-only because 10 of the 21 ranked models are not present in the pinned TB4 table.

## Limitations

- DeepSWE and AA measure different tasks, harnesses, and sampling procedures; this is a transparent synthesis, not a new benchmark.
- Rank normalization discards magnitude differences and should be read with the raw values and uncertainty fields.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Speed is intentionally coverage-only in this release because one current page has N/A.
- LiveBench and Terminal-Bench have different task suites and release surfaces from the AA source component; their displayed values should not be substituted for one another or read as a continuous version-to-version series.
