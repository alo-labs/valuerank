# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.9.8
**Updated:** October 18, 2026
**Scope:** 19 primary-ranked models from a 31-model AA-mapped comparison roster, 16 retained dimensions including Bug Hunt Bench

Publication updated October 8, 2026 with the current AA frontier reconciliation and selected benchmark updates. The complete 31-configuration DeepSWE v1.1 chart was observed October 8; the original 25 configuration records retain their earlier per-row observation dates. Earlier AA component snapshots retain their recorded dates, while the newly captured AA frontier profiles are dated October 8 and MiMo owner run notes October 7. See per-model dates and capture precision in raw-data.md.

## Current result

The selected catalog is reconciled against AA's [Intelligence Index score versus total benchmark-run cost Pareto frontier](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), and includes every model family on that observed frontier plus every near-frontier family (see Model inclusion below). The primary score uses each model's available exact-version values across the 16 retained dimensions; missing values remain null and each row's available priorities are renormalized to 100%. Every DeepSWE result retains its displayed agent, model and effort; results from other model versions or composite agents are not transferred. Provider claims fill owner gaps only for the exact benchmark version and evaluated variant, remain visibly labelled, and are replaced by owner results when available. Coverage and missing metrics are shown beside each score.

| Rank | Model | Overall | Quality | AA eval-cost penalty (lower better) | Baseline priority coverage | Missing metrics |
|---:|---|---:|---:|---:|---:|---|
| 1 | Gemini 4 Argon | 74.1 | 82.6 | 27.64 | 84.85% (112/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy), Speed |
| 2 | GPT-6.1 Sol | 70.1 | 71.0 | 12.42 | 88.64% (117/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 3 | Claude Sonnet 5.5 | 69.5 | 85.4 | 83.36 | 88.64% (117/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 4 | GPT-6 Astra | 64.1 | 75.2 | 43.67 | 81.06% (107/132 priority) | Missing: DeepSWE v1.1 |
| 5 | GPT-5.6 Sol | 62.9 | 69.8 | 39.79 | 100.00% (132/132 priority) | Missing: none |
| 6 | Claude Opus 5.5 | 60.3 | 76.7 | 100.00 | 88.64% (117/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 7 | GPT-6 Sol | 58.6 | 59.3 | 17.64 | 92.42% (122/132 priority) | Missing: Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 8 | Grok 4.7 | 56.6 | 66.9 | 57.04 | 92.42% (122/132 priority) | Missing: Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 9 | MiMo-V2.6-Pro | 53.7 | 42.7 | 2.37 | 69.70% (92/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy) |
| 10 | MiMo-V2.6-Flash | 50.7 | 24.5 | 1.26 | 54.55% (72/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy), Bug Hunt Bench |
| 11 | GPT-5.6 Luna | 46.0 | 38.6 | 3.67 | 100.00% (132/132 priority) | Missing: none |
| 12 | Gemini 3.8 Flash | 43.5 | 42.0 | 18.63 | 100.00% (132/132 priority) | Missing: none |
| 13 | GPT-6 Luna | 42.4 | 29.0 | 1.40 | 92.42% (122/132 priority) | Missing: Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 14 | Claude Opus 5 | 40.7 | 48.9 | 83.54 | 100.00% (132/132 priority) | Missing: none |
| 15 | GLM-5.3 | 40.5 | 40.8 | 28.75 | 100.00% (132/132 priority) | Missing: none |
| 16 | Claude Haiku 5.5 | 37.9 | 24.0 | 1.81 | 88.64% (117/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 17 | DeepSeek V4 Flash | 31.4 | 21.9 | 5.45 | 100.00% (132/132 priority) | Missing: none |
| 18 | Qwen3.8 Max | 31.3 | 33.5 | 56.67 | 95.45% (126/132 priority) | Missing: Terminal-Bench 4.0 |
| 19 | DeepSeek V4 Pro | 26.5 | 17.9 | 12.89 | 95.45% (126/132 priority) | Missing: Terminal-Bench 4.0 |

The current Pareto frontier—undominated on composite cost versus quality—is: **GPT-6.1 Sol, GPT-6 Luna, MiMo-V2.6-Pro, MiMo-V2.6-Flash, Claude Sonnet 5.5, Gemini 4 Argon**.

## Model inclusion

**Frontier rule.** Every model family on the Pareto frontier that Artificial Analysis (AA) renders on its Intelligence Index versus total cost to run chart is ranked, with the exact configuration AA selects on that line. Frontier membership is AA's rendered line as observed; ValueRank never recomputes it from rounded values.

**Near-frontier rule.** A plotted configuration is near-frontier when its public (rounded integer) Intelligence Index is within 3 points of the rendered frontier's Index at its cost, meaning the highest Index among rendered-frontier points that cost no more. Every near-frontier family is ranked (its selected configuration may differ from the near configuration) or is explicitly deferred by a dated, reasoned roster decision. The cost ratio to the frontier is reported for information only.

Policy as recorded: A plotted configuration is near-frontier when it lies within 3 Intelligence Index points of the rendered frontier at its cost. Every near-frontier model family must be in the primary ranking, with its own selected configuration, or be explicitly deferred with a dated, reasoned roster decision. The cost ratio to the cheapest frontier point of equal or higher intelligence is reported for information only.

Chart observed 2026-10-17T18:48:27Z (Intelligence Index v4.3.2): 694 catalog models selected, 189 plotted points and 18 rendered Pareto vertices across 7 families. 9 plotted points across 6 families are near-frontier.

Near-frontier models: 6 required, 0 deferred by roster decision.

Frontier families and the configuration selected for each:

- Claude Haiku 5.5: Claude Haiku 5.5 (xhigh)
- Claude Opus 5.5: Claude Opus 5.5 (max with fallback)
- Claude Sonnet 5.5: Claude Sonnet 5.5 (max with fallback)
- GPT-6 Luna: GPT-6 Luna (max)
- GPT-6.1 Sol: GPT-6.1 Sol (max)
- MiMo-V2.6-Flash: MiMo-V2.6-Flash
- MiMo-V2.6-Pro: MiMo-V2.6-Pro

Near-frontier families and the configuration selected for each:

- Claude Haiku 5.5: Claude Haiku 5.5 (low), 1 Index points below the frontier
- Claude Opus 5.5: Claude Opus 5.5 (medium with fallback), 1 Index points below the frontier
- Claude Sonnet 5.5: Claude Sonnet 5.5 (xhigh with fallback), 2 Index points below the frontier
- GPT-5.6 Luna: GPT-5.6 Luna (low), 1 Index points below the frontier
- GPT-6 Astra: GPT-6 Astra (xhigh), 2 Index points below the frontier
- Gemini 4 Argon: Gemini 4 Argon (high), 1 Index points below the frontier

AA footnote (Claude Haiku 5.5): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## Refresh basis and v1.9 scoring update

- The primary rank includes available exact-version evidence for each selected AA frontier model; it does not require every model to have every retained metric. The remaining **12** candidates have no rankable primary score: **Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, GLM-5.2, GLM-5.3 Flash, GPT-5.5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Grok 4.6, Kimi K3, Muse Spark 1.2**.
- For each model, ValueRank retains only its observed metrics, renormalizes that row's available dimension priorities, and reports `availablePriority / totalPriority` coverage plus missing metric names. No missing value receives a zero or neutral fill.
- Bug Hunt Bench has priority **20** and weight **15.15%** in the main rank. DeepSWE v1.1 has priority **25** and weight **18.94%**. A separate Bug Hunt emphasis view gives Bug Hunt still more weight.
- AA's Coding Agent Index v1.5 chart reports **42 configurations** for DeepSWE v1.1 across **113 tasks**, observed **2026-10-17T19:26:26Z**. All configurations and model-version mapping decisions are retained in [data/aa_deepswe.json](data/aa_deepswe.json); **16** configurations map to selected model variants.
- Artificial Analysis now uses **Artificial Analysis Intelligence Index v4.3.2**: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-LCR v1.1, and split AA-Omniscience accuracy/reliability components. τ³-Banking and Terminal-Bench 2.1 remain historical source fields only.
- The standalone Terminal-Bench page has **23 official rows**, including **11/31** direct cohort matches. One separately labelled DeepSeek V4.1-Flash provider claim is used for the current `deepseek-v4-flash` API alias; official and claim counts are kept distinct.
- **[LiveBench](https://livebench.ai/) 2026-06-25** provides the four-task Instruction Following mean plus Overall Score and Cost Per Successful Task views; Instruction Following contributes where a selected model has an eligible value and is included in the row's available-priority calculation.
- The companion Bug Hunt emphasis ranking covers **16** eligible exact-variant owner results and raises Bug Hunt to **21.13%** within that separate view; its ranked table and source snapshot are documented in [scores.md](scores.md#bug-hunt-emphasis-ranking) and [data/bug_hunt.json](data/bug_hunt.json).
- The AA chart's full **42-configuration** DeepSWE v1.1 result set remains available in the raw-data table; model variants and Devin composite-agent results stay separate.
- The score retains **16 primary dimensions**; **none** remain supplemental under the published dimension-selection policy. A missing value in a retained dimension remains null and is omitted from that model's weighted score.
- AA output speed is numeric for **18/19** selected pages; **Gemini 4 Argon** has no value. Where Speed is retained, its weight is applied only to rows with a value and included in their displayed coverage.
- AA total evaluation cost is available for **19/19** primary models. API Costs uses that amount where available; Plan Costs divides the same amount by each model's highest eligible subscription Value Multiple and by its AA Intelligence Index (USD per Index point), and both views renormalize each row over its available dimensions.
- Earlier ValueRank versions are not numerically comparable because this release changes benchmark weights and the ranked cohort.

## Sources and audit trail

- [AA Coding Agent Index v1.5 — DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1) is the benchmark-owner source for all DeepSWE values in this release. The complete 42-configuration chart inventory, observed 2026-10-17T19:26:26Z, and model-variant decisions are recorded in [data/aa_deepswe.json](data/aa_deepswe.json).
- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and the linked first-party model pages for current component values and Intelligence Index evaluation cost.
- [LiveBench](https://livebench.ai/) and its [official release data repository](https://github.com/livebench/new-livebench), pinned at [release data commit 7be9f746f36a6f007dd78461f67cb7d06cfe2304](https://github.com/livebench/new-livebench/commit/7be9f746f36a6f007dd78461f67cb7d06cfe2304), for the 2026-06-25 task/category table, Instruction Following means, Overall Score, and Cost Per Successful Task.
- [Terminal-Bench 4.0](https://www.tbench.ai/) and the [official Harbor repository](https://github.com/harbor-framework/terminal-bench) for the current rendered leaderboard and task identity.
- [Bug Hunt Bench](https://bughunt.productcompass.pm/), with owner-published [combined scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/aec976170df89a371384174ca87646a9a8c82415/results/combined-scoreboard.csv) and [run notes](https://github.com/phuryn/bug-hunt-bench/blob/aec976170df89a371384174ca87646a9a8c82415/results/run-notes.md) pinned to commit **aec976170df89a371384174ca87646a9a8c82415**.
- [Refresh record](research/2026-09-29-valuerank-refresh-v4-3-2/README.md) for the v4.3.2 source change, evidence boundary, provider claims, and scoring decisions.
- [Provider claim ledger](data/provider_claims.json) for provider-sourced values, eligibility, and alias/variant caveats. Provider values never masquerade as benchmark-owner measurements.
- [Coverage matrix](data/coverage_matrix.json) for primary and supplemental availability, including fields not used in the score.

## Files

- [scores.md](scores.md): final ranking, weights, and normalized matrix
- [raw-data.md](raw-data.md): source values, selected AA variants, and supplemental coverage
- [methodology.md](methodology.md): frontier selection, benchmark versions, normalization, and row-level coverage
- [https://valuerank.alolabs.dev/](https://valuerank.alolabs.dev/): website, generated by `valuerank.site.build` (source under [valuerank/site/](valuerank/site/))
- [https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/](https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/): current Terminal-Bench 4.0 score-versus-cost page
- [research/2026-09-29-valuerank-refresh-v4-3-2/](research/2026-09-29-valuerank-refresh-v4-3-2/): reproducible v4.3.2 refresh package
- [data/](data/): machine-readable snapshots and generated outputs (pipeline code lives in [valuerank/](valuerank/))
- [docs/](docs/README.md): contributor documentation (repository layout, architecture, development, testing, refresh and release); `npm run verify` runs every check


## AA intelligence and total-cost comparison

Observed 2026-10-17T18:48:27Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 694 catalog models selected; 189 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 694 models, plotted 189 eligible points, and displayed 18 frontier points. Public metric/export gaps are shown explicitly. All 7 distinct frontier model families are required in the main ranking using exact selected configurations; 7 are included. Other effort configurations remain separate comparison entries. 9 plotted configurations from 6 families lie within 3 Index points of the rendered frontier; 6 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | $10.63 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | $31.17 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | $47.85 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 34 (rounded) | $56.36 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Haiku 5.5 family is represented in the primary ranking by its selected configuration (claude-haiku-5-5-xhigh). No result is transferred between efforts. |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 38 (rounded) | $94.07 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Haiku 5.5 family is represented in the primary ranking by its selected configuration (claude-haiku-5-5-xhigh). No result is transferred between efforts. |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.55 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 41 (rounded) | $157.58 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6.1 Sol family is represented in the primary ranking by its selected configuration (gpt-6-1-sol). No result is transferred between efforts. |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6.1 Sol family is represented in the primary ranking by its selected configuration (gpt-6-1-sol). No result is transferred between efforts. |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6.1 Sol family is represented in the primary ranking by its selected configuration (gpt-6-1-sol). No result is transferred between efforts. |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 56 (rounded) | $7,259.50 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |
| [GPT-5.6 Luna (low)](https://artificialanalysis.ai/models/gpt-5-6-luna-low) | gpt-5-6-luna-low | 21 (rounded) | $27.02 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-5.6 Luna family is represented in the primary ranking by its selected configuration (gpt-5-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 29 (rounded) | $34.31 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the Claude Haiku 5.5 family is represented in the primary ranking by its selected configuration (claude-haiku-5-5-xhigh). No result is transferred between efforts. |
| [Claude Haiku 5.5 (max)](https://artificialanalysis.ai/models/claude-haiku-5-5) | claude-haiku-5-5 | 43 (rounded) | $330.25 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the Claude Haiku 5.5 family is represented in the primary ranking by its selected configuration (claude-haiku-5-5-xhigh). No result is transferred between efforts. |
| [Claude Opus 5.5 (medium with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-medium) | claude-opus-5-5-medium | 51 (rounded) | $1,626.81 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh) | claude-sonnet-5-5-xhigh | 52 (rounded) | $2,176.82 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the Claude Sonnet 5.5 family is represented in the primary ranking by its selected configuration (claude-sonnet-5-5). No result is transferred between efforts. |
| [Gemini 4 Argon (high)](https://artificialanalysis.ai/models/gemini-4-argon) | gemini-4-argon | 53 (rounded) | $2,407.24 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 51 (rounded) | $2,925.01 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-6 Astra family is represented in the primary ranking by its selected configuration (gpt-6-astra-xhigh). No result is transferred between efforts. |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 52 (rounded) | $3,802.98 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 53 (rounded) | $5,324.10 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-6 Astra family is represented in the primary ranking by its selected configuration (gpt-6-astra-xhigh). No result is transferred between efforts. |


## Plan Costs candidate comparison

Plan route evidence as of 2026-10-08. Effective Plan evaluation cost is AA API evaluation cost divided by the highest eligible Value Multiple. Effective Plan cost per Index point is that amount divided by the model's AA Intelligence Index; the Plan-basis rank uses it so that a plan allowance is credited with the work it buys and token-efficient models are rewarded, while models without an eligible route are compared on API cost per Index point. The candidate comparison includes unranked source candidates; a Plan route does not establish a primary composite rank or ValueRank quality frontier membership. For Anthropic and Codex, the user-selected SemiAnalysis analysis supplies controlled subscription-account measurements with workload projections; its allocation regime, workload and evaluated model remain in the route evidence. The common ChatGPT multiples (Plus 8.1×; Pro $100 10.55×; Pro $200 10.42×; Pro $500 10.772×) are a provisional cross-model application: the source projections evaluate Astra for Plus and Sol for the Pro tiers, and do not establish the same allowance for every GPT variant. The common Claude multiples (Pro 58.9×; Max $100 57.25×; Max $200 58.63×) are an owner-authorized (2026-10-18) application of Opus 5.5's measured figures to the other Claude models, not measurements of those models; the same source measured Fable 5.1 at 12.4–12.7× on the Max plans, so the applied multiples may overstate the plan value of cheaper Claude models. The highest eligible common GPT route is Pro $500 at 10.772×. MiMo Pro and MiMo Flash use a provisional user assumption of 1.5×; their subscription fee is not established and their API equivalent dollar numerator is not measured. For other providers, eligible measured routes require actual end-user API-priced usage, exact variants, plan tier and report date in the preceding month. Mixed or unidentified model usage remains provider/plan evidence and does not enter a model route. Provider allowance, quota and marketing figures cannot supply a measured numerator.

| Model | Primary rank | AA Intelligence Index | API evaluation cost | Effective Plan evaluation cost | Effective Plan cost per Index point | Selected plan / multiple | Evidence / source variant | Source date | Source |
|---|---|---|---|---|---|---|---|---|---|
| Gemini 4 Argon | 1 | 52.56 | $2,407.24 | API fallback | $45.80 (API fallback) | No eligible route | API fallback | — | — |
| GPT-6.1 Sol | 2 | 51.83 | $1,081.55 | $100.40 | $1.94 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Sonnet 5.5 | 3 | 56.00 | $7,259.50 | $123.25 | $2.20 | Claude Pro $20 · common Claude assumption / 58.9× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GPT-6 Astra | 4 | 52.39 | $3,802.98 | $353.04 | $6.74 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GPT-5.6 Sol | 5 | 46.97 | $3,464.84 | $321.65 | $6.85 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Opus 5.5 | 6 | 57.62 | $8,708.20 | $147.85 | $2.57 | Claude Pro $20 · Opus 5.5 / 58.9× | Controlled account measurement / workload projection / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GPT-6 Sol | 7 | 47.63 | $1,535.80 | $142.57 | $2.99 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Grok 4.7 | 8 | 46.45 | $4,967.35 | $858.66 | $18.49 | SuperGrok Heavy $300 · Grok 4.7 XHigh / 5.785× | user reported projection / Grok 4.7 XHigh | 2026-09-25 | [Source](https://www.remakebench.com/capacity/plans/supergrok-heavy) |
| MiMo-V2.6-Pro | 9 | 46.32 | $206.66 | $137.77 | $2.97 | MiMo · provisional 1.5x assumption / 1.5× | Provisional assumption | 2026-10-08 | User assumption |
| MiMo-V2.6-Flash | 10 | 37.88 | $109.55 | $73.03 | $1.93 | MiMo · provisional 1.5x assumption / 1.5× | Provisional assumption | 2026-10-08 | User assumption |
| GPT-5.6 Luna | 11 | 37.32 | $319.93 | $29.70 | $0.80 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Gemini 3.8 Flash | 12 | 40.93 | $1,622.73 | API fallback | $39.65 (API fallback) | No eligible route | API fallback | — | — |
| GPT-6 Luna | 13 | 38.12 | $122.05 | $11.33 | $0.30 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Opus 5 | 14 | 50.78 | $7,274.74 | $123.51 | $2.43 | Claude Pro $20 · common Claude assumption / 58.9× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GLM-5.3 | 15 | 44.78 | $2,503.48 | API fallback | $55.91 (API fallback) | No eligible route | API fallback | — | — |
| Claude Haiku 5.5 | 16 | 41.25 | $157.58 | $2.68 | $0.06 | Claude Pro $20 · common Claude assumption / 58.9× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| DeepSeek V4 Flash | 17 | 34.33 | $474.19 | API fallback | $13.81 (API fallback) | No eligible route | API fallback | — | — |
| Qwen3.8 Max | 18 | 45.42 | $4,934.79 | API fallback | $108.66 (API fallback) | No eligible route | API fallback | — | — |
| DeepSeek V4 Pro | 19 | 36.00 | $1,122.27 | API fallback | $31.18 (API fallback) | No eligible route | API fallback | — | — |
| Claude Fable 5 | Unranked candidate | 49.63 | $11,160.86 | $189.49 | $3.82 | Claude Pro $20 · common Claude assumption / 58.9× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Opus 4.8 | Unranked candidate | 41.79 | $6,873.86 | $116.70 | $2.79 | Claude Pro $20 · common Claude assumption / 58.9× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Sonnet 5 | Unranked candidate | 38.16 | $6,998.25 | $118.82 | $3.11 | Claude Pro $20 · common Claude assumption / 58.9× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GLM-5.2 | Unranked candidate | 33.71 | $2,097.29 | API fallback | $62.22 (API fallback) | No eligible route | API fallback | — | — |
| GLM-5.3 Flash | Unranked candidate | 41.81 | $305.52 | API fallback | $7.31 (API fallback) | No eligible route | API fallback | — | — |
| GPT-5.5 | Unranked candidate | 38.36 | $5,294.36 | $491.49 | $12.81 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Gemini 3.5 Flash | Unranked candidate | 32.60 | $4,222.12 | API fallback | $129.52 (API fallback) | No eligible route | API fallback | — | — |
| Gemini 3.6 Flash | Unranked candidate | 33.98 | $1,614.42 | API fallback | $47.51 (API fallback) | No eligible route | API fallback | — | — |
| Gemini 3.7 Flash | Unranked candidate | 39.62 (estimated) | Not established | API fallback | Not established | No eligible route | API fallback | — | — |
| Grok 4.6 | Unranked candidate | 42.84 | $1,557.04 | API fallback | $36.35 (API fallback) | No eligible route | API fallback | — | — |
| Kimi K3 | Unranked candidate | 43.59 | $3,658.07 | API fallback | $83.91 (API fallback) | No eligible route | API fallback | — | — |
| Muse Spark 1.2 | Unranked candidate | 39.58 | $1,385.40 | API fallback | $35.01 (API fallback) | No eligible route | API fallback | — | — |

### Plan route evidence

| Plan | Eligible model variants | Monthly fee | API equivalent numerator | Value Multiple | Evidence / source model | Source date | Source |
|---|---|---|---|---|---|---|---|
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna | $20.00 | $162.00 (applied estimate) | 8.1× | Provisional assumption / GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro $100 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna | $100.00 | $1,055.00 (applied estimate) | 10.55× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro $200 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna | $200.00 | $2,084.00 (applied estimate) | 10.42× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro $500 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna | $500.00 | $5,386.00 (applied estimate) | 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · Opus 5.5 | Claude Opus 5.5 | $20.00 | $1,178.00 | 58.9× | Controlled account measurement / workload projection / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $100 · Opus 5.5 | Claude Opus 5.5 | $100.00 | $5,725.00 | 57.25× | Controlled account measurement / workload projection / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Opus 5.5 | Claude Opus 5.5 | $200.00 | $11,726.00 | 58.63× | Controlled account measurement / workload projection / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| SuperGrok Heavy $300 · Grok 4.7 XHigh | Grok 4.7 | $300.00 | $1,735.50 | 5.785× | user reported projection / Grok 4.7 XHigh | 2026-09-25 | [Source](https://www.remakebench.com/capacity/plans/supergrok-heavy) |
| MiMo · provisional 1.5x assumption | MiMo-V2.6-Pro, MiMo-V2.6-Flash | Not established | Not measured | 1.5× | Provisional assumption | 2026-10-08 | User assumption |
| Claude Pro $20 · common Claude assumption | Claude Opus 5, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 5.5, Claude Sonnet 5.5 | $20.00 | $1,178.00 (applied estimate) | 58.9× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Opus 5, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 5.5, Claude Sonnet 5.5 | $100.00 | $5,725.00 (applied estimate) | 57.25× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Opus 5, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 5.5, Claude Sonnet 5.5 | $200.00 | $11,726.00 (applied estimate) | 58.63× | Provisional assumption / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |

The selected source is [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x). Full route assumptions, allocation regimes, workloads, source links and eligibility are retained in `data/plan_cost_routes.json`.
