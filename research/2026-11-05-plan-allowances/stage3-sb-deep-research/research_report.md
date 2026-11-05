# Subscription plan allowance reports for coding agents: stage 3 deep research, 2026-11-05

## Executive Summary

This stage re-read every qualifying or near-qualifying report from stages 1 and 2 against its primary page, swept Reddit, Hacker News, GitHub, the Google AI forum, LINUX DO and V2EX for reports both stages missed, and tested each provider cell against the O11 rule. The answer for the cutoff release is unchanged: no provider, plan and window cell has two independent, non-provisional, concordant reports. Seven things are new or corrected.

First, the Oleg-125 report for GPT-6.1 Sol on ChatGPT Plus over a 5-hour window prices to about $3.58 to $3.69, not $3.6 to $7.4, because the comment says 67% of the 5h allowance was consumed [12]. Second, the Google AI Pro report by Faheem_Anis1 is the same data as a Reddit post by Ultimitehand, so it is one observation, not two [21][22]. Third, a Google quota raise around 2026-10-21 to 2026-10-22 is claimed by one blog and fits the Pro dispersion, but Google's documentation shows no change [23][24]. Fourth, a primary retest of Kimi Allegretto coefficients on 2026-11-03 found the 5-hour charge unchanged since 2026-10-25, which contradicts the claimed 5-hour doubling [26].

Fifth, three Claude reports dated 2026-11-02 to 2026-11-04 are new or newly priced and all fall after the cutoff: a Pro measurement through headless `claude -p` at about $25 to $33 per 5-hour window [6][7], a controlled Max test at about $204 per 5-hour window through the interactive terminal [4], and an Ultra weekly test of $1,560 to $3,087 [5]. Sixth, headless and SDK entrypoints drain meters faster than interactive use, by 1.14 to 1.95 times on Claude [4][5] and by 1.36 times or more on Google [25]. Seventh, a ChatGPT Team 1x black-box test and post-reset ChatGPT Pro shrink reports exist but cannot be priced [16][17].

Blocked or limited: linux.do search endpoints return the Cloudflare challenge, GitHub repository endpoints are not enabled, and X search is unavailable [34][36].

## Introduction

The question asks for user-reported dollar-equivalent allowances per rate-limit window for six provider groups since about 2026-10-19 [36]. A report counts under O11 only if it states the plan tier, the window, the measured consumption and how the dollar figure was computed [36]. Stage 1 used plain web search and stage 2 used Claude Deep Research [36]. This stage runs the Silver Bullet deep workflow in `deep` mode with two critique cycles [36]. Prices follow stage 1: Opus 5.5 at $4 input, $20 output, $0.20 cache read and $5 or $8 cache write per million tokens, GPT-6.1 Sol at $2, $0.10 and $10, GPT-6 Astra at $10, $1 and $50, and Gemini 4 Argon at the introductory $2, $0.10 and $10 [35].

## Main Analysis

### Anthropic Claude plans

Jbdamask reported that an agent team burned 36% of the Max 20x weekly limit in under 20 hours with eight agents all running Opus 5.5 [1]. His table shows 2,449M cache reads at $490, 27M cache writes at $136, 35M cache rebuilds at $176 and 1.5M output and input at $29, a total of $831 [1]. Dividing $831 by 0.36 gives about $2,308 per week, or $2,277 to $2,341 with integer rounding [35]. The dollar figure was computed by asking Claude to sum the previous 20 hours at Opus 5.5 API rates [1]. I confirmed the post text and the table image. The entrypoint is not stated, so the figure may understate an interactive allowance.

Deepfoundationdesign reported Max 5x with `claude-opus-5-5` for effectively all requests, 7,089 requests, 5.9 M output tokens, 3.19 B cache read and 24.2 M cache write, and 64% of the weekly limit after two days [2]. Pricing those tokens gives $877.0 to $949.6, so the weekly value is about $1,360 to $1,495 [35]. Uncached input is not reported and claude.ai chat use is not in the logs, so this is a slight undercount [2]. A later Nov 1 comment reports 98% with no tokens and cannot be priced [2].

Simon83 reported that 1% of the Max 20x weekly limit is worth about $20 and 1% of the 5-hour window about $5.20 [10]. The model is not stated, so neither figure qualifies.

Coriatel reported an Ultra week with a reset on Oct 31 at 04:00 Asia/Jerusalem, 38% used after 2,600 requests and $307 measured with ccusage at Opus 5.5 list prices, about $800 per week [3]. The reset is 02:00Z, not 01:00Z. The week is 98% Opus, so it is provisional. Clem-pxp reported 76% on Ultra from 2.1B tokens with 84% Opus requests and no dollars [3].

Three controlled tests were published after the cutoff. Douflou ran a fixed task on a Max plan with Opus 5.5 at medium effort: $20.46 moved the 5-hour meter from 16% to 26% through the interactive terminal, while $19.83 moved it from 26% to 45% through `claude -p` [4]. That is about $204 per 5-hour window interactively and about $104 through the SDK paths, and the weekly meter moved about 3 points per $40 of work [4]. Ricardoraposo, on Max 20x with Opus 5.5 at low effort, measured $15.6 per weekly point for `sdk-ts` and $20.6 for the interactive terminal with caching off, and $27.15 against $30.87 with caching on [5]. That is $1,560 to $3,087 per week. The x2v measurement of a Claude Pro account used headless `claude -p` with Opus 5.5 and moved the 5-hour meter from 0% to 28% for $9.39 of list-priced usage and the weekly meter from 4% to 7% [7]. Pricing each row gives $26.2 to $32.7 per 5-hour window and about $305 per week with a range of $229 to $458 [7][35].

Other Claude readings are weaker. Sergiokapone reported a Pro 5-hour window at 100% with Opus 5.5 plus 22 Haiku 4.5 requests and one Sonnet 5.5 request, valued at roughly $13 to $14 [9]. Smaug42 reported that a 99M-token task worth about $32 used 16% of the 5-hour session and 3% of the weekly limit on Pro [8], which is about $200 per 5-hour window and far above every other Pro figure. Leolim031 gave two Oct 14 Opus 5.5 windows at 38% and 13% of 5h, which price to $41 to $48 and $57 to $64, but the plan is a placeholder [9]. JCorners68 gave 26% of a session for one request on a plan called "Max" [8].

No single-model report exists for Sonnet 5.5 or Haiku 5.5 on any tier.

### OpenAI ChatGPT and Codex plans

Jitendersingh0411 reported ChatGPT Plus with GPT-6.1 Sol at high reasoning and two readings of 30% of the 5-hour quota, with about 13.21M input at 99.0% cached on Oct 25 and about 5.19M at 99.4% cached on Oct 31 [11]. Pricing gives about $7.5 and $2.9 per 5-hour window, a 2.6 times spread, and the post's 7-minute table segment is not reconciled with its 30-minute narrative [11][35]. Oleg-125 reported 67% of the 5h allowance consumed in a roughly 40-minute Oct 11 session with 232,120 input, 14,130,560 cached input and 55,692 output tokens [12]. That prices to $2.43, so $3.58 to $3.69 per 5-hour window, and the model is named in the comment header as GPT-6.1 Sol Medium [12][35]. The earlier record of $3.6 to $7.4 for the upper bound is contradicted by the word "consumed".

Xu62u4u6 gave Plus with gpt-6-astra and gpt-5.6-sol, about 9.56M tokens and a 5h meter from 0% to 99%, so the report is mixed-model and has no input and output split [12].

The aiplans ledgers show a synthetic Astra test on an account the owner confirmed as ChatGPT Pro 200. On Oct 28, 28 calls with 2,320,149 input, 271,104 cache read and 4,070 output moved the weekly meter from 89% to 92% [13]. Pricing gives $23.68, so $789 per week with a range of $592 to $1,184 [35]. On Oct 30, 60 calls with 4,765,206 input, 806,400 cache read and 8,733 output moved the meter from 49% to 53% [14]. That is $48.90, so $1,222 per week with a range of $978 to $1,630 [35]. The Sol batch on Oct 30 moved the meter from 48% to 49% and supports only a lower bound of about $481 per week [14][35]. The account's 20x or 10x variant is not stated, so both Astra readings are provisional.

Pensuke89 reported about $5.50 of Terra per 5-hour limit and $34.33 per weekly limit on Plus [15]. A black-box test on a ChatGPT Team 1x account across 2,700 requests is quoted on LINUX DO but its original post could not be located [17]. On 2026-11-05 several users reported that the allowance felt much smaller after a reset, for example Pro 200 at about 1200 dollars against about 2600 dollars before, without token splits [16].

### Google AI Pro and Ultra on Antigravity

Yiji_Kong ran an A/B test on Ultra 5x in Antigravity. A clean Argon High request with 14,918 input and 4,233 output tokens dropped the shared 5-hour fraction by 0.00144340, and a 42-step session dropped it by 0.03154810 [18]. Priced at $2, $0.10 and $10, the two readings give $50.0 and $49.2 per 5-hour window [35]. Jamie950315 stated Ultra 5x, Antigravity 2.26.0, Argon Medium, and four weekly probes that price to $199.9 to $200.1 per week [19][35]. His 5-hour figure is derived from a Flash calibration and does not count. Jamie950315 also states that Antigravity bills Argon at $6, $30 and $0.30, three times the launch price, so the same data read at the post-introductory $4 and $20 price would double the dollar figures [19].

Muhammed_Alpler reported Google AI Pro with 2.61M tokens worth $0.864 draining about 10.2% of the weekly pool on 2026-10-19, which is $8.47 per week [20]. Faheem_Anis1 reported 185,443 input, 1,684,364 cache read and 19,961 output tokens, $0.72 used, and a $12 weekly value [21]. The identical counts, the same 0.72 dollar figure and the same sentences appear in a Reddit post by Ultimitehand dated 2026-10-23 [22]. The forum copy is stamped 2026-10-26 [21]. They are one observation.

An independent blog dated 2026-10-22 says Google doubled Antigravity quotas, raising Pro from $10 to $15 per week and Ultra 5x from $25 to $50 per 5 hours and from $100 to $200 per week [23]. The ratio of $12 to $8.47 is 1.42 and matches that 1.5 times step, and the Ultra 5x measurements of $50 per 5 hours and $200 per week match the post-change figures [23][35]. Google's plans page states that baseline limits are determined by available capacity and gives no numbers [24]. A Google staff reply says Antigravity quota isn't based on public API prices [20]. The change is therefore a candidate, not a confirmed split, and the 1.42 ratio could also come from different accounts or pools.

Jyongchulwp measured on Google AI Ultra that interactive Argon High used 26.5% less 5-hour quota than `agy -p` on the same prompts (307 ppm against 418 ppm), and a cold headless start used 2.5 to 7.2 times more [25]. An Ultra user reported about 450 million tokens at a 96% cache hit with 71% of the quota left, but did not state the tier [33].

### Kimi, Xiaomi MiMo and MiniMax

Astralyn's LINUX DO record of Kimi Allegretto (legacy 199 CNY) 5-hour coefficients for K3.1 Pro is 0.2810 per million for input, 0.001407 for cache read and 2.247 for output, unchanged since 10/25, with a 11/03 retest at 0.2814 and 2.229 [26]. At a 2.5%, 0.5% and 97% input, output and cache-read mix the 5-hour window holds 51.0M tokens, which is about $15 at K3.1 Pro list prices, and 7d is 5 times 5h [26][35]. That contradicts the claim that the legacy Allegretto 5-hour window doubled around Oct 27 to 29, because a doubling would halve the coefficients; it says nothing about the new subscription system, where the Reddit claim may refer to a different ratio.

Direct readings on the legacy plan are SunnyDoll's full 5-hour window of 31.9M tokens on Oct 26 (about $9 to $21), PaperPlane's roughly 100M tokens at 98.5% cache, and SunnyDoll's 150M tokens at 99.2% cache on Oct 29 [27][28]. The wide spread is explained by cache share, because the subscription charges cache reads at about 1/200 of input while the API list charges 1/10 [26]. MoonPostman's weekly reading on the legacy 699 plan spans the Oct 24 split [29]. New-plan reports from Nov 4 are estimates [30]. A Kimi Plus user reported a 785k-token 5-hour session equal to 13% of the monthly limit, about $12.42 per month by the reporter's own arithmetic, after the cutoff [32].

The mirror thread locdd 103607 is a copy of LINUX DO topic 3071240, so the moondrinker and astralyn records are one observer [31][26]. No new priced MiMo or MiniMax report was found in the sweeps [34].

## Synthesis

The qualifying set is small and the dispersion within a cell is larger than the 1.20 margin. For Pro 5-hour windows the reports range from about $14 to $200, and the cause is partly entrypoint (headless against interactive), partly cache share, and partly metering instability around 2026-10-28 to 2026-11-03. Taken together, the evidence suggests that dollar-equivalent allowances measured by list price are not stable per plan, so the O11 margin will rarely pass until partitions are drawn tightly. Two partition proposals follow from this stage: a Google split near 2026-10-21 to 2026-10-22, which would put Alpler and ansofteng before it and Faheem and Ultimitehand after it, and an entrypoint attribute on every Claude and Google report.

## Counterevidence Register

- The Oleg-125 upper bound of $7.4 assumed ambiguity that the word "consumed" removes [12].
- A Kimi 5-hour doubling is claimed on Reddit but the primary coefficient retest shows no change [26].
- Google staff and documentation deny that quota tracks API prices or announce no change, against a blog that reports a doubling [24][23].
- Smaug42's Pro figure of about $200 per 5-hour window is contradicted by the x2v and other Pro readings at $25 to $42 [8][7].

## Claims-Evidence Table

| Claim | Evidence ids (see claims.jsonl) | Status |
|---|---|---|
| Oleg-125 prices to $3.58 to $3.69 | sources [12] | verified arithmetic |
| Faheem and Ultimitehand are one observation | sources [21][22] | verified by text identity |
| Kimi 5h coefficient unchanged to 11-03 | source [26] | primary retest |

## Limitations

The sample is biased toward complaint threads. Reddit was read through a mirror capped at 100 results per query and 11-05 coverage is partial [34]. GitHub comments were read through rendered pages summarised by the fetch tool, so quotes are verbatim only to the extent the tool reported them and no byte-exact copy exists [34]. Locdd pseudonyms cannot establish observer identity. The x2v and douflou tests are synthetic and after the cutoff. Argon dollar figures depend on introductory pricing that ends 2026-11-30. Entrypoint is unstated in most reports. The x2v dollars use the $8 one-hour cache-write price, and the $5 five-minute price would lower the 5-hour figure by about 7% [35]. The Kimi coefficient retest comes from the same author as the original fit.

## Recommendations

1. Correct the Oleg-125 record to $3.58 to $3.69 per 5-hour window and keep the Sol, Plus, 5-hour cell conditional on assigning the Oct 11 reading after the 10-11 split.
2. Merge moondrinker-allegretto into the Astralyn observer and record Faheem_Anis1 and Ultimitehand as one Google AI Pro observation.
3. Do not record a Kimi 5-hour partition split on the Oct 27 to 29 claim.
4. Open a Google change-detection check for 2026-10-21 to 2026-10-22 and record the Argon price basis on every Google report.
5. Add an entrypoint field (interactive, sdk-cli, sdk-ts, headless) to Claude and Google reports and queue the three after-cutoff Claude tests for the next release.
6. Run the O167 freshness check for an OpenAI Pro limit change after the 2026-11-05 shrink reports.

## Bibliography

[1] jbdamask (2026). "Claude Max 20x weekly limit burn with eight Opus 5.5 agents". X. [https://x.com/jbdamask/status/2115515191039545712](https://x.com/jbdamask/status/2115515191039545712)
[2] deepfoundationdesign (2026). "Max 5x weekly limit reached every week since mid-October with an unchanged workload". GitHub issue 106322. [https://github.com/anthropics/claude-code/issues/106322](https://github.com/anthropics/claude-code/issues/106322)
[3] Coriatel and clem-pxp (2026). "Ultra migration weekly allowance reports". GitHub issue 106274. [https://github.com/anthropics/claude-code/issues/106274](https://github.com/anthropics/claude-code/issues/106274)
[4] douflou (2026). "Entrypoint-dependent 5h meter drain, controlled measurement". GitHub issue 106375. [https://github.com/anthropics/claude-code/issues/106375](https://github.com/anthropics/claude-code/issues/106375)
[5] ricardoraposo (2026). "Weekly-meter entrypoint test on Max 20x". GitHub issue 97074. [https://github.com/anthropics/claude-code/issues/97074](https://github.com/anthropics/claude-code/issues/97074)
[6] aiplans (2026). "Claude Pro Opus 5.5 quota measurement summary". aiplans.dev. [https://aiplans.dev/reports/claude-pro-opus55-2026-11-04.md](https://aiplans.dev/reports/claude-pro-opus55-2026-11-04.md)
[7] x2v (2026). "Pro Plan Opus 5.5 Quota experiment page". claude.ai artifact. [https://claude.ai/artifact/DcK5UbxR1SmkgDn38QtBo2](https://claude.ai/artifact/DcK5UbxR1SmkgDn38QtBo2)
[8] smaug42 and JCorners68 (2026). "Pro and Max usage comments". GitHub issue 105621. [https://github.com/anthropics/claude-code/issues/105621](https://github.com/anthropics/claude-code/issues/105621)
[9] sergiokapone and leolim031 (2026). "Pro 5h window data points". GitHub issue 101937. [https://github.com/anthropics/claude-code/issues/101937](https://github.com/anthropics/claude-code/issues/101937)
[10] simon83 (2026). "HN comment: 1% of Max 20x weekly limit worth about $20". Hacker News. [https://news.ycombinator.com/item?id=50289476](https://news.ycombinator.com/item?id=50289476)
[11] jitendersingh0411 (2026). "Plus Codex 5h quota depletion, Oct 25 and Oct 31 readings". GitHub issue 55210. [https://github.com/openai/codex/issues/55210](https://github.com/openai/codex/issues/55210)
[12] Oleg-125 and xu62u4u6 (2026). "Plus Codex quota drain, Oct 11 session". GitHub issue 51088. [https://github.com/openai/codex/issues/51088](https://github.com/openai/codex/issues/51088)
[13] aiplans (2026). "Codex Pro 200 retest ledger 2026-10-28". aiplans.dev. [https://aiplans.dev/reports/codex-models-2026-10-28.json](https://aiplans.dev/reports/codex-models-2026-10-28.json)
[14] aiplans (2026). "Codex Pro 200 retest ledger 2026-10-30". aiplans.dev. [https://aiplans.dev/reports/codex-models-2026-10-30.json](https://aiplans.dev/reports/codex-models-2026-10-30.json)
[15] pensuke89 (2026). "Limits decreased when using 6.1 Terra". Reddit r/codex. [https://www.reddit.com/r/codex/comments/1xgcwoq/limits_decreased_when_using_61_terra/](https://www.reddit.com/r/codex/comments/1xgcwoq/limits_decreased_when_using_61_terra/)
[16] LINUX DO mirror (2026). "Codex allowance shrink reports after reset, 2026-11-05". locdd.com. [https://www.locdd.com/t/topic/106945](https://www.locdd.com/t/topic/106945)
[17] LINUX DO mirror (2026). "gpt-6.1 terra consumption, Team 1x black-box quote". locdd.com. [https://www.locdd.com/t/topic/104275](https://www.locdd.com/t/topic/104275)
[18] Yiji_Kong (2026). "Gemini 4 Argon draws Antigravity quota at 3x Gemini 3.8 Flash per published dollar". Google AI developer forum. [https://discuss.ai.google.dev/t/196351](https://discuss.ai.google.dev/t/196351)
[19] jamie950315 (2026). "Measured: Antigravity bills Gemini 4 Argon at 3x". Reddit r/google_antigravity. [https://www.reddit.com/r/google_antigravity/comments/1xfnvds/](https://www.reddit.com/r/google_antigravity/comments/1xfnvds/)
[20] Muhammed_Alpler (2026). "Quota Economics: Argon depletes Antigravity quota". Google AI developer forum. [https://discuss.ai.google.dev/t/190608](https://discuss.ai.google.dev/t/190608)
[21] Faheem_Anis1 (2026). "Estimating quota for Gemini 4 Argon on Google AI Pro". Google AI developer forum. [https://discuss.ai.google.dev/t/191879](https://discuss.ai.google.dev/t/191879)
[22] Ultimitehand (2026). "Estimating Updated Usage for Claude and Gemini 4 Argon". Reddit r/google_antigravity. [https://www.reddit.com/r/google_antigravity/comments/1xdghgq/](https://www.reddit.com/r/google_antigravity/comments/1xdghgq/)
[23] Mr. O (2026). "Google raises Gemini 4 Argon quota in Antigravity". O's World blog. [https://ooo.run/post/gemini-4-argon-antigravity-quota-update.html](https://ooo.run/post/gemini-4-argon-antigravity-quota-update.html)
[24] Google (2026). "Antigravity plans and baseline quota documentation". antigravity.google. [https://antigravity.google/docs/plans](https://antigravity.google/docs/plans)
[25] jyongchulwp (2026). "Headless agy -p quota consumption versus interactive on Google AI Ultra". Google AI developer forum. [https://discuss.ai.google.dev/t/198073](https://discuss.ai.google.dev/t/198073)
[26] Astralyn (2026). "Kimi Allegretto quota deduction coefficient record". LINUX DO. [https://linux.do/t/topic/3071240](https://linux.do/t/topic/3071240)
[27] LINUX DO mirror (2026). "Kimi plan measurements, SunnyDoll and PaperPlane". locdd.com. [https://www.locdd.com/t/topic/103915](https://www.locdd.com/t/topic/103915)
[28] LINUX DO mirror (2026). "Kimi k2.8 Preview half-price thread, 5h exhaustion reading". locdd.com. [https://www.locdd.com/t/topic/104985](https://www.locdd.com/t/topic/104985)
[29] LINUX DO mirror (2026). "Estimate of legacy 699 Kimi plan allowance". locdd.com. [https://www.locdd.com/t/topic/103774](https://www.locdd.com/t/topic/103774)
[30] LINUX DO mirror (2026). "New Kimi Max plan K3.1 Pro monthly usage estimate". locdd.com. [https://www.locdd.com/t/topic/106583](https://www.locdd.com/t/topic/106583)
[31] LINUX DO mirror (2026). "Mirror of Kimi Allegretto K3.1 Pro quota test thread". locdd.com. [https://www.locdd.com/t/topic/103607](https://www.locdd.com/t/topic/103607)
[32] Defiant-Pepper-7263 (2026). "Kimi Plus 5h session equals 13 percent of monthly limit". Reddit r/kimi. [https://www.reddit.com/r/kimi/comments/1xl4r76/guys_wanna_hear_a_joke/](https://www.reddit.com/r/kimi/comments/1xl4r76/guys_wanna_hear_a_joke/)
[33] Ad_Content420 (2026). "Usage limits thread, Ultra Argon 450M tokens comment". Reddit r/GeminiAI. [https://www.reddit.com/r/GeminiAI/comments/1xig0er/usage_limits/](https://www.reddit.com/r/GeminiAI/comments/1xig0er/usage_limits/)
[34] Stage 3 (2026). "Sweep log with query counts and blocked venues". Local research artifact. [file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/raw/sweep-log.md](file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/raw/sweep-log.md)
[35] Stage 3 (2026). "Researcher arithmetic worksheet". Local research artifact. [file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/raw/arithmetic-worksheet.md](file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/raw/arithmetic-worksheet.md)
[36] Stage 3 (2026). "Run manifest for the plan-allowance deep research". Local research artifact. [file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/run_manifest.json](file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/run_manifest.json)
[37] Stage 3 (2026). "Archive manifest of hashed raw copies". Local research artifact. [file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/raw/MANIFEST.sha256](file:///home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research/raw/MANIFEST.sha256)

## Methodology

Retrieval used host WebSearch and WebFetch with direct fetches because `search-cli` is not installed [34][36]. Reddit comments were pulled by day through the Arctic Shift mirror (5,359 Claude-subreddit comments from 2026-10-19 to 2026-11-05 and 2,515 comments in six other subreddits from 2026-10-26) and filtered for dollar, token and percentage content [34]. Hacker News was queried through Algolia (4,004 hits, 17 queries) [34]. Twenty-six locdd queries and 38 recent topics were read [34]. Dollar arithmetic is mine at the list prices above, with each meter reading widened by 0.5 percentage points at each end [35]. The archive manifest in `raw/MANIFEST.sha256` lists sha256, file and bytes for each raw copy archived 2026-11-05 [37]. GitHub issue text came from rendered pages and has no byte-exact copy [34].

## Report Metadata

- Run: WF-SILVER-DEEP-RESEARCH, mode deep, research_type default [36]
- Date: 2026-11-05
- Output directory: /home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research
- Sources registered: 37; evidence rows: 132
- Search provider: host WebSearch and WebFetch (search-cli unavailable)
