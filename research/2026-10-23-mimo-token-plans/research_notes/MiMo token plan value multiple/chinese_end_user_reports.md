# Chinese-language end-user reports of actual usage on Xiaomi MiMo Token Plans (MiMo-V2.6-Pro / V2.6-Flash), as of 2026-10-23

Researcher scope: real subscribers who state how much they actually used on a MiMo Token Plan in a billing window, so that value multiple = API-priced value of usage / plan fee can be computed. Provider quotas are kept apart as provider claims. Priority window: 2026-09-22 (V2.6 release) to 2026-10-23.

Bottom line: **I found no qualifying in-window end-user report of MiMo-V2.6-Pro or MiMo-V2.6-Flash usage on a Token Plan that gives a measured quantity (credits, tokens, % used or an API-priced estimate) for a billing window.** The in-window evidence is three V2EX replies dated 2026-09-22. They cover the billing month that ended around the V2.6 launch, so the usage is V2.5-era or unstated. Two of them give only a renewal charge, from which usage can be inferred only through the renewal-offset rule. The third reports zero use. All older measured reports (May to June 2026) are V2.5-era and partial-window.

## Which subscribers report concrete usage on a MiMo plan (tier, price, date, window, model, token split, API-priced value, link)?

### Takeaway
No subscriber report in 2026-09-22..2026-10-23 states measured V2.6-Pro or V2.6-Flash consumption on a Token Plan. Three V2EX replies dated 2026-09-22 are plan-level and model-unstated, and they cover the billing month that ended at the V2.6 launch. One reports zero use on a Max plan, which implies a value multiple of about 0. Two report only a renewal charge (¥10 on a Pro plan; "十几块" after paying ¥99 the month before). Usage can be backed out of those charges only through the renewal-offset rule, which a user says changed around then. Older measured reports (May to June 2026, V2.5 era) show light users consuming about 8–9% of a Pro allowance in 10 days or less.

### Cited Findings

**Pricing rule that turns plan credits into API-priced value (from the provider's rate cards; a conversion, not an allowance measurement)**
- The official Token Plan page (updated 2026-10-21) gives the personal monthly tiers: Lite ¥39/$6 with 41亿 credits, Standard ¥99/$16 with 110亿, Pro ¥329/$50 with 380亿, Max ¥659/$100 with 820亿. Annual plans are ¥408/¥1044/¥3468/¥6948 for 492/1320/4560/9840亿 credits. — [MiMo Token Plan subscription doc](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription)
- The same page gives credits per token. mimo-v2.6-pro: 2.5 (cache hit input), 300 (uncached input), 600 (output). mimo-v2.6-flash: 2, 100, 200. There is a 0.8x consumption coefficient from 00:00 to 08:00 Beijing time. The page states no explicit "1亿 credits = ¥1" rule. — [MiMo Token Plan subscription doc](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription)
- MiMo-V2.6-Pro API prices on the official model page are ¥0.025/M (cache hit input), ¥3/M (uncached input) and ¥6/M (output). — [MiMo-V2.6-Pro model page via search result](https://mimo.mi.com/models/zh-CN/mimo-v2.6-pro). The V2.6 series kept V2.5's API prices: Flash ¥1/¥2 and Pro ¥3/¥6 per M input/output. — [中华网, 2026-10-21](https://tech.china.com/article/20261021/202610211967503.html); [动点科技, 2026-10-21](https://cn.technode.com/post/2026-10-21/xiaomi-mimo-v2-5-retirement/)
- An end user on V2EX gives the same rule: "一亿 credits 等同于一块钱的额度…以这个 pro 套餐为例，其实就是花了 329 买了 380 的额度" (haukuen, 2026-09-22). The screenshot is the V2.6 pricing card showing "380 亿 Credits = 9.3 x Lite", "夜间 0.8x 消耗" and "无周限额 · 无 5 小时限额". — [V2EX t/1243835 #1](https://www.v2ex.com/t/1243835)
- A linux.do author (lanvent, 2026-05-27) derived the same rule: "1亿 credits = ¥1 API 额度". The derived table: Lite ¥39 → ¥41 of API value (+5%), Standard ¥99 → ¥110 (+11%), Pro ¥329 → ¥380 (+16%), Max ¥659 → ¥820 (+24%). These are theoretical figures, not observed use. — [linux.do t/2254166](https://linux.do/t/topic/2254166)

**In-window reports (2026-09-22..2026-10-23)**

| # | User / platform | Report date | Plan tier & price | Window | Model | Stated usage | API-priced value (derived) | Link |
|---|---|---|---|---|---|---|---|---|
| A | Kei001 / V2EX | 2026-09-22 | Max, ¥659/month (screenshot: "续订 Token Plan · Max 月度 · 到期后按 659 元/月 自动续费 · 预估实付金额 ¥0.00") | The billing month ending at renewal, around 2026-09-22 | None used. Unstated, and pre-V2.6 for most of the window | "这个月一点都没用，提前点续费是 0 元" | ≈ ¥0, so the multiple for that window is ≈ 0 | [V2EX t/1243835 #11](https://www.v2ex.com/t/1243835); screenshot https://i.imgur.com/OaGTxZt.png |
| B | CosmoLau / V2EX | 2026-09-22 | Pro (¥329/month list). Obtained through the "百亿 token 活动", then "续了三个月" | The billing month before the 2026-09-22 renewal | Unstated (V2.5 era) | "平时用的不多，这个月续费只花了 10 元" | Not stated by the user. Under the documented offset formula on the plan price, ¥10 implies about 97% of credits left, so about 3% used ≈ 11.6亿 credits ≈ ¥11.6. This is invalid if the newer rule (offset on last month's paid price, row D) applies, because last month's payment is unknown | [V2EX t/1243835 #17](https://www.v2ex.com/t/1243835) |
| C | dko / V2EX | 2026-09-22 | Paid ¥99 to renew last month (that price matches Standard, 110亿 credits; the tier is inferred) | The billing month before the 2026-09-22 renewal | Unstated (V2.5 era) | "我上个月花了 99 续费的，这个月续费花了十几块" | Not stated by the user. If the offset is (remaining/total) × last paid price (row D), a charge of ¥10–19 implies 81–90% left, so 10–19% used ≈ 11–21亿 credits ≈ ¥11–21. That gives about 0.11–0.21× of the ¥99 fee. Low confidence: the tier is inferred and "十几块" is imprecise | [V2EX t/1243835 #20](https://www.v2ex.com/t/1243835) |
| D | Denys / V2EX (rule context, not usage) | 2026-09-22 | Renewed at ¥0.01 the previous month | n/a | n/a | "现在改规则了是按上月续费价格来抵消的，之前是按套餐价格来抵消" and "上月没用完的不管剩多少都只抵 0.01 元" (when the previous renewal cost ¥0.01) | n/a | [V2EX t/1243835 #10, #18](https://www.v2ex.com/t/1243835) |
| E | konakona / V2EX | 2026-09-24 | "小米 MIMO 平台的套餐" (tier unstated) | n/a | V2.6 (thread topic) | No quantity. Only says "mimo 2.6 的确慢" | n/a | [V2EX t/1244361 #10](https://www.v2ex.com/t/1244361) |

- The official doc states the upgrade offset formula as "差价 = 新套餐价格 -（原套餐剩余额度/原套餐总额度）* 原套餐价格". It does not document the renewal offset. — [MiMo Token Plan subscription doc](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription). The linux.do analysis (2026-05-27) says the renewal discount is "(原套餐剩余额度/原套餐总额度) × 原套餐价格" and that renewal costs ¥0.01 when at least about 77% is left. — [linux.do t/2254166](https://linux.do/t/topic/2254166)
- The only in-window post with a full token ledger is not MiMo plan usage. dmonz (V2EX, 2026-09-23) repriced one month of his DeepSeek usage (1,922,529,457 tokens: Flash 1,400,807,021, of which 1,367,203,824 cache-hit, 23,041,473 cache-miss and 10,561,724 output; Pro 521,722,436, of which 502,112,256 cache-hit, 15,317,504 cache-miss and 4,292,676 output) at MiMo **API** prices: ¥155.77 against ¥317.88 on DeepSeek. That is API-to-API on DeepSeek tokens, not plan usage. — [V2EX t/1244361](https://www.v2ex.com/t/1244361); table https://i.v2ex.co/Z6Gr57KB.png
- Model routing during the window: V2.5-Pro and V2.5 were retired on 2026-10-21 at 10:00 UTC+8 and replaced by V2.6-Pro and V2.6-Flash. — [MiMo subscription doc](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription); [动点科技](https://cn.technode.com/post/2026-10-21/xiaomi-mimo-v2-5-retirement/). A third-party page says V2.5 IDs were auto-routed to V2.6 from 2026-10-14 18:00 Beijing time. This is unverified against an official source. — [coding-plan.org (via search result)](https://coding-plan.org/plans/xiaomi)
- In-window posts that mention V2.6 on a plan but give no quantities: syyyyy says "mimo plan 可以用，但是别用它们的 mimo cli" (2026-09-22, privacy/telemetry). — [V2EX t/1244057](https://www.v2ex.com/t/1244057). elias94 asks how V2.6-Pro works in practice (2026-10-20, 0 replies). — [V2EX t/1250309](https://www.v2ex.com/t/1250309). A Bilibili tutorial by 跟着小陈玩AI covers V2.6 Token Plan setup and a DeepSeek value comparison (2026-09-23, BV1xfhf6dEQR). The description and hot or recent comments (through 2026-10-20) contain no usage figures, and the video body was unreachable. — [Bilibili BV1xfhf6dEQR](https://www.bilibili.com/video/BV1xfhf6dEQR/)
- An SMZDM "WorkBuddy 实测" of V2.6-Pro (2026-10-20) is AI-compiled from 27 authors. Its "200积分" anecdote is about WorkBuddy credits, not a MiMo Token Plan, so it is excluded. — [什么值得买](https://post.smzdm.com/p/a82pw9e7/)

**Older reports (before 2026-09-22; V2.5-era plan unless noted) — listed separately**

| User / platform | Date | Plan | Window | Model | Stated usage | Derived API-priced value (1亿 credits = ¥1) | Link |
|---|---|---|---|---|---|---|---|
| maweirdos / linux.do | 2026-06-16 | Pro (received through an application) | "用了几天" | "1M多模态模型" (V2.5 by date; unstated) | "用了几天也才消耗了8%的额度", "还剩余92%"; renewal estimate "不到27块钱" (consistent with 329 × 8% = ¥26.3) | ≈ 30.4亿 credits ≈ ¥30.4 over a few days | [linux.do t/2412590](https://linux.do/t/topic/2412590) |
| 库洛米大人的大人 / Bilibili | 2026-06-08 | Pro | 10 days of heavy use | Unstated (V2.5 era) | Title: "狂用10天就用了 pro 套餐的 9% 额度" | ≈ 34.2亿 credits ≈ ¥34.2 in 10 days. Title-only evidence; video body not reachable | [Bilibili BV1sVEG6oEPS](https://www.bilibili.com/video/BV1sVEG6oEPS/) |
| 烛光烛光烛光 / Bilibili comment on the above | 2026-06-08 | Unstated (5% = ¥2 is consistent with Lite 41亿) | One feature | Unstated | "写了一个串口功能耗了5%，2块钱" | ≈ ¥2 (user's own CNY figure) | [Bilibili BV1sVEG6oEPS](https://www.bilibili.com/video/BV1sVEG6oEPS/) |
| 账号已注销 / Bilibili | 2026-06-04 | Standard ¥99, 110亿 credits | 2026-05-31 to 2026-06-04 ("实际使用数据") | Unstated (V2.5 era) | Chapter text only: "价格对比结果（Token Plan 省10.6%）" against DeepSeek | Not extractable; the video body is unreachable | [Bilibili BV1mx7Z6pEAb](https://www.bilibili.com/video/BV1mx7Z6pEAb/) |
| edwinskin / Bilibili comment on the above | 2026-06-06 | "买了mimo 套餐" (tier unstated) | One streaming task | mimo-v2.5-pro | "同一个流式任务，mimo跑了67元没跑下来，DSV4 40元就能完美交卷" | User's own CNY figure ≈ ¥67 for one unfinished task | [Bilibili BV1mx7Z6pEAb](https://www.bilibili.com/video/BV1mx7Z6pEAb/) |
| DS-Brain / Bilibili | 2026-06-01 | Unstated | Unstated | Unstated | "220亿的额度只需要12亿的token 消耗" (joking tone, "[狗头]") | If it means 220亿 credits, ≈ ¥220. Ambiguous | [Bilibili BV1ThVZ6LEeS](https://www.bilibili.com/video/BV1ThVZ6LEeS/) |
| 小心鸦Xxya / Bilibili | 2026-06-28 | Unstated | "用完一个月" | Unstated | Title: "用完一个月 mimo Token Plan，可以使用多少Token？". Content not reachable | Not extractable | [Bilibili BV1w1T36oEXg](https://www.bilibili.com/video/BV1w1T36oEXg/) |
| antony98 / V2EX #86 | 2026-05-27/28 | Unstated | "一个月" on Token Plan | V2.5-Pro (per thread) | 97.x% cache hit; about 1M tokens ≈ 20M credits | ≈ ¥0.20 per M tokens blended (a credit-per-token ratio, not window usage) | [V2EX t/1215784](https://v2ex.com/t/1215784) |
| coderfee #47, runstone #79, Hilalum #75 / V2EX | 2026-05-27/28 | Standard (11B) for coderfee | Single sessions or one hour | V2.5-Pro | "9,786,840 / 11,000,000,000"; "3 个多亿 credits" in under 10 interactions; "刚一小时掉了 5 亿" | ≈ ¥0.098; ≈ ¥3+; ≈ ¥5 in an hour | [V2EX t/1215784](https://v2ex.com/t/1215784) |

- A Zhihu snippet says "仅使用了22条 prompt 就干完了 39 元档位套餐一个月的全部份额". It concerns the April plan (60M-credit Lite, before the 2026-05-27 repricing), and I did not open the page, so it is unverified and not comparable. — [Zhihu question 2023373802445318091 (search snippet only)](https://www.zhihu.com/question/2023373802445318091)

**Provider claims (NOT measurements; do not compute a measured multiple from these)**
- The V2.6 pricing cards state "380 亿 Credits = 9.3 x Lite", "820 亿 Credits = 20 x Lite", "= 2.7 x Lite" (Standard), "夜间 0.8x 消耗" and "畅快使用 · 无周限额 · 无 5 小时限额". — [V2EX screenshots in t/1243835](https://www.v2ex.com/t/1243835) (https://i.imgur.com/g8ULSGx.png, https://i.imgur.com/OaGTxZt.png)
- The official doc's task estimates use mimo-v2.6-flash as the baseline: about 200 (Lite), 1,600 (Standard), 5,600 (Pro) and 12,800 (Max) rounds of medium-to-complex tasks. — [MiMo subscription doc (via search result)](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription)
- Credit quotas compared with API prices (my arithmetic on provider figures; the full-utilisation ceiling, not measured). CNY: Lite 41/39 = 1.05×, Standard 110/99 = 1.11×, Pro 380/329 = 1.16×, Max 820/659 = 1.24×. Usage entirely at night (0.8x) raises these by up to 1/0.8: 1.31×, 1.39×, 1.44×, 1.56×. USD: Pro's $0.435/M uncached input (V2EX quote of the official USD rate card) equals 300 credits/token, so 1亿 credits ≈ $0.145. That gives Lite $5.95/$6 = 0.99×, Standard $15.95/$16 = 1.00×, Pro $55.1/$50 = 1.10×, Max $118.9/$100 = 1.19×. — Inputs: [MiMo subscription doc](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription); [V2EX t/1243832 (USD API prices)](https://www.v2ex.com/t/1243832)
- Exchange rate: I made no CNY↔USD conversion of user amounts. The USD figures above use Xiaomi's own USD rate card. The implied rate, ¥3/$0.435, is ≈ 6.90 CNY/USD.

### Inferences
- Plan credits are API-priced by construction. The V2.6 credit coefficients divided by the official CNY API rates give exactly 1亿 credits = ¥1 for Pro and Flash input and output, and for Pro cache hits. So any user figure in credits or "% of quota" converts directly into an API-priced value. Night use (0.8x) understates API value by up to 25%.
- The few measured or derivable windows (rows B and C, plus the older 8–9% Pro reports) suggest light-to-moderate Chinese users consume far less than the allowance. Their realised multiples are well below 1×: about 0.0 (A), about 0.04 (B, if the plan-price rule applied) and about 0.11–0.21 (C). The full-utilisation ceiling is only 1.05–1.24× (CNY). The renewal-offset mechanism refunds unused value into the next renewal, so these single-window multiples understate a renewing user's long-run multiple. That effect cannot be quantified from the evidence.
- None of these data points can be attributed to MiMo-V2.6-Pro or V2.6-Flash specifically. Under the project rule (match the exact model the user names), they all stay at plan level and are unidentified or V2.5-era.

### Gaps
- No V2.6-Pro or V2.6-Flash-specific measured plan usage was found for 2026-09-22..2026-10-23 on V2EX (sov2ex index searched through 2026-10-21), Bilibili (search API), or general web search. The window is short: V2.6 shipped on 2026-09-22, and the first full V2.6 billing month only ended around 2026-10-22.
- Unreachable sources (URLs attempted):
  - linux.do search: https://linux.do/search?q=mimo%20%E5%A5%97%E9%A4%90%20after%3A2026-09-21%20order%3Alatest and https://linux.do/search.json?q=mimo%20plan%20order%3Alatest returned HTTP 403 (Cloudflare challenge).
  - https://linux.do/t/topic/2872583 ("mimo的tokenplan分享") returned HTTP 404.
  - Bilibili video pages via WebFetch returned navigation only.
  - https://api.bilibili.com/x/web-interface/view returned an error page (risk control).
  - Bilibili subtitles and AI summary (x/player/v2, x/web-interface/view/conclusion/get, WBI-signed) returned "账号未登录". The bodies of BV1w1T36oEXg, BV1sVEG6oEPS, BV1mx7Z6pEAb and BV1xfhf6dEQR were therefore not inspected.
- Not directly searched, or no results surfaced through web search: 小红书, Weibo, 即刻, NGA, 微信公众号, 掘金 and 少数派. No such pages appeared in any result set.
- Rows B and C need the exact renewal-offset rule in force on 2026-09-22, which the official doc does not state. They also need each user's previous-month paid price, which is unknown for B. A user says the rule changed to offsetting against last month's paid price.
- Searches run: "小米 MiMo Token Plan 用量 实测"; "MiMo-V2.6-Pro 套餐 额度 用完"; "linux.do MiMo token plan"; "MiMo V2.6 Token Plan 一个月 用了 亿 token"; "小米 MiMo 套餐 回本 V2.6"; "v2ex mimo v2.6 plan 消耗 credits"; ""mimo-v2.6-pro" token plan 体验 一周 消耗"; "小米 MiMo Token Plan 用了多少 额度 截图 10月"; "linux.do mimo v2.6 pro token plan 用量"; "MiMo token plan 性价比 GLM coding plan Kimi 对比 实测 V2.6"; "知乎 MiMo-V2.6-Pro Token Plan 使用体验 额度"; "小红书 小米mimo套餐 用完了"; "v2ex mimo 2.6 token plan 续费 用了"; "mimo-v2.6-flash token plan 额度 消耗 用户"; "MiMo V2.6 API 价格 缓存命中…"; "bilibili 小米 MiMo token plan V2.6 实测 消耗"; ""用完一个月" mimo Token Plan 可以使用多少Token"; ""token plan" mimo 2.6 用了 % 额度 续费 10月". Bilibili API keywords: "mimo token plan", "mimo token plan 用量", "mimo 套餐 额度", "mimo v2.6 token plan", "小米 token plan 实测", "mimo plan 用了". sov2ex: "mimo", "mimo 额度", "token plan", "mimo 套餐", "小米 plan", "coding plan 额度", "mimo 用量".

## Are there user comparisons of MiMo plan value vs GLM / Kimi / MiniMax / 百炼 / 火山方舟 Coding Plans that include measured MiMo usage?

### Takeaway
I found none in the window. The comparisons I found are either quota- or price-sheet based (provider-derived) or compare API to API. The only one that cites actual MiMo plan usage is a June Bilibili video, Standard plan, 2026-05-31..06-04, which reports savings of 10.6% against DeepSeek. Its body was unreachable, and it compares against DeepSeek, not GLM, Kimi, MiniMax or the cloud Coding Plans.

### Cited Findings
- The awesome-coding-plan GitHub repo lists "Xiaomi MiMo Token Plan Pro (mimo-v2.5-pro) ￥329.00 · 380亿 Credits · ￥381 额度价值 · 1.12". Its ratio is defined as "当前周期额度 ÷ 包月价格", so it is quota-derived, not measured, and the arithmetic is internally inconsistent (381/329 = 1.16). No date is shown. — [GitHub mahonzhan/awesome-coding-plan](https://github.com/mahonzhan/awesome-coding-plan)
- V2EX opinions (2026-09-22, no measurements): "他们家的 plan 基本就是 API 打一个很小的折扣" (longaiwp). Another user recommends Volcengine's ¥9.9 plan over MiMo (coderwitt). Another runs "mimo + glm" in parallel (zhouhuade). — [V2EX t/1243835](https://www.v2ex.com/t/1243835)
- linux.do (Ovear, 2026-05-27) says the plan is about 8–9折 against pay-as-you-go. That is a price comparison, not usage. — [linux.do t/2254166](https://linux.do/t/topic/2254166)
- DeepSeek vs MiMo plan, measured but old: Standard ¥99/110亿 credits, "实际使用数据（5月31日-6月4日）", "Token Plan 省10.6%". — [Bilibili BV1mx7Z6pEAb (description chapters)](https://www.bilibili.com/video/BV1mx7Z6pEAb/)
- DeepSeek vs MiMo **API** (not plan), in window: dmonz repriced one month of DeepSeek tokens at MiMo API rates, ¥155.77 against ¥317.88. — [V2EX t/1244361](https://www.v2ex.com/t/1244361)
- Third-party comparison articles exist, but in the snippets I saw they are price- or quota-sheet based and older than the window: a CSDN July comparison, a Zhihu early-May comparison, a watermelonwater "横评", and a txtmix comparison. — [CSDN](https://blog.csdn.net/zhangay1998/article/details/162555439); [Zhihu](https://zhuanlan.zhihu.com/p/2035064344753485174); [watermelonwater](https://watermelonwater.tech/insights/tokenplan%E5%B0%8F%E7%B1%B3minimax%E6%99%BA%E8%B0%B1api%E5%AE%9E%E6%B5%8B/); [txtmix](https://txtmix.com/posts/thoughts/china-coding-plan-comparison/)

### Inferences
- Community consensus in the window is that the MiMo plan is a small discount on API: 5–24% extra credit value at full use, plus a renewal carry-over. Users discuss it as such and rarely post consumption, because the plan has no 5-hour or weekly cap to "hit".

### Gaps
- I did not open the CSDN, Zhihu, watermelonwater or txtmix comparisons in full. Search snippets indicate they are quota- or price-based and predate V2.6. That was not verified line by line.
- No GLM, Kimi, MiniMax, 百炼 or 火山 comparison containing measured MiMo V2.6 plan usage was found.

## Are there reports of hitting the 5-hour / weekly limits with token counts?

### Takeaway
No. The V2.6-era personal MiMo Token Plans advertise no 5-hour and no weekly limit, only a monthly credit pool, and I found no user report of exhausting the monthly pool in the window.

### Cited Findings
- The V2.6 pricing cards (user screenshots, 2026-09-22) state "畅快使用 · 无周限额 · 无 5 小时限额" for Lite, Standard, Pro and Max. — [V2EX t/1243835](https://www.v2ex.com/t/1243835) (https://i.imgur.com/OaGTxZt.png)
- The official doc describes only a monthly fixed allowance, and says service stops when it is exhausted. — [MiMo subscription doc](https://mimo.mi.com/docs/zh-CN/tokenplan/Token%20Plan/subscription)
- Older V2EX burn-rate anecdotes are not limit hits: "刚一小时掉了 5 亿" credits (≈ ¥5) and "3 个多亿 credits" in under 10 interactions (V2.5-Pro, 2026-05-27/28). — [V2EX t/1215784](https://v2ex.com/t/1215784)

### Inferences
- With no rolling caps, the binding constraint is the monthly credit pool. At the 1亿 credits = ¥1 conversion, that pool is worth only ¥41–¥820 of API usage, so "limit hit" reports would be monthly exhaustion. None were found for V2.6.

### Gaps
- No report of monthly-pool exhaustion on V2.6-Pro or V2.6-Flash was found. Bilibili video bodies and linux.do search could not be checked (see the Gaps under the first question).
