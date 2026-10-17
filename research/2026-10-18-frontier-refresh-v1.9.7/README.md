# Refresh record: ValueRank v1.9.7 (frontier and near-frontier inclusion)

Trigger: the owner asked that ValueRank include every model on Artificial Analysis' Intelligence Index versus total-cost Pareto frontier and, as far as possible, the near-Pareto models, noting that Claude Haiku 5.5 was missing.

## Findings

- The rendered AA frontier observed on 2026-10-17 has 18 vertices in 7 families (`aa-frontier-evidence.md`). Two frontier families were absent from the v1.9.6 roster: Claude Haiku 5.5 (released 2026-10-07, after the previous capture) and Claude Sonnet 5.5.
- A near-frontier rule was adopted: within 3 rounded Index points of the rendered line at the point's cost. It admits 9 configurations in 6 families; one family, Gemini 4 Argon, was absent from the roster. The cost-ratio criterion was rejected (see the evidence note).
- Artificial Analysis changed its model-page markup; the automatic page capture now decodes the payload object keyed by the page slug. The three pages previously read by hand in the browser (MiMo-V2.6-Pro, MiMo-V2.6-Flash, GPT-6.1 Sol) are now captured automatically at full precision.
- The DeepSWE v1.1 coding-agent chart is now captured from the coding-agents page payload (42 configurations, owner's full-precision mean reward) instead of a hand-read chart (31 rounded values).

## Roster and ranking changes

| Change | Models | Reason |
|---|---|---|
| Added | Claude Haiku 5.5 (xhigh), Claude Sonnet 5.5 (max with fallback), Gemini 4 Argon (high) | Frontier (Haiku, Sonnet) and near-frontier (Gemini) families |
| Newly ranked | the three additions, GPT-6 Astra, GPT-5.6 Luna | Overlap coverage, or forced inclusion as near-frontier families |
| Left the ranked cohort | Kimi K3, Grok 4.6 | Exact-variant DeepSWE mapping no longer holds: the chart row for Kimi K3 shows no effort (roster: max); Grok 4.6's chart row is xhigh (roster: medium). The previous hand-curated snapshot had mapped both; no result is transferred between efforts. |
| DeepSWE mapping gained | DeepSeek V4 Pro 0813 (max), DeepSeek V4 Flash 0731 (max) | The chart labels equal the roster's AA short names |
| DeepSWE mapping lost | GPT-6 Astra (chart max, roster xhigh) | Effort mismatch; the model remains ranked as a near-frontier family with the DeepSWE dimension missing |

Ranked cohort: 16 → 19 models. API-basis leader: Gemini 4 Argon (previously GPT-6.1 Sol).

## Source snapshots in this release

| Source | Observation | Note |
|---|---|---|
| AA Intelligence Index chart | 2026-10-17T18:48:27Z | 694 catalog, 189 plotted, 18 vertices, 9 near-frontier |
| AA model pages | 2026-10-17T19:25:14Z | 31 pages, slug-keyed payload decoder |
| AA DeepSWE v1.1 | 2026-10-17T19:26:26Z | 42 configurations, 16 exact mappings |
| Bug Hunt Bench | commit aec9761 (2026-10-17) | 31 entries, 25 matched (`bug-hunt-evidence.md`) |
| Terminal-Bench 4.0 | scrape 2026-10-17T19:17:55Z | 23 rows, one without a published cost |
| LiveBench | release 2026-06-25 (unchanged) | re-fetched 2026-10-17; the three additions post-date the release |

## Files

- `aa-frontier-evidence.md`: chart method, frontier and near-frontier tables, roster decisions.
- `aa-chart-tooltips.json`: all 189 tooltips as captured, with the overlapped-circle resolution.
- `bug-hunt-evidence.md`: per-model Bug Hunt matches, changes against the previous pin, raw file hashes.

## Addendum: v1.9.8 (same day)

- **Claude shared-plan routes (owner decision, Option 2).** The owner noted that Claude Haiku 5.5 is available on every Claude plan. The plan basis needs a measured API-priced allowance for the exact model; the selected SemiAnalysis source measures Opus 5.5 (Pro 58.9×, Max 5x 57.25×, Max 20x 58.63×) and Fable 5.1 (12.73× and 12.425× on the Max plans) only. Three options were put to the owner: a conservative shared assumption at the lower measured Claude figure, Opus 5.5's multiples for all Claude models, or keeping the API fallback. The owner chose Opus 5.5's multiples for all Claude models. Three routes (`claude-pro-common-opus55-assumption`, `claude-max5x-…`, `claude-max20x-…`) now apply them to Claude Opus 5, Fable 5, Opus 4.8, Sonnet 5, Haiku 5.5 and Sonnet 5.5, labelled `user_assumption` with the recorded caution that the Fable 5.1 measurement shows allowances are model-specific and that the applied figures may overstate cheaper models. Opus 5.5 keeps its exact measured routes. Plan-basis effect: Claude Sonnet 5.5 first (was Opus 5.5), Haiku 5.5 16th → 14th, Opus 5 14th → 9th; API-basis ranks unchanged.
- **Chart labels.** Model labels on every scatter chart now stay within 18 px of their own marker and no longer use leader lines; a Plotly vertical-shift sign error in the previous placement was corrected at the same time.
- **Ranking history** gains `v197` (the v1.9.7 API-basis ranks).
