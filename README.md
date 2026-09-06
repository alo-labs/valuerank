# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.5.0
**Updated:** September 6, 2026
**Scope:** 21 models from the current DeepSWE Best roster, 12 retained zero-gap dimensions

## Current result

ValueRank combines current DeepSWE agent performance with Artificial Analysis Intelligence Index v4.2 source results and a DeepSWE-only cost penalty. The complete current DeepSWE Best roster is retained; no missing cell is filled with a neutral value. LiveBench Instruction Following and Terminal-Bench 4.0 are published alongside the score as separately sourced coverage-only views until their official coverage is complete for this cohort.

| Rank | Model | Overall | Quality | Composite Cost |
|---:|---|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 68.5 | 67.9 | 8.94 |
| 2 | Grok 4.6 | 64.1 | 64.9 | 13.07 |
| 3 | GLM-5.3 Flash | 63.8 | 47.0 | 0.91 |
| 4 | GPT-6 Astra | 59.4 | 75.3 | 24.70 |
| 5 | GPT-5.6 Sol | 59.1 | 72.6 | 24.47 |
| 6 | Gemini 3.7 Flash | 58.9 | 49.2 | 7.69 |
| 7 | GLM-5.3 | 54.9 | 61.8 | 15.11 |
| 8 | Kimi K3 | 54.6 | 63.7 | 17.61 |
| 9 | GPT-5.6 Luna | 53.1 | 36.0 | 2.31 |
| 10 | Claude Opus 5 | 53.1 | 70.7 | 44.85 |
| 11 | DeepSeek V4 Pro | 52.1 | 36.8 | 6.33 |
| 12 | Muse Spark 1.2 | 49.5 | 46.9 | 14.02 |
| 13 | Claude Fable 5 | 48.6 | 68.8 | 50.80 |
| 14 | Qwen3.8 Max | 48.3 | 47.5 | 14.13 |
| 15 | DeepSeek V4 Flash | 47.7 | 25.7 | 1.74 |
| 16 | Gemini 3.6 Flash | 42.8 | 28.0 | 8.37 |
| 17 | GPT-5.5 | 42.2 | 52.5 | 27.39 |
| 18 | Gemini 3.5 Flash | 36.0 | 23.7 | 13.07 |
| 19 | GLM-5.2 | 33.8 | 28.7 | 14.85 |
| 20 | Claude Opus 4.8 | 32.4 | 42.8 | 50.08 |
| 21 | Claude Sonnet 5 | 27.0 | 39.5 | 100.00 |

The current Pareto frontier—undominated on composite cost versus quality—is: **GPT-6 Astra, Gemini 3.8 Flash, GPT-5.6 Sol, Gemini 3.7 Flash, GLM-5.3 Flash**.

## What changed in v1.5

- DeepSWE is refreshed to the live v1.1 Best page: **21 models**, **113 tasks**, source updated **September 3, 2026**.
- Artificial Analysis is migrated to the current **Artificial Analysis Intelligence Index v4.2** identity: AA-Briefcase, GDPval-AA v2, τ³-Banking, Terminal-Bench v2.1, SciCode, AA-LCR v1.1, HLE, GDP.pdf, CritPt, and split AA-Omniscience accuracy/non-hallucination components. GPQA Diamond is retained only as a separately labelled legacy ValueRank input.
- The standalone Terminal-Bench view is replaced by the official **Terminal-Bench 4.0** snapshot: **14 rows**, with **11/21** overlap with the ranked cohort.
- **LiveBench 2026-06-25** supplies the Instruction Following component and Overall-vs-Cost view: **20/21** ranked cohort rows matched, **21** rows published in total, plus **1 official supplemental model** (**Claude Fable 5.1**); the current LiveBench Pareto frontier is **DeepSeek V4 Flash, GLM-5.3 Flash, Gemini 3.7 Flash, Kimi K3, GPT-5.5, GPT-5.6 Sol, Claude Fable 5.1**.
- The ranked pool is **21 models**, with all current DeepSWE entries preserved.
- The score retains **12 zero-gap dimensions**; **Terminal-Bench 4.0, Instruction Following (LiveBench), SciCode** are excluded because each has incomplete official cohort coverage. Missing external values remain null and are not neutral-filled.
- The v4.2 snapshot publishes numeric AA speed for all 21 selected pages, so Speed is now a retained ValueRank dimension.
- AA total evaluation cost is available for 18/21 pages; because coverage is incomplete (GPT-5.5, Claude Opus 4.8, GLM-5.2), the score uses one cohort-wide DeepSWE-only cost mode instead of selectively substituting AA costs.
- Legacy v1.3.1 values are not numerically comparable: the AA benchmark identities and the DeepSWE cohort have changed.

## Sources and audit trail

- [DeepSWE Best](https://deepswe.datacurve.ai/) for pass@1, uncertainty, average cost, output tokens, and agent steps.
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench), pinned at [release data commit 62240f848c977d4202c1029191ac663498745f2f](https://github.com/livebench/new-livebench/commit/62240f848c977d4202c1029191ac663498745f2f), for the 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Refresh record](research/2026-09-06-valuerank-refresh-v4-2/README.md) for the v4.2 source change, evidence boundary, and scoring decisions.
- [Coverage matrix](.refresh/v1.4/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): cohort, benchmark versions, normalization, and zero-gap rule
- [site/index.html](site/index.html): interactive static publication
- [site/tb4/index.html](site/tb4/index.html): current Terminal-Bench 4.0 score-versus-cost publication
- [research/2026-09-06-valuerank-refresh-v4-2/](research/2026-09-06-valuerank-refresh-v4-2/): reproducible v4.2 refresh package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs
