# ValueRank Methodology

**Version:** v3.0.0 (methodology 3.0.0)
**Updated:** October 19, 2026

This page summarises how ValueRank scores value. The normative specification, its review record and every owner and editor decision are in [research/2026-10-19-methodology-codesign/](research/2026-10-19-methodology-codesign/); where this summary is less precise, the specification governs.

## Objective and claim scope

ValueRank asks which frontier AI model configuration is lowest cost for the value it delivers on software-development work, once subscription economics and software-engineering benchmarks are weighed alongside general capability. It serves two buyers, ranked separately: **API buyers**, who pay per token (including through third-party agents), and **Plan buyers**, who use a provider subscription such as Claude Code, Codex or ChatGPT. The claim is scoped to value among the ranked configurations, under the published benchmark mix and evidence; it is not a market-wide optimum. Every ranked row is a **configuration**: a model version at one reasoning effort. Results are never transferred between versions or efforts.

## Cohort

19 configurations are ranked:

- On AA's rendered frontier (7): GPT-6.1 Sol (max), Claude Sonnet 5.5 (max), Claude Opus 5.5 (max), MiMo-V2.6-Pro, GPT-6 Luna (max), MiMo-V2.6-Flash, Claude Haiku 5.5 (xhigh)
- Near-frontier family (3): Gemini 4 Argon (high), GPT-6 Astra (max), GPT-5.6 Luna (max)
- Retained from earlier releases for exact DeepSWE and Bug Hunt evidence (9): GPT-5.6 Sol (max), GPT-6 Sol (max), Grok 4.7 (xhigh), Gemini 3.8 Flash (high), GLM-5.3 (max), Claude Opus 5 (max), DeepSeek V4 Flash (max), Qwen3.8 Max, DeepSeek V4 Pro (max)

The remaining 12 roster models are not ranked; each keeps a page with the evidence held for it.

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

Near-frontier families and each family's near point closest to the frontier (a family is ranked at its configuration with exact DeepSWE and Bug Hunt results when it has one, O30, so the ranked configuration can differ):

- Claude Haiku 5.5: Claude Haiku 5.5 (low), 1 Index point below the frontier
- Claude Opus 5.5: Claude Opus 5.5 (medium with fallback), 1 Index point below the frontier
- Claude Sonnet 5.5: Claude Sonnet 5.5 (xhigh with fallback), 2 Index points below the frontier
- GPT-5.6 Luna: GPT-5.6 Luna (low), 1 Index point below the frontier
- GPT-6 Astra: GPT-6 Astra (xhigh), 2 Index points below the frontier
- Gemini 4 Argon: Gemini 4 Argon (high), 1 Index point below the frontier

AA footnote (Claude Haiku 5.5): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## Value

Value on a basis = **25%** × cost score + **75%** × quality score (owner decision, 2026-10-19). Both scores run from 0 to 100, higher is better. Cost's share is fixed: a configuration missing quality evidence keeps cost at 25%, and a configuration without a cost score has no value score. Ranks are competition ranks; equal values share the better rank.

## Cost: the SDLC basket

The cost figure is the **contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost)**. SDLC basket v1 holds the components the admission rule admits (maximise components, then panel size, then target order, over subsets with a complete-evidence panel of at least two-thirds); its reference panel is 17 of the 19 ranked configurations (at least 13 required):

| Component | Status | Exact cost available | Complete | Ranked |
|---|---|---:|---:|---:|
| Coding Agent Index | admitted | 17 | 17 | 19 |
| FrontierCode | pending capture | 12 | 11 | 19 |
| ITBench-AA | pending capture | 8 | 8 | 19 |
| AA-Briefcase | admitted | 19 | 19 | 19 |
| GDPval-AA | admitted | 19 | 19 | 19 |
| GDP.pdf | admitted | 19 | 19 | 19 |
| AutomationBench-AA | admitted | 19 | 19 | 19 |
| Terminal-Bench 4.0 (AA Index run) | admitted | 19 | 19 | 19 |
| SciCode | admitted | 19 | 19 | 19 |
| AA-LCR | admitted | 19 | 19 | 19 |

A configuration's basket cost is the sum of AA's published costs for the admitted components at that exact model and effort: each Intelligence Index component is AA's cost per task times its task count, and the Coding Agent Index cost is read from AA's chart (rounded to USD 1). The Index components plus AA's residual reproduce AA's published Index total for every configuration (see raw-data.md).

**Cost boundary.** Source: https://artificialanalysis.ai/methodology/intelligence-benchmarking (fetched 2026-10-19). AA's cost covers the contestant model's API tokens; other charges are included, excluded or unknown per component:

| Component | Contestant tokens | Other model calls | External tools | Execution environment | Preparation | Grading |
|---|---|---|---|---|---|---|
| Coding Agent Index | included | unknown | unknown | unknown | unknown | unknown |
| AA-Briefcase | included | unknown | unknown | unknown | unknown | unknown |
| GDPval-AA | included | unknown | unknown | unknown | unknown | unknown |
| GDP.pdf | included | excluded | unknown | unknown | excluded | excluded |
| AutomationBench-AA | included | unknown | unknown | unknown | unknown | unknown |
| Terminal-Bench 4.0 (AA Index run) | included | unknown | unknown | unknown | unknown | unknown |
| SciCode | included | unknown | unknown | unknown | unknown | unknown |
| AA-LCR | included | unknown | unknown | unknown | unknown | unknown |

**Subset workloads (O17).** A configuration without exact cost for an admitted component is scored on the workload made of the components it has, against that workload's own frozen anchors, and flagged "subset cost"; its ordering against main-workload configurations is not identified. A component AA marks with missing or declined tasks is flagged "partial component" (E37).

## Cost score and anchors

Cost score S_C = 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100. The anchors are frozen per workload and basis: c_L is half the cheapest reference cost and c_H twice the dearest, so no reference configuration clips. A release is held when more than max(1, 10% of ranked rows) clip on a basis or any row lies beyond an anchor by more than a factor of 2 (owner decision O12).

| Workload | Basis | Low anchor c_L (USD) | High anchor c_H (USD) | References | Status |
|---|---|---:|---:|---:|---|
| `9a0d376cc6080f3c` (main) | api | $66.43 | $19,978.30 | 17 | frozen |
| `9a0d376cc6080f3c` (main) | plan | $2.48 | $13,400.04 | 17 | frozen |
| `1453a9a0576b02ea` (subset) | api | $30.18 | $12,078.25 | 19 | frozen |
| `1453a9a0576b02ea` (subset) | plan | $0.91 | $8,725.81 | 19 | frozen |

**Anchor policy** (`complete-evidence-panel` v1). Population: ranked configurations with complete cost evidence (exact cost, no AA missing- or declined-task marker) on every component of the workload at the freeze cutoff; on the main workload this is the admission reference panel. Plan anchors: the same configurations at their displayed Plan cost: measured routes, owner-named transfers and API-cost fallbacks alike, since each is scored in the Plan table (O13, O16) and a narrower panel would clip them. At least 2 references; below that, anchors unavailable: configurations on that workload get no cost score (the main workload must meet the minimum). Lifetime: reference IDs and costs are frozen; a population or rule change is a new anchor version with an old/new bridge, and evidence lost after freezing never rebuilds an anchor.

**Exchange rate.** In the unclipped region a cost doubling changes value by −100 × 0.25 × ln 2 / ln(c_H / c_L) points, offset by +100 × 0.25 × ln 2 / ((1 − 0.25) × ln(c_H / c_L)) quality points. At the main-workload anchors:

| Basis | Anchor ratio c_H / c_L | Value points per cost doubling | Quality points that offset it |
|---|---:|---:|---:|
| api | 300.7 | 3.04 | 4.05 |
| plan | 5404.5 | 2.02 | 2.69 |

**Within-cohort influence (E91, E126).** Cost's share of the value dispersion on the common-workload panel, 0.25 × SD(S_C) / (0.25 × SD(S_C) + 0.75 × SD(S_Q)), is published and flagged below 10% or above 90%; the flag is informational and the cost weight never changes (O2). Because cost and quality covary, that ratio describes dispersion; the value-variance allocation Cov(0.25 S_C, V) / Var(V) and the Kendall tau of the cost-only and quality-only orderings against the value ordering show contribution (E189).

| Basis | Panel | Cost's share | Status | Cost's variance allocation | Tau, cost vs value | Tau, quality vs value |
|---|---:|---:|---|---:|---:|---:|
| api | 17 | 54.9% | defined | 81.1% | 0.47 | 0.04 |
| plan | 17 | 54.7% | defined | 61.8% | 0.60 | 0.29 |

## Quality

Quality is the weighted mean of the leaves observed for the exact configuration, each placed on fixed 0–100 anchors from its raw value (clipped, with saturation disclosed). Group shares of quality: Software engineering 60%, General professional work 20%, Reliability 10%, Long context, science & knowledge 10%.

| Leaf | Group | Weight in quality | Weight in value | Raw unit | Score | Run by |
|---|---|---:|---:|---|---|---|
| [DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1) | Software engineering | 30.00% | 22.50% | % pass@1 | z = pass@1 % | AA-run |
| [Bug Hunt Bench](https://bughunt.productcompass.pm/) | Software engineering | 10.00% | 7.50% | bugs fixed of 105 | z = 100 × bugs fixed / 105 | independent |
| [AA FrontierCode 1.1](https://artificialanalysis.ai/evaluations/frontiercode) | Software engineering | 10.00% | 7.50% | AA score (0-1) | z = 100 × score | AA-run |
| [Terminal-Bench 4.0 (tbench.ai)](https://www.tbench.ai/leaderboard/terminal-bench/4.0) | Software engineering | 10.00% | 7.50% | % resolved | z = resolution % | independent |
| [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | General professional work | 10.00% | 7.50% | Elo | z = 100 × (Elo − 500) / 2000 (AA's integration transform) | AA-run |
| [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | General professional work | 10.00% | 7.50% | AA score (0-1) | z = 100 × score | AA-run |
| [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience) | Reliability | 10.00% | 7.50% | AA Omniscience Index (-100 to 100) | z = (I + 100) / 2 on AA's Omniscience Index I (O28) | AA-run |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | Long context, science & knowledge | 5.00% | 3.75% | accuracy (0-1) | z = 100 × accuracy | AA-run |
| [Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | Long context, science & knowledge | 1.67% | 1.25% | accuracy (0-1) | z = 100 × accuracy | AA-run |
| [SciCode](https://artificialanalysis.ai/evaluations/scicode) | Long context, science & knowledge | 1.67% | 1.25% | score (0-1) | z = 100 × score | AA-run |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | Long context, science & knowledge | 1.67% | 1.25% | score (0-1) | z = 100 × score | AA-run |

Coverage is the observed share of quality weight. A row is **provisional** when coverage is below 70%, fewer than 2 software-engineering leaves are observed, observed software-engineering weight is below 40%, or a leaf weighing 20% or more of quality (DeepSWE) is missing. Provisional rows are ranked and flagged; there is no quality floor (O8). Missing leaves are never filled; the interval outputs treat each one as anywhere in 0–100.

## Plan basis

Plan cost = basket API cost ÷ the Value Multiple of the selected subscription route, at full utilisation. A Value Multiple is the API-priced usage a subscription delivers per dollar of fee. Route evidence is graded: **controlled** measurements of the exact model, **reports** (at least two independent, comparable end-user reports concordant within 20%), owner-named **assumptions** (a measured multiple transferred to another model, labelled), and **diagnostic** evidence, which is shown but never ranked. Routes certifiably dearer than another identified route of at least equal grade are set aside (E88); the official route is then chosen by identification class, evidence grade, the comparison multiple, lower gross cash and route ID (E85). Evidence past its 90-day expiry and 30-day grace is demoted to diagnostic. A configuration without an admitted route uses its API cost, flagged. Each Plan row publishes its fee period, the cash paid and the selected multiple's amount (multiple × gross cash), typed by what the measurement establishes (E166): measured-workload capacity, observed eligible consumption with capacity not established, assumed API-equivalent consumption for an owner-named transfer (with its donor), or identified target-workload capacity; API-fallback rows publish none.

**Identification (E61).** A multiple is measured on its own workload; it identifies the basket's multiple only when the workloads match. Today 0 of 19 Plan rows are point-identified and 0 set-identified, so the Plan ranking is labelled exploratory. A measured-only Plan view (`3d83f7643d4a85b7`) re-runs the selection over exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics), without transfers or fallbacks. Because the official Plan anchors include transfers and fallbacks, a calibration diagnostic rescores the measured-only rows on anchors built from measured evidence alone (E164), so an assumption's effect through the exchange rate is visible.

**Subscription evidence policy** (as of 2026-10-08; reporting window 2026-09-08 to 2026-10-08):

- Default numerator: Actual API-priced end-user-reported use or reported estimate anchored to measured use; exact model, tier and dates required.
- Selected source for Anthropic, OpenAI: [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (2026-10-06, owner-selected 2026-10-07): Controlled subscription-account measurements with agentic workload projections.
- GPT: User authorizes the same ChatGPT plan multiples for every GPT model. Use the lower reported model-conditional figure per plan, preserve its original evaluated variant, and label cross-model application as an assumption.
- Claude: User authorizes (2026-10-18, Option 2) applying Opus 5.5's measured SemiAnalysis Claude plan multiples to every other Claude model. Opus 5.5 keeps its exact measured routes; the shared routes are labelled user assumptions, carry the recorded caution that allowances are model-specific (Fable 5.1 measured 12.4-12.7x on the same plans), and are superseded by any exact measurement for the listed model.
- MiMo: User authorizes provisional 1.5x for both MiMo candidate variants. Plan fee and measured API-equivalent numerator remain unavailable.
- Other models: Use API fallback; do not transfer evidence across model versions, variants or thinking effort except for the explicit common GPT, Claude and MiMo assumptions.
- Provider allowance, quota and marketing figures never supply the measured numerator; a provider's published price can be the fee denominator only when the tier mapping is supported.

## Uncertainty outputs

**Interval outputs (O25).** Each observed leaf is placed anywhere inside its published reporting precision, each missing leaf anywhere in 0–100 and each cost inside its rounding. A configuration is on the **definite frontier** when no other configuration can beat it on both cost and quality for any values in those boxes, and on the **possible frontier** when some values put it there. The **cheapest above a quality bar** is confirmed only when its worst cost is below the best cost of every other configuration that could qualify. The bar is pinned by policy `median-quality-level` v2: the lower median of non-provisional ranked configurations with a displayed quality, ordered by displayed quality ascending, then configuration ID, selected deterministic at anchor freeze, before any bar outcome is computed; the displayed quality of the population's lower-median configuration, frozen as a level; the configuration itself is recorded for audit and competes like any other; with at least two population configurations, at least two are at or above the level at freeze, so the output always compares alternatives; fixed for the anchor version; replaced only by a versioned re-freeze that publishes old- and new-bar results on the common evaluable panel. Current bar: quality 56.7 (the displayed quality of Grok 4.7 at freeze).

**Scenario shares** are frequencies over declared streams, never probabilities (10,000 scenarios per run, seed 20261021, input hash `551abe507e20a0d4`):

- **S0**: published-record reporting precision.
- **S1**: published-record reporting precision + conventional identification of missing leaves.
- **S2**: published-record reporting precision + conventional identification of missing leaves + weight-specification stress.
- **S1M**: published-record reporting precision + conventional identification of missing leaves + conventional range sensitivity inside published 95% confidence intervals (no tail model).

S1 also runs with the endpoint-heavy kernel. On the Plan basis the core streams (S1, S2 and S1M) run with owner-named transfers off (E167): a row whose selected route is a transfer is unevaluable there, never reselected or replaced by API cost, while S0 keeps the displayed record. S1M draws Terminal-Bench 4.0 (tbench.ai) inside its source's published 95% confidence interval, labelled conventional CI-range sensitivity (endpoint-conditioned; no tail model) under its interpretation contract (E165; estimand: not established from the captured documentation; method: not established from the captured documentation; sampling unit: not established from the captured documentation); values outside the interval are not explored; no tail mass is invented. A cheapest-above-the-bar label is published only when the share clears a sequential threshold with its per-look error controlled. Not quantified in these shares:

- benchmark repeatability beyond the conventional Terminal-Bench interval-range sensitivity in S1M (other published intervals, run-to-run ranges): not quantified in v1 scenario shares.
- fitted-parameter uncertainty (e.g. Elo rating intervals): not quantified in v1 scenario shares.

## Diagnostics

Diagnostics are published beside the ranking and never change a score: Terminal-Bench same-harness agreement, anchor stability (exchange-rate series and trimmed-anchor rank shifts), Omniscience abstention sensitivity, quality source shares, matched-panel quality agreement, non-discriminating leaves, group drift, quality dispersion, deletion sensitivity (leave-one-benchmark-out and source deletions) and the standing removal of the Terminal-Bench cost component. Current results are in [scores.md](scores.md#diagnostics).

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | fired | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a pinned identity |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |

## Limitations

- Cost is the contestant-model API token cost of AA's runs, not total agent or workflow operating cost.
- Cost scores use frozen anchors; a new anchor version is a published migration, never a silent change.
- The basket is AA's SDLC-relevant evaluations at AA's token mix, not your own workload.
- Results are never transferred between model versions or reasoning efforts; missing evidence stays missing.
- Published values are rounded; interval outputs and scenario shares show which differences the evidence supports, and benchmark run-to-run noise is not yet quantified.
- Subscription Value Multiples are measured on their own workloads; none is yet identified on the basket, so the Plan ranking is exploratory.

## Machine-readable files

- [data/scores.json](data/scores.json): the `v3` section holds every row, workload, anchor, interval output, scenario result, diagnostic and the evidence bundle
- [data/plan_cost_routes.json](data/plan_cost_routes.json): subscription routes, their evidence, sources and policy
- [data/v3_frozen.json](data/v3_frozen.json): frozen anchors, bar policy and anchor policy for anchor version `v3-2026-10-21`
- [data/v3_scenarios.json](data/v3_scenarios.json): scenario-share runs for every stream
- [data/aa_deepswe.json](data/aa_deepswe.json), [data/tb4.json](data/tb4.json), [data/bug_hunt.json](data/bug_hunt.json): independent benchmark snapshots
