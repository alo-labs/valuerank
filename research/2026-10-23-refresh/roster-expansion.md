# Roster expansion 2026-10-23 (owner decision O51)

Owner decision O51 (2026-10-23): the cohort is every configuration Artificial Analysis (AA) plots on its rendered Intelligence Index vs. Cost to Run frontier or within 3 Index points of it, and each plotted effort is its own row. Ten plotted configurations in `data/aa_reconciliation_inventory.json` (observed 2026-10-23T05:27:39Z) had no roster row of their own. They were represented only through their family's selected configuration, under the "alternate configuration retained" roster decisions. This record covers how each was added.

All web content was treated as data. No sign-in, cookie, paid export or private API was used.

## Capture instant

- **AA model pages:** `python3 -m valuerank.capture_aa` (`npm run capture:aa`) captured all 61 pages in `data/aa/aa_extract.json`: the 51 existing rows plus the 10 new ones. It ran from 2026-10-23T06:26:02Z to **2026-10-23T06:26:23Z**, which is the snapshot's `capturedAt`. Every page returned HTTP 200, and `capture_aa` refused none.
- **AA metrics:** `valuerank.build_aa_metrics` ran through a scratch wrapper. The wrapper sent its second output, `coverage_matrix.json`, to the session scratchpad, so the repository's `data/coverage_matrix.json` was not touched. It ran with `VALUERANK_NOW=2026-10-23T06:26:23Z`. `data/aa_metrics.json` now has 61 models with `observedAt` 2026-10-23T06:26:23Z, and `data/price_records.json` `observedAt` is the same instant.
- **Not re-captured:**
  - The chart capture (`data/aa_frontier_capture.json`, inventory at 2026-10-23T05:27:39Z).
  - The cost-chart capture (`data/aa/cost_charts_capture.json`, 2026-10-23T05:35:10Z).
  - The Bug Hunt pin (46802fc). `git ls-remote` at about 06:25Z still reports HEAD = 46802fc312b6fd467b0baee519df05693f120232. The scoreboard and run-notes sha256 values were re-verified unchanged.

### Re-capture of the 51 existing pages (05:30:42Z to 06:26:23Z)

None of the following changed for any existing row: Intelligence Index, Index cost, price, FrontierCode, Terminal-Bench, GDPval Elo, AutomationBench, Omniscience (accuracy, hallucination rate and index), AA-LCR, HLE, SciCode, CritPt, GDP.pdf or Briefcase.

The payload did change:
- AA no longer sends the `gdpvalNormalized` field on any page. The pages now carry `gdpvalInterval` (Elo lower and upper bound), and some pages also carry `aa3dEloInterval`. As a result `aa_metrics.json` `gdpvalV21Normalized` is now `null` for every model. It is a pass-through display field (`build_scores.py`), not a quality leaf; the leaf reads `gdpvalV21`, the Elo, which is unchanged. **Code follow-up:** derive (Elo − 500)/2000 when AA omits the field, or drop it.
- Speed, latency and time-per-task fields moved slightly, as they do on every capture.

## The ten new rows

Index and cost are AA's page values (`intelligenceIndex`, `intelligenceIndexCost.total`) at 06:26:23Z. They equal the chart tooltip values (rounded Index; two-decimal USD). Prices are USD per 1M input / output tokens.

| Id | AA URL | AA name (short) | Tier on the 05:27:39Z chart | Index | Index cost (USD) | Price |
|---|---|---|---|---|---|---|
| `gpt-6-luna-low` | https://artificialanalysis.ai/models/gpt-6-luna-low | GPT-6 Luna (low) | frontier vertex | 21.53 (22) | 10.63 | 0.10 / 0.50 |
| `gpt-6-luna-medium` | https://artificialanalysis.ai/models/gpt-6-luna-medium | GPT-6 Luna (medium) | frontier vertex | 29.93 (30) | 31.17 | 0.10 / 0.50 |
| `gpt-6-luna-high` | https://artificialanalysis.ai/models/gpt-6-luna-high | GPT-6 Luna (high) | frontier vertex | 32.93 (33) | 47.85 | 0.10 / 0.50 |
| `gpt-6-luna-xhigh` | https://artificialanalysis.ai/models/gpt-6-luna-xhigh | GPT-6 Luna (xhigh) | frontier vertex | 34.56 (35) | 66.81 | 0.10 / 0.50 |
| `claude-opus-5-5-high` | https://artificialanalysis.ai/models/claude-opus-5-5-high | Claude Opus 5.5 (high with fallback) | frontier vertex | 53.58 (54) | 2,172.43 | 4 / 20 |
| `claude-opus-5-5-xhigh` | https://artificialanalysis.ai/models/claude-opus-5-5-xhigh | Claude Opus 5.5 (xhigh with fallback) | frontier vertex | 55.99 (56) | 4,056.65 | 4 / 20 |
| `claude-opus-5-5-medium` | https://artificialanalysis.ai/models/claude-opus-5-5-medium | Claude Opus 5.5 (medium with fallback) | near, gap 1 (ref. GPT-6.1 Sol (max)) | 51.24 (51) | 1,626.81 | 4 / 20 |
| `gpt-5.6-luna-low` | https://artificialanalysis.ai/models/gpt-5-6-luna-low | GPT-5.6 Luna (low) | near, gap 1 (ref. GPT-6 Luna (low)) | 21.01 (21) | 27.02 | 0.20 / 1.20 |
| `gpt-6-astra-high` | https://artificialanalysis.ai/models/gpt-6-astra-high | GPT-6 Astra (high) | near, gap 3 (ref. Claude Opus 5.5 (high with fallback)) | 50.92 (51) | 2,925.01 | 10 / 50 |
| `gpt-6-astra-xhigh` | https://artificialanalysis.ai/models/gpt-6-astra-xhigh | GPT-6 Astra (xhigh) | near, gap 2 (ref. Claude Opus 5.5 (high with fallback)) | 52.39 (52) | 3,802.98 | 10 / 50 |

Ids follow the existing effort-row convention: `gpt-6.1-sol-xhigh`, `claude-haiku-5-5-low`, `claude-sonnet-5-5-xhigh`. Each `data/aa_mapping.json` row carries `family`, `aaSlug` and `aaVariant` (AA's effort slug; for Claude, the effort without the "with fallback" qualifier, as for Claude Sonnet 5.5). `build_aa_metrics` validated the slug and effort of every new page against the mapping.

With these rows, all 29 rendered-frontier and near-frontier configurations in the inventory resolve to their own roster row: `aa_reconciliation.exact_roster_match` returns the matching id for each. The inventory was not edited:
- A roster decision is consulted only when a row has no exact roster match.
- The ten "alternate configuration retained" decisions still name observed variants, so they remain valid.
- Their wording now describes a superseded state. They can be removed or re-dated at the next inventory review, as for the Haiku and GPT-6.1 Sol effort rows that were already in the roster.

## Leaves on each AA page (exact configuration)

| Id | FrontierCode | Terminal-Bench 4.0 | GDPval-AA (Elo) | AutomationBench-AA | Omniscience Index | AA-LCR | HLE | SciCode | CritPt |
|---|---|---|---|---|---|---|---|---|---|
| `gpt-6-luna-low` | 14.06% | 0.00% | 1029.43 | 12.05% | −9.17 | 74.00% | 20.25% | 46.88% | 2.57% |
| `gpt-6-luna-medium` | 31.81% | 2.53% | 1261.32 | 40.46% | −5.05 | 78.33% | 28.27% | 50.93% | 10.57% |
| `gpt-6-luna-high` | 32.03% | 4.55% | 1339.36 | 47.82% | −5.50 | 79.33% | 32.95% | 50.35% | 15.43% |
| `gpt-6-luna-xhigh` | 33.22% | 8.08% | 1362.25 | 47.80% | −1.83 | 80.00% | 34.34% | 51.74% | 17.43% |
| `claude-opus-5-5-high` | 53.96% | 56.57% | 1703.40 | 63.21% | 40.63 | 82.67% | 55.56% | 60.42% | 30.86% |
| `claude-opus-5-5-xhigh` | 53.54% | 59.60% | 1830.29 | 64.95% | 42.65 | 84.67% | 57.51% | 65.05% | 31.71% |
| `claude-opus-5-5-medium` | 57.05% | 52.53% | 1582.90 | 61.22% | 40.32 | 84.33% | 54.73% | 59.26% | 27.71% |
| `gpt-5.6-luna-low` | **missing** | 0.00% | 992.25 | 11.69% | −14.65 | 70.00% | 19.83% | 46.06% | 2.57% |
| `gpt-6-astra-high` | **missing** | 54.04% | 1522.36 | 66.61% | 43.73 | 80.00% | 53.06% | 55.44% | 28.86% |
| `gpt-6-astra-xhigh` | **missing** | 59.60% | 1555.31 | 67.18% | 43.42 | 80.00% | 54.59% | 55.67% | 31.43% |

Every page also has GDP.pdf and AA-Briefcase. Terminal-Bench 0.00% for GPT-6 Luna (low) and GPT-5.6 Luna (low) is AA's published value, not a missing value.

**FrontierCode gap, and a registered second source:** AA's `frontierCode` is null for GPT-5.6 Luna (low), GPT-6 Astra (high) and GPT-6 Astra (xhigh). Under O37 the next source is Cognition. `data/cognition_frontiercode.json` (sha256 `ff004077…d75f`, byte-identical at the 2026-10-23 refresh) has each exact effort, all run in the Codex harness:

| Configuration | Cognition value | Locator |
|---|---|---|
| GPT-6 Astra (high) | 0.5094 | `v1_1.data['GPT-6 Astra'].high.main.new_score` |
| GPT-6 Astra (xhigh) | 0.5062 | `v1_1.data['GPT-6 Astra'].xhigh.main.new_score` |
| GPT-5.6 Luna (low) | 0.1538 | `v1_1.data['GPT-5.6 Luna'].low.main.new_score` |

These have **not** been written to `data/leaf_evidence.json`, which is outside this task's file ownership. The owner of that file must add them as `supplements` in the same form as the existing Cognition entries, for example claude-opus-5. Until then, those three rows lack FrontierCode.

## Pinned configuration identities (`data/v3_configuration_map.json`)

| Id | FrontierCode cost chart (05:35:10Z all-model capture) | ITBench-AA cost chart | Coding Agent Index v2.0 |
|---|---|---|---|
| `gpt-6-luna-low` | GPT-6 Luna (low), $1 | none | none |
| `gpt-6-luna-medium` | GPT-6 Luna (medium), $3 | none | none |
| `gpt-6-luna-high` | GPT-6 Luna (high), $4 | none | none |
| `gpt-6-luna-xhigh` | GPT-6 Luna (xhigh), $5 | none | none |
| `claude-opus-5-5-high` | Claude Opus 5.5 (high with fallback), $125 | none | none |
| `claude-opus-5-5-xhigh` | Claude Opus 5.5 (xhigh with fallback), $398 | none | none |
| `claude-opus-5-5-medium` | Claude Opus 5.5 (medium with fallback), $78 | none | none |
| `gpt-5.6-luna-low` | none | none | none |
| `gpt-6-astra-high` | none | none | none |
| `gpt-6-astra-xhigh` | none | none | none |

Notes on the pins:
- **Terminal-Bench** needs no pin: AA's own run is on each model page, and every new row has it.
- **Coding Agent Index v2.0:** the capture (`research/2026-10-23-refresh/coding-agents-v2.0-capture-2026-10-23.json`, the same labels as the current `data/aa/coding_agents_capture.json`) lists Opus 5.5, GPT-6 Luna and GPT-6 Astra only at max. The "Devin Fusion CLI" rows ("Claude Opus 5.5 Max + GPT-6 Luna High", "GPT-6 Astra XHigh + SWE-2 Medium") are model combinations, not these configurations. All ten labels are therefore absent.
- **No new cost-chart capture was made:** the existing capture had no label for GPT-5.6 Luna (low), GPT-6 Astra (high) or GPT-6 Astra (xhigh) on either chart.

## Bug Hunt (`data/bug_hunt.json`, rule E206, pinned commit 46802fc)

Each record is the owner's largest-sample published result for the exact model and effort. Each was checked with `build_scores.check_bug_hunt_selection` against `data/bug_hunt_scoreboard.json`, and its run-notes anchor exists at the pinned commit.

| Id | Owner row | Fixed of 105 | n | Harness / route | Reported |
|---|---|---|---|---|---|
| `gpt-6-luna-low` | GPT-6 Luna (low effort) | 4 | 1 | Codex CLI 0.155.1 / ChatGPT account | 2026-09-23 |
| `gpt-6-luna-medium` | GPT-6 Luna (medium effort) | 4 | 1 | Codex CLI 0.155.1 / ChatGPT account | 2026-09-23 |
| `gpt-6-luna-high` | GPT-6 Luna (high effort) | 9 | 1 | Codex CLI 0.155.1 / ChatGPT account | 2026-09-23 |
| `gpt-6-luna-xhigh` | GPT-6 Luna (xhigh effort) | 14 | 1 | Codex CLI 0.155.1 / ChatGPT account | 2026-09-23 |
| `claude-opus-5-5-high` | Opus 5.5 (high effort) - mean of 3 | 31.7 | 3 | Claude Code / Anthropic API | 2026-09-23 |
| `claude-opus-5-5-xhigh` | Opus 5.5 (xhigh effort) - mean of 3 | 36.0 | 3 | Claude Code / Anthropic API | 2026-09-23 |
| `claude-opus-5-5-medium` | Opus 5.5 (medium effort) - mean of 3 | 30.3 | 3 | Claude Code / Anthropic API | 2026-09-23 |
| `gpt-5.6-luna-low` | GPT-5.6 Luna (low effort) | 4 | 1 | Codex CLI / OpenAI | 2026-08-27 |
| `gpt-6-astra-high` | GPT-6 Astra (high effort) | 35 | 1 | Codex CLI / OpenAI | 2026-09-04 |
| `gpt-6-astra-xhigh` | GPT-6 Astra (xhigh effort) | 43 | 1 | Codex CLI / OpenAI | 2026-09-04 |

Notes on the records:
- **"With fallback" matching:** AA plots every Claude configuration only "with fallback" (E214). The existing `claude-opus-5-5` record matches AA's "max with fallback" to the owner's "Opus 5.5 (max effort) - mean of 3", and the Sonnet 5.5 effort records follow the same convention. The new Opus records match "high/xhigh/medium with fallback" to the owner's "(high/xhigh/medium effort) - mean of 3" rows in the same way. The superseded single runs and means of two are listed in `excludedResults`.
- **Single runs:** the owner publishes only single runs for GPT-6 Luna low to xhigh, GPT-6 Astra high and xhigh, and GPT-5.6 Luna low. Each record says so.
- **Missing detail in the run notes:** the run-notes entries for GPT-6 Astra (high), GPT-6 Astra (xhigh) and GPT-5.6 Luna (low) carry only the result line, with no judge, route or caveat. Their route is recorded as for the family's max record ("OpenAI").
- No cross-harness result exists for any of the ten (E224).

## Leaves each new row lacks

Under the current ten-leaf set (FrontierCode, Terminal-Bench, Bug Hunt, GDPval, AutomationBench, Omniscience, AA-LCR, HLE, SciCode, CritPt; DeepSWE dropped under O49):

- **Complete on AA plus Bug Hunt:** the four GPT-6 Luna rows and the three Claude Opus 5.5 rows.
- **FrontierCode missing on AA:** `gpt-5.6-luna-low`, `gpt-6-astra-high` and `gpt-6-astra-xhigh`. Each has an exact-effort Cognition value, listed above, which still has to be registered in `data/leaf_evidence.json`.

## Files changed by this task

- `data/aa/aa_extract.json`: 10 entries added, each with an O51 note.
- `data/aa_mapping.json`: 10 rows added (`family`, `aaSlug`, `aaVariant`). The stale `gpt-6-astra-xhigh` URL was removed from the `gpt-6-astra` (max) row; that URL now belongs to its own row.
- `data/aa/aa_v432_snapshot.json`: 61 pages, `capturedAt` 2026-10-23T06:26:23Z.
- `data/aa_metrics.json`: 61 models, `observedAt` 2026-10-23T06:26:23Z.
- `data/v3_configuration_map.json`: 10 rows added.
- `data/bug_hunt.json`:
  - 10 model records.
  - 6 `excludedResults` entries (Opus 5.5 high, xhigh and medium: superseded single runs and means of two).
  - 1 `supplementalSourceCaptures` entry.
- `data/price_records.json`: `observedAt` set to the new snapshot instant.
- `research/2026-10-23-refresh/roster-expansion.md`: this file.

Unchanged on purpose:
- `data/aa_reconciliation_inventory.json` (see above).
- `data/aa/cost_charts_capture.json`: every pin used a label already captured.
- `data/coverage_matrix.json`: redirected to scratch.

## Follow-ups outside this task's file ownership

- **`data/leaf_evidence.json`:** add the three Cognition FrontierCode supplements listed above.
- **`valuerank/build_scores.py` `DEVELOPER` / `SHORT`:** add the ten display names.
- **`valuerank/exact_match.py` `TB4_BASE_NAMES`:** "Opus 5.5", "GPT-6 Luna", "GPT-6 Astra" and "GPT-5.6 Luna" name only one id each. The new effort ids need adding if tbench.ai is ever to fill a gap. AA's own Terminal-Bench run is present for all ten, so nothing is missing today.
- **`data/livebench.json`, `data/tb4.json` and `valuerank/fetch_livebench.py` `COHORT_MAP`:** these may need entries for the new ids, as for the two families added at the 05:38 refresh.
- **`gdpvalV21Normalized` is now null:** AA stopped publishing `gdpvalNormalized` (see the capture section above).
- **Release instant:** `aa_metrics.json` `observedAt` is now 2026-10-23T06:26:23Z, later than the refresh's `VALUERANK_NOW` of 2026-10-23T05:38:13Z. The release instant must be at or after this capture.
