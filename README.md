# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.9.6
**Updated:** October 8, 2026
**Scope:** 16 primary-ranked models from a 28-model AA-mapped comparison roster, 16 retained dimensions including Bug Hunt Bench

Publication updated October 8, 2026 with the current AA frontier reconciliation and selected benchmark updates. The complete 31-configuration DeepSWE v1.1 chart was observed October 8; the original 25 configuration records retain their earlier per-row observation dates. Earlier AA component snapshots retain their recorded dates, while the newly captured AA frontier profiles are dated October 8 and MiMo owner run notes October 7. See per-model dates and capture precision in raw-data.md.

## Current result

The selected catalog is reconciled against AA's [Intelligence Index score versus total benchmark-run cost Pareto frontier](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index), and includes every model represented on that observed frontier. The primary score uses each model's available exact-version values across the 16 retained dimensions; missing values remain null and each row's available priorities are renormalized to 100%. Every DeepSWE result retains its displayed agent, model and effort; results from other model versions or composite agents are not transferred. Provider claims fill owner gaps only for the exact benchmark version and evaluated variant, remain visibly labelled, and are replaced by owner results when available. Coverage and missing metrics are shown beside each score.

| Rank | Model | Overall | Quality | AA eval-cost penalty (lower better) | Baseline priority coverage | Missing metrics |
|---:|---|---:|---:|---:|---:|---|
| 1 | GPT-6.1 Sol | 74.3 | 74.6 | 12.42 | 88.64% (117/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 2 | GPT-5.6 Sol | 65.5 | 71.5 | 39.79 | 100.00% (132/132 priority) | Missing: none |
| 3 | GPT-6 Astra | 64.2 | 72.9 | 43.67 | 100.00% (132/132 priority) | Missing: none |
| 4 | GPT-6 Sol | 61.9 | 60.7 | 17.75 | 92.42% (122/132 priority) | Missing: Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 5 | Claude Opus 5.5 | 61.6 | 78.4 | 100.00 | 88.64% (117/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 6 | Grok 4.7 | 58.4 | 70.1 | 57.04 | 92.42% (122/132 priority) | Missing: Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 7 | MiMo-V2.6-Pro | 54.1 | 41.9 | 2.37 | 69.70% (92/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy) |
| 8 | MiMo-V2.6-Flash | 51.6 | 25.8 | 1.26 | 54.55% (72/132 priority) | Missing: Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy), Bug Hunt Bench |
| 9 | Kimi K3 | 46.2 | 49.6 | 42.01 | 91.67% (121/132 priority) | Missing: Terminal-Bench 4.0, Speed |
| 10 | Grok 4.6 | 45.6 | 43.8 | 22.24 | 100.00% (132/132 priority) | Missing: none |
| 11 | GPT-5.6 Luna | 43.3 | 34.8 | 3.67 | 100.00% (132/132 priority) | Missing: none |
| 12 | Gemini 3.8 Flash | 42.7 | 38.7 | 18.63 | 100.00% (132/132 priority) | Missing: none |
| 13 | GLM-5.3 | 36.7 | 34.3 | 28.75 | 100.00% (132/132 priority) | Missing: none |
| 14 | GPT-6 Luna | 36.5 | 21.8 | 1.40 | 92.42% (122/132 priority) | Missing: Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 15 | Claude Opus 5 | 35.8 | 42.6 | 83.54 | 100.00% (132/132 priority) | Missing: none |
| 16 | Qwen3.8 Max | 26.7 | 28.3 | 56.67 | 95.45% (126/132 priority) | Missing: Terminal-Bench 4.0 |

The current Pareto frontier—undominated on composite cost versus quality—is: **Claude Opus 5.5, GPT-6.1 Sol, MiMo-V2.6-Pro, MiMo-V2.6-Flash**.

## Refresh basis and v1.9 scoring update

- The primary rank includes available exact-version evidence for each selected AA frontier model; it does not require every model to have every retained metric. The remaining **12** candidates have no rankable primary score: **Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, DeepSeek V4 Flash, DeepSeek V4 Pro, GLM-5.2, GLM-5.3 Flash, GPT-5.5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Muse Spark 1.2**.
- For each model, ValueRank retains only its observed metrics, renormalizes that row's available dimension priorities, and reports `availablePriority / totalPriority` coverage plus missing metric names. No missing value receives a zero or neutral fill.
- Bug Hunt Bench has priority **20** and weight **15.15%** in the main rank. DeepSWE v1.1 has priority **25** and weight **18.94%**. A separate Bug Hunt emphasis view gives Bug Hunt still more weight.
- AA's Coding Agent Index v1.5 chart reports **31 configurations** for DeepSWE v1.1 across **113 tasks**, observed **2026-10-08**. All configurations and model-version mapping decisions are retained in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json); **14** configurations map to selected model variants.
- Artificial Analysis now uses **Artificial Analysis Intelligence Index v4.3.2**: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-LCR v1.1, and split AA-Omniscience accuracy/reliability components. τ³-Banking and Terminal-Bench 2.1 remain historical source fields only.
- The standalone Terminal-Bench page has **14 official rows**, including **11/28** direct cohort matches. One separately labelled DeepSeek V4.1-Flash provider claim is used for the current `deepseek-v4-flash` API alias; official and claim counts are kept distinct.
- **[LiveBench](https://livebench.ai/) 2026-06-25** provides the four-task Instruction Following mean plus Overall Score and Cost Per Successful Task views; Instruction Following contributes where a selected model has an eligible value and is included in the row's available-priority calculation.
- The companion Bug Hunt emphasis ranking covers **14** eligible exact-variant owner results and raises Bug Hunt to **21.13%** within that separate view; its ranked table and source snapshot are documented in [scores.md](scores.md#bug-hunt-emphasis-ranking) and [.refresh/v1.4/bug_hunt.json](.refresh/v1.4/bug_hunt.json).
- The AA chart's full **31-configuration** DeepSWE v1.1 result set remains available in the raw-data table; model variants and Devin composite-agent results stay separate.
- The score retains **16 primary dimensions**; **none** remain supplemental under the published dimension-selection policy. A missing value in a retained dimension remains null and is omitted from that model's weighted score.
- AA output speed is numeric for **15/16** selected pages; **Kimi K3** has no value. Where Speed is retained, its weight is applied only to rows with a value and included in their displayed coverage.
- AA total evaluation cost is available for **16/16** primary models. API Costs uses that amount where available; Plan Costs divides the same amount by each model's highest eligible subscription Value Multiple, and both views renormalize each row over its available dimensions.
- Earlier ValueRank versions are not numerically comparable because this release changes benchmark weights and the ranked cohort.

## Sources and audit trail

- [AA Coding Agent Index v1.5 — DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1) is the benchmark-owner source for all DeepSWE values in this release. The complete 31-configuration chart inventory, observed 2026-10-08, and model-variant decisions are recorded in [.refresh/v1.4/aa_deepswe.json](.refresh/v1.4/aa_deepswe.json).
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
- [methodology.md](methodology.md): frontier selection, benchmark versions, normalization, and row-level coverage
- [site/index.html](site/index.html): interactive static publication
- [site/tb4/index.html](site/tb4/index.html): current Terminal-Bench 4.0 score-versus-cost publication
- [research/2026-09-29-valuerank-refresh-v4-3-2/](research/2026-09-29-valuerank-refresh-v4-3-2/): reproducible v4.3.2 refresh package
- [.refresh/v1.4/](.refresh/v1.4/): refresh scripts and machine-readable snapshots/outputs


## AA intelligence and total-cost comparison

Observed 2026-10-07T16:22:14Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 691 catalog models selected; 173 eligible plotted points. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 691 models, plotted 173 eligible points, and displayed 14 frontier points. Public metric/export gaps are shown explicitly. All 5 distinct frontier model families are required in the main ranking using exact selected configurations; 5 are included. Other effort configurations remain separate comparison entries.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | $10.63 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | $31.17 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | $47.85 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.41 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-07T16:22:14Z: Alternate effort retained in the AA frontier comparison; the same model family is required in the primary ranking using its selected exact frontier configuration. No result is transferred between efforts. |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |


## Plan Costs candidate comparison

Plan route evidence as of 2026-10-08. Effective Plan evaluation cost is AA API evaluation cost divided by the highest eligible Value Multiple. The candidate comparison includes unranked source candidates; a Plan route does not establish a primary composite rank or ValueRank quality frontier membership. For Anthropic and Codex, the user-selected SemiAnalysis analysis supplies controlled subscription-account measurements with workload projections; its allocation regime, workload and evaluated model remain in the route evidence. The common ChatGPT multiples (Plus 8.1×; Pro $100 10.55×; Pro $200 10.42×; Pro $500 10.772×) are a provisional cross-model application: the source projections evaluate Astra for Plus and Sol for the Pro tiers, and do not establish the same allowance for every GPT variant. The highest eligible common GPT route is Pro $500 at 10.772×. MiMo Pro and MiMo Flash use a provisional user assumption of 1.5×; their subscription fee is not established and their API equivalent dollar numerator is not measured. For other providers, eligible measured routes require actual end-user API-priced usage, exact variants, plan tier and report date in the preceding month. Mixed or unidentified model usage remains provider/plan evidence and does not enter a model route. Provider allowance, quota and marketing figures cannot supply a measured numerator.

| Model | Primary rank | AA Intelligence Index | API evaluation cost | Effective Plan evaluation cost | Selected plan / multiple | Evidence / source variant | Source date | Source |
|---|---|---|---|---|---|---|---|---|
| GPT-6.1 Sol | 1 | 52.00 | $1,081.55 | $100.40 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GPT-5.6 Sol | 2 | 46.97 | $3,464.84 | $321.65 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GPT-6 Astra | 3 | 52.39 | $3,802.98 | $353.04 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| GPT-6 Sol | 4 | 47.53 | $1,545.83 | $143.50 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Opus 5.5 | 5 | 57.62 | $8,708.20 | $147.85 | Claude Pro $20 · Opus 5.5 / 58.9× | Controlled account measurement / workload projection / Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Grok 4.7 | 6 | 46.45 | $4,967.35 | $858.66 | SuperGrok Heavy $300 · Grok 4.7 XHigh / 5.785× | user reported projection / Grok 4.7 XHigh | 2026-09-25 | [Source](https://www.remakebench.com/capacity/plans/supergrok-heavy) |
| MiMo-V2.6-Pro | 7 | 46 (rounded) | $206.66 | $137.77 | MiMo · provisional 1.5x assumption / 1.5× | Provisional assumption | 2026-10-08 | User assumption |
| MiMo-V2.6-Flash | 8 | 38 (rounded) | $109.41 | $72.94 | MiMo · provisional 1.5x assumption / 1.5× | Provisional assumption | 2026-10-08 | User assumption |
| Kimi K3 | 9 | 43.59 | $3,658.07 | API fallback | No eligible route | API fallback | — | — |
| Grok 4.6 | 10 | 42.84 | $1,936.75 | API fallback | No eligible route | API fallback | — | — |
| GPT-5.6 Luna | 11 | 37.32 | $319.93 | $29.70 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Gemini 3.8 Flash | 12 | 40.93 | $1,622.73 | API fallback | No eligible route | API fallback | — | — |
| GLM-5.3 | 13 | 44.78 | $2,503.48 | API fallback | No eligible route | API fallback | — | — |
| GPT-6 Luna | 14 | 37.26 | $122.05 | $11.33 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Opus 5 | 15 | 50.78 | $7,274.74 | API fallback | No eligible route | API fallback | — | — |
| Qwen3.8 Max | 16 | 45.42 | $4,934.79 | API fallback | No eligible route | API fallback | — | — |
| Claude Fable 5 | Unranked candidate | 49.63 | $11,160.86 | API fallback | No eligible route | API fallback | — | — |
| Claude Opus 4.8 | Unranked candidate | 41.79 | $6,873.86 | API fallback | No eligible route | API fallback | — | — |
| Claude Sonnet 5 | Unranked candidate | 38.16 | $6,998.25 | API fallback | No eligible route | API fallback | — | — |
| DeepSeek V4 Flash | Unranked candidate | 34.33 | $474.19 | API fallback | No eligible route | API fallback | — | — |
| DeepSeek V4 Pro | Unranked candidate | 36.00 | $1,122.27 | API fallback | No eligible route | API fallback | — | — |
| GLM-5.2 | Unranked candidate | 33.71 | $2,097.29 | API fallback | No eligible route | API fallback | — | — |
| GLM-5.3 Flash | Unranked candidate | 41.81 | $280.28 | API fallback | No eligible route | API fallback | — | — |
| GPT-5.5 | Unranked candidate | 38.36 | $5,294.36 | $491.49 | ChatGPT Pro $500 · common GPT assumption / 10.772× | Provisional assumption / GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Gemini 3.5 Flash | Unranked candidate | 32.60 | $2,172.43 | API fallback | No eligible route | API fallback | — | — |
| Gemini 3.6 Flash | Unranked candidate | 33.98 | $1,036.81 | API fallback | No eligible route | API fallback | — | — |
| Gemini 3.7 Flash | Unranked candidate | 39.62 (estimated) | Not established | API fallback | No eligible route | API fallback | — | — |
| Muse Spark 1.2 | Unranked candidate | 39.58 | $1,385.40 | API fallback | No eligible route | API fallback | — | — |

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

The selected source is [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x). Full route assumptions, allocation regimes, workloads, source links and eligibility are retained in `.refresh/v1.4/plan_cost_routes.json`.
