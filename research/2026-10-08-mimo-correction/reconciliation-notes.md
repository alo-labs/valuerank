# AA frontier reconciliation

The selected model roster cannot prove it contains AA's displayed intelligence/total-cost frontier. The guard compares a separate dated capture with exact AA profile IDs and evaluated variants in `aa_metrics.json`. Several effort variants share a profile URL, so a slug alone never establishes exact coverage. Before allowing any name match, the guard checks canonical effort, reasoning mode, and fallback state. A contradictory `evaluatedVariant` cannot be bypassed by an identical display name. Effort and fallback are compared separately, so `max with fallback` can match stored `aaVariant: max` plus the explicit fallback display label. MiMo's `reasoning` variant matches `isReasoning: true` when `aaVariant` is null. Unknown declared variants and contradictory metadata do not match.

`npm run refresh` invokes `npm run reconcile:aa` after scoring and before publication. Missing, stale, partial, invalid, or version-mismatched capture blocks refresh. Observed frontier variants absent from the exact source roster block it with an actionable list. Primary eligibility rules remain unchanged; documented unranked source candidates satisfy roster reconciliation and remain unranked.

## Public capture schema

Save `.refresh/v1.4/aa_reconciliation_inventory.json` with:

- `mode`: `observedFrontier`.
- `intelligenceIndexPrecision`: `rounded_whole_public_label` for this capture. All 14 AA intelligence inputs are rounded public whole-number labels and publish as, for example, `46 (rounded)`, without invented decimal precision. Per-row metadata can override the global field in future captures. Observed-frontier rows lacking precision metadata preserve their provided numeric representation rather than adding two decimal places. Captured MiMo total costs publish to cents.
- `observedAt`: timezone-qualified ISO 8601 timestamp, no more than seven days old.
- `benchmarkVersion`: exact AA intelligence index version matching `aa_metrics.json`.
- `sourceUrl`: first-party AA intelligence versus total evaluation cost chart URL.
- `scope`: exact filters and capture scope; distinguish catalog models, plotted eligible points, and displayed frontier.
- `sourceUniverse`: `{ "selectedModelN": 691, "plottedPointN": 173, "observedFrontierPointN": 14 }` for the parent's October 8 observation. Counts are capture evidence, not hardcoded constants; update them on future observations.
- `completeness`: `{ "status": "complete", "note": "Capture method, all displayed frontier identity coverage, artifact references, and public export limitations" }`. Complete refers to all displayed frontier identities, not a fabricated numeric catalog.
- `rows`: one record per displayed frontier variant: `{ "aaId": "profile-slug", "name": "Exact displayed evaluated variant", "evaluatedVariant": "exact effort", "sourceUrl": "https://artificialanalysis.ai/models/profile-slug", "directlyObservedFrontier": true, "intelligenceIndex": null, "totalCostUsd": null }`. Numeric metrics remain null when unavailable. Exact stored names can establish matching without `evaluatedVariant`; generic family/profile names cannot.

All frontier identities must be captured uniquely by profile plus evaluated variant, and row count must equal `observedFrontierPointN`. Repeated slugs with distinct variants are allowed. Missing public numeric exports do not block identity reconciliation; gaps remain visible.

For intentionally excluded evaluated variants, provide `rosterDecisions`: an array of `{ "aaId": "exact-slug", "name": "same exact captured name", "evaluatedVariant": "same captured variant if supplied", "decision": "defer", "reviewedAt": "timezone-qualified ISO8601", "reason": "specific reviewed omission and no transfer to selected effort" }`. Review must follow this capture. This allows a refresh to proceed after each missing variant has been explicitly reviewed without pretending it is included. Missing, deferred, and unresolved frontier IDs remain separate report fields, and the table shows each dated reason. An unmatched decision blocks reconciliation.

The integrated October 8 capture has 14 observed frontier points and 10 explicit deferrals, including GPT-6.1 Sol max; that exact generation remains absent from the current roster. These counts describe the present capture rather than implementation constants.

Membership comes directly from AA's displayed frontier. The guard does not recompute an all-AA frontier from 14 rows, infer metrics from SVG coordinates, require unplotted catalog models to have costs, or treat the public benchmark selector as DeepSWE evidence.

Optional `fullNumericUniverse` mode retains numeric dominance computation for an actually complete documented chart universe. It requires finite intelligence/cost pairs. A partial selected roster must not be labelled a full universe.

## Outputs and integration

The guard writes `.refresh/v1.4/aa_reconciliation_report.json`, including freshness, missing exact frontier variants, observed entries, metric gaps, universe counts, and primary-rank status. `--report-only` writes a blocked diagnostic without passing refresh.

`emit_v14_docs.py` recomputes reconciliation and adds the separate table to README, raw-data, and the main site. It distinguishes AA's observed intelligence/total-cost frontier from ValueRank's composite-quality/cost frontier, labels missing numbers, and preserves unranked status and exact primary evidence gaps. The raw Bug Hunt table additionally shows available nonselected owner configurations, including MiMo Flash's default-route result whose selected reasoning equivalence remains unresolved. Direct publication can show a partial capture with a blocked scope warning; it does not constitute successful `npm run refresh`.

Graphify was queried first; its older graph served as navigation evidence. Static current-source review confirmed exact roster fields, publication boundaries, refresh chain, and the site's `</main>` insertion point. No tests or builds were run as instructed. Parent integration owns capture validation, guard execution, publication generation, and rendered review.

Independent review found an earlier matcher could accept a matching display name before validating contradictory declared effort. That material defect was repaired by validating canonical metadata first. Parent integration must verify the repaired matching behavior against the real capture and its reviewed roster decisions before publication.

Context Mode JavaScript execution returned an unsupported-language error; native fallback was hook-blocked. Short routed reads/searches were used, and edits used `apply_patch`.
