# Subscription API-equivalent route research

Research artifact dated **2026-10-05**. It covers all 25 exact model IDs in ValueRank's current roster and keeps exact variant identity, plan tier, cadence, price currency, allowance denominator, API tariff, and workload profile visible.

## Start here

- [table.md](table.md): 25-row Markdown coverage and best quantified current route.
- [tier-register.md](tier-register.md): complete Markdown table of 60 qualified exact-model paid tier/cadence routes; ambiguous DeepSeek catalog tiers are separated in `route-exceptions.csv`.
- [model-coverage.csv](model-coverage.csv): one machine-readable coverage row per exact ValueRank model ID.
- [route-tiers.csv](route-tiers.csv): 60 qualified model × provider × tier × cadence rows with denominators, profile calculations, source links, and unknown fields. [route-exceptions.csv](route-exceptions.csv) retains eight DeepSeek V4/V4.1 catalog tier rows excluded from exact-version ranking.
- [routes.json](routes.json): complete structured model records, candidate routes, sources, evidence, claims, and validation counts.

## Evidence package

`sources.jsonl`, `evidence.jsonl`, and `claims.jsonl` provide the source registry and claim-support trail. `scope.md`, `research-plan.md`, `triangulation.md`, `outline.md`, `research_report.md`, `critique.md`, `decision-record.md`, `handoff.md`, `methodology.md`, `query-log.md`, `run_manifest.json`, and `vloop-rollup.json` record the Silver Bullet Deep Research Ultradeep workflow.

The table uses the three transparent profiles in [methodology.md](methodology.md). Every value is a dated estimate, not a universal token total. Z.AI values are time-sensitive and include peak-only, all-off-peak, and current campaign treatment. Quarterly Z.AI fee rows remain unknown when the official page did not disclose a fee.

## Selection boundary

“Selected” means best API-equivalent usage per effective monthly price among the qualified, exact-model routes in this package. It is not a complete provider-market census. Some exact model subscriptions have a public plan but no API-comparable denominator; these are marked not computable. For OpenAI/Codex, crowdsourced allowance evidence came only from the TiboTattle homepage; the homepage was in a checking state, so no numeric allowance was used.

User-reported numeric allowance observations were not used in route calculations. The current-window package review was bounded to 2026-09-05 through 2026-10-05; where reports in those packages named no plan, they were treated as “not stated” and not promoted to a plan-tier denominator.

## Workflow and verification status

Silver Bullet's `WF-SILVER-DEEP-RESEARCH` Ultradeep artifact contract is followed, including scope, plan, retrieval, triangulation, outline, synthesis, three critique cycles, refinement notes, decision record, handoff, and validation logs. The listed JavaScript `ctx_execute` route rejected that language, so the package's saved Python validator was run through the supported LeanCTX shell execution route; all local package checks passed. Silver Bullet-specific automated phase gates were not run, and parent review is pending.

All artifacts are in this newly owned directory. No project files outside it were changed.
