# Ultradeep critique cycles

## Cycle 1 — coverage and cohort audit

**Question:** Does the refresh maximize the defensible cohort and benchmark count without manufacturing data?

**Findings:** The live DeepSWE Best view supplied 21 current model cards. The AA page parser supplied complete primary coverage for 12 benchmark/index fields plus AA evaluation cost; numeric Speed was incomplete for GPT-6 Astra. Supplemental fields were intentionally not promoted into the score because their coverage is partial.

**Resolution:** Retain 21 models and 13 dimensions including the composite cost; drop Speed from the primary score, keep its raw null, and record all supplemental coverage in `coverage_matrix.json`.

## Cycle 2 — adversarial source and version audit

**Question:** Could the result silently mix benchmark versions, owner views, or provider configurations?

**Findings:** AA v4.1/v4.1.1 changed several benchmark identities and grading procedures. The owner tau/HLE/SciCode/GPQA/Terminal-Bench sources establish provenance but do not provide a directly interchangeable matrix for every selected model/configuration. A prior visible-label extraction pattern could confuse a version token such as `v2.1` with a metric.

**Resolution:** Pin the current AA v4.1.1 page payloads, decode `currentModel`, preserve selected effort variants, use owner sources only for interpretation, and exclude retired benchmark labels from v1.4.

## Cycle 3 — publication and reproducibility audit

**Question:** Do the generated data, scoring code, docs, site, and research ledger tell the same story?

**Findings:** Generated outputs agree on version 1.4.0, 21 models, 13 retained dimensions, the top-five order, and the Speed caveat. Cost and quality are separated, Pareto membership is captured, and no neutral-fill path is used. The research validators still need to be run against the completed ledger before release.

**Resolution:** Keep the generation scripts and machine-readable snapshots together under `.refresh/v1.4/`, keep the research ledger under its dated directory, run all Silver validation gates, then refresh Graphify and verify the final Git tree before push.

## Counterevidence register

- **Higher raw capability does not guarantee a higher overall rank:** Claude Opus 5 and GPT-5.6 Sol have stronger quality scores than the overall leader, but the composite gives cost substantial priority.
- **Speed cannot be treated as complete:** GPT-6 Astra’s selected page reports N/A, so including Speed would require an unjustified fill.
- **Owner leaderboard values are not assumed interchangeable:** separate tau owner results are retained as provenance, not silently merged with AA tau3 Banking values.
- **Historical benchmark names are not current data:** legacy labels remain documented only to explain exclusions.
