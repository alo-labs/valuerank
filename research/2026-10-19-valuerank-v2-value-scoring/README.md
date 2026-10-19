# ValueRank v2.0.0 value-scoring record

- Decision date: 2026-10-19 (owner request)
- Source snapshots: unchanged from v1.9.8 (AA Intelligence Index v4.3.2 chart observed 2026-10-17T18:48:27Z; scores stamped 2026-10-17T20:23:57Z)
- Primary ranked cohort: unchanged, 19 AA frontier and near-frontier families
- Scope: scoring method only; no source capture, roster or evidence change

The owner restated ValueRank's objective: rank the AA Pareto and near-Pareto models by their actual value, where value is token efficiency (AA's total cost to run the AA Intelligence Index benchmarks) and, on the Plan basis, the API-equivalent usage a subscription delivers against its fee. A review of v1.9.8 against that objective found four gaps, and the owner asked for all of them to be addressed with cost weighted at 25% on both bases.

## Gaps in v1.9.8 and decisions

| Gap in v1.9.8 | v2.0.0 decision |
|---|---|
| The API basis compared raw AA total evaluation cost, so a cheap but weak model earned full cost credit; only the Plan basis divided by the Intelligence Index. | Both bases compare cost per AA Intelligence Index point. API: AA total evaluation cost ÷ Index. Plan: that ÷ highest eligible Value Multiple (unchanged). |
| "Token efficiency" mixed tokens spent with per-token price. | Kept by definition: the owner defines token efficiency as AA's total benchmark cost (tokens × price). Documented in the publication; token counts are not scored separately. |
| Cost was rank-normalized, so a 1.1× and a 10× cost gap could count the same, though costs across the frontier span about 50×. | Cost is scored on a log scale within the ranked cohort: 100 × (ln c_max − ln c) / (ln c_max − ln c_min). Quality dimensions stay rank-normalized. |
| Cost carried 18.94% nominally, and more for rows missing quality metrics, because all priorities were renormalized together. | Cost carries a fixed 25% of every overall score on both bases (`COST_WEIGHT_PCT`); quality dimensions share the other 75% by their unchanged priorities, renormalized per row over available quality metrics. A row without a cost is scored on quality alone. |

The Bug Hunt emphasis view applies the same rule: cost per Index point on the log scale at a fixed 25%, with Bug Hunt's priority 30 inside the 75% quality share.

Overall-score ties now break by lower cost on the basis, then name, on the site as well as in `scores.json`.

## Effect on the ranking

API-basis ranks move little because quality still carries 75%: Gemini 4 Argon, GPT-6.1 Sol and Claude Sonnet 5.5 remain the top three. Several token-efficient models rise (MiMo-V2.6-Pro 9→7, GPT-6 Luna 13→11, Claude Haiku 5.5 16→13). MiMo-V2.6-Flash, the cheapest per point, still falls 10→12: rank scoring had already given it the top cost score, and its low quality now weighs 75%. Among expensive models Claude Opus 5 falls 14→15, while Claude Opus 5.5 moves 6→5 past GPT-5.6 Sol. Both now lose more to cost, but GPT-5.6 Sol loses more: its cost score drops from 33.3 to 18.1 on the log scale (73.76 USD per point is closer, as a ratio, to the dearest model than to the cheapest), so its overall falls to 56.8 against Opus 5.5's 57.5. v2.0.0 scores are not numerically comparable with earlier releases.

## Reproduction

The source snapshots are unchanged, so the release is rebuilt from them with the original observation instant:

```sh
export VALUERANK_NOW=2026-10-17T20:23:57Z
python3 -m valuerank.build_scores
python3 -m valuerank.aa_reconciliation
npm run build:publication
npm run verify
```
