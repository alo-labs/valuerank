# OpenAI ChatGPT / Codex plan allowances: stage-2 verification and extension (2026-11-05)

Scope: user reports of API-list-priced Codex usage per meter fraction for GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Astra, GPT-6 Luna and GPT-5.6 Luna on Plus, Pro 100, Pro 200 (incl. grandfathered 20x) and Pro 500. Window: measured at least partly 2026-10-02 .. 2026-11-01T06:10Z. Rules: `data/plan_cost_routes.json` evidencePolicy.reportEligibilityProfile (O71 v1 / E270). Prices as in stage 1, per 1M tokens: Sol $2 / $0.10 cached / $10 output; Astra $10 / $1 / $50; Terra $1 / $0.05 / $5. Fast = 2.5×, Ultrafast = 8× (`plan_reports.json` speedModeMultipliers).

Access notes: GitHub REST/GraphQL for openai/codex were refused in this session ("GitHub access to this repository is not enabled", "GraphQL is not available"), and api.github.com returned 403 to WebFetch. Issue text was therefore read through rendered github.com pages (WebFetch, plus an r.jina.ai rendering for #51088). Exact comment `created_at` timestamps could not be retrieved. Only dates were visible.

Relevant split dates (OpenAI) in the profile: price split 2026-10-11 (all plans: "long-context fees removed on subscriptions"); limit split 2026-10-29 (Pro 100/200/500, factor 2.0); limit split 2026-09-29 (Pro 200, DevDay 20x→10x for new subscriptions); reset days that exclude spanning readings: 10-07, 10-10, 10-12, 10-14, 10-17, 10-19, 10-21, 10-22, 10-24, 10-27; accounting-fault days 10-16, 10-17.

## 1. Do the stage-1 qualifying and near-qualifying candidates say what stage 1 recorded?

### Takeaway
jitendersingh0411 and aiplans/hd264 are confirmed as stage 1 recorded, with two corrections. First, jitendersingh0411's Oct 31 "30 pp" is one segment of a 93-point drop that the post never reconciles. Second, Oleg-125 is unambiguous: 67% was *consumed*. That collapses the recorded $3.6–7.4 range to about $3.6–3.7 per 5h. The aiplans account is "Pro 200" by owner confirmation only; neither source says whether it is 20x or 10x.

### Cited Findings

**jitendersingh0411, openai/codex #55210 (comment dated Oct 31, 2026). Plus, GPT-6.1 Sol, 5h**
- He is a commenter, not the issue author. The issue was opened Oct 19, 2026 by gaborbanyai7-boop, titled "[Windows][GPT-6.1 Sol][Fast] Sudden excessive Codex usage/quota depletion after update (Oct 2026)". The author's body says "Subscription: ChatGPT Pro", "Speed: Fast" and gives no token or percentage numbers. The Fast flag belongs to the issue author, not to jitendersingh0411 — [#55210](https://github.com/openai/codex/issues/55210)
- His environment block, verbatim: "Rapid Codex quota depletion after Windows app updates (Plus / GPT-6.1 Sol / High)"; "Subscription: ChatGPT Plus (unchanged)"; "Model: GPT-6.1 Sol"; "Reasoning: High"; "Platform: Windows desktop app"; "Incident: October 31, 2026". It says nothing about speed, Fast, service tier, Codex version or context size — [#55210](https://github.com/openai/codex/issues/55210)
- His comparison table, as rendered: Quota consumed 30% | 30%; Input tokens ~13.21M | ~5.19M; Output tokens ~68.9K | ~29.0K; Cached input ~99.0% | ~99.4%; Elapsed time ~67 min | ~7 min (Oct 25 | Oct 31) — [#55210](https://github.com/openai/codex/issues/55210)
- Method, verbatim: "These figures are calculated from differences between cumulative token counters in the local JSONL session records", aligned with the recorded five-hour quota percentages — [#55210](https://github.com/openai/codex/issues/55210)
- Narrative, verbatim: "my five-hour allowance dropped from **100% remaining to just 7% within approximately 30 minutes**" "(3:42–4:12 PM IST)". He also says "approximately **2.5× fewer recorded input tokens corresponded to the same 30-percentage-point quota deduction**" and "I'm not asserting a confirmed metering bug" — [#55210](https://github.com/openai/codex/issues/55210)
- He gives no clock time or before/after percentages for the Oct 25 reading. The ~7 min table segment versus the 30-minute, 93-point narrative is not reconciled in the post — [#55210](https://github.com/openai/codex/issues/55210)
- Stage 1's arithmetic checks out:
  - Oct 25: c ≈ 13.08M × $0.10 + u ≈ 132K × $2 + o 68.9K × $10 = $2.26 per 30 pp → $7.54/5h.
  - Oct 31: c ≈ 5.16M + u ≈ 31K + o 29.0K = $0.87 per 30 pp → $2.89/5h.
  - Allowing for "~" rounding of the token counts and cache %, plus ±1 pp on the meter, the range is $2.78–7.84 (computed here from the quoted figures).
- Other commenters in #55210 (erniecohen Oct 19, wumeijun666 Oct 27, Pro) give token totals or meter rates, never both — [#55210](https://github.com/openai/codex/issues/55210)

**Oleg-125, openai/codex #51088 (comment dated Oct 11, 2026). Plus, GPT-6.1 Sol medium, 5h**
- Verbatim: "I can independently confirm a very similar quota-drain issue on ChatGPT Plus / Windows / Codex CLI 0.162.1". Model GPT-6.1 Sol, Medium effort; no mention of "fast" or service tier — [#51088](https://github.com/openai/codex/issues/51088)
- Oct 11 session, verbatim: "In another approximately 40-minute review/testing session, usage went from essentially a fresh allowance to:" / "67% of the 5h allowance consumed" / "10% of the weekly allowance consumed" / "only 215K context used at the end" — [#51088](https://github.com/openai/codex/issues/51088)
- Token telemetry "for that affected session", verbatim: `total=287,812 input=232,120 cached input=14,130,560 output=55,692 reasoning=19,068` — [#51088](https://github.com/openai/codex/issues/51088)
- No clock time, timezone or reset timestamp is given for the Oct 11 session; the comment header shows only "on Oct 11, 2026". All the clock times in the comment (19:48:30, 20:23:24, 10:55:29, 12:21:41, "Europe/Sofia, UTC+3") belong to Oct 10 — [#51088 via r.jina.ai](https://r.jina.ai/https://github.com/openai/codex/issues/51088)
- Repricing (computed here): total = input + output (232,120 + 55,692 = 287,812), so "input" is uncached input and reasoning sits inside output.
  - u 232,120 × $2 = $0.464; c 14,130,560 × $0.10 = $1.413; o 55,692 × $10 = $0.557. Total $2.434 per 67 pp → **$3.63/5h**.
  - With ±1 pp: **$3.58–3.69**.
  - The recorded upper value of $7.4 ("if 67% remained") is contradicted by the word "consumed".
- Other #51088 readings, none eligible:
  - VecnyTeoretik (Oct 18): gpt-5.6-sol, not a cohort model.
  - xu62u4u6 (Oct 28): model and plan not given.
  - kapcina69's issue body (Oct 5): "Say hello" ×18, Plus, model not given; 5h 49% → 52% — [#51088](https://github.com/openai/codex/issues/51088)

**hd264 / aiplans.dev, V2EX t1253221 and the aiplans report files. Pro 200, Astra and Sol, weekly**
- V2EX topic title: "Codex Pro 200 复测： GPT-6.1 Sol 每周至少约 2.74 亿 tokens（条件下界，附测法）", by hd264, posted Oct 30. Verbatim: "只适用于 ChatGPT Pro 200 ，不适用于 Pro 100 / Pro 500 。" and "「 Pro 200 额度升级」是账号持有人报告的，我没有独立核验升级政策和倍率。" — [V2EX t1253221](https://www.v2ex.com/t/1253221)
- The post says nothing about subscription date, 20x vs 10x, or grandfathering. No reply contains an eligible measurement: jackerbauer measured DeepSeek; foursking's "一周 ccswitch 统计 9.4b" has no plan, model or % — [V2EX t1253221](https://www.v2ex.com/t/1253221)
- aiplans 10-28 report (Astra main test):
  - "主测 28 次，2,595,323 tokens；同一周窗口已用 89% → 92%，即时与延迟读数一致；控制会话累计计数未变" and "普通输入 2,320,149；缓存读取 271,104；输出 4,070；缓存写入 0".
  - Calls ran 2026-10-28 from ~06:31:16Z. The weekly window reset was "2026-11-02T06:22:01Z".
  - JSON: `plan`="ChatGPT Pro 200 (Codex)", `tierSource`="account_owner_confirmation". The ledger has no speed or service-tier field.
  - Source: [aiplans 10-28](https://aiplans.dev/reports/codex-models-2026-10-28.md) (+ [.json](https://aiplans.dev/reports/codex-models-2026-10-28.json))
- Repricing (computed here): $23.20 + $0.27 + $0.20 = $23.68. At 3 pp that is **$789/week**; at 4 pp to 2 pp it is **$592–1,184**. This matches stage 1.
- The 10-28 Sol batches were not published. The last batch read 92% → 94% immediate and then 0% settled, with the reset changing to 2026-11-04T06:35:21Z. aiplans wrote "没有把 92→0 当作消费" — [aiplans 10-28](https://aiplans.dev/reports/codex-models-2026-10-28.md)
- aiplans 10-30 report (Astra main test):
  - Verbatim: "账号持有人确认仍为 Pro 200，并已暂停其他模型任务；本次升级属于用户报告，未独立核验升级政策和倍率。"
  - The run: "主测60次连续区间 49% → 53%，即时及延迟读数一致，重置时间不变，控制会话累计 token 计数未变。普通输入 4,765,206；缓存读取 806,400；输出 8,733；缓存写入 0。"
  - First call 2026-10-30T06:36:41Z; reset 2026-11-04T06:35:31Z; JSON `upgradeSource`="account_owner_report_not_independently_verified".
  - Source: [aiplans 10-30](https://aiplans.dev/reports/codex-models-2026-10-30.md) (+ [.json](https://aiplans.dev/reports/codex-models-2026-10-30.json))
- Repricing (computed here): $47.65 + $0.81 + $0.44 = $48.90. At 4 pp that is **$1,222/week**; at 5 pp to 3 pp it is **$978–1,630**. This matches stage 1.
- 10-30 Sol: "主测59次成功，已知5,484,515 tokens，周读数48% → 49%，重置时间稳定，但控制会话计数有增量" → "条件下界 274,225,750 tokens … 没有有限上界，也不发布点估计". This is a lower bound only — [aiplans 10-30](https://aiplans.dev/reports/codex-models-2026-10-30.md)

### Inferences
- jitendersingh0411 still qualifies for Plus × Sol × 5h: exact tier and model, a meter fraction, inside the window, and neither Oct 25 nor Oct 31 is a reset or fault day. Speed is unstated; treat it as standard, but do not import the issue author's "Fast". The 7-min vs 30-min inconsistency makes the per-reading attribution soft. It is still one observer carrying [$2.78, 7.84].
- Oleg-125's record should be corrected to about [$3.58, 3.69]. The "meter direction ambiguous" note is refuted by "consumed".
- aiplans 2a and 2b are one observer with per-period readings: valid for the Pro 200 split test, but only one report per partition. The Pro 200 variant (grandfathered 20x vs new 10x) is unstated in every source checked. An owner-reported "upgrade" after 10-29 fits either a 10x account that was doubled or a 20x account that was doubled, so the tier key stays provisional.
- The post/pre Astra point ratio is 1,222 / 789 ≈ 1.55 in dollars (139.5M / 86.5M ≈ 1.61 in tokens). The rounding ranges allow 978 / 1,184 = 0.83 up to 1,630 / 592 = 2.75. The doubling is neither confirmed nor refuted, as aiplans itself says ("新区间与其重叠…不能用点估计之比证明升级倍率").

### Gaps
- Exact `created_at` timestamps for the Oleg-125 and jitendersingh0411 comments could not be read: the GitHub API was blocked and the rendered pages show dates only.
- jitendersingh0411's Oct 25 clock time and starting percentage are not stated in the source.

## 2. Which side of the 2026-10-11 split is Oleg-125 on, and is the aiplans Pro 200 account grandfathered 20x or new 10x?

### Takeaway
Oleg-125's session is dated Oct 11, the split day itself, with no clock time, so its side cannot be fixed by timestamp. Assigning it to the post-split partition rests only on the convention that a split takes effect on its date. The price change cannot affect this reading in substance: its context peaked at 215K, below the 272K long-context threshold. The aiplans account's 20x/10x status is unstated.

### Cited Findings
- The comment opens the Oct 11 reading with "I saw similar abnormal behavior again on Oct 11" and gives no start or end time. The comment itself is dated "Oct 11, 2026" — [#51088 via r.jina.ai](https://r.jina.ai/https://github.com/openai/codex/issues/51088)
- The only Oct 10 events the comment records are a banked full reset (10:55:29 at 5h 30% / weekly 98%, then 12:21:41 at 5h 0% / weekly 0%) and a session from 19:48:30 to 20:23:24 (Europe/Sofia, UTC+3). The Oct 11 session therefore starts after that, "essentially a fresh allowance" — [#51088](https://github.com/openai/codex/issues/51088)
- "only 215K context used at the end" — [#51088](https://github.com/openai/codex/issues/51088)
- The profile's 2026-10-11 split is typed "price", with basis "provider announcement, Day 7 (O77): long-context fees removed on subscriptions" (`data/plan_cost_routes.json`, partitionSplits). The neighbouring reset splits on 10-10 and 10-12 do not bracket a single-day session, so the Oct 11 session spans neither.
- One Pro 200 holder states the 10x cohort explicitly: "My current Pro 200 subscription began on **October 6, 2026** … I report that this account had the lower 10X allowance before October 29". This is qiyuanye0825, who gives weekly % only (Oct 28 0% → 4%, Oct 29 4% → 19%, Oct 30 19% → 26%, Oct 31 26% → 30%) and no tokens, so the post is not a report — [OpenAI forum 1402804 #6](https://community.openai.com/t/1402804/6)
- The aiplans and V2EX sources say only "ChatGPT Pro 200" (owner confirmation) and an owner-reported "升级" — [aiplans 10-30](https://aiplans.dev/reports/codex-models-2026-10-30.md); [V2EX t1253221](https://www.v2ex.com/t/1253221)
- Day 25 announcement as quoted on the forum: "OpenAI is doubling usage limits for Pro 100, Pro 200, Pro 500, and Business Premium, effective today. Following community feedback, the limits for Pro 200 will not be reduced." — [OpenAI forum 1403525 #117](https://community.openai.com/t/1403525/117)

### Inferences
- **Oleg-125 placement.** If the split date opens the new partition, which is the plain reading of "splits … at that change's date", Oleg is post-10-11. That convention also matches the comment being posted on Oct 11.
  - The Sofia-local date could map to Oct 10 UTC only if the session ran 00:00–03:00 local. Nothing suggests that.
  - Its pricing is the same on either side of the split, because the context stayed under 272K.
- **aiplans Pro 200 tier.** Leave it "Pro 200 (variant unstated)", provisional for the grandfathered-20x key.
  - An owner-reported "upgrade" after an announcement that doubled every Pro tier says nothing about the cohort.
  - qiyuanye0825 shows that new 10x Pro 200 accounts existed in the window, so 10x cannot be ruled out.

### Gaps
- No source gives the hour at which the Oct 11 long-context change took effect, and none gives Oleg-125's session clock time.
- No source gives the aiplans account's subscription date.

## 3. Reports stage 1 missed (window 10-02..11-01T06:10Z), with emphasis on Pro after 10-29

### Takeaway
Nothing new qualifies. Searches of late-October openai/codex issues and of OpenAI forum posts after 10-28 turned up only meter impressions, tier-unstated readings, or Fast-mode readings with no starting meter value. There is still no second priced Pro reading after 10-29.

### Cited Findings
- **mooyee233-ctrl, #56890 (Oct 26, 2026)** — [#56890](https://github.com/openai/codex/issues/56890)
  - Reported: `gpt-6.1-sol`, medium, "service tier `priority`" (Fast). Input 7,595,762 (6,670,592 cached), output 58,835 ("Replay's own spend record"). "use up the entire 5-hour window in about 6 minutes".
  - Plan not stated; starting meter level not stated.
  - Computed here: $1.85 + $0.67 + $0.59 = $3.11 standard, about $7.8 standard-equivalent at 2.5×. This is a lower bound only, so it does not qualify.
- **MatthieuStigler, #56890 (Nov 1, 2026)** — [#56890](https://github.com/openai/codex/issues/56890)
  - Reported: gpt-6.1-sol medium, priority tier; 7,484,519 input / 6,231,936 cached / 64,767 output; "approximately $7.58 in estimated API-equivalent costs".
  - No meter reading and no plan, so it does not qualify.
- **SwanVods (Oct 25) and emincan2000 (Oct 29), #56890**: Plus, weekly −16% / −15% with the 5h window exhausted. No tokens, no model — [#56890](https://github.com/openai/codex/issues/56890)
- **h3tek, #55997 (Oct 27)** — [#55997](https://github.com/openai/codex/issues/55997)
  - Confirms stage 1: GPT-6.1 Sol "Max", Codex Desktop for Windows, fresh input 2,141,700 / cached 24,327,424 / output 169,628 (reasoning 50,276). "10:35:13 — 4% used" → "10:43:44 — 99% used", 5-hour window. Plan/tier not stated.
  - Additional exclusion grounds: Oct 27 is a global-reset day (O112), and the 13 subagent sessions' models are not given.
- **loisoi1123, #55997 issue body**: Plus, "Sol High" (version not given), "approximately 15 million tokens", 100% → 0% in about 11 min. No split; dated Oct 21/22 inconsistently — [#55997](https://github.com/openai/codex/issues/55997)
- **kaderebak, #57579 (Oct 27)**: the model is written "GPT-6 Sol (Medium reasoning)", not GPT-6.1 Sol. Plus; 9,380,242 input / 9,317,760 cached / 40,842 output; 5h "from approximately 30% to 0%". Not a cohort model, and Oct 27 is a reset day — [#57579](https://github.com/openai/codex/issues/57579)
- **Forum after 10-28.**
  - uruzu, Pro tier not given (Oct 30): "my usage seems to be burning same rate" after the doubling. No numbers — [forum 1403897 #46](https://community.openai.com/t/1403897/46)
  - kalmaninnovations (Oct 31): no numbers — [forum 1409401 #1005](https://community.openai.com/t/1409401/1005)
  - XMG3, Plus (Oct 29): qualitative only — [forum 1409401 #990](https://community.openai.com/t/1409401/990)
- **GitHub issue search** (`gh api search/issues`, created 2026-10-24..11-01). The queries were "weekly cached tokens", "Pro weekly doubled", "Pro 200 weekly tokens", "Pro 500 weekly tokens", "Terra 5h cached" and "Luna cached tokens 5h".
  - Hits: #56890, #56669 (recorded), #57559, #58533, #56819, #58723, #56866 (read in stage 1).
  - No Pro 200 or Pro 500 token-plus-% issue was created after 10-29.

### Inferences
- Pro evidence after the doubling is still limited to one observer, aiplans, for Astra (Sol is a lower bound only).
- Priority-tier (Fast) Sol readings are appearing in #56890. Any future qualifying Fast reading needs the 2.5× conversion and a stated starting meter value.

### Gaps
- Searches not repeated this pass: Reddit (arctic-shift) and Hacker News, already covered in stage 1. Of V2EX, only the t1253221 thread was re-read. Unread comment threads on other openai/codex issues may still hold readings, because comment search was unavailable without API access.
- #57559 (Qualle1980, Plus, Oct 27, compaction loop) was listed in the search results but not read.

## 4. Per-cell O11 verdicts (two independent non-provisional reports; largest lower ≤ 1.20 × smallest upper)

### Takeaway
Plus × Sol × 5h passes in the post-10-11 partition (jitendersingh0411 + Oleg-125). This assumes Oleg's split-day reading belongs post-split; if it does not, the cell fails. Plus × Terra × 5h still passes. Every Pro cell and every Luna cell fails.

### Cited Findings
- **GPT-6.1 Sol × Plus × 5h, post-10-11**
  - Reports: jitendersingh0411 [$2.78, 7.84] ([#55210](https://github.com/openai/codex/issues/55210)) and Oleg-125, corrected to [$3.58, 3.69] ([#51088](https://github.com/openai/codex/issues/51088)).
  - Test: 3.58 ≤ 1.2 × 3.69 = 4.43 → **pass**. With the recorded [3.6, 7.4] it also passes (3.6 ≤ 8.88).
  - If Oleg is placed pre-10-11 instead: the post partition has one report and **fails**. The pre partition becomes mehoney [8.3, 8.7] + Oleg [3.58, 3.69], and 8.3 > 4.43 → **fails**.
  - This differs from stage 1, which had the pre partition passing on Oleg's spurious $7.4 upper bound.
- **GPT-6.1 Sol × Plus × 5h, pre-10-11:** mehoney alone → **fail**. Recorded window 10-06..10-07 touches the 10-07 banked reset; O112 should be re-checked.
- **Provisional-report hazard (Sol Plus 5h).** h3tek (≈$8.8–8.9/5h computed from the quoted tokens, tier unstated) would break the post-10-11 margin if admitted to the range test even provisionally: 8.8 > 4.43. It is excluded on three grounds: tier unstated and not inferable, subagent models unstated (mixed), and the Oct 27 reset day.
- **GPT-6.1 Sol × Plus × week:** mehoney $57 only → **fail**.
- **GPT-6.1 Sol × Pro 100 / Pro 500:** no qualifying single-model report → **fail**.
- **GPT-6.1 Sol × Pro 200:**
  - Pre-10-29: sadiqmdasif [105, 130] (anomaly) and DhAdaptive Fast [401.5, 407.9], about $1,004–1,020 standard-equivalent: the margin fails.
  - Post-10-29: aiplans ≥ $481/week, a lower bound only → **fail**.
- **GPT-6.1 Terra × Plus × 5h:** pensuke89 [5.28, 5.51], IndividualPlus2011 [5.33] and SouthWindKnows [6.06, 6.15] → **pass**. pensuke89's recorded window (10-26..10-27) and SouthWindKnows (10-27) touch the 10-27 reset day, so check O112. Even with pensuke89 dropped, IndividualPlus2011 + SouthWindKnows gives 6.06 ≤ 1.2 × 5.33 = 6.40 → pass (from `data/plan_reports.json` values).
- **GPT-6.1 Terra, other cells:** 0 qualifying → **fail**.
- **GPT-6 Astra × Pro 200:** pre-10-29 aiplans [$592, 1,184]; post-10-29 aiplans [$978, 1,630]. One observer each, tier variant provisional → **fail in both partitions** ([aiplans 10-28](https://aiplans.dev/reports/codex-models-2026-10-28.md), [aiplans 10-30](https://aiplans.dev/reports/codex-models-2026-10-30.md)).
- **GPT-6 Astra × Pro 100, pre-10-29:** sentrybottale [330, 400] + YiwenPang [318] (anomaly) gives 330 ≤ 381.6, a pass only if the anomaly flag admits YiwenPang. Adding mrak- (Fast, $193 → about $482.5) gives 482.5 > 381.6 → fail. Nothing new.
- **GPT-6 Astra × Pro 100, post-10-29:** 0 reports → **fail**.
- **GPT-6 Astra × Plus × 5h:** Crystal4276 (anomaly) and kamo-k (before the window) → **fail**.
- **GPT-6 Astra × Pro 500:** totorofly only (Fast, upgrade-fault interval) → **fail**.
- **GPT-6 Luna and GPT-5.6 Luna, all plans:** recorded reports predate the window or are lower bounds; no new ones → **fail**.

### Inferences
- The only O11 change from this pass:
  - The Plus Sol 5h verdict is the same as stage 1 if Oleg is post-10-11.
  - If Oleg is pre-10-11, the corrected range removes stage 1's alternative pass in the pre partition.
  - Either way, the post-10-11 pass depends on accepting a split-day reading.
- jitendersingh0411's own 2.6× swing between Oct 25 and Oct 31 is observer-reported metering instability. Under O99 it splits nothing, but the cell's value is soft.

### Gaps
- The Pro 200 tier-variant question cannot be resolved from public sources.
- Comment-level search of openai/codex was not possible without API access.
- Reports after the cutoff (2026-11-01T06:10Z or later; listed only, none counts): MatthieuStigler #56890 (Nov 1, no meter); Agapkin #55997 (Nov 3, Plus, durations only); plus the post-cutoff items stage 1 already listed (Fun_Squirrel5446, Global_Knee5354, maksymturskyi-del #58898, tonyfenwick8814121 #59398, dpglobalWeb #59235, Procureallyai #59194, Any_Evidence4750, AmthorTheDestroyer, ProfessionalJackals).
