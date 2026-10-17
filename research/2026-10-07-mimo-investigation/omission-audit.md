# MiMo omission audit

Date: 2026-10-07. Scope: repository source and ranking pipeline only; live AA frontier membership and launch dates are being checked separately. Models requested: MiMo V2.6 Pro and MiMo V2.6 Flash.

## Finding

Both models were omitted at the input-roster stage. The current selected AA input roster contains 25 models and neither MiMo nor Xiaomi occurs in its records. Capture refreshes only those selected URLs, metric extraction iterates only those records, and ranking construction iterates only the resulting metric dictionary. Consequently an otherwise eligible newly launched AA model cannot enter through the current `npm run refresh` command.

This is a selected-roster maintenance gap, not a demonstrated Pareto rejection. The repository supplies no model-specific rejection record for either MiMo model and does not establish that either was assessed against the primary ranking's coverage gate.

## Evidence chain

| Stage | Observed fact | Source |
|---|---|---|
| Selected identities | 25 records; zero MiMo/Xiaomi matches | `.refresh/v1.4/aa_mapping.json` |
| Selected AA pages | 25 records; zero MiMo/Xiaomi matches | `.refresh/v1.4/aa/aa_extract.json` |
| Refresh entrypoint | `refresh` calls external refresh, AA build, score build and publication; no roster-discovery step | `package.json:11-16` |
| Capture | Loads `aa_extract.json`, requires unique selected URLs, maps `capture` over those entries | `.refresh/v1.4/capture_aa_v432.py:47-51` |
| AA extraction | Loads mapping and selected extraction files; loops `for entry in extracted` | `.refresh/v1.4/build_aa_metrics.py:165-179` |
| Current metrics | 25 keyed models; zero MiMo/Xiaomi matches; observed `2026-09-29T18:16:57Z` | `.refresh/v1.4/aa_metrics.json` |
| Ranking input | Reads metric dictionary as `aa_models`; loops that dictionary only | `.refresh/v1.4/build_scores.py:217-223`, `:267-277` |
| Main-rank gate | Requires eligible Bug Hunt match AND non-null exact AA DeepSWE score | `.refresh/v1.4/build_scores.py:337-344` |
| Exact DeepSWE variants | Chart mappings require `exact_variant` and mapped IDs must belong to selected AA roster; current chart has zero MiMo/Xiaomi records | `.refresh/v1.4/build_scores.py:233-247`; `.refresh/v1.4/aa_deepswe.json` |
| Output | v1.9.3, published September 30, observed September 29; 25 source models and 13 ranked models | `.refresh/v1.4/ranking_summary.json` |
| Exclusions | Twelve existing roster rows fail the ranking gate; neither MiMo is in that exclusion list | `.refresh/v1.4/ranking_summary.json`, `rankingExcludedModels` |

The most recent recorded change to selected input files is commit `52427df` (2026-09-30T04:21:04+10:00), subject “Add GPT-6 Sol, Luna and Grok 4.7 to rankings.” This proves dated selected-file maintenance; it does not establish the historical intent behind failing to add MiMo.

## Pareto comparison

The repository's emitted Pareto set compares normalized AA evaluation cost against **ValueRank's weighted quality composite**, within the 13-row primary cohort. It is not the AA Intelligence Index versus total AA benchmark execution cost frontier requested by the user. `qualityScore` combines retained non-cost weights (`build_scores.py:452-455`); the Pareto dominance check uses `costComposite` and `qualityScore` (`:469-483`). Cost is AA execution-cost-only normalized by the primary cohort maximum (`:346-359`). Therefore live membership of both MiMo models on AA's Intelligence/cost frontier would not cause the present pipeline to discover or include them automatically.

The only located MiMo text in the publication emitter is an old illustrative Plotly annotation string at `emit_v14_docs.py:990` (“MiMo +13.9 pts (cost bonus)”). It supplies no identity, source record, current metric, or exclusion explanation.

## Defensible explanation and limits

The direct implementation cause is that neither model was ingested into the selected AA source roster. The refresh workflow reuses a dated finite roster rather than discovering all current AA models or Intelligence/cost frontier members. No model-specific evidence supports an explanation that they were deliberately excluded for weak value or for missing Bug Hunt/DeepSWE coverage.

Even after roster ingestion, exact AA DeepSWE and eligible Bug Hunt coverage must be checked before granting a primary composite rank. The repository's absent records cannot prove current external benchmark coverage. If a model lacks required coverage, it can be listed in source/comparison data with explicit missing fields and a reason for withholding that particular composite; no result should be transferred across variants or neutral-filled.

## Concrete correction path

1. Capture the exact MiMo V2.6 Pro and Flash AA pages, IDs, variants, current Intelligence Index scores and total benchmark costs, preserving observation dates.
2. Extend the selected identities, page roster and identity maps; capture and build metrics.
3. Check exact AA DeepSWE and eligible Bug Hunt rows for each model. Record each gate outcome explicitly.
4. Expose the requested AA Intelligence Index/cost Pareto frontier independently of the primary composite's stricter cohort, if the intended product scope includes that frontier.
5. Add roster-discovery or a dated reconciliation report so future frontier entrants cannot disappear silently from a successful refresh.

No ranking code or published ranking artifacts were modified for this audit.

## Reproduction

Read-only helper: `research/2026-10-07-mimo-investigation/omission-helper.cjs`.

`node research/2026-10-07-mimo-investigation/omission-helper.cjs json .refresh/v1.4/aa_mapping.json .refresh/v1.4/aa/aa_extract.json .refresh/v1.4/aa_metrics.json .refresh/v1.4/aa_deepswe.json`

`node research/2026-10-07-mimo-investigation/omission-helper.cjs window .refresh/v1.4/build_scores.py 336 350`

`node research/2026-10-07-mimo-investigation/omission-helper.cjs window .refresh/v1.4/build_scores.py 464 484`

Graphify was queried first and pointed to the current builders; conclusions above were then checked against actual files. Native ctx tools returned an agent-registration capacity error, so execution used the project-authorized `/Users/shafqat/.local/bin/lean-ctx -c` CLI with bounded Node output.
