# Exact-effort evidence notes

Evidence inspected against the 2026-11-01T06:10:00Z v3.0.0 release. JSON locators below use zero-based array indices. These notes do not establish evidence outside the stored captures.

## Requested efforts

The common diagnostic requires ten leaves: `bugHunt`, `terminalBench`, `gdpval`, `frontierCode`, `automationBench`, `lcr`, `hle`, `tbScience`, `critpt`, `omniscience`. Main adds `vibeCode`, `codeMigration`, `livebench2Overall`; AI Coding Daily adds `aiCodingDaily`. These are the actual `quality.leaves` keys in `data/scores.json` at `v3.rows[0]`, `v3Tracks.aicd.rows[0]`, and `v3Tracks.common.rows[0]`. See also `valuerank/value_v3.py` for the scorer. Only exact configuration evidence qualifies.

Neither `claude-sonnet-5-5-medium` nor `claude-opus-5-5-low` has a row in any of the three track `rows`, a model record in `data/aa_metrics.json`, an entry in `data/aa_mapping.json`, or a direct `modelId` entry in `data/leaf_evidence.json` supplements or searches. Neither has a captured model page in `data/aa/aa_v432_snapshot.json` (`pages`). Thus a complete scorer-ready set of any track's leaves is not established, and there is no basis to score either effort. The absence of a direct record does not prove every benchmark was never run.

There is partial evidence worth distinguishing: `data/leaf_evidence.json` `searches[105].notes` and `searches[110].notes` mention AI Coding Daily Sonnet 5.5 Medium 60.54, Claude Code, 2026-09-29; `searches[102].notes` and `searches[106].notes` mention Opus 5.5 Low 60.5, Claude Code, 2026-10-19. These are notes in searches for *other* effort IDs, not admitted exact-effort scorer records. The remaining required leaves are not established as scorer-ready for either effort in the inspected records. AA's FrontierCode configuration catalogue records Sonnet Medium as a cleared unheld label in `data/v3_configuration_map.json` `unheldLabels.cleared[13]`, not a held score. Do not transfer other-effort scores.

## Stand-ins, not the requested efforts

| Configuration | Track | Published API cost / value / rank | Published Plan cost / value / rank |
|---|---|---|---|
| Sonnet 5.5 Max | main | $10,501.82 / 53.659 / 6 | $178.30 / 67.746 / 7 |
| Sonnet 5.5 Max | common diagnostic | $6,644.38 / 47.063 / 8 | $112.81 / 57.313 / 16 |
| Sonnet 5.5 XHigh | common diagnostic | $2,611.82 / 43.793 / 17 | $44.34 / 56.098 / 30 |
| Opus 5.5 Medium | AI Coding Daily | $1,867.53 / 48.082 / 13 | $31.71 / 59.526 / 7 |
| Opus 5.5 Medium | common diagnostic | $1,867.53 / 43.070 / 18 | $31.71 / 56.114 / 29 |

Source: `data/scores.json`, each named track's `rows`, matched by `id` and `effort`. These are different workloads and efforts, not estimates of the requested efforts. The common track is diagnostic only and earns no interval or scenario label.

The unlabelled `claude-sonnet-5-5` row is Max: `data/scores.json` main and common row `effort` is `max`; `data/aa_mapping.json[25].aaVariant` is `max`; `data/v3_configuration_map.json` `rows.claude-sonnet-5-5.frontiercode` names max with fallback; `data/aa/aa_v432_snapshot.json` `pages[25].model.name` explicitly says Max, Default Fallback. The mapping's unsuffixed ID is not an effort indicator.

## DeepSeek price basis

`data/scores.json` DeepSeek V4.1 Flash 1017 row's `valuationGate.inForce` records AA's displayed capture prices per million input/cache-read/output/cache-write as $0.30/$0.006/$1.20/$0.30, observed 2026-11-01T05:57:26Z. `data/aa/aa_v432_snapshot.json` `pages[31].model` records input $0.30, output $1.20, cache hit $0.006, but cache-write price null; the gate supplies its own $0.30 figure. `data/aa_metrics.json` `models.deepseek-v4-1-flash-1017` points to this snapshot and AA model page. Compared with the user-stated OpenCode peak prices ($0.30/$1.20/$0.006 input/output/cache read), those three categories match; off-peak ($0.15/$0.60/$0.003) is half. OpenCode cache-write treatment and exact underlying run's time/category distribution are not established here. Consequently a nominal 10x at OpenCode prices cannot generally be translated to an exact AA-priced allowance without the token mix and peak/off-peak distribution: at a uniform all-peak rate the three matching categories imply 10x, and at uniform all-off-peak, 20x on AA's corresponding peak-rate basis, assuming matching quantities and no additional category differences. This differs from simply halving the nominal ratio for all-peak; the calculation's baseline must be specified. OpenCode's 1017 mapping is an owner assumption and its usage limit is not measured consumption.

## Inspection checks

Read-only Python JSON inspection confirmed v3.0.0 and cutoff; track row counts 9, 20, 33; the exact leaf key sets and stand-in values above; zero direct supplements/searches for the requested IDs; and AA snapshot and mapping identity. The sandbox Python checks imported only the standard library; `PYTHONDONTWRITEBYTECODE=1` was not explicitly set, contrary to the assigned instruction. No project modules were imported. A JavaScript JSON parse initially failed because this file contains non-standard numeric values; Python's JSON parser read it. No benchmarks, builds, external model calls, or production data edits were performed. This audit did not independently search every raw board for new exact-effort results or fetch OpenCode's page.
