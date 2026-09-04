# Triangulation and conflict register

## Source triangulation

The refresh uses a layered source hierarchy. The live DeepSWE leaderboard is the cohort authority; its changelog and technical overview provide release and methodology context. Artificial Analysis first-party model pages supply the comparable cross-benchmark matrix, while the Artificial Analysis methodology and release notes define the benchmark-version contract. Benchmark-owner pages and papers are used to validate interpretation and lineage, not to replace the selected comparable matrix.

| Question | Primary source | Independent check | Resolution |
| --- | --- | --- | --- |
| Which models enter the cohort? | [S1] DeepSWE Best leaderboard | [S2] changelog and [S3] technical overview | Use the 21 current Best cards and record the v1.1/113-task snapshot. |
| Which benchmark definitions are current? | [S4] AA methodology | [S5] v4.1 and [S6] v4.1.1 release notes | Use AA v4.1.1 identities and current grading; do not mix retired labels into v1.4. |
| Are task families interpreted correctly? | [S8] Terminal-Bench repository, [S10] tau repository, [S12] SciCode repository | [S7] Terminal-Bench release, [S9] tau leaderboard, [S11] HLE owner leaderboard, [S13] GPQA paper | Preserve owner provenance and use AA’s comparable page values for the score matrix. |
| Are page values parsed as metrics? | [S18]–[S38] first-party AA model pages | [S4] methodology and [S17] model directory | Decode the structured `currentModel` payload; never infer a value from a visible version label or chart text. |
| Can a candidate dimension be retained? | `.refresh/v1.4/coverage_matrix.json` | `aa_metrics.json` plus the parsed page snapshots | Retain only dimensions complete across all 21 models; preserve nulls and drop Speed. |

## Conflicts and decisions

1. Artificial Analysis publishes its own component weights, while ValueRank has a separate product objective that explicitly gives cost priority and incorporates DeepSWE. The report distinguishes AA’s published index construction from the ValueRank composite; the v1.4 weights are not presented as a reproduction of AA’s overall index.
2. DeepSWE exposes more configurations than the Best view. The refresh uses the current Best cards because that is the product’s cohort gate; effort/configuration identity remains attached to each row.
3. The benchmark-owner tau view and the AA tau3 Banking matrix are related but not interchangeable. The owner view validates lineage; the AA page values remain the comparable cohort inputs.
4. GPT-6 Astra has no numeric speed value on the selected AA page. Speed is therefore excluded from the primary composite rather than imputed, and the raw null is retained for transparent supplemental reporting.
5. Legacy IFBench, Terminal-Bench Hard, and tau2 Telecom labels are historical context only. They are not merged into v1.4 because current AA releases replaced those benchmark identities.

## Residual uncertainty

The snapshot is time-bounded to 2026-09-04 UTC. Public pages may change after capture, some supplemental benchmark fields remain partial, and the DeepSWE leaderboard’s uncertainty intervals are not converted into a probabilistic ValueRank ranking. A future refresh should re-fetch the live pages and repeat the same coverage and version checks.
