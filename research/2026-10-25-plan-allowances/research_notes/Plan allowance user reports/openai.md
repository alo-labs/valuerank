# OpenAI ChatGPT plans in Codex: API-priced allowance, user reports (stage 2, 2026-10-25)

Scope: new reports not already in `stage1-openai.md`. Sources searched: OpenAI community forum (search.json), Hacker
News Algolia (comments since 2026-09-25), Reddit via arctic-shift (r/codex, r/OpenAI, r/ChatGPTPro, since
2026-09-25), the openai/codex issue list (the newest 25 "usage limit" issues), and learn.chatgpt.com/docs/pricing.
Dollar figures marked "computed" are my arithmetic at the API list prices in the brief. Normalisation rules used:
- "Fast-mode $/week" = tokens priced at standard API list ÷ weekly fraction consumed.
- "Standard-equivalent $/week" = Fast-mode $/week × 2.5 (Fast spends included usage at 2.5×). For Ultrafast, × 8.
- A user who priced Fast at 2× and Ultra at 6× (the purchased-credit rates) had those figures divided by 2 and 6 to
  get standard list values.

## 1. GPT-6.1 Sol: more meter-based reports (Plus, Pro $100, Pro $200 new/grandfathered, Pro $500)

### Takeaway
I found one strong new token-plus-meter report (u/DhAdaptive, Oct 8–9). It gives GPT-6.1 Sol xhigh in **Fast** mode on
**Pro $200 grandfathered 20×** and on **Pro $500**, from one user, one chat and the same day. Standard-equivalent
values are ≈$1,004–1,020/week (20×) and ≈$920–964/week (Pro 500). I also found one new Plus lower bound
(u/Pasto_Shouwa, Oct 8, ≥$65.6/week, output not reported, during a cache-miss bug). No token-plus-meter report
exists for Pro $100 or for Pro $200 new 10×.

### Cited findings
- **Pro $200 grandfathered 20× → Pro $500, GPT-6.1 Sol xhigh, Fast (u/DhAdaptive, r/codex, 2026-10-09).** "The same
  ongoing chat used `gpt-6.1-sol` with `xhigh` reasoning effort in both periods. The logged speed settings included
  two brief Ultrafast intervals after the upgrade". The figures are native per-response records, deduplicated by
  response ID; "zero exceeded 272,000 input tokens".
  - Before the upgrade (20× plan, Oct 8 14:04 to Oct 9 08:30 MDT): weekly meter "13% → 30%" (17 pp); uncached
    9,529,974, cached 279,467,392, output 2,125,392. The author's value at 2× Fast prices was $136.52.
  - After the upgrade (Pro $500, Oct 9 09:42 to 14:26 MDT): weekly meter "0% → 7%" (7 pp); uncached 3,184,568, cached
    90,563,712, output 681,335. That is $50.80 at the author's Fast-2× and Ultra-6× pricing. Breakdown: Ultra interval
    1 $3.51, Ultra interval 2 $5.98, Fast $41.31.
  - Fast-only subsets: 15 pp → $122.3845288 (20×); 5 pp → $38.5483064 (Pro 500); "API value per meter point $8.16 /
    $7.71".
  - The author concludes "an estimated 21.2% reduction in effective raw-token allowance" after the upgrade (tokens
    per point 17.12M vs 13.49M). On the Fast-only subset it is 3.7%.
  - Source: [Reddit r/codex 1x1y2c1](https://reddit.com/r/codex/comments/1x1y2c1/codex_200_500_my_logs_show_apiequivalent_token/)
  - Computed: 20× full sample $68.26 standard list / 0.17 = **$401.5/week in Fast → ≈$1,004/week
    standard-equivalent**. 20× Fast-only $61.19 / 0.15 = $407.9 → **≈$1,020/week**. Pro 500 Fast-only $19.27 / 0.05
    = $385.5 → **≈$964/week**. Pro 500 combined: (20.66 × 2.5 + (0.586 + 0.996) × 8) / 0.07 = **≈$919/week**.
  - Caveats: Fast mode (standard-equivalent assumes the 2.5× multiplier holds exactly). The meter deltas are small
    (5–7 pp, ±0.5 pp rounding ⇒ ±7–10%). The analysis was done by Codex itself on the user's logs. Commenters noted
    that subscriptions may weight cached input differently from the API (u/RealSuperdau, same thread). The sample is
    1–2 days after DevDay and before the Day 12/16 caching changes (see §4).
- **Plus, GPT-6.1 Sol High with two GPT-6 Luna High subagents (u/Pasto_Shouwa, r/codex, 2026-10-09, describing
  2026-10-08).** "basically destroyed my 5 hour window in only 11 minutes. And my weekly went from 100% to around
  82%". Session: "Total input tokens 6,414,812 / Cached input tokens 534,272 / Uncached input tokens 5,880,540 /
  Overall cache hit rate 8.33%". No output count was given. — [Reddit r/codex 1x1qj57](https://reddit.com/r/codex/comments/1x1qj57/possible_codex_bug_since_october_7_gpt_61_sol_has/)
  - Computed: input only, 5,880,540 × $2 + 534,272 × $0.10 = **≥$11.81 per 5h**; at 18 pp weekly, **≥$65.6/week**.
    These are lower bounds, because Sol output and the Luna subagents' tokens are not counted. Caveat: the author
    suspects a cache-miss bug starting with the Oct 7 update.
- **Plus, GPT-6.1 Sol Medium (shinsunx, openai/codex#56672, 2026-10-24).** A "100% available" 5h allowance was
  exhausted after "4m21s" with "Codex and Work usage limit exhausted". "None [token counts] are reported." This is an
  anomaly report and does not qualify. — [GitHub #56672](https://github.com/openai/codex/issues/56672)
- **Plus, "GPT-6.1 Sol Light" (CosmicProjects, openai/codex#56618, 2026-10-23).** 5h meter 100% → 34% → 17% in about
  2 h; weekly "90% remaining to 87% remaining"; "Token usage: Not available." It does not qualify. —
  [GitHub #56618](https://github.com/openai/codex/issues/56618)
- **Plus, 6.1 Sol xhigh (u/cern0, r/codex, 2026-10-18).** "one prompt of 6.1 xhigh … depleted nearly 100% of my 5hr
  limit and 15% of my weekly". No tokens; on an anomaly day. — [Reddit 1x8zmy9](https://reddit.com/r/codex/comments/1x8zmy9/usage_after_reset_become_unusable/)
- **Plus, 6.1 Sol medium (u/aceaxelblaze, 2026-10-17).** "in 1 minute 5hr limit dropped to 95% and weekly dropped to
  99% … weekly only used to drop like 3-4% tops". No tokens. — [Reddit 1x8dzxx](https://reddit.com/r/codex/comments/1x8dzxx/usage_bug_after_supposed_usage_improvement/)
- **Pro $100, Sol 6.1 xhigh + Luna 6 max (u/etrec89, 2026-10-04).** "I'm sitting at 97% weekly usage now, on Pro 5x".
  Logs gave "Sol 6.1 xhigh: 95.3 combined agent-hours; Luna 6 max: 54.6 combined agent-hours". There are no token
  counts, so it does not qualify. — [Reddit 1wxmxt4](https://reddit.com/r/codex/comments/1wxmxt4/sol_61_luna_6_on_pro_5x_i_actually_struggled_to/)
- **$200 plan (tier generation unstated), 6.1 Sol (u/innociv, 2026-10-03).** "6.1 Sol … under 0.25% per hour" of a
  $200 plan's usage. No tokens. — [Reddit 1wwunz9](https://reddit.com/r/codex/comments/1wwunz9/61_sol_is_the_first_model_ive_seen_that_can_play/)
- **Pro 20×, Sol 6.1 Max (u/3electron, 2026-10-01).** "around 35% of my weekly limit left … suddenly at 0%. The 10k
  credits I was granted were gone within a few minutes". This is an anomaly. — [Reddit 1wuy20y](https://reddit.com/r/codex/comments/1wuy20y/codex_remaining_limit_just_disappeared/)
- **Plus, GPT-6.1 Sol normal speed (u/Zealousideal_Cod_661, 2026-10-16).** The local log showed "55% remaining" at
  17:32 UTC and "0%" at 18:19 UTC. This is an anomaly (Oct 16). — [Reddit 1x7pcx9](https://reddit.com/r/codex/comments/1x7pcx9/codex_usage_suddenly_dropped_from_54_to_0_on/)

### Inferences
- DhAdaptive is one independent source. Its 20× figure (≈$1,004–1,020/week standard-equivalent) is not concordant
  with stage-1 janrysavy #51145 (≈$569 and ≈$323/week, high/xhigh). It would be close only if janrysavy's sessions
  were in Fast mode (×2.5 → ≈$1,420 / ≈$808), and that is not established. So Pro $200 grandfathered still fails.
- DhAdaptive's 20× figure divided by 20 is ≈$50/week per Plus-unit. That is within ≈14% of stage-1 #51604 (Plus Sol
  ≈$57/week, coarse). This is a cross-tier plausibility check, not a qualifying pair.
- On DhAdaptive's numbers, Pro 500 is ≈0.90–0.95× the grandfathered 20× per week rather than 1.25×. The sample is
  small (5–7 pp), so this may be meter rounding, but it does not support "Pro 500 ≈ 25× Plus" relative to "20×" on
  that day.
- Pasto_Shouwa's Plus lower bound (≥$11.8 per 5h) is above stage-1 #51604 (≈$8.3–8.7 per 5h). With a different
  workload (cache-miss-heavy) that is not a contradiction, but the two do not form a concordant pair.

### Gaps
- No token-plus-meter report for GPT-6.1 Sol on Pro $100 or Pro $200 new 10× (the new 10× tier mostly starts after
  Oct 29 for existing subscribers).
- No standard-mode (non-Fast) Pro $500 Sol report.
- I could not query the GitHub issue list beyond the first page (the HTML list returned 403 to curl; WebFetch read
  only page 1).

## 2. GPT-6 Astra (Plus, Pro $100, Pro $500) in standard mode

### Takeaway
I found no new qualifying standard-mode Astra report. The new items are Fast/Ultra or anomaly reports without token
counts, or mixed-model logs without a meter delta.

### Cited findings
- **Pro $500 (claimed), "GPT-6 Ultra Max", "1.5× speed" (totorofly, openai/codex#56634, 2026-10-24).** Weekly "from
  approximately 40% to 31% within only a few minutes"; "Token usage" not provided; the plan tier is unstated in the
  issue. It does not qualify. — [GitHub #56634](https://github.com/openai/codex/issues/56634)
- **Astra Ultra + Fast (u/FoxheadWorkshop, r/codex, 2026-10-22).** "burned through my weekly allowance before I hit
  the banked reset … with 19% left … set everything to Astra Ultra w/ Fast mode". No tokens. —
  [Reddit comment](https://reddit.com/r/codex/comments/1xcpmtx/another_day_another_reset/19ri5r0fvfuis/)
- **Astra as reviewer with DeepSeek (u/_DeerHunter_, 2026-10-24).** "Input tokens: 206,505,491 Output tokens: 601,214
  DeepSeek: 203,547,471, Astra: 2,958,020". There is no meter delta, so it does not qualify. —
  [Reddit comment](https://reddit.com/r/codex/comments/1xdga9u/what_is_wrong_with_the_limits_i_burned_through_50/19rkvy14nciio/)
- **$200 plan (u/innociv, 2026-10-03).** "Fable and Astra … would use like $250-$500 (10%-20%) of your weekly usage per
  hour". This implies ≈$2,500/week, but the source of the dollar figure and the model split are unstated. It does not
  qualify. — [Reddit 1wwunz9](https://reddit.com/r/codex/comments/1wwunz9/61_sol_is_the_first_model_ive_seen_that_can_play/)
- **Pro $100, Astra 6 xhigh (u/Arcticfox2049, 2026-10-03).** "burning my weekly usage like 30%" for multi-repo work.
  No tokens. — [Reddit 1wwio9x](https://reddit.com/r/codex/comments/1wwio9x/opus_55_vs_astra_6_both_xhigh/)
- **Pro (tier unstated), Astra (HN shashu10, 2026-09-28).** "an afternoon with GPT-6 Astra and 100% of my weekly limit
  on a Pro subscription". No tokens. — [HN 49885115](https://news.ycombinator.com/item?id=49885115)
- **Pro $100, Sol and Astra (HN joshstrange, 2026-09-29).** "they both decimated the $100/mo plan's weekly limits in a
  single day running only 1 agent". No tokens. — [HN 49891766](https://news.ycombinator.com/item?id=49891766)
- **Enterprise/Pro $500, Astra (HN iforgotmypasswo, 2026-10-13).** "$500/month for 40+ hours a week of Astra usage,
  with ultrafast mode available". No tokens. — [HN 50077811](https://news.ycombinator.com/item?id=50077811)
- **Pro $500, Astra Ultra (u/CipherSorcerer, 2026-10-09).** "Burned 100% of weekly $500 plan". The body is truncated
  in the mirror; no token counts were seen. — [Reddit 1x1w8yp](https://reddit.com/r/codex/comments/1x1w8yp/burned_100_of_weekly_500_plan_on_70k_lines_of/)
- **Pro 5× (YiwenPang, #56669, 2026-10-24, already in stage 1).** Title: "after Tibo's reset, 176M tokens used 76% of
  allowance vs 490M for 100% the previous day". In the same user's experience, accounting changed between consecutive
  days. — [GitHub #56669](https://github.com/openai/codex/issues/56669)

### Inferences
- The stage-1 Pro $100 standard-mode pair (#56669 ≈$318, #54995 ≈$330–400) remains the only candidate. #56669 itself
  documents a day-to-day change in tokens per percent (490M per 100% vs 176M per 76%), so the meter was not stationary
  during Oct 23–24.

### Gaps
- No standard-mode Astra token-plus-meter report for Plus or Pro $500 was found in the window.

## 3. GPT-6 Luna and GPT-5.6 Luna (any tier)

### Takeaway
I found no new qualifying Luna report. The reports describe Luna as cheap on the meter, but none gives both token
counts and a meter delta.

### Cited findings
- **Plus, 6-Luna only (u/lervfo, r/codex, 2026-10-22).** "I use about 10-15% of my weekly every day with the plus plan.
  I only use 6-Luna". No tokens. — [Reddit comment](https://reddit.com/r/codex/comments/1xcpmtx/another_day_another_reset/19rhulexyhjk1/)
- **Plus, Luna 6 (u/ExoneratedPhoenix, 2026-10-12).** "around 6000 lines of code done in just a few days using just 9%
  of weekly use on my Plus plan". No tokens. — [Reddit 1x41y5h](https://reddit.com/r/codex/comments/1x41y5h/had_a_break_and_come_back/)
- **Plus → higher tier, Luna xhigh (u/totoer008, 2026-10-22).** "I am at 6B per day. Mostly Luna … when I was on plus I
  did 500M per day". Tier, meter and cache split are unknown. Computed only as a rough bound: at 97% cached, 500M
  GPT-6 Luna tokens a day is about $6–7/day. — [Reddit comment](https://reddit.com/r/codex/comments/1xcs47c/3569_million_tokens_in_6_days_on_chatgpt_plus_is/19rhxwndp0ry9/)
- **$100 plan, Luna (HN notatoad, 2026-10-07).** A 15k-ticket categorisation "used <10% of my 5hr limit on a $100 codex
  plan". No tokens. — [HN 49997155](https://news.ycombinator.com/item?id=49997155)
- **Pro (tier unstated), GPT-5.6 Luna Max as "mindless minion" with 6.1 Sol and Astra (u/ErwinWHeisenberg,
  2026-10-20).** Mixed workflow, no tokens. — [Reddit comment](https://reddit.com/r/codex/comments/1xadaw0/codex_used_to_supercharge_my_scientific_research/)
- **Background Luna calls.** Codex sends prewarm and title-generation requests "with gpt-6-luna at reasoning_effort:
  'low' regardless of what the picker says" (66680560, forum, 2026-10-05/06). Auto-review (Guardian) uses a Luna model
  and is "free" (VeitB, forum 2026-10-08; Ship 2.1). — [forum 1403393](https://community.openai.com/t/1403393/1);
  [forum 1403525/28](https://community.openai.com/t/1403525/28)

### Inferences
- These are qualitative signals of a large Luna allowance on Plus (≈7–10%+ of weekly per working day). They cannot be
  turned into $/week without token counts.
- Luna token totals in session logs can include background title and prewarm calls and free auto-review calls. Future
  qualifying reports should exclude those.

### Gaps
- No GPT-5.6 Luna token-plus-meter report at all in the window. The official Plus 5h table no longer lists GPT-5.6 Luna.

## 4. Official limits, credit rates and changes (2026-09-29 → 10-25); anomaly days

### Takeaway
The official pricing page publishes credit rates that equal the API list prices × 25, Plus/Business 5h
local-message ranges, "no five-hour limit" for Pro, and no weekly numbers. During the "28 days of shipping"
(from ≈Oct 6), OpenAI repeatedly reset meters and changed caching and long-context accounting. The Oct 16–17 drains
were later acknowledged by email as a bug and compensated with credits. I found no official note for Sep 26 or
Oct 22–24 beyond user reports.

### Cited findings
- Credit rates (standard speed, credits per 1M input / cached / output): GPT-6 Astra 250 / 25 / 1,250; GPT-6.1 Sol 50 /
  2.5 / 250; GPT-6 Luna 2.5 / 0.25 / 12.5; GPT-5.6 Luna 5 / 0.5 / 30. These equal the API list prices at 25 credits per
  $. — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing) (developers.openai.com/codex/pricing
  redirects here)
- Plus and standard Business local messages per 5h: GPT-6 Astra 5–45; GPT-6.1 Sol 15–160; GPT-6 Sol 15–150; GPT-6 Luna
  350–3,000; GPT-5.6 Luna not listed. "Weekly limits may also apply" (no weekly ranges). Pro plans are "$100, $200, or
  $500" and "Pro plans currently have no five-hour limit." The page has no Pro 200 grandfathering note and no
  last-updated date. — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing)
- Multipliers: Fast 2.5× on included usage, 2× on purchased credits; GPT-6 Astra and GPT-6.1 Sol Ultrafast 8× included,
  6× credits. — [learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing); OpenAI_Support confirms
  "Fast mode uses included subscription limits at 2.5x the Standard rate, while purchased credits … at 2x" (forum,
  2026-10-13) — [forum 1389168/4](https://community.openai.com/t/1389168/4)
- DevDay plan change, press quote: "$200 Pro subscribers will see their included usage decrease from 20x … down to
  10x"; "existing subscribers will keep their current limits for a time" (Engadget, quoted on HN 2026-09-29/10-01). —
  [HN 49897140](https://news.ycombinator.com/item?id=49897140); [HN 49923425](https://news.ycombinator.com/item?id=49923425)
- "28 days of shipping" (Thibault Sottiaux on X, tracked in forum thread 1403897 from 2026-10-06; the thread gives no
  calendar dates per day):
  - Day 1: default Astra/6.1 Sol speeds +≈50%.
  - Day 2: auto-review free.
  - Day 3: a banked reset for all paid accounts.
  - Global resets on Days 6, 8, 10, 13, 15, 17/18 and 20.
  - **Day 7: "Default context for GPT-6.1 Sol in Codex and Work rose from 272k to 500k … no long-context fees on
    subscription usage."**
  - **Day 12: "more effective usage through context reuse across subagents, longer caching, and better routing."**
  - **Day 16: cached context kept indefinitely.**
  - **Day 19: changing reasoning mid-conversation no longer invalidates the cache.**
  - Source: [forum 1403897](https://community.openai.com/t/1403897.json); e.g. [Day 7 on X](https://x.com/thsottiaux/status/2109430343346581527),
    [Day 12 on X](https://x.com/thsottiaux/status/2111244596131111253)
- Tibo poll (≈Oct 11) on "doubling weekly usage quotas in exchange for reinstating 5-hour limits" — [forum 1405254](https://community.openai.com/t/1405254/1)
- Oct 16 anomaly: u/ErwinWHeisenberg (2026-10-20): "I just received an email from OpenAI explaining that there was a
  bug affecting my usage allowance, and they're giving me $500 in credits as compensation". u/AerieIntelligent
  (2026-10-21): "On 16th of October my weekly usage went from 70% to full in one jump. I got mail with explanation and
  $500 worth of credits". A thread summary says "account changes around October 16 left some users with the wrong
  weekly allowance" and "Compensation ranged from 12,500 credits to $500 worth" (bot summary, not primary). —
  [Reddit 1xadaw0](https://reddit.com/r/codex/comments/1xadaw0/codex_used_to_supercharge_my_scientific_research/);
  [Reddit comment](https://reddit.com/r/codex/comments/1xay01g/well_at_least_they_are_admitting_it/19rfxo3nexby9/);
  [Reddit 1xaw2j5 summary](https://reddit.com/r/codex/comments/1xaw2j5/got_free_credits_as_compensation_for_usage_limit/19repksr9djz4/)
- Sep 26: "Since the September 26 Codex outage/recovery, I've noticed my Codex usage dropping much faster" (Tchatter,
  Pro $100, forum 2026-09-27). — [forum 1400938/4](https://community.openai.com/t/1400938/4)
- Oct 22–24: a cluster of fast-drain issues (#56672, #56618, #56634, #56669, #56890 "Project Import Consumed All My
  5-hours Token Limit") with no staff response on those pages; the Oct 24 #56669 title references "Tibo's reset". —
  [GitHub issue list](https://github.com/openai/codex/issues?q=is%3Aissue%20usage%20limit%20sort%3Acreated-desc)
- Oct 7–9 (not a listed anomaly day): a cache-miss pattern on Windows after the Oct 7 update (Pasto_Shouwa, above).
  OpenAI_Support (forum, 2026-10-08, irisa) noted `generate_memories = true` as a quota drain. —
  [forum 1383015/5](https://community.openai.com/t/1383015/5)

### Inferences
- Because the subscription waives long-context fees (Day 7), pricing subscription Sol usage above 272K at the
  long-context API rate would overstate the API-equivalent value after ≈Oct 13. Reports should be priced at
  short-context rates, or flagged.
- The caching changes on Days 12, 16 and 19 and the frequent global resets mean reports before and after ≈mid-October
  may belong to different accounting regimes. Weekly meter deltas that span a global reset are invalid.
- Oct 16–17 reports are explained by an acknowledged allowance bug (user-quoted emails, not an OpenAI public post) and
  should be excluded. Oct 22–24 reports remain unexplained officially.

### Gaps
- I did not reach the OpenAI status page or an official public incident note for Sep 8–9, Sep 26 or Oct 22–24. The
  Oct 16 bug is evidenced only by users quoting OpenAI emails.
- The pricing page gives no weekly allowance or official Pro multiple (10×, 20×, 25×). The "≈25× Plus" for Pro 500
  rests on press and user statements.

## Summary table: model × tier → qualifying reports (stage 1 + this stage), normalised $/week at API list

| Model | Tier | Qualifying reports ($/week, standard-equivalent unless noted) | ≥2 independent within 20%? |
|---|---|---|---|
| GPT-6.1 Sol | Plus | #51604 ≈$57 (stage 1); #51088 ambiguous (stage 1); NEW Pasto_Shouwa ≥$65.6 (lower bound, output missing, cache bug, Oct 8) | No (one firm, one lower bound; would be within 15% only if output were small) |
| GPT-6.1 Sol | Pro $100 | none | No |
| GPT-6.1 Sol | Pro $200 new 10× | none | No |
| GPT-6.1 Sol | Pro $200 grandfathered 20× | janrysavy ≈$569 / ≈$323 (stage 1, one user); sadiqmdasif ≈$105–130 (anomalous, stage 1); NEW DhAdaptive ≈$1,004 (full) / ≈$1,020 (Fast-only) standard-equivalent, i.e. ≈$402–408 in Fast, xhigh, Oct 8–9 | No |
| GPT-6.1 Sol | Pro $500 | NEW DhAdaptive ≈$964 (Fast-only, 5 pp) / ≈$919 (incl. Ultrafast, 7 pp) standard-equivalent, ≈$385 in Fast, Oct 9 | No (one user) |
| GPT-6 Astra | Plus | kamo-k ≈$15.5/5h (Sep 9 anomaly day); Crystal4276 ≈$2.5/5h (anomaly) | No |
| GPT-6 Astra | Pro $100 | YiwenPang ≈$318 (Oct 24 anomaly window); sentrybottale ≈$330–400; mrak- ≈$480 (Fast-equivalent) — all stage 1; no new | Only #56669 ($318) and #54995 low end (≤$382) are within 20%, and #56669 is on an anomaly day |
| GPT-6 Astra | Pro $200 grandfathered | genellect ≈$2,000 (Fast-equivalent, stage 1) | No |
| GPT-6 Astra | Pro $500 | totorofly ≈$1.5–2.6k (Fast-equivalent, stage 1); NEW #56634 no tokens | No |
| GPT-6 Luna | Plus | yoggypap ≈$6.5–7.5/5h (stage 1); HN mekpro ≥$100/month (stage 1); NEW lervfo, ExoneratedPhoenix: % only, no tokens | No |
| GPT-6 Luna | Pro tiers | none (notatoad: <10% of 5h on $100, no tokens) | No |
| GPT-5.6 Luna | Plus | tagorr ≈$4.9/5h (stage 1, Sep 8 anomaly day); Shekelphile ~$150/week (unverified, stage 1) | No |
| GPT-5.6 Luna | Pro tiers | none | No |

Net: stage 2 adds one strong qualifying source (DhAdaptive, GPT-6.1 Sol xhigh Fast on 20× and Pro 500) and one Plus
lower bound. No model × tier cell gains a second independent concordant report.
