# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.9.4
**Updated:** October 8, 2026
**Scope:** 13 primary-ranked models from a 27-model AA-mapped comparison roster, 12 retained dimensions including Bug Hunt Bench

Publication updated October 8, 2026 with selective MiMo and AA frontier additions. Earlier AA/DeepSWE observations remain dated September 29–30; current MiMo owner run notes were observed October 7. See per-model dates and capture precision in raw-data.md. This publication combines source snapshots with different dates.

## Current result

ValueRank uses AA's [Coding Agent Index v1.5 DeepSWE v1.1 chart](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1), which publishes 25 agent/model configurations across 113 tasks, alongside the 27-model AA-mapped comparison roster. The main score includes 13 rows with an exact DeepSWE model-variant result and an eligible Bug Hunt owner result; the other 14 candidates remain source-only. Every chart result retains its displayed agent and effort, and results from other model versions or composite agents are not transferred. Provider claims fill benchmark-owner gaps only for the exact benchmark version and evaluated variant, remain visibly labelled, and are replaced by owner results when available.

| Rank | Model | Overall | Quality | AA eval-cost penalty (lower better) |
|---:|---|---:|---:|---:|
| 1 | GPT-6 Sol | 70.5 | 66.9 | 17.75 |
| 2 | GPT-5.6 Sol | 70.0 | 75.8 | 39.79 |
| 3 | GPT-6 Astra | 64.8 | 73.9 | 43.67 |
| 4 | Claude Opus 5.5 | 63.6 | 81.9 | 100.00 |
| 5 | Grok 4.7 | 57.8 | 69.6 | 57.04 |
| 6 | GPT-5.6 Luna | 50.8 | 39.0 | 3.67 |
| 7 | Kimi K3 | 49.3 | 51.4 | 42.01 |
| 8 | Grok 4.6 | 48.5 | 43.3 | 22.24 |
| 9 | Gemini 3.8 Flash | 41.5 | 31.9 | 18.63 |
| 10 | GLM-5.3 | 36.3 | 30.0 | 28.75 |
| 11 | GPT-6 Luna | 35.6 | 17.1 | 1.40 |
| 12 | Claude Opus 5 | 34.7 | 42.3 | 83.54 |
| 13 | Qwen3.8 Max | 26.5 | 26.9 | 56.67 |

The current Pareto frontier—undominated on composite cost versus quality—is: **GPT-5.6 Sol, GPT-5.6 Luna, Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna**.

## Refresh basis and v1.9 scoring update

- **13/27** AA-mapped candidates have both an exact DeepSWE v1.1 chart variant and a Bug Hunt owner result, so only those enter the main composite. The other candidates remain unranked: **Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, DeepSeek V4 Flash, DeepSeek V4 Pro, GLM-5.2, GLM-5.3 Flash, GPT-5.5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, MiMo-V2.6-Flash, MiMo-V2.6-Pro, Muse Spark 1.2**.
- Bug Hunt Bench has priority **20** and weight **17.86%** in the main rank. DeepSWE v1.1 has priority **25** and weight **22.32%**. A separate Bug Hunt emphasis view gives Bug Hunt still more weight.
- AA's Coding Agent Index v1.5 chart reports **25 configurations** for DeepSWE v1.1 across **113 tasks**, observed **2026-09-29**. All configurations and model-version mapping decisions are retained in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json); **13** configurations map to the current model variants.
- Artificial Analysis now uses **Artificial Analysis Intelligence Index v4.3.2**: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-LCR v1.1, and split AA-Omniscience accuracy/reliability components. τ³-Banking and Terminal-Bench 2.1 remain historical source fields only.
- The standalone Terminal-Bench page has **15 official rows**, including **11/27** direct cohort matches. One separately labelled DeepSeek V4.1-Flash provider claim is used for the current `deepseek-v4-flash` API alias; official and claim counts are kept distinct.
- **[LiveBench](https://livebench.ai/) 2026-06-25** provides the four-task Instruction Following mean plus Overall Score and Cost Per Successful Task views; the primary score includes Instruction Following because it has zero gaps in the exact-match cohort.
- The companion Bug Hunt emphasis ranking covers the same **13** exact-overlap models and raises Bug Hunt to **24.59%**; its ranked table and the full source snapshot are documented in [scores.md](scores.md#bug-hunt-emphasis-ranking) and [.refresh/v1.4/bug_hunt.json](.refresh/v1.4/bug_hunt.json).
- The AA chart's full **25-configuration** DeepSWE v1.1 result set remains available in the raw-data table; model variants and Devin composite-agent results stay separate.
- The score retains **12 zero-gap dimensions**; **Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy), Speed** remain excluded because each has incomplete eligible coverage. Missing values remain null and are not neutral-filled.
- AA output speed is numeric for **12/13** selected pages; **Kimi K3** has no value, so Speed is excluded under the zero-gap rule.
- AA total evaluation cost is available for **13/13** primary models. The API Costs baseline uses it consistently; the Plan Costs basis divides the same value by each model's highest eligible subscription Value Multiple.
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


## AA intelligence and total-cost comparison

Observed 2026-10-07T14:23:09Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 691 catalog models selected; 173 eligible plotted points. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 691 models, plotted 173 eligible points, and displayed 14 frontier points. Public metric/export gaps are shown explicitly.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.41 | Observed AA frontier | Unranked source candidate | No eligible exact-variant Bug Hunt match; owner default result 23.3/105 available; selected reasoning equivalence is unverified; No exact-variant AA DeepSWE result in the selected source snapshot |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Unranked source candidate | No exact-variant AA DeepSWE result in the selected source snapshot |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | Not publicly captured | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Lower-effort comparison candidate retained explicitly; the current selected roster uses Opus max with fallback. Exact-variant benchmark coverage has not been collected, and max results cannot be transferred. |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Lower-effort comparison candidate retained explicitly; the current selected roster uses Opus max with fallback. Exact-variant benchmark coverage has not been collected, and max results cannot be transferred. |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: New-generation frontier candidate explicitly retained for subsequent exact benchmark ingestion. This correction ingests the two MiMo models; the existing roster contains GPT-6 Sol, not GPT-6.1 Sol. No older-generation result is transferred. |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Exact-effort comparison candidate retained explicitly for subsequent ingestion; the current selected roster has GPT-6 Sol max, not this generation. Exact-variant benchmark coverage has not been collected, and no other effort or generation is transferred. |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Exact-effort comparison candidate retained explicitly for subsequent ingestion; the current selected roster has GPT-6 Sol max, not this generation. Exact-variant benchmark coverage has not been collected, and no other effort or generation is transferred. |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Exact-effort comparison candidate retained explicitly for subsequent ingestion; the current selected roster has GPT-6 Sol max, not this generation. Exact-variant benchmark coverage has not been collected, and no other effort or generation is transferred. |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | Not publicly captured | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Lower-effort comparison candidate retained explicitly; the current selected roster uses Luna max. Exact-variant benchmark coverage has not been collected, and max results cannot be transferred. |
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Lower-effort comparison candidate retained explicitly; the current selected roster uses Luna max. Exact-variant benchmark coverage has not been collected, and max results cannot be transferred. |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Lower-effort comparison candidate retained explicitly; the current selected roster uses Luna max. Exact-variant benchmark coverage has not been collected, and max results cannot be transferred. |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | Not publicly captured | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T14:23:09Z: Lower-effort comparison candidate retained explicitly; the current selected roster uses Luna max. Exact-variant benchmark coverage has not been collected, and max results cannot be transferred. |
