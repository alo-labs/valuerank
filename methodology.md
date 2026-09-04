# ValueRank Methodology

**Version:** v1.4.0
**Updated:** September 4, 2026

## Cohort and source versions

The ranked cohort is the complete **21-model current DeepSWE Best roster**. Each model is represented by the Best-page effort row shown by DeepSWE; all 21 rows have pass@1, uncertainty, average cost, output-token, and agent-step values.

- DeepSWE source: [live leaderboard](https://deepswe.datacurve.ai/), v1.1, 113 tasks, updated September 3, 2026.
- AA source: [Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), current Artificial Analysis Intelligence Index v4.1.1.
- AA model values: one first-party model page per DeepSWE family, with the effort-specific URL selected by .refresh/v1.4/aa_mapping.json and recorded in aa_metrics.json.

The old v1.3.1 publication used an earlier cohort and older AA benchmark identities. It remains historical; its numerical scores must not be compared directly with v1.4.0.

## Primary dimensions

The score retains only dimensions with a genuine value for every one of the 21 ranked models. Values are stored as raw fractions in scores.json, then converted to rank scores.

| # | Dimension | ValueRank weight | Direction |
|---:|---|---:|---|
| 1 | Cost | 29.76% | lower |
| 2 | Non-Hallucination | 7.14% | higher |
| 3 | Terminal-Bench v2.1 | 7.14% | higher |
| 4 | DeepSWE | 8.33% | higher |
| 5 | GDPval-AA v2 | 7.14% | higher |
| 6 | τ³-Banking | 5.95% | higher |
| 7 | AA-LCR | 4.76% | higher |
| 8 | AA-Omniscience Accuracy | 4.76% | higher |
| 9 | HLE | 4.76% | higher |
| 10 | GPQA Diamond | 4.76% | higher |
| 11 | SciCode | 4.76% | higher |
| 12 | CritPt | 3.57% | higher |
| 13 | AA Intelligence Index | 7.14% | higher |

The ten AA component entries below correspond to the nine current AA evaluations because Omniscience is split into accuracy and non-hallucination reliability:

| AA evaluation/component | Current methodology weight |
|---|---:|
| GDPval-AA v2 | 20% |
| τ³-Banking | 14% |
| Terminal-Bench v2.1 | 16% |
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

Dropped candidate dimensions:

| Dimension | Missing models | Decision |
|---|---|---|
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

Artificial Analysis exposes additional evaluations—such as MLCR, Harvey, APEX-Agents, MMMU-Pro, AutomationBench, EnterpriseOpsGym, ITBench SRE, Briefcase, and other legacy/current fields. They are preserved in aa_metrics.json when published, and their coverage is reported in coverage_matrix.json, but they are not added to the primary score when incomplete or outside the current v4.1.1 index definition.

## Limitations

- DeepSWE and AA measure different tasks, harnesses, and sampling procedures; this is a transparent synthesis, not a new benchmark.
- Rank normalization discards magnitude differences and should be read with the raw values and uncertainty fields.
- Page variants can differ by reasoning effort; the selected URL and variant are recorded per model.
- Speed is intentionally coverage-only in this release because one current page has N/A.
