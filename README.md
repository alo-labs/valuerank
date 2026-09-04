# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.4.0
**Updated:** September 5, 2026
**Scope:** 21 models from the current DeepSWE Best roster, 12 retained zero-gap dimensions

## Current result

ValueRank combines current DeepSWE agent performance with Artificial Analysis Intelligence Index v4.1.1 component results and a two-source cost penalty. The complete current DeepSWE Best roster is retained; no missing cell is filled with a neutral value. LiveBench Instruction Following and Terminal-Bench 4.0 are published alongside the score as separately sourced coverage-only views until their official coverage is complete for this cohort.

| Rank | Model | Overall | Quality | Composite Cost |
|---:|---|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 68.2 | 67.4 | 12.04 |
| 2 | GLM-5.3 Flash | 66.1 | 50.0 | 1.72 |
| 3 | Grok 4.6 | 60.9 | 61.3 | 15.06 |
| 4 | GPT-5.6 Sol | 59.1 | 71.7 | 30.72 |
| 5 | GLM-5.3 | 58.9 | 65.5 | 18.91 |
| 6 | GPT-6 Astra | 58.2 | 70.3 | 30.72 |
| 7 | Kimi K3 | 58.0 | 73.5 | 31.03 |
| 8 | Claude Opus 5 | 57.1 | 76.9 | 57.58 |
| 9 | Muse Spark 1.2 | 54.8 | 50.0 | 12.87 |
| 10 | Gemini 3.7 Flash | 53.9 | 39.2 | 6.39 |
| 11 | GPT-5.6 Luna | 50.5 | 29.5 | 2.75 |
| 12 | Claude Fable 5 | 50.5 | 72.0 | 75.40 |
| 13 | Qwen3.8 Max | 48.3 | 52.2 | 21.11 |
| 14 | DeepSeek V4 Pro | 46.8 | 33.4 | 8.82 |
| 15 | Gemini 3.6 Flash | 43.1 | 25.8 | 7.96 |
| 16 | GPT-5.5 | 42.1 | 52.5 | 39.32 |
| 17 | DeepSeek V4 Flash | 41.5 | 18.6 | 3.83 |
| 18 | GLM-5.2 | 37.1 | 28.6 | 15.16 |
| 19 | Gemini 3.5 Flash | 35.1 | 28.1 | 16.09 |
| 20 | Claude Opus 4.8 | 34.0 | 45.3 | 59.43 |
| 21 | Claude Sonnet 5 | 25.9 | 38.1 | 86.76 |

The current Pareto frontier—undominated on composite cost versus quality—is: **Gemini 3.8 Flash, Claude Opus 5, GPT-5.6 Sol, Kimi K3, GLM-5.3 Flash**.

## What changed in v1.4

- DeepSWE is refreshed to the live v1.1 Best page: **21 models**, **113 tasks**, source updated **September 3, 2026**.
- Artificial Analysis is migrated to the current **Artificial Analysis Intelligence Index v4.1.1** identity: GDPval-AA v2, τ³-Banking, its source Terminal-Bench v2.1 component, SciCode, AA-LCR, HLE, GPQA Diamond, CritPt, and split AA-Omniscience accuracy/non-hallucination components.
- The standalone Terminal-Bench view is replaced by the official **Terminal-Bench 4.0** snapshot: **14 rows**, with **11/21** overlap with the ranked cohort.
- **LiveBench 2026-06-25** supplies the Instruction Following component and Overall-vs-Cost view: **20/21** ranked cohort rows matched, **21** rows published in total, plus **1 official supplemental model** (**Claude Fable 5.1**); the current LiveBench Pareto frontier is **DeepSeek V4 Flash, GLM-5.3 Flash, Gemini 3.7 Flash, Kimi K3, GPT-5.5, GPT-5.6 Sol, Claude Fable 5.1**.
- The ranked pool is **21 models**, with all current DeepSWE entries preserved.
- The score retains **12 zero-gap dimensions**; **Terminal-Bench 4.0, Instruction Following (LiveBench), Speed** are excluded because each has incomplete official cohort coverage. Missing external values remain null and are not neutral-filled.
- Speed remains an auditable coverage field (20/21 AA pages publish a numeric value) but is not imputed into the primary score because GPT-6 Astra's selected page reports N/A.
- Legacy v1.3.1 values are not numerically comparable: the AA benchmark identities and the DeepSWE cohort have changed.

## Sources and audit trail

- [DeepSWE Best](https://deepswe.datacurve.ai/) for pass@1, uncertainty, average cost, output tokens, and agent steps.
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench), pinned at [release data commit 62240f848c977d4202c1029191ac663498745f2f](https://github.com/livebench/new-livebench/commit/62240f848c977d4202c1029191ac663498745f2f), for the 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Research report](research/2026-09-04-valuerank-refresh/research_report.md) for the source ledger, evidence spans, triangulation, critique cycles, and decisions.
- [Coverage matrix](.refresh/v1.4/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): cohort, benchmark versions, normalization, and zero-gap rule
- [site/index.html](site/index.html): interactive static publication
- [site/tb4/index.html](site/tb4/index.html): current Terminal-Bench 4.0 score-versus-cost publication
- [research/2026-09-04-valuerank-refresh/](research/2026-09-04-valuerank-refresh/): reproducible research package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs
