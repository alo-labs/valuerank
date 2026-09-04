# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.4.0
**Updated:** September 4, 2026
**Scope:** 21 models from the current DeepSWE Best roster, 13 retained zero-gap dimensions

## Current result

ValueRank combines current DeepSWE agent performance with Artificial Analysis Intelligence Index v4.1.1 component results and a two-source cost penalty. The complete current DeepSWE Best roster is retained; no missing cell is filled with a neutral value.

| Rank | Model | Overall | Quality | Composite Cost |
|---:|---|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 69.4 | 69.2 | 12.04 |
| 2 | GLM-5.3 Flash | 65.6 | 51.1 | 1.72 |
| 3 | GPT-5.6 Sol | 61.3 | 73.5 | 30.72 |
| 4 | GPT-6 Astra | 61.0 | 73.1 | 30.72 |
| 5 | Grok 4.6 | 60.8 | 61.2 | 15.06 |
| 6 | Claude Opus 5 | 59.9 | 79.0 | 57.58 |
| 7 | Kimi K3 | 59.6 | 74.2 | 31.03 |
| 8 | GLM-5.3 | 58.3 | 63.9 | 18.91 |
| 9 | Muse Spark 1.2 | 53.0 | 47.9 | 12.87 |
| 10 | Claude Fable 5 | 52.1 | 72.0 | 75.40 |
| 11 | Gemini 3.7 Flash | 50.8 | 36.3 | 6.39 |
| 12 | GPT-5.6 Luna | 49.8 | 30.6 | 2.75 |
| 13 | Qwen3.8 Max | 48.0 | 51.4 | 21.11 |
| 14 | DeepSeek V4 Pro | 44.9 | 32.1 | 8.82 |
| 15 | GPT-5.5 | 43.4 | 53.3 | 39.32 |
| 16 | Gemini 3.6 Flash | 40.1 | 23.1 | 7.96 |
| 17 | DeepSeek V4 Flash | 39.9 | 18.7 | 3.83 |
| 18 | Claude Opus 4.8 | 36.8 | 48.1 | 59.43 |
| 19 | GLM-5.2 | 34.8 | 26.2 | 15.16 |
| 20 | Gemini 3.5 Flash | 34.0 | 27.3 | 16.09 |
| 21 | Claude Sonnet 5 | 26.5 | 37.8 | 86.76 |

The current Pareto frontier—undominated on composite cost versus quality—is: **Gemini 3.8 Flash, Claude Opus 5, GPT-5.6 Sol, Kimi K3, GLM-5.3 Flash**.

## What changed in v1.4

- DeepSWE is refreshed to the live v1.1 Best page: **21 models**, **113 tasks**, source updated **September 3, 2026**.
- Artificial Analysis is migrated to the current **Artificial Analysis Intelligence Index v4.1.1** identity: GDPval-AA v2, τ³-Banking, Terminal-Bench v2.1, SciCode, AA-LCR, HLE, GPQA Diamond, CritPt, and split AA-Omniscience accuracy/non-hallucination components.
- The ranked pool is **21 models**, with all current DeepSWE entries preserved.
- The score retains **13 zero-gap dimensions**; **Speed** is excluded because GPT-6 Astra.
- Speed remains an auditable coverage field (20/21 AA pages publish a numeric value) but is not imputed into the primary score because GPT-6 Astra's selected page reports N/A.
- Legacy v1.3.1 values are not numerically comparable: the AA benchmark identities and the DeepSWE cohort have changed.

## Sources and audit trail

- [DeepSWE Best](https://deepswe.datacurve.ai/) for pass@1, uncertainty, average cost, output tokens, and agent steps.
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [Research report](research/2026-09-04-valuerank-refresh/research_report.md) for the source ledger, evidence spans, triangulation, critique cycles, and decisions.
- [Coverage matrix](.refresh/v1.4/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): cohort, benchmark versions, normalization, and zero-gap rule
- [site/index.html](site/index.html): interactive static publication
- [research/2026-09-04-valuerank-refresh/](research/2026-09-04-valuerank-refresh/): reproducible research package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs
