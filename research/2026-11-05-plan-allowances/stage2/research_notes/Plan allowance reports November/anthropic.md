# Anthropic Claude plan allowances: user reports for Opus 5.5, Sonnet 5.5 and Haiku 5.5 (stage 2, 2026-11-05)

Scope: verify stage 1 (`research/2026-11-05-plan-allowances/stage1-anthropic.md`) and extend it. Report window: measured
at least partly in 2026-10-02 .. 2026-11-01T06:10Z. Eligibility: `data/plan_cost_routes.json`
evidencePolicy.reportEligibilityProfile (O71 v1). Partition splits for Anthropic: Claude family at 2026-10-09 and
2026-10-17T13:00Z; Max 20x only at 2026-10-30 (rename to Ultra, five-hour limit removed). Max 5x and Pro have no split
at 10-30 (rename only). Opus 5.5 list prices used for researcher pricing (per 1M tokens): input $4, output $20, cache
read $0.20, 5-min write $5, 1-h write $8.

Method notes (for the writer):
- GitHub issue bodies came from the GitHub search API (`gh api search/issues`, verbatim). Comments came from WebFetch
  of the rendered issue pages (the fetch model was told to quote verbatim; the quotes below are as returned). The
  repo REST endpoints are not enabled for this session.
- X posts came from api.fxtwitter.com (verbatim text). jbdamask's table image (pbs.twimg.com) and deepfoundationdesign's
  Nov 1 screenshot (private-user-images.githubusercontent.com) were downloaded and read.
- HN came from the Algolia API (`search_by_date`, comments since 2026-10-20, 13 queries, 1,776 unique comments,
  filtered for "$" and "%").
- Reddit came from the Arctic Shift API (comment full-text search, r/ClaudeCode and r/ClaudeAI, 2026-10-20..11-05).
  Reddit itself was not read (login wall).

## Q1. Do the stage-1 candidates say exactly what stage 1 recorded?

### Takeaway
Yes for the three named candidates, with small corrections. jbdamask's figures are verbatim correct, but the post sums
"the previous 20 hours" of "last week" and gives no calendar dates. deepfoundationdesign's issue body matches exactly,
and two later comments add a 98% reading (Nov 1) with no tokens. Coriatel's comment matches, but the reset is
04:00 Asia/Jerusalem, which is 02:00Z (UTC+2 after Israel's DST end), not 01:00Z.

### Cited Findings

**jbdamask (X, Max 20x, weekly), verified**
- Post time: "Wed Oct 28 18:45:00 +0000 2026". Opening: "Last week my agent team burned 36% of my Max 20x weekly limit
  in less than 20 hours. At that pace the whole week's allowance would be gone in about 55 hours." —
  [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- Model: "My project used the typical agent orchestrator pattern with eight agents; all running Opus 5.5." —
  [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- Method: "I had Claude sum the previous 20 hours, counting each request once, and pricing at Opus 5.5 API rates (this
  is hand-wavy since my plan isn't billed per token, but API prices are the only ones published)." —
  [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- Meter restated: "my Claude usage showed that 36% was gone in under 20 hours; this is 1.8% an hour, which empties the
  tank in about 2.3 days." — [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- Table image (read from pbs.twimg.com/media/HVubFtyXUAA0TEz.jpg), titled "Token type | Tokens | API-dollar
  equivalent": "Cache reads 2,449M $490"; "Cache writes, new context 27M $136"; "Cache rebuilds after idle 35M $176";
  "Output and input 1.5M $29"; "Total 2,512.5M $831". —
  [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- Write price basis: the post says a rebuild "costs $5 per million tokens to rewrite", which is the 5-minute write
  price. 27M × $5 = $135 and 35M × $5 = $175 match the table. —
  [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- The post also says Claude Code subagents and spawned agents "default to 5 minutes" of cache idle time, and that 72
  rebuilds of "roughly 490K tokens" each came from teammates. —
  [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- The post quotes Wokey's aggregator figures ("Max 20x at about $1,643") and a Monte Carlo model. Those are context
  only. The 36% reading and the $831 are the reporter's own. —
  [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- Per-unit value: $831 / 0.36 = $2,308/week. With integer rounding (35.5–36.5%) the range is $2,277–2,341. Stage 1 is
  correct. — computed from [X / jbdamask](https://x.com/jbdamask/status/2115515191039545712)
- The same post is listed as High-confidence item 1 in the Fei2411 daily digest (aggregator; it adds no new data). —
  [Fei2411/real-api-pricing issues](https://github.com/Fei2411/real-api-pricing/issues/156)

**deepfoundationdesign (anthropics/claude-code #106322, Max 5x, weekly), verified**
- Created 2026-10-31T01:13:28Z. Title: "[BUG] Max 5x: weekly limit now reached every week since mid-October 2026 with an
  unchanged workload". — [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Environment: "Plan: Claude Max 5x, $100/month"; "Model: `claude-opus-5-5` for effectively all requests in the
  period below"; "Weekly reset: Wednesday 23:00 (CET)". —
  [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Meter: "Current week (reset Wed Oct 28, 23:00): 64% used after two working days. The dashboard warns: 'At this rate
  you will reach your limit tomorrow morning, before it resets on Wednesday.'" —
  [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Method: "I totalled the `usage` fields of every assistant response in `~/.claude/projects/**/*.jsonl` (deduplicated
  by message/request ID, subagent sessions included)." —
  [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Table row "Oct 28 → now | 7,089 | 5.9 M | 3.19 B | 24.2 M | 387 M | 64% after 2 days, warning shown". The columns are
  Requests, Output tokens, Cache read, Cache write, Weighted and Weekly limit. Uncached input is not given. —
  [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Earlier rows:
  - "Sep 30 → Oct 7 | 6,418 | 6.1 M | 3.46 B | 26.9 M | 427 M | no warning at all"
  - "Oct 7 → Oct 14 | 2,543 | 2.7 M | 0.97 B | 16.2 M | 141 M | no warning (light week)"
  - "Oct 14 → Oct 21 | — | ~4.4 M at the limit | — | — | ~230 M at the limit | reached ~Sun/Mon"
  - "Oct 21 → Oct 28 | — | ~5.3 M at the limit | — | — | ~433 M at the limit | reached ~Mon night, second account used
    afterwards"
  — [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Caveat stated by the reporter: "Usage of claude.ai (web/desktop chat) counts towards the same weekly limit but is not
  in these logs." — [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Researcher pricing:
  - Cache read: 3.19B × $0.20 = $638.00.
  - Cache write: 24.2M × $5 = $121.00 (5-min) or × $8 = $193.60 (1-h).
  - Output: 5.9M × $20 = $118.00.
  - Total $877.0–949.6. Divided by 0.635–0.645, that gives **$1,360–1,495/week**. Stage 1 is correct.
  - Input is missing, so the figure is a slight undercount, and claude.ai chat use (if any) is uncounted.
  — computed from [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- Window timing: Wed Oct 28 23:00 CET is 22:00Z (CET is UTC+1 after Oct 25). "After two working days" puts the reading at
  about Oct 30 evening, before the issue was filed at 10-31T01:13Z. The whole measurement is inside the report window. —
  [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- NEW, not in stage 1: two comments by the same author, both dated Nov 1, 2026.
  - The first is a screenshot only (German UI). It reads "Dein Verbrauch  Max"; "Aktuelle Sitzung … 4 % verwendet";
    "Diese Woche … Zurücksetzung am Mittwoch, 23:00 … 98 % verwendet"; "Hinweis: Bei diesem Tempo erreichst du dein
    Limit heute Nacht, bevor es am Mittwoch zurückgesetzt wird."
  - The second says: "It is Sunday afternoon, not even 6 PM, and I have already reached 98% of my weekly usage
    limit … I am programming as usual, using a single session, exclusively with Opus. I am not even using Fable … I am
    effectively receiving only around 4/7 of the usable weekly capacity I previously had."
  - No tokens are given for the 98% reading, so it cannot be priced. Sunday Nov 1 before 18:00 CET is after the cutoff.
  — [GitHub #106322](https://github.com/anthropics/claude-code/issues/106322)
- The same author also commented on #105240 (Nov 1): "In the last year I have never reached my weekly limit. Now from
  Wednesday to Sunday I reach it easily. So in 3.5 - 4 days." —
  [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240)

**Coriatel (anthropics/claude-code #106274, Ultra, weekly), verified with one time correction**
- Comment dated Nov 1, 2026 (as returned by the fetch): "Same here: Max 20x → Ultra (auto-migrated Oct 30), Claude Code
  only, 98% Opus 5.5. * Weekly reset Oct 31 04:00 Asia/Jerusalem → 38% used after 2,600 requests ($307 API-equivalent at
  Opus 5.5 list prices, measured with ccusage). * That implies ~$800 API-equivalent per week. * Oct 4–24 on Max 20x,
  same workflow: $1,900–2,300 API-equivalent per week (20k–24k requests per week), all within the weekly limit. * So a
  normal week now needs ~250% of the weekly limit." —
  [GitHub #106274](https://github.com/anthropics/claude-code/issues/106274)
- Per-unit value: $307 / 0.38 = $808. With rounding (37.5–38.5%) the range is $797–819. —
  computed from [GitHub #106274](https://github.com/anthropics/claude-code/issues/106274)
- Correction: 04:00 Asia/Jerusalem on Oct 31 is 02:00Z (Israel Standard Time is UTC+2 after the last Sunday of
  October), not 01:00Z. The end time of the reading is unknown (comment dated Nov 1), so it may extend past the
  06:10Z cutoff. It still starts inside the window. —
  [GitHub #106274](https://github.com/anthropics/claude-code/issues/106274)
- "Oct 4–24 … all within the weekly limit" has no meter fraction, so it is a lower bound only. It also spans the 10-09
  and 10-17 splits. — [GitHub #106274](https://github.com/anthropics/claude-code/issues/106274)

**Other stage-1 entries re-checked**
- tait143 (#106385, filed Oct 31). The fetch returned:
  - "Reporter: Tait Absher (Max plan)"
  - "Model: claude-opus-5-5"
  - "2026-10-29, 05:34-09:49 EDT (09:34-13:49 UTC)"
  - "List-price value: about $281"
  - "Share of weekly Max allowance: about 14% (7.7% last week + 6.3% this week); range 11-15%"
  - "Weekly limit reset: 2026-10-29 08:00 EDT (12:00Z), during the freeze"
  The tier is unstated, as stage 1 said. — [GitHub #106385](https://github.com/anthropics/claude-code/issues/106385)
- Thraetaona (#105240, Oct 29):
  - "Plan: Max 20x"; "Model: Opus 5.5 Xhigh (ultracode workflow)"
  - "I received my weekly quota Tuesday, Oct. 27. Barely a day later, on Oct. 28, I had exhausted 100% of my weekly
    usage!"
  - "23 threads; primarily Opus 5.5, very little Fable usage."
  - "19.5M input, 38.8M output, 113.9M cache-write, and approximately 4.9B cache-read tokens."
  This matches stage 1. It is mixed (some Fable). — [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240)
- lucthesloth (#105240, Oct 31), Max 5x: "Rest of each window is Sonnet 5.5 / Haiku 5.5, mostly subagents. Week totals:
  11,407 requests, 11.4M output, 58M cache write, 1.68B cache read." Mixed, weighted tokens only, no dollars. This
  matches stage 1. — [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240)
- WojtekVoy (#105240, Nov 2):
  - "on Claude Ultra (formerly Max 20x), primarily using Opus 5.5"
  - "My weekly usage indicator rose from approximately 2% in the morning to 99% by 13:16 Europe/Warsaw time."
  - For Nov 2, midnight–13:16: requests 1,373; output 0.75M; cache read 416.52M; cache write 7.41M.
  This matches stage 1 and is after the cutoff. — [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240)
- Eth66 (#105240, Nov 1): "Weekly window started Oct 31 ~18:00 UTC. As of Nov 1 22:40 UTC (~29h): 26% used, Claude Code
  100%." There are no tokens or dollars. This matches stage 1. —
  [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240)
- simon83 (HN 50286504, 2026-10-29T09:36Z): "I'm on the 20x Max plan and my quota is at 98% (resets today) … API
  equivalent spending for this week: $1,970 Hidden status-label calls: ~$380 Share of the true total: 16%". The model is
  unstated (he "showed Opus the gist" only to run the analysis). This matches stage 1. —
  [HN 50286504](https://news.ycombinator.com/item?id=50286504)
- sammysanchan (X, 2026-10-27T23:04Z):
  - "5h Window Evolution: Jumped from 76% (53% elapsed) to 99% (68% elapsed)"
  - "Weekly Window: Scaled from 10% to 27%"
  - "Total tokens nearly doubled from 80.5M ($54.16) to 156.1M tokens ($95.26)"
  The text gives no plan name. This matches stage 1. — [X / sammysanchan](https://x.com/sammysanchan/status/2115218215127208052)
- albrxt (X, 2026-10-27T22:23Z): "Claude Pro $20 5h limit on Opus 5.5 med consume 8% of weekly limit in 2h". There are
  no dollars or tokens. — [X / albrxt](https://x.com/albrxt/status/2115207720563519990)
- rbartoli (X, 2026-10-27T23:06Z): "On Max 5x, a 5-hour window held a median $155 before the limit hit." This is a
  multi-month median, not dated. — [X / rbartoli](https://x.com/rbartoli/status/2115218617071476827)
- BoboThePirate (r/ClaudeCode, 2026-11-02T23:52Z): "my last three weeks (Saturday reset, 8:00 AM), is that my usage when
  measured against several usage % measurements per week, equated to $2030 +- $30 … THIS weekly session, the first
  since the Ultra rebrand … I'll run out at about $1600 API equivalent. The prior 3 weeks that measured at $2030 had a
  mix of models, subagent usage, etc". Mixed, as stage 1 said. —
  [Reddit / BoboThePirate](https://www.reddit.com/r/ClaudeCode/comments/1xm1378/10_hours_after_the_ultra_plan_reset_and_now_at_50/19s1w4nvxshkx/)

### Inferences
- jbdamask stays an admitting report for Opus 5.5 × Max 20x × week. The timing is the weak point: "last week" plus
  "previous 20 hours" means a 20-hour span somewhere in about 10-19..10-27. That is inside P3 (10-17T13Z..10-30)
  whichever day it was, so the partition does not change.
- deepfoundationdesign stays an admitting report for Opus 5.5 × Max 5x × week (P3, researcher-priced, slight
  undercount). The Nov 1 98% reading adds no priceable data. The reporter's own weighted column (387M → "~600 M
  projected") gives the same proportion and is not an extra report.
- Coriatel stays borderline (98% Opus means mixed) and is in P4 (Ultra). The P4 start is 10-30 and the reading starts
  10-31T02:00Z.

### Gaps
- jbdamask gives no calendar dates and no per-category token split for "Output and input" (1.5M combined).
- deepfoundationdesign's 64% screenshot is referenced in the body but was not visible in the fetched page. Only the
  Nov 1 98% screenshot was recovered.
- Coriatel's exact reading time on Nov 1 is not given.

## Q2. Further reports that stage 1 missed

### Takeaway
About a dozen new items were found: mostly GitHub issue comments, plus a few Reddit and HN comments. None of them adds
a second admitting Opus 5.5 report to any partition inside the window. ruuurbag's Max 5x "$1300-$1400 per week" agrees
with deepfoundationdesign numerically, but it states no model and no meter fraction. The strongest new items are after the cutoff:
- ricardoraposo: controlled Max 20x/Ultra weekly runs on Opus 5.5 low, $20.6 per weekly point in the interactive arm,
  2026-11-03.
- smaug42: Pro, Opus 5.5, $32 = 3% of the week and 16% of the 5h window, 2026-11-02.
- douflou: "Max", Opus 5.5, about $40 per 3 weekly points and about $20.4 per 10 points of the 5h window, 2026-11-02/03.
Inside the window there is one near-miss. sergiokapone (Pro, 5h, Oct 27) gives $13–14 for a full 5-hour window, but the
model mix is about 93% Opus 5.5.

### Cited Findings

**Inside the window (new)**
- sergiokapone (#101937, comment Oct 27, 2026), Pro, 5h. Quotes:
  - "Adding a data point from a Pro plan (not Max)." "Plan: Claude Pro"
  - "Models: Opus 5.5 (main session), Haiku 4.5, 1 Sonnet 5.5 request"
  - "Window started ~13:30, the 5h limit reached 100% at ~15:07 (reset 18:29)"
  - "/usage at that moment: weekly limit only 10% (resets Nov 3)"
  - "Opus 5.5: 153 requests, ~97k output tokens, ~31M cache-read, ~1.2M cache-write"; "Haiku 4.5: 22 requests (~13k
    output total)"; "Sonnet 5.5: 1 request"
  - "API-equivalent cost of the whole window: roughly $13-14"
  - Comparison days: "23 Oct: ~$95 API-equivalent (Opus: ~876k output, ~308M cache-read)" and "24 Oct: ~$250
    API-equivalent (Opus: ~1.49M output, ~645M cache-read)". "Windows then lasted ~3.5 h before the limit; now ~1.5 h."
  - Times are Kyiv (UTC+2).
  — [GitHub #101937](https://github.com/anthropics/claude-code/issues/101937)
- Researcher check on sergiokapone: the Opus part alone prices at $1.94 (output) + $6.20 (read) + $6.00–9.60 (write) =
  $14.1–17.7. So the reporter's "$13-14" is at or below the 5-minute-write pricing. Haiku 4.5 is a small share (about
  13k output and 0.68M writes), and the 22 Haiku requests came from "sdk-ts" sessions he "did not start manually". —
  computed from [GitHub #101937](https://github.com/anthropics/claude-code/issues/101937)
- JCorners68 (#105621, comment Oct 30, 2026), tier unstated, 5h. Quotes:
  - "Linux CLI, Max, Opus 5.5."
  - "That one request consumed 26% of my session in under a minute."
  - "From my local transcript: 48 calls on Opus 5.5 over a context of about 156k tokens, roughly 5.07M cache-read
    tokens, 424k cache-creation tokens, 75k output tokens."
  Researcher-priced at $4.63–5.91, which gives ≈$17.5–23.2 per 5h. "Max" on Oct 30 is ambiguous: it was the day Max 5x
  was renamed "Max", and the comment uses neither name. So the tier is unstated or inferred. —
  [GitHub #105621](https://github.com/anthropics/claude-code/issues/105621)
- SandDanGlokta (#105162, comment Oct 26, 2026): "Upgrade to Max 20x on October 16, 2026 … I use only Opus 5.5; I do
  not use Fable … Current week (reset on Saturday at 11:00 p.m. CET): 32% of the weekly limit has already been used up
  after about 1.6 days, while the current session is at 51%". There are no tokens or dollars. The issue is about weekly
  limits "not recalculated after Max 5x → Max 20x upgrade", so this would be an anomaly in any case. —
  [GitHub #105162](https://github.com/anthropics/claude-code/issues/105162)
- sharkzamos (#105240, comment Oct 28, 2026): "Plan: Max 20x" "Model: Opus 5.5" "Starting around October 27, 2026,
  about 60% of my weekly limit was consumed in ~2 days with my normal workload." There are no tokens or dollars. —
  [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240)
- Gonzalitoms (#105621, Oct 29), Max 20x, Cowork: "Weekly usage went from ~60% on Wed Oct 28 to 97% on Thu Oct 29".
  There are no tokens or dollars and no model. — [GitHub #105621](https://github.com/anthropics/claude-code/issues/105621)
- maks-chipurnov (#102667, Oct 29): "Max x20 … 5 hour window never more than 25% (usually from 5-20) but already 70% of
  weekly limit at a middle of week". There is no model and no dollars. —
  [GitHub #102667](https://github.com/anthropics/claude-code/issues/102667)
- ggotye (#105162, body Oct 26), Max 20x after a mid-cycle upgrade: "Oct 18–25 | Max 20x | ~9.9M | Weekly meter at 88% on
  Tuesday Oct 20". It gives output tokens only, the "Opus share varied between 21% and 31%", and the weekly limit was not
  recalculated after the upgrade. It is unpriceable and an anomaly. —
  [GitHub #105162](https://github.com/anthropics/claude-code/issues/105162)
- UberMouse (HN 50299481, 2026-10-30): "Considering I use on average close to $3k a week at API prices on my 20x plan … Some
  weeks I've used >$3.5k". There is no meter fraction and no model, so it is a lower bound. —
  [HN 50299481](https://news.ycombinator.com/item?id=50299481)
- stymaar (HN 50341690, 2026-11-02): "the only time I maxed my $20 plan for a week I made the calculation that I had
  spend close to $200 in a single week". It is undated, with no model, and does not qualify. —
  [HN 50341690](https://news.ycombinator.com/item?id=50341690)
- ruuurbag (r/ClaudeAI, 2026-10-30T15:32Z), replying to Unlikely-Peace1268's Max 5x "$55 … 3–4%" comment: "That's roughly
  the usage I see. $55 for 4% extrapolates to $1375 per week, and I've seen $1300-$1400 per week for the past few weeks."
  The plan is implied by the thread. The model is unstated and no meter fraction is tied to his own dollars. —
  [Reddit / ruuurbag](https://www.reddit.com/r/ClaudeAI/comments/1xj7z30/are_limits_for_opus_55_on_pro_seemingly_increased/19rvx5vumchoh/)
- ruuurbag again (r/ClaudeAI, 2026-11-03T17:11Z): "On my $100 plan, I have been getting $1350-1400 API-equivalent usage
  per week for the month and change that I've had this plan, and am on pace for the same right now." Model unstated. It
  does not say the week was exhausted, so it is at most a lower bound. Numerically it agrees with deepfoundationdesign's
  $1,360–1,495. —
  [Reddit / ruuurbag](https://www.reddit.com/r/ClaudeAI/comments/1xmmmte/what_the_hel_is_happening_with_limits/19s36hkoqbk8y/)
- Old_Ad_6033 (r/ClaudeCode, 2026-11-02): "Multiply those nums by api pricing, and that's where the $1,000–1,100 comes
  from … I also build a tracker that measures usage % of the weekly (or 5h) limit in realtime". Plan and model are not in
  the comment. —
  [Reddit / Old_Ad_6033](https://www.reddit.com/r/ClaudeCode/comments/1xlrlj5/is_it_just_me_or_the_subscription_is_getting/19s0z2nhc16qs/)
- Mistuv (r/ClaudeAI, 2026-11-03): "last month my usage on the $100 tier was about $4500 in API costs with about another
  10-15% in total that I didn't get to spend before, the usage expired." Monthly, model unstated, loose meter tie. —
  [Reddit / Mistuv](https://www.reddit.com/r/ClaudeAI/comments/1xmmmte/what_the_hel_is_happening_with_limits/19s3b54e1ejwl/)
- badcookies (r/ClaudeCode, 2026-10-30), the same observer as stage 1 rows 7–9: "Roughly $11-12 API credit for the weekly
  / $1 paid. Max 20 was 10x Pro. Max 5 was 5x Pro". This is a cross-plan summary of his own post, not a new report. —
  [Reddit / badcookies](https://www.reddit.com/r/ClaudeCode/comments/1xjm3ah/max_plans_renamed_20x_is_now_ultra_no_more_5_hour/19rwbftiv4vaa/)
- Meter-only Reddit readings (no dollars or tokens):
  - thtanner (2026-10-27): "$200 max plan used 70% in a day vs ~10-15 prior".
  - MannToots (2026-10-27): "less than 15% of my weekly on a $20 account".
  — [Reddit / thtanner](https://www.reddit.com/r/ClaudeAI/comments/1xh3yyu/claude_code_usage_exploded_8x_today_anthropic/19rr09nq3fdfk/);
  [Reddit / MannToots](https://www.reddit.com/r/ClaudeAI/comments/1xh3yyu/claude_code_usage_exploded_8x_today_anthropic/19rr5o1ulrnic/)

**Entrypoint (interactive vs. SDK) changes the meter rate: a new caveat for any comparison**
- douflou (#106375, comment Nov 3, 2026): "Controlled measurement on a Max plan (2026-11-02/03, Claude Code 2.1.316,
  Opus 5.5, effort medium)". Table rows:
  - "1 | interactive TUI (`cli`) | $20.46 | 16 → 26 %"
  - "2 | `claude --no-session-persistence -p` (`sdk-cli`) | $19.83 | 26 → 45 %"
  - "3 | Agent SDK TS (`sdk-ts`) | $19.88 | 45 → 64 %"
  - "4 | interactive TUI (`cli`) | $20.38 | 64 → 74 %"
  - "6 | Agent SDK TS (`sdk-ts`) | $19.74 | 0 → 19 %"
  The percentages are the 5-hour meter. "Weekly utilization moved 3 points per path in total (about $40 of work
  each)." "non-interactive paths … consume the 5-hour limit about 1.95× faster than the interactive TUI." —
  [GitHub #106375](https://github.com/anthropics/claude-code/issues/106375)
- ricardoraposo (#97074, comment Nov 3, 2026):
  - Setup: "Max 20x, Linux, `claude-opus-5-5` at low effort, 2026-11-03. On this account the `five_hour` window no longer
    appears at all … so the weekly window is the only limit left."
  - Table: "Uncached (`DISABLE_PROMPT_CACHING=1`) … `sdk-ts` vs interactive TUI (`cli`) | 18 vs 15 | $15.6 vs $20.6 |
    1.32×"; "Cache on (mostly 1h writes) … `sdk-ts` vs custom label, both `claude -p` | 14 vs 14 | $27.15 vs $30.87 |
    1.14×". The column headers are "Points measured | $ per weekly point".
  - Method: "The arm switches each time the weekly meter ticks … So every segment is exactly one weekly point, and the
    meter's rounding does not blur it."
  - Pitfall: "When Opus's safety classifier stops a response … The stopped request is billed … but it has no assistant
    `message.usage` in the transcript … Summing `message.usage` undercounts those sessions by ~$2.3 each."
  — [GitHub #97074](https://github.com/anthropics/claude-code/issues/97074)
- ricardoraposo, passive October data (same comment): "Agent SDK (`sdk-ts`) traffic cost a median of $3.07 per 1% of
  the 5-hour window across 34 windows. That matches harry924's Max 20x `sdk-cli` figure ($3.2), against $8.1–8.5 for
  interactive use." The model is not stated for the passive data, and harry924's comment could not be retrieved (it is
  folded on the page). — [GitHub #97074](https://github.com/anthropics/claude-code/issues/97074)
- smaug42 (#105621, comment Nov 2, 2026):
  - "Claude Pro, Linux, Opus 5.5, unchanged workflow"
  - "ccusage (local logs) shows Claude token volume of ~$60–140/day API-equivalent Oct 12–21, rising to ~$180–270/day from
    Oct 25"
  - "Today (2.1.311), a single task of ~99M tokens ( approx $32 API-equivalent, 07:30–08:50 PT) used 16% of the 5-hour
    session and 3% of the weekly limit."
  — [GitHub #105621](https://github.com/anthropics/claude-code/issues/105621)
- betterCallHex (#106375, body Oct 31) quotes "Anthropic's Oct 28 public update" and says Anthropic "said it was rolling
  out fixes for smaller issues that made some sessions use tokens faster than intended". I found no primary Anthropic
  source for this (web search returned nothing dated Oct 28). —
  [GitHub #106375](https://github.com/anthropics/claude-code/issues/106375)
- Plan-definition signal from users, not Anthropic:
  - Eth66 (Nov 1): "Per the pricing page Ultra is 10x Pro weekly, vs 5x Pro on Max."
  - thisray (#105162, Nov 3) calls the plan "Ultra 10x ($200/month)".
  — [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240); [GitHub #105162](https://github.com/anthropics/claude-code/issues/105162)

**After the cutoff (measured wholly after 2026-11-01T06:10Z; not for this release)**

| Plan | Unit | Model | Observer | Date | Reading | Per unit |
|---|---|---|---|---|---|---|
| Ultra (ex-Max 20x) | week | Opus 5.5 low, single model, controlled | ricardoraposo [#97074](https://github.com/anthropics/claude-code/issues/97074) | 2026-11-03 | $ per weekly point: interactive `cli` uncached $20.6; `sdk-ts` uncached $15.6; cache-on `claude -p` $27.15 (sdk-ts) / $30.87 (custom label) | $1,560–3,087/week depending on entrypoint and caching; interactive uncached ≈$2,060 |
| Pro | week | Opus 5.5 | smaug42 [#105621](https://github.com/anthropics/claude-code/issues/105621) | 2026-11-02 07:30–08:50 PT | ≈$32 = 3% weekly | ≈$1,067 ($914–1,280 at 2.5–3.5%). Far above every earlier Pro report (≈$230–320), so treat as anomalous |
| Pro | 5h | Opus 5.5 | smaug42 | same | ≈$32 = 16% of 5h | ≈$200 ($194–206) per 5h |
| "Max" (Max 5x by the post-10-30 name; tier inferred) | week | Opus 5.5 medium | douflou [#106375](https://github.com/anthropics/claude-code/issues/106375) | 2026-11-02/03 | "Weekly utilization moved 3 points per path … about $40 of work each" | ≈$1,333 ($1,143–1,600) |
| "Max" (as above) | 5h | Opus 5.5 medium | douflou | same | interactive `cli` $20.46 → 10 points; $20.38 → 10 points | ≈$204 per 5h (interactive); about half that via SDK |
| Max (ex-Max 5x) | week | Opus 5.5 | deepfoundationdesign [#106322](https://github.com/anthropics/claude-code/issues/106322) | Nov 1 | 98% weekly, no tokens | — |
| Ultra | week | Opus 5.5 | WojtekVoy, z4k3ru, Eth66, BoboThePirate (see stage 1) | Nov 1–2 | as in stage 1 | as in stage 1 |

### Inferences
- The entrypoint effect matters for the O11 margin. Two independent controlled tests (douflou 1.95× on the 5h meter;
  ricardoraposo 1.14–1.32× on the weekly meter) show the same API dollars move the meter faster through `claude -p` or
  the Agent SDK than through the interactive TUI. A report from agent orchestration or headless runs can therefore
  understate the interactive allowance. Neither jbdamask nor deepfoundationdesign states the entrypoint.
- The transcript-priced undercounts now have three named sources:
  - hidden `agent_summary` calls (stage 1: 2–16%);
  - classifier-stopped retries ("~$2.3 each", ricardoraposo);
  - claude.ai chat use not in local logs (deepfoundationdesign).
- The post-cutoff readings disagree with each other by more than 2× on the same plan. Ultra ranges from Coriatel's ≈$808
  to ricardoraposo's ≈$2,060 interactive, and WojtekVoy's ≈$150 is anomalous. Pro: smaug42's ≈$1,067 is about 4× the
  Pro history. This suggests the metering was unstable around 10-28..11-03.

### Gaps
- Reddit coverage is partial. Arctic Shift rate-limited this session to about one query a minute.
  - Completed: comment searches over 2026-10-20..11-05 in 8-day slices for "ccusage", "API equivalent", "API price",
    "of my weekly" and "API cost", in r/ClaudeCode and r/ClaudeAI. That is 975 unique comments, filtered for "$" and "%".
  - Truncated: "of my weekly" hit the 100-result cap in every slice.
  - Failed: r/ClaudeAI "API cost" 10-20..10-28.
  - Not run: "Opus 5.5", "Ultra", "Sonnet 5.5" and "Haiku 5.5".
  - Stage 1 recorded "ccusage" as returning 0 hits. It returned 9–18 per slice in this session.
- harry924's Max 20x comment in #97074 (the "$8.1–8.5 for interactive use" per 1% of 5h) was not retrievable. The
  folded comments on the 68-comment page were not shown.
- No X search was possible. Only X posts linked from GitHub or Fei2411 digests were read.

## Q3. Per-cell O11 verdicts (model × plan × unit, per partition)

### Takeaway
No cell passes. The only cells with two non-provisional single-model admitting reports in one partition are unchanged
from stage 1: Opus 5.5 × Max 20x × week in P3 has jbdamask and NicoAica "after", and it fails by about 11×. Stage 2 adds
no second admitting report to any cell. Sonnet 5.5 and Haiku 5.5 still have zero single-model, meter-tied reports on
any tier.

### Cited Findings
- O11 test (O86): the largest lower bound must be ≤ 1.20 × the smallest upper bound across two independent
  non-provisional admitting reports. — `data/plan_cost_routes.json` evidencePolicy.reportEligibilityProfile

Opus 5.5 cells:

| Plan × unit | Partition | Admitting reports ($ range) | Near-misses (why excluded) | Verdict |
|---|---|---|---|---|
| Pro × week | P2 (10-09..10-17T13Z) | ganpei777 1,266 (recorded) | — | FAIL (1) |
| Pro × week | P3 (10-17T13Z..) | none | K45SLE 210–300 (provisional); sammysanchan ≈242 (tier unstated) | FAIL (0) |
| Pro × 5h | P3 | none | sergiokapone 13–14 (NEW; ≈93% Opus, so mixed); K45SLE 42 (provisional); Fast-and-Pythonic 42 (spans split, fit) | FAIL (0). Even if admitted, 42 > 1.2 × 14 = 16.8 |
| Max 5x × week | P1 (to 10-09) | muscgab 750–830; unlabelled /usage screenshot 1,920 (recorded) | — | FAIL: 1,920 > 1.2 × 830 = 996 |
| Max 5x × week | P3 (10-17T13Z.., open, no split at 10-30) | deepfoundationdesign 1,360–1,495 (verified) | badcookies 1,153–1,187 (98% Opus, weeks undated); douflou ≈1,143–1,600 (after cutoff, tier inferred) | FAIL (1). Note: badcookies would pass the margin (1,360 ≤ 1.2 × 1,187 = 1,424) if admitted, and douflou overlaps, but neither is admissible |
| Max 5x × 5h | any | none | JCorners68 17.5–23.2 (tier unstated or inferred); rbartoli (mixed, medians) | FAIL |
| Max 20x × week | P1 | Kanttz 2,484–2,920; leaflavaplanetmoss 1,140 (challenged); Theo 2,446–2,600 (recorded) | — | FAIL: 2,484 > 1.2 × 1,140 = 1,368 |
| Max 20x × week | P2 | NicoAica "before" 1,294–1,681 | — | FAIL (1) |
| Max 20x × week | P3 (10-17T13Z..10-30) | jbdamask 2,277–2,341 (verified); NicoAica "after" 182–212 (recorded) | simon83 ≈2,010 (model unstated); Thraetaona 2,403–2,745 (some Fable); badcookies 2,278–2,386 (97.6% Opus, undated) | FAIL: 2,277 > 1.2 × 212 = 254. Without NicoAica "after", only 1 admitting report remains |
| Max 20x × 5h | P2/P3 | none | simon83 ≈520 (model unstated); ricardoraposo October passive $3.07/1% sdk-ts (model unstated, SDK path) | FAIL |
| Ultra × week | P4 (from 10-30) | none admitting inside the window | Coriatel 797–819 (98% Opus); ricardoraposo 1,560–3,087 (after cutoff) | FAIL / no cell this release |

Sonnet 5.5 and Haiku 5.5: every plan × unit cell FAILS with 0 admitting reports. The only Sonnet 5.5 or Haiku 5.5 data
are derived fits (lambdita, Fast-and-Pythonic, perfektcrash; see stage 1) and mixed windows (lucthesloth, sergiokapone
with one Sonnet 5.5 request). — [GitHub #105240](https://github.com/anthropics/claude-code/issues/105240);
[GitHub #101937](https://github.com/anthropics/claude-code/issues/101937)

### Inferences
- The nearest any cell comes to passing is Opus 5.5 × Max 5x × week P3. deepfoundationdesign (1,360–1,495) sits within
  the margin of badcookies' Max 5x 1,153–1,187. badcookies is 98% Opus by dollars with undated weeks, so it fails the
  single-model rule and possibly the partition. A second clean Max 5x Opus-only week inside 10-17..11-01 would likely
  open this cell.
- In Max 20x P3, NicoAica "after" (182–212) is about 11× below both jbdamask and every other P3 Max 20x figure (≈2,000–2,700
  in the near-misses). It looks like a stuck-meter outlier. The writer may want to flag it rather than let it decide the
  cell. Even without it, the cell has only one admitting report.

### Gaps
- No Sonnet 5.5-only or Haiku 5.5-only meter-tied report exists in any venue searched (GitHub, HN, partial Reddit,
  linked X posts).
- Whether Anthropic's reported "Oct 28" fixes are a metering change (typed metering, so no split) or an
  accounting-fault event could not be confirmed from a primary source.
