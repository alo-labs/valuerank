# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.7.0
**Updated:** September 29, 2026
**Scope:** 21 models from the current DeepSWE Best roster, 12 retained zero-gap dimensions

## Current result

ValueRank combines the current [DeepSWE Best](https://deepswe.datacurve.ai/) agent results with [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) v4.3.2 and the updated external benchmark views. The complete current DeepSWE Best roster is retained. Exact-version provider claims fill eligible benchmark-owner gaps and remain visibly labelled; unmatched cells stay null.

| Rank | Model | Overall | Quality | Composite Cost |
|---:|---|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 68.4 | 67.6 | 8.94 |
| 2 | GPT-6 Astra | 64.7 | 78.7 | 16.78 |
| 3 | Grok 4.6 | 63.0 | 63.2 | 13.07 |
| 4 | GLM-5.3 Flash | 59.6 | 40.6 | 0.91 |
| 5 | Gemini 3.7 Flash | 57.6 | 47.1 | 7.69 |
| 6 | GPT-5.6 Sol | 57.2 | 72.4 | 24.47 |
| 7 | Kimi K3 | 56.3 | 68.6 | 17.61 |
| 8 | Claude Fable 5 | 54.6 | 78.0 | 50.80 |
| 9 | Qwen3.8 Max | 54.4 | 56.4 | 14.13 |
| 10 | Claude Opus 5 | 53.9 | 72.3 | 44.85 |
| 11 | GLM-5.3 | 52.9 | 59.0 | 15.11 |
| 12 | GPT-5.6 Luna | 51.7 | 33.7 | 2.31 |
| 13 | Muse Spark 1.2 | 49.0 | 46.2 | 14.02 |
| 14 | DeepSeek V4 Pro | 48.5 | 31.3 | 6.33 |
| 15 | Gemini 3.6 Flash | 45.1 | 30.9 | 8.37 |
| 16 | DeepSeek V4 Flash | 41.7 | 16.5 | 1.74 |
| 17 | GPT-5.5 | 41.7 | 51.9 | 27.39 |
| 18 | Gemini 3.5 Flash | 38.6 | 27.3 | 13.07 |
| 19 | Claude Opus 4.8 | 36.1 | 48.4 | 50.08 |
| 20 | GLM-5.2 | 29.9 | 22.8 | 14.85 |
| 21 | Claude Sonnet 5 | 25.2 | 37.1 | 100.00 |

The current Pareto frontier—undominated on composite cost versus quality—is: **GPT-6 Astra, Gemini 3.8 Flash, Gemini 3.7 Flash, GLM-5.3 Flash**.

## What changed in v1.7

- DeepSWE is refreshed to the live v1.1 Best page: **21 models**, **113 tasks**, source updated **September 22, 2026**.
- Artificial Analysis now uses **Artificial Analysis Intelligence Index v4.3.2**: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-LCR v1.1, and split AA-Omniscience accuracy/reliability components. τ³-Banking and Terminal-Bench 2.1 remain historical source fields only.
- The standalone Terminal-Bench page has **15 official rows**, including **11/21** direct cohort matches. One separately labelled DeepSeek V4.1-Flash provider claim is used for the current `deepseek-v4-flash` API alias; official and claim counts are kept distinct.
- **[LiveBench](https://livebench.ai/) 2026-06-25** has **21/21** ranked cohort rows matched and **64** published rows, plus **1 official supplemental model** (**Claude Fable 5.1**); its seven-category Pareto frontier is **DeepSeek V4 Flash, GLM-5.3 Flash, Gemini 3.7 Flash, Kimi K3, GPT-5.5, GPT-5.6 Sol, GPT-6 Astra, Claude Fable 5.1**. Complete LiveBench Instruction Following coverage now makes that dimension eligible for the primary score.
- Bug Hunt Bench adds a separate matched-cohort emphasis ranking for **16/21** models. It has a **20.41%** weight in that alternate ranking; the full 21-model primary score and its zero-gap rule are unchanged. The provider-claim audit found no matching provider result for the five uncovered entries.
- The ranked pool is **21 models**, with all current DeepSWE entries preserved.
- The score retains **12 zero-gap dimensions**; **Terminal-Bench 4.0, AutomationBench-AA, Speed** remain excluded because each has incomplete eligible coverage. Missing values remain null and are not neutral-filled.
- AA output speed is numeric for **20/21** selected pages; **Kimi K3** has no value, so Speed is excluded under the zero-gap rule.
- AA total evaluation cost is available for 20/21 pages; because coverage is incomplete (Gemini 3.7 Flash), the score uses one cohort-wide DeepSWE-only cost mode instead of selectively substituting AA costs.
- Legacy v1.3.1 values are not numerically comparable: the AA benchmark identities and the DeepSWE cohort have changed.

## Sources and audit trail

- [DeepSWE Best](https://deepswe.datacurve.ai/) for pass@1, uncertainty, average cost, output tokens, and agent steps.
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench), pinned at [release data commit 7be9f746f36a6f007dd78461f67cb7d06cfe2304](https://github.com/livebench/new-livebench/commit/7be9f746f36a6f007dd78461f67cb7d06cfe2304), for the 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Bug Hunt Bench](https://bughunt.productcompass.pm/), its [owner-published combined scoreboard pinned to commit 0630b120a81363c343ed7dfaf3c6d3be7f7da38c](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv), and the matching [run notes](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/run-notes.md).
- [Refresh record](research/2026-09-29-valuerank-refresh-v4-3-2/README.md) for the v4.3.2 source change, evidence boundary, provider claims, and scoring decisions.
- [Provider claim ledger](.refresh/v1.4/provider_claims.json) for provider-sourced values, eligibility, and alias/variant caveats. Provider values never masquerade as benchmark-owner measurements.
- [Coverage matrix](.refresh/v1.4/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.
- [Bug Hunt source and match ledger](.refresh/v1.4/bug_hunt.json) for the pinned owner snapshot, exact variant/harness matches, and exclusions.
- [Bug Hunt integration research note](research/2026-09-29-bug-hunt-bench-integration/README.md) for the cohort, claim policy, scoring decision, and caveats.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): cohort, benchmark versions, normalization, and zero-gap rule
- [site/index.html](site/index.html): interactive static publication
- [site/tb4/index.html](site/tb4/index.html): current Terminal-Bench 4.0 score-versus-cost publication
- [research/2026-09-29-valuerank-refresh-v4-3-2/](research/2026-09-29-valuerank-refresh-v4-3-2/): reproducible v4.3.2 refresh package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs
