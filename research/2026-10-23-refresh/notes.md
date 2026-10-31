# Source refresh 2026-10-23 (owner decision O47)

On 2026-10-23 the owner moved the release cutoff from 2026-10-21T05:24:16Z to this refresh (O47) and asked for every Artificial Analysis (AA) source and the other benchmark sources to be captured again.

**Capture instant (new `VALUERANK_NOW`): `2026-10-23T05:38:13Z`.** This is when the last capture finished (the DeepSWE primary leaderboard render). `data/aa_metrics.json` carries this instant as `observedAt`.

All web content was treated as data. No sign-in, cookie, paid export or private API was used.

## What was captured, when and how

| Source | URL | Method | Finished (UTC) | Written to |
|---|---|---|---|---|
| AA Intelligence Index vs. Cost to Run chart | https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index?eval-cost=intelligence-vs-total-cost | Playwright, headless Chromium (repo `playwright` 1.62.0, browsers in `/opt/pw-browsers`), 1600 x 1200 viewport. Model selector set to Select all (697 of 697). Read every circle and the dotted Pareto path from the SVG, then hovered each circle centre once (189 hovers, 189 distinct tooltips). | 05:27:39 | `data/aa_frontier_capture.json`, `data/aa_reconciliation_inventory.json`, `aa-chart-tooltips.json` |
| AA catalog (slug, name, releaseSlug; 707 entries) | embedded in https://artificialanalysis.ai/models/gpt-6-luna-low | HTTPS (curl) | 05:27:58 | used only to resolve owner URLs |
| AA model pages (51) | https://artificialanalysis.ai/models/... | `npm run capture:aa`, which writes only the snapshot | 05:30:42 | `data/aa/aa_v432_snapshot.json` |
| AA metrics | built from the snapshot | `valuerank.build_aa_metrics` run through a wrapper that sends its second output, `coverage_matrix.json`, to scratch so that file is not touched. `VALUERANK_NOW=2026-10-23T05:38:13Z`. | n/a | `data/aa_metrics.json` |
| AA Coding Agents page | https://artificialanalysis.ai/agents/coding-agents | HTTPS, parsed with `valuerank.capture_coding_agents.capture_document`; page also rendered with Playwright | 05:31:41 | evidence only: `coding-agents-v2.0-capture-2026-10-23.json` (see Finding 1) |
| AA Coding Agent methodology | https://artificialanalysis.ai/methodology/coding-agents-benchmarking | Playwright render | 05:32:56 | `coding-agents-methodology-version-history-2026-10-23.txt` |
| AA FrontierCode and ITBench-AA "Total Cost to Run" charts | https://artificialanalysis.ai/evaluations/frontiercode, https://artificialanalysis.ai/evaluations/itbench-aa | Playwright. The run imports the exported functions of `scripts/capture-aa-cost-charts.js` (tab click, chart read, `parseChartRows`) and adds one step: Select all in the chart's model selector (FrontierCode 67 of 67 models, 62 bars; ITBench-AA 45 of 45, 42 bars). The script's own default-view run (05:33:53; 29 and 15 bars) is kept for comparison. | 05:35:10 | `data/aa/cost_charts_capture.json`; `cost-charts-default-view-2026-10-23.json` |
| Terminal-Bench 4.0 (tbench.ai) | https://www.tbench.ai/leaderboard/terminal-bench/4.0 | `npm run capture:tb4`, then `python3 -m valuerank.build_tb4 data/tb4-scrape.json data/tb4.json` | 05:35:48 | `data/tb4-scrape.json`, `data/tb4.json` |
| Cognition FrontierCode | https://cognition.com/data/frontiercode-leaderboard/data.json | HTTPS (curl) | 05:36:49 | unchanged (byte-identical; see below) |
| Bug Hunt Bench | https://github.com/phuryn/bug-hunt-bench (main = `46802fc312b6fd467b0baee519df05693f120232`, 2026-10-19T12:02:52+02:00); https://bughunt.productcompass.pm/data/benchmark.json (updated 2026-10-19) | `git ls-remote` and a blob-less `git clone` over HTTPS; site data over HTTPS | 05:37:06 (clone), 05:37:28 (site) | `data/bug_hunt_scoreboard.json`, `data/bug_hunt.json` |
| DeepSWE primary leaderboard | https://deepswe.datacurve.ai/ | Playwright render | 05:38:13 | evidence only: `deepswe-datacurve-leaderboard-2026-10-23.txt` |
| LiveBench (pinned release 2026_06_25) | https://raw.githubusercontent.com/LiveBench/new-livebench/7be9f746.../public/... | `valuerank.fetch_livebench` | failed | not re-fetched (see Finding 4) |

## Finding 1: AA dropped DeepSWE from the Coding Agent Index (v2.0)

AA's Coding Agents page now shows **Coding Agent Index v2.0**, described as "the equal-weight average of FrontierCode v1.1, Terminal-Bench 4.0 and SWE-Atlas-QnA-AA". The methodology page's version history reads: "Version 2.0, October 2026 - current: Replaced DeepSWE v1.1 with FrontierCode v1.1 from Cognition …; Renamed SWE-Atlas-QnA to SWE-Atlas-QnA-AA with adjustments to Scale AI's grading". The version history is quoted verbatim in `coding-agents-methodology-version-history-2026-10-23.txt`.

- **DeepSWE v1.1 is gone from AA.** The page payload has no `DeepSWE v1.1` evaluation (`evaluationDatasetSlug` values are only `FrontierCode v1.1 Main`, `SWE-Atlas-QnA` and `Terminal-Bench v4`). `npm run capture:deepswe` therefore fails with "the page payload has no configuration with a DeepSWE v1.1 evaluation", and `/evaluations/deepswe` returns 404. **`data/aa_deepswe.json` is unchanged: it is still the 2026-10-17T19:26:26Z capture, now the last AA publication of DeepSWE v1.1.**
- **DeepSWE's own leaderboard** (deepswe.datacurve.ai) still says "113 tasks · updated September 22, 2026" with the same 21 Best rows as `data/deepswe.json` (2026-09-29). It has no row for either new family. `data/deepswe.json` and `data/deepswe-scrape.json` are unchanged; `data/deepswe.json` is also a test golden.
- **The Coding Agent Index cost component.** v2.0 lists 24 configurations (v1.5 had 42) priced over 290 tasks (FrontierCode 100, Terminal-Bench 66, SWE-Atlas-QnA-AA 124). `valuerank/basket.py` prices the v1.5 composition: `CODING_AGENT_TASKS = {deep-swe-v1.1: 113, swe-atlas-qna: 124, terminal-bench-v4: 66}` × the mean cost per task. v2.0 also includes FrontierCode, which the basket already counts as a separate chart component. **`data/aa/coding_agents_capture.json` is therefore left as the v1.5 capture of 2026-10-19T19:31:46Z.** The v2.0 capture is stored as evidence only (`coding-agents-v2.0-capture-2026-10-23.json`, response sha256 `b3388f6a…c3760`).
- The owner or editor has to decide whether the DeepSWE leaf may keep reading the 2026-10-17 capture, and how the basket treats Coding Agent Index v2.0. Both are outside capture scope.

## Finding 2: Frontier and near-frontier

The rendered Pareto path is **unchanged**: 18 vertices, the same circle ids, tooltips and SVG y coordinates as on 2026-10-17. The x coordinates differ only because the viewport is wider. Universe: 697 catalog models (was 694), 189 plotted points, 18 vertices in 7 families.

Frontier families (all in the roster): GPT-6 Luna (5 vertices), Claude Haiku 5.5 (medium, high, xhigh), MiMo-V2.6-Flash, MiMo-V2.6-Pro, GPT-6.1 Sol (medium, high, xhigh, max), Claude Opus 5.5 (high, xhigh, max with fallback), Claude Sonnet 5.5 (max with fallback).

The near-frontier set uses the rendered line, within 3 Index points, and grows from 9 to 11 configurations:

| Configuration | Index | Cost (USD) | Gap | Frontier reference | Roster |
|---|---|---|---|---|---|
| GPT-5.6 Luna (low) | 21 | 27.02 | 1 | GPT-6 Luna (low) | yes (gpt-5.6-luna) |
| Claude Haiku 5.5 (low) | 29 | 34.31 | 1 | GPT-6 Luna (medium) | yes |
| **MiniMax-M3.1-Flash** | 43 | 283.18 | 3 | MiMo-V2.6-Pro | **added 2026-10-23** |
| Claude Haiku 5.5 (max) | 43 | 330.25 | 3 | MiMo-V2.6-Pro | yes |
| **DeepSeek V4.1 Flash 1017 (max)** | 45 | 444.60 | 3 | GPT-6.1 Sol (medium) | **added 2026-10-23** |
| Claude Opus 5.5 (medium with fallback) | 51 | 1,626.81 | 1 | GPT-6.1 Sol (max) | yes |
| Claude Sonnet 5.5 (xhigh with fallback) | 52 | 2,176.82 | 2 | Claude Opus 5.5 (high with fallback) | yes |
| Gemini 4 Argon (high) | 53 | 2,407.24 | 1 | Claude Opus 5.5 (high with fallback) | yes |
| GPT-6 Astra (high) | 51 | 2,925.01 | 3 | Claude Opus 5.5 (high with fallback) | yes (family) |
| GPT-6 Astra (xhigh) | 52 | 3,802.98 | 2 | Claude Opus 5.5 (high with fallback) | yes (family) |
| GPT-6 Astra (max) | 53 | 5,324.10 | 3 | Claude Opus 5.5 (xhigh with fallback) | yes |

The two new families are clearly required by AGENTS.md: each sits exactly 3 points below the rendered line, and neither has an owner deferral. Both are AA's only configuration of their model, were released after the previous capture (2026-10-17 and 2026-10-19) and first appear on the chart now. They were added to `data/aa/aa_extract.json`, `data/aa_mapping.json` and the inventory (`requiredFamilyModelId` `deepseek-v4-1-flash-1017` and `minimax-m3-1-flash`).

`python3 -m valuerank.frontier research/2026-10-23-refresh/aa-chart-tooltips.json --roster data/aa_mapping.json` reports every family as `in_roster: true` (`frontier-cli-report.json`). The CLI recomputes a frontier from rounded values (15 frontier and 14 near points), so its tiers are diagnostic. Membership above is AA's rendered line.

Other chart changes since 2026-10-17:
- Points added: DeepSeek V4.1 Flash 1017 (max), MiniMax-M3.1-Flash, Ling 3.1 Flash 1019 (44, USD 1,551.81, dominated).
- Points removed: Gemini 3.7 Flash (high), Qwen3 30B A3B 2507, Quasar 438B (max).
- Cost changes, all on dominated points:
  - DeepSeek V4 Flash 0731 (max) 474.19 → 199.63 (roster `deepseek-v4-flash`)
  - DeepSeek V4.1 Flash (max) 476.89 → 599.70
  - DeepSeek V4 Flash Vision (max) 445.41 → 1,081.42
  - DeepSeek V4.1 Flash (non-reasoning) 155.52 → 238.91
  - Beam 1.0 739.78 → 318.73
  - Nemotron 3 Ultra 801.45 → 696.84
  - Nemotron 3.5 Lightning 105.48 → 92.76
  - gpt-oss-120b (high) 110.26 → 122.71
  - gpt-oss-20b (high) 30.48 → 36.29
  - Muse Spark Open (xhigh) 1,183.43 → 1,184.90
  - Ling 3.1 Flash 990.44 → 995.11
- No public Index value changed.

The inventory's 18 roster decisions ("alternate configuration retained; family represented by its selected configuration") were re-reviewed against this capture and re-dated `2026-10-23T05:41:55Z`. Their reasons are unchanged.

## Finding 3: Leaves (AA model pages, Cognition, Bug Hunt, Terminal-Bench)

**AA Intelligence Index values are unchanged for every roster configuration.** AA re-estimated the GDPval-AA and AA-Briefcase Elos: GDPval moved by −0.3 to −3.3 Elo for every roster model except Claude Opus 5.5, Claude Sonnet 5.5, Muse Spark 1.3 (max and xhigh), Muse Wonder, Muse Wonder Full, GLM-5.3 Flash and Gemini 3.7 Flash, which are unchanged.

FrontierCode 1.1 (AA field `frontierCode`) newly published on AA model pages:

| Configuration | Before (2026-10-17 snapshot) | Now (AA) | Effect on the leaf |
|---|---|---|---|
| Muse Wonder (max) | missing (listed, O38) | 46.47% (0.464713) | **gap filled**; its leaf search is moot |
| Muse Spark 1.3 (xhigh) | missing (listed, O38) | 38.63% (0.386338) | **gap filled**; its leaf search is moot |
| Muse Wonder Full (max) | aa_recapture supplement 44.89% | 44.89% (primary) | same value, now primary |
| DeepSeek V4 Pro 0813 (max) | aa_recapture supplement 38.80% | 38.80% (primary) | same value, now primary |
| GPT-6.1 Sol (xhigh) | Cognition supplement 49.29% | AA 46.29% | **changes** (AA takes precedence, O37) |
| GPT-6.1 Sol (high) | Cognition supplement 47.98% | AA 46.61% | **changes** |
| GPT-6.1 Sol (medium) | Cognition supplement 50.23% | AA 43.33% | **changes** |
| GPT-6.1 Sol (low) | Cognition supplement 45.46% | AA 36.68% | **changes** |

The leaf supplements in `data/leaf_evidence.json` are left in place. `valuerank/value_v3.py` applies a supplement only when the page lacks the leaf, so these entries are now inert.

Leaves still missing (registered sources re-checked at this capture):
- **Grok 4.6 (xhigh), FrontierCode:** AA `frontierCode` is null. Cognition lists only low, medium and high.
- **DeepSeek V4 Flash 0731 (max), FrontierCode:** AA null. Cognition lists V4 Flash 0731 at high only.
- **MiMo-V2.6-Flash, Bug Hunt:** the owner still publishes only "MiMo-V2.6-Flash - mean of 3" (default effort, reasoning state not asserted). No new MiMo row at 46802fc.

All three searches in `leaf_evidence.json` (dated 2026-10-21, open-web steps 2026-10-23) are within 7 days of the new cutoff. They were not edited.

Cognition FrontierCode `data.json`: Last-Modified is now 2026-10-22T22:28:12Z, but the body is byte-identical to the 2026-10-21 capture (sha256 `ff0040778b7bdf69c705ad7474f771fb5e53cfaf5cf8573b3a4614153543d75f`, 46 models, no Muse model, no Grok 4.6 xhigh). `data/cognition_frontiercode.json` is unchanged. `leaf_evidence.json` `cognitionCapture` now reads lastModified 2026-10-22T22:28:12Z and capturedOn 2026-10-23; the sha256 is unchanged.

Bug Hunt Bench: re-pinned from aec9761 (2026-10-17) to `46802fc` (2026-10-19).
- The scoreboard grows from 192 to 202 rows. All ten new rows are DeepSeek V4.1 Flash 1017 (Claude Code mean of 7 at max; DeepSeek Harness, Pi and OpenCode at max, high and low). No existing row changed.
- New sha256: combined-scoreboard.csv `1636e4e08269a5d9b57214438f030374fb2b127cfe88cbb100734ac0195f490b`; run-notes.md `f4d4078f288780d0dac38021a548e71f914ed056546873ca441c14cdf9bccce2`.
- Every existing matched record was re-verified at the new commit: same value, and its run-notes anchor still exists. Those records keep their aec9761 provenance.

Terminal-Bench 4.0 (tbench.ai): the same 23 rows. The only change is GLM-5.3-Flash (none) / Claude Code, whose cost label changed from $2.9k to $0.1k; that row is not mapped to the roster. `cohortN` is now 51. No roster leaf changed. AA's own Terminal-Bench run, which is the leaf, is unchanged for every roster model.

## New families: evidence at capture

| | DeepSeek V4.1 Flash 1017 (max) | MiniMax-M3.1-Flash |
|---|---|---|
| AA slug / release | `deepseek-v4-1-flash-1017`, released 2026-10-17 | `minimax-m3-1-flash`, released 2026-10-19 (reasoning) |
| Index / Index cost | 45.10 / USD 444.60 | 42.71 / USD 283.18 |
| Price (USD per 1M tokens, input/output) | 0.30 / 1.20 | 0.15 / 0.60 |
| AA leaves | all nine AA leaves present; FrontierCode 43.66%, Terminal-Bench 33.84% | all nine AA leaves present; FrontierCode 38.58%, Terminal-Bench 25.76% |
| DeepSWE v1.1 | **missing** (AA withdrew DeepSWE; DeepSWE's own board has no row) | **missing** |
| Bug Hunt | 42.7 / 105, "DeepSeek V4.1 Flash 1017 (max effort, DeepSeek Harness) - mean of 7" (editor's selection, see below) | **missing**: no MiniMax row in the scoreboard, run notes or site data |
| FrontierCode cost chart | USD 35 | USD 35 |
| Coding Agent Index v1.5 cost | none (not in the v1.5 capture) | none |
| LiveBench | none (released after the pinned release) | none |

Bug Hunt selection for DeepSeek V4.1 Flash 1017: the owner publishes two featured means of seven runs at max effort, DeepSeek Harness 42.7 and Claude Code 39.1.
- The DeepSeek Harness row is selected, with a `selectionReason`. It is DeepSeek's own agent, which matches the benchmark's native-CLI method, and AA's Coding Agent Index v2.0 also uses DeepSeek Harness for this model.
- The Claude Code row (39.1), Pi (42.2, mean of 5) and OpenCode (37.6, mean of 5) are kept as unselected owner configurations.
- **This choice is for owner review.**

Both new families lack DeepSWE, and MiniMax also lacks Bug Hunt. Under O36 and O38 they will be listed, not ranked, unless a registered source fills the gap. The build requires an exhaustive search for each missing leaf, logged in `leaf_evidence.json` with its open-web step. **That search has not been done in this capture** and is still outstanding:
- deepseek-v4-1-flash-1017 / deepswe
- minimax-m3-1-flash / deepswe
- minimax-m3-1-flash / bugHunt

## Costs and prices for roster configurations

- **DeepSeek V4 Flash 0731 (max)** (`deepseek-v4-flash`): AA prices fell from 0.44/1.32 to 0.14/0.28 USD per 1M tokens (cache hit 0.014 → 0.023). Index cost fell from USD 474.19 to USD 199.63, and every per-evaluation cost in the SDLC basket changed with it. AA's cost reconciles with the displayed prices (valuation gate "compatible as captured").
- **Gemini 3.7 Flash:** AA removed every price, and its (high) point left the chart. Its Index cost was already missing. Its valuation gate now reads "valuation basis unverified".
- No other roster configuration's Index cost or price changed.
- **FrontierCode cost chart:** every label captured on 2026-10-19 is unchanged. Selecting all models exposes exact labels for more roster configurations, now pinned in `data/v3_configuration_map.json`:
  - GPT-6.1 Sol: xhigh $60, high $42, medium $19, low $8
  - Claude Haiku 5.5: high $8\*, medium $4\*, low $2\*
  - Claude Sonnet 5.5 (with fallback): high $30, medium $16, low $13
  - MiMo-V2.6-Flash $8
  - Muse Spark 1.3: max $281, xhigh $236
  - Muse Wonder (max) $503
  - DeepSeek V4 Pro 0813 (max) $117
  - DeepSeek V4.1 Flash 1017 (max) $35
  - MiniMax-M3.1-Flash $35
- **ITBench-AA cost chart:** new pins for Muse Spark 1.3 (max) $85 and GPT-5.6 Luna (max) $12. The only changed label is DeepSeek V4.1 Flash (max), $26 → $22, which is not in the roster.
- Labels marked "\*" are AA's declined-tasks marker.
- Ambiguous chart names that do not carry AA's dated version were not pinned: "DeepSeek V4 Flash (max)" and "DeepSeek V4 Pro (max)" on ITBench.
- `data/price_records.json`: observedAt now 2026-10-23T05:30:42Z (the page snapshot); records remain empty.

## Files changed in this refresh

- `data/aa/aa_extract.json`, `data/aa_mapping.json`: two near-frontier families added.
- `data/aa/aa_v432_snapshot.json`: 51 pages, capturedAt 2026-10-23T05:30:42Z.
- `data/aa_metrics.json`: 51 models, observedAt 2026-10-23T05:38:13Z.
- `data/aa_frontier_capture.json`, `data/aa_reconciliation_inventory.json`: 2026-10-23T05:27:39Z observation; 18 frontier rows; 11 near-frontier rows.
- `data/aa/cost_charts_capture.json`: all-model capture, 2026-10-23T05:35:10Z.
- `data/v3_configuration_map.json`: observedAt 2026-10-23; pins listed above; rows added for the two new families.
- `data/tb4-scrape.json`, `data/tb4.json`: 2026-10-23T05:35:48Z.
- `data/livebench.json`: unmatched rows for the two new families. The pinned release could not be re-fetched, so `observedAt` stays 2026-10-17.
- `data/bug_hunt_scoreboard.json`, `data/bug_hunt.json`: re-pinned to 46802fc; DeepSeek V4.1 Flash 1017 and MiniMax-M3.1-Flash records added.
- `data/leaf_evidence.json`: `observedAt` 2026-10-23 and `cognitionCapture` dates only. The searches and their open-web blocks written by the other agent are preserved.
- `data/price_records.json`: `observedAt`.

Unchanged on purpose:
- `data/aa/coding_agents_capture.json` (Finding 1)
- `data/aa_deepswe.json` (Finding 1)
- `data/deepswe.json` and `data/deepswe-scrape.json` (no change at the source)
- `data/cognition_frontiercode.json` (byte-identical at the source)

## Finding 4: captures that could not run as scripted (code follow-ups for the code owner)

- `npm run capture:deepswe` (`valuerank/fetch_deepswe.py`) fails because AA no longer publishes DeepSWE (Finding 1).
- `npm run capture:basket`:
  - `capture_coding_agents` would overwrite the v1.5 capture with v2.0 rows that `basket.py` would misprice, so it was not run into `data/`.
  - `scripts/capture-aa-cost-charts.js` captures only the chart's default model selection (29 of 67 FrontierCode bars). It should select all models.
- `valuerank/fetch_livebench.py`:
  - Its hard-coded `COHORT_MAP` must gain `deepseek-v4-1-flash-1017` and `minimax-m3-1-flash` (both `None`).
  - Separately, the pinned raw URLs (`raw.githubusercontent.com/LiveBench/new-livebench/7be9f746…`) return HTTP 404, and github.com returns 403 through this session's proxy. The repository may be private or renamed; this was not established.
- `npm run build:aa` was not run as-is because `build_aa_metrics` also writes `data/coverage_matrix.json`, which belongs to the score build.
- `valuerank/basket.py` hard-codes Coding Agent Index v1.5 task counts.

## Scratch tools used (not committed)

- A wrapper that runs `valuerank.build_aa_metrics` with outputs redirected.
- A wrapper that runs `valuerank.fetch_livebench` with the two new ids added to `COHORT_MAP`. It failed on the 404.
- The Playwright chart capture and the all-models cost-chart capture.

They live in the session scratchpad. No repository code was modified.
