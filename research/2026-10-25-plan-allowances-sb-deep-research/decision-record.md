# Decision record — O71 stage 3 (AF-DECIDE, FS-SILVER_DEEP_RESEARCH)

Date: 2026-10-25. Mode: deep. research_type: default. Question: which model × tier cells pass O11 on actual end-user
reports of API-priced plan allowance, after stages 1–3. Full analysis: research_report.md. Evidence: sources.jsonl
(55), evidence.jsonl, triangulation.md (T1–T8), critique.md (2 cycles).

## Decision

**No model × tier passes O11 after three stages.** Every cell keeps the verdict "fails". ValueRank's plan basis stays on
the provider-derived routes (O46/O62 ceilings for MiMo; the existing SemiAnalysis-based and provider routes elsewhere).
No O11 value or multiple is adopted for any cell.

## What stage 3 changed (eligibility rulings)
1. Claude Pro · Opus 5.5: one new eligible report (u/K45SLE, 2026-10-21, $210–300/week; provisional, model version
   inferred) [5]. #124's data-reuse question is resolved against reuse (different dates; output and cache writes
   differ by 28% and 54%) [3][4]. #124 stays eligible, so the cell fails (6.03×; 1.53× even without #124).
2. Claude Max 20x · Opus 5.5: u/leaflavaplanetmoss's ≈$1,140 week is challenged as internally inconsistent (~30M output
   tokens ≈ $600 against an $800 total) [12]. The verdict is unchanged: P1 still spans 2.26×.
3. Claude 10-17 split: two direct per-token measurements (NicoAica, kakki-1) plus two weaker observations (push42,
   Randomblock1) [13][14]. No Anthropic statement [15]. The split is kept as user-evidenced and extended to Max 5x.
4. OpenAI GPT-6.1 Sol · Pro $500: u/DhAdaptive's same-day-upgrade figure is excluded under eligibility condition 5,
   because of an OpenAI support e-mail quoted by Vanja Petreski: Pro 200 → Pro 500 upgrades "kept the allowance from
   your previous plan", corrected 2026-10-16 [52]. The cell now has no eligible report. totorofly's Pro $500 Astra report
   is flagged.

## Alternatives considered
- Exclude #124 as an outlier: rejected. O11 judges every eligible report of a partition, and no eligibility ground
  exists (T1).
- Split Gemini 4 Argon AI Pro by effort (Low $12.3 against Medium/High $8.40–8.47): rejected. Effort is not a
  quota-schema change.
- Treat CN legacy Kimi fits (MoonDrinker $48.6 against Astralyn $55.9 per week, 1.15×) as a passing pair: rejected,
  because legacy Allegretto is not a ValueRank USD cell (stage-2 rule 7). It would pass if that tier were listed.
- Accept the Claude split as a provider-grade schema change: not adopted. It stays user-evidenced.

## Evidence summary
51 web sources plus 4 local documents. Average admiralty-derived credibility 53.6/100 (user-reported evidence class).
New source classes reached: Bluesky, HN Algolia, YouTube search snippets, Qiita, Bilibili, the locdd mirror of LINUX DO,
the OpenAI forum's 968-post Codex thread, arctic-shift Reddit to ≈10-24. Unreachable: YouTube video pages and
transcripts (bot check), X (402), nitter (challenge), Zhihu and LINUX DO search (403), Xiaohongshu.

## Tradeoffs and risks
- The closest cells are decided by eligibility, not by data volume: Claude Pro (#124), Argon AI Pro (Low effort),
  GPT-6 Astra Pro $100 (whole-range rule). A future owner ruling on outlier handling would flip at least Claude Pro.
- The leaflavaplanetmoss and DhAdaptive rulings rest on single pieces of evidence (token-share arithmetic; one quoted
  support e-mail).
- The Claude split date is uncertain: NicoAica's pre-split value is already low.

## Confidence and remaining gaps
High confidence that no cell passes (every cell fails on at least one robust ground). Medium confidence in the
individual rulings T1, T3, T4 and T8. Gaps: Sonnet 5.5, Haiku 5.5, Argon Ultra, Kimi USD tiers above Plus, MiMo-V2.6-Flash
and every MiniMax M Plan tier have zero eligible reports. YouTube leads (Binh Dad; Iris Ludd on Pro $200 new 10×) are
unread.

## Downstream handoff route
AF-DECIDE → AF-DOCUMENT (`silver-ensure-docs`) → AF-VALIDATE (`silver-validate`). The coordinator commits this directory.
See handoff.md.

## Sources cited in this record

[1] NTRYourWaifu (2026). "[數據] Anthropic · Claude Pro $20 · Opus 5.5". GitHub Fei2411/real-api-pricing issue 52. URL: https://github.com/Fei2411/real-api-pricing/issues/52 (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/issues/52)
[2] Fei2411 maintainers (2026). "real-api-pricing community dataset (transcribed X post by @kanzakichiya)". GitHub. URL: https://github.com/Fei2411/real-api-pricing (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing)
[3] ganpei777 (2026). "[Data] Anthropic · Claude Pro $20 · Opus 5.5 (weekly quota 0% to 100%)". GitHub Fei2411/real-api-pricing issue 124. URL: https://github.com/Fei2411/real-api-pricing/issues/124 (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/issues/124)
[4] Fei2411 maintainers (2026). "claude-team-opus55-round1-2026-10-06 data file (Team Premium screenshot)". GitHub. URL: https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-team-opus55-round1-2026-10-06.json (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-team-opus55-round1-2026-10-06.json)
[5] u/K45SLE (2026). "Comment on 'I helped Claude leave itself a note before the usage limit hits'". Reddit r/ClaudeCode. URL: https://www.reddit.com/r/ClaudeCode/comments/1xb70h0/_/19resfcjmw52b/ (Retrieved: 2026-10-25 via arctic-shift) [link](https://www.reddit.com/r/ClaudeCode/comments/1xb70h0/_/19resfcjmw52b/)
[6] u/Ok-Cauliflower-7568 (2026). "Comment on 'I logged every Claude Code run for 5 months'". Reddit r/ClaudeAI. URL: https://www.reddit.com/r/ClaudeAI/comments/1x8637w/_/pha0c76/ (Retrieved: 2026-10-25 via arctic-shift) [link](https://www.reddit.com/r/ClaudeAI/comments/1x8637w/_/pha0c76/)
[7] devin-ai-integration for a user (2026). "[数据 / Data] Anthropic · Claude Pro $20 · Opus 5.5". GitHub Fei2411/real-api-pricing issue 47. URL: https://github.com/Fei2411/real-api-pricing/issues/47 (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/issues/47)
[8] muscgab (2026). "[数据 / Data] Anthropic · Claude Max 5x $100 · Opus 5.5". GitHub Fei2411/real-api-pricing issue 98. URL: https://github.com/Fei2411/real-api-pricing/issues/98 (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/issues/98)
[9] Fei2411 maintainers (2026). "claude-max5x-opus55-round1-2026-10-03 data file". GitHub. URL: https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-max5x-opus55-round1-2026-10-03.json (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/blob/main/data/research/claude-max5x-opus55-round1-2026-10-03.json)
[10] Kanttz (2026). "[数据 / Data] Anthropic · Claude Max 20x · Opus 5.5 (two full weekly windows and a 36-window 5h fit)". GitHub Fei2411/real-api-pricing issue 96. URL: https://github.com/Fei2411/real-api-pricing/issues/96 (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/issues/96)
[11] Theo, pingdotgg (2026). "ts-rust README". GitHub. URL: https://github.com/pingdotgg/ts-rust (Retrieved: 2026-10-25) [link](https://github.com/pingdotgg/ts-rust)
[12] u/leaflavaplanetmoss (2026). "Comment on a Max 20x weekly limit thread". Reddit r/ClaudeCode. URL: https://www.reddit.com/r/ClaudeCode/comments/1x1esxn/_/peuarxu/ (Retrieved: 2026-10-25 via arctic-shift) [link](https://www.reddit.com/r/ClaudeCode/comments/1x1esxn/_/peuarxu/)
[13] NicoAica, kakki-1, push42 and others (2026). "claude-code issue 102667 (weekly meter moves faster per token from Oct 17)". GitHub anthropics/claude-code. URL: https://github.com/anthropics/claude-code/issues/102667 (Retrieved: 2026-10-25) [link](https://github.com/anthropics/claude-code/issues/102667)
[14] u/Randomblock1 (2026). "Comment on weekly-limit thread 1x8bmku". Reddit r/ClaudeAI. URL: https://www.reddit.com/r/ClaudeAI/comments/1x8bmku/_/phcyqkp/ (Retrieved: 2026-10-25 via arctic-shift) [link](https://www.reddit.com/r/ClaudeAI/comments/1x8bmku/_/phcyqkp/)
[15] Anthropic (2026). "Claude release notes". Claude Help Center. URL: https://support.claude.com/en/articles/12138966-release-notes (Retrieved: 2026-10-25) [link](https://support.claude.com/en/articles/12138966-release-notes)
[16] wokey.ai (2026). "Claude Usage Limits (October 2026): Pro & Max Weekly Limits, Measured". wokey.ai. URL: https://wokey.ai/claude-usage-limits (Retrieved: 2026-10-25) [link](https://wokey.ai/claude-usage-limits)
[19] cannonpalms (2026). "HN comment on Max 20x value". Hacker News. URL: https://news.ycombinator.com/item?id=50220613 (Retrieved: 2026-10-25) [link](https://news.ycombinator.com/item?id=50220613)
[20] mehoney (2026). "openai/codex issue 51604". GitHub. URL: https://github.com/openai/codex/issues/51604 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/51604)
[21] Oleg-125 (2026). "openai/codex issue 51088". GitHub. URL: https://github.com/openai/codex/issues/51088 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/51088)
[22] u/DhAdaptive (2026). "Codex $200 to $500: my logs show API-equivalent token value". Reddit r/codex. URL: https://reddit.com/r/codex/comments/1x1y2c1/codex_200_500_my_logs_show_apiequivalent_token/ (Retrieved: 2026-10-25) [link](https://reddit.com/r/codex/comments/1x1y2c1/codex_200_500_my_logs_show_apiequivalent_token/)
[23] sadiqmdasif (2026). "Codex Rate Limit Discussion Thread, post 953". OpenAI Developer Community. URL: https://community.openai.com/t/1409401/953 (Retrieved: 2026-10-25) [link](https://community.openai.com/t/1409401/953)
[24] sentrybottale (2026). "openai/codex issue 54995". GitHub. URL: https://github.com/openai/codex/issues/54995 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/54995)
[25] mrak- (2026). "openai/codex issue 55348". GitHub. URL: https://github.com/openai/codex/issues/55348 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/55348)
[26] YiwenPang (2026). "Pro 5x: after Tibo's reset, 176M tokens used 76% of allowance vs 490M for 100% the previous day". GitHub openai/codex issue 56669. URL: https://github.com/openai/codex/issues/56669 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/56669)
[27] Crystal4276 (2026). "openai/codex issue 55648". GitHub. URL: https://github.com/openai/codex/issues/55648 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/55648)
[28] totorofly (2026). "openai/codex issue 52530". GitHub. URL: https://github.com/openai/codex/issues/52530 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/52530)
[29] yoggypap (2026). "openai/codex issue 49572". GitHub. URL: https://github.com/openai/codex/issues/49572 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/49572)
[30] OpenAI community, Thibault Sottiaux announcements (2026). "28 days of shipping tracking thread". OpenAI Developer Community. URL: https://community.openai.com/t/1403897.json (Retrieved: 2026-10-25) [link](https://community.openai.com/t/1403897.json)
[31] muscgab (2026). "[数据 / Data] OpenAI · ChatGPT Pro $100 / Pro $200 · GPT-6.1 Sol / GPT-5.6 Sol / GPT-5.6 Terra / GPT-6 Astra". GitHub Fei2411/real-api-pricing issue 97. URL: https://github.com/Fei2411/real-api-pricing/issues/97 (Retrieved: 2026-10-25) [link](https://github.com/Fei2411/real-api-pricing/issues/97)
[32] u/Danikk (2026). "Comment on Codex usage drain thread". Reddit r/OpenAI. URL: https://www.reddit.com/r/OpenAI/comments/1xbm4mn/_/19rfub0swkgw2/ (Retrieved: 2026-10-25 via arctic-shift) [link](https://www.reddit.com/r/OpenAI/comments/1xbm4mn/_/19rfub0swkgw2/)
[33] janrysavy (2026). "openai/codex issue 51145". GitHub. URL: https://github.com/openai/codex/issues/51145 (Retrieved: 2026-10-25) [link](https://github.com/openai/codex/issues/51145)
[34] @noz.am (2026). "This is what a $100 Codex Pro weekly limit looks like". Bluesky. URL: https://bsky.app/profile/noz.am/post/3mykomfdblk2r (Retrieved: 2026-10-25) [link](https://bsky.app/profile/noz.am/post/3mykomfdblk2r)
[35] u/ansofteng (2026). "Comment in 'Got Gemini 4 Argon in AntiGravity (Paid Pro Plan)'". Reddit r/GeminiAI. URL: https://www.reddit.com/r/GeminiAI/comments/1x6zv2f/comment/ph0hzk4/ (Retrieved: 2026-10-25) [link](https://www.reddit.com/r/GeminiAI/comments/1x6zv2f/comment/ph0hzk4/)
[36] Muhammed_Alpler (2026). "Google AI developer forum topic 190608". Google AI Developers Forum. URL: https://discuss.ai.google.dev/t/190608 (Retrieved: 2026-10-25) [link](https://discuss.ai.google.dev/t/190608)
[37] Faheem_Anis1 (2026). "Estimating Updated Quota for Claude / Gemini 4 Argon". Google AI Developers Forum. URL: https://discuss.ai.google.dev/t/191879 (Retrieved: 2026-10-25) [link](https://discuss.ai.google.dev/t/191879)
[38] Google staff (2026). "Google AI developer forum topic 188900 (staff on the Argon quota)". Google AI Developers Forum. URL: https://discuss.ai.google.dev/t/188900 (Retrieved: 2026-10-25) [link](https://discuss.ai.google.dev/t/188900)
[39] @spin.pyokosmeme.group (2026). "Bluesky post on an Argon weekly limit". Bluesky. URL: https://bsky.app/profile/spin.pyokosmeme.group/post/3mynbs4nfys2y (Retrieved: 2026-10-25) [link](https://bsky.app/profile/spin.pyokosmeme.group/post/3mynbs4nfys2y)
[41] u/TheVoyant (2026). "MiMo Token Plan dashboard screenshot". Reddit image host. URL: https://i.redd.it/xw17jwr9fbxh1.png (Retrieved: 2026-10-25) [link](https://i.redd.it/xw17jwr9fbxh1.png)
[42] u/AppleHuman8535 (2026). "r/opencode thread 1x71142". Reddit r/opencode. URL: https://www.reddit.com/r/opencode/comments/1x71142/ (Retrieved: 2026-10-25) [link](https://www.reddit.com/r/opencode/comments/1x71142/)
[43] waximabbax (2026). "Ask HN comment on Kimi Plus limits". Hacker News. URL: https://news.ycombinator.com/item?id=50222093 (Retrieved: 2026-10-25) [link](https://news.ycombinator.com/item?id=50222093)
[44] okarin, shown as NightRain on the mirror (2026). "K3.1 Pro额度掉得快？两个¥699订阅实测". locdd mirror of LINUX DO 3069671. URL: https://www.locdd.com/t/topic/103507 (Retrieved: 2026-10-25) [link](https://www.locdd.com/t/topic/103507)
[45] MoonDrinker (2026). "Kimi Allegretto K3.1 Pro 额度实测，订阅中 K3.1 Pro 价格约为 K3 订阅价格的 85%". locdd mirror of LINUX DO. URL: https://www.locdd.com/t/103607/1 (Retrieved: 2026-10-25) [link](https://www.locdd.com/t/103607/1)
[46] Moonshot AI (2026). "Kimi membership update rules". Kimi Help Center. URL: https://www.kimi.com/en/help/membership/membership-update-rules (Retrieved: 2026-10-25) [link](https://www.kimi.com/en/help/membership/membership-update-rules)
[47] kojimako (2026). "kojimako K3.1 Pro quota fit". LINUX DO. URL: https://linux.do/t/topic/3070992 (Retrieved: 2026-10-25) [link](https://linux.do/t/topic/3070992)
[48] MiniMax (2026). "M Plan tiers, windows and credit pricing (platform documentation)". MiniMax platform docs. URL: https://platform.minimax.io/docs/m-plan/intro (Retrieved: 2026-10-25) [link](https://platform.minimax.io/docs/m-plan/intro)
[49] u/Ok_Bug1610 (2026). "Comment in r/MiniMax_AI thread 1x6p4d6". Reddit r/MiniMax_AI. URL: https://www.reddit.com/r/MiniMax_AI/comments/1x6p4d6/_/19re6xfrt9bwl/ (Retrieved: 2026-10-25 via arctic-shift) [link](https://www.reddit.com/r/MiniMax_AI/comments/1x6p4d6/_/19re6xfrt9bwl/)
[50] DeepSeek (2026). "DeepSeek API pricing". DeepSeek API docs. URL: https://api-docs.deepseek.com/quick_start/pricing (Retrieved: 2026-10-25) [link](https://api-docs.deepseek.com/quick_start/pricing)
[52] Vanja Petreski (2026). "Fuck You OpenAI (blog post quoting an OpenAI support e-mail)". vanja.io. URL: https://vanja.io/fuck-you-openai/ (Retrieved: 2026-10-25) [link](https://vanja.io/fuck-you-openai/)

## Provider tables (all three stages)

Monthly = weekly × 4.33. "S1/S2/S3" marks the stage that found the report. Per-window values with a binding weekly cap are left in their own unit. Std-eq = OpenAI Fast-mode value × 2.5. A cell passes only if every eligible report in a partition lies within 1.20× of the partition's smallest value; a passing value would be the median of the concordant set ($/month), with the multiple = value ÷ plan fee.

### Anthropic (Claude Pro $20 / Max 5x $100 / Max 20x $200)

| Model × tier | Eligible reports (author, date, $/week → $/month, link) | Partition and split evidence | Verdict |
|---|---|---|---|
| Opus 5.5 · Pro | NTRYourWaifu, 2026-09-22..27, $321 → $1,390 (S1) [1]; @kanzakichiya, ≈2026-09-30, ≈$302 → $1,308 (S1) [2]; ganpei777, 2026-10-09..13, $1,266 → $5,482 (S1; S3: reuse ruled out) [3]; u/K45SLE, 2026-10-21, Opus xhigh (version inferred, provisional), $210–300 → $909–1,299 (S3) [5]. Excluded: Ok-Cauliflower-7568 $250–316 (mixed) [6]; #47 ≥$112 (snapshot) [7]; hakanavgin ≈$270, Planyy $400–500 (mixed); wokey $170 (aggregate) [16] | One partition 09-22 → 10-25. No Pro limit change in Anthropic's release notes [15]; 10-17 evidence concerns Max accounts | **fails** (1,266 / 210 = 6.03; without #124, 321 / 210 = 1.53 over K45SLE's whole range) |
| Opus 5.5 · Max 5x | muscgab, 2026-10-03, $750–830 (cache off) → $3,248–3,594 (S1) [8]; unlabelled /usage screenshot, week of 2026-09-29, ≈$1,920 → $8,314 (S1) [9]. Excluded: Fancy_Leave7798 $1,538 (model unstated); push42 (% only) [13]; jegudev ≈$757/month and a YouTube "$987 last week" claim (no meter fraction) | P1 to 2026-10-17; P2 after (S3: push42 measures a full window at ≈18% of the week, against ≤10% before [13]) | **fails** (P1: 1,920 / 750 = 2.56; P2: no report) |
| Opus 5.5 · Max 20x | P1: Kanttz, 2026-10-02, $2,578 (5-min) / $2,920 (1-h) → $11,163–12,644 (S1) [10]; Theo, two weeks to ≤2026-10-13, $2,446–2,600 → $10,591–11,258 (S1) [11]; u/Last_Lab_3627, 2026-09-27, ≈$2,045 → $8,855 (S1, link not recovered); u/Delicious-Shower8401, 2026-09-26, $2,175 → $9,418 (S1, link not recovered); @NicoAica, 2026-10-15..17 08:00 CDT, $1,294–1,681 → $5,603–7,279 (S2) [13]. P2: @NicoAica, 2026-10-17 pm, $182–212 → $788–918 (S2) [13]. Challenged (S3): u/leaflavaplanetmoss, ≈2026-10-09, ≈$1,140 → $4,936, does not reproduce from its own 30M output tokens [12]. Excluded: Randomblock1 $1,395 (model unstated, straddles the split) [14]; kakki-1 (tier unstated) [13]; cannonpalms ≥$2k (no meter) [19]; tomm3hshipp, PELORA, daakkast (mixed) | P1 to 2026-10-17 ≈13:00 UTC; P2 after. Split evidence: NicoAica, kakki-1, push42, Randomblock1 (public, timestamped) [13][14]; no Anthropic statement [15]; contrary: Wokey week 10-12..19 [16] | **fails** (P1: 2,920 / 1,294 = 2.26, and 2,578 / 2,045 = 1.26 even within the upper cluster; P2: one report) |
| Sonnet 5.5 · Pro / Max 5x / Max 20x | None in any stage | n/a | **fails** (no eligible report) |
| Haiku 5.5 · Pro / Max 5x / Max 20x | None in any stage | n/a | **fails** (no eligible report) |

### OpenAI (ChatGPT plans in Codex)

| Model × tier | Eligible reports | Partition and split evidence | Verdict |
|---|---|---|---|
| GPT-6.1 Sol · Plus | mehoney, 2026-10-06/07, $8.3–8.7 per 5-h window; coarse ≈$57/week → $247/month (S1) [20]; Oleg-125, 2026-10-11, $3.6 per 5-h window (or $7.4 if 67% remained) (S1) [21]. Excluded: Danikk $46/week (legacy tier, anomaly) [32]; Pasto_Shouwa (lower bound) | One partition DevDay 09-29 → Day 7 ≈10-12; later partitions on Days 7/12/16/19 [30] | **fails** (8.7 / 3.6 = 2.42; meter direction unresolved) |
| GPT-6.1 Sol · Pro $100 | None. Excluded: muscgab #97 (mixed four-model run, derived ≈$234/week) [31]; noz.am (mixed Sol + Luna) [34] | n/a | **fails** (no eligible report) |
| GPT-6.1 Sol · Pro $200 new (10×) | None | n/a | **fails** (no eligible report) |
| GPT-6.1 Sol · Pro $200 grandfathered (20×) | u/DhAdaptive, 2026-10-08/09, xhigh, std-eq $1,004–1,020/week → $4,347–4,417 (S2) [22]; sadiqmdasif, 2026-10-22, ≈$105–130/week → $455–563 (S1) [23]. Excluded: janrysavy $323 / $569 (Astra 5.6–7.3% of requests) [33] | P1 (DhAdaptive) and P3 after Day 16 (sadiqmdasif) [30]; tier ends 2026-10-29 | **fails** (one report per partition) |
| GPT-6.1 Sol · Pro $500 | None. Excluded (S3): u/DhAdaptive, 2026-10-09, std-eq $919–964/week → $3,979–4,174 (S2) [22], measured on the day of a Pro 200 → Pro 500 upgrade inside OpenAI's acknowledged error period, when upgraded accounts "kept the allowance from your previous plan", corrected 2026-10-16 [52] | Error period ≤2026-10-16 [52]; Days 7/12/16/19 [30] | **fails** (no eligible report) |
| GPT-6 Astra · Plus | Crystal4276, 2026-10-20, ≈$2.5 per 5-h window (anomaly report) (S1) [27] | P2 | **fails** (one report) |
| GPT-6 Astra · Pro $100 | sentrybottale, 2026-10-18, high, $330–400/week → $1,429–1,732 (S1) [24]; mrak-, 2026-10-19, high, Fast $193 → std-eq ≈$480/week → $2,078 (S1) [25]; YiwenPang, 2026-10-24, ultra, $318/week → $1,377 (S1) [26]. Excluded: muscgab #97 derived ≈$313/week (mixed, contributor-derived) [31] | P2 ≈10-17 → ≈10-21 (sentrybottale, mrak-); P3 after Day 16 (YiwenPang) [30] | **fails** (P2: 480 / 330 = 1.45; P3: one report) |
| GPT-6 Astra · Pro $200 new / grandfathered | None. Excluded: genellect (mixed, Fast); ppgnox (tier unknown) | n/a | **fails** (no eligible report) |
| GPT-6 Astra · Pro $500 | totorofly, 2026-10-11, mostly max, std-eq $1.5–2.6k/week → $6,495–11,258 (S1) [28]; flagged (S3): upgrade history unknown, inside the upgrade-error period [52] | P1/P2 boundary | **fails** (one report) |
| GPT-6 Luna · Plus | yoggypap, 2026-09-30, max, $6.5–7.5 per 5-h window (S1) [29] | P1 | **fails** (one report) |
| GPT-6 Luna · Pro tiers | None | n/a | **fails** (no eligible report) |
| GPT-5.6 Luna · all tiers | None in the window (tagorr 09-08 and Shekelphile 09-22 predate it) | n/a | **fails** (no eligible report) |

### Google (Antigravity; Gemini 4 Argon at introductory API prices $2 / $0.10 / $10 per 1M)

| Model × tier | Eligible reports | Partition and split evidence | Verdict |
|---|---|---|---|
| Gemini 4 Argon · AI Pro ($19.99) | u/ansofteng, 2026-10-16, Medium, $8.40/week ($7.84–9.04) → $36 ($34–39) (S2, tier inferred) [35]; Muhammed_Alpler, 2026-10-19, High, $8.47/week → $37 (S1) [36]; Faheem_Anis1, 2026-10-23, Low, $12.3/week ($11.4–13.4) → $53 ($49–58) (S1) [37]. Excluded: spin.pyokosmeme (tier and basis unstated) [39]; percentage-only posts | One partition from the Pro Argon quota launch on 2026-10-16 [38]; no public schema change since; effort is not a split ground | **fails** (12.3 / 8.40 = 1.46) |
| Gemini 4 Argon · AI Ultra | None in any stage | n/a | **fails** (no eligible report) |

### Xiaomi MiMo Token Plan (V2.6-Pro $0.0036 / $0.435 / $0.87 per 1M)

| Model × tier | Eligible reports | Partition and split evidence | Verdict |
|---|---|---|---|
| MiMo-V2.6-Pro · Lite | AppleHuman8535, posted 2026-10-15, ≈$4.60 per monthly period (weak) (S1) [42] | No change in Xiaomi's credit table found | **fails** (one report) |
| MiMo-V2.6-Pro · Standard | None | n/a | **fails** (no eligible report) |
| MiMo-V2.6-Pro · Pro | None | n/a | **fails** (no eligible report) |
| MiMo-V2.6-Pro · Max | TheVoyant, 2026-10-21, one day of 1.03B tokens = 12–13% of the month → ≈$80–105/month (S1) [41] | as above | **fails** (one report) |
| MiMo-V2.6-Flash · all tiers | None | n/a | **fails** (no eligible report) |

### Kimi membership (USD tiers; K3.1 Pro $2 / $0.20 / $10 per 1M)

| Model × tier | Eligible reports | Partition and split evidence | Verdict |
|---|---|---|---|
| K3.1 Pro · Plus $19 | waximabbax, 2026-10-24, Standard, $1.37 per 5-h window (S1) [43]; not normalisable to a month (pool unpublished [46]) | Split on the ≈+50% quota increase of 2026-10-24 [47]; waximabbax's side unknown | **fails** (one report) |
| K3.1 Pro · Pro $39 | None (USD). CN reference only: Weibo CN Pro ≈$90/month | as above | **fails** (no eligible report) |
| K3.1 Pro · Max $99 | None (USD). CN reference only: okarin new CN Max ≈$333/month [44] | as above | **fails** (no eligible report) |
| K3.1 Pro · Ultra $199 | None (USD). CN reference only: legacy Allegretto fits, MoonDrinker $48.6/week (S3) [45] against Astralyn $55.9/week (S1) | as above | **fails** (no eligible report) |

### MiniMax M Plan (M3.1-Flash $0.15 / $0.015 / $0.60 per 1M)

| Model × tier | Eligible reports | Partition and split evidence | Verdict |
|---|---|---|---|
| MiniMax-M3.1-Flash · Go $22 | None (legacy Token Plan items only) | M Plan replaced Token Plan ≈09-29/30 [48]; M2.5/M2.7 traffic rerouted to M3.1-Flash on 10-19 [49] | **fails** (no eligible report) |
| MiniMax-M3.1-Flash · Explore $55 | None | as above | **fails** (no eligible report) |
| MiniMax-M3.1-Flash · Build $132 | None | as above | **fails** (no eligible report) |

DeepSeek sells no first-party plan, so it has no cell [50].
