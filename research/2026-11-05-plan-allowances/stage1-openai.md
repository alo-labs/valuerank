# Stage 1 (plain web search), OpenAI ChatGPT / Codex plans — 2026-11-05

Scope: user reports of API-list-priced Codex usage per meter fraction for GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Astra,
GPT-6 Luna and GPT-5.6 Luna on ChatGPT Plus, Pro 100, Pro 200 (including grandfathered 20x) and Pro 500. The report
window is 2026-10-02 to 2026-11-01T06:10Z. Priority went to 2026-10-25..11-01 and to Pro readings after the
2026-10-29 doubling. Rules: `data/plan_cost_routes.json` evidencePolicy.reportEligibilityProfile (O71 v1). Already
recorded reports were matched against `data/plan_reports.json` (provider OpenAI, 27 rows) by observer and URL.

## Summary

- **Two new qualifying observers, both found in this pass.**
  - **jitendersingh0411** (openai/codex#55210): Plus, GPT-6.1 Sol, 5h window, two 30-point readings from local logs.
  - **hd264 / aiplans.dev** (V2EX t1253221 and the aiplans.dev report files): Pro 200, GPT-6 Astra, weekly window. It
    is a controlled synthetic test with a full per-call ledger. It has one reading before the 2026-10-29 doubling
    (Oct 28) and one after it (Oct 30). It is the only priced Pro reading after the doubling that this pass found.
- **No new qualifying reports** for Terra, GPT-6 Luna, GPT-5.6 Luna, Pro 100 or Pro 500.
- **After the doubling, Pro evidence is almost absent.** Apart from aiplans, users posted only meter impressions
  ("can't make a dent", "45% left after two days of Astra high"), with no token counts.
- **The sample is still biased.** Complaint threads dominate, as in the earlier passes. Several late-window reports
  describe 2–3× per-token meter swings within one observer, for example jitendersingh0411's two readings.
- **O11 status changes.** Plus 5h for GPT-6.1 Sol can now pass in the post-Oct-11 partition, but only if Oleg-125's
  Oct 11 reading is assigned to that partition (see the verdicts). Every Pro cell still fails: one report at most per
  partition.

## Prices used (API list, per 1M tokens, ≤272K context)

| Model | Input | Cached input | Output |
|---|---|---|---|
| GPT-6.1 Sol | $2 | $0.10 | $10 |
| GPT-6.1 Terra | $1 | $0.05 | $5 |
| GPT-6 Astra | $10 | $1 | $50 |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |
| GPT-5.6 Luna | $0.20 | $0.02 | $1.20 |

These are the prices used in the 2026-10-25 and 2026-10-31 records.

- Long-context fees were removed on subscriptions on 2026-10-11, so readings after that date are priced at standard
  rates.
- Fast mode is converted at 2.5× and Ultrafast at 8× (`speedModeMultipliers`).
- Codex credits are 25 per API dollar.

## Candidate table

Abbreviations: u = uncached input, c = cached input, o = output; pp = percentage points; "5h" = five-hour window.
NEW / REC = new or already recorded. Q = qualifies under O71 v1.

| # | Plan | Unit | Model | Observer | URL | Date (UTC) | Token split | Meter movement | $ at API list | Speed | NEW / REC | Q? | Reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Plus | 5h | GPT-6.1 Sol (high) | jitendersingh0411 | github.com/openai/codex/issues/55210 (comment 2026-10-31) | readings Oct 25 and Oct 31 (Oct 31: 15:42–16:12 IST) | Oct 25: "~13.21M input", "~99.0% cached", "~68.9K" output → u ≈132K, c ≈13.08M. Oct 31: "~5.19M input", "~99.4% cached", "~29.0K" output → u ≈31K, c ≈5.16M | 30pp of 5h in each reading, from local JSONL logs against recorded 5h percentages | Oct 25: $2.26 per 30pp → **$7.54/5h**. Oct 31: $0.87 per 30pp → **$2.89/5h**. With cache-% rounding and ±1pp meter: **$2.78–7.84** | standard (not stated otherwise) | NEW | **Y** | Exact model and tier stated; one model; meter fraction; inside the window; not a fault day. The observer flags a ~2.6× per-token metering change between the two readings. That is observer-reported only, so under O99 it splits nothing and the report carries the whole range. Token split derived from the stated cache % (rounded) |
| 2a | Pro 200 (variant unstated) | week | GPT-6 Astra | hd264 / aiplans.dev | v2ex.com/t/1253221; aiplans.dev/reports/codex-models-2026-10-28.md (+ .json) | 2026-10-28 06:31–06:32Z | 28 calls: u 2,320,149 / c 271,104 / o 4,070 (cache write 0) | weekly 89% → 92% used (3 ± 1pp); control session quiet; same reset time | $23.68 → point **$789/week**; rounding range **$592–1,184** | not reported | NEW | **Y (provisional tier)** | **Pre-Oct-29.** Synthetic run (~93K-token review prompt, short output, nonce), single model, isolated batch. "ChatGPT Pro 200" is confirmed by the account owner, but whether it is grandfathered 20x or new 10x is not stated, so it is provisional for the grandfathered cell. The measurer runs the test on someone else's account; it is still one direct measurement, not an aggregate |
| 2b | Pro 200 (variant unstated) | week | GPT-6 Astra | hd264 / aiplans.dev | aiplans.dev/reports/codex-models-2026-10-30.md (+ .json) | 2026-10-30 06:47–06:51Z | 60 calls: u 4,765,206 / c 806,400 / o 8,733 | weekly 49% → 53% (4 ± 1pp); control quiet; reset 2026-11-04T06:35:31Z unchanged | $48.90 → point **$1,222/week**; range **$978–1,630** | not reported | NEW | **Y (provisional tier)** | **Post-Oct-29.** The same observer as 2a gives per-period readings. The account owner reports an entitlement upgrade, which aiplans did not verify. A 32-call batch (u 2,588,635 / c 374,528 / o 4,681; 45→47%) is consistent ($883–2,650) |
| 2c | Pro 200 | week | GPT-6.1 Sol | hd264 / aiplans.dev | as 2b | 2026-10-30 06:42–06:46Z | 59 calls: u 4,725,504 / c 750,208 / o 8,803 | 48% → 49% | $9.61 per ≤2pp → **≥$481/week** (lower bound only) | not reported | NEW | N | Lower bound only, with no upper bound. The control session was not quiet. The author publishes no point estimate |
| 3 | Plus (stated in post) | 5h | GPT-6.1 Sol medium | ayudha90 | reddit.com/r/codex/comments/1xgq393 (also 1xgriu5) | 2026-10-27 | none | 1% of 5h = "$0.146" (author's $) | $14.6/5h (1% resolution: ~$9.7–29) | standard | NEW for Sol (Terra readings evaluated 10-31) | N | No token split. The $ is the author's or Codex's display, with unstated pricing (same ground as the 10-31 Terra assessment). 1pp resolution |
| 4 | Plus | 5h | GPT-6 Luna max | ayudha90 | as #3 | 2026-10-27 | none | 1% = "$0.040" | ≈$4/5h | standard | NEW | N | Same grounds as #3 |
| 5 | Plus | 5h | GPT-6.1 Terra xhigh / max | ayudha90 | as #3 | 2026-10-27 | none | 1% = "$0.074"; 4% = "$0.282" | $7.4 / $7.05 per 5h | standard | REC (assessed 10-31, not in plan_reports) | N | Already assessed as not qualifying |
| 6 | Plus | 5h | GPT-6 Astra light + Luna subagents | Fickle-Ad3007 | reddit 1xjpxrx comment 19rwfxbwc0n42 | 2026-10-30 | "6.7M tokens total", no split | 56% of 5h | author's "$5.26" → ≈$9.4/5h | standard | NEW to plan_reports (quoted in 10-31 stage 3 evidence) | N | Mixed model, no split |
| 7 | unstated (5h meter shown) | 5h? | GPT-6.1 Sol max (+13 subagent sessions) | h3tek | github.com/openai/codex/issues/55997 (comment 2026-10-27) | 2026-10-27 | u 2,141,700 / c 24,327,424 / o 169,628 | "4% used" → "99% used" in 8m31s | $8.41 per 95pp → ≈$8.86/5h | not stated | NEW | N | Tier unstated (Plus can only be inferred; at most provisional). Window not named. Subagent models not stated |
| 8 | Plus | 5h | GPT-6 Sol medium | kaderebak | github.com/openai/codex/issues/57579 | 2026-10-27 | input 9,380,242 (c 9,317,760) / o 40,842 | ~30% → 0% left (≈30pp) | $1.47 → ≈$4.9/5h | standard | NEW | N | Model GPT-6 Sol, not a cohort model. The meter reading is approximate |
| 9 | Pro (tier unstated) | week | GPT-6 Astra | AstrumNya | github.com/openai/codex/issues/54767 | 2026-10-17 00:32–00:52 | c 8,466,304 / u 30,402 / o 14,901 | weekly 100% → 97% | $9.51 per 3pp → ≈$317/week | not stated | NEW | N | Oct 17 is an accounting-fault day. Tier unstated |
| 10 | unstated (5h) | 5h | Luna max + Sol medium supervisor | dictionizzle | reddit 1xg0vvk comment 19rtkg2nnvvno | 2026-10-29 | "50M tokens… 49.5M cached input, 0.5M output" | "100%" | at GPT-6 Luna prices ≈$0.75/5h | standard | NEW | N | Mixed model. Luna version and tier unstated. Not a measured reading ("near like") |
| 11 | Pro 100 ("5x") | week | not restated (issue model GPT-6 Astra ultra) | YiwenPang (2nd reading) | github.com/openai/codex/issues/56669 (comment 2026-10-29) | 2026-10-29 03:13–07:43Z | "about 137M tokens… mostly cached", no split | 8% → 58% used | not priceable | not stated | REC observer (new reading) | N | No split. Falls on the doubling day at an unknown hour, so it cannot be assigned to a partition |
| 12 | Pro 500 | week (exhaustion) | GPT-6.1 Sol medium | ponzu07 | reddit 1xh7xvv (screenshot s6ixcgkxd3yh1) | 2026-10-27 | "4.6M" lifetime tokens, no split | "hit the usage limit" | not priceable | **Ultrafast** | NEW | N | No split. Commenters say the meter lags; probably not weekly exhaustion |
| 13 | Pro 200 (tier unstated in post; "pre-50% cut") | week | GPT-6.1 Sol | spierce7 | reddit.com/r/codex/comments/1wzn2tv | 2026-10-07 (reset "a few days ago") | none (ccusage) | 100% → 0% | "~<$400" | not stated | NEW | N | Tier inferred. No split. The window likely spans the Oct 7 banked reset |
| 14 | Plus (2-week aggregate) | — | 7 Codex models mixed | tuhdo | reddit.com/r/codex/comments/1x84sa3 (i.redd.it/jn4jl77tjzvh1) | 2026-10-17 | Codex: u 121.7M / o 21.8M / c 3.84B; "$781.58" | "100% quota consumed weekly + 70–80% from resets" | — | — | NEW | N | Mixed model, multi-week aggregate |
| 15 | Pro 100 | week | Astra Fast + Sol + Luna | Teva_Soft | reddit 1x1f92n comment peuhaxg | 2026-10-09 | per-model totals only | "roughly 10% usage" | author: $161 + $6 + $1 | Fast (Astra) | NEW | N | Mixed model |
| 16 | Pro 200 | week | unstated | Dangerous-Sport-2347 | reddit 1ww9cf7 comment pdj9j3o | 2026-10-03 | none | 13% weekly | "$21" → ≈$162/week | — | NEW | N | Model unstated; spans a reset day |
| 17 | unstated | unstated | unstated | Repulsive_Round_5401 | reddit 1ww9cf7 comment pdjuq1h | 2026-10-03 | none | "Each 1% of quota represented $13.73 … vs $12.04" | — | — | NEW | N | Plan, model and window unstated |
| 18 | Pro 200 ("20x") | week | Sol 6.1 Fast + ~33% Terra | AmthorTheDestroyer | reddit 1xm6cci/19s1jyxkfokn8; 1xmtppj/19s35144ai3dv | 2026-11-02/03 | none per % | "approximately 4$ API usage per % weekly" | ≈$400/week | Fast | NEW | N | Mixed model, no split, after cutoff |
| 19 | Pro 100 | week | mostly Sol 6.1 low | ProfessionalJackals | reddit 1xmtppj/19s34jm52ndt1 | 2026-11-03 | none | "100% + 2 resets divided by 3" | "$1120 / week" | — | NEW | N | Multi-week average across resets. No split or model breakdown. After cutoff |
| 20 | Pro 100 | week | unstated | midraos | v2ex.com/t/1252790 #7 | 2026-10-29 | none | — | "约是 6000 credits" ≈$240/week | — | NEW | N | Derived figure, model unstated |

### After the cutoff (2026-11-01T06:10Z or later): listed only, none counts for this release

| Plan / unit | Model | Observer | URL | Date | Data | Note |
|---|---|---|---|---|---|---|
| Plus 5h | GPT-6.1 Sol medium | Fun_Squirrel5446 | reddit.com/r/codex/comments/1xm2jd0 | 2026-11-02 | "$0.55 (used 7% of the 5 hour limit)" → ≈$7.9/5h | Codex-displayed $, no split |
| Plus 5h | GPT-5.6 Luna low | Global_Knee5354 | reddit.com/r/codex/comments/1xnj6d5 | 2026-11-04 | "119,000 tokens", "$0.01", 8% of 5h | The author doubts the attribution. Anomaly |
| Plus 5h | "Luna" xhigh (version unverified) | maksymturskyi-del | github.com/openai/codex/issues/58898 | 2026-11-02 | 4,420,438 input / 15,537 output, no cache split; 5h 22% → 98% | No cache split |
| Plus 5h | GPT-6 Astra medium | tonyfenwick8814121 | github.com/openai/codex/issues/59398 | 2026-11-04 | c 8,592,000 / u 395,059, output not reported; 5h 0 → 98% | No output count |
| Plus 5h | Sol xhigh → Terra high | dpglobalWeb | github.com/openai/codex/issues/59235 | 2026-11-03 | 5h exhausted; no tokens | Mixed |
| Pro 500 week | GPT-6 Astra high, standard | Procureallyai | github.com/openai/codex/issues/59194 | 2026-11-03 | 100% → 92% remaining in ~2h; no tokens | Post-doubling, unpriceable |
| Pro 500 day | mostly GPT-6.1 Sol medium | Any_Evidence4750 | reddit.com/r/codex/comments/1xmtppj | 2026-11-02 | 296,688,363 input / 14,114,468,864 cache read / 58,451,142 output ≈$2,589 (Sol prices) in "one day" on a banked reset | No meter reading. Mixed tools (ccusage) |

## Per-cell O11 verdicts

O11 needs two independent, non-provisional reports where the largest lower bound ≤ 1.20 × the smallest upper bound.
The verdicts below combine recorded and new reports under the flags as recorded. Stage 2 should recompute them with
the E270 partition tests.

- **GPT-6.1 Sol × Plus × 5h**
  - Post-Oct-11 partition: jitendersingh0411 [$2.78, 7.84] (NEW) and Oleg-125 [$3.6, 7.4] (REC).
    Test: 3.6 ≤ 1.2 × 7.4 = 8.88. **Passes only if Oleg-125's Oct 11 reading (window unstated, on the split day,
    meter direction ambiguous) is placed after the 2026-10-11 price split.** Otherwise one report: **fail**.
  - Pre-Oct-11 partition: mehoney [8.3, 8.7] alone (Pasto_Shouwa is a mixed-model lower bound): **fail**, unless
    Oleg is placed here, in which case 8.3 ≤ 8.88 passes.
  - Either placement gives exactly one passing partition.
  - Caveat: jitendersingh's own 2.6× spread signals unstable metering.
- **GPT-6.1 Sol × Plus × week:** mehoney $57 only; Pasto_Shouwa is a lower bound. **Fail** (no new report).
- **GPT-6.1 Sol × Pro 100 / Pro 500 × week:** no qualifying single-model reports. **Fail.**
- **GPT-6.1 Sol × Pro 200 (incl. grandfathered) × week:**
  - Pre-Oct-29: the recorded reports conflict. sadiqmdasif [105, 130] (anomaly) and DhAdaptive [401.5, 407.9] in Fast
    dollars (≈$1,004–1,020 standard-equivalent) fail the margin.
  - Post-Oct-29: only aiplans' lower bound (≥$481). **Fail.**
- **GPT-6.1 Terra × Plus × 5h:** **passes, unchanged** (pensuke89, IndividualPlus2011; 2026-10-31 record). No new
  qualifying report. ayudha90 does not qualify.
- **GPT-6.1 Terra × all other cells:** 0 qualifying. **Fail.**
- **GPT-6 Astra × Pro 200 × week:**
  - Pre-Oct-29: aiplans [$592, 1,184], provisional for the grandfathered key because the tier variant is unstated.
    genellect is mixed and Fast. **Fail** (one report).
  - Post-Oct-29: aiplans [$978, 1,630] only. **Fail** (one report; tier variant also unstated).
- **GPT-6 Astra × Pro 100 × week:** pre-Oct-29 only, all recorded. sentrybottale [330, 400]; YiwenPang [318]
  (anomaly); mrak- $193 Fast ≈ $482.5 standard. sentrybottale + YiwenPang: 330 ≤ 381.6, which passes only if the
  anomaly flag admits YiwenPang. With mrak-: 482.5 > 1.2 × 318 → fail. No new report. Post-Oct-29: 0 reports,
  **fail**.
- **GPT-6 Astra × Plus × 5h:** Crystal4276 (anomaly) and kamo-k (before the window) only. **Fail.**
- **GPT-6 Astra × Pro 500 × week:** totorofly (Fast, pre-Oct-29) only. **Fail.**
- **GPT-6 Luna (all plans) and GPT-5.6 Luna (all plans):** no new qualifying reports. Recorded ones are before the
  window or lower bounds. **Fail.**

## Plan facts found on this pass (no partition edits made)

- **Oct 29 doubling text.** Tibo's X post (x.com/thsottiaux/status/2115850175868727621): "doubling all usage limits for
  all Pro 100/200/500 tiers and Business Premium, effective today … won't be reducing usage limits for Pro 200".
  - ContextBolt and Xenospectrum report a different split: Pro 100 and Pro 500 doubled, and Pro 200 lower-allowance
    subscribers raised to the higher allowance.
  - This bears on whether post-Oct-29 Pro 200 still has a separate grandfathered key.
- **The Oct 29 doubling shows on the meter.** wmpeng (#58128, plan_type prolite) saw used_percent go 18 → 9 without a
  reset on 2026-10-30 ~01:06 UTC+8.
- **Reset dates moved on the aiplans account.** The Oct 28 window reset at 2026-11-02T06:22Z; the Oct 30 window resets
  at 2026-11-04T06:35:31Z. aiplans' Oct 28 report also records a reading of 92 → 0% with a changed reset time, which
  it does not treat as consumption.
- **Codex now shows a per-task $ figure** (ayudha90, Fun_Squirrel5446, Global_Knee5354). Its pricing basis is not
  documented, so it is not used as a token-priced reading.
- **O165 archiving.** Every report added after 2026-11-01 needs an archived hashed copy. Copies of the aiplans
  markdown and JSON ledgers were downloaded to the session scratchpad, not to the repo. Stage 2 should archive them.

## Queries run

1. **HN Algolia** `search_by_date`, `created_at_i > 1790899200` (2026-10-02), 200 hits per query: "weekly limit
   codex", "codex API pricing equivalent", "codex pro limit doubled", "codex usage % week", "Sol codex usage", "Terra
   codex", "Astra codex limit", "Luna codex", "pro 500 codex", "codex plus subscription worth", "ccusage codex", "codex
   $ API", "codex quota". 416 unique hits, filtered for % plus $. Nothing priceable.
2. **Reddit via arctic-shift.**
   - All r/codex posts 2026-10-02..11-05 (4,858).
   - r/ChatGPTPro, r/OpenAI, r/ChatGPTCoding posts with title "codex".
   - r/codex comments by body keyword: "cached", "api price", "api pricing", "api cost", "equivalent", "ccusage" (timed
     out), "tokscale", "per 5h", "of my weekly", "doubled". 3,968 unique.
   - Full comment threads for 1xmtppj, 1xh7xvv, 1ww9cf7, 1wzn2tv.
   - Images: s6ixcgkxd3yh1, vort94tepezh1, jn4jl77tjzvh1.
3. **OpenAI community forum.**
   - search.json: "weekly limit", "usage limit", "api price", "tokens %", "codex usage", "cached tokens weekly", "terra",
     "astra weekly", "luna", "pro 500", "doubled" (with `after:` dates).
   - Topic posts read: 1409401 #940–#1027, 1403525 #100–#132, 1407973, 1389878 (Codexometer), 1378553.
4. **GitHub openai/codex** via `gh api search/issues`.
   - Issues created 2026-10-02..11-05 matching weekly, 5h, 5-hour, quota, "usage limit", "rate limit", cached, "token
     usage", "API price", "Pro 500", "Pro 200", "Pro 100", Plus. 2,340 unique, filtered to 82.
   - Issues updated since 10-25 matching comment terms ("cached weekly", "terra cached", "tokens per 1%", "API price",
     "doubled", …).
   - Pages read with WebFetch: #56866, #41220, #55997, #59398, #55210 (twice), #58128, #42987, #40880, #52851, #45086,
     #56669, #54995, #51088, #54956.
5. **V2EX** via sov2ex: "codex 额度 pro", "codex 周限额", "codex plus 5小时", "codex terra 额度", "codex 翻倍" (since
   ~10-26). Topics 1253221 and 1252790 read with replies.
6. **aiplans.dev**: reports codex-models-2026-10-28 and 2026-10-30 (.md and .json), the guide
   codex-pro-200-quota-benchmark, and sitemap.xml.
7. **Qiita API**: "Codex created:>2026-10-20". Titles only, no measurements.
8. **WebSearch**:
   - "Codex Pro usage limits doubled October 29 2026 API equivalent weekly measured tokens"
   - "GPT-6.1 Sol Codex Plus 5-hour limit API cost per window measured"
   - "Codex Pro 500 weekly limit API equivalent dollars November 2026"
   - X / Sol / doubling query
   - GPT-6 Luna Plus query
   - Pro 100 tokens-per-1% query
   - inventivehq.com/blog/codex-subscription-usage-measured was read: last modified 2026-10-04, nothing new.

## Venues unreachable or limited

- **GitHub REST repo endpoints** (`repos/openai/codex/issues/comments`): refused ("GitHub access to this repository is
  not enabled for this session"). Only search worked, so comment text was read through WebFetch for selected issues.
  Unread comment threads on other issues may hold more readings.
- **arctic-shift**: frequent "Timeout. Maybe slow down a bit". The `ccusage` body search never completed, and
  subreddit coverage beyond r/codex was title-filtered only.
- **Not attempted**: X (no login; seen only through search snippets), LINUX DO (Cloudflare), YouTube, Bluesky.
- **Aggregators**: modeldial.com and codexradar.com were cited by V2EX users. They are aggregators (cross-check only)
  and were not fetched.
