# ValueRank
**Frontier AI configurations ranked by value for software engineering and DevOps: benchmark quality against what the work costs**

**Version:** v3.0.0
**Updated:** October 19, 2026
**Methodology:** 3.0.0 · SDLC basket v1 · anchor version v3-2026-10-21
**Scope:** 37 cohort configurations (36 with a value score) from a 49-model AA-mapped roster; value is a 25% cost score (nominal weight; 47% of API and 61% of Plan value variance) plus 75% quality over 11 benchmark leaves

## Current result

ValueRank ranks frontier AI model configurations (see Model inclusion) by value for software engineering and DevOps work, separately for API buyers and for subscription (Plan) buyers. Value is a fixed **25%** cost score plus **75%** benchmark quality. That weight is nominal: on the current panel cost accounts for 47% of the variance in API value and 61% in Plan value, because cost scores spread more than quality scores (see [methodology.md](methodology.md)). Cost is the contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost): Artificial Analysis' (AA) published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, scored on a log scale against frozen anchors so cost ratios keep their size. Coding and terminal tasks (Coding Agent Index, Terminal-Bench 4.0 (AA Index run), SciCode) make up 53% of the basket's cost (median over 33 configurations with the full basket; 35% to 85%); AA-Briefcase, GDP.pdf, which have no quality leaf, make up 15%; the Coding Agent Index's SWE-Atlas QnA (124 of its 303 tasks) has no quality leaf either, and its cost share is not separable because AA publishes one pooled cost. Quality is the weighted mean of 11 benchmark leaves on fixed 0–100 anchors, over the leaves observed for the exact configuration; missing evidence is never filled in. The Plan ranking divides the basket's API cost by the selected subscription route's Value Multiple at full utilisation, and uses the API cost, flagged, when no route is admitted. No Value Multiple is yet identified on the basket itself (0 of 37 rows), so the Plan ranking is labelled exploratory.

GPT-6.1 Sol (xhigh) leads the Plan ranking at 60.9 (owner-named transfer); GPT-6.1 Sol (xhigh) leads the API ranking at 60.6; Muse Wonder Full leads on quality.

| Plan rank | API rank | Configuration | Plan value | API value | Quality | Quality coverage | API cost (USD per basket run) | Plan cost (USD per basket run) | Plan route | Flags |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | 1 | [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 60.9 | 60.6 | 64.0 | 80% | $827.23 | $76.79 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 2 | 3 | [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 59.8 | 59.7 | 62.0 | 80% | $700.51 | $65.03 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 3 | 2 | [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 59.7 | 60.0 | 60.9 | 80% | $531.56 | $49.35 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 4 | 19 | [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 59.3 | 51.2 | 64.3 | 100% | $9,373.65 | $159.15 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 5 | 22 | [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 59.1 | 50.9 | 64.2 | 100% | $9,989.15 | $169.60 | Claude Pro $20 · Opus 5.5 (58.9×, measured) | — |
| 6 | 15 | [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 58.8 | 52.5 | 59.7 | 90% | $2,836.05 | $48.15 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 7 | 11 | [Claude Sonnet 5.5 (high)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-high/) | 58.5 | 53.4 | 56.6 | 90% | $1,248.00 | $21.19 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 8 | 6 | [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 57.8 | 56.9 | 61.3 | 100% | $1,267.66 | $117.68 | ChatGPT Pro $500 · common GPT assumption (10.772×, measured) | — |
| 9 | 5 | [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 57.0 | 57.8 | 56.2 | 80% | $375.21 | $34.83 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 10 | 18 | [Claude Sonnet 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-medium/) | 55.8 | 51.4 | 51.2 | 90% | $731.63 | $12.42 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 11 | 33 | [Claude Opus 5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5/) | 54.6 | 46.6 | 57.8 | 80% | $8,733.13 | $148.27 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 12 | 13 | [GPT-6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-sol/) | 54.4 | 52.8 | 58.3 | 90% | $1,999.41 | $185.61 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 13 | 24 | [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 53.8 | 50.7 | 45.4 | 90% | $292.07 | $4.96 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat |
| 14 | 28 | [Claude Sonnet 5.5 (low)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-low/) | 53.6 | 49.6 | 47.5 | 90% | $578.39 | $9.82 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — |
| 15 | 21 | [GPT-5.6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-5-6-sol/) | 53.6 | 50.9 | 59.7 | 90% | $4,238.14 | $393.44 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 16 | 8 | [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 53.3 | 55.6 | 47.7 | 100% | $132.87 | $12.33 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 17 | 23 | [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 53.1 | 50.8 | 42.9 | 90% | $181.35 | $3.08 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat |
| 18 | 25 | [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 52.9 | 50.3 | 60.9 | 100% | $6,107.09 | $753.96 | ChatGPT Plus $20 · common GPT assumption (8.1×, measured) | — |
| 19 | 20 | [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 52.8 | 51.1 | 40.9 | 90% | $114.51 | $1.94 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat |
| 20 | 10 | [GPT-5.6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-5-6-luna/) | 52.8 | 53.9 | 50.0 | 90% | $319.25 | $29.64 | ChatGPT Pro $500 · common GPT assumption (10.772×, assumption) | — |
| 21 | 7 | [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 52.2 | 55.7 | 65.3 | 90% | $3,628.64 | $3,628.64 | — | API-cost fallback |
| 22 | 30 | [Claude Fable 5.1 (max)](https://valuerank.alolabs.dev/models/claude-fable-5-1/) | 51.9 | 47.3 | 60.3 | 100% | $11,580.62 | $909.71 | Claude Max $100 · Fable 5.1 (12.73×, measured) | partial component, valuation basis unverified |
| 23 | 4 | [MiMo-V2.6-Flash](https://valuerank.alolabs.dev/models/mimo-v2-6-flash/) | 51.6 | 58.4 | 51.7 | 50% | $60.37 | $40.25 | MiMo · provisional 1.5x assumption (1.5×, assumption) | subset cost, provisional quality |
| 24 | 27 | [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 50.9 | 49.9 | 36.9 | 90% | $71.52 | $1.21 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat |
| 25 | 35 | [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 50.7 | 45.9 | 45.3 | 90% | $973.34 | $16.53 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat |
| 26 | 14 | [Muse Wonder (max)](https://valuerank.alolabs.dev/models/muse-wonder/) | 50.1 | 52.7 | 64.4 | 80% | $6,534.16 | $6,534.16 | — | API-cost fallback |
| 27 | 9 | [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 48.4 | 54.2 | 50.1 | 60% | $136.13 | $90.75 | MiMo · provisional 1.5x assumption (1.5×, assumption) | subset cost, provisional quality |
| 28 | 16 | [Muse Spark 1.3 (max)](https://valuerank.alolabs.dev/models/muse-spark-1-3/) | 48.1 | 51.9 | 58.8 | 90% | $2,764.98 | $2,764.98 | — | API-cost fallback |
| 29 | 17 | [Grok 4.6 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-6-xhigh/) | 47.9 | 51.7 | 58.9 | 80% | $2,983.67 | $2,983.67 | — | API-cost fallback |
| 30 | 12 | [DeepSeek V4 Flash (max)](https://valuerank.alolabs.dev/models/deepseek-v4-flash/) | 45.7 | 52.9 | 48.1 | 80% | $279.51 | $279.51 | — | API-cost fallback |
| 31 | 29 | [Muse Spark 1.3 (xhigh)](https://valuerank.alolabs.dev/models/muse-spark-1-3-xhigh/) | 45.3 | 49.4 | 54.7 | 90% | $2,366.16 | $2,366.16 | — | API-cost fallback |
| 32 | 26 | [DeepSeek V4 Pro (max)](https://valuerank.alolabs.dev/models/deepseek-v4-pro/) | 44.5 | 50.2 | 50.0 | 80% | $801.50 | $801.50 | — | API-cost fallback |
| 33 | 31 | [Grok 4.7 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-7/) | 44.3 | 46.8 | 56.7 | 100% | $6,700.02 | $6,700.02 | — | API-cost fallback |
| 34 | 34 | [GLM-5.3 (max)](https://valuerank.alolabs.dev/models/glm-5-3/) | 42.7 | 46.3 | 52.1 | 100% | $3,186.29 | $3,186.29 | — | API-cost fallback |
| 35 | 32 | [Gemini 3.8 Flash (high)](https://valuerank.alolabs.dev/models/gemini-3-8-flash/) | 42.4 | 46.7 | 50.3 | 100% | $2,073.44 | $2,073.44 | — | API-cost fallback |
| 36 | 36 | [Qwen3.8 Max](https://valuerank.alolabs.dev/models/qwen3-8-max/) | 38.0 | 40.9 | 47.7 | 100% | $5,417.03 | $5,417.03 | — | API-cost fallback |
| — | — | [Muse Wonder Full (max)](https://valuerank.alolabs.dev/models/muse-wonder-full/) | — | — | 67.7 | 80% | — | — | — | no cost |

Values are rounded for display; ranks are competition ranks (equal values share the better rank).

- **subset cost**: scored on the workload of the components it has, against that workload's own anchors; its ordering against main-workload rows is not identified (O17).
- **provisional quality**: observed leaves cover under 70% of quality weight, fewer than two software-engineering leaves or under 40% software-engineering weight are observed, or DeepSWE is missing; ranked and flagged, never floored (O8).
- **partial component**: AA marks tasks of a basket component missing or declined (E37), or the component's cost cannot be reconciled with AA's prices (E170).
- **valuation basis unverified**: AA's cost reconciles with neither its displayed prices nor a registered price record; ranked, but outside interval outputs and cost anchors (E170 outcome 4).
- **no cost**: AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown.
- **AA cost caveat**: AA states that its published cost omits a pricing term.
- **API-cost fallback**: no admitted Plan route; the Plan ranking uses the API cost (O13).

Not ranked (12 roster models): Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, GLM-5.2, GLM-5.3 Flash, GPT-5.5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Grok 4.6, Kimi K3, Muse Spark 1.2. Reasons are listed in [scores.md](scores.md#not-ranked).

### What the evidence supports

- API basis, main workload: the definite frontier (no configuration can beat it on both cost and quality anywhere inside the published record's precision and missing-evidence bounds) is GPT-6 Luna (max), Claude Haiku 5.5 (low); the possible frontier adds Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), Claude Sonnet 5.5 (max), GPT-6.1 Sol (max), GPT-6.1 Sol (high), Muse Wonder (max), GPT-6.1 Sol (medium), GPT-5.6 Sol (max), Muse Spark 1.3 (max), Claude Sonnet 5.5 (xhigh), GPT-6 Sol (max), Claude Sonnet 5.5 (high), GPT-6.1 Sol (low), GPT-5.6 Luna (max), Grok 4.6 (xhigh), Claude Haiku 5.5 (xhigh), Claude Sonnet 5.5 (medium), Claude Opus 5 (max), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), DeepSeek V4 Flash (max), Claude Sonnet 5.5 (low), DeepSeek V4 Pro (max). Not evaluable on this workload: Claude Fable 5.1 (max), MiMo-V2.6-Flash, MiMo-V2.6-Pro, Muse Wonder Full (max). Cheapest at or above quality 56.7: not unique; possibly GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), Claude Sonnet 5.5 (high), GPT-6.1 Sol (low), DeepSeek V4 Flash (max), DeepSeek V4 Pro (max). (Bar comparison: compares 21 configurations that can qualify.) Cheapest at or above quality 48.1: not unique; possibly GPT-6.1 Sol (medium), GPT-6.1 Sol (low), GPT-5.6 Luna (max), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), DeepSeek V4 Flash (max). (Bar comparison: compares 29 configurations that can qualify.) Cheapest at or above quality 60.9: not unique; possibly GPT-6.1 Sol (xhigh), GPT-6.1 Sol (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), Claude Sonnet 5.5 (high), GPT-6.1 Sol (low). (Bar comparison: compares 17 configurations that can qualify.)
- Plan basis: interval outputs not evaluated (no row has FullCost and an identified M_W (E61/E67)).
- API basis, displayed record (not a claim; E203): cheapest at or above quality 56.7: GPT-6.1 Sol (medium) ($531.56 per basket run; 17 reach it); at or above quality 48.1: DeepSeek V4 Flash (max) ($279.51 per basket run; 26 reach it); at or above quality 60.9: GPT-6.1 Sol (medium) ($531.56 per basket run; 9 reach it).
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 56.7: Claude Sonnet 5.5 (xhigh) ($48.15 per basket run; 17 reach it); at or above quality 48.1: Claude Sonnet 5.5 (medium) ($12.42 per basket run; 26 reach it); at or above quality 60.9: GPT-6.1 Sol (medium) ($49.35 per basket run; 9 reach it).

Scenario shares by stream, diagnostics and the release gates are in [scores.md](scores.md); the inputs behind every number are in [raw-data.md](raw-data.md).

## Model inclusion

**Frontier rule.** Every model family on the Pareto frontier that Artificial Analysis (AA) renders on its Intelligence Index versus total cost to run chart is ranked at its highest point on that line (along the strictly rising line also its dearest). Frontier membership is AA's rendered line as observed; ValueRank never recomputes it from rounded values.

**Near-frontier rule.** A plotted configuration is near-frontier when its public (rounded integer) Intelligence Index is within 3 points of the rendered frontier's Index at its cost, meaning the highest Index among rendered-frontier points that cost no more. Every near-frontier family is ranked or is explicitly deferred by a dated, reasoned roster decision. Its selected configuration may differ from the near configuration: it is the configuration already ranked for exact DeepSWE and Bug Hunt evidence when there is one, else the near point with the smallest Index gap. The cost ratio to the frontier is reported for information only.

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

Near-frontier families and each family's near point closest to the frontier (a family's primary configuration is its configuration with exact DeepSWE and Bug Hunt results when it has one, O30, and every other effort with both results is ranked as its own row, O33, so the ranked configurations can differ):

- Claude Haiku 5.5: Claude Haiku 5.5 (low), 1 Index point below the frontier
- Claude Opus 5.5: Claude Opus 5.5 (medium with fallback), 1 Index point below the frontier
- Claude Sonnet 5.5: Claude Sonnet 5.5 (xhigh with fallback), 2 Index points below the frontier
- GPT-5.6 Luna: GPT-5.6 Luna (low), 1 Index point below the frontier
- GPT-6 Astra: GPT-6 Astra (xhigh), 2 Index points below the frontier
- Gemini 4 Argon: Gemini 4 Argon (high), 1 Index point below the frontier

AA footnote (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (low)): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## How v3 scores value

- **Cost is the SDLC basket.** SDLC basket v1: AA's published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, in USD per basket run. Pending capture: FrontierCode, ITBench-AA. v2 used AA's cost to run the whole Intelligence Index per Index point.
- **Cost keeps its magnitude.** The cost score is 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100, against anchors frozen with anchor version `v3-2026-10-21`. A model entering or leaving the cohort does not move another model's score. At the API anchors, doubling cost costs 2.74 value points, which 3.65 quality points offset.
- **Quality is measured, not ranked.** Each of the 11 leaves is placed on fixed 0–100 anchors from its raw value, so quality no longer depends on which other models are ranked. A missing leaf is left out of that configuration's mean, its coverage is shown, and low coverage marks the row provisional.
- **Plan value is route evidence.** Each subscription route carries its Value Multiple, evidence grade (controlled measurement, concordant reports, owner-named assumption) and identification status; the Plan ranking is labelled exploratory until multiples are identified on the basket.
- **Uncertainty is shown, not hidden.** Interval outputs certify which frontier and cheapest-above-a-bar claims the published record supports; scenario shares report frequencies over declared streams.
- v3 values are not numerically comparable with v2 or earlier releases.

## Sources and audit trail

- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and its model pages: Intelligence Index component scores and the per-task evaluation costs of the basket.
- [AA Coding Agent Index, DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1): DeepSWE pass@1 and the Coding Agent Index cost for each exact configuration.
- [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) official leaderboard rows and [Bug Hunt Bench](https://bughunt.productcompass.pm/) owner-published runs.
- [SemiAnalysis subscription measurements](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (owner-selected 2026-10-07) for the Claude and ChatGPT plan Value Multiples; owner-named transfers are labelled as assumptions.
- The evidence bundle in `data/scores.json` lists every input artifact with its SHA-256; bundle hash `15dd4ea9c6287ccd873a7d565f8fb13edb281b4bca574e90445a9a2b7557b750`.
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
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 34 (rounded) | $56.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 38 (rounded) | $94.07 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.55 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 41 (rounded) | $157.58 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 56 (rounded) | $7,259.50 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |
| [GPT-5.6 Luna (low)](https://artificialanalysis.ai/models/gpt-5-6-luna-low) | gpt-5-6-luna-low | 21 (rounded) | $27.02 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-5.6 Luna family is represented in the primary ranking by its selected configuration (gpt-5-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 29 (rounded) | $34.31 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Haiku 5.5 (max)](https://artificialanalysis.ai/models/claude-haiku-5-5) | claude-haiku-5-5 | 43 (rounded) | $330.25 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (medium with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-medium) | claude-opus-5-5-medium | 51 (rounded) | $1,626.81 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh) | claude-sonnet-5-5-xhigh | 52 (rounded) | $2,176.82 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Gemini 4 Argon (high)](https://artificialanalysis.ai/models/gemini-4-argon) | gemini-4-argon | 53 (rounded) | $2,407.24 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 51 (rounded) | $2,925.01 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-6 Astra family is represented in the primary ranking by its selected configuration (gpt-6-astra-xhigh). No result is transferred between efforts. |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 52 (rounded) | $3,802.98 | Near AA frontier (within 3 Index points) | Missing from source roster | Exact evaluated variant absent from source roster |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 53 (rounded) | $5,324.10 | Near AA frontier (within 3 Index points) | Primary ranked | None |
