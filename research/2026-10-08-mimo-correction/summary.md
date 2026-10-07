# MiMo V2.6 ingestion correction

Both exact identities, `mimo-v2-6-pro` and `mimo-v2-6-flash`, are now in ValueRank's 27-model source roster. They were missing from the selected AA ingestion roster; neither omission was justified by its position on AA's displayed cost/intelligence Pareto frontier.

## Captured evidence

AA public profile/chart capture on 7 October 2026, Intelligence Index v4.3.2:

| Model | Intelligence Index (rounded public label) | Total AA benchmark cost | Briefcase Elo | GDPval-AA 2.1 Elo |
|---|---:|---:|---:|---:|
| MiMo V2.6 Pro | 46 | $206.66 | 1516 | 1686 |
| MiMo V2.6 Flash | 38 | $109.41 | 1495 | 1611 |

Sources: [Pro profile](https://artificialanalysis.ai/models/mimo-v2-6-pro), [Flash profile](https://artificialanalysis.ai/models/mimo-v2-6-flash), [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa). Per-metric source URLs, capture dates and precision notes are retained in the AA snapshot and metrics artifacts. Both selected AA identities have reasoning enabled.

The [pinned Bug Hunt owner notes](https://github.com/phuryn/bug-hunt-bench/blob/7dd3c23a4c86a3fac586707d01129bf549bae325/results/run-notes.md) supply Pro's first-party, thinking-enabled result of 18/105 (single run). Flash's default-route mean is 23.3/105 across three runs, but the notes do not establish its reasoning configuration. That result is visible as an owner configuration, without being transferred to the selected reasoning variant.

## Primary-ranking coverage gaps

- Pro: no exact-variant AA DeepSWE result in the selected AA snapshot.
- Flash: no exact-variant AA DeepSWE result; Bug Hunt reasoning equivalence remains unverified.
- Provider DeepSWE launch claims are retained separately with their provenance, but the selected AA harness/variant equivalence is unverified.
- LiveBench and the separate retained Terminal-Bench 4.0 snapshot lack exact MiMo matches; these remain null. AA's own TB4 component is recorded separately.

Both MiMo models therefore appear as unranked source candidates and frontier entries. The existing 13 primary ranks and scores remain unchanged.

## Future omission guard

The new AA reconciliation gate compares the selected roster with an explicitly captured displayed AA frontier. The capture has 691 selected catalog entries, 173 plotted eligible models and 14 frontier vertices. Ten other frontier variants have explicit dated deferrals rather than silent omissions. The gate checks freshness, source/version metadata and variant identity; unresolved entrants block publication. Display-rounded intelligence labels are identified as rounded.

## Build and publication record

The correction uses selected-source builds, not a claim that every benchmark was freshly recaptured. AA metrics, LiveBench ingestion, scores, frontier reconciliation and publication generation were rebuilt. No tests were run. Publication commit and deployment status are recorded in the completion response.
