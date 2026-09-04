# Research plan: ValueRank periodic refresh

## Mode and rationale

Mode: **ultradeep**. The request is a recurring, high-impact public ranking refresh with an explicit requirement to maximize benchmark coverage and model count. The Silver-Bullet phase contract therefore targets up to 40 sources, a minimum average credibility of 75, three critique cycles, and a complete evidence/claim audit.

## Retrieval lanes

### Lane A — cohort and coding cost

- DeepSWE live leaderboard: version, task count, update date, Best roster, effort, pass@1, average cost, output tokens, and agent steps.
- DeepSWE methodology/changelog/blog: benchmark version, task construction, harness, and comparability constraints.
- DeepSWE paper or official technical material where it clarifies methodology beyond the live table.

### Lane B — Artificial Analysis benchmark matrix

- Current model pages for every DeepSWE Best model, trying the relevant effort/configuration variants.
- AA Intelligence Index v4.1.1 announcement and methodology: component definitions, weights, version transitions, cost-per-task semantics, and grading changes.
- Individual benchmark pages or owner documentation for GDPval-AA v2, Terminal-Bench 2.1, τ³-Bench Banking, HLE, GPQA Diamond, SciCode, CritPt, AA-Omniscience, AA-LCR, and any additional AA evaluation that has broad cohort coverage.
- AA Data API documentation as the structured-data route if an authenticated API key is available; never place a key in the repository.

### Lane C — independent benchmark triangulation

- Official benchmark owner repositories/papers for the retained dimensions.
- Current benchmark leaderboards or release notes for newly added models, used to cross-check identity and version rather than to replace AA’s comparable measurements.
- Release announcements from model providers only for model identity, release date, and configuration facts.

### Lane D — implementation and integrity

- Existing `.refresh/v1.3/` scripts and ledgers.
- Current root methodology/raw-data/scores and the publication emitter.
- Generated output consistency and zero-gap validation.

## Search strategy

1. Start with first-party/live leaderboard pages and official benchmark documentation.
2. For each newly observed model, resolve one stable model identity and all plausible AA page slugs/configurations.
3. Capture benchmark version, configuration, value, retrieval date, and exact source URL together; never copy a number without its variant context.
4. Build a model × benchmark coverage table before choosing the cohort or retained dimensions.
5. Cross-check high-materiality changes (new models, score leaders, cost changes, version upgrades, and exclusions) against at least one independent source.
6. Delta-retrieve only where coverage, version, or claim-support checks expose a gap.

## Analysis rules

- Prefer comparable benchmark versions over superficially larger coverage.
- Keep model family, effort, harness, provider, and fallback metadata explicit.
- Preserve provider isolation and do not merge distinct model variants merely because their display names are similar.
- Retain a dimension only when all ranked models have a current value for the same definition/version.
- If a candidate dimension is incomplete, record the missing models and keep it as a documented candidate/drop rather than imputing.
- Recompute normalization and weights after benchmark/version decisions; do not carry forward old weights blindly when AA changed its index composition.

## Deliverables

This research run will produce the Silver-Bullet artifacts in this directory and a downstream handoff describing exact files, commands, data changes, and verification required to publish the next ValueRank version.
