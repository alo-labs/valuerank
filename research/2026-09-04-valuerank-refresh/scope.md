# Scope: ValueRank periodic ranking refresh (2026-09-04)

## Decision question

What is the most current, source-backed ValueRank ranking of frontier models, using the latest DeepSWE Best roster and the largest defensible set of benchmark dimensions with comparable coverage across the ranked cohort?

## Objective

Refresh the dated ranking inputs and all dependent publication artifacts. Increase the number of ranked models and retained benchmark dimensions where current evidence supports them, while preserving the zero-gap rule: no missing benchmark cells, neutral fills, or silently mixed benchmark versions.

## In scope

- Current DeepSWE Best roster, effort configuration, pass@1, average cost per task, task count, and source update date.
- Current Artificial Analysis model-page data, including the Intelligence Index version, component evaluations, evaluation cost, speed, and model identity/variant mapping.
- Official benchmark or benchmark-owner documentation needed to interpret version changes and validate coverage.
- Cohort inclusion/exclusion, benchmark-version compatibility, normalization, composite-cost construction, ranking, quality score, Pareto frontier, and publication outputs.
- Citation-tracked research artifacts and an implementation handoff for the canonical `.refresh/v1.4/` pipeline.

## Out of scope

- Running new model evaluations or submitting benchmark tasks.
- Merging provider-specific pricing or measurements that do not represent the selected model/configuration.
- Rewriting historical ValueRank versions.
- Treating unverified social posts or snippets as benchmark evidence.

## Working assumptions

1. The periodic refresh should create the next version after v1.3.1 rather than overwrite history.
2. DeepSWE v1.1 Best is the primary cohort source because the current product explicitly uses DeepSWE as its roster gate.
3. Artificial Analysis remains the primary cross-benchmark source for the AA component matrix, but its benchmark-version changes must be reflected in the methodology.
4. A model may be retained in a non-ranked appendix when useful data exists but a required cost or benchmark field is unavailable.
5. Values are captured as observed on 2026-09-04 UTC; later page changes require a new refresh.

## Success criteria

- Every ranked model has complete values for every retained dimension.
- Every retained dimension has one compatible benchmark definition/version across the cohort.
- Current sources are independently cross-checked where practical, with source identity and evidence spans persisted.
- The generated ranking, README, methodology, raw-data, site, and ledgers agree on version, cohort, dimensions, and scores.
- Validation logs show report structure, citation integrity, claim support, and phase-gate status.
