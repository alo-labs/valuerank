# Stage 2 verification: plan-allowance reports for Gemini 4 Argon (Google AI Pro/Ultra), Kimi K3.1 Pro (USD and CN tiers), MiMo-V2.6-Pro/Flash (Token Plan) and MiniMax-M3.1-Flash (M Plan / coding plan), report window 2026-10-02 to 2026-11-01T06:10Z

Run 2026-11-05. This run verifies `research/2026-11-05-plan-allowances/stage1-others.md` against primary sources and extends it. Rules applied: O71 v1 profile (`data/plan_cost_routes.json` → `evidencePolicy.reportEligibilityProfile`).

- O11 margin: a cell passes when it has at least 2 independent, non-provisional, non-derived reports, and the largest lower bound is at most 1.20 × the smallest upper bound across every eligible report in the cell. Provisional reports stay in the range test.
- Dollar figures are my own arithmetic at the API list prices stage 1 used, unless the text says the reporter gave them:
  - Argon: $2 input / $0.10 cache / $10 output per 1M.
  - K3.1 Pro: $2 / $0.20 / $10.
- Where a source leaves the token split open, the range runs from all uncached tokens as input (low) to all uncached tokens as output (high).

Sources and access:
- Google AI forum: `/raw/<id>`. JSON was rate-limited.
- Reddit: Arctic Shift API.
- locdd.com: topic JSON. This is the LINUX DO mirror.
- LINUX DO 3071240: a JSON copy cached in the session scratchpad on 2026-10-25, because linux.do returns 403. The original is https://linux.do/t/topic/3071240.
- Hacker News: Algolia.
- V2EX: sov2ex search plus the V2EX v1 API.

## Q1. Does each qualifying or near-qualifying stage-1 candidate say exactly what stage 1 recorded?

### Takeaway
Stage 1's figures are faithful to the sources, with two corrections:
1. jamie950315's Reddit post states its tier explicitly ("Ultra 5x, Antigravity 2.26.0, Argon Medium, 2026-10-26"). The archive copy was taken 27 seconds after posting and is unedited. So his weekly report is **not provisional on tier grounds**, as stage 1 had it.
2. His "~$150 per five-hour window" is **derived** from his weekly calibration. He measured only weekly deltas, so it must not count as a 5-hour reading.

The Kimi Allegretto quotes (K1, K2, K3, K4, K5) are verbatim-correct. K1's screenshot confirms the numbers. K5's tier rests on a separate post whose author cannot be linked to the #7 author, so K5 should be **provisional**.

### Cited Findings

**G1: Yiji_Kong, Google AI forum t/196351 #1 (verified)**
- Setup quote: "I ran a controlled A/B test in Google Antigravity (2.27.0, Ultra 5x, Windows) comparing how much of the shared 5-hour Gemini quota bucket a single, comparable request consumes on **Gemini 4 Argon (High)** vs **Gemini 3.8 Flash (High)**." — [Google AI forum t/196351 #1](https://discuss.ai.google.dev/t/196351/1)
- Dates: the raw view stamps the post 2026-10-28 04:03:48 UTC; the search index gives the topic creation as 2026-10-28T02:23:46Z.
- Method quote: "Quota: `quotaInfo.remainingFraction` from the local language server RPC `LanguageServerService/GetUserStatus`, polled every 30 s. Argon and Flash share the same bucket (identical fraction and `resetTime`)." Tokens come "from `GetCascadeTrajectoryGeneratorMetadata` (`inputTokens`, `cacheReadTokens`, `outputTokens`)". — [t/196351 #1](https://discuss.ai.google.dev/t/196351/1)
- Clean A/B row: "Gemini 4 Argon (High) | 14,918 / 4,233 | 0.00144340 | 0.0722 USD (2 / 10)".
  - My check: $0.072166 / 0.0014434 = **$50.0 per 5-hour window** at list. — [t/196351 #1](https://discuss.ai.google.dev/t/196351/1)
- 42-step session quote: "A separate 42-step Argon session (220,998 input / 3,948,273 cache-read / 71,432 output tokens, quota drop 0.03154810) gives an implied bucket of ~147.5 USD at 6 / 0.30 / 30."
  - My check at list ($2 / $0.10 / $10): $0.4420 + $0.3948 + $0.7143 = $1.5511, and $1.5511 / 0.0315481 = **$49.2 per 5h**. — [t/196351 #1](https://discuss.ai.google.dev/t/196351/1)
- Reporter's own framing: "Argon consumes exactly 3.0x more quota per dollar than Flash … the implied bucket size is ~150 USD, and Argon's consumption matches 6.00 / 30.00 USD per 1M input/output tokens". — [t/196351 #1](https://discuss.ai.google.dev/t/196351/1)
- Caveats the reporter gives: "n = 1 per model for the clean A/B"; "`remainingFraction` occasionally rises by about 0.0028 … with no change to `resetTime`"; "Context compaction model calls do not appear in the trajectory token metadata". — [t/196351 #1](https://discuss.ai.google.dev/t/196351/1)

**G3: Yiji_Kong, t/196351 #5, 2026-10-29 07:37 UTC (Gemini web app; verified)**
- Same subscription ("under the same Google AI Ultra subscription"). The `/usage` response gives "the exact 8-decimal float `percentageUsed` for the **Weekly pool** (alongside the 2-decimal **5-Hourly pool**, where **1 Weekly Pool = 20 × 5-Hourly Pool**)". — [t/196351 #5](https://discuss.ai.google.dev/t/196351/5)
- Test 1B row: "Gemini 4 Argon (Low) | `51,262` chars (Perm B) in / `"OK"` (`2`c) out | `0.10 → 0.12` (+0.02) | `0.09987733 → 0.10078641` | +0.00090908". The input is described as "~13,500 tokens", an estimate from character count.
  - My check: about $0.0270 / 0.00090908 = **$29.7 per week**.
  - Net of the 1C overhead (+0.00015849): $0.027 / 0.00075059 = **$36.0 per week**.
  - 5-hourly reading +0.02 on 2-decimal rounding: $1.08–1.80 per 5h. — [t/196351 #5](https://discuss.ai.google.dev/t/196351/5)
- The test 2B row (Argon High, a 4,284-word article) gives words, not tokens, so it cannot be priced. — [t/196351 #5](https://discuss.ai.google.dev/t/196351/5)

**Context posts in t/196351 (no figures)**
- Google staff reply, Maniraj_Chervirala #6, 10-29: "5-hour and weekly subscription limits reflect available capacity, model compute, and total agent work rather than matching API token list prices … Fixed per-model quota multipliers are not published because subscription limits adjust dynamically with system capacity." — [t/196351 #6](https://discuss.ai.google.dev/t/196351/6)
- shuai_guo #4 (10-29) is on "Google AI Ultra (5x)". He describes "~3x over its published API token pricing ratio" and gives no tokens or meter numbers, so he is not a report. — [t/196351 #4](https://discuss.ai.google.dev/t/196351/4)

**G2: jamie950315, r/google_antigravity 1xfnvds (verified; stage 1 corrected)**
- Created 2026-10-26T05:03:45Z. Arctic Shift retrieved it at 05:04:12Z with `edited: false`. — [Arctic Shift record](https://arctic-shift.photon-reddit.com/api/posts/ids?ids=1xfnvds); [Reddit 1xfnvds](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/)
- Tier and setup are stated verbatim on the closing line: "Ultra 5x, Antigravity 2.26.0, Argon Medium, 2026-10-26." The opening says "On Google AI Ultra, Gemini 4 Argon draws from Antigravity's shared Gemini usage at $6.00 input / $30.00 output / $0.30 cache-read per 1M tokens". — [Reddit 1xfnvds](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/)
- Argon probe table, labelled "Weekly delta":
  - "15,683 | 0 | 5 | 0.00015703"
  - "16,088 | 0 | 25,193 | 0.00142053"
  - "41,355 | 0 | 14 | 0.00041420"
  - "2,136 | 39,306 | 14 | 0.00004174"
  - My check at list: $200.06 / $200.00 / $200.03 / $199.87 → **$199.9–200.1 per week**, or about $866 per month at 52/12. — [Reddit 1xfnvds](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/)
- His 5-hour figure is derived. The quote: "Both land on the card exactly … That fixes the bucket at **~$600 weekly, ~$150 per five-hour window**". It follows from a Flash calibration of *weekly* deltas, and no 5-hour meter reading appears in the post. — [Reddit 1xfnvds](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/)
- Thinking tokens are included. His comment: "The meter's output field already includes thinking — `.9` is a subset of `.3` … So the $6/$30 covers everything you're billed for, thinking included." — [comment 19ro4f1jzlly9](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/comment/19ro4f1jzlly9/)
- The same text was cross-posted 23 s later to r/AntigravityGoogle (1xfnvml). This is one observer, not two. — [Arctic Shift author listing](https://arctic-shift.photon-reddit.com/api/posts/search?author=jamie950315&limit=100)
- Replies, none with own figures:
  - Ok_Noise_9883 (10-26 05:28Z): "I just verified it on my machine, seems like truth".
  - Seikojin: "in my testing, Argon uses its quota aggressively". — [Reddit 1xfnvds comments](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/)

**G4: ubelai (verified as mixed-model)**
- Quote: "I'm on the **x20** plan … sitting at **64% remaining** (`0.6384909` …) barely two and a half days into my weekly reset (`2026-10-23T22:53:16Z`)". His table mixes Argon and Flash 3.8 rows, so it counts at plan level only. — [comment 19robavwvb5us](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/comment/19robavwvb5us/)

**K1: SunnyDoll (locdd pseudonym), locdd 103915 #1 (verified)**
- Quote: "老套餐199，claude desktop使用，纯3.1pro。 这是用完一个5H的用量，周限是5个5H，3.1pro应该是等价400元的额度。" Mirror timestamp 2026-10-26 06:24Z. — [locdd 103915](https://www.locdd.com/t/topic/103915)
- The screenshot shows:
  - "总成本 ¥79.60", "总请求数 221", "真实消耗 Tokens 31.9M", "缓存命中率 95.4%"
  - model row "k3.1-pro | 166 | ¥79.60 | 31.9M | 100%"
  - hourly bars at 10:00, 12:00, 13:00 and 14:00, in a "当天" (today) view
  - [image](https://oss.locdd.com/2026/10/26/1792995863061.png)
- My check: cache 30.43M × $0.20 = $6.09, plus 1.47M uncached at $2–10 = $2.94–14.67 → **$9.0–20.8 per 5h**. It matches stage 1.
- Note that the screenshot is a calendar-day view, not a window view. The bars all fall within 10:00–14:59, which is consistent with one 5-hour window.

**K2: PaperPlane, locdd 103915 #6 (verified)**
- Quote: "我早上测 5h 大概 100M ，老 199 ，缓存率 98.5% 差不多， K3.1 Pro". — [locdd 103915](https://www.locdd.com/t/topic/103915)
- My check: $19.70 + $3.0–15.0 = **$22.7–34.7**.
- It is approximate ("大概", "差不多"). The morning of 10-26 CST may overlap the 10-26 reset; see Q3.

**K3: StarryWalker, locdd 103792 #12 (verified)**
- Quote: "我有个199的老套餐,98.x的缓存命中,现在5小时大概能跑7000万,一周就是3.5亿". — [locdd 103792](https://www.locdd.com/t/topic/103792)
- This is a capacity estimate, not a stated exhaustion. The weekly figure is derived as 5 × 5h.
- My check: **$15.3–27.7 per 5h**.

**K4: TimeMachine, locdd 104222 #4 (verified)**
- Quote: "老 199 套餐，这周只用了 3.1，做了俩项目，目前消耗 token 72M，周限用量 33% 总的缓存率大概 90~95% 左右". — [locdd 104222](https://www.locdd.com/t/topic/104222)
- My check: consumed $20.9–85.0, giving **$62–261 per week** across 32.5–33.5% rounding. Stage 1 had $63–260, essentially the same.
- It is not known whether "这周" (this week) started before or after the 10-26 weekly reset.

**K5: SunnyDoll then KiteRunner, locdd 104985 #7–#8 (verified; tier provisional)**
- #7: "现在如果是老套餐，k3.1pro额度其实也挺够的了。今天我5h额度跑完，99.2的缓存命中，跑了1.5亿". #8: "补充下，我是老的199套餐". — [locdd 104985](https://www.locdd.com/t/topic/104985)
- My check: $29.76 + $2.4–12.0 = **$32.2–41.8 per 5h**.
- On locdd, one person's posts carry different pseudonyms (see Q2). So #8 is not demonstrably the #7 author, and the tier is an inference.

**K8: MoonPostman, locdd 103774 (not re-fetched this run)**
- Stage 1's reading ($185–191/week, Allegro ¥699) spans the 10-24 split per stage 1. — [locdd 103774](https://www.locdd.com/t/topic/103774)

### Inferences
- G1 is a clean qualifying report for Ultra 5x · Argon · 5h (Antigravity), non-provisional, with two readings, at **$49.2–50.0**.
- G2 should be re-tagged **non-provisional** for Ultra 5x · Argon · week (Antigravity), at **$199.9–200.1**. Its "$150/5h" (≈$50/5h at list) is a derived figure and does not enter the 5-hour cell.
- G1 (5h) and G2 (week) imply week ≈ 4 × 5h for Antigravity Ultra 5x. That matches jamie's own "$600 weekly, $150 per five-hour" framing. By O82 it is a cross-check only, and no conversion is allowed.
- The Gemini web app is a different meter. Its Argon cost per weekly fraction is about 6× lower in dollars than Antigravity's ($30–36 vs $200/week). The two should not be pooled. Even if they were, the cell would fail (199.9 > 1.2 × 36.0).
- K5 should be marked **provisional** because its tier is inferred. Under the profile, provisional reports stay in the range test.

### Gaps
- Yiji_Kong's G1 lists no window start or end times, and only two readings were taken.
- K1–K5 original LINUX DO usernames and post times could not be checked, because linux.do returns 403. locdd timestamps are crawl times (see Q2).

## Q2. Are locdd 103607 and LINUX DO 3071240 the same post, making moondrinker-allegretto and astralyn-allegretto one observer? Is Yiji_Kong the same person as jamie950315?

### Takeaway
locdd 103607 **is** a mirror of LINUX DO 3071240: the title is identical and the posts follow in the same order. `moondrinker-allegretto` and `astralyn-allegretto` are therefore **the same observer (Astralyn) and the same thread**. Both are derived, so neither could admit a cell anyway. The mirror also shows that locdd pseudonyms are reassigned per post, so locdd pseudonyms carry no identity information.

Yiji_Kong and jamie950315 **cannot be shown to be the same person**. Their setups differ: Windows vs macOS, Antigravity 2.27.0 vs 2.26.0, different RPC methods and token sources, and 5-hour vs weekly meters. They do share the conclusion and the "~$150 per 5h" framing. They fall in different cells, so the question does not affect any O11 verdict.

### Cited Findings

**The mirror match**
- Both topics carry the title "Kimi Allegretto K3.1 Pro 额度实测，订阅中 K3.1 Pro 价格约为 K3 订阅价格的 85%".
  - LINUX DO OP: Astralyn, 2026-10-25T01:53:12Z.
  - locdd OP: "MoonDrinker", stamped 2026-10-25T02:20:42Z.
  - Both OPs give the same method ("在 Pi 中接入 K3.1 Pro 进行开发 … 扣费点数 = x·Input + y·Output + z·CacheRead"). — [locdd 103607](https://www.locdd.com/t/topic/103607); [LINUX DO 3071240](https://linux.do/t/topic/3071240)
- Post-by-post mapping (locdd pseudonym → LINUX DO user), verbatim-identical bodies:

  | locdd post | LINUX DO post | Body |
  |---|---|---|
  | #8 CloudWalker | #9 fenglinnet | "之前我的199老套餐一周也就顶多200M，刚才试了k3.1 pro，43M消耗周额度9%，不过我缓存率估计的98%以上了。" |
  | #9 StarryWalker | #10 hanashiro | "昨晚上 Moonshot 已经暗改过一次了 …" |
  | #10 Dev_Leo | #11 choulei (2026-10-25T03:44:41Z, with image) | "刚才实测5h的额度是10美元。全程用3.1pro，价格按照官方定价设置。" |
  | #16 MoonDrinker | #17 Astralyn | "计算出应该是 12.7% 周额度（63.5% 5H 额度）" |
  | #17 SunnyDoll | #18 Astralyn | the "改动前 / 改动后" coefficient table |
  | #12 WindTraveler | #13 Astralyn | (Astralyn) |
  | #19 RainPoet | #20 Astralyn | (Astralyn) |

  — [locdd 103607](https://www.locdd.com/t/topic/103607); [LINUX DO 3071240](https://linux.do/t/topic/3071240)
- Pseudonyms are inconsistent in both directions:
  - One LINUX DO user (Astralyn) appears on locdd as MoonDrinker, WindTraveler, SunnyDoll and RainPoet.
  - One locdd pseudonym ("Dev_Leo") stands for jackliu100 (#6), choulei (#11) and ayoka (#16). — same sources
- locdd timestamps are crawl times. Locdd #2–#12 are all stamped 04:28:10–04:28:59Z, while the originals run from 01:55Z to 03:49Z. — same sources
- The recorded `choulei-legacy` report (URL null in `plan_reports.json`) can be given the URL https://linux.do/t/topic/3071240/11. The post is dated 2026-10-25T03:44:41Z and states no tier. — [LINUX DO 3071240](https://linux.do/t/topic/3071240)

**Yiji_Kong vs jamie950315**
- Yiji_Kong's forum profile shows the display name "Edmund Kong", an account created 2026-07-21, and a Windows setup ("Google Antigravity (2.27.0, Ultra 5x, Windows)"). His method uses "`LanguageServerService/GetUserStatus`" and "`GetCascadeTrajectoryGeneratorMetadata`". — [forum profile](https://discuss.ai.google.dev/u/Yiji_Kong); [t/196351](https://discuss.ai.google.dev/t/196351/1)
- jamie950315's repro is macOS-specific: "pgrep -f 'Resources/bin/language_server'", `lsof`, and "sqlite3 ~/.gemini/antigravity/conversations/<id>.db". He uses the method "`RetrieveUserQuo*taSummary`" and states "Antigravity 2.26.0". His Reddit history runs from 2021 and includes Mac and iOS posts (r/MacOSBeta, r/MacOS: "i got my m4 MacBook air"). — [Reddit 1xfnvds](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/); [author listing](https://arctic-shift.photon-reddit.com/api/comments/search?author=jamie950315&limit=100)
- Yiji_Kong's posts do not cite jamie950315's earlier post. — [t/196351](https://discuss.ai.google.dev/t/196351)

### Inferences
- `moondrinker-allegretto` (week $48.6, derived) and `astralyn-allegretto` (week $55.9, derived) are the same observer: one report at most, carrying the $48.6–55.9 range. Both are derived, so neither can be an admitting report.
- Because locdd pseudonyms are reassigned per post, **no locdd pseudonym can establish independence or identity**. Two locdd candidates may be one LINUX DO user, and one pseudonym may cover different users. This affects:
  - K1 vs K5: both "SunnyDoll", which is no evidence they are the same person.
  - The independence of any locdd candidate from LINUX DO-sourced recorded reports such as fcten.
- A different OS, client version, RPC and meter make Yiji_Kong and jamie950315 more likely two people, or at least two independent setups. A shared identity cannot be ruled out: same tier, same "3x" result, two days apart. Since G1 is 5h and G2 is week, the question changes no verdict.

### Gaps
- LINUX DO originals of locdd 103915, 103792, 104222 and 104985 (K1–K5) could not be identified, because linux.do returns 403. Their true usernames and post times remain unknown.

## Q3. Did Kimi double its legacy 5-hour window around 2026-10-27..29?

### Takeaway
**Not established.** The only explicit claim is one Reddit comment with no tier, tokens or source. No Kimi announcement of a 5-hour change was found, and new locdd searches returned no corroboration.

The rise in API-priced dollars per Allegretto 5h window between 10-26 and 10-29 follows from the higher cache-hit rate. Kimi weights cache reads at about 1/200 of input, against 1/10 at API list prices. Every K1–K5 reading fits the post-10-24 fitted weights without any doubling.

No E18 split should be recorded. The documented Kimi events in the window are:
- the 10-24 limit change (already a split);
- the 10-26 reset with a 25% monthly credit (a reset, so readings spanning it are excluded under O112);
- a 10-29 limited-time 50% discount on K2.8 Preview (metering, another model).

### Cited Findings
- **The claim.** Spare-Choice-6019, 2026-10-29T02:03:01Z: "usually like this monty limit = 4x weekly weekly = 5x 5 hour but there is an update on 5 hour limit they expand it 100%, and now weekly = 2.5x 5 hour limit". No tier, tokens or link. — [r/kimi 1xi5bnt comment 19rt4tis3b83o](https://www.reddit.com/r/kimi/comments/1xi5bnt/comment/19rt4tis3b83o/)
- **Other r/kimi comments in the thread and after 10-25 do not report a 5h doubling:**
  - CrimsonBolt33, 10-26, on a CN legacy Allegro: "It's much better after the fix yesterday … They did a weekly reset and partial monthly quota refund yesterday after implementing a fix … I have yet to hit my 5 hour window cap". — [r/kimi 1xg795b](https://www.reddit.com/r/kimi/comments/1xg795b/)
  - Defiant-Pepper-7263 (Plus, after the cutoff): "Kimi's 5-hour session limits are random, each session being 13% of the monthly total … Session 1: 785k, Session 2: 11M, Session 3: 1.2M." — [r/kimi 1xmr8vv](https://www.reddit.com/r/kimi/comments/1xmr8vv/)
- **Searches with no relevant hit.** locdd searches after 2026-10-26 for "5h 额度 变多", "5小时 额度 增加", "5h 扩容", "kimi 5h 两倍", "周限 5h 比例" and "kimi 额度 公告 5h" returned no relevant hit. Stage 1's earlier searches ("kimi 5h 翻倍", "kimi 周限 2.5" and others) also found none. — [locdd search](https://www.locdd.com/search?q=kimi%205h%20%E4%B8%A4%E5%80%8D)
- **The 10-26 provider event.** locdd 103792, titled "Kimi 道歉并重置周限额、返还 25% 月限额", reports a weekly reset and a 25% monthly return. A reply in that topic (#5) says "周六白天下调了扣费系数，也就是提高了额度", which is the 10-24 change. — [locdd 103792](https://www.locdd.com/t/topic/103792)
- **The 10-29 event.** locdd 104985 is titled "Kimi k2.8 Preview 额度消耗限时5折" ("Kimi 也是吃上压力了，直接Kimi k2.8 Preview开始5折了"). This is a metering promotion for another model, not a K3.1 Pro limit change. — [locdd 104985](https://www.locdd.com/t/topic/104985)
- **The fitted weights.** The post-10-24 Allegretto 5h weights (Astralyn's fit, per 1M tokens, as a fraction of the window) are "输入 0.2810 … 读缓 0.001407 … 输出 2.247". The ratio of cache to input is 1/200, against the API's 1/10. One reply says "订阅中缓存命中是输入价格的 1/200 ，API 是 1/10". — [LINUX DO 3071240](https://linux.do/t/topic/3071240); [locdd 103915 #5](https://www.locdd.com/t/topic/103915)
- **Same-day indications of a larger allowance (not a 5h doubling):**
  - locdd 104222 #1 (10-27): "好像额度上涨了一点". — [locdd 104222](https://www.locdd.com/t/topic/104222)
  - KiteRunner #6 there: "额度应该确实是之前有"bug"或者确实是bug". — [locdd 104222](https://www.locdd.com/t/topic/104222)

### Inferences
- Applying the fitted weights (my arithmetic; a derived cross-check, not evidence for a cell):
  - K5: 150M at 99.2% cache. Cache uses 148.8M × 0.001407 ≈ 0.21 of the window and 1.2M uncached input about 0.34, leaving room for about 0.2M output to reach 1.0.
  - K1: 31.9M at 95.4% cache. Cache ≈ 0.04, and 1.47M uncached fills the window with about 0.28M output.
  - K2 (100M, 98.5%) and K3 (70M, 98%+) are likewise feasible within 1.0.
  - So the growth from about $9–21 (K1) to $32–42 (K5) is explained by cache share under unchanged weights. A doubling is not required by the data, though not excluded.
- The doubling claim fails the profile's split standard. It is not provider-documented, and it is not detected by two independent per-token fits. **No new Kimi partition**: the 2026-10-24 split stays the only limit split.
- The 10-26 reset is typed "reset". Readings that span it should be excluded under O112. That puts these at risk:
  - K2: measured "早上" on 10-26 CST. The exact reset hour is unknown.
  - K4: a weekly reading whose week may span the reset.
- If a 5h change were later accepted around 10-27..29, K5 would sit alone in a new partition, and the pre-change Allegretto 5h cell would lose K5.

### Gaps
- No primary Kimi notice (Kimi Code console changelog, Weibo or X) about the 5-hour window after 10-26 was found or reachable.
- DolphinLover's coefficient thread on LINUX DO ("最后更新：2026-11-03", per stage 1) is unreachable (403).
- The exact time of the 10-26 reset is unknown.

## Q4. Are there further in-window reports that stage 1 missed (Google AI forum, Reddit, Hacker News, LINUX DO mirrors, V2EX, Zhihu)?

### Takeaway
**No new qualifying in-window reports** were found for any cell:
- Gemini 4 Argon: none.
- Kimi K3.1 Pro, USD or CN: none.
- MiMo-V2.6-Pro/Flash: none.
- MiniMax-M3.1-Flash: none.

Near-misses found this run (none qualifies):
- jamie950315's earlier 10-19 AI Pro comment: no model, no meter.
- HN Argon comments: percentages or hours only.
- Google forum DeSinc (AI Pro, percentages only).
- V2EX Vaspike (MiniMax ¥119 plan, no meter).

### Cited Findings
- **jamie950315, 2026-10-19 (r/google_antigravity 1x9pkjc):** "yeah if you calculate your usage via tools like ccusage and then do some math you will find out your weekly usage is ~$25, so month usage is ~$100" and "$100 in google ai pro in antigravity is monthly usage". No model, meter fraction or token counts, so not eligible. — [Reddit 1x9pkjc](https://www.reddit.com/r/google_antigravity/comments/1x9pkjc/)
- **Google AI forum:**
  - DeSinc (t/192044, 2026-10-26): a Pro user losing "3% of total quota in a single turn" and "5-7% of my 5 hour limit in instant chunks". Percentages only. — [t/192044](https://discuss.ai.google.dev/t/192044)
  - frey (t/195006, 2026-10-26): AI Pro. The "GEMINI 4 ARGON (Separate Pro Bucket)" weekly remaining is "97.97%", and the general bucket is stuck at 0%. This is a bug report with no tokens. It confirms that Pro has a separate weekly Argon bucket. — [t/195006](https://discuss.ai.google.dev/t/195006)
  - Forum search after 2026-10-25 ("argon 5-hour tokens", "argon ultra remainingFraction", "argon weekly tokens ultra", "argon 20x") surfaced only t/196351 and topics already in stage 1 (198073, 198255, 189085, 189620). — [forum search](https://discuss.ai.google.dev/search?q=argon%20ultra%20remainingFraction%20after%3A2026-10-25)
- **Reddit replicators.** Arctic Shift comment-body searches across Reddit since 2026-10-02 for "remainingFraction", "RetrieveUserQuo", "gen_metadata" and "percentageUsed" returned no comments, so no third replicator with figures was found. Searches for "mimo token plan" / "mimo credits" (after 10-24) and "m3.1 flash" / "M Plan" / "minimax plan" (after 10-19) returned no metered comment. — [Arctic Shift API](https://arctic-shift.photon-reddit.com/api/comments/search?body=remainingFraction&after=2026-10-02)
- **Hacker News, Argon (after 10-02):**
  - ez_mmk (10-29): "The quotas on Pro are about 2 hours of usage per week for Argon". — [HN 50288698](https://news.ycombinator.com/item?id=50288698)
  - spockz (10-29): "When I ask the same question to Argon it is 50% of my weekly usage limit gone". — [HN 50285425](https://news.ycombinator.com/item?id=50285425)
  - Neither gives tokens; spockz gives no tier.
- **V2EX.** Vaspike (2026-10-21): "我买了个 minimax 的 ￥ 119 plan". He reports only per-task token totals for other providers, plus a 529 overload error. No meter fraction. — [V2EX 1250555](https://www.v2ex.com/t/1250555)
- **V2EX: other searches.** sov2ex searches for "kimi 额度 5h", "mimo token plan" and "minimax 套餐 额度" returned only ads, reseller posts and unrelated threads. — [sov2ex](https://www.sov2ex.com/?q=kimi%20%E9%A2%9D%E5%BA%A6%205h)
- **locdd 104222 near-misses (10-27):**
  - #3: "老199现在一个月250刀 还行吧" (no meter detail).
  - #14 on the ¥699 plan: "一个会话跑5个小时，只能用到5h限额的40%" (no tokens). — [locdd 104222](https://www.locdd.com/t/topic/104222)
- **After cutoff (listed separately; unchanged from stage 1, re-seen this run):**
  - Defiant-Pepper-7263, Kimi Plus. First post 2026-11-01T14:42Z; follow-ups 11-02/11-03: "Session 1: 785k, Session 2: 11M, Session 3: 1.2M", each "13% of the monthly total". — [r/kimi 1xmr8vv](https://www.reddit.com/r/kimi/comments/1xmr8vv/)
  - ShortGuitar7207, Kimi $39 tier, 11-01/11-03: "burned through my entire month's credit in just 3 days" (no tokens). — [r/kimi 1xi5bnt](https://www.reddit.com/r/kimi/comments/1xi5bnt/)
  - Google forum t/198255 (11-05) and t/198073 (11-04): no tokens or after the cutoff. — [t/198073](https://discuss.ai.google.dev/t/198073)

### Inferences
- The candidate pool for every cell is as stage 1 left it, apart from the reclassifications in Q1 and Q2.
- MiMo and MiniMax remain without any in-window first-party-plan report tying M3.1-Flash or V2.6-Pro/Flash consumption to a meter fraction.

### Gaps
- Zhihu was not attempted; it was blocked in earlier runs.
- r/XiaomiMiMo and r/MiniMax_AI comment search were unavailable in stage 1 and not retried.
- Bluesky and X were not searched.

## Q5. Does the O11 test pass for each model × plan × unit cell and partition?

### Takeaway
**No cell passes O11.** The closest are:
- Ultra 5x · Argon · 5h (Antigravity) and Ultra 5x · Argon · week (Antigravity): one clean, non-provisional report each (Yiji_Kong $49.2–50.0 per 5h; jamie950315 $199.9–200.1 per week, now non-provisional). Each lacks a second report.
- Allegretto ¥199 (CN) · 5h, post-10-24: fcten t2 ($9.59) and K1 ($9.0–20.8) alone would satisfy the margin. But the cell's other eligible reports (K2 $22.7–34.7, K3 $15.3–27.7, K5 $32.2–41.8 provisional) push the largest lower bound far above 1.2 × 9.59, and locdd independence is unverifiable.

### Cited Findings (cell by cell; reports as cited in Q1–Q4 and `data/plan_reports.json`)

**Google, Gemini 4 Argon (no Google partition split recorded or documented in the window)**

| Cell | Eligible reports | Verdict |
|---|---|---|
| AI Pro · week | Muhammed_Alpler $8.47 ([t/190608](https://discuss.ai.google.dev/t/190608)); Faheem_Anis1 $11.4–13.4 ([t/191879](https://discuss.ai.google.dev/t/191879)); ansofteng $7.84–9.04 (provisional). Nothing new | **Fails**: 11.4 > 1.2 × 8.47 = 10.16 |
| AI Pro · 5h | none; Argon is a weekly-only bucket on Pro ([t/195006](https://discuss.ai.google.dev/t/195006)) | **Fails** (no reports) |
| AI Ultra 5x · 5h (Antigravity) | Yiji_Kong $49.2–50.0 ([t/196351](https://discuss.ai.google.dev/t/196351/1)); jamie950315's $150-at-3× figure is derived, so excluded | **Fails**: one report |
| AI Ultra 5x · week (Antigravity) | jamie950315 $199.9–200.1, now non-provisional ([1xfnvds](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/)) | **Fails**: one report |
| AI Ultra 5x · week (Gemini app, a separate meter) | Yiji_Kong $29.7–36.0, weak: tokens estimated from characters ([t/196351 #5](https://discuss.ai.google.dev/t/196351/5)) | **Fails**: one report. Pooled with Antigravity, it would still fail: 199.9 > 1.2 × 36.0 |
| AI Ultra 5x · 5h (Gemini app) | Yiji_Kong about $1.08–1.80 (2-decimal reading) | **Fails**: one report |
| AI Ultra 20x · any | ubelai, mixed Argon and Flash, plan level only | **Fails** |
| Ultra (tier unstated) · week | spin.pyokosmeme $50 (recorded); iluvios (after cutoff, loose) | **Fails** (no tier) |
| Gemini 4 Carbon · any | none | **Fails** |

**Kimi K3.1 Pro (partition: after the 2026-10-24 limit split; no further split; readings spanning the 2026-10-26 reset excluded under O112)**

| Cell | Eligible reports | Verdict |
|---|---|---|
| Plus / Pro / Max / Ultra (USD) · 5h, week, month | none in-window after the split. waximabbax $1.37 is from 10-24 ([HN](https://news.ycombinator.com/item?id=50222093)); Defiant-Pepper-7263 is after the cutoff | **Fails** |
| Allegretto ¥199 (CN, legacy) · 5h | fcten t2 $9.59 (10-25); K1 $9.0–20.8; K2 $22.7–34.7 (approximate; may span the reset); K3 $15.3–27.7 (estimate); K5 $32.2–41.8 (provisional, tier inferred) | **Fails**. Largest lower bound 32.2 (22.7 without K5) > 1.2 × 9.59 = 11.51. fcten t2 + K1 alone pass (9.59 ≤ 1.2 × 9.59), but the cell includes the others. K1–K5 carry the locdd-pseudonym independence caveat. weibo-allegretto $10 (10-24 09:35 CST) and choulei $10–10.09 (tier unstated, so not this cell) are recorded; weibo's side of the 10-24 split is ambiguous |
| Allegretto ¥199 (CN) · week | K4 $62–261 (week may span the 10-26 reset); Astralyn/MoonDrinker derived and one observer | **Fails** (one non-derived report, possibly excluded) |
| Allegretto ¥199 (CN) · month | recorded only: fcten t2 $240; Astralyn $279 (derived) | **Fails** (one non-derived) |
| Allegro ¥699 (CN, legacy) · week | K8 $185–191 (spans the 10-24 split); kojimako $167 (derived) | **Fails** |
| Allegro ¥699 (CN) · 5h | kojimako $33.5 (derived); okarin $25.8 (derived); weibo-allegro $25 (10-24 morning, side of the split ambiguous) | **Fails** (no two non-derived post-split reports) |
| Max ¥699 (CN, new) · 5h / month | weibo-max $13.9 (10-24); okarin (derived); K9 and K10 after the cutoff or derived | **Fails** |
| Plus / Pro / Ultra (CN, new) | weibo table only (one observer) | **Fails** |

**Xiaomi MiMo**

| Cell | Eligible reports | Verdict |
|---|---|---|
| V2.6-Pro · Lite · month | AppleHuman8535 $4.6, one report ([r/opencode 1x71142](https://www.reddit.com/r/opencode/comments/1x71142/)) | **Fails** |
| V2.6-Pro · Max · month | TheVoyant $80–105, one report ([image](https://i.redd.it/xw17jwr9fbxh1.png)) | **Fails** |
| V2.6-Pro · Standard / Pro | none | **Fails** |
| V2.6-Flash · all tiers | none | **Fails** |

**MiniMax M3.1-Flash**

| Cell | Eligible reports | Verdict |
|---|---|---|
| M Plan Go / Explore / Build | none in-window after GA | **Fails** |
| Legacy Token Plan cells | only provisional Preview-era reports (Illustrious-Many-782, AwayTeamRedShirt, Money-String4165, nnayrdev) plus Illustrious-Many-782's mixed-modality 10-30 post ([r/MiniMax_AI 1xjt5o1](https://www.reddit.com/r/MiniMax_AI/comments/1xjt5o1/)) | **Fails** |
| ¥119 CN plan (V2EX Vaspike) | no meter ([V2EX 1250555](https://www.v2ex.com/t/1250555)) | **Fails** |

### Inferences
- **Data changes suggested for `data/plan_reports.json`:**
  - (a) Add G1 Yiji_Kong (Ultra 5x, 5h, $49.2–50.0) and G2 jamie950315 (Ultra 5x, week, $199.9–200.1). Mark G2 non-provisional and label its 5h figure derived.
  - (b) Merge `moondrinker-allegretto` into the Astralyn observer, since it is the same thread and person.
  - (c) Give `choulei-legacy` the URL https://linux.do/t/topic/3071240/11.
  - (d) Tag K5 provisional (tier inferred).
  - (e) Flag every locdd-sourced report as independence-unverifiable.
- The Allegretto 5h dispersion is structural. The O11 metric prices tokens at API list, where cache costs 1/10 of input, while Kimi meters cache at about 1/200 of input. So a window's API-priced value rises steeply with cache-hit rate (95.4% → about $9–21; 99.2% → about $32–42). Reports at different cache rates will rarely fall within 1.20×. This is a methodology observation for the report writer, not a rule change.
- For Google, a second independent Antigravity Ultra 5x reading on the same meter (5h or week) would likely satisfy the margin: G1 is $49.2–50.0, a tight range. Until one exists, both cells fail.

### Gaps
- Window start and end times for G1 and G2 are not stated. G2's weekly window started at an unstated reset time.
- The exact time of the 10-26 Kimi reset is unknown, which decides whether K2 and K4 span it.
- LINUX DO originals are unverifiable (403), so independence of K1–K5 from fcten and from each other is unknown.
