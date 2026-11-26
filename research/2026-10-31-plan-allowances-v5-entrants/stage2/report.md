# O71 stage 2 (Claude's Deep Research): GPT-6.1 Terra and Gemini 4 Carbon plan allowances, 2026-10-31

Release cutoff 2026-10-31T04:10:00Z; report window 2026-10-01..2026-10-31. Usable Terra window 2026-10-26..cutoff.
This stage extends `../stage1-openai-terra.md` and `../stage1-google-carbon.md`. Notes are in `research_notes/`:
`openai-terra.md`, `google-carbon.md` and `queries-and-sources.md`. Prices per 1M tokens: Terra $1.00 input /
$0.05 cached / $5.00 output. The deep-research skill's subagent tool was unavailable in this session, so the
research was run directly (skill fallback).

## Summary
- **Terra: Plus, 5h.** O11 is still **met** on stage 1's two admitting reports (pensuke89 $5.28–5.51 and
  IndividualPlus2011 $5.33 per 5h). Stage 2 adds one new priced candidate, ayudha90 ($2.60–14.8 per 5h). It does not
  qualify: the pricing basis is undisclosed and there is no token split. It would not break the range test even if
  admitted.
- **Terra: Plus weekly, and every Pro tier (weekly, before or after 2026-10-29).** No priceable report exists, so
  O11 is not met. The only new readings are meter-only: two Plus weekly anecdotes and a few Pro anecdotes.
- **Metering discrepancy.** No new evidence settles it. Most of the GitHub readings are compatible in dollars once
  their unknown cache share is allowed for. dennisvoss1978's pre-update CLI reading is the true outlier. A user
  reports that headless-CLI Terra usage is billed as Sol (2×); this is unverified.
- **Gemini 4 Carbon.** Confirmed **not available on any Google consumer plan** (AI Plus, AI Pro, AI Ultra; Gemini
  app, Antigravity) as of the cutoff. There are 0 reports.

## Candidate reports: GPT-6.1 Terra
"Q" = qualifies under the eligibility profile (O71 v1). Items S1–S6 are from stage 1, carried over unchanged;
N1 is new in stage 2.

| # | Plan | Unit | Effort | Observer | URL | Date (UTC) | Token split | Meter movement | $ at list | Q? | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | Plus (stated) | 5h | unstated | pensuke89 | reddit.com/r/codex/comments/1xgcwoq (comments 19rpkdemtj84g, 19rq2uvffez8h) | 10-26 23:37 – 10-27 08:57 | 43,758,336 cached / 748,338 uncached / 45,459 output | 58% of 5h (also 27% earlier) | $5.28–5.51 per 5h | **Yes** | exact model, stated tier, one model, priced split, before Day 23 reset and before the 10-27 17:23 UTC shift |
| S2 | Plus (stated) | 5h | xhigh | IndividualPlus2011 | reddit.com/r/codex/comments/1xhhrxs | 10-28 07:44 | not published | own measurement (method stated, raw readings not shown) | $5.33 per 5h | **Yes** | observer's own measurement, stated tier and model; postdates the Day 23 reset (does not span it) |
| S2w | Plus | week | xhigh | IndividualPlus2011 | same | 10-28 | — | derived (6 × 5h) | $32 per week | No | derived figure; the author confirms "it only includes regular usage" (19rttnkpclvj9) |
| S1w | Plus | week | — | pensuke89 | 1xgcwoq 19rpkdemtj84g | 10-27 | — | not shown | $34.33 per week | No | basis not shown; later says it is computed from the 5h figure and IndividualPlus2011's (19rsujitn7rad) |
| S3 | Plus (carried; provisional) | 5h | medium | el-rocho | github.com/openai/codex/issues/56866 | 10-28 | ≈5.14M tokens, "heavily cached", no split | 40→56% (+16pp) | $1.8–7.8 per 5h | No (provisional in range test) | no split; tier carried over from an earlier comment |
| S4 | Plus | 5h | xhigh | dennisvoss1978 | openai/codex #56866 | 10-27 | input only (1.91M; 1.92M), no cached or output split | 9→19%; after the update 22→26% | before $1.0–2.8, after $2.5–6.9 (plus output) | No | no split or output; CLI session files (see discrepancy) |
| S5 | "Pro Plan" (tier unstated) | 5h (doubtful) | mixed | Emotional-Cut2952 | r/codex 1xhx3ab | 10-28 | full split for 3 models | 90% | ≈$5.9 per 5h at plan level | No | three models; tier unstated; Pro has no 5h window |
| S6 | Plus | 5h / week | high | HoshiEstrellas | openai/codex #57627 | 10-28 | 0 tokens | 5h shows 0% remaining | — | No | accounting anomaly |
| **N1** | **Plus (stated: "GPT 6.1 Terra on GPT Plus"; "5hr in plus")** | **5h** | xhigh; max | **ayudha90** | reddit.com/r/codex/comments/1xgcjjb (19rq3j8qxks1t, 19rq3tppay6ma); reddit.com/r/codex/comments/1xgriu5 (19rsetm8ka18g) | 10-27 09:12 – 12:44 | none; author's $ only ($0.091; $0.074; $0.282) | xhigh 3%; xhigh 1%; max 4% | points $3.03 / $7.40 / $7.05; with ±0.5pp rounding **$2.60–14.8 per 5h** | **No** | dollar figures are the author's with no stated pricing basis and no tokens, so API pricing can't be verified (rule 1); deltas of 1–4% are coarse |

New meter-only context (not candidates: no tokens or dollars):
- Plus weekly:
  - SlipperyBandicoot (r/codex 1xhgnnp, 10-28, Terra medium): 16% of weekly plus the whole 5h window in about 2 h.
  - facciocosevedogente3 (r/ChatGPTCoding 1xhl958, 10-28, Terra High): 70% of weekly on one migration.
  - psamytron (1xjjzut, 10-30): mixed models.
- Plus 5h: jimmym007 (10-28), TheMythicSorcerer (10-30), nickmullen_real (10-28, fast mode).
- Pro: benzonchan (Pro $100, 10-30, mixed Terra/Sol, one task 50% weekly), ArugulaAnnual1765 (Pro 100), Proxiconn
  ("20x"), TheTwistedTabby (Pro 100), Humble-Kiwi-5272 and BearsAreCrying (Pro). None has a token count or a
  single-model priced reading.

## Metering discrepancy (Plus 5h)
1. Stage 1's dollar ranges for el-rocho ($1.8–7.8) and for dennisvoss1978 after the update ($2.5–6.9 plus output)
   both contain $5.3–5.5. The 2–3× gap is in tokens per 1%, and that ratio depends on the cache share, which the
   GitHub comments omit. Only dennisvoss1978's pre-update CLI reading ($1.0–2.8 plus unknown output) cannot be
   reconciled.
2. HoYin1600p (r/codex 1xizol3, 19ruxfb27va1v, 10-30) reports that Terra used through the headless CLI is billed as
   Sol, at 2× the rate, while the Windows app bills it correctly. dennisvoss1978's readings are CLI-based. The
   report is unverified, single and not provider-acknowledged: no GitHub issue was found.
3. Codex **credits** are priced at list for Terra (LaoZhang AI, 10-27: 58,622 / 49,792 cached / 1,245 output =
   0.44 credits, which is 25 credits per API $). The credit schedule therefore does not explain any meter
   difference.
4. openai/codex #58477 (10-31): the CLI's displayed "tokens used" excludes cached input. Readings taken from that
   display understate total tokens.
5. ayudha90's own Terra readings vary 2.4× between tasks on the same account and day, and the meter is coarse
   (0.5–1pp steps).

Conclusion: the evidence is consistent with task, cache-share and harness variance, plus a possible CLI billing
fault, rather than a second, faster meter rate. It is not settled. A same-task A/B on the CLI and the app with a
full cached/uncached/output split is still needed.

## Partition notes (Pro)
- **Day 25 (2026-10-29):** "doubling all usage limits for all Pro 100/200/500 tiers … won't be reducing usage
  limits for Pro 200, so your Work and Codex usage will stay the same." Source: forum 1403525 #117, quoting Tibo.
  For Pro 200 the Codex effect is ambiguous; several users see no change in Codex burn (forum 1403897 #46–47;
  r/codex 1xjnmmr). Readings before and after 10-29 stay apart on every Pro tier. None exist on either side.
- Pro has no 5h window, so every Pro cell is weekly (or monthly at 4.33 weeks).
- **Day 23 reset:** announced 2026-10-28 02:42 UTC (Qiita sponge841841, 11:42 JST), i.e. 10-27 PT. Stage 1's
  admitting readings do not span it.

## O11 assessment (two independent non-provisional reports; largest lower bound ≤ 1.20 × smallest upper bound)
| Model × tier × unit | Qualifying reports | Range test | O11 |
|---|---|---|---|
| Terra × Plus × 5h | pensuke89 [5.28, 5.51]; IndividualPlus2011 [5.33] | 5.33 ≤ 1.20 × 5.33 = 6.40 ✓. Still passes with provisional S3 [1.8, 7.8] and, if admitted, N1 [2.60, 14.8] | **Met** (≈$5.3–5.5 per 5h; no conversion to a billing period, O82) |
| Terra × Plus × week (→ month) | 0 | — | Not met (cross-checks $32 and $34.33, both derived from 5h) |
| Terra × Pro $100 × week, before / after 10-29 | 0 / 0 | — | Not met |
| Terra × Pro $200 × week, before / after 10-29 | 0 / 0 | — | Not met |
| Terra × Pro $500 × week, before / after 10-29 | 0 / 0 | — | Not met |
| Terra × Pro (any) × 5h | n/a | — | n/a (Pro has no 5h window) |
| Carbon × AI Plus / AI Pro / AI Ultra × any unit | 0 | — | Not met: model not offered on any consumer plan |

## Gemini 4 Carbon availability
**Verdict: not available on any Google consumer plan as of 2026-10-31T04:10Z (stage 1 confirmed).**
- one.google.com plans page: Pro and Ultra list Gemini 4 Argon; Carbon is absent.
- Antigravity models page: no Carbon.
- Gemini app release notes: newest entry 2026-10-13 (Argon).
- HN 50288810 (10-29): "I only see Argon via gemini.google.com".
- theaicareerlab (reviewed 10-30): "It isn't in the Gemini app or on any Google AI plan".
- Reddit Carbon mentions 10-28..31 are all anticipatory.
- Rollout remains cyber defenders → Fairwind partners → consumers. The Argon precedent (13 days) points to
  mid-November at the earliest.

## Queries
30 query groups, about 110 queries and fetches. The full list is in `research_notes/queries-and-sources.md`:
- arctic-shift comment, post and thread searches across 13 subreddits
- GitHub issue pages and search
- OpenAI forum search and topics
- HN Algolia
- Qiita, Zenn and sov2ex
- Google AI forum
- 5 WebSearch queries and 5 WebFetch page reads

## Sources reached / unreachable
- **Reached:**
  - Reddit via arctic-shift, using curl (Python urllib got 403)
  - i.redd.it
  - github.com HTML through WebFetch
  - OpenAI community JSON
  - HN Algolia
  - Qiita
  - Zenn
  - sov2ex
  - discuss.ai.google.dev
  - WebSearch
  - blog.laozhang.ai
  - gemini.google
  - antigravity.google
  - one.google.com
  - theaicareerlab.com
- **Unreachable:**
  - LINUX DO (403)
  - Bluesky public API (403)
  - X (not attempted, login wall)
  - GitHub REST/GraphQL (403 in this session per stage 1; not used)
  - r/codex 1xjir5f (removed)
  - pullpush (index stale; not used)
