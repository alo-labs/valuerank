# MiMo ingestion correction

Date: 2026-10-08. Scope: selected identities, AA extraction, benchmark coverage inputs, and primary-score eligibility. Exact AA page identities and numerical capture are supplied by the coordinating agent from the built-in browser.

## Changes

- Added `mimo-v2-6-pro` / `MiMo-V2.6-Pro` and `mimo-v2-6-flash` / `MiMo-V2.6-Flash` to `aa_mapping.json` and the selected `aa/aa_extract.json` roster. The exact page URLs are `https://artificialanalysis.ai/models/mimo-v2-6-pro` and `https://artificialanalysis.ai/models/mimo-v2-6-flash`. No reasoning-effort slug is inferred: selected `variant` remains null until a source explicitly identifies an effort variant.
- Added Xiaomi developer identities and publication short names in `build_scores.py` so the new records pass identity validation.
- Added explicit null LiveBench identity mappings. The selected LiveBench release stays pinned to `2026_06_25` and commit `7be9f746f36a6f007dd78461f67cb7d06cfe2304`. Null means no verified exact mapping; it does not establish that the model has never been evaluated. Unmatched records keep all scores/costs null and expose a match status and coverage note.
- Added per-record AA capture dates and methods to metric provenance. This supports a mixed-date source snapshot without presenting every retained model as newly captured. Missing Intelligence Index data receive `intelligenceIndexStatus: missing`.
- Added explicit ranking exclusion reasons per score row and in scoring coverage / ranking summaries. The existing exact AA DeepSWE plus eligible Bug Hunt gate is preserved. The missing-field list now reports Bug Hunt missing only when its actual source result is unmatched; exclusion solely for DeepSWE no longer incorrectly marks Bug Hunt missing.

## Source boundaries

AA owner values, provider claims, and null external coverage stay distinct. No score is copied from another MiMo release or effort variant. No AA cost is inferred from API token prices or a cost-per-task label. Required primary ranking coverage is assessed against the selected source snapshots; absence there is not a claim of universal external absence.

The coordinating agent independently read both exact AA reasoning profiles and public charts in the built-in browser. Those supplied observations are now appended to `aa/aa_v432_snapshot.json` with per-record UTC observation dates and capture method; existing September records and their original top-level capture date are preserved. No precise payload extraction is claimed for these display readings.

| Owner field | Pro | Flash | Precision |
|---|---:|---:|---|
| Intelligence Index | 46 | 38 | Whole display score |
| Total AA evaluation cost | $206.66 | $109.41 | Public total-cost tooltip, cents |
| Speed | 40.1 | 56.4 | Profile display, one decimal |
| Briefcase Elo | 1516 | 1495 | Separate profile card, whole Elo |
| GDPval-AA v2.1 Elo | 1686 | 1611 | Separate owner evaluation chart, whole Elo |
| Briefcase normalized | 51% | 50% | Display-rounded percentage |
| GDPval-AA v2.1 normalized | 59% | 56% | Display-rounded percentage |
| AutomationBench-AA | 59% | 64% | Display-rounded percentage |
| Terminal-Bench 4.0, AA evaluation | 35% | 23% | Display-rounded percentage |
| SciCode | 61% | 51% | Display-rounded percentage |
| HLE | 49% | 35% | Display-rounded percentage |
| GDP.pdf | 19% | 9% | Display-rounded percentage |
| CritPt | 27% | 12% | Display-rounded percentage |
| Omniscience accuracy | 35% | 27% | Display-rounded percentage |
| Omniscience non-hallucination | 59% | 46% | Display-rounded percentage |
| AA-LCR | 86% | 74% | Display-rounded percentage |

Briefcase normalized and GDPval normalized fields are explicitly separate from raw Elo. The raw GDPval Elo readings come from [the owner evaluation chart](https://artificialanalysis.ai/evaluations/gdpval-aa); they are not substituted from Xiaomi's launch claim or reverse-converted from the displayed percentages. Existing raw GDPval scores are not mixed with normalized percentages. Original score construction is unchanged; the additional normalized fields are retained in source coverage and score rows for display.

Provider DeepSWE launch claims of 71.9% Pro and 67.9% Flash are retained in `provider_claims.json` with direct launch citation, source type and publication date. They are ineligible for the primary rank because exact AA DeepSWE v1.1 benchmark, harness and evaluated-variant equivalence have not been established. The existing AA DeepSWE gate remains in place.

## Independently observed Bug Hunt coverage

The official all-runs board, updated 2026-10-01, and its run notes at commit `7dd3c23a4c86a3fac586707d01129bf549bae325` were inspected through the built-in browser. Both MiMo models have owner results; calling either universally missing would be wrong.

| Configuration | Owner score / 105 | Sample | Run date | Treatment |
|---|---:|---:|---|---|
| Pro, Xiaomi first-party, thinking explicitly enabled | 18 | 1 | 2026-09-22 | Selected exact reasoning configuration |
| Pro, OpenRouter default, reasoning state unasserted | 22.7 | 3 | 2026-09-22 | Retained as a distinct alternate configuration |
| Flash, OpenRouter default, reasoning state unasserted and untested | 23.3 | 3 | 2026-09-22 | Retained owner evidence; selected-variant equivalence unresolved |

The Pro first-party run uses a binary thinking toggle, not a graduated reasoning tier. Its $0.59 cost is a list-rate estimate according to its specific run notes. The Pro OpenRouter $0.86 and Flash OpenRouter $0.49 means are measured bills. Pro's OpenRouter mean blends two judge standards. Flash's three runs span 19–26 fixes; Pro's OpenRouter runs span 20–24. None of those alternate results are transferred to an explicitly enabled configuration. Records carry per-model current source URLs, commit and observation time; the retained September source snapshot metadata is not advanced.

Sources: [all-runs board](https://bughunt.productcompass.pm/?preset=all), [first-party Pro notes](https://github.com/phuryn/bug-hunt-bench/blob/7dd3c23a4c86a3fac586707d01129bf549bae325/results/run-notes.md#mimo-v26-pro-first-party), [Pro OpenRouter mean](https://github.com/phuryn/bug-hunt-bench/blob/7dd3c23a4c86a3fac586707d01129bf549bae325/results/run-notes.md#mimo-v26-pro---mean-of-3), [Flash OpenRouter mean](https://github.com/phuryn/bug-hunt-bench/blob/7dd3c23a4c86a3fac586707d01129bf549bae325/results/run-notes.md#mimo-v26-flash---mean-of-3).

## Review and remaining integration

Graphify was queried first and pointed to the current pipeline. Targeted source reads and diff review confirmed the selected-roster loop, identity gate, exact external roster checks, and eligibility gate. The read-only helper `ingestion-inspection.cjs` reports bounded schema and roster evidence through LeanCTX.

No tests or builds were run by this implementation agent. The coordinating agent owns independent verification, generation, and publication. Both AA numerical records are integrated from supplied browser observations. Bug Hunt records declare both new IDs and preserve the exact configurations. Terminal-Bench cohort metadata is reconciled against its retained source snapshot. Before generation, LiveBench must be regenerated from the expanded AA cohort.

The parent integration run found an existing missing `claude-opus-5-5` key in the strict LiveBench map: 27 AA IDs versus 26 mapping IDs, with no extra keys. Read-only comparison confirmed the retained pinned-release LiveBench snapshot already declares this model unmatched with a null LiveBench identity. Added an explicit null mapping for that existing identity; no alias or benchmark value was inferred. This repairs roster completeness while preserving the retained snapshot's missing coverage.

## Review rework

- Publication metadata in `build_scores.py` is now v1.9.4 / October 8, 2026. Underlying source observation dates are preserved.
- GDPval primary metadata now names raw `gdpval` Elo. `gdpvalV21` reads only raw Elo and remains null when that source field is absent; normalized percentages cannot silently enter the raw-Elo column. Normalized observations stay in the separate `gdpvalV21Normalized` field.
- Each selected MiMo entry declares `captureMode: public-rendered`. `capture_aa_v432.py` checks those records before initiating automatic network captures. It retains the existing record, including precision, source URLs and original observation date, only when its per-record UTC capture is no more than seven days old and matches the selected URL. Missing, stale, future-dated or incomplete public records fail with an actionable built-in-browser recapture instruction. The automatic payload path cannot replace those records.
- Other automatic records retain their normal capture path. No full capture run or tests were performed for this rework; parent static review and the normal generation steps remain the validation boundary.
