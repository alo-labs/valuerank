# AA Intelligence Index frontier observation (2026-10-17T18:48:27Z)

Source: Artificial Analysis, "Intelligence Index vs. Cost to Run Artificial Analysis Intelligence Index" chart on the Intelligence Index v4.3.2 evaluation page (`https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index?eval-cost=intelligence-vs-total-cost`), all 694 catalog models selected ("694 of 694 models" in the selector). Observed in the built-in browser only; no embedded payload, API, export or paid data was used for this chart.

## Method

1. Selected "Intelligence Index vs. Total Cost" and "Select all" in the public chart.
2. Read the chart SVG: 189 circles with both coordinates, one Pareto path with 18 M/L vertices. Every vertex matched a circle centre exactly (distance 0 px).
3. Hovered every circle through ordinary mouse input and recorded its tooltip verbatim (`aa-chart-tooltips.json`: order, circle id, fill colour, SVG coordinates, tooltip text). Tooltips give the model name, the total cost in USD to two decimals and the Intelligence Index as a rounded integer.
4. One overlapped pair (circles 72 and 137, 0.1 px apart) returned the same tooltip at both centres. A hover 2 px to the left returned "GPT-5.5 (medium), $2,095.12, 34" verbatim. It was assigned to circle 72 because the log-scale x axis ($2k at 498.30 px, $3k at 531.25 px) places $2,095.12 at 502.08 px (circle 72: 502.07) and $2,097.29 at 502.17 px (circle 137: 502.16), and because circle 72 carries the OpenAI fill (#1f1f1f) and circle 137 the Zhipu fill (#1c7ff8) used by each provider's other points. Both points are dominated, so the resolution does not affect the frontier or the near-frontier set.
5. Claude Haiku 5.5 tooltips carry an asterisk footnote: "Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis." The footnote is recorded on each affected point and carried into the inventory as `sourceFootnote`.
6. AA model page slugs for frontier and near-frontier points were taken from AA's own catalog list embedded in a model page (`{slug, name, releaseSlug}` triples, 704 entries) by exact name match after case folding; every frontier and near-frontier point resolved. Ten dominated points (dated DeepSeek, Nemotron, Quasar and Claude Fable 5 variants with ambiguous catalog names) have no URL in the points list.

## Frontier (18 rendered vertices, 7 families)

| # | Configuration | Index | Total cost (USD) |
|---|---|---|---|
| 1 | GPT-6 Luna (low) | 22 | 10.63 |
| 2 | GPT-6 Luna (medium) | 30 | 31.17 |
| 3 | GPT-6 Luna (high) | 33 | 47.85 |
| 4 | Claude Haiku 5.5 (medium) | 34 | 56.36 |
| 5 | GPT-6 Luna (xhigh) | 35 | 66.81 |
| 6 | Claude Haiku 5.5 (high) | 38 | 94.07 |
| 7 | MiMo-V2.6-Flash | 38 | 109.55 |
| 8 | GPT-6 Luna (max) | 38 | 122.05 |
| 9 | Claude Haiku 5.5 (xhigh) | 41 | 157.58 |
| 10 | MiMo-V2.6-Pro | 46 | 206.66 |
| 11 | GPT-6.1 Sol (medium) | 48 | 361.37 |
| 12 | GPT-6.1 Sol (high) | 50 | 521.32 |
| 13 | GPT-6.1 Sol (xhigh) | 51 | 662.28 |
| 14 | GPT-6.1 Sol (max) | 52 | 1,081.55 |
| 15 | Claude Opus 5.5 (high with fallback) | 54 | 2,172.43 |
| 16 | Claude Opus 5.5 (xhigh with fallback) | 56 | 4,056.65 |
| 17 | Claude Sonnet 5.5 (max with fallback) | 56 | 7,259.50 |
| 18 | Claude Opus 5.5 (max with fallback) | 58 | 8,708.20 |

Three vertices (MiMo-V2.6-Flash, GPT-6 Luna (max), Claude Sonnet 5.5 (max with fallback)) tie at rounded precision with a cheaper frontier point; AA's line is drawn from full-precision values and is taken as observed, not recomputed.

Change since the 2026-10-07 observation (14 vertices): added Claude Haiku 5.5 (medium, high, xhigh) and Claude Sonnet 5.5 (max with fallback); nothing removed. Claude Haiku 5.5 was released on 2026-10-07, after the previous capture.

## Near-frontier policy and set

A plotted configuration is near-frontier when its public rounded Intelligence Index is within 3 points of the rendered frontier's intelligence at its cost (the highest frontier intelligence at or below that cost). A cost ratio alone was rejected because it admits models 13 to 17 Index points below the line at the cheap end (Gemma 4 E4B, Granite 4.2 3B, Ministral 3 3B). The cost ratio is reported for information.

| Configuration | Index | Total cost (USD) | Gap | Frontier reference |
|---|---|---|---|---|
| GPT-5.6 Luna (low) | 21 | 27.02 | 1 | GPT-6 Luna (low) |
| Claude Haiku 5.5 (low) | 29 | 34.31 | 1 | GPT-6 Luna (medium) |
| Claude Haiku 5.5 (max) | 43 | 330.25 | 3 | MiMo-V2.6-Pro |
| Claude Opus 5.5 (medium with fallback) | 51 | 1,626.81 | 1 | GPT-6.1 Sol (max) |
| Claude Sonnet 5.5 (xhigh with fallback) | 52 | 2,176.82 | 2 | Claude Opus 5.5 (high with fallback) |
| Gemini 4 Argon (high) | 53 | 2,407.24 | 1 | Claude Opus 5.5 (high with fallback) |
| GPT-6 Astra (high) | 51 | 2,925.01 | 3 | Claude Opus 5.5 (high with fallback) |
| GPT-6 Astra (xhigh) | 52 | 3,802.98 | 2 | Claude Opus 5.5 (high with fallback) |
| GPT-6 Astra (max) | 53 | 5,324.10 | 3 | Claude Opus 5.5 (xhigh with fallback) |

Tier counts over the 189 plotted points: 18 frontier, 9 near-frontier, 162 dominated.

## Roster decisions

- Frontier families absent from the v1.9.6 roster: Claude Haiku 5.5 and Claude Sonnet 5.5. Added with their selected frontier configurations: `claude-haiku-5-5` (xhigh, the family's highest-intelligence frontier configuration; max is not on the line) and `claude-sonnet-5-5` (max with fallback).
- Near-frontier families absent from the roster: Gemini 4 Argon. Added as `gemini-4-argon` (high, AA's page configuration; the API rejects higher efforts per the Bug Hunt owner's notes). GPT-6 Astra and GPT-5.6 Luna were already in the roster with their own selected configurations.
- Every non-selected frontier or near-frontier configuration has a dated defer decision in the inventory; no result is transferred between efforts.
- The three AA model pages previously captured by hand in the browser (MiMo-V2.6-Pro, MiMo-V2.6-Flash, GPT-6.1 Sol) now go through the automatic page capture, which decodes the slug-keyed payload object of each page after AA removed the `currentModel` marker from its markup on or before 2026-10-17.

## Supplementary benchmark coverage for the additions

- DeepSWE v1.1 (AA coding-agents chart): captured automatically from the page payload; 42 configurations including Claude Haiku 5.5 at five efforts, Claude Sonnet 5.5 (max) and Gemini 4 Argon (high). See `data/aa_deepswe.json`.
- Bug Hunt Bench: re-pinned to the owner's commit `aec976170df89a371384174ca87646a9a8c82415` (2026-10-17); see `bug-hunt-evidence.md`.
- Terminal-Bench 4.0: local leaderboard capture rebuilt; the Muse Spark 1.3 (xhigh) row has no published cost and is kept with a null cost.
- LiveBench: no release newer than 2026-06-25 exists (checked the LiveBench repository on 2026-10-17); the pinned release is unchanged.
