# Decision record: O71 stage 3 (AF-DECIDE rollup), GPT-6.1 Terra and Gemini 4 Carbon

## Decision
| Cell | O11 verdict | Value |
|---|---|---|
| GPT-6.1 Terra × ChatGPT Plus × 5h | **Met** (three independent qualifying reports) | ≈$5.3–6.1 API-$ per 5h. Bounds [5.28, 5.51], [5.33, 5.33], [6.06, 6.15]. Test: 6.06 ≤ 1.20 × 5.33 = 6.40. Not convertible to a billing period (O82). |
| GPT-6.1 Terra × Plus × week (→ month) | Not met | 0 qualifying (derived, mixed or unbased candidates only) |
| GPT-6.1 Terra × Pro $100 × week, before / after 2026-10-29 | Not met / Not met | 0 / 0 |
| GPT-6.1 Terra × Pro $200 × week, before / after | Not met / Not met | 0 / 0 |
| GPT-6.1 Terra × Pro $500 × week, before / after | Not met / Not met | 0 / 0 |
| GPT-6.1 Terra × Pro (any) × 5h | n/a | Pro has no 5h window |
| Gemini 4 Carbon × AI Plus / AI Pro / AI Ultra × any unit | Not met | Not available on any consumer plan at 2026-10-31T04:10Z; 0 reports |

## What changed from stages 1–2
1. **A new qualifying report.** SouthWindKnows (LINUX DO, read through the locdd mirror), Plus, 2026-10-27 03:19 UTC: 57.54M tokens priced at $4.70 at 77% of the 5h window, which is $6.06–6.15 per 5h. It is concordant with pensuke89 (747k against 768k tokens per point) [3].
2. **The discrepancy is mostly settled.** Five observers give a same-account Terra/Sol token ratio of 1.25–1.53, against the 2× implied by the provider. Once normalised, the #56866 readings imply $5.1–6.2 per 5h, which is consistent with the priced cluster. One pre-update CLI reading (dennisvoss1978, ratio 0.52) remains unexplained. It is compatible with an unverified report that the CLI bills Terra as Sol.
3. **Weekly and Pro.** New candidates exist: Fei2411 #149 (Pro $200, model unstated), Theo's chart (Terra values unreachable), a SouthWindKnows week (mixed), DreamRiver (no basis), and meter-only posts. None qualifies.
4. **Carbon.** Unavailability is reconfirmed through the cutoff from primary changelogs (API to 10-30, Antigravity to 10-29, app notes to 10-13) and from a user report on 10-31 at 02:51 UTC. A contrary news claim (El-Balad) is rejected as unsourced.

## Alternatives considered
- **Disqualify SouthWindKnows as tool-priced, as stage 2 did with ayudha90.** Rejected. Tokens, the cache share and the meter fraction are all shown, and the dollar figure is feasible at list prices. ayudha90 showed no tokens. Even if it were disqualified, the cell would still pass on the stage-1 pair.
- **Read the SouthWindKnows window at 73%.** That would give $6.44, which fails the margin. Rejected as the primary reading, because 77% is the meter's own used fraction and the token count covers the whole window. Disclosed as a sensitivity.
- **Treat el-rocho as an eligible upper/lower bound.** Rejected. He gives no split and his tier is carried over (provisional). He is shown in the range test only.

## Evidence summary
- 39 sources (34 web, 5 local) and 67 evidence spans.
- Average reliability C–D. User reports dominate. Primary sources are used only for Carbon availability and partition events.
- Claim verification: 0 unsupported factual claims in strict mode.

## Tradeoffs and risks
- All admitting Plus 5h readings are from launch week (10-26..28).
- The Plus 5h margin headroom is 5% (6.06 against 6.40) on the third report.
- Speed mode is unstated by all reporters.
- OpenAI has made no statement about Terra metering.

## Confidence and remaining gaps
- **Plus 5h pass: medium-high.**
- **Weekly and Pro: a well-searched negative**, though X and YouTube remain unreachable.
- **Carbon unavailability: high.**
- Remaining gaps: Terra-only full-week measurements, any Pro measurement in either partition, and a CLI-versus-app A/B.

## Downstream handoff
`silver-ensure-docs` (record the verdicts in the ValueRank decision log; this run edits no file outside its folder) → `silver-validate`. See handoff.md.
