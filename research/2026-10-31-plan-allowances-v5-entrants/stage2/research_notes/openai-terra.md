# Stage 2 notes: GPT-6.1 Terra on ChatGPT Plus / Pro $100 / Pro $200 / Pro $500 (2026-10-31)

Scope: extends `../../stage1-openai-terra.md`. Items already there (pensuke89, IndividualPlus2011, el-rocho,
dennisvoss1978, Emotional-Cut2952, HoshiEstrellas and the meter-only anecdotes) are not re-listed except where new
facts were found. Window used: 2026-10-26 (launch) .. 2026-10-31T04:10Z. Prices: $1.00 input / $0.05 cached /
$5.00 output per 1M (AA snapshot, as stage 1). Dollar arithmetic is mine unless marked "author's".

Note on method: the deep-research skill expects researcher subagents; no subagent tool was available in this
session, so the coordinator ran the research directly, per the skill's fallback.

## New candidate report (priceable, but not qualifying)

### N1. ayudha90, ChatGPT Plus, 5h window, GPT-6.1 Terra xhigh and max (r/codex, 2026-10-27)
- Tier and unit stated by the observer: post title "GPT 6.1 Terra on GPT Plus" (1xgcjjb); "5hr in plus" (comment
  19rsetm8ka18g, 2026-10-28 16:20 UTC, answering which meter the 1xgriu5 readings are on).
- Readings (dollar figures are the author's; the author does not say how they were priced, and no token split is
  given):
  1. Document task, Terra **xhigh**: "$0.091 total … usage of Terra is 3%" (comments 19rq3tppay6ma and 19rq3j8qxks1t,
     2026-10-27 09:12–09:19 UTC; Sol medium on the same task $0.4475 for 6%).
     Point $3.03 per 5h; with the meter's ±0.5pp integer rounding, **$2.60–3.64 per 5h**.
  2. Blender 3D task, Terra **xhigh**: "1% usage, $0.074, 3 mins" (posts 1xgpxyf / 1xgq393 / 1xgriu5, 2026-10-27
     11:26–12:44 UTC). Point $7.40; rounded range **$4.93–14.8 per 5h**.
  3. Same task, Terra **max**: "4% usage, $0.282, 11 mins". Point $7.05; rounded range **$6.27–8.06 per 5h**.
  (Comparators in the same post: Sol 6.1 medium 1% $0.146; Luna 6 max 1% $0.040.)
- Report range (one observer = one report): **$2.60–14.8 per 5h** (points $3.03–7.40).
- Timing: all before the Oct 27 ~10:23 PT (17:23 UTC) shift dennisvoss1978 described, before the Day 23 reset
  (announced 2026-10-28 02:42 UTC = 11:42 JST, per Qiita sponge841841), and not on a fault day.
- Eligibility: exact model, stated tier, stated unit, one model per reading, inside the window, observer.
  **Does not qualify**: the dollar figures are the author's with an undisclosed pricing basis and no token split,
  so "API-priced consumption" (rule 1) cannot be verified; the meter deltas (1–4%) are within a few rounding
  steps, so the readings are imprecise. Listed as a cross-check.
- Sensitivity: if admitted as a range report it would **not** break the Plus 5h range test: largest lower bound
  $5.33 (IndividualPlus2011) ≤ 1.20 × smallest upper bound $5.33 = $6.40.
- Its own readings disagree by 2.4× (document task $3.03 vs Blender tasks $7.0–7.4), which matches the
  task-to-task variance seen in el-rocho and dennisvoss1978.

## New meter-only anecdotes (no token or dollar figures; context only)
- SlipperyBandicoot (r/codex 1xhgnnp / 1xhhzme, 2026-10-28 09:05–09:08 UTC; Plus implied by a 5h window): Terra
  medium, "entire 5 hour usage, and 16% of weekly usage" in about 2 hours of UI tweaks, starting at the Day 23
  reset. **Weekly** fraction, but no tokens.
- facciocosevedogente3 (r/ChatGPTCoding 1xhl958, 2026-10-28 11:16 UTC, **Plus**, Terra High): one website
  migration "consumed roughly 70% of my entire weekly Codex usage allowance". **Weekly**, no tokens.
- psamytron (r/codex 1xjjzut, 2026-10-30, Plus, no 5h meter shown): weekly 70–80% → 0% in about 4 hours; usage
  screenshot wb1ft0765nyh1 shows a mixed day (gpt-6.1-terra 51.9%, gpt-6-astra 28.6%, gpt-6.1-sol 12.2%, gpt-6-sol
  7.3%). Mixed model; no tokens.
- jimmym007 (1xhhf0z 19rt2jrf926m9, Oct 28): Terra low with 4 subagents drained the 5h limit in under 10 minutes; a
  rerun without subagents used 20% of 5h.
- TheMythicSorcerer (1xjjzut 19rw8hbemeoyr, Oct 30, Plus): Terra used 23% of 5h for a spreadsheet task where Sol had
  used 46% the week before.
- nickmullen_real (1xhz6z1, Oct 28, Plus): Terra low **fast mode**, 5h window gone in about 4 minutes.
- Pro-tier mentions, none priceable:
  - benzonchan (r/OpenaiCodex 1xipkr0, Oct 30, Pro "5x" = $100, after Day 25): one task 50% of weekly; mixed
    Terra/Sol.
  - Humble-Kiwi-5272 (Oct 29, Pro): weekly ends quickly on Sol; no numbers.
  - ArugulaAnnual1765 (Oct 26 and 29, Pro 100): Terra high "havent used a single percentage".
  - Proxiconn (Oct 27, "20x"): under 1% weekly for 3 Blender models.
  - TheTwistedTabby (Oct 27, Pro 100): "a joke against my weekly"; mostly Luna.
  - xter418 (Oct 27, plan unstated): ~50% weekly for a 10.5 h Terra-plus-Sol workflow.
  - BearsAreCrying (Oct 29, Pro): mixed Astra and Terra.
  - Due_Warthog749 (Oct 31): Astra, not Terra.

## Metering-discrepancy evidence (Plus 5h)
Stage 1's discrepancy: pensuke89 and IndividualPlus2011 (≈$5.3–5.5 per 5h, priced) against el-rocho and
dennisvoss1978 (2–3× more meter per token, unpriced). New facts:
1. **Not a discrepancy in dollars for most readings.** Stage 1's own dollar ranges for el-rocho ($1.8–7.8) and
   dennisvoss1978 after the update ($2.5–6.9 plus output) contain $5.3–5.5. Tokens per 1% differ mainly with the
   cache share, which neither GitHub report gives. Only dennisvoss1978's pre-update CLI reading ($1.0–2.8 plus
   unknown output) cannot reach $5.3 at any plausible output share.
2. **Possible CLI misattribution, unverified.** HoYin1600p (r/codex 1xizol3, comment 19ruxfb27va1v, 2026-10-30
   02:11 UTC): "using Terra in the windows app bills the usage correctly as Terra, but if you use headless CLI it
   shows up as Sol. Being double the price it moves twice as fast as you'd expect." Both of dennisvoss1978's
   fast-moving readings come from CLI session files. No matching GitHub issue was found
   (`author:HoYin1600p` returned 0; the report may have gone through /feedback). It is a single observation, not
   provider-acknowledged. Under O99 it splits nothing and is flagged.
3. **Credits are priced at list for both models.** LaoZhang AI blog (2026-10-27, Codex CLI 0.164.0-alpha, plan
   unstated): Terra medium billing task 58,622 input / 49,792 cached / 1,245 output = **0.44 credits**. That is
   exactly 25 credits per API dollar at $1/$0.05/$5. Sol medium 78,624 / 64,512 / 1,821 = 1.32 credits at
   $2/$0.10/$10. So credit metering is proportional to list price for both models; a 5h-meter discrepancy is not
   explained by the credit schedule.
4. **The CLI's displayed tokens exclude cached input.** openai/codex #58477 (hx-design, 2026-10-31, gpt-6.1-terra
   medium): the CLI's "tokens used" = input − cached_input + output. Any reading based on the CLI's displayed total
   rather than session-file token_count events is uncached plus output, not total. This cuts the other way (it
   would make such readings more valuable per 1%). It cannot be applied to el-rocho without knowing his source.
5. **Meter granularity.** IndividualPlus2011 (r/OpenaiCodex 19rqcnat7yqpx, Oct 27) says the usage meter is rounded
   to 0.5. Small-delta readings (ayudha90's 1–4%, dennisvoss1978's 4pp) carry large relative error.
6. ayudha90's own readings span $3.03–7.40 per 5h on the same account and day: a 2.4× within-observer spread
   comparable to the GitHub gap.

Assessment: the evidence leans toward task, cache-share and harness variance (with a possible CLI-as-Sol billing
fault) rather than a stable 2–3× different meter rate. The two token-priced reports remain the best-measured
values. Nothing new settles it. A clean A/B measurement with a cached/uncached/output split on the CLI and the app,
same task, is still missing.

## Partition facts (Pro) found on this pass
- Day 25 text (forum 1403525 #117, VeitB quoting Tibo's X post 2026-10-29 16:56 PT): "We are doubling all usage
  limits for all Pro 100/200/500 tiers and Business Premium, effective today. We heard your kind feedback and won't
  be reducing usage limits for Pro 200, so your Work and Codex usage will stay the same." VeitB's paraphrase:
  "Work and Codex usage will remain unchanged."
- So, for Pro 200 (grandfathered 20×), Codex limits may be unchanged rather than doubled. Users report no visible
  doubling in Codex:
  - uruzu (forum 1403897 #46, Oct 30): "my usage seems to be burning same rate"
  - xwo (#47)
  - Responsible-Ad-6846 (r/codex 1xjnmmr, Oct 30): about 25% more, then back to normal
  - anthonyaluna (1xipvti, Oct 29): weekly jumped from <20% to ~60% left, a one-off reset-like jump
  r/codex 1xixihf (Active_Potential_795) reads it as Pro $100 10×, $200 20×, $500 50×.
- The partition split at 2026-10-29 still applies to every Pro tier (provider-documented limit change). Whether
  Codex weekly limits on Pro $200 actually doubled is unresolved.
- Day 23 reset timing: announced 2026-10-28 02:42 UTC (Qiita sponge841841, "日本時間10月28日11:42頃"), i.e. Oct 27
  PT. A reading spanning it is excluded (O112). IndividualPlus2011's Oct 28 table and el-rocho's Oct 28 A/B
  postdate it.
- Pro plans have no 5h window (Codex pricing page via Qiita Takuya__; Round_Ganache_4634 quoting the official
  breakdown, Oct 29). Pro cells are weekly-only.

## Counts (GPT-6.1 Terra; candidates / qualifying; stage 1 + stage 2)
| Tier × unit | Stage-1 cand./qual. | New stage-2 candidates | Total qualifying |
|---|---|---|---|
| Plus 5h | 5 / 2 | +1 (ayudha90, not qualifying) | 2 (pensuke89, IndividualPlus2011) |
| Plus week | 2 / 0 (derived figures) | 0 priceable (2 meter-only) | 0 |
| Pro $100 week (pre / post Oct 29) | 0 / 0 | 0 | 0 / 0 |
| Pro $200 week (pre / post) | 0 / 0 | 0 | 0 / 0 |
| Pro $500 week (pre / post) | 0 / 0 | 0 | 0 / 0 |
| Pro tier unstated | 1 / 0 (mixed) | 0 | 0 |
