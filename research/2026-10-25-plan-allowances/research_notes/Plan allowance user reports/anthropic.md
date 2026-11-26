# Plan allowance user reports: Anthropic Claude plans (Pro, Max 5x, Max 20x) × Opus / Sonnet / Haiku 5.5 (stage 2, 2026-10-25)

Scope: new end-user reports not already in `stage1-anthropic.md`, plus evidence that explains the discordant ones.
List prices used throughout (per 1M tokens): Opus 5.5 $4 in / $20 out / $0.20 cache read / $5 5-min write / $8 1-h write;
Sonnet 5.5 $2 / $10, cache read $0.20 then $0.10 from about 2026-10-08, writes $2.50 (5-min) / $4 (1-h); Haiku 5.5 $0.10 / $0.50 /
$0.01 for prompts up to 100K tokens, and $0.50 / $2.50 / $0.05 above 100K. Week normalisation: weekly $ = $ used ÷ (meter
fraction used). Monthly = weekly × 4.33 where needed. "(5m)" and "(1h)" mark the cache-write price assumption when a reporter
gave only "cache write".

Sources: GitHub was read via WebFetch. Reddit was read via the arctic-shift mirror (reddit.com is blocked); its index runs
to about 2026-10-24, and some threads are only partly indexed. X posts were not reachable directly.

## Q1. Sonnet 5.5 and Haiku 5.5: any user reporting API-equivalent dollars or typed tokens against a meter percentage?

### Takeaway
Still no model-pure qualifying report for Sonnet 5.5 or Haiku 5.5 on any tier. The best new evidence is indirect, and it
points against ValueRank's price-ratio assumption. One Max 20x user's meter fit (four accounts) finds that Sonnet 5.5 drains
the meter about 2× faster per list-price dollar than Opus 5.5, so Sonnet's API-priced allowance would be about half of
Opus's, not equal to it (wide CI, provisional, dated 2026-10-05). The Fei2411 "Sonnet/Haiku" rows are price-ratio
extrapolations, not measurements.

### Cited Findings
- **u/tomm3hshipp, Max 20x, week Sun 2026-10-04 → Fri 2026-10-09 midday (posted 2026-10-10), mixed Opus/Sonnet.** "90% of the
  weekly limit used, 5.17B tokens total". Opus 5.5: 1.3M input, 16.8M output, 2.14B cache read, 44.6M cache write → $1,125.
  Sonnet 5.5: 2.0M input, 29.2M output, 2.76B cache read, 89.3M cache write → $1,203. Other (Haiku etc.): $47. Total $2,375 (OTel,
  "Cost is what Claude Code reports at API list prices"). Opus high effort at first, then "sonnet 5.5 high". Both model totals
  close exactly at 1-h writes and a $0.20 Sonnet cache read (my check). The whole week normalises to **$2,639/week** (or
  ≈$2,330 if Sonnet cache reads are repriced at $0.10). It is mixed, about 51% Sonnet by dollars, so it is not a model-pure
  Sonnet report. — [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1x22re1/how_well_did_you_guys_pace_yourself_this_week/)
  - The author's follow-up links "https://3hship.com/blog/sonnet-5-5-week-usage-breakdown/" for a Sonnet-only week. That URL
    now serves an unrelated Christmas shop page (with embedded prompt-like text), so the data could not be retrieved. —
    [Reddit comment 2026-10-16](https://www.reddit.com/r/ClaudeAI/comments/1x22re1/)
- **Cadaverr / jonathanavis96 claude-usage-tracker (four Max accounts, analysis as of 2026-10-05).** This is a fitted meter rate
  per model family in "interactive-equivalent" units, as multiples of the Opus 5 rate: Opus 5.5 0.847 [0.711, 1.020] ("List is
  0.8x"); Sonnet 5.5 (provisional) 0.904 [0.682, 1.233] ("List is 0.4x Opus 5; 0.904x is 2.3x its list ratio"); Fable 2.954;
  older Sonnet 0.527. There is no Haiku 5.5 rate. — [rates-in-five-hour-unit.md](https://github.com/jonathanavis96/claude-usage-tracker/blob/main/docs/findings/2026-10-05-rates-in-five-hour-unit.md)
  - In the same author's fit, cache reads count for "0.00398 of an Opus input credit" in the headline run (list price is 0.05×
    input). On Reddit (2026-10-23) the author says: "a cache read counts for about 1% of a fresh input token in my fits, and each
    model has its own rate." — [PROOF.md](https://github.com/jonathanavis96/claude-usage-tracker/blob/main/docs/findings/2026-10-05-headless-repro/PROOF.md); [Reddit comment](https://www.reddit.com/r/ClaudeCode/comments/1xdk3cn/heads_up_headless_claude_p_eats_your_5hour_limit/19rjqian85tut/)
- **u/Pheidiase, 2026-10-22.** An orchestrator ran Sonnet 5.5 at medium/high effort: "one full 5 hour window used about 15-16% of
  the weekly quota", with "around 39-44 fixes" per window. There are no tokens or dollars, and the tier is not stated. —
  [Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1xcequa/follow_up_to_my_do_people_lie_about_claude_usage/)
- **u/watermelonsegar (2× Max 20x), 2026-10-10:** "Opus 5.5 Low for executions (Sonnet 5.5 tends to use more limits + is much slower
  than Opus 5.5 low)". Qualitative only. — [Reddit](https://www.reddit.com/r/ClaudeCode/comments/1x2duqm/i_upgraded_from_max_5x_to_max_20x_heres_what_30/pf1exy3/)
- **u/JackRabbit999 (Max 20x), 2026-10-22, opinion only:** about 15–20 h/week if only Fable, "maybe 30-50 if only on opus", and
  "maybe 100-120 hours if only on sonnet" (unconfirmed, all 5.5 at medium). — [Reddit r/Anthropic](https://www.reddit.com/r/Anthropic/comments/1xcacgy/claude_limits/19rhba21euzdw/)
- **Fei2411 `claude-haiku55-round1-2026-10-08.json`.** Every Sonnet 5.5 and Haiku 5.5 subscription row is "派生非实测"
  (derived, not measured): the Opus 5.5 pool times the price-blend ratio (Sonnet ×2.0 post-cut; Haiku ×19.53 with a 90/10 split
  across the ≤100K and >100K price bands). The file warns that if the pool weights depart from price ratios, "采用值须重推" (the
  adopted values must be re-derived). It also records the Sonnet 5.5 cache-read cut to $0.10 ("Cache hits and refreshes on
  Claude Opus 5.5 and Claude Sonnet 5.5 are priced at 0.05x the base input price") and Haiku 5.5's >100K price band. —
  [GitHub data file](https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-haiku55-round1-2026-10-08.json)
- **Issue #109 (IcyRyna, 2026-10-08):** "现在sonnet5.5缓存价格是0.1美元了" (Sonnet 5.5's cache price is now $0.10). There is no
  usage data. — [GitHub](https://github.com/Fei2411/real-api-pricing/issues/109)
- **Haiku 5.5:** u/howchie (Max, 2026-10-12) shows a /cost panel with "claude-haiku-5-5: 1.2k input, 28 output … ($0.0001)" next
  to Opus 5.5 at $6.20, which is useless for sizing. Issue #124 has nine Haiku calls ($0.99). No other Haiku meter data was
  found. — [Reddit r/Anthropic](https://www.reddit.com/r/Anthropic/comments/1x3rt3f/limits_inconsistency/)

### Inferences
- If Cadaverr's fit holds, Sonnet 5.5's API-priced weekly allowance is about 0.85/0.904 × 0.4/0.8 ≈ 0.47× Opus 5.5's per list
  dollar. The CI spans about 0.35–0.6×, and the fit predates the Sonnet cache-read cut, which lowers Sonnet's list $ further and
  so its allowance in list $. That is roughly $1.0–1.3k/week on Max 20x, not the ≈$2.0–2.6k the price-ratio assumption implies.
  This is one analyst and is not a qualifying report.
- tomm3hshipp's mixed week ($2,639/week at 90%) sits inside the Opus-only Max 20x cluster. A Sonnet meter rate 2× Opus's per
  list dollar would be hard to reconcile with that unless the Opus rate on that account was low. The two sources conflict
  mildly.

### Gaps
- No Sonnet-only or Haiku-only week (or 5-hour window) with dollars or typed tokens plus a meter delta, on any tier.
- The 3hship.com Sonnet-week write-up is unreachable (the domain is repurposed).
- No Haiku 5.5 meter weight has been published. Haiku's >100K-prompt price band (5× the base rate) makes list-$ normalisation
  depend on prompt length, which Claude Code main sessions usually exceed.

## Q2. Opus 5.5 Max 5x and Max 20x: further reports; why u/leaflavaplanetmoss (≈$1,140/week) and issue #124 (≈$1,266/week Pro) diverge

### Takeaway
New Max 20x reports split into two clusters. Pre-10-17 full or near-full weeks give $1.96k–2.86k/week (OmegaNetRob gives
$4.58k). A growing set of low readings ($1.0k–1.7k/week; daakkast, NicoAica, kakki-1, leolim031, and wokey's $1.64k median)
agrees with leaflavaplanetmoss's $1,140. Several users time-stamp a step change on about 2026-10-15/17. One user (NicoAica)
measured a 5× jump in meter use per token on 2026-10-17. The Pro outlier (#124) is not explained by cache weighting alone. Its
token totals are suspiciously close to a separate Team Premium screenshot.

### Cited Findings: Max 20x
- **u/Fancy_Leave7798, 2026-10-16** (Claude Code logs, deduplicated by message.id, list prices "with assumed cache-write rates",
  model not stated). The poster gives 20x: "2.8B tokens and $903 with 46% used, which implies a full week of about $1,960" →
  **$1,963/week**. — [Reddit r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1x7s2h4/max_20x_gave_me_about_13x_the_weekly_room_of_max/)
- **u/OmegaNetRob, 2026-10-16:** "I got $4580 for last week on a 20x plan using your prompt. I ran it to 100%." → **$4,580/week**.
  Model, effort and dedupe are unverified, and this is an outlier against everything else. — [Reddit comment](https://www.reddit.com/r/ClaudeCode/comments/1x7s2h4/_/ph6vsig/)
- **u/tomm3hshipp (see Q1):** mixed Opus/Sonnet, $2,375 at 90% → **$2,639/week** (2026-10-04..09).
- **u/PELORA-MARKETING, 2026-10-14:** "$200 Max plan … first two days of this week at about $2,000 at API rates, and we hit 70% of
  the weekly limit by Tuesday" → **≈$2,857/week**. The workload is mixed ("putting the simpler roles on Sonnet"). The quoted text
  reads like an AI-drafted reply ("Reddit is your call to post"). — [Reddit comment](https://www.reddit.com/r/ClaudeCode/comments/1wz3e35/_/pgm006k/)
- **u/BoboThePirate, 2026-10-22:** "fairly consistently like $2k+ per week of usage on x20". This is vague and has no meter
  figures. — [Reddit comment](https://www.reddit.com/r/Anthropic/comments/1xcacgy/claude_limits/19rgyhjjf8joh/)
- **u/daakkast, 2026-10-23** (Max 20x, Claude Code; the logs were priced by Claude): "Opus 5.5 launch week (w/c 22 Sep …): $4k+ of
  API-equivalent usage, never came near the weekly cap." "This week: reset Wed 7am, and I'm at 78% after ~$840. So the cap is now
  roughly $1k/week, about $10 per 1%." → **$1,077/week**. The workload is mixed ("Fable/Mythos halved", no ultracode). —
  [Reddit comment](https://www.reddit.com/r/ClaudeCode/comments/1xcwfob/semianalysis_claims_anthropic_is_ab_testing_usage/19rit8ed1txuq/)
- **@NicoAica, anthropics/claude-code #102667, 2026-10-17** (Max 20x, "Opus 5.5 only (2.1.302)"):
  - Oct 15 reset → Oct 17 08:00 CDT: 835M cache read, 40M cache write, 1.7M output, meter 0 → 31%. That is $401 (5m) to $521
    (1h) → **$1,294–1,681/week**.
  - Oct 17 08:00–17:53: 92M cache read, 2M write, 0.4M output, meter 31 → 51%. That is $36–42 → **$182–212/week**.
  - Quote: "roughly a 5× increase in quota consumed per token starting Oct 17". The user was also hit by the 5-min-write bug
    #101685. — [GitHub issue #102667](https://github.com/anthropics/claude-code/issues/102667)
- **SemiAnalysis, 2026-10-22** (as reported by cellcog.ai): two Max 20x accounts, Opus 5.5, same day. Weekly budget is 6,579M
  vs 5,266M tokens, and monthly API value is "$11,726 vs $9,385" → **≈$2,706 vs $2,166/week** (÷4.33). — [cellcog.ai summary](https://cellcog.ai/blog/claude-max-usage-limits-ab-test/); [FourWeekMBA](https://fourweekmba.com/ai-same-200-claude-plan-two-limits-one-gets-20-less-a-week/)
- **wokey.ai aggregate** (reseller with a commercial interest; all models; medians across accounts): Max 20x "$1,643 ($1,547–$1,751)"
  for the week of 10/12–10/19 (17 accounts), and "10-08 $1,727" → "10-12 $1,751", labelled "No change". — [wokey.ai](https://wokey.ai/claude-usage-limits)

### Cited Findings: Max 5x
- **u/Fancy_Leave7798, 2026-10-16:** "On 5x, a full week was about 3.4B tokens and $1,538" (the last full 5x week, 100% used,
  about 2026-10-09..16; model not stated) → **$1,538/week**. — [Reddit](https://www.reddit.com/r/ClaudeCode/comments/1x7s2h4/max_20x_gave_me_about_13x_the_weekly_room_of_max/)
- **@push42, #102667, 2026-10-20** (Max 5x, "I only use Opus 5.5 and Opus 4.8"): "5h 31% → 42% while weekly 74% → 76%, i.e. a full
  window ≈ 18% of the week". There are no dollars. — [GitHub](https://github.com/anthropics/claude-code/issues/102667)
- **u/emarkosov, 2026-10-10** (Max 5x, 30 days, "Mostly Opus 5.5"): "at least $1,900 of tokens … leaves out output and thinking …
  never the weekly limit". This is a lower bound with no meter figure, so it does not qualify. — [Reddit](https://www.reddit.com/r/ClaudeCode/comments/1x2duqm/i_upgraded_from_max_5x_to_max_20x_heres_what_30/)
- **Team Premium ($125, "5x more usage than standard seats"), X @leo114119, about 2026-10-05/06** (recorded by Fei2411): a full
  week of Opus 5.5 on a relay panel came to 4,029M cache read, 49.2M write, 13.4M output → $1,320.38 (5m). The tweet says "这个量和
  claude 5x max 几乎一致的" (this amount is almost the same as Claude Max 5x). The plan is not Max 5x, and the panel is not the
  official /usage. — [Fei2411 data file](https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-team-opus55-round1-2026-10-06.json)

### Cited Findings: Max tier unstated (likely relevant to the low cluster)
- **@kakki-1, #102667, 2026-10-24** ("Max", mostly Opus 5.5):
  - Sep 27: 129.3M cache read / 4.3M write / 0.2M output = week 5% → **$1,028–1,286/week**.
  - Oct 16–23: full week, "never blocked", 2,864M / 74.7M / 6.8M → $1,082–1,306 used (a lower bound on the cap).
  - Oct 24: 54.5M / 2.6M / 0.3M = week 4% → **$748–943/week** (integer rounding gives about $660–1,080).
  - Quote: "Today the meter implies a weekly cap of ~261M [weighted], i.e. ≤63% of what I used last week." —
    [GitHub](https://github.com/anthropics/claude-code/issues/102667)
- **@leolim031, #101937, 2026-10-14** (plan redacted, all Opus 5.5, 1-h writes): "Weekly meter looks unchanged … ~4M per 1%"
  (their weighting: cache read 0.1, write 1.25, output 5). Converting with their own 10:10–11:21 window ($18.4 list for 5.61M
  weighted) gives ≈$12/1% → **≈$1,200/week** (my conversion). They also report "the 5-hour session meter got much stricter around
  Oct 13". — [GitHub issue #101937](https://github.com/anthropics/claude-code/issues/101937)

### Cited Findings: Pro (Opus 5.5)
- **u/Planyy, 2026-10-15:** "roughly one 100% 5h session equals 10% of my weekly. and one 5h session is worth about $40-$50 (api
  equivalent)" with "90% opus 5.5" → **$400–500/week**. Weak, and the author is unsure ("could not tell really"). —
  [Reddit comment](https://www.reddit.com/r/ClaudeCode/comments/1x6p448/_/pgxgq8h/)
- **wokey.ai Pro median:** "$170 ($158–$182)" for the week of 10/12–10/19 (474 accounts, all models) and "10-08 $162". — [wokey.ai](https://wokey.ai/claude-usage-limits)
- **u/ScRdX_TCU, 2026-10-14:** "about $530 at API list prices in three weeks on a $20 Pro seat, and about 97% of the tokens were
  cache reads". There is no meter figure, so it does not qualify. — [Reddit comment](https://www.reddit.com/r/ClaudeAI/comments/1x61pdw/_/pgrzf6i/)
- **u/debian3, 2026-10-23, unsupported:** "In Febuary it was over $1000 API value on the $20 plan, now they are down to $200. A
  month ago it was still $400." — [Reddit comment](https://www.reddit.com/r/ClaudeCode/comments/1xcwfob/_/19rim25qfbkwx/)
- **u/Ok_Potential359 (Pro, Opus 5.5 high), 2026-10-16:** two prompts on a 400K-token session took the weekly meter to 14%. There
  are no dollars. — [Reddit](https://www.reddit.com/r/ClaudeCode/comments/1x7onzb/genuinely_i_dont_see_how_anyone_can_get_any_real/)

### Cited Findings: Issue #124 (Pro, $1,266/week) re-examined
- Issue body: "Window 2026-10-09 06:00 UTC → first 100% 2026-10-13 16:10 UTC", Opus 5.5 99.99%, 12,951 API rows. Cache read
  4,029.712 MTok ($805.94), 1-h write 30.219 ($241.75), output 10.474 ($209.49) → $1,266.15. "From 10% to 100% the increment
  averaged about $12.98 per point." The five-hour peak was 45%.
- Collaborator klarkxy merged it as research-only (PR #125, 2026-10-19) and verified the gist CSV: "1,670 rows, all `pro`", a
  monotonic seven-day series and matching timestamps. Tokens and prices could not be verified because they are not in the CSV.
- klarkxy's open hypotheses: "a Pro weekly allowance increase after 9/22, or … cache reads counting for less in the meter than in
  list price". — [GitHub issue #124](https://github.com/Fei2411/real-api-pricing/issues/124)

### Inferences
- **The leaflavaplanetmoss reading is no longer isolated.** daakkast ($1,077, 2026-10-22), NicoAica's pre-jump period
  ($1.3–1.7k, 2026-10-15..17), kakki-1 ($0.75–1.3k), leolim031 (≈$1.2k) and wokey's median ($1.64k) all sit at $1.0–1.7k/week.
  Pre-10-08 reports (Kanttz, Theo, Last_Lab, Delicious-Shower) and Fancy_Leave7798, tomm3hshipp and PELORA sit at $2.0–2.9k.
- **Candidate explanations, none confirmed by Anthropic:**
  1. **Per-account A/B arms.** SemiAnalysis reported a −20% weekly arm. That covers part of the gap but not a 2× one.
  2. **Metering changes.** Several users report an unannounced change around 10-13 (5-hour meter) and 10-15/17 (weekly meter):
     #101937, #102667, and r/ClaudeCode posts from 10-14 onward ("/usage has suddenly skyrocketed this week").
  3. **Cache-read weighting.** If the meter counts cache reads far below list price (Cadaverr: about 0.4–1% of input, against
     5% at list), then API-$ per meter point rises with the cache-read share of the dollars, and reports become
     workload-dependent rather than plan-dependent. That would push high-cache-read users up, not down. It cannot explain the
     low cluster, whose users are also about 97–99% cache reads.
  4. **Fable/Mythos in mixed weeks.** Fable is metered at about 3× Opus 5 per credit, so mixed weeks priced at list depress
     $/point. This applies to daakkast.
  5. **The 1h→5m cache-write bug (#101685, from about 10-12).** Rebuilds raise list $ and meter use roughly together. It is a
     composition shift, not obviously a $/point change.
- **Issue #124 is anomalous on three counts:**
  - Cache weighting does not reconcile it. Its non-cache-read dollars are about $460/week, against about $172/week for #52.
  - Its cache-read total (4,029.712 MTok) and row count (12,951) are within 0.02% and 1% of the separate Team Premium
    screenshot (4,028.79 MTok; 12,836 requests) that Fei2411 recorded on 2026-10-06.
  - That coincidence could be chance (both are "one full Opus week"), but it is worth flagging: possible mislabelling or
    reuse of numbers between sources. Its $/point also sits near the Team Premium week ($1,320).
  - If genuine, the remaining explanation is the collaborator's: Pro was raised after 9/22. Planyy's $400–500 and debian3's
    contrary "$200 now" claim leave this unresolved, and wokey's 474-account Pro median ($170) argues strongly against a Pro
    allowance of about $1.27k.
- **Max 5x vs 20x.** Fancy_Leave7798's 5x week ($1,538) is close to muscgab's cache-adjusted $1,040–1,150 and to the /usage
  screenshot ($1,920). It also implies 20x is only about 1.3× 5x in dollars for that user, consistent with "20x weekly ≈ 2× 5x"
  claims at best.

### Gaps
- No Anthropic statement explains the low cluster or the 10-15/17 step.
- OmegaNetRob's $4,580 is unexplained: no model mix or dedupe is given.
- No public token-by-type data exists for daakkast or leaflavaplanetmoss.
- kakki-1's and leolim031's tiers are unknown.
- The Spudguy post ("roughly $17.50 of API-priced work per 1% of my Max weekly limit", 2026-10-17, which would be ≈$1,750/week)
  has been removed. The mod bot summary says "Opus 4.8 Max", so it is unusable for 5.5. — [mod-bot log](https://www.reddit.com/r/ClaudeAI/comments/1x8637w/)

## Q3. Did Anthropic change limits, cache-read weighting or the weekly meter around 2026-10-08, or run A/B tests?

### Takeaway
No official announcement of a limit or meter change in October 2026 was found. Anthropic made only pricing and product changes
(Haiku 5.5 launch, the Sonnet 5.5 cache-read cut, an Agent SDK help-article update on 10-07). Users and trackers report three
things: a larger 5-hour window from about 10-09, a stricter 5-hour meter from about 10-13 on some accounts, and a sharp weekly
tightening from about 10-15/17 on some accounts. The "A/B test" claim comes from SemiAnalysis (10-22); Anthropic has not
commented.

### Cited Findings
- **Last official changes.** The 25% permanent weekly raise replaced the 50% promo on 09-14 ("this works out to a 17% reduction in
  weekly limits on Claude Code", per Anthropic via BleepingComputer). Five-hour limits were raised at the Opus 5.5 launch on
  09-22. wokey lists no official change after 2026-09-22. — [BleepingComputer](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/); [wokey.ai](https://wokey.ai/claude-usage-limits); [explainx timeline](https://explainx.ai/blog/claude-usage-limits-2026-timeline-explained)
- **Haiku 5.5 launched on 2026-10-07/08.** The Sonnet 5.5 cache read went to $0.10 on the pricing page; Fei2411 dates it to the
  Haiku launch because "官方表未标降价生效日" (the official price table gives no effective date). — [Fei2411 data file](https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-haiku55-round1-2026-10-08.json)
- **Agent SDK help article.** An "October 7 update" says `claude -p` and third-party apps can still use subscription limits.
  Max plans gained monthly API credits covering `claude -p` (7 Oct). — [Reddit summary of the help article](https://www.reddit.com/r/ClaudeCode/comments/1xbdj0k/october_2026_does_claude_p_consume_subscription/); [PROOF.md](https://github.com/jonathanavis96/claude-usage-tracker/blob/main/docs/findings/2026-10-05-headless-repro/PROOF.md)
- **Cadaverr (four Max 20x accounts, 2026-10-23):** "since about 9 Oct, the 5-hour window looks about 15% bigger, while the weekly
  limit has barely moved … you now hit the weekly cap after about 9% fewer of them … provisional". Headless `claude -p` moves the
  5-hour meter about 1.49× faster per weekly point. — [Reddit](https://www.reddit.com/r/ClaudeCode/comments/1xdk3cn/heads_up_headless_claude_p_eats_your_5hour_limit/)
- **leolim031 (#101937, 10-14):** "the 5-hour session meter got much stricter around Oct 13, while the weekly meter didn't change". —
  [GitHub](https://github.com/anthropics/claude-code/issues/101937)
- **#102667 (opened 10-16 by jihjun-ai):** a 5-hour window went from "approximately 10% of my weekly quota" to "approximately 15%".
  Comments from NicoAica (5× per token from 10-17), push42 (about 18% per window on 5x) and kakki-1 (cap ≤63% of the prior week)
  agree. "Support chat (Fin) says there's no human escalation for usage metering." No staff replies. — [GitHub](https://github.com/anthropics/claude-code/issues/102667)
- **The support bot, quoted by u/DeKamme (10-20):** "While we haven't made changes to how usage is calculated…" — [Reddit comment](https://www.reddit.com/r/ClaudeAI/comments/1x8bmku/_/19re3ljg8xd40/)
- **#101685 (opened 10-13):** from about 2026-10-12 18:18 UTC on some accounts (2.1.296–2.1.304), interactive sessions write 5-min
  cache despite requesting 1-h. The suspected cause is the "`cache-keepalive-2026-09-03` beta … switched on per account by a remote
  flag". The workaround is `"promptCacheTtl": "1h"`. No staff reply. — [GitHub](https://github.com/anthropics/claude-code/issues/101685)
- **Claude Code CHANGELOG (2.1.299–2.1.305, undated):**
  - New `/usage` warnings and a fix for "/usage … sometimes showing more than 100% used".
  - A warning that resuming an idle conversation would use "a noticeable share of your 5-hour usage limit".
  - `api_request` gained `cache_creation_5m_tokens` / `cache_creation_1h_tokens`.
  - No entry changes limits or weighting. — [CHANGELOG](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md)
- **SemiAnalysis (X, 10-22):** "We detected an A/B test going on that DECREASES your monthly API-value by ~20%" and "This only
  affects SOME accounts". The B arm has a +19% 5-hour window and a −20% weekly budget. As of 10-23 Anthropic had not commented. —
  [cellcog.ai](https://cellcog.ai/blog/claude-max-usage-limits-ab-test/); [Reddit thread](https://www.reddit.com/r/ClaudeCode/comments/1xcwfob/semianalysis_claims_anthropic_is_ab_testing_usage/)
- **wokey.ai:** the medians do not move between the weeks of 10-05 and 10-12 ("No change"). Their methodology note says a single
  outlier account does not move the median. — [wokey.ai](https://wokey.ai/claude-usage-limits)
- **Weekly ratio between tiers.** There is still no official statement. Claims of 20x ≈ 1.7–2.3× 5x come from an X post and a
  class-action filing (2026-08-31 article). — [promptblueprints](https://promptblueprints.tech/news-article/anthropic-max-plans-why-20x-may-mean-2x-weekly-usage/)

### Inferences
- The +19% five-hour / −20% weekly pattern of SemiAnalysis's B arm matches Cadaverr's "5-hour about 15% bigger since 9 Oct". It
  also fits users who say the 5-hour meter "barely moves" while the weekly meter drains (rethyria, 10-24). This suggests the
  10-09 change may be the A/B arm itself on some accounts.
- The 10-15/17 reports (5× on one account, ≤63% on another) are larger than a 20% arm. They could be a second, unannounced change
  or a metering fault. Reports cluster on accounts that also hit the 5-min-cache flag.
- Reports dated after 10-15 should be kept separate from the pre-10-08 cluster when testing agreement.

### Gaps
- No Anthropic staff statement was found on X, GitHub, the status page or the help center. The Max usage help article URL
  returned 404 at support.claude.com.
- SemiAnalysis's original X post and methodology are unreadable (paywall/X), so the figures above are second-hand.
- Whether the 10-17 step persists, or is limited to accounts in the keepalive/5m flag cohort, is untested.

## Q4. Published aggregates with per-model per-tier figures after 2026-10-08

### Takeaway
Fei2411 has added no new measured Anthropic rows since #124 (merged as research-only). Its Sonnet and Haiku rows are derived from
price ratios. wokey.ai publishes per-plan, all-model medians only. Neither gives measured Sonnet 5.5 or Haiku 5.5 figures.

### Cited Findings
- **Fei2411 `data/research` Claude files after 10-08:** `claude-haiku55-round1-2026-10-08.json` (derived Sonnet/Haiku rows),
  `list-prices-claude55-round1-2026-10-08.json` and `claude-pro-opus55-community-issue124-2026-10-18.json`.
  - Adopted values: Pro × Opus 5.5 = 30.54亿 tok/month (≈$320/week), Max 5x × Opus 5.5 = 183.34亿 (≈$1,920/week, from the 19%
    /usage screenshot), Max 20x × Opus 5.5 = 315.38亿 (≈$3,304/week, derived from MiaAI's window and Pro×10).
  - Derived values: Sonnet 5.5 = Opus × 2.0 and Haiku 5.5 = Opus × 19.53 in tokens. — [Fei2411 data/research](https://github.com/Fei2411/real-api-pricing/tree/main/data/research); [max5x round1](https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-max5x-opus55-round1-2026-10-03.json); [max20x round2](https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-opus55-max20x-round2-2026-09-30.json)
- **New Fei2411 issues after 10-08** (#131, #134, #139) are generic "Contribute evidence" templates or DeepSeek requests. The Claude
  ones are #109 (Sonnet price) and #111 (Haiku effort filter). — [issues list](https://github.com/Fei2411/real-api-pricing/issues)
- **wokey.ai (10-12..19):** Pro $170/week (474 accounts), Max 20x $1,643/week (17), Max 5x "Collecting (1 accounts; published at 5)".
  It says "Opus 5.5 uses about 0.6× the limit per token of other Opus and Fable models". It has no per-model dollars. —
  [wokey.ai](https://wokey.ai/claude-usage-limits)

### Inferences
- Fei2411's Max 20x adopted value (≈$3.3k/week) is above every direct Max 20x measurement except OmegaNetRob, because it is derived
  from Pro×10 and one 5-hour window. Direct full-week measurements cluster lower.

### Gaps
- There is no aggregate with per-model splits. wokey's Pro median mixes Sonnet and Opus (and claude.ai chat), so it cannot be
  assigned to Opus 5.5.

## Summary table: qualifying reports by model × tier (API-priced $/week; ≥2 within 20% means largest ≤ 1.20 × smallest)

Key: S1 = already in stage1; N = new here. Only reports with an exact model (or a stated dominant model), tier, date and
computable $/period are listed. Mixed-model and unstated-model reports are marked.

| Model × tier | Reports (normalised $/week) | ≥2 agree within 20%? |
|---|---|---|
| **Opus 5.5 · Pro** | S1 #52 $321 (09-22..27); S1 kanzakichiya ≈$302 (≈09-30); S1 hakanavgin ≈$261–285 (10-07); S1 r/ClaudeCode ≈$304 (≈09-24, weak); N Planyy $400–500 (10-15, weak, ~90% Opus); S1/N-reanalysed #124 $1,266 (10-09..13, anomalous) | **Yes.** #52 $321, kanzakichiya $302 and hakanavgin ≈$270 are within 1.19× (all pre-10-08). Planyy and #124 fall outside. |
| **Opus 5.5 · Max 5x** | S1 #98 $750–830 no-cache / ≈$1,040–1,150 cache-adjusted (10-03); S1 /usage screenshot ≈$1,920 (wk of 09-29, lower bound); N Fancy_Leave7798 $1,538 (≈10-09..16, model not stated) | **Weak/No.** Fancy $1,538 against the screenshot $1,920 is 1.25×, just outside. Fancy against #98's cache-adjusted $1,150 is 1.34×. No pair is within 20% unless #98's upper back-solve is stretched. |
| **Opus 5.5 · Max 20x (≤ 10-14)** | S1 Kanttz ≈$2,484–2,578 (10-02); S1 Theo $2,446–2,600 (10-08); S1 Last_Lab ≈$2,045 (09-27); S1 Delicious-Shower $2,175 (09-26); N Fancy_Leave7798 $1,963 (10-16, model not stated); N tomm3hshipp $2,639 (10-04..09, mixed ~49% Opus $); N PELORA ≈$2,857 (10-13/14, mixed, AI-drafted); S1 leaflavaplanetmoss ≈$1,140 (10-09); N OmegaNetRob $4,580 (≈10-09..16, model unstated); N SemiAnalysis A ≈$2,706 / B ≈$2,166 (10-22, second-hand) | **Yes.** Kanttz, Theo and Delicious-Shower are within 1.19×, and adding Last_Lab still holds ($2,045 → $2,446 is 1.20×). leaflavaplanetmoss and OmegaNetRob are outside. |
| **Opus 5.5 · Max 20x (≥ 10-15)** | N NicoAica $1,294–1,681 (10-15..17) then $182–212 (10-17 pm); N daakkast $1,077 (10-22/23, mixed with Fable); N wokey median $1,643 (10-12..19, all models, aggregate) | **Borderline.** daakkast $1,077 and leaflavaplanetmoss $1,140 are within 1.06×, but daakkast is mixed-model. NicoAica's low end $1,294 is within 1.20× of $1,077 (1.20×). There is evidence of a second, lower regime or an A/B arm. |
| **Opus 5.5 · Max (tier unstated)** | N kakki-1 $1,028–1,286 (09-27) / ≥$1,082–1,306 used (10-16..23) / $748–943 (10-24); N leolim031 ≈$1,200 (10-14, plan redacted) | Not assignable to a tier. |
| **Sonnet 5.5 · Pro / Max 5x / Max 20x** | None qualifying. tomm3hshipp Max 20x mixed week (Sonnet $1,203 of $2,375 at 90%); Pheidiase 15–16%/5h window (no $); Cadaverr fit says Sonnet ≈2.3× its list ratio (≈0.47× Opus's $ allowance, provisional) | **No.** |
| **Haiku 5.5 · all tiers** | None qualifying (howchie $0.0001 of Haiku; #124 nine calls) | **No.** |

Caveats for the table:
- Cache-write tier (5m vs 1h) moves totals by about 10–25% for write-heavy reports.
- Pre- and post-10-08 Sonnet prices differ by up to 2× on cache reads.
- Reporters' dedupe (message.id across resumed files) is often unstated, and duplicates inflate dollars 2–3× (ScRdX_TCU, Drasezv).
- Meter percentages are integers.
- Several reports mix Fable/Mythos, Sonnet or claude.ai chat into the same weekly meter.
