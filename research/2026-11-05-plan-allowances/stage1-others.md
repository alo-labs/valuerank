# Stage 1 (plain web search): Google, Kimi, Xiaomi MiMo, MiniMax and DeepSeek, run 2026-11-05

Scope: O71 v1 profile (`data/plan_cost_routes.json` `evidencePolicy.reportEligibilityProfile`). The report window is
2026-10-02 to the 2026-11-01T06:10Z cutoff. This run concentrated on 2026-10-25..11-01, since the previous search ran on
2026-10-25. Each candidate is marked NEW or RECORDED (RECORDED means it is already in `data/plan_reports.json`).
"Qualifies" applies only the O71 rules. It does not mean admitted. Every dollar figure is the agent's arithmetic at API
list prices, unless the text quotes the reporter. Ranges cover the token split the source leaves open. The low end treats
unsplit uncached tokens as input and the high end treats them as output, or the range follows whatever the source
leaves open.

O11 test applied below: a cell needs at least 2 independent non-provisional, non-derived reports. Across the cell's
eligible reports, the largest lower bound must be at most 1.20 × the smallest upper bound.

---

## 1. Google: Gemini 4 Argon / Gemini 4 Carbon (AI Pro $19.99, AI Ultra 5x $99.99, AI Ultra 20x $199.99)

Prices used. Gemini 4 Argon, Standard tier, per 1M tokens: $2.00 input, $0.10 cached, $10.00 output (thinking
included). These are the introductory rates to 2026-11-30, from ai.google.dev/gemini-api/docs/pricing. Gemini 3.8
Flash: $0.75 input, $0.075 cached, $3.75 output (only for context).

Summary
- **AI Ultra 5x, Antigravity, 5-hour: one new qualifying report.** Yiji_Kong (Google AI forum t/196351, 2026-10-28)
  read the language server's `remainingFraction` directly. A clean A/B run and a 42-step session give **$49.2–50.0 per
  5-hour window** at Argon's list price. The reporter's own framing is different: the bucket is "~150 USD" at the price
  the meter really charges, and Argon "consumes exactly 3.0x more quota per dollar than Flash".
- jamie950315 (r/google_antigravity 1xfnvds, 2026-10-26) used the same method and reached the same "3x" conclusion.
  His four Argon probes give **$200 per week** at list price. His tier ("Google AI Ultra") is unstated; it is inferred
  as Ultra 5x, so the report is provisional. He is probably the same observer as Yiji_Kong: same method, same "$150 per
  5h" bucket, same 3× finding, two days apart.
- **Gemini app, Ultra 5x: a separate meter.** Yiji_Kong's follow-up (t/196351 #5, 2026-10-29) measured the Gemini web
  app's weekly pool at 8-decimal precision. One pure-input prompt of about 13,500 tokens implies roughly **$30–36 per
  week**, or about $1.1–1.8 per 5 hours. That is an order of magnitude below Antigravity. Users report that on Ultra the
  app and Antigravity are metered separately (adjutanto, r/GeminiAI 1xiw7ci, 10-29; Much_Blacksmith_5833, 11-04).
- **AI Pro:** no new qualifying Argon report in the window. All new Pro posts give percentages only.
- **AI Ultra 20x:** one priced ledger (ubelai, 10-26). It mixes Argon and Flash in the shared bucket, so it counts only
  at plan level.
- **Gemini 4 Carbon:** still not on any consumer plan at the cutoff. Posts from 11-02 still ask "When can I use carbon
  as a pro user?" (r/GeminiAI 1xltz0f). There are no candidates.
- **Change signals (none documented by Google):**
  - Several users report much lower Argon drain around 2026-10-29/30: Far_Management_7991 ("20x reduction"),
    outofideas234, ChaozR, and AutomateEverything0's removed post "Weekly usage allowance has dramatically
    changed...like 5x increase". Others report no change (Ok-Strawberry6, SteakHausMann, hi-brawlstars). These are
    percentages only, so they are not enough for E18.
  - From 11-03/04, Pro users see Argon drawing from the general Gemini bucket instead of the Argon bucket
    (AdministrativeBit849, Altruistic_Answer120, Street-Location-2414). This is after the cutoff.
  - Difficult-Fee5299 mentions "two Argon resets by Google" (about 10-20..10-27).
  - A Google staff reply (t/196351 #6, Maniraj_Chervirala, 10-29) says subscription limits "reflect available capacity,
    model compute, and total agent work rather than matching API token list prices", and that per-model multipliers
    "are not published because subscription limits adjust dynamically".

### Candidates (Gemini 4 Argon)

| # | Plan / surface | Unit | Observer | URL | Date (UTC) | Tokens | Meter movement | $ at list ($2/$0.10/$10) | NEW/REC | Qualifies |
|---|---|---|---|---|---|---|---|---|---|---|
| G1 | AI Ultra 5x, Antigravity 2.27.0 (shared Gemini 5h bucket), Argon High | 5h | Yiji_Kong | https://discuss.ai.google.dev/t/196351 (#1) | 2026-10-28 04:03 | (a) 14,918 in / 0 cache / 4,233 out; (b) 42 steps: 220,998 in / 3,948,273 cache / 71,432 out | (a) −0.00144340; (b) −0.03154810 of the 5h `remainingFraction` | (a) $0.0722/0.0014434 = **$50.0**; (b) $1.5511/0.0315481 = **$49.2** → $49.2–50.0 | NEW | **Y** |
| G2 | AI Ultra (tier unstated; inferred 5x), Antigravity, Argon | week | jamie950315 | https://www.reddit.com/r/google_antigravity/comments/1xfnvds/ | 2026-10-26 05:03 | four probes, e.g. 16,088 in / 0 / 25,193 out → weekly −0.00142053; 15,683/0/5 → −0.00015703; 41,355/0/14 → −0.00041420; 2,136/39,306/14 → −0.00004174 | weekly fraction deltas | each probe gives **$199.9–200.1/week** (≈$867/month at 52/12). He also states "~$150 per five-hour window" at the 3× card, which is $50 at list | NEW | **Y, provisional** (tier inferred; probably the same observer as G1) |
| G3 | AI Ultra (5x), Gemini web app (separate meter), Argon Low | week (and 5h) | Yiji_Kong | https://discuss.ai.google.dev/t/196351 (#5) | 2026-10-29 07:37 | test 1B: 51,262 characters ≈ "~13,500 tokens" of input, 1 output token, no cache; test 1C (base overhead, a 28-character prompt): weekly +0.00015849 | weekly `percentageUsed` +0.00090908; 5-hourly 0.10→0.12 | $0.0270/0.00090908 = **$29.7/week**, or **$36.0** net of the 1C overhead; 5h: $0.027/0.02 = $1.35 (whole-percent display: $1.08–1.80) | NEW | **Y, weak** (token count estimated from characters; per-turn overhead unknown). A different surface meter from G1/G2, so it should not be pooled with Antigravity |
| G4 | AI Ultra 20x, Antigravity shared bucket | week | ubelai | https://www.reddit.com/r/google_antigravity/comments/1xfnvds/ (comment 19robavwvb5us) | 2026-10-26 09:12 | 2.45 days, 8,061 generations: Argon Low 60.05M in / 549.53M cache / 4.32M out; Argon High 9.50M / 117.96M / 0.93M; Argon Med 1.22M / 23.48M / 0.26M; Flash 3.8 rows (21.29M/257.42M/0.97M; 6.23M/51.67M/0.18M; 2.17M/30.91M/0.32M; table cut off in the archive) | 64% remaining (0.6384909) after the reset at 2026-10-23T22:53Z | Argon $265.61 + Flash ≥$53.29 at list. Mixed models | NEW | N (mixed Argon and Flash in one bucket: plan level only) |
| G5 | "Gemini Ultra" (tier unstated), Antigravity, "99.94% GEMINI 4 (HIGH)" | 14 days | iluvios | https://www.reddit.com/r/google_antigravity/comments/1xlp3sf/ (image i.redd.it/266eeqx0z4zh1.png) | posted 2026-11-02 05:40; data 10-17..11-01 | 699M cached / 91M in / 8.3M out = 799M | "close to 60% at the end of each week" (comment); "never … less than 20% usage left" in a day | $334.90 over 14 days (commenter Gohab2001's table reproduces it) | NEW | N (tier unstated; loose meter reading across two weekly windows; posted after the cutoff) |
| G6 | AI Ultra (tier unstated), Antigravity CLI, `gemini-4-argon-high` | 5h | jyongchulwp | https://discuss.ai.google.dev/t/198073 | 2026-11-04 | three short prompts, no token counts | 307 ppm (interactive) vs 418 ppm (`agy -p`) vs 1,294 ppm cold | n/a | NEW (after cutoff) | N (no tokens) |
| G7 | AI Pro, Antigravity | week | Ok-Strawberry6, ChaozR, SteakHausMann, hi-brawlstars, Comfortable_Travel97, nixgut, xGSTQ, enzo09, behist | r/google_antigravity 1xj84e4, 1xnph3c, 1xmg9eo; forum t/189085, t/196484 | 10-24..11-04 | none | 5–50% of weekly | n/a | NEW | N (percentages only) |
| G8 | AI Ultra 5x / 20x | 5h, week | Mphrts2 (5x: 50%→30% in 10h on Argon High), Even_Particular5334 (5x: 3% weekly, 12% of 5h on three chats), lex_orandi_62 (20x: 2% weekly left), Much_Blacksmith_5833 (5x), needs-more-code (20x: "can't get more than 50% used") | r/google_antigravity 1xj84e4, 1xf09pi, 1xmd0t9, 1xnludg | 10-25..11-04 | none | percentages | n/a | NEW | N (no tokens) |
| G9 | Ultra 5x (removed post "100$ Ai Ultra can give you 140$ of usage") | week | ares0027 | https://www.reddit.com/r/GeminiAI/comments/1xe1mix/ (image 0h695lmj2dxh1.png) | 2026-10-24 | a third-party quota widget: weekly "~15.55M left", 99%, "Weighted $34.98"; 4.5k in / 556 out / 156k cache | 99% remaining | the widget's own dollar estimate | NEW | N (derived by a tool; whole-percent meter barely moved) |
| R1 | AI Pro, Antigravity, Argon | week | Muhammed_Alpler | https://discuss.ai.google.dev/t/190608 | 2026-10-19 | (as recorded) | ~10.2% | $8.47 | RECORDED | (recorded) |
| R2 | AI Pro, Antigravity, Argon Low | week | Faheem_Anis1 | https://discuss.ai.google.dev/t/191879 | 2026-10-23 | (as recorded) | 6% | $11.4–13.4 | RECORDED | (recorded) |
| R3 | AI Pro (inferred), Argon | week | ansofteng | r/GeminiAI 1x6zv2f | 2026-10-16 | (as recorded) | 7% | $7.84–9.04 | RECORDED (provisional) | (recorded) |
| R4 | tier unstated, Argon | week | @spin.pyokosmeme.group | Bluesky | 2026-10-24 | (as recorded) | - | $50 | RECORDED | (recorded) |

Not Argon: Lberondroth (r/google_antigravity 1xk8jm1, 10-31, AI Pro) measured Gemini 3.8 Flash and Opus 5.5 only. Gemini
4 Carbon: no candidate on any surface or tier.

### O11 verdicts (Google)

| Cell | Eligible reports | Verdict |
|---|---|---|
| AI Pro · Argon · week | alpler $8.47, faheem $11.4–13.4 (ansofteng provisional); nothing new | **Not met**: 11.4 > 1.2 × 8.47 = 10.16 |
| AI Pro · Argon · 5h | none (Argon is a weekly-only bucket on Pro) | **Not met** |
| AI Ultra 5x · Argon · 5h (Antigravity) | Yiji_Kong $49.2–50.0; jamie950315 $50 (provisional, probably the same observer) | **Not met**: one non-provisional observer |
| AI Ultra 5x · Argon · week (Antigravity) | jamie950315 $200 (provisional) | **Not met** |
| AI Ultra 5x · Argon · week (Gemini app) | Yiji_Kong $29.7–36.0 (weak) | **Not met**: one report |
| AI Ultra 20x · Argon · any | none (ubelai is mixed-model) | **Not met** |
| AI Ultra (tier unstated) · Argon | spin.pyokosmeme $50/week (recorded), iluvios (N) | **Not met** (no tier) |
| Any tier · Gemini 4 Carbon | none; not offered on consumer plans by the cutoff | **Not met** |

---

## 2. Moonshot Kimi: K3.1 Pro

Prices used: K3.1 Pro API, per 1M tokens: $2.00 input, $0.20 cached, $10.00 output. A reporter's CNY figure is quoted, not
converted. USD tiers and China-region CNY tiers are separate cells. Partition: the recorded 2026-10-24 limit split
(owner decision O84) applies.

Summary
- **International USD tiers:** no new in-window report with tokens. Defiant-Pepper-7263 (Kimi Plus, r/kimi 1xl4r76) gives
  a K3.1 Pro token split at full 5h exhaustion with the monthly meter at 13%. It works out to **$0.22–1.62 per 5h** and
  **$1.7–13.0 per month**. It was posted 2026-11-01T14:42Z and is almost certainly measured after the cutoff, so it is
  listed under "after cutoff". Every other USD-tier post gives percentages only. Two independent Plus users say one
  full 5-hour window ≈ **13% of the monthly pool** (Defiant-Pepper-7263; rubenthechadestj).
- **China legacy Allegretto ¥199:** four new 5-hour readings from the LINUX DO mirror locdd.com, all after the
  10-24 split.
  - SunnyDoll, 10-26: **$9.0–20.8**
  - PaperPlane, 10-26: **$22.7–34.7**
  - StarryWalker, 10-26: **$15.3–27.7**
  - SunnyDoll, 10-29: **$32.2–41.8**

  There is also one weekly reading: TimeMachine, 10-27, **$63–260/week**.
- **China legacy Allegro ¥699:** MoonPostman (10-25) ties a K3.1-Pro-only ledger to the weekly meter, giving
  **$185–191/week**. The reading spans the 10-24 change.
- **China new Max ¥699:** NightRain's month ledger (mixed models, spans the 10-26 reset and the cutoff) and KiteRunner's
  11-04 probe fit are both after the cutoff or derived.
- **Provider event, 2026-10-26 (a reset, not a limit change).** Kimi apologised for "限流及不必要额度消耗" when members
  used K3.1 Pro. It credited every active subscriber 25% of the monthly total ("相当于一周的用量"), with usage below 25%
  reset to 0, and reset weekly limits. It also said it had changed configuration to cut unnecessary subagent calls and
  output length. Sources: Kimi post mirrored at locdd 103808 and 103792; tech.ifeng.com/c/8xWrSDBLrWR;
  t.cj.sina.com.cn/articles/view/1887344341/707e96d502001x4ha. By O112, readings that span 2026-10-26 should be excluded.
- **E18 candidate: the legacy 5-hour window may have doubled about 10-27..10-29.**
  - Spare-Choice-6019 (r/kimi 1xi5bnt, 10-29): "there is an update on 5 hour limit they expand it 100%, and now weekly =
    2.5x 5 hour limit". Previously week = 5 × 5h.
  - Per-window Allegretto values roughly double between 10-26 (~$9–35) and 10-29 ($32–42).
  - KiteRunner's 11-04 probe found that the Allegretto coefficient model no longer fits ("7d / 5h 比例可能变化").
  - DolphinLover's coefficient thread on LINUX DO says it was "最后更新：2026-11-03", but LINUX DO was unreachable.

  This is not verified by two independent per-token fits. If it is accepted, it splits every Kimi plan (O84 rule).
- **Data-quality flag for the existing record.** locdd.com topic 103607 is a mirror of LINUX DO topic 3071240:
  - its #8 is fenglinnet's "43M消耗周额度9%";
  - its #10 is choulei's "实测5h的额度是10美元";
  - its OP "MoonDrinker" posts the Pi-based weekly weights that belong to the 3071240 OP.

  So `moondrinker-allegretto` and `astralyn-allegretto` are very likely the **same observer and the same thread**. More
  generally, locdd shows a fixed pool of pseudonyms that do not match the LINUX DO usernames. Observer identity
  (one observer = one report, independence) **cannot be verified from locdd**. Every locdd candidate below carries this
  caveat. (locdd 77463 contains a shared credential. It was not used or copied.)

### Candidates (K3.1 Pro)

| # | Plan (region) | Unit | Observer | URL | Date (UTC) | Tokens | Meter | $ at list | NEW/REC | Qualifies |
|---|---|---|---|---|---|---|---|---|---|---|
| K1 | Allegretto ¥199 legacy (CN), Claude desktop, k3.1-pro only | 5h | SunnyDoll (locdd pseudonym) | https://www.locdd.com/t/topic/103915 (#1; image oss.locdd.com/2026/10/26/1792995863061.png) | 2026-10-26 06:24 (usage 10:00–14:00 CST) | 31.9M total, cache hit 95.4% (30.43M cache, 1.47M uncached, split not given); 166 k3.1-pro requests; tool cost "¥79.60" | "这是用完一个5H的用量" (a full window) | $6.09 cache + $2.94–14.68 → **$9.0–20.8** | NEW | **Y** (locdd identity caveat; same day as the 10-26 reset, which concerned week/month) |
| K2 | Allegretto ¥199 legacy (CN), K3.1 Pro | 5h | PaperPlane (locdd) | https://www.locdd.com/t/topic/103915 (#6) | 2026-10-26 06:36 | "5h 大概 100M", cache "98.5% 差不多" | full window (approximate) | $19.70 + $3.0–15.0 → **$22.7–34.7** | NEW | **Y, weak** (approximate; locdd caveat) |
| K3 | Allegretto ¥199 legacy (CN) | 5h (week = 5 × 5h derived) | StarryWalker (locdd) | https://www.locdd.com/t/topic/103792 (#12) | 2026-10-26 05:27 | "98.x的缓存命中,现在5小时大概能跑7000万,一周就是3.5亿" | full window (estimate) | 98–99% cache → **$15.3–27.7 per 5h** | NEW | **Y, weak** (capacity estimate; the week figure is derived, so it does not count) |
| K4 | Allegretto ¥199 legacy (CN), K3.1 only this week | week | TimeMachine (locdd) | https://www.locdd.com/t/topic/104222 (#4) | 2026-10-27 04:38 | "消耗 token 72M，周限用量 33% 总的缓存率大概 90~95%" | weekly 33% | consumed $20.9–85.7 → **$63–260/week** | NEW | **Y, wide range** (week started at or after the 10-26 weekly reset; check that the 72M excludes pre-reset tokens) |
| K5 | Allegretto ¥199 legacy (CN) ("补充下，我是老的199套餐" in the next post) | 5h | SunnyDoll / KiteRunner (locdd #7/#8, probably one person) | https://www.locdd.com/t/topic/104985 (#7–#8) | 2026-10-29 15:27 | "今天我5h额度跑完，99.2的缓存命中，跑了1.5亿" | full window exhausted | $29.76 + $2.40–12.0 → **$32.2–41.8** | NEW | **Y** (locdd caveat; possibly after a 5h doubling, see E18 candidate) |
| K6 | legacy plan (tier unstated, CN) | week | NightRain (locdd) | https://www.locdd.com/t/topic/104911 (#2) | 2026-10-29 08:35 | "100%周额度跑了4亿的 3.1pro" (no cache rate) | 100% week | at 97–99% cache: ~$86–199 | NEW | N (tier and cache split unstated) |
| K7 | Allegretto ¥199 legacy | week | RainPoet (locdd) | https://www.locdd.com/t/topic/105558 (#8) | 2026-10-31 11:03 | "大概一周 2.5 亿" | - | - | NEW | N (no split; no meter detail) |
| K8 | Allegro ¥699 legacy (CN), k3.1-pro only | week | MoonPostman (locdd) | https://www.locdd.com/t/topic/103774 (#1; images oss.locdd.com/2026/10/26/1792949294790.png, …973.png) | 2026-10-25 17:28 | daily ledger 10-23..10-26: total 5,490,110 in / 1,133,482 out / 237,680,029 cache = $69.85 (the tool's own price equals list: 10-24 row $17.66 reproduces); 10-24..26 = $69.30 | weekly "37% used, resets in 4d 21h 12m" (window opened ≈10-23 22:00 CST) | $69.30–69.85 / 0.365–0.375 → **$185–191/week**; reporter's "外推周额度大概 6.6 亿 token" | NEW | **Y?** The reading spans the 10-24 split (the increase came on Saturday 10-24 during the day), so it is probably excluded |
| K9 | Max (new, CN ¥699) | month | NightRain (locdd) | https://www.locdd.com/t/topic/106583 (#1; images oss.locdd.com/2026/11/04/1793758882121.png, …2710.png, …2898.png) | posted 2026-11-04 02:21 | cycle (all models) 1,923M tokens = 1,853M cache + 71M fresh in+out; k3.1-pro daily 10-26..11-03: 1,569.3M total, 45.94M fresh input, 2.95M output | cycle 40.05% (11-03) | if all K3.1 Pro: ≈$547 consumed → ≈$1,366/month (derived) | NEW (after cutoff) | N (mixed models; spans the 10-26 reset and the cutoff) |
| K10 | Max (new, CN) | 5h | KiteRunner (locdd) | https://www.locdd.com/t/topic/106583 (#12) | 2026-11-04 04:45 | probe: 4 requests, 41,137 in / 81,920 cache / 2,112 out = 0.51% of 5h; fit 5h weights input 0.08667, cache 0 [0–0.000923], output 0.7144 per 1M | 5h 4.79% | window ≈ 11.5M input ($23.1) or 1.40M output ($14.0); at 97.5% cache with input = 2.5 × output: ≈$40–45 | NEW (after cutoff) | N (after cutoff; derived fit) |
| K11 | Plus (USD, new), Kimi Code, K3.1 Pro high | 5h, month | Defiant-Pepper-7263 | https://www.reddit.com/r/kimi/comments/1xl4r76/ (image i.redd.it/tkajwz6jj0zh1.jpeg; comments 19s14mnkk2y5e, 19s2xfwippvdx) | posted 2026-11-01 14:42 | "kimi-code/k3.1-pro input 778k output 6.8k total 785k" (cache not split out) | "5h limit 100% used", "Monthly limit 13% used (kimi 0% · code 13%)" | 5h: $0.22 (all input cached) … $1.62 (all uncached); month: /0.125–0.135 → $1.7–13.0. Reporter: "roughly $12.42" for the month | NEW (after cutoff) | N for the window: measured after 06:10Z on 11-01 (5h window opened ~19 min before the screenshot). Also a lower bound, because the background explore agents that hit 429 may be outside "session usage". The reporter's next session: "10 million + token" for the same 13% (no split) |
| K12 | Plus (USD), mixed K3.1 Pro + K2.8 Preview | 5h vs month | rubenthechadestj | https://www.reddit.com/r/kimi/comments/1xlh8su/ | 2026-11-01 23:05 | none | "a single maxed out 5h limit = 13% of the entire monthly usage limit" | n/a | NEW | N (no tokens; mixed) |
| K13 | USD tiers: Plus (xtmzhd0 10-30; Optimal-Help9991 11-02, 44.48%), Pro $39 (Katze47 10-31; ShortGuitar7207 "entire month in 3 days"; Chaosuka 11-03), Max $99 (nev3rfail 10-27, 36% monthly in about a day; Avocados_number73 2–3% per day) | various | various | r/kimi 1xfscur, 1xlk0s1, 1xkc46l, 1xlh8su, 1xmr8vv, 1xdkngh | 10-27..11-03 | none | percentages | n/a | NEW | N (percentages only) |
| K14 | legacy "200老套餐" (CN) | month | WindGoesOn (locdd) | https://www.locdd.com/t/topic/104683 (#11) | 2026-10-28 | none | "一天写代码用完了13%月额度" | n/a | NEW | N |
| K15 | Allegretto legacy | week | InkBlue (locdd) | https://www.locdd.com/t/topic/106606 (#6) | 2026-11-05 | "一周蹬个4亿没问题" | - | - | NEW (after cutoff) | N |
| - | fcten t1/t2, Astralyn, kojimako, hanashiro, choulei, raymondchau, MoonDrinker, okarin, weibo table, waximabbax | - | - | (see `data/plan_reports.json`) | ≤10-25 | - | - | - | RECORDED | (recorded; see the duplicate-observer flag above) |

### O11 verdicts (Kimi, post-10-24 partition; a further split may follow if the ~10-27/29 5h change is accepted)

| Cell | Eligible reports | Verdict |
|---|---|---|
| Plus (USD) · 5h / month | none in the window after the split (waximabbax $1.37 is from 10-24; Defiant-Pepper is after the cutoff) | **Not met** |
| Pro / Max / Ultra (USD) | none | **Not met** |
| Allegretto ¥199 (CN) · 5h | fcten t2 $9.59 (10-25, RECORDED); K1 $9.0–20.8; K2 $22.7–34.7; K3 $15.3–27.7; K5 $32.2–41.8 | **Not met**. Largest lower bound 32.2 (22.7 within 10-25..26) vs smallest upper bound 9.59 → ratio > 1.20. fcten t2 and K1 alone would pass (9.59 ≤ 1.2 × 9.59), but the cell's other reports disperse. K1–K3 and K5 carry the locdd identity caveat |
| Allegretto ¥199 (CN) · week | K4 $63–260 (Astralyn/MoonDrinker are derived and are the same observer) | **Not met** |
| Allegretto ¥199 (CN) · month | recorded only (fcten t2 $240, Astralyn $279 derived) | **Not met** |
| Allegro ¥699 (CN) · week | K8 $185–191 (spans the 10-24 split); kojimako $167 is derived | **Not met** |
| Max ¥699 new (CN) · 5h / month | K9 and K10 (N); okarin derived (recorded) | **Not met** |
| Plus / Pro / Ultra new (CN) | none new (weibo table recorded, pre-split) | **Not met** |

---

## 3. Xiaomi: MiMo-V2.6-Pro / MiMo-V2.6-Flash (Token Plan Lite / Standard / Pro / Max)

Prices used, per 1M tokens:
- V2.6-Pro: $0.0036 cache hit, $0.435 cache miss, $0.87 output.

The credit quotas on the Token Plan subscription page are unchanged (mimo.mi.com/docs/en-US/tokenplan/…/subscription,
via search 2026-11-05):

| Tier | Monthly credits |
|---|---|
| Lite | 4.1B |
| Standard | 11B |
| Pro | 38B |
| Max | 82B |

Off-peak (00:00–08:00 Beijing time) burns 20% fewer credits. The O46 provider-derived ceilings stay as recorded.

Summary: **no new in-window end-user report** for either model on any tier.
- Reddit comment search turned up no new metered figures, only TheVoyant again (RECORDED).
- OpenCode Go mentions are about a third-party plan.
- locdd 104988 #4 (10-29) says "mimo官宣加了一次额度". The thread is about the MiMo Desktop subscription; the OP says
  "注意这个不是mimo的token plan". It is unverified and not a Token Plan change.

| # | Plan | Unit | Model | Observer | URL | Date | Tokens / meter | $ | NEW/REC | Qualifies |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | Max | month | V2.6-Pro | TheVoyant | i.redd.it/xw17jwr9fbxh1.png; r/ClaudeCode 1xcwfob, 1xdljo1, 1xdznh3 (10-24: "Mimo gives several Billions of compute for $100 a month") | 10-21..24 | 1,029,044,569 tokens = "barely 12%" / 13% | $80–105 | RECORDED | (recorded) |
| M2 | Lite | month | V2.6-Pro | AppleHuman8535 | r/opencode 1x71142 | 10-15 | "$5 … around $4.60" | $4.6 | RECORDED | (recorded) |
| M3 | Standard | month | unclear | Houssein_ | r/openclaw 1u2wdo4 (pgmbow6) | 10-14 | "29% of my allowance (around 3–4 billion tokens)" (credits or tokens unclear; "the cheapest model") | n/a | seen in stage 1 (near-miss) | N |
| M4 | (Qwen vs MiMo plan advice) | - | - | Typical_GeorgeJungle | r/openclaw 1x14vzq | 10-09 | advice only | - | NEW | N |

O11 (MiMo): every cell (V2.6-Pro × Lite/Standard/Pro/Max; V2.6-Flash × all tiers) has **at most one** report →
**Not met**. The owner O46 ceilings remain the route (O62: one report alone does not replace them).

---

## 4. MiniMax: MiniMax-M3.1-Flash (M Plan Go $22 / Explore $55 / Build $132; legacy Token Plan)

Prices used, per 1M tokens: $0.15 input, $0.015 cache read, $0.60 output.

Summary: **no new qualifying report.** Nothing found ties M3.1-Flash consumption to a meter on a named M Plan tier
(Go/Explore/Build) after GA (2026-10-19).

| # | Plan | Unit | Observer | URL | Date | Content | NEW/REC | Qualifies |
|---|---|---|---|---|---|---|---|---|
| X1 | legacy Token Plan Max (annual, "under 1200 RMB … about $15/mo") | week | Illustrious-Many-782 | https://www.reddit.com/r/MiniMax_AI/comments/1xjt5o1/ | 2026-10-30 22:18 | maxed the plan this week with "1.8B tokens" plus thousands of TTS clips and images and 2–3 videos per day; Flash used for "simpler programming tasks" | NEW (same observer as RECORDED R1) | N (mixed models and modalities; no cache split) |
| X2 | "$20 token plan" | - | ahmedranaa | r/MiniMax_AI 1xgz8s0 | 10-27 | speed complaint only | NEW | N |
| X3 | (third-party plan comparison) | - | LinsaFTW | r/opencode 1xcoajv | 10-22 | "x4 times more usage" than DeepSeek; not first-party | NEW | N |
| - | Illustrious-Many-782 R1, AwayTeamRedShirt R2, Money-String4165 R3, nnayrdev R4, ConsiderationNo9952 | - | - | - | ≤10-17 | (legacy Token Plan or M3.1-Flash-Preview) | RECORDED | (recorded, provisional) |

O11 (MiniMax): Go, Explore and Build × M3.1-Flash have 0 eligible reports. The legacy Token Plan cells have only
provisional Preview-era reports → **Not met** everywhere.

## 5. DeepSeek

Confirmed again on 2026-11-05: https://api-docs.deepseek.com/quick_start/pricing describes pay-as-you-go billing only
(top-up or granted balance). It mentions no subscription, plan or membership. deepseek-flash
(DeepSeek-V4.1-Flash-1017), per 1M tokens:

| Period | Cache hit | Cache miss | Output |
|---|---|---|---|
| Off-peak | $0.003 | $0.15 | $0.60 |
| Peak (01:00–04:00 and 06:00–10:00 UTC, Mon–Fri) | $0.006 | $0.30 | $1.20 |

There is no first-party plan, so there are no cells.

---

## After-cutoff list (dated after 2026-11-01T06:10Z or measured after it)

| Observer | Provider / plan / model | Figure | Note |
|---|---|---|---|
| Defiant-Pepper-7263 | Kimi Plus (USD), K3.1 Pro | $0.22–1.62 per 5h; $1.7–13.0 per month (5h = 13% of month) | lower bound (background agents) |
| NightRain (locdd 106583) | Kimi Max new (CN), mixed | ≈$1,366/month if all K3.1 Pro (derived) | spans the 10-26 reset and the cutoff; mixed |
| KiteRunner (locdd 106583 #12) | Kimi Max new (CN), K3.1 Pro | ≈$40–45 per 5h at an assumed mix (fit) | derived |
| InkBlue (locdd 106606) | Kimi Allegretto legacy | "一周蹬个4亿" | vague |
| iluvios | Google AI Ultra (tier unstated), Argon | $334.90 over 10-17..11-01, about 40% of each week | loose meter |
| jyongchulwp | Google AI Ultra, Argon High, CLI | 307 / 418 / 1,294 ppm per 3 prompts | no tokens |
| AdministrativeBit849, Altruistic_Answer120, Street-Location-2414 | Google AI Pro | Argon billed to the general Gemini bucket (11-03/04) | possible change after the cutoff |

## Queries and venues

Web search:
1. "Google AI Ultra" "5x" $99.99 plan Antigravity
2. MiMo token plan V2.6-Pro usage "%" credits billion tokens month report (extended)
3. Kimi K3.1 Pro 会员 额度 实测 5小时 token 缓存 v2ex OR zhihu

Pages fetched:
- antigravity.google/docs/plans (no prices, no Argon or Carbon quotas, no 5x/20x)
- api-docs.deepseek.com pricing

Google AI developer forum (search.json, `after:2026-10-01`, pages 1–2):
- argon weekly order:latest; argon quota/tokens/limit/usage after 10-24..26; carbon after:2026-10-28; argon ultra
- argon tokens; argon "cache read"; argon remainingFraction; argon "API value"; argon litellm; argon "input tokens";
  argon "weekly limit" tokens; argon quota tokens; argon "5-hour" tokens; ultra argon tokens; argon $; quota per dollar;
  argon cost quota; gemini app usage argon tokens; argon ppm; argon percentageUsed; carbon quota; carbon tokens
- 146 topics scanned through /raw for posts with both a token count and a percentage
- topics read in full: 196351, 198073, 197997, 197139, 196484, 198255, 195006, 197768, 189085, 189747, 191218, 195955

Reddit (arctic-shift):
- Post listings after 2026-10-24 for r/google_antigravity, r/GeminiAI, r/Bard, r/GoogleGeminiAI (973 posts) and r/kimi
  after 2026-10-25 (75 posts).
- Post listings after 2026-10-02 for r/MiniMax_AI, r/opencode, r/opencodeCLI, r/LocalLLaMA, r/ClaudeCode, r/openclaw
  (1,556 posts).
- About 70 threads dumped with their comments.
- Comment body searches:
  - "mimo" in 9 subreddits
  - "tokens", "5 hour" and "monthly" in r/kimi
  - "kimi" in r/ClaudeCode, r/opencode, r/opencodeCLI
- Screenshots read: i.redd.it tkajwz6jj0zh1, khz90zrom3zh1, 266eeqx0z4zh1, 0h695lmj2dxh1, 1oa9dfvw9azh1, wtodx1e1xazh1

Hacker News (Algolia, created after 2026-10-02): kimi, kimi code, moonshot, argon, antigravity, mimo, minimax (about 1,400
hits filtered for plan + % + tokens/$). No new candidates; waximabbax is RECORDED.

LINUX DO (via the locdd.com mirror, search.json and topic JSON):
- Searches:
  - Kimi: kimi 额度; k3.1 5h; kimi 用量; kimi 周限; allegretto; kimi 实测; kimi 3.1; k3.1 pro 额度; kimi 套餐; kimi 重置;
    kimi 美元; kimi api 价格 额度; kimi plus; kimi max 699; kimi 199; kimi 月额度; 扣费系数; Allegretto 扣费;
    计费方程 Allegro; 5h 权重; kimi 5h 翻倍; kimi 5小时 翻倍; kimi 5h 额度 提升; kimi 周限 2.5; kimi 暗改;
    kimi 调整 额度 10月; kimi code 额度 变化
  - MiMo and MiniMax: mimo token plan; mimo 套餐; mimo credits; mimo 额度; 小米 token plan; mimo v2.6 pro 额度;
    minimax m plan; minimax 套餐 额度; m3.1 flash 额度; minimax coding plan
- Topics read: 103808, 103792, 103915, 104222, 104911, 104985, 105558, 106583, 106606, 104683, 103774, 103607, 104988,
  77463, 100518 (with images).

## Unreachable or limited

- **LINUX DO directly:** 403 (Cloudflare). A reader-proxy fetch was refused by this environment's policy and was not
  pursued. As a result, DolphinLover's Allegretto coefficient thread (updated 2026-11-03) and the original usernames
  behind locdd pseudonyms could not be checked.
- **arctic-shift:**
  - rate limits and timeouts on some listings: r/XiaomiMiMo (empty or timeout), r/kilocode, r/opencode and
    r/opencodeCLI windows, r/ClaudeCode from 10-02
  - comment body search returned 422 for r/LocalLLaMA and r/MiniMax_AI
  - Python's default user agent got 403
- **Other venues:**
  - pullpush: 521
  - V2EX API v2: 404
  - Zhihu, X, Bluesky, YouTube and GitHub search: not attempted (blocked in earlier runs)
  - Google forum topic JSON with `?print=true`: 422 (`/raw` was used instead)
  - Removed Reddit posts (1xe1mix, 1xjilhr, 1xiw8iw, 1xfzvxv): body text gone
