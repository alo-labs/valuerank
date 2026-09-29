# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.9.0
**Updated:** September 29, 2026
**Scope:** 9 primary-ranked models from a 21-model AA-mapped comparison roster, 14 retained dimensions including Bug Hunt Bench

## Current result

ValueRank uses AA's [Coding Agent Index v1.5 DeepSWE v1.1 chart](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1), which publishes 25 agent/model configurations across 113 tasks, alongside the 21-model AA-mapped comparison roster. The main score includes 9 rows with an exact DeepSWE model-variant result and an eligible Bug Hunt owner result; the other 12 candidates remain source-only. Every chart result retains its displayed agent and effort, and results from other model versions or composite agents are not transferred. Provider claims fill benchmark-owner gaps only for the exact benchmark version and evaluated variant, remain visibly labelled, and are replaced by owner results when available.

| Rank | Model | Overall | Quality | AA eval-cost penalty (lower better) |
|---:|---|---:|---:|---:|
| 1 | GPT-5.6 Sol | 72.2 | 78.0 | 47.63 |
| 2 | GPT-6 Astra | 68.8 | 80.3 | 52.28 |
| 3 | Grok 4.6 | 55.2 | 50.1 | 26.62 |
| 4 | Kimi K3 | 51.3 | 54.9 | 50.28 |
| 5 | GPT-5.6 Luna | 50.7 | 37.8 | 4.40 |
| 6 | Gemini 3.8 Flash | 50.1 | 40.4 | 22.31 |
| 7 | GLM-5.3 | 37.5 | 31.0 | 34.41 |
| 8 | Claude Opus 5 | 36.5 | 46.0 | 100.00 |
| 9 | Qwen3.8 Max | 27.6 | 31.6 | 67.83 |

The current Pareto frontier—undominated on composite cost versus quality—is: **GPT-6 Astra, Gemini 3.8 Flash, GPT-5.6 Sol, Grok 4.6, GPT-5.6 Luna**.

## Refresh basis and v1.9 scoring update

- **9/21** AA-mapped candidates have both an exact DeepSWE v1.1 chart variant and a Bug Hunt owner result, so only those enter the main composite. The other candidates remain unranked: **Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, DeepSeek V4 Flash, DeepSeek V4 Pro, GLM-5.2, GLM-5.3 Flash, GPT-5.5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Muse Spark 1.2**.
- Bug Hunt Bench has priority **20** and weight **16.53%** in the main rank. DeepSWE v1.1 has priority **25** and weight **20.66%**. A separate Bug Hunt emphasis view gives Bug Hunt still more weight.
- AA's Coding Agent Index v1.5 chart reports **25 configurations** for DeepSWE v1.1 across **113 tasks**, observed **2026-09-29**. All configurations and model-version mapping decisions are retained in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json); **9** configurations map to the current model variants.
- Artificial Analysis now uses **Artificial Analysis Intelligence Index v4.3.2**: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-LCR v1.1, and split AA-Omniscience accuracy/reliability components. τ³-Banking and Terminal-Bench 2.1 remain historical source fields only.
- The standalone Terminal-Bench page has **15 official rows**, including **11/21** direct cohort matches. One separately labelled DeepSeek V4.1-Flash provider claim is used for the current `deepseek-v4-flash` API alias; official and claim counts are kept distinct.
- **[LiveBench](https://livebench.ai/) 2026-06-25** provides the four-task Instruction Following mean plus Overall Score and Cost Per Successful Task views; the primary score includes Instruction Following because it has zero gaps in the exact-match cohort.
- The companion Bug Hunt emphasis ranking covers the same **9** exact-overlap models and raises Bug Hunt to **22.90%**; its ranked table and the full source snapshot are documented in [scores.md](scores.md#bug-hunt-emphasis-ranking) and [.refresh/v1.4/bug_hunt.json](.refresh/v1.4/bug_hunt.json).
- The AA chart's full **25-configuration** DeepSWE v1.1 result set remains available in the raw-data table; model variants and Devin composite-agent results stay separate.
- The score retains **14 zero-gap dimensions**; **Terminal-Bench 4.0, Speed** remain excluded because each has incomplete eligible coverage. Missing values remain null and are not neutral-filled.
- AA output speed is numeric for **8/9** selected pages; **Kimi K3** has no value, so Speed is excluded under the zero-gap rule.
- AA total evaluation cost is available for **9/9** primary models. The API Costs baseline uses it consistently; the Plan Costs basis divides the same value by each model's highest eligible subscription Value Multiple.
- Earlier ValueRank versions are not numerically comparable because this release changes benchmark weights and the ranked cohort.

## Sources and audit trail

- [AA Coding Agent Index v1.5 — DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1) is the benchmark-owner source for all DeepSWE values in this release. The public 25-configuration capture and model-variant decisions are recorded in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json).
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench), pinned at [release data commit 7be9f746f36a6f007dd78461f67cb7d06cfe2304](https://github.com/livebench/new-livebench/commit/7be9f746f36a6f007dd78461f67cb7d06cfe2304), for the 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Bug Hunt Bench](https://bughunt.productcompass.pm/), with owner-published [combined scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv) and [run notes](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/run-notes.md) pinned to commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c**.
- [Refresh record](research/2026-09-29-valuerank-refresh-v4-3-2/README.md) for the v4.3.2 source change, evidence boundary, provider claims, and scoring decisions.
- [Provider claim ledger](.refresh/v1.4/provider_claims.json) for provider-sourced values, eligibility, and alias/variant caveats. Provider values never masquerade as benchmark-owner measurements.
- [Coverage matrix](.refresh/v1.4/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): cohort, benchmark versions, normalization, and zero-gap rule
- [site/index.html](site/index.html): interactive static publication
- [site/tb4/index.html](site/tb4/index.html): current Terminal-Bench 4.0 score-versus-cost publication
- [research/2026-09-29-valuerank-refresh-v4-3-2/](research/2026-09-29-valuerank-refresh-v4-3-2/): reproducible v4.3.2 refresh package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs
