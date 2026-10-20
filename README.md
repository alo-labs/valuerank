# ValueRank
**Frontier AI configurations ranked by value: benchmark quality against what the work costs**

**Version:** v3.0.0
**Updated:** October 19, 2026
**Methodology:** 3.0.0 · SDLC basket v1 · anchor version v3-2026-10-19
**Scope:** 19 ranked configurations from a 31-model AA-mapped roster; value is a 25% cost score plus 75% quality over 11 benchmark leaves

## Current result

ValueRank ranks frontier AI model configurations (see Model inclusion) by value for software-development work, separately for API buyers and for subscription (Plan) buyers. Value is a fixed **25%** cost score plus **75%** benchmark quality. Cost is the contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost): Artificial Analysis' (AA) published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, scored on a log scale against frozen anchors so cost ratios keep their size. Quality is the weighted mean of 11 benchmark leaves on fixed 0–100 anchors, over the leaves observed for the exact configuration; missing evidence is never filled in. The Plan ranking divides the basket's API cost by the selected subscription route's Value Multiple at full utilisation, and uses the API cost, flagged, when no route is admitted. No Value Multiple is yet identified on the basket itself (0 of 19 rows), so the Plan ranking is labelled exploratory.

Claude Sonnet 5.5 leads the Plan ranking at 61.1; MiMo-V2.6-Flash leads the API ranking at 60.9 (subset cost, provisional quality); Gemini 4 Argon leads on quality.

| Plan rank | API rank | Configuration | Plan value | API value | Quality | Quality coverage | API cost (USD per basket run) | Plan cost (USD per basket run) | Plan route | Flags |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 13 | [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 61.1 | 51.6 | 64.3 | 100% | $9,373.65 | $159.15 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 2 | 14 | [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 60.9 | 51.2 | 64.2 | 100% | $9,989.15 | $169.60 | Claude Pro $20 · Opus 5.5 (58.9×, measured) | — |
| 3 | 2 | [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 59.8 | 58.1 | 61.3 | 100% | $1,267.66 | $117.68 | ChatGPT Pro $500 · common GPT assumption (10.772×, measured) | — |
| 4 | 10 | [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 57.0 | 52.5 | 45.4 | 90% | $292.07 | $4.96 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat |
| 5 | 8 | [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 56.6 | 53.8 | 63.8 | 40% | $2,899.42 | $357.95 | ChatGPT Plus $20 · common GPT assumption (8.1×, measured) | subset cost, provisional quality |
| 6 | 18 | [Claude Opus 5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5/) | 56.5 | 47.0 | 57.8 | 80% | $8,733.13 | $148.27 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 7 | 9 | [GPT-6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-sol/) | 56.2 | 53.8 | 58.3 | 90% | $1,999.41 | $185.61 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 8 | 3 | [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 56.1 | 57.8 | 47.7 | 100% | $132.87 | $12.33 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 9 | 6 | [GPT-5.6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-5-6-luna/) | 55.3 | 55.6 | 50.0 | 90% | $319.25 | $29.64 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 10 | 12 | [GPT-5.6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-5-6-sol/) | 55.0 | 51.6 | 59.7 | 90% | $4,238.14 | $393.44 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 11 | 1 | [MiMo-V2.6-Flash](https://valuerank.alolabs.dev/models/mimo-v2-6-flash/) | 53.5 | 60.9 | 51.7 | 50% | $60.37 | $40.25 | MiMo · provisional 1.5x assumption (1.5×, assumption) | subset cost, provisional quality |
| 12 | 4 | [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 52.8 | 56.4 | 65.3 | 90% | $3,628.64 | $3,628.64 | — | API-cost fallback |
| 13 | 5 | [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 50.0 | 56.3 | 50.1 | 60% | $136.13 | $90.75 | MiMo · provisional 1.5x assumption (1.5×, assumption) | subset cost, provisional quality |
| 14 | 7 | [DeepSeek V4 Flash (max)](https://valuerank.alolabs.dev/models/deepseek-v4-flash/) | 47.3 | 54.8 | 48.1 | 80% | $279.51 | $279.51 | — | API-cost fallback |
| 15 | 11 | [DeepSeek V4 Pro (max)](https://valuerank.alolabs.dev/models/deepseek-v4-pro/) | 45.7 | 51.6 | 50.0 | 80% | $801.50 | $801.50 | — | API-cost fallback |
| 16 | 16 | [Grok 4.7 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-7/) | 44.5 | 47.3 | 56.7 | 100% | $6,700.02 | $6,700.02 | — | API-cost fallback |
| 17 | 17 | [GLM-5.3 (max)](https://valuerank.alolabs.dev/models/glm-5-3/) | 43.2 | 47.1 | 52.1 | 100% | $3,186.29 | $3,186.29 | — | API-cost fallback |
| 18 | 15 | [Gemini 3.8 Flash (high)](https://valuerank.alolabs.dev/models/gemini-3-8-flash/) | 43.1 | 47.6 | 50.3 | 100% | $2,073.44 | $2,073.44 | — | API-cost fallback |
| 19 | 19 | [Qwen3.8 Max](https://valuerank.alolabs.dev/models/qwen3-8-max/) | 38.4 | 41.5 | 47.7 | 100% | $5,417.03 | $5,417.03 | — | API-cost fallback |

Values are rounded for display; ranks are competition ranks (equal values share the better rank).

- **subset cost**: scored on the workload of the components it has, against that workload's own anchors; its ordering against main-workload rows is not identified (O17).
- **provisional quality**: observed leaves cover under 70% of quality weight, fewer than two software-engineering leaves or under 40% software-engineering weight are observed, or DeepSWE is missing; ranked and flagged, never floored (O8).
- **partial component**: AA marks tasks of a basket component missing or declined (E37).
- **AA cost caveat**: AA states that its published cost omits a pricing term.
- **API-cost fallback**: no admitted Plan route; the Plan ranking uses the API cost (O13).

Not ranked (12 roster models): Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, GLM-5.2, GLM-5.3 Flash, GPT-5.5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Grok 4.6, Kimi K3, Muse Spark 1.2. Reasons are listed in [scores.md](scores.md#not-ranked).

### What the evidence supports

- API basis, main workload: the definite frontier (no configuration can beat it on both cost and quality anywhere inside the published record's precision and missing-evidence bounds) is GPT-6.1 Sol (max), GPT-6 Luna (max); the possible frontier adds Gemini 4 Argon (high), Claude Sonnet 5.5 (max), GPT-5.6 Sol (max), GPT-6 Sol (max), GPT-5.6 Luna (max), Claude Haiku 5.5 (xhigh), Claude Opus 5 (max), DeepSeek V4 Flash (max), DeepSeek V4 Pro (max). Not evaluable on this workload: GPT-6 Astra (xhigh), MiMo-V2.6-Flash, MiMo-V2.6-Pro. Cheapest at or above GPT-6 Luna (max)'s quality: GPT-6 Luna (max) (confirmed).
- Plan basis: interval outputs not evaluated (no row has FullCost and an identified M_W (E61/E67)).

Scenario shares by stream, diagnostics and the release gates are in [scores.md](scores.md); the inputs behind every number are in [raw-data.md](raw-data.md).

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

- Claude Haiku 5.5: Claude Haiku 5.5 (low), 1 Index point below the frontier
- Claude Opus 5.5: Claude Opus 5.5 (medium with fallback), 1 Index point below the frontier
- Claude Sonnet 5.5: Claude Sonnet 5.5 (xhigh with fallback), 2 Index points below the frontier
- GPT-5.6 Luna: GPT-5.6 Luna (low), 1 Index point below the frontier
- GPT-6 Astra: GPT-6 Astra (xhigh), 2 Index points below the frontier
- Gemini 4 Argon: Gemini 4 Argon (high), 1 Index point below the frontier

AA footnote (Claude Haiku 5.5): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## How v3 scores value

- **Cost is the SDLC basket.** SDLC basket v1: AA's published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, in USD per basket run. Pending capture: FrontierCode, ITBench-AA. v2 used AA's cost to run the whole Intelligence Index per Index point.
- **Cost keeps its magnitude.** The cost score is 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100, against anchors frozen with anchor version `v3-2026-10-19`. A model entering or leaving the cohort does not move another model's score. At the API anchors, doubling cost costs 3.04 value points, which 4.05 quality points offset.
- **Quality is measured, not ranked.** Each of the 11 leaves is placed on fixed 0–100 anchors from its raw value, so quality no longer depends on which other models are ranked. A missing leaf is left out of that configuration's mean, its coverage is shown, and low coverage marks the row provisional.
- **Plan value is route evidence.** Each subscription route carries its Value Multiple, evidence grade (controlled measurement, concordant reports, owner-named assumption) and identification status; the Plan ranking is labelled exploratory until multiples are identified on the basket.
- **Uncertainty is shown, not hidden.** Interval outputs certify which frontier and cheapest-above-a-bar claims the published record supports; scenario shares report frequencies over declared streams.
- v3 values are not numerically comparable with v2 or earlier releases.

## Sources and audit trail

- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and its model pages: Intelligence Index component scores and the per-task evaluation costs of the basket.
- [AA Coding Agent Index, DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1): DeepSWE pass@1 and the Coding Agent Index cost for each exact configuration.
- [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) official leaderboard rows and [Bug Hunt Bench](https://bughunt.productcompass.pm/) owner-published runs.
- [SemiAnalysis subscription measurements](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (owner-selected 2026-10-07) for the Claude and ChatGPT plan Value Multiples; owner-named transfers are labelled as assumptions.
- The evidence bundle in `data/scores.json` lists every input artifact with its SHA-256; bundle hash `15f19ba84998746ebec56dcf98f74ea25a757867b71c05e9575483982b3aea84`.
- [Methodology co-design record](research/2026-10-19-methodology-codesign/): the reviewed specification, every owner and editor decision, and each reviewer's findings.

## Files

- [methodology.md](methodology.md): how value, cost, quality, the Plan basis and the uncertainty outputs are computed
- [scores.md](scores.md): rankings, leaf scores, basket costs, Plan routes, interval outputs, scenario shares, diagnostics and release gates
- [raw-data.md](raw-data.md): every leaf input with its evidence locator, component costs, benchmark source tables, Plan routes and the evidence bundle
- [https://valuerank.alolabs.dev/](https://valuerank.alolabs.dev/): website, generated by `valuerank.site.build` (source under [valuerank/site/](valuerank/site/))
- [https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/](https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/): current Terminal-Bench 4.0 score-versus-cost page
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
