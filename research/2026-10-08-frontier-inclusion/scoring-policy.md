# AA Frontier Inclusion in the Primary Score

## Source and roster

The score builder reads the refreshed frontier reconciliation inventory at
`.refresh/v1.4/aa_reconciliation_inventory.json`. The inventory retains every
directly observed Pareto point, its exact Artificial Analysis URL, family,
evaluated configuration, observation values, and the canonical ValueRank model
ID required for that family. The builder checks the inventory against its
referenced capture artifact before using it.

For each distinct frontier family, all inventory rows must agree on one
`requiredFamilyModelId`. Exactly one observed inventory row must identify that
model ID. The selected AA metrics row must have the same model ID, display
family, direct owner URL, and effort. Reasoning-only catalog entries must have
no selected effort; fallback configurations must preserve their fallback
label. A missing family mapping or changed selected identity stops the refresh
instead of silently dropping a frontier family.

The primary cohort is the union of:

1. Models with an exact DeepSWE v1.1 result and an eligible Bug Hunt result.
2. The canonical selected model ID required for each family in the current AA
   frontier inventory.

Other AA catalog models remain outside the primary score unless they meet one
of those two inclusion rules. The full frontier configurations remain in the
reconciliation inventory, including alternate efforts; results are never
transferred between efforts.

## Missing metrics and scoring

Missing benchmark values stay null in source fields. A null value never becomes
a zero, average, or rank. Each score dimension is percentile-ranked across only
the primary-cohort models with an observed value for that dimension. At least
two observations are required to assign a comparative percentile; a singleton
observation remains available as source data but is omitted from normalized
score dimensions and reported as a dropped dimension.

The existing priority values remain unchanged: DeepSWE v1.1 has priority 25 and
Bug Hunt has priority 20. For each model, the weighted composite is the
priority-weighted mean of only its available normalized dimensions. The score
builder records `metricCoverage` on every model row with:

- `availablePriority`: sum of priorities for dimensions with a normalized value
  on that row.
- `totalPriority`: sum of priorities for dimensions with at least two cohort
  observations, including Bug Hunt's priority 20 when at least two eligible
  results are available.
- `coveragePct`: `100 * availablePriority / totalPriority`, on a 0–100 scale.
- `missingKeys`: effective primary dimensions without a normalized value on
  that row.

Rows without a normalized non-cost quality dimension remain in the primary
cohort with null overall and quality scores and no rank, even if a cost value
is available. Required frontier rows must have a finite quality score to pass
the source guard. Dimensions absent from a row are omitted from `dims` and
`vRanks`.

The Bug Hunt emphasis view remains a measured-only companion ranking. It uses
only rows with both an eligible Bug Hunt result and an exact DeepSWE result;
frontier inclusion by itself does not qualify a model for that view. Its
dimensions also require at least two observations and renormalize per row over
the dimensions with actual values.

## Current capture

The 2026-10-08 inventory records 14 observed frontier configurations across
five model families. The family-to-model mapping is read from the inventory at
each refresh, rather than maintained as a fixed list in the scoring code.
