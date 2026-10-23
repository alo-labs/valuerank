# ValueRank Methodology

**Version:** v3.0.0 (methodology 3.0.0)
**Updated:** October 19, 2026

This page summarises how ValueRank scores value. The normative specification, its review record and every owner and editor decision are in [research/2026-10-19-methodology-codesign/](research/2026-10-19-methodology-codesign/); where this summary is less precise, the specification governs.

## Objective and claim scope

ValueRank asks which frontier AI model configuration is lowest cost for the value it delivers on software-development work, once subscription economics and software-engineering benchmarks are weighed alongside general capability. It serves two buyers, ranked separately: **API buyers**, who pay per token (including through third-party agents), and **Plan buyers**, who use a provider subscription such as Claude Code, Codex or ChatGPT. The claim is scoped to value among the ranked configurations, under the published benchmark mix and evidence; it is not a market-wide optimum. Every ranked row is a **configuration**: a model version at one reasoning effort. Results are never transferred between versions or efforts.

## Cohort

9 configurations are ranked:

- On AA's rendered frontier (5): Claude Sonnet 5.5 (max), Claude Opus 5.5 (max), GPT-6.1 Sol (max), MiMo-V2.6-Pro, GPT-6 Luna (max)
- Near-frontier family (2): DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high)
- Plotted on or near AA's rendered frontier, another effort of a frontier or near family (O51) (2): GPT-6 Astra (max), Claude Haiku 5.5 (max)

20 more cohort configurations are listed, not ranked, because a quality benchmark is still missing after an exhaustive search logged within 7 days of the cutoff (O36; a required frontier family is listed the same way, O38): GPT-6.1 Sol (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Opus 5.5 (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Opus 5.5 (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6.1 Sol (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Astra (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-5.6 Luna (low) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (low) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Opus 5.5 (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Sonnet 5.5 (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Astra (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (low) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6.1 Sol (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); MiMo-V2.6-Flash (no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); MiniMax-M3.1-Flash (no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall). Of these, 11 are ranked in the AI Coding Daily ranking (O53): GPT-6.1 Sol (high), Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Sol (medium), GPT-6 Astra (high), Claude Haiku 5.5 (high), GPT-6 Luna (xhigh), Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-5.6 Luna (low). AA plots Claude Opus 5.5 and Claude Sonnet 5.5 only "with fallback", and every other cohort family (Claude Haiku 5.5, DeepSeek V4.1 Flash 1017, GPT-5.6 Luna, GPT-6 Astra, GPT-6 Luna, GPT-6.1 Sol, Gemini 4 Argon, MiMo-V2.6-Flash, MiMo-V2.6-Pro and MiniMax-M3.1-Flash) without it; a third-party record matches by model and effort, and the build stops if AA plots one model and effort both ways (E214). AA plots MiMo-V2.6-Flash, MiMo-V2.6-Pro and MiniMax-M3.1-Flash with no effort (O54). A listed frontier or near-frontier family also shows, apart from the ranking, an indicative value on the leaves it has, labelled not ranked and not comparable (O41).

The remaining 32 roster models are not ranked; each keeps a page with the evidence held for it.

## Model inclusion

**Frontier rule.** Every model family on the Pareto frontier that Artificial Analysis (AA) renders on its Intelligence Index versus total cost to run chart is ranked at its highest point on that line (along the strictly rising line also its dearest). Frontier membership is AA's rendered line as observed; ValueRank never recomputes it from rounded values.

**Near-frontier rule.** A plotted configuration is near-frontier when its public (rounded integer) Intelligence Index is within 3 points of the rendered frontier's Index at its cost, meaning the highest Index among rendered-frontier points that cost no more. Every near-frontier family is ranked or is explicitly deferred by a dated, reasoned roster decision. Every configuration AA plots on the frontier or within the gap is a cohort row (O51); a near family's primary configuration is its near point with the smallest Index gap. The cost ratio to the frontier is reported for information only.

Policy as recorded: A plotted configuration is near-frontier when it lies within 3 Intelligence Index points of the rendered frontier at its cost. Every near-frontier model family must be in the primary ranking, with its own selected configuration, or be explicitly deferred with a dated, reasoned roster decision. The cost ratio to the cheapest frontier point of equal or higher intelligence is reported for information only.

Chart observed 2026-10-23T05:27:39Z (Intelligence Index v4.3.2): 697 catalog models selected, 189 plotted points and 18 rendered Pareto vertices across 7 families. 11 plotted points across 8 families are near-frontier.

Near-frontier models: 8 required, 0 deferred by roster decision.

Frontier families and the configuration selected for each:

- Claude Haiku 5.5: Claude Haiku 5.5 (xhigh)
- Claude Opus 5.5: Claude Opus 5.5 (max with fallback)
- Claude Sonnet 5.5: Claude Sonnet 5.5 (max with fallback)
- GPT-6 Luna: GPT-6 Luna (max)
- GPT-6.1 Sol: GPT-6.1 Sol (max)
- MiMo-V2.6-Flash: MiMo-V2.6-Flash
- MiMo-V2.6-Pro: MiMo-V2.6-Pro

Near-frontier families and each family's near point closest to the frontier (every configuration AA plots on or near the frontier is a cohort row, each effort its own row, O51; a family's primary configuration is its near point closest to the frontier, E193):

- Claude Haiku 5.5: Claude Haiku 5.5 (low), 1 Index point below the frontier
- Claude Opus 5.5: Claude Opus 5.5 (medium with fallback), 1 Index point below the frontier
- Claude Sonnet 5.5: Claude Sonnet 5.5 (xhigh with fallback), 2 Index points below the frontier
- DeepSeek V4.1 Flash 1017: DeepSeek V4.1 Flash 1017 (max), 3 Index points below the frontier
- GPT-5.6 Luna: GPT-5.6 Luna (low), 1 Index point below the frontier
- GPT-6 Astra: GPT-6 Astra (xhigh), 2 Index points below the frontier
- Gemini 4 Argon: Gemini 4 Argon (high), 1 Index point below the frontier
- MiniMax-M3.1-Flash: MiniMax-M3.1-Flash, 3 Index points below the frontier

AA footnote (Claude Haiku 5.5 (max), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (low)): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## Value

Value on a basis = **25%** × cost score + **75%** × quality score (owner decision, 2026-10-19). Both scores run from 0 to 100, higher is better. Cost's share is fixed: a configuration missing quality evidence keeps cost at 25%, and a configuration without a cost score has no value score. Ranks are competition ranks; equal values share the better rank.

## Cost: the SDLC basket

The cost figure is the **contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost)**. SDLC basket v1 holds the components the admission rule admits (maximise components, then panel size, then target order, over subsets with a complete-evidence panel of at least two-thirds); its reference panel is 8 of the 9 ranked configurations (at least 6 required):

| Component | Status | Exact cost available | Complete | Ranked |
|---|---|---:|---:|---:|
| Coding Agent Index | admitted | 8 | 8 | 9 |
| ITBench-AA | pending capture | 2 | 2 | 9 |
| AA-Briefcase | admitted | 9 | 9 | 9 |
| GDPval-AA | admitted | 9 | 9 | 9 |
| GDP.pdf | admitted | 9 | 9 | 9 |
| AutomationBench-AA | admitted | 9 | 9 | 9 |
| Terminal-Bench 4.0 (AA Index run) | admitted | 9 | 9 | 9 |
| SciCode | admitted | 9 | 9 | 9 |
| AA-LCR | admitted | 9 | 9 | 9 |

A configuration's basket cost is the sum of AA's published costs for the admitted components at that exact model and effort: each Intelligence Index component is AA's cost per task times its task count, and the Coding Agent Index cost is AA's unrounded mean cost per task times its 290 required tasks (O27, O50). The Index components plus AA's residual reproduce AA's published Index total for every configuration (see raw-data.md).

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

Cost score S_C = 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100. The anchors are frozen per workload and basis: c_L is half the cheapest reference cost and c_H twice the dearest, so no reference configuration clips. A release is held when more than max(1, 10% of ranked rows) clip on a basis or any ranked row lies beyond an anchor by more than a factor of 2 (owner decision O12). The gate counts ranked rows only; a listed configuration beyond the anchors never holds a release and is disclosed (owner decision O58). Max-effort ranking, listed beyond the API anchors: GPT-6 Luna (high) (below the low anchor, by a factor of 1.1, a point on AA's rendered frontier); GPT-6 Luna (medium) (below the low anchor, by a factor of 1.6, a point on AA's rendered frontier); GPT-5.6 Luna (low) (below the low anchor, by a factor of 1.9); Claude Haiku 5.5 (low) (below the low anchor, by a factor of 1.4); GPT-6 Luna (low) (below the low anchor, by a factor of 4.8, a point on AA's rendered frontier). AI Coding Daily ranking, listed beyond the API anchors: Claude Sonnet 5.5 (above the high anchor, by a factor of 1.1, a point on AA's rendered frontier); Claude Opus 5.5 (above the high anchor, by a factor of 1.3, a point on AA's rendered frontier); GPT-6 Luna (low) (below the low anchor, by a factor of 1.2, a point on AA's rendered frontier).

| Workload | Basis | Low anchor c_L (USD) | High anchor c_H (USD) | References | Status |
|---|---|---:|---:|---:|---|
| `9a0d376cc6080f3c` (main) | api | $62.86 | $18,703.43 | 8 | frozen |
| `9a0d376cc6080f3c` (main) | plan | $5.84 | $7,115.53 | 23 | frozen |
| `1453a9a0576b02ea` (subset) | api | $39.78 | $12,078.25 | 9 | frozen |
| `1453a9a0576b02ea` (subset) | plan | $1.63 | $3,715.87 | 27 | frozen |

**Anchor policy** (`complete-evidence-panel` v1). Population: ranked configurations with complete cost evidence (exact cost, no AA missing- or declined-task marker) on every component of the workload at the freeze cutoff; on the main workload this is the admission reference panel. Plan anchors: the same configurations at their displayed Plan cost: measured routes, owner-named transfers and API-cost fallbacks alike, since each is scored in the Plan table (O13, O16) and a narrower panel would clip them. At least 2 references; below that, anchors unavailable: configurations on that workload get no cost score (the main workload must meet the minimum). Lifetime: reference IDs and costs are frozen; a population or rule change is a new anchor version with an old/new bridge, and evidence lost after freezing never rebuilds an anchor.

**Exchange rate.** In the unclipped region a cost doubling changes value by −100 × 0.25 × ln 2 / ln(c_H / c_L) points, offset by +100 × 0.25 × ln 2 / ((1 − 0.25) × ln(c_H / c_L)) quality points. At the main-workload anchors:

| Basis | Anchor ratio c_H / c_L | Value points per cost doubling | Quality points that offset it |
|---|---:|---:|---:|
| api | 297.5 | 3.04 | 4.06 |
| plan | 1219.4 | 2.44 | 3.25 |

**Within-cohort influence (E91, E126).** Cost's share of the value dispersion on the common-workload panel, 0.25 × SD(S_C) / (0.25 × SD(S_C) + 0.75 × SD(S_Q)), is published and flagged below 10% or above 90%; the flag is informational and the cost weight never changes (O2). Because cost and quality covary, that ratio describes dispersion; the value-variance allocation Cov(0.25 S_C, V) / Var(V) and the Kendall tau of the cost-only and quality-only orderings against the value ordering show contribution (E189).

| Basis | Panel | Cost's share | Status | Cost's variance allocation | Tau, cost vs value | Tau, quality vs value |
|---|---:|---:|---|---:|---:|---:|
| api | 8 | 54.4% | defined | 115.4% | 0.36 | -0.21 |
| plan | 23 | 47.8% | defined | 28.2% | -0.03 | 0.55 |

## Quality

Quality is the weighted mean of the leaves observed for the exact configuration, each placed on fixed 0–100 anchors from its raw value (clipped, with saturation disclosed). Group shares of quality: Software engineering 60%, General professional work 20%, Reliability 10%, Long context, science & knowledge 10%.

**Two rankings (owner decisions O52–O55, O61).** ValueRank picks each ranking's benchmark set and ranks the configurations that have all of it, balancing the number of benchmarks against the number of configurations ranked. Outside AA, independent software-engineering benchmarks run few efforts per model, so no single set covers the cohort: LiveBench 2.0 and Vals AI run each model once at its top effort, and AI Coding Daily mostly at high and medium effort. The **max-effort ranking** (leading, O54) adds LiveBench 2.0 Overall, the mean of its seven categories (Long Agentic, Reasoning, Coding, Browser, Data Analysis, Research, Design; O61: all are needed in the SDLC, and as an uncontaminated benchmark it carries no less weight than any single AA leaf), Vals Vibe Code Bench v1.1 and Vals Code Migration v1.1; the **AI Coding Daily ranking** adds AI Coding Daily (its bug-finding column excluded because it overlaps Bug Hunt). Each ranking has its own frozen anchors, quality bars, scenario run and diagnostics, so values are comparable within a ranking, not across. Surge's Complex Constraints (instruction following, IFBench's successor) is dropped for now and CursorBench 4.0 and Surge sudo L7 are excluded by the owner; Epoch MirrorCode, SWE-bench-Live and SWE-PolyBench each cover too few cohort configurations at their exact effort (O53, O54; [research record](research/2026-10-23-swe-benchmarks/reports/SWE%20benchmark%20candidates.md)). MiMo-V2.6-Pro's results are taken at high, its AA configuration (O54); Vals records its run without a level, read as the same single reasoning mode (E252).

| Leaf | Group | Weight, max-effort ranking | Weight, AI Coding Daily ranking | Raw unit | Score | Run by |
|---|---|---:|---:|---|---|---|
| [FrontierCode 1.1](https://artificialanalysis.ai/evaluations/frontiercode) | Software engineering | 15.00% | 21.00% | AA score (0-1) | z = 100 × score | AA-run |
| [Terminal-Bench 4.0 (AA run)](https://www.tbench.ai/leaderboard/terminal-bench/4.0) | Software engineering | 11.00% | 17.00% | % resolved | z = resolution % | AA-run |
| [Bug Hunt Bench](https://bughunt.productcompass.pm/) | Software engineering | 8.00% | 12.00% | bugs fixed of 105 | z = 100 × bugs fixed / 105 | independent |
| [Vibe Code Bench v1.1 (Vals)](https://www.vals.ai/benchmarks/vibe-code) | Software engineering | 5.00% | — | % of test workflows passed | z = pass rate % | independent |
| [Code Migration v1.1 (Vals)](https://www.vals.ai/benchmarks/code-migration-v1-1) | Software engineering | 6.00% | — | % of hidden tests passed | z = pass rate % | independent |
| [LiveBench 2.0 Overall](https://livebench.ai/) | Software engineering | 15.00% | — | mean of seven category scores (0-100) | z = mean of the seven category scores | independent |
| [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | General professional work | 10.00% | 10.00% | Elo | z = 100 × (Elo − 500) / 2000 (AA's integration transform) | AA-run |
| [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | General professional work | 10.00% | 10.00% | AA score (0-1) | z = 100 × score | AA-run |
| [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience) | Reliability | 10.00% | 10.00% | AA Omniscience Index (-100 to 100) | z = (I + 100) / 2 on AA's Omniscience Index I (O28) | AA-run |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | Long context, science & knowledge | 5.00% | 5.00% | accuracy (0-1) | z = 100 × accuracy | AA-run |
| [Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | Long context, science & knowledge | 1.67% | 1.67% | accuracy (0-1) | z = 100 × accuracy | AA-run |
| [SciCode](https://artificialanalysis.ai/evaluations/scicode) | Long context, science & knowledge | 1.67% | 1.67% | score (0-1) | z = 100 × score | AA-run |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | Long context, science & knowledge | 1.67% | 1.67% | score (0-1) | z = 100 × score | AA-run |
| [AI Coding Daily (excl. bug finding)](https://aicodingdaily.com/leaderboard) | Software engineering | — | 10.00% | points of 60 | z = 100 × points / 60 | independent |

**Source clocks (owner decisions O59, O60).** Each non-AA quality source is captured at most 30 days before the release cutoff; a capture taken after the cutoff stands only when the source's own last update is dated before the cutoff's day. Vals AI: Vibe Code Bench v1.1, captured 2026-10-23T07:58:05Z (source updated 2026-10-20); Vals AI: Code Migration v1.1, captured 2026-10-23T07:58:05Z (source updated 2026-10-20); LiveBench: LiveBench 2.0 Overall (release 2026-10-14), captured 2026-10-23T07:58:31Z (source updated 2026-10-18); AI Coding Daily (Povilas Korop): AI Coding Daily LLM Coding Leaderboard (Laravel quality + React-TS quality + edge-case testing, max 60), captured 2026-10-23T07:58:31Z (source updated 2026-10-21); Bug Hunt Bench scoreboard, captured 2026-10-23T05:37:06Z (source updated 2026-10-19); tbench.ai Terminal-Bench 4.0 leaderboard, captured 2026-10-23T05:35:48Z; Cognition: FrontierCode leaderboard, captured 2026-10-23 (source updated 2026-10-22).

Only configurations with every leaf are ranked (O36). A leaf is taken, in order, from AA (or the benchmark's own primary source), from a newer AA capture, from another party that ran the same benchmark version on the exact configuration (Cognition for FrontierCode, tbench.ai for Terminal-Bench), then from the model provider's published result. A row with a provider-claimed leaf competes in the interval outputs but earns no label of its own (E233). A configuration still missing a leaf after an exhaustive search logged within 7 days of the cutoff is listed with its missing leaves and search, not ranked; a required frontier family is listed the same way (O38). For a listed frontier or near-frontier family the search also logs an open-web discovery step: its queries and every candidate result, each resolved by a dated registry addition or a dated rejection with its reason, and the build fails on an unresolved candidate (E240). Every gap fill and search is in [raw-data.md](raw-data.md#leaf-gap-fills-and-searches-o36).

Coverage is the observed share of quality weight. A row is **provisional** when coverage is below 70%, fewer than 2 software-engineering leaves are observed, observed software-engineering weight is below 40%, or a leaf weighing 20% or more of quality (FrontierCode 1.1) is missing. Provisional rows are ranked and flagged; there is no quality floor (O8). Missing leaves are never filled; the interval outputs treat each one as anywhere in 0–100.

## Plan basis

Plan cost = basket API cost ÷ a subscription route's Value Multiple, at full utilisation. **The Plan ranking has one row per configuration and plan (owner decision O48)**: every plan on which the configuration has an eligible route, each plan's route chosen by the comparator below among that plan's candidates; rows of one configuration share its quality and API cost and differ only by the plan's multiple, share every scenario draw, and are told apart by any value gap; a configuration's own Plan figures (the main table, model pages, and the Plan diagnostics that rebuild anchors or move evidence) are those of its selected route's plan row. Every route record names one model and one plan (O45). A Value Multiple is the API-priced usage a subscription delivers per dollar of fee. Route evidence is graded: **controlled** measurements of the exact model, **reports** (at least two independent, comparable end-user reports concordant within 20%), owner-named **assumptions** (a measured multiple transferred to another model, labelled), and **diagnostic** evidence, which is shown but never ranked. Two owner-authorised classes sit beside them: GPT-6.1 Sol and GPT-6 Astra keep their own SemiAnalysis figure on every ChatGPT plan (a figure that names a model without an effort binds to its unsuffixed, max row), and every other GPT row takes the lower of the two figures per plan as a labelled assumption (O45); each MiMo-V2.6 model takes, per Token Plan tier, the quota-implied ceiling — the tier's monthly credits valued at Xiaomi's API rate for that model over the list fee — labelled provider-derived and not a measurement (O46), because Xiaomi prices credits at parity with its API and no end-user measurement of a V2.6 billing period exists. Routes certifiably dearer than another identified route of at least equal grade are set aside (E88); the official route is then chosen by identification class, evidence grade, the comparison multiple, lower gross cash and route ID (E85). Evidence past its 90-day expiry and 30-day grace is demoted to diagnostic. A configuration without an admitted route uses its API cost, flagged. Each Plan row publishes its fee period, the cash paid and the selected multiple's amount (multiple × gross cash), typed by what the measurement establishes (E166): measured-workload capacity, observed eligible consumption with capacity not established, assumed API-equivalent consumption for an owner-named transfer (with its donor), or identified target-workload capacity; API-fallback rows publish none.

**Identification (E61).** A multiple is measured on its own workload; it identifies the basket's multiple only when the workloads match. Today 0 of 27 Plan rows are point-identified and 0 set-identified, so the Plan ranking is labelled exploratory. A measured-only Plan view (`3d83f7643d4a85b7`) re-runs the selection over exact-route measurement candidates of grade controlled or concordant reports (no transfers, no diagnostics), without transfers or fallbacks. Because the official Plan anchors include transfers and fallbacks, a calibration diagnostic rescores the measured-only rows on anchors built from measured evidence alone (E164), so an assumption's effect through the exchange rate is visible.

**Subscription evidence policy** (as of 2026-10-08; reporting window 2026-09-23 to 2026-10-23; end-user reports were last searched on 2026-10-21, so reports dated in the 2 days after it were not searched):

- Default numerator: Actual API-priced end-user-reported use or reported estimate anchored to measured use; exact model, tier and dates required.
- Selected source for Anthropic, OpenAI: [SemiAnalysis](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (2026-10-06, owner-selected 2026-10-07): Controlled subscription-account measurements with agentic workload projections.
- GPT: User authorizes the same ChatGPT plan multiples for every GPT model. Owner decision O45 (2026-10-23): GPT-6.1 Sol and GPT-6 Astra keep their own SemiAnalysis figures on every ChatGPT plan, bound to each model's unsuffixed (max) row because SemiAnalysis names the models without an effort; every other GPT row (other GPT models and GPT-6.1 Sol at xhigh, high, medium and low, ranked as their own rows under O33) takes, per plan, the lower of the two reported model-conditional figures as a labelled user assumption naming its donor route. Routes are one row per model and plan.
- Claude: User authorizes (2026-10-18, Option 2) applying Opus 5.5's measured SemiAnalysis Claude plan multiples to every other Claude model. Opus 5.5 keeps its exact measured routes; the shared routes are labelled user assumptions, carry the recorded caution that allowances are model-specific (Fable 5.1 measured 12.4-12.7x on the same plans), and are superseded by any exact measurement for the listed model. Claude Fable 5.1 (retained 2026-10-21, owner decision O31) has exact SemiAnalysis measurements on Max 5x (12.73x) and Max 20x (12.425x), which replace the shared routes for it; it has no Pro route, because the source records Fable as unavailable on Pro, so there is no Pro allowance to measure or assume. Owner decision O33 (2026-10-21) ranks Claude Haiku 5.5 (max, high, medium, low) and Claude Sonnet 5.5 (xhigh, high, medium, low) as their own rows; as other Claude models in the roster they take the shared assumption routes.
- MiMo: Owner decision O46 (2026-10-23), an explicit exception to the end-user numerator rule: each MiMo-V2.6 model takes, per Token Plan tier, the quota-implied ceiling (the tier's monthly credits valued at Xiaomi's pay-as-you-go rate for that model, divided by the list fee), labelled provider-derived. It replaces the 2026-10-08 provisional 1.5x assumption. End-user measurements for the exact model and tier replace the ceiling once they meet the admission rule of any other provider's route (O11); one report alone does not (owner decision O62).
- Other models: Use API fallback; do not transfer evidence across model versions, variants or thinking effort except for the explicit common GPT, Claude and MiMo assumptions.
- Provider allowance, quota and marketing figures never supply the measured numerator; a provider's published price can be the fee denominator only when the tier mapping is supported.

## Uncertainty outputs

**Interval outputs (O25).** Each observed leaf is placed anywhere inside its published reporting precision, each missing leaf anywhere in 0–100 and each cost inside its rounding. A configuration is on the **definite frontier** when no other configuration can beat it on both cost and quality for any values in those boxes, and on the **possible frontier** when some values put it there. The **cheapest above a quality bar** is confirmed only when its worst cost is below the best cost of every other configuration that could qualify. The bar is pinned by policy `quality-quartile-ladder` v3: the lower quartile, lower median (the headline bar) and upper quartile, each the displayed quality at zero-based position floor((n - 1) * k / 4), k = 1, 2, 3 (O34) of non-provisional ranked configurations with a displayed quality, ordered by displayed quality ascending, then configuration ID, selected deterministic at anchor freeze, before any bar outcome is computed; the displayed quality at each ladder position, frozen as a level; the configuration at that position is recorded for audit and competes like any other; a frozen level is never a configuration, so no bar can return its setter by construction; whether a result compares alternatives is published per result (possibleQualifierN, E198); fixed for the anchor version; replaced only by a versioned re-freeze that publishes old- and new-bar results on the common evaluable panel. Current headline bar: quality 64.3 (the displayed quality of Gemini 4 Argon at freeze); ladder: quality 54.2, quality 65.0.

**Scenario shares** are frequencies over declared streams, never probabilities (10,000 scenarios per run, seed 20261023, input hash `a7281cc9e1dcee4b`):

- **S0**: published-record reporting precision.
- **S1**: published-record reporting precision + conventional identification of missing leaves.
- **S2**: published-record reporting precision + conventional identification of missing leaves + weight-specification stress.
- **S1M**: published-record reporting precision + conventional identification of missing leaves + conventional range sensitivity inside published 95% confidence intervals (no tail model).
- **S1T**: published-record leaf values redrawn with plug-in binomial task-sampling noise from each leaf's published task count (independent-task approximation; GDPval-AA from its displayed rating interval, an assumption) + conventional identification of missing leaves.

S1 also runs with the endpoint-heavy kernel. **S1T (owner decision O39)** redraws every leaf with plug-in binomial noise from its published task count (the proportion taken as (k + ½)/(n + 1), so a 0% or 100% score keeps a positive spread) (FrontierCode 100, Terminal-Bench 66, AutomationBench-AA 657, AA-LCR 100, SciCode 288, HLE 2,158, CritPt 70, Bug Hunt's 105 bugs, AA-Omniscience's 6,000 questions scored +1/0/−1, LiveBench 2.0 Overall as the mean of its seven category shares (Long Agentic 18, Reasoning 4, Coding 29, Browser 25, Data Analysis 3, Research 22, Design 25; Reasoning and Data Analysis publish only their parts, so their counts are the wide reading, E264), AI Coding Daily's 6 graded projects), with GDPval-AA drawn from its displayed rating interval read as a 95% normal interval (an assumption) and the two Vals boards from Vals' published standard error (E256). Tasks are treated as independent, so it is an approximation; it never authorises a label or changes a score. From the same noise the ranking prints a **noise band** beside each rank (O42): rows in value order join the current band while their value is not separable from the band's first row (1.96 × √(SD_i² + SD_j²), with analytic quality-leaf SDs; cost is not drawn), otherwise they start a new one, so every row is inseparable from its band's first row and adjacent rows in different bands may also be inseparable. Shared tasks correlate two rows' errors and narrow the true threshold (separable adjacent ranks at correlations 0.3 and 0.6 are published), while omitted sources widen it (run-to-run and harness variance, AA's single cost run, owner-named transfer error on the Plan basis); the net direction is not established. Each bar also has a **noise-margin companion** (O44): the cheapest configuration whose displayed quality clears the bar by at least the quality noise margin, 1.96 × √2 × the median row's quality SD. On the Plan basis the core streams (S1, S2, S1M and S1T) run with owner-named transfers off (E167): a row whose selected route is a transfer is unevaluable there, never reselected or replaced by API cost, while S0 keeps the displayed record. S1M draws Terminal-Bench 4.0 (AA run) inside its source's published 95% confidence interval, labelled conventional CI-range sensitivity (endpoint-conditioned; no tail model) under its interpretation contract (E165; estimand: not established from the captured documentation; method: not established from the captured documentation; sampling unit: not established from the captured documentation); values outside the interval are not explored; no tail mass is invented. A cheapest-above-the-bar label is published only when the share clears a sequential threshold with its per-look error controlled. Not quantified in these shares:

- benchmark repeatability beyond S1T's independent-task approximation (correlated tasks, harness and attempt effects): not quantified in v1 scenario shares.
- fitted-parameter uncertainty beyond S1T's assumed GDPval-AA rating interval: not quantified in v1 scenario shares.

## Diagnostics

Diagnostics are published beside the ranking and never change a score: Terminal-Bench cross-source agreement (AA's run against tbench.ai), FrontierCode cross-source agreement (AA against Cognition) and gap-fill removal (E234), anchor stability (exchange-rate series and trimmed-anchor rank shifts), Omniscience abstention sensitivity, quality source shares, matched-panel quality agreement, non-discriminating leaves, group drift, quality dispersion, deletion sensitivity (leave-one-benchmark-out and source deletions) and the standing removal of the Terminal-Bench cost component. Current results are in [scores.md](scores.md#diagnostics).

## Release gates

| Rule | Status | Detail |
|---|---|---|
| clip gate (E20) | passed | no basis exceeds the clipping allowance |
| cost influence flag (E91) | passed | cost not discriminating (< 10%); informational only; beta never changes (O2) |
| quality influence flag (E126) | passed | quality not discriminating (cost share > 90%); informational only |
| subset scoring (O17) | fired | subset rows scored on their own workload and anchors |
| partial component flag (E37) | vacuous | AA declined- or missing-task markers, or an Index reconstruction that misses AA's total (E209) |
| route dominance filter (E88) | vacuous | certifiably dearer routes set aside |
| Plan exploratory label (E61) | fired | fewer than half of Plan rows have an identified M_W |
| score swing gate (E177) | vacuous | first v3 release: no previous v3 release to compare |
| anchor migration (E184) | vacuous | no main-workload migration deferred |
| configuration map coverage | passed | every cohort row has a pinned identity |
| quality clipping audit (E110) | passed | saturation disclosed; domain violations block the build |
| full benchmark set (O36, O38) | fired | listed, not ranked: gpt-6.1-sol-high, claude-opus-5-5-high, claude-opus-5-5-medium, gpt-6.1-sol-medium, gpt-6-astra-high, claude-haiku-5-5-high, gpt-6-luna-xhigh, claude-haiku-5-5-medium, gpt-6-luna-high, gpt-6-luna-medium, gpt-5.6-luna-low, claude-haiku-5-5, claude-haiku-5-5-low, claude-opus-5-5-xhigh, claude-sonnet-5-5-xhigh, gpt-6-astra-xhigh, gpt-6-luna-low, gpt-6.1-sol-xhigh, mimo-v2-6-flash, minimax-m3-1-flash |
| missing-leaf rules (O8 provisional, E198b, E201b, E219, E221, E226) | vacuous | no ranked row has a missing leaf (O36) |
| S1M interval stream (E145) | vacuous | dormant: no ranked leaf carries a published confidence interval since O37, so S1M equals S1 (E236) |
| provider-claim label denial (E233) | vacuous | no row has a provider-claimed leaf |
| scenario outputs current (E72) | passed | scenario input hash matches the scored inputs |

## Limitations

- Cost is the contestant-model API token cost of AA's runs, not total agent or workflow operating cost.
- Cost scores use frozen anchors; a new anchor version is a published migration, never a silent change.
- The basket is AA's SDLC-relevant evaluations at AA's token mix, not your own workload.
- Results are never transferred between model versions or reasoning efforts; missing evidence stays missing.
- Published values are rounded; interval outputs and scenario shares show which differences the evidence supports. Benchmark sampling noise is approximated in one scenario stream (S1T) that treats tasks as independent, so adjacent ranks often lie within that noise.
- Subscription Value Multiples are measured on their own workloads; none is yet identified on the basket, so the Plan ranking is exploratory.

## Machine-readable files

- [data/scores.json](data/scores.json): the `v3` section holds every row, workload, anchor, interval output, scenario result, diagnostic and the evidence bundle
- [data/plan_cost_routes.json](data/plan_cost_routes.json): subscription routes, their evidence, sources and policy
- [data/v3_frozen.json](data/v3_frozen.json): frozen anchors, bar policy and anchor policy for anchor version `v3-2026-10-23`
- [data/v3_scenarios.json](data/v3_scenarios.json): scenario-share runs for every stream
- [data/tb4.json](data/tb4.json), [data/bug_hunt.json](data/bug_hunt.json): independent benchmark snapshots ([data/aa_deepswe.json](data/aa_deepswe.json) keeps AA's last DeepSWE v1.1 capture, no longer scored, O49)
- [data/leaf_evidence.json](data/leaf_evidence.json), [data/cognition_frontiercode.json](data/cognition_frontiercode.json): leaf gap fills and the exhaustive-search log (O36/O37)
