# Kimi K3.1 Pro: user reports of plan allowances (new USD/CN plans), 2026-10-25

Scope: reports that are NOT already in `stage1-kimi.md` (that file has waximabbax Plus $1.37/5h, plus fcten, Astralyn, kojimako, hanashiro, choulei and raymondchau on legacy CN plans). API prices used: K3.1 Pro $2.00 input / $0.20 cached input / $10.00 output per 1M tokens. For Highspeed I doubled input and output and kept cache at $0.20, which matches okarin's statement that the API's Highspeed cache price equals the standard one. Times are UTC unless marked CST (UTC+8). Saturday was 2026-10-24.

## Key question 1: reports on new-plan tiers (USD or CN) after the quota change, and the monthly pool's size in 5-hour windows

### Takeaway
I found three new numeric sources for new-plan tiers. All three are on CN tiers or carry caveats:
- **okarin / "NightRain":** a careful measurement of the new CN Max (¥699) on K3.1 Pro: 28.4M tokens per 5-hour window at a 92.2% cache mix, which is about $13.4 per window at USD API prices, and a monthly pool of 24.84 windows (about $333 per month).
- **Weibo blogger 贾凡-失落的大蒜:** a table for all four new CN tiers (Plus $0.9, Pro $4.3, Max $13.9, Ultra $27.8 per 5-hour window). The method is not given, and the post predates the quota increase.
- **A USD Ultra screenshot:** it implies about 16 windows per month, but gives no token counts.

No USD tier has two independent qualifying reports that agree within 20%.

### Cited Findings

**1. okarin (LINUX DO; the deleted topic 3069671 survives on the locdd.com mirror), 2026-10-24, two ¥699 accounts: legacy Allegro and new Max**
- The thread is mirrored at locdd.com "大佬说" topic 103507, created 2026-10-24T11:26Z. The mirror shows the poster as "NightRain"; locdd appears to rename users. The title matches LINUX DO 3069671 exactly. On LINUX DO, okarin then posted a short version (topic 3070058, 2026-10-24T12:59Z) with the same figures and wrote: "详细测试就不说了，辛辛苦苦写的被举报了不让发" (I won't go into the detailed test; what I worked hard to write was reported and can't be posted). So 3069671 was removed after a report and returns 404. — [locdd mirror](https://www.locdd.com/t/topic/103507); [okarin, LINUX DO 3070058](https://linux.do/t/topic/3070058)
- Setup, verbatim: "我这边有两个¥699/月的会员，一个旧套餐Allegro，一个新套餐Max，两个号在pi里都配了k3.1-pro和highspeed … 跑了两个账号、两个模型、49次请求，按API价折算花了27块" (I have two ¥699/month memberships, one legacy Allegro and one new Max, both set up in pi with k3.1-pro and highspeed … ran two accounts, two models, 49 requests; ¥27 at API prices). Method: "额度读数走GET /coding/v1/usages … 返回limit_5h、limit_7d、limit_month_total、limit_month_code各自的used_ratio，精度0.01个百分点" (quota readings come from GET /coding/v1/usages, which returns used_ratio for limit_5h, limit_7d, limit_month_total and limit_month_code, to 0.01 percentage points). Token counts were read from /coding/v1/chat/completions responses, and the weights were fitted by least squares. The effort level is not stated. — [locdd 103507](https://www.locdd.com/t/topic/103507)
- Fitted weights, in percentage points of the 5-hour window per 1M tokens (uncached input / cache hit / output):
  - legacy Allegro standard: 9.361 / 0.04811 / 74.61
  - legacy Allegro Highspeed: 18.73 / 0.09292 / 150.9
  - **new Max standard: 17.20 / 0.08246 / 146.8**
  - new Max Highspeed: 34.42 / 0.1632 / 295.7

  — [locdd 103507](https://www.locdd.com/t/topic/103507)
- Pool sizes, verbatim: "旧号5小时窗口与周窗口的容量比是5.00，月池相当于25.09个5小时窗口；新号月池相当于24.84个5小时窗口" (on the legacy account the week holds 5.00 five-hour windows and the month 25.09 windows; on the new account the month holds 24.84 windows). Also: "5小时窗口只占月额度的约4%" (one 5-hour window is only about 4% of the monthly quota). — [locdd 103507](https://www.locdd.com/t/topic/103507)
- Capacity at okarin's historical mix (92.2% cache hit, 6.2% uncached input, 1.6% output), per 5-hour window and per month:
  - legacy Allegro standard: 54.6M and 1.37B
  - **new Max standard: 28.4M and 706M**
  - new Max Highspeed: 14.1M and 351M

  — [locdd 103507](https://www.locdd.com/t/topic/103507)
- Headline, in CNY API value: "旧Allegro 6.08倍（满月约¥4251）… 新Max 3.14倍（约¥2192）" (legacy Allegro 6.08× at about ¥4,251 for a full month; new Max 3.14× at about ¥2,192). Also: "同价699，旧Allegro折成API价的价值差不多是新Max的1.94倍" (at the same ¥699, legacy Allegro is worth about 1.94× new Max at API prices). The multiple ranges from 5.61× to 10.58× on the legacy plan, depending on cache share. — [locdd 103507](https://www.locdd.com/t/topic/103507); [okarin 3070058](https://linux.do/t/topic/3070058)
- Effective subscription prices, verbatim: "kimi订阅的缓存价格是API价格的1%（新版是2%），但是输入输出价格算下来是API20和30%（新版37%和61%）" (on legacy plans the subscription charges cache at 1% of the API price and input/output at 20% and 30%; on new plans 2%, 37% and 61%). — [okarin, 3070058 #4](https://linux.do/t/topic/3070058)
- Huxiu's independent write-up of the same test: "开发者用两个 699 账号测试 49 次 API 请求 … 旧套餐 API 价值约为新套餐 1.94 倍" (a developer tested 49 API requests on two ¥699 accounts … the legacy plan's API value is about 1.94× the new plan's). — [Huxiu](https://www.huxiu.com/article/4900212.html)
- My USD normalisation for **new Max ¥699, K3.1 Pro standard**:

  | Mix (cache / input / output) | Tokens per 5h | $ per 5h | $ per month (× 24.84) |
  |---|---|---|---|
  | 92.2 / 6.2 / 1.6 (okarin's) | 28.6M | $13.42 | ≈ $333 |
  | 90 / 8 / 2 | — | $12.31 | ≈ $306 |
  | 97.5% cache, uncached input = 2.5 × output (Astralyn/kojimako convention) | — | $21.04 | ≈ $523 |

  - Highspeed at okarin's mix: $10.72 per 5h, about $266 per month.
  - Legacy Allegro at okarin's mix, for comparison: $25.8 per 5h, about $646 per month.

  (Computed from the fitted weights above.)
- **Timing.** okarin's legacy-Allegro weights match kojimako's *second-day* (post-increase) weights in `stage1-kimi.md` almost exactly: 0.0936 / 0.000473 / 0.751 as a share of the window, against okarin's 9.361 / 0.04811 / 74.61 percentage points. So okarin's test almost certainly ran after the increase, which therefore happened before about 19:26 CST on Saturday 2026-10-24. The same author, in a 2026-10-25 reply: "根据其他大佬的测试数据，周六的确上调过额度" (according to other people's test data, the quota was indeed raised on Saturday). — [locdd 103510 #9](https://www.locdd.com/t/topic/103510)

**2. Weibo blogger 贾凡-失落的大蒜 ("微博认证：科技博主", a Weibo-verified tech blogger), 2026-10-24 09:35 CST, all new CN tiers plus legacy plans**
- Verbatim: "Kimi K3.1 Pro 五个新套餐两个老套餐额度最新测算：（仅计算 K3.1 Pro）" (latest estimates of the quota on five new plans and two legacy plans, K3.1 Pro only).
  - "Plus:99元，月额度：73m，5H：3.48M，5H 换算 0.9 刀 倍率：1x" (Plus ¥99: 73M per month, 3.48M per 5h, worth $0.9 per 5h; multiplier 1×)
  - "Pro: 199元，月额度：365m，5H：17.4M，5H 换算 4.3 刀 倍率：2x" (Pro ¥199: 365M per month, 17.4M per 5h, $4.3 per 5h; 2×)
  - "Max: 699元，月额度：1169M，5H：55.7M，5H 换算 13.9 刀 倍率：5x" (Max ¥699: 1,169M per month, 55.7M per 5h, $13.9 per 5h; 5×)
  - "Max: 1399元 [sic, the Ultra tier]，月额度：2338m，5H：111.3M，5H 换算 27.8 刀 倍率：10x" (¥1,399: 2,338M per month, 111.3M per 5h, $27.8 per 5h; 10×)
  - "老Allegretto：199 元，月额度：703M，5H：34.8M，5H 换算 10 刀" (legacy Allegretto ¥199: 703M per month, 34.8M per 5h, $10 per 5h)
  - "老Allegro：699 元，月额度：2191M，5H：104.3M，5H 换算 25 刀" (legacy Allegro ¥699: 2,191M per month, 104.3M per 5h, $25 per 5h)

  — [Sina mirror of the Weibo post](https://www.sina.cn/weibo/detail/5357477820630662.html)
- Implied pool: each new tier's month equals about 21 five-hour windows (73/3.48, 365/17.4, 1169/55.7, 2338/111.3). Implied monthly value is about $19 (Plus), $90 (Pro), $292 (Max) and $584 (Ultra).
- Caveats:
  - The token mix, effort and method are not given, and it is unclear which tiers were measured and which were scaled.
  - The stated multipliers do not match the token figures (Pro is labelled 2× Plus, but 17.4M / 3.48M = 5×).
  - The post went up at 09:35 CST on 10-24, probably before Saturday's increase.
  - The implied price is about $0.25 per 1M tokens on every tier, which suggests a very high cache share.
  - The legacy-plan figures ($10 for Allegretto, $25 for Allegro per 5h) roughly match choulei's $10.09 and okarin's $25.8.

**3. LessComplexity (r/kimi), 2026-10-25T03:08Z, USD Ultra $199, pool-to-window ratio only**
- Verbatim: "K3.1 pro, max with swarm on, capped on sub-agents per swarm (2-3 max) … this is literally all my session on a single prompt". The screenshot shows: "Ultra · Credits reset monthly · Next auto-renewal date: 2026-11-24 … Total usage 4.61% … 5-hour usage Code 75.74% Resets 10-25 02:38". — [Reddit post](https://reddit.com/r/kimi/comments/1xerert/even_the_ultra_subscription_is_unusable_for/); [screenshot](https://i.redd.it/s0bv4jf75jxh1.png)
- The subscription began 2026-10-24 20:38, so this session was likely the only usage. 75.74% of a window used 4.61% of the month, so one window is about 6.1% of the month, or about **16.4 windows per month on USD Ultra**. No token counts are given, so this does not qualify as a report.

**4. Bilibili video by 能工智人永不为奴 (screenshot posted on LINUX DO 3068845 by mumuhaha487, 2026-10-24)**
- The "新套餐" (new plans) slide reads "四档单价一样，只多给量" (all four tiers have the same unit price; higher tiers just give more volume) and "每米 ≈ 23.5 万 Token" (about 235,000 tokens per yuan):
  - Plus ¥99: 2,333万 tokens (23.33M), ×2
  - Pro: 4,667万 (46.67M), ×4
  - Max: 1.63亿 (163M), ×14
  - Ultra: 3.27亿 (327M), ×28
  - Note on the slide: "Plus 实测；Pro / Max / Ultra 按倍数推算" (Plus measured; Pro, Max and Ultra extrapolated from the multipliers)
- The model is unclear (the video has a "别家 K3" tab), the period is presumably monthly, and there is no token mix or dollar figure. Not qualifying. The post's author reads it as "200 刀才能用 0.3b" (only 0.3B tokens for $200). doraemonzh, on Max ¥699 annual, replied: "这个图中的统计纯纯招笑" (the statistics in this image are laughable). — [LINUX DO 3068845](https://linux.do/t/topic/3068845)

**5. Other new or legacy anecdotes without usable numbers (for context)**
- ArtemCrazy, r/kimi, 2026-10-24: "I bought the $39 plan … About 10 minutes later, my entire 5-hour usage limit was gone." — [Reddit](https://reddit.com/r/kimi/comments/1xdlmsq/how_good_are_kimi_limits_on_plans/19rku9gkuk57k/)
- mateszhun, 2026-10-24: "On the 20 dollar plan, I was able to run 2 tasks in the 5 hour limit." — [Reddit](https://reddit.com/r/kimi/comments/1xdk3y1/kimi_k31_pro_benchmarks/19rkgwwi6m45e/)
- Emergency-River-7696, 2026-10-23: "used it like 1 hour and consumed 25% of my monthly limit" (tier not stated). — [Reddit](https://reddit.com/r/kimi/comments/1xdt9lu/im_not_impressed_with_31/19rk1wi8elaww/)
- CrimsonBolt33, 2026-10-24: "even on the most expensive plan it hits usage limited super fast (within an hour)". — [Reddit](https://reddit.com/r/kimi/comments/1xdkyv4/meet_kimi_k31_pro/19rkf03mczygz/)
- Ok-Stomach-8050, 2026-10-25: "same result in high reasoning level as what I got with K3 in max … more of the same job … before hitting the 5h limit". — [Reddit](https://reddit.com/r/kimi/comments/1xdkngh/how_good_is_kimi_k31_pro/19rm0unlzt4ch/)
- 3princip, HN, $99 Max: "ran out of the 5hr budget in less than 10 minutes". — [HN 50215365](https://news.ycombinator.com/item?id=50215365)
- cvooc, V2EX, 2026-10-24: "额度 10 分钟就烧光了" (quota burned through in 10 minutes). — [V2EX 1251425](https://www.v2ex.com/t/1251425)
- fenglinnet, LINUX DO 3068845 #17 (legacy ¥199): "用了4300w，消耗了周额度9%，不过我这个缓存率98%以上了" (used 43M tokens, 9% of the weekly quota, at a cache hit rate above 98%). This partial report is already in Stage 1. — [LINUX DO 3068845](https://linux.do/t/topic/3068845)
- jackliu100, 3068845 #16, legacy tokens per week: "原来的199还能用8亿周，结果变3亿 … 699 … 改了之后是14亿~24亿" (the ¥199 plan used to give 800M a week, then 300M … ¥699 … after the change it was 1.4B–2.4B). The model and date are unclear. — [LINUX DO 3068845](https://linux.do/t/topic/3068845)

### Inferences
- **New CN Max (¥699), the best evidence:** about $12–13 per 5-hour window at a 90–92% cache mix, and about $21 at 97.5% cache, after the 10-24 increase. That is about $300–520 per month at 24.84 windows. Weibo's $13.9 lies within 4% of okarin's $13.4, but the two probably come from different quota regimes (before vs after the increase) and from unknown and different token mixes. I treat the agreement as coincidental and not as two independent confirmations.
- **Windows per month on new plans:**
  - okarin (CN Max): 24.84
  - Weibo (CN, all tiers): about 21
  - USD Ultra screenshot: about 16.4. This can be read only one way and may include non-Code "Kimi" usage counted in the same pool.

  So the monthly pool appears to be roughly 16–25 five-hour windows. It is not consistent across sources and may differ between tiers or regions.
- **Effective price on new plans:** the subscription charges about 37% of the API price for input, 61% for output and about 2% for cache (okarin). New-plan value is therefore highly sensitive to the cache share, and low-cache workloads get only about 0.6–1.2× API value per dollar of window.
- **Legacy vs new at the same price:** the legacy plan gives about 1.94× the value of the new one (okarin), which matches community claims that the new ¥699 is about half the old.

### Gaps
- No second numeric report on any **USD** tier (Plus, Pro, Max or Ultra) with token counts or dollars. Reddit, HN and V2EX hold only anecdotes. Kimi has not published an official CN-to-USD tier mapping, so it is unconfirmed whether USD Max ($99) has the same quota as CN Max (¥699). The USD page states Max "5×", Ultra "10×"; Weibo uses 1/2/5/10 multipliers; the Bilibili slide uses 2/4/14/28.
- None of the new reports states the effort level.
- The Weibo image (wx4.sinaimg.cn) could not be downloaded (connection reset). Its source data and method remain unknown.
- The full original LINUX DO 3069671 is gone (404; the Wayback Machine has no snapshot; archive.ph returned 429). Only the locdd mirror and okarin's summary survive.

## Key question 2: LINUX DO topic 3069671 and other legacy-vs-new comparisons

### Takeaway
I recovered topic 3069671 in full from the locdd.com mirror. Under the same pi agent and API-price conversion, the new Max (¥699) delivers about half the API value of the legacy Allegro (¥699): 3.14× vs 6.08× the subscription price at a 92.2% cache mix. The new plan's monthly pool is 24.84 five-hour windows.

### Cited Findings
- The title on locdd and in search results is identical to the LINUX DO title: "K3.1 Pro额度掉得快？两个¥699订阅实测：旧号5.6～10.6倍、新号2.9～5.5倍API价". The range applies to "缓存90%～97%、输出2%～0.5%的常见agent负载" (common agent workloads with 90–97% cache and 2–0.5% output). — [locdd 103507](https://www.locdd.com/t/topic/103507); [LINUX DO 3069671 (404)](https://linux.do/t/topic/3069671)
- okarin's short version: "旧Allegro5.61～10.58倍API额度 / 新Max2.89～5.50倍API" (legacy Allegro 5.61–10.58× API value; new Max 2.89–5.50×). — [LINUX DO 3070058](https://linux.do/t/topic/3070058)
- The earlier community estimate okarin cites: "社区之前估的是旧号5.5~6.5倍、新号3~3.4倍" (the community previously estimated 5.5–6.5× for legacy accounts and 3–3.4× for new ones). — [locdd 103507](https://www.locdd.com/t/topic/103507)
- Highspeed penalty: "缓存90%时高速版每额度API价值只剩普速的0.83，按历史mix是0.80，97%缓存掉到0.68" (at 90% cache, Highspeed's API value per unit of quota is only 0.83 of standard; 0.80 at the historical mix; 0.68 at 97% cache). — [locdd 103507](https://www.locdd.com/t/topic/103507)
- arxiv (3070058 #8, 2026-10-24): "好像只是提高了5h的 月限感觉变化不大呢" (it seems only the 5-hour limit was raised; the monthly limit doesn't feel much different). This is unverified. — [LINUX DO 3070058](https://linux.do/t/topic/3070058)
- The 80aj.com article (2026-10-25) republishes kojimako's 3070992 analysis. It gives legacy Allegro K3.1 Pro "约1102元" (about ¥1,102) per full week, and says "K3.1权重在两轮测试间下调35%" (the K3.1 weight fell 35% between two test rounds). This is not new evidence. — [80aj](https://www.80aj.com/2026/10/25/kimi-api-value-analysis/)

### Inferences
- okarin's legacy-Allegro weights agree with kojimako's day-2 legacy-Allegro weights to within about 2%. That is strong cross-validation of the metering method, and it suggests okarin's new-Max figures are reliable for the post-increase regime. It cannot be ruled out that kojimako and okarin are the same person; I found no evidence either way.

### Gaps
- Only one new-plan account (CN Max) has been measured at this level of rigour. There is no equivalent fit for new Plus, Pro or Ultra, or for any USD account.

## Key question 3: Did Kimi publish quota numbers or changes between 2026-10-20 and 2026-10-25?

### Takeaway
I found no official numeric quota and no announcement of the 10-24 increase. Kimi's help pages describe only the structure: a rolling 5-hour window, no weekly limit on new plans, a shared monthly total, and Highspeed costing about 2× quota. Users infer the increase from metering (it took effect on Saturday 10-24) and from hearsay in official groups.

### Cited Findings
- Kimi Code benefits page: "新会员取消每周额度限制，仅保留每 5 小时的滚动频率窗口" (new members have no weekly limit, only a rolling 5-hour window). Both legacy and new plans are capped by a monthly total; when it is reached, "Kimi Code quota is frozen until the monthly quota resets or the subscription is upgraded" (my paraphrase of the page). There are no per-tier numbers and no changelog. — [kimi.com/help/kimi-code/benefits](https://www.kimi.com/help/kimi-code/benefits)
- Huxiu: no official statement on quotas. It reports only "discussion of Kimi adjusting membership quotas before and after the new model's release" (Huxiu's wording, paraphrased; no details given). — [Huxiu](https://www.huxiu.com/article/4900212.html)
- okarin: "官方一直只给窗口百分比和重置时间，每个档位有多少token、百分比怎么换算，从来不写" (the official side only ever gives window percentages and reset times; it never states how many tokens each tier has or how percentages convert). — [locdd 103507](https://www.locdd.com/t/topic/103507)
- Hearsay of an increase on 10-25:
  - CloudWalker (locdd 103510 #7): "我官群的老哥说额度涨了" (a guy in the official group said the quota went up)
  - BlackCoffee (#8): "我的体感也是涨额度了，199的老套餐" (it feels like the quota went up for me too, on the legacy ¥199 plan)
  - TimeMachine (#2, 10-24): "据说在调整额度，观望两天看看" (the quota is reportedly being adjusted; wait a couple of days and see)
  - markh4 (3070058 #6): "好像是今天额度开始提高了吧" (it looks like the quota started going up today)

  — [locdd 103510](https://www.locdd.com/t/topic/103510); [LINUX DO 3070058](https://linux.do/t/topic/3070058)
- The official WeChat launch article is linked by cvooc on V2EX: https://mp.weixin.qq.com/s/Q6Z-skAUH_na9g37VWbHew. I did not open it. — [V2EX 1251425](https://www.v2ex.com/t/1251425)
- An X search found no Moonshot post about raised limits. — (WebSearch, no result)

### Gaps
- I did not read the WeChat article or Kimi's X timeline directly. An official notice may exist there.

## Summary table: USD tier → qualifying reports (K3.1 Pro, 5-hour window, USD API prices)

| USD tier (CN equivalent) | Qualifying reports | $ per 5h | $ per month | ≥2 agree within 20%? |
|---|---|---|---|---|
| Plus $19 (¥99) | waximabbax, HN, USD Plus, 2026-10-24 (Stage 1) | $1.37 | n/a | **No** (34% apart; Weibo's method is unknown and it predates the increase) |
| | 贾凡, Weibo, CN Plus, 10-24 09:35 CST (pre-increase, mix unknown) | $0.9 | ≈ $19 (≈ 21 windows) | |
| Pro $39 (¥199) | 贾凡, Weibo, CN Pro (pre-increase, mix unknown) | $4.3 | ≈ $90 | **No** (one report) |
| Max $99 (¥699) | okarin / NightRain, CN new Max, measured 10-24 after the increase, 92.2/6.2/1.6 mix | $13.4 | ≈ $333 (24.84 windows) | **Nominally yes (4% apart), but not robust**: CN, not USD; different regimes and mixes; Weibo's method is unknown |
| | 贾凡, Weibo, CN Max (pre-increase) | $13.9 | ≈ $292 | |
| Ultra $199 (¥1,399) | 贾凡, Weibo, CN Ultra (pre-increase) | $27.8 | ≈ $584 | **No** (one report) |
| | LessComplexity, USD Ultra screenshot: pool ratio only, no tokens | n/a | ≈ 16.4 windows per month | |

Legacy plans, for reference: okarin's legacy Allegro gives $25.8 per 5h and about $646 per month at the 92.2% mix. Weibo gives legacy Allegro $25 per 5h and legacy Allegretto $10 per 5h, which agrees with Stage 1's choulei ($10.09).
