# Decision record: ValueRank v1.4.0 refresh

Date: 2026-09-04 UTC
Baseline: v1.3.1 at `a2edc36d8451cdeef253eebacbc4202b2b3c1a06`
Decision status: accepted for validation and release

## Decisions

### D1 — cohort gate

Use the current DeepSWE v1.1 Best roster as the ranked cohort. This produces 21 models and preserves the selected effort/configuration on each model record. Do not expand the cohort using arbitrary models absent from the Best view.

### D2 — benchmark source and version

Use current Artificial Analysis v4.1.1 first-party model-page payloads for the comparable matrix. Record the v4.1/v4.1.1 benchmark identity and grading changes in the methodology. Do not mix IFBench, Terminal-Bench Hard, or tau2 Telecom into current v1.4 dimensions.

### D3 — parser correctness

Decode the structured `currentModel` payload embedded in each selected first-party page. Visible labels and chart text are not a safe metric parser because version strings can resemble numeric values.

### D4 — dimension retention

Apply a strict zero-gap rule: retain a candidate dimension only when all 21 ranked models have numeric values for the same definition/version. Retain 13 dimensions including cost; drop Speed because GPT-6 Astra is null. Never neutral-fill missing data.

### D5 — composite and interpretation

Use normalized AA evaluation cost plus normalized DeepSWE average cost per task as the cost composite, with lower cost better. Report quality separately from the cost-inclusive overall score so users can distinguish capability from value.

### D6 — supplemental data

Keep partial supplemental fields in the extraction and coverage matrix for future expansion, but exclude them from the primary score until cohort coverage is complete and definitions are compatible.

### D7 — provenance and secrets

Persist source IDs, evidence spans, capture dates, and direct URLs. Use public first-party pages for this refresh; do not add an Artificial Analysis API key or other credentials to the repository.

## Consequences

The ranking maximizes the currently defensible model and dimension count while remaining auditable. The score is a ValueRank decision model, not a claim that AA’s published index weights or any benchmark owner’s leaderboard has been reproduced. The result is a time-bounded snapshot and requires another refresh when source pages or benchmark versions change.
