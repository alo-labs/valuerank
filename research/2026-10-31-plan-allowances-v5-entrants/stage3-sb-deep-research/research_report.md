# GPT-6.1 Terra and Gemini 4 Carbon plan allowances after stage 3: the Plus 5-hour cell strengthens, weekly and Pro cells stay empty

## Executive Summary

Stage 3 ran Silver Bullet's Deep Research in deep mode, in the degraded configuration used in the previous run: no search-cli and no helper agents. It reached four channels that stages 1 and 2 did not [39]:
- LINUX DO, through its locdd.com mirror [3];
- Bluesky, through api.bsky.app [14];
- public X posts, through Yahoo! JAPAN real-time search [16];
- the Fei2411 community dataset [7].

It found one new qualifying report. On 2026-10-27, LINUX DO user SouthWindKnows logged a Terra-only Plus 5-hour window: 57.54M tokens priced at $4.70 at 77% of the window, which is $6.06–6.15 per 5 hours [3]. With pensuke89's $5.28–5.51 [1] and IndividualPlus2011's $5.33 [2], **GPT-6.1 Terra × Plus × 5h now meets O11 on three independent reports**. The largest lower bound, $6.06, is below 1.20 × the smallest upper bound, $6.40. The allowance is about $5.3–6.1 per 5h, and under O82 it does not convert to a billing period.

Stage 3 mostly settled the #56866 discrepancy. Five observers measured Terra against Sol on their own accounts and found that Terra yields 1.25–1.53× Sol's tokens per meter point, not the 2× that the provider implies [2][4][1][3][14][15]. Normalised by this ratio, el-rocho's and dennisvoss1978's post-update readings imply $5.1–6.2 per 5h, inside the priced cluster [4]. The "2–3× faster meter" was a difference in tokens per point between accounts with different cache and output mixes. Only dennisvoss1978's pre-update CLI reading remains an outlier [4][6].

No priceable Terra weekly report exists on Plus, and none exists on Pro $100, $200 or $500 either before or after the 2026-10-29 doubling. Each candidate is derived from 5-hour figures, mixed-model, or meter-only [1][2][3][7][8][11]. Those cells fail O11. **Gemini 4 Carbon was not available on any Google consumer plan at the cutoff** [22][23][24][25][28]. One contrary news claim is unsourced and is rejected [29]. Every Carbon cell has zero reports [38][37].

## Introduction

Owner decision O71 values first-party plans from actual end-user reports, and O11 sets the bar [35]. A cell needs at least two independent, non-provisional reports whose largest lower bound is at most 1.20 × the smallest upper bound (O86) [35]. The eligibility profile in `data/plan_cost_routes.json` (O71 v1, E270) has six requirements [35]:
- API-priced consumption tied to a meter fraction or window exhaustion;
- an exact model and tier;
- one model;
- a reading inside the window and not on an accounting-fault day;
- one observer per report;
- 5-hour figures pooled only with other 5-hour figures (O82) [35].

For OpenAI it records two partition events: the Pro 100/200/500 limit doubling on 2026-10-29, and the Day 23 global reset of 2026-10-27, which excludes any reading that spans it [35].

Stages 1 and 2 (see `../stage1-openai-terra.md` and `../stage2/report.md`) left three gaps [36][37]. There were no weekly reports, no Pro reports, and an open question over openai/codex #56866, whose readings implied a meter 2–3× faster per token than the two priced Plus reports [36][4]. Stage 2 also confirmed that Carbon was not offered on consumer plans [37]. Stage 3 prioritised weekly and Pro readings, then channels not yet searched, then the discrepancy, then Carbon. Prices used throughout: Terra $1 input / $0.05 cached input / $5 output per 1M tokens, plus $1.25 cache write (AA snapshot, as in stage 1) [36].

## Main Analysis

### Finding 1: A third independent Plus 5-hour report agrees with the first two

SouthWindKnows posted on LINUX DO on 2026-10-27 at 03:22 UTC under the title "Codex 20$ Plus Terra 今日速度和额度 100t/s 5小时可用 7000 万 Token 6 美元". The title means "Codex $20 Plus, Terra: today's speed and allowance, 100 t/s, a 5-hour window holds 70M tokens, 6 dollars." Three screenshots from the reporter's macOS usage tool are attached [3].

The usage-mix panel for 2026-10-27 (CST) lists:
- gpt-6.1-terra: 56.98M tokens, $4.70, 98% cache hits;
- codex-auto-review: 0.57M tokens, $0.00 [3][39].

The allowance panel, at 11:19 CST (03:19 UTC), shows the Codex 5-hour window "已用 5754.39 万 · $5 · 77%". That is 57.54M tokens used, which equals the day's Terra and auto-review tokens exactly. The panel's full-window estimate is "7473.23 万 · $6" [3]. Auto-review has been free since Day 2, so the priced consumption in the window is Terra alone.

The meter fraction comes from the official meter, which the tool reads, and the dollar figure comes from the tool. The tool's per-model split of input and output is not shown, so stage 3 checked the $4.70 against list prices [3][39]:
- a 97.5–98.5% cache share on 56.98M tokens gives $2.78–2.81 of cached input;
- the remaining $1.89–1.92 is explained by 0.60–1.30M uncached input tokens and 0.12–0.26M output tokens.

That is an output share of 0.2–0.5%, close to pensuke89's 0.1% [1]. The figure is therefore consistent with list pricing. The value is $4.70 / 0.77 = $6.10 per 5h. Allowing for whole-percent meter rounding and cent rounding, the range is $6.06–6.15. The 5-hour chart shows the window resetting at about 06:20 CST, with "6m" left at 11:19. The window therefore ran from about 22:20 UTC on 10-26 to 03:25 UTC on 10-27, entirely after Terra's launch [3]. The meter shows 23% remaining, so 77% was used. The chart's first sample (about 09:35 CST) already reads about 96%, which is why the tool shows "today −73%" [3]. The 57.54M tokens are the whole day's Codex logs, so they cover the earlier 4 points as well, and 77% is the matching fraction. Sensitivity: if those first 4 points had no tokens in the day count, the value would be $4.70 / 0.73 = $6.44. The bound test would then fail narrowly (6.44 > 6.40), and the cell would rest on the first two reports, which pass by themselves [1][2].

The report qualifies under the eligibility profile [35][3]:
- exact model;
- stated tier (a USD Plus subscription);
- one priced model;
- inside the window;
- not on a fault day;
- taken before the Day 23 reset and before the 17:23 UTC metering change that dennisvoss1978 reported.

It is independent of the other two. The observer, platform and tool are all different from pensuke89's DeepSeek-summed session logs and IndividualPlus2011's measurement. It also agrees with pensuke89 on a second axis: 747k tokens per meter point against pensuke89's 768k (58% of the window for 44.55M tokens), at almost the same cache share [1][3]. With three qualifying reports at [5.28, 5.51], [5.33, 5.33] and [6.06, 6.15], the cell passes, because 6.06 ≤ 1.20 × 5.33 = 6.40.

### Finding 2: The #56866 discrepancy reduces to one pre-update CLI reading

Tokens per meter point cannot be compared across accounts. They scale with the price per token of each run's mix, which depends on the cache and output shares. The #56866 commenters did not report those shares. The same-account ratio of Terra to Sol cancels the mix to first order. OpenAI's own framing implies a ratio of 2: Tibo, as relayed by QuotaTick, said Terra offers "2X more usage than 6.1 Sol", and a price-change log recorded "Half GPT-6.1 Sol's credit rate" [14][15].

Five observers measured or reported the ratio:
- IndividualPlus2011's $5.33 for Terra against $7.8 for Sol per 5h implies 1.37 at half the price [2].
- el-rocho's controlled same-task run gave 321k against 225k tokens per 1%, a ratio of 1.43. In his words, "So Terra was only about 1.43x more quota-efficient than Sol, not ~2x as the published credit pricing would suggest" [4].
- dennisvoss1978's post-update CLI reading gave 480k against 369k tokens per 1%, a ratio of 1.30 [4].
- pensuke89's derived weekly values ($34.33 for Terra against "$45-50 with sol") imply 1.37–1.53 [1].
- SouthWindKnows remembers about 60M tokens per 5h on Sol, against the 74.7M measured on Terra, about 1.25 [3][11].

The five values agree on 1.25–1.53. On Plus, a 5-hour window therefore holds about 0.65–0.75× as much Terra as Sol in dollar terms.

Applied to the Plus Sol anchors ($7.8 from IndividualPlus2011 [2] and $8.3–8.7 from mehoney in the 2026-10-25 run), the ratios give two implied values:
- el-rocho's run: $5.6–6.2 per 5h;
- dennisvoss1978's post-update run: $5.1–5.7 per 5h.

Both fall inside the priced cluster. The "2–3× faster meter" in #56866 was therefore a difference in tokens per point between accounts with different mixes, not a different dollar rate. The exception is dennisvoss1978's reading before the update at about 10:23 PT on 10-27. That reading gives a ratio of 0.52, or about $2.0–2.3 per 5h [4]. It fits HoYin1600p's unverified report that "if you use headless CLI it shows up as Sol" [6], since billing Terra as Sol would give a ratio near 0.7.

The faster rate was not universal. pensuke89's and SouthWindKnows's readings were taken before 17:23 UTC on 10-27, and both agree with the cluster [1][3]. On the same day, Chinese users reported fast drain in the morning that later slowed [12]. No OpenAI staff reply exists on #56866 [4]. Two weighting claims remain unverified and change no verdict:
- SunnyDoll quotes a ChatGPT Team black-box test that found a Terra "hidden multiplier as high as 1.9x" [12]. The test is on Team, which is outside the cohort, and the text is truncated.
- WindGoesOn asserts that GPT-6-series cache reads are metered at double rate [13]. No data is given.

### Finding 3: Plus weekly has candidates, but every one is derived, mixed-model or unpriced

No Plus weekly reading prices Terra-only consumption against the weekly meter. The candidates are listed below [1][2][3][11].
- pensuke89's "weekly 100% is $ 34.33" [1]. He later says "The weekly allowance is calculated from my own sub and there's also some people that measured it", so it is derived from 5-hour figures [1].
- IndividualPlus2011's $32 per week, which is exactly 6 × the 5h value [2].
- SouthWindKnows's weekly panel: 27% used, 102M tokens, $15, about $55.6 per week. The week started about 13 hours before Terra launched, and 44.5M of its tokens predate Terra, so it is a mixed-model week and is excluded [3].
- DreamRiver: "用下来一个星期只有30多刀的额度" ("a week only holds 30-odd dollars"). No plan, basis or meter fraction is given [11].

Meter-only weekly anecdotes carry no tokens. TimeMachine reports "Plus weekly gone in two hours" [12]. Stage 2 recorded SlipperyBandicoot and facciocosevedogente3. The two derived values ($32 and $34.33) agree with each other, and the 5h × 6 convention is consistent with them. Neither is a measurement of the weekly meter, so O11 is not met.

### Finding 4: Pro $100 / $200 / $500 have no Terra-priceable report on either side of the 2026-10-29 doubling

Tibo's Day 25 post doubled "all usage limits for all Pro 100/200/500 tiers and Business Premium, effective today" and kept Pro 200 "unchanged" [10][8]. Users saw the meter jump mid-week: "$100 weekly plan went from 3% remaining to 51%" [20].

Stage 3 found these Pro items:
- RealVovaPutin's Pro $200 week: "barely 1B tokens" ≈ 88%, with no model, no split, and a span across Terra's launch [7].
- Theo's chart of weekly API-equivalents. It has Terra line items, but the Fei2411 transcription records only the Sol values: about $981 per week on Pro $200 and about $2.4k on Pro $500 [8]. The X original was not reachable.
- benzonchan's Pro $100 task: "50% on Codex", mixed Terra and Sol [21].
- TimeMachine's "30% of a Pro week", with no tokens [12].
- Sol-only Pro readings such as Legitimate_Roll_2432's [20].

None prices Terra-only consumption against a Pro weekly meter. All six Pro cells (three tiers × two partitions) have zero qualifying reports. Under the eligibility profile, a Pro 5-hour cell does not exist.

### Finding 5: Gemini 4 Carbon was not available on any consumer plan at the cutoff

Primary sources hold the staged rollout:
- Google's blog: cyber defenders, then Fairwind partners, then "developers, businesses, and consumers" [22];
- the Gemini API changelog to October 30 has no Carbon entry [23];
- the Gemini app release notes' newest entry is the 2026-10-13 Argon launch [24];
- the Antigravity changelog to v2.28.2 (October 29) has no Carbon and no model-pool change [25].

User and press checks agree [27][28][30][31]:
- "How can one access Carbon? I only see Argon via gemini.google.com" (HN, 10-29) [27];
- "The Gemini team largely still can't access Carbon" (r/singularity, 2026-10-31 02:51 UTC) [28];
- a paid API key showed no Carbon model [30];
- YouTube titles from 10-29 and 10-30 describe it as "inaccessible" [31].

El-Balad's 10-28 article says Pro and Ultra subscribers "can also use it in Google Antigravity, the Gemini app" [29]. It links no Google source and contradicts every primary source, so it is rejected. A Hacker News comment that "it should be available on Pro in Antigravity now … separate weekly limit" replies to a comment about Argon, not Carbon, and a later reply says "Still not seeing it" [26]. Carbon therefore has no report on AI Plus, AI Pro or AI Ultra in any unit [38][37].

## Candidate Report Register (all stages)

"Q" means the report qualifies under the eligibility profile. S-numbers are stage-1 items, N1 is a stage-2 item, and T-numbers are new in stage 3. Dollar values are at list prices. Times are UTC.

| # | Plan | Unit | Model | Effort | Observer | URL | Date | Token split | Meter movement | $ at list | Q? | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | Plus (stated) | 5h | GPT-6.1 Terra | unstated | pensuke89 | reddit.com/r/codex/comments/1xgcwoq | 10-26 23:37 – 10-27 08:57 | 43,758,336 cached / 748,338 uncached / 45,459 output | 58% (also 27% earlier) | $5.28–5.51 per 5h | **Yes** | exact model and tier, one model, priced split, before the Day 23 reset [1] |
| S2 | Plus (stated) | 5h | GPT-6.1 Terra | xhigh | IndividualPlus2011 | reddit.com/r/codex/comments/1xhhrxs | 10-28 07:44 | not published | own measurement | $5.33 per 5h | **Yes** | observer's own measurement; after the Day 23 reset, not spanning it [2] |
| T1 | Plus (stated "Codex 20$ Plus") | 5h | GPT-6.1 Terra (plus free auto-review) | unstated | SouthWindKnows | locdd.com/t/104195 (mirror of LINUX DO) | 10-27 03:19 | 56.98M tokens, 98% cache hit, $4.70 (tool-priced; consistent with list at 0.6–1.3M uncached / 0.12–0.26M output) | 77% of 5h | **$6.06–6.15 per 5h** | **Yes (new)** | exact model and tier, Terra-only priced window, official meter fraction, before the 17:23 shift and the Day 23 reset [3] |
| S1w | Plus | week | GPT-6.1 Terra | — | pensuke89 | 1xgcwoq 19rpkdemtj84g | 10-27 | — | not shown | $34.33 per week | No | derived from 5h figures [1] |
| S2w | Plus | week | GPT-6.1 Terra | xhigh | IndividualPlus2011 | 1xhhrxs | 10-28 | — | derived (6 × 5h) | $32 per week | No | derived [2] |
| T1w | Plus | week | mixed (pre-launch models on 10-26 + Terra) | — | SouthWindKnows | locdd.com/t/104195 | 10-27 03:19 | 102M tokens, $15 | 27% of week | ≈$55.6 per week (plan level) | No | mixed-model week (started 10-26 ≈05:19, before Terra's launch) [3] |
| T2 | unstated (Plus implied) | week | GPT-6.1 Terra | unstated | DreamRiver | locdd.com/t/105059 #8 | 10-29 | none | none | "30-odd dollars" per week | No | no plan, basis or meter fraction [11] |
| S3 | Plus (carried; provisional) | 5h | GPT-6.1 Terra | medium | el-rocho | github.com/openai/codex/issues/56866 | 10-28 | ≈5.14M, "heavily cached", no split | 40→56% | $1.8–7.8 per 5h; same-account Sol ratio implies $5.6–6.2 | No (provisional in the range test) | no split; tier carried over [4] |
| S4 | Plus | 5h | GPT-6.1 Terra | xhigh | dennisvoss1978 | openai/codex #56866 | 10-27 | input only (1.91M; 1.92M) | 9→19%; after the update 22→26% | before ≈$2.0–2.3 (ratio 0.52), after $5.1–5.7 (ratio 1.30) | No | no split or output; CLI [4] |
| S5 | "Pro Plan" (tier unstated) | 5h (doubtful) | mixed (Sol, Terra, Luna) | — | Emotional-Cut2952 | r/codex 1xhx3ab | 10-28 | full split, 3 models | 90% | ≈$5.9 per 5h at plan level | No | three models; tier unstated; Pro has no 5h window |
| S6 | Plus | 5h / week | GPT-6.1 Terra | high | HoshiEstrellas | openai/codex #57627 | 10-28 | 0 tokens | 5h shows 0% remaining | — | No | accounting anomaly |
| N1 | Plus (stated) | 5h | GPT-6.1 Terra | xhigh; max | ayudha90 | r/codex 1xgcjjb, 1xgriu5 | 10-27 | none; author's $ only | 3%; 1%; 4% | $2.60–14.8 per 5h | No | pricing basis undisclosed, no tokens [5] |
| T3 | Pro $200 | week | unstated (spans Terra's launch) | — | RealVovaPutin (via Fei2411 #149) | github.com/Fei2411/real-api-pricing/issues/149 | 10-26/27 | ≈1B total, no split | ≈88% of week | not priceable | No | model unstated, no split, aggregator transcription of an X post [7] |
| T4 | Pro $200 / $500 | week | Terra line items (values not transcribed) | — | Theo (via Fei2411 #161) | github.com/Fei2411/real-api-pricing/issues/161 | ≈10-29/30 | — | — | Sol only: ≈$981 / ≈$2.4k per week | No | Terra values unreachable (X); chart method not shown [8] |
| T5 | Plus | 5h | GPT-6.1 Terra | xhigh | @terapicos | x.com/terapicos/status/2115273055975137495 | 10-28 02:42 | none | 80% in 20 min (subagents) | — | No | meter only [16] |
| T6 | Plus | 5h | GPT-6.1 Terra | high | RainPoet | locdd.com/t/105059 #1 | 10-29 16:34 | none | 25% in 10 min | — | No | meter only [11] |
| T7 | unstated | 5h | GPT-6.1 Terra | — | @smotanija | x.com/smotanija/status/2116194247108071621 | 10-30 15:43 | none | <10% of 5h for a session | — | No | meter only [18] |
| T8 | unstated | unstated | GPT-6.1 Terra (computer use) | — | @kamikamidaisuki | x.com/kamikamidaisuki/status/2116157639998787841 | 10-30 13:17 | none | ≈4% | — | No | meter only; unit unstated [17] |
| T9 | Plus then Pro | week | Terra (implied) | — | TimeMachine | locdd.com/t/104275 #17 | 10-27 09:06 | none | Plus week in 2 h; 30% of a Pro week | — | No | meter only; tier and model loosely stated [12] |
| T10 | unstated | week | "terra ultra" | ultra / ultrafast | KiteHasWind | locdd.com/t/105274 #3 | 10-30 07:47 | none | weekly gone in 2 h | — | No | meter only; plan unstated |
| T11 | Team 1x (out of cohort) | 5h / 7d | GPT-6.1 Terra | — | SunnyDoll (quoted) | locdd.com/t/104275 #9 | 10-25..27 | not available | "hidden multiplier as high as 1.9x" | — | No | Team plan; original post unreachable [12] |
| — | Pro $100 / Pro tier unstated / "20x" | week | mixed or Luna | — | benzonchan, ArugulaAnnual1765, Proxiconn, TheTwistedTabby, Humble-Kiwi-5272, BearsAreCrying, xter418 (stage 2) | r/OpenaiCodex 1xipkr0 etc. | 10-27..30 | none | various | — | No | meter only and/or mixed [21] |

No Gemini 4 Carbon candidate report exists on any tier.

## O11 Assessment (model × tier × unit)

| Model × tier × unit | Qualifying reports (bounds, $) | Range test (largest lower bound ≤ 1.20 × smallest upper bound) | O11 |
|---|---|---|---|
| Terra × Plus × 5h | pensuke89 [5.28, 5.51]; IndividualPlus2011 [5.33, 5.33]; **SouthWindKnows [6.06, 6.15] (new)** | 6.06 ≤ 1.20 × 5.33 = 6.40 ✓. Adding the provisional el-rocho [1.8, 7.8] still passes | **Met**, ≈$5.3–6.1 per 5h; no conversion to week or month (O82) [1][2][3][35] |
| Terra × Plus × week (→ month) | 0 (two derived values, one mixed week, one unbased claim) | — | Not met |
| Terra × Pro $100 × week, before 10-29 / after 10-29 | 0 / 0 | — | Not met |
| Terra × Pro $200 × week, before / after | 0 / 0 | — | Not met |
| Terra × Pro $500 × week, before / after | 0 / 0 | — | Not met |
| Terra × Pro (any) × 5h | n/a (Pro has no 5h window) | — | n/a |
| Carbon × AI Plus / AI Pro / AI Ultra × 5h, day, week, month | 0 | — | Not met: not offered on any consumer plan at the cutoff |

## Synthesis

Stage 3 strengthens the one passing cell and leaves the empty cells empty. The Plus 5-hour value now rests on three independent observers, on two platforms and three tools, within a 1.16× spread. Two of them also agree on tokens per meter point, to within 3%. The metering question that threatened the cell has a mechanical explanation. Measured against Sol on the same account, Terra yields about 1.4× Sol's tokens per point, against the 2× implied by price. The GitHub readings that looked 2–3× faster are consistent with the priced cluster once each account's mix is normalised. One pre-update CLI reading remains anomalous. It points to a transient or harness-specific metering issue on 10-27, not to a second steady meter rate.

The weekly and Pro gaps are structural. Terra had been on sale for about four and a half days at the cutoff, with a global reset on day 2 and a Pro doubling on day 4. Few users could complete a Terra-only weekly measurement in that time. Every Pro measurer found mixed Terra with Sol, Luna or Astra.

## Limitations

- **Unreachable channels.**
  - X itself: login wall. Only Yahoo! JAPAN real-time snippets were available, and these skew Japanese. Theo's chart with its Terra lines was not reachable.
  - YouTube watch pages redirect to a consent or bot check. Only result metadata was used.
  - linux.do: 403. The locdd mirror was used, and SunnyDoll's original post is not mirrored.
  - Zhihu: 403. Xiaohongshu: redirect. Bilibili search API: 412. public.api.bsky.app: 403 (api.bsky.app worked).
  - note.com search API returned nothing.
- **Degraded configuration.** search-cli was absent and no helper agents could be spawned, so all retrieval was sequential.
- **The new report's window attribution.** It assumes that the tool's whole-day token count belongs to the 77% window. The alternative reading (73%) would fail the margin narrowly.
- **The new report's pricing.** It relies on the reporter's tool. Stage 3 checked feasibility at list prices but did not see the per-model input and output split. It also relies on the mirror's fidelity. Timestamps match linux.do conventions, and the post references linux.do topic 2998090.
- **Speed mode.** No Plus 5-hour reporter states standard or Fast mode. Fast mode would multiply the value by 2.5. The agreement of three reporters makes Fast unlikely, but it is unverified.
- **Same-account ratios.** Two are derived (IndividualPlus2011 from dollar values, pensuke89 from weekly derivations), and one is from memory (SouthWindKnows's Sol value).
- **Source quality.** Average source reliability is C–D. That is inherent to user reports.

## Recommendations

1. Record GPT-6.1 Terra × ChatGPT Plus × 5h as passing O11 at about $5.3–6.1 API-$ per 5h, based on three reports (pensuke89, IndividualPlus2011, SouthWindKnows). Note the launch-week caveat and the one unexplained pre-update CLI reading.
2. Keep Plus weekly and all Pro Terra cells at "not met". Recruit Terra-only, full-week measurements after the Day 25 doubling: Plus, then Pro $100 and Pro $200. Each should give the cached, uncached and output split and state standard or Fast mode.
3. Keep Carbon at "not available". Recheck once Google lists Carbon on the AI plans page, the Gemini app release notes or the Antigravity changelog.
4. If the owner wants the discrepancy closed fully, ask a CLI user for a same-task CLI-versus-app A/B with session-file token_count events.

## Counterevidence Register

- **Against the Plus 5h pass:**
  - dennisvoss1978's pre-update CLI reading implies about $2.0–2.3 per 5h [4]. It has no split, so it is not eligible.
  - SunnyDoll's "1.9x hidden multiplier" (Team) implies a lower Terra allowance than the cluster [12].
  - Many meter-only complaints describe very fast drain [11][16].
  - All three admitting readings fall in launch week (10-26..28).
  - SouthWindKnows's tool shows a 73% fall since its first sample against 77% used on the meter. Read at 73%, the value is $6.44, above the 6.40 margin [3].
- **Against the discrepancy ruling:**
  - el-rocho says both his runs were "heavily cached". If his Terra run matched pensuke89's mix, his tokens per point would imply a lower dollar value [4].
  - The ratio method assumes that same-account Sol values match the Plus Sol anchors.
- **Against "Carbon not available":** El-Balad's claim [29], and jeremyjjj's Antigravity remark, which this report reads as being about Argon [26].

## Claims-Evidence Table

| Claim | Evidence | Sources |
|---|---|---|
| SouthWindKnows: 57.54M Terra tokens, $4.70, 77% of the Plus 5h window → $6.06–6.15 | screenshots (allowance and usage panels) | [3] |
| Plus 5h O11 met on three reports | bound test 6.06 ≤ 6.40 | [1][2][3] |
| Same-account Terra/Sol token ratio 1.25–1.53, not 2 | five observers; provider claims | [2][4][1][3][11][14][15] |
| #56866 readings consistent once normalised; one pre-update CLI outlier | ratio arithmetic; CLI billing report | [4][6] |
| No qualifying Plus weekly report | derived, mixed and unbased items | [1][2][3][11] |
| No Terra-priceable Pro report before or after 10-29 | Pro items mixed, unstated or unreachable | [7][8][20][21][10] |
| Carbon not on consumer plans at the cutoff | primary changelogs, blog, user checks | [22][23][24][25][27][28][30] |

## Bibliography

[1] u/pensuke89 (2026). "GPT-6.1 Terra Plus 5-hour API-equivalent measurement (post and comments 19rpkdemtj84g, 19rq2uvffez8h, 19rsujitn7rad)". Reddit r/codex. URL: https://www.reddit.com/r/codex/comments/1xgcwoq/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/codex/comments/1xgcwoq/)
[2] u/IndividualPlus2011 (2026). "Allowance table update for GPT & competitors and Terra opinion". Reddit r/codex. URL: https://www.reddit.com/r/codex/comments/1xhhrxs/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/codex/comments/1xhhrxs/)
[3] SouthWindKnows (2026). "Codex 20$ Plus Terra 今日速度和额度 100t/s 5小时可用 7000 万 Token 6 美元". LINUX DO, via the locdd.com mirror. URL: https://locdd.com/t/104195 (Retrieved: 2026-10-31) [link](https://locdd.com/t/104195)
[4] el-rocho; dennisvoss1978 (2026). "Plus 5-hour limit drains in minutes (comments)". GitHub openai/codex issue 56866. URL: https://github.com/openai/codex/issues/56866 (Retrieved: 2026-10-31) [link](https://github.com/openai/codex/issues/56866)
[5] u/ayudha90 (2026). "GPT 6.1 Terra on GPT Plus". Reddit r/codex. URL: https://www.reddit.com/r/codex/comments/1xgcjjb/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/codex/comments/1xgcjjb/)
[6] u/HoYin1600p (2026). "Comment 19ruxfb27va1v on 'Is anyone else burning through Codex usage faster with GPT-6.1 Terra Max than Sol High?'". Reddit r/codex. URL: https://www.reddit.com/r/codex/comments/1xizol3/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/codex/comments/1xizol3/)
[7] Fei2411 maintainers (2026). "2026-10-28 · Codex / ChatGPT Pro $200 周限用量（~1B tokens ≈ 88–94%）". GitHub Fei2411/real-api-pricing issue 149. URL: https://github.com/Fei2411/real-api-pricing/issues/149 (Retrieved: 2026-10-31) [link](https://github.com/Fei2411/real-api-pricing/issues/149)
[8] Fei2411 maintainers (2026). "2026-10-30 ChatGPT Pro 100/200/500 Day25 用量翻倍 + theo API-eq + Dec 共享池信号". GitHub Fei2411/real-api-pricing issue 161. URL: https://github.com/Fei2411/real-api-pricing/issues/161 (Retrieved: 2026-10-31) [link](https://github.com/Fei2411/real-api-pricing/issues/161)
[9] Fei2411 maintainers (2026). "2026-10-27 · GPT-6.1 Terra API/订阅上线 + 促销/折扣信号". GitHub Fei2411/real-api-pricing issue 145. URL: https://github.com/Fei2411/real-api-pricing/issues/145 (Retrieved: 2026-10-31) [link](https://github.com/Fei2411/real-api-pricing/issues/145)
[10] OpenAI community (VeitB quoting Tibo) (2026). "28 days of shipping (Days 22-25 posts #110, #117)". OpenAI Developer Community. URL: https://community.openai.com/t/1403525 (Retrieved: 2026-10-31) [link](https://community.openai.com/t/1403525)
[11] RainPoet; SouthWindKnows; DreamRiver; KiteRunner (2026). "terra计费真的没问题吗？". LINUX DO, via the locdd.com mirror. URL: https://locdd.com/t/105059 (Retrieved: 2026-10-31) [link](https://locdd.com/t/105059)
[12] SunnyDoll; DolphinLover; TimeMachine (2026). "gpt-6.1 terra max消耗问题". LINUX DO, via the locdd.com mirror. URL: https://locdd.com/t/104275 (Retrieved: 2026-10-31) [link](https://locdd.com/t/104275)
[13] WindGoesOn (2026). "Tibo：取消额度减半". LINUX DO, via the locdd.com mirror. URL: https://locdd.com/t/105062 (Retrieved: 2026-10-31) [link](https://locdd.com/t/105062)
[14] QuotaTick (2026). "Terra Model Relaunched with 2X Usage (relay of @thsottiaux)". Bluesky. URL: https://bsky.app/profile/quotatick.com/post/3myshn2u5bm2t (Retrieved: 2026-10-31 via api.bsky.app) [link](https://bsky.app/profile/quotatick.com/post/3myshn2u5bm2t)
[15] AI Builders Use (2026). "Codex adds GPT-6.1 Terra on Plus and up (price-changes log)". Bluesky. URL: https://bsky.app/profile/aibuildersuse.bsky.social/post/3myuflvks4b2l (Retrieved: 2026-10-31 via api.bsky.app) [link](https://bsky.app/profile/aibuildersuse.bsky.social/post/3myuflvks4b2l)
[16] @terapicos (2026). "Terra (xhigh) 20分間 80%消費 (Plus 5時間制限)". X. URL: https://x.com/terapicos/status/2115273055975137495 (Retrieved: 2026-10-31 via Yahoo! JAPAN real-time search) [link](https://x.com/terapicos/status/2115273055975137495)
[17] @kamikamidaisuki (2026). "6.1 Terraの使用量増えてない?". X. URL: https://x.com/kamikamidaisuki/status/2116157639998787841 (Retrieved: 2026-10-31 via Yahoo! JAPAN real-time search) [link](https://x.com/kamikamidaisuki/status/2116157639998787841)
[18] @smotanija (2026). "6.1Terraしか動かしてないけど、５h枠の10%も使わなかった". X. URL: https://x.com/smotanija/status/2116194247108071621 (Retrieved: 2026-10-31 via Yahoo! JAPAN real-time search) [link](https://x.com/smotanija/status/2116194247108071621)
[19] u/Fickle-Ad3007 (2026). "Plus Codex window value (comment 19rwfxbwc0n42)". Reddit r/codex. URL: https://www.reddit.com/r/codex/comments/1xjpxrx/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/codex/comments/1xjpxrx/)
[20] r/codex users (2026). "Day 25 doubling thread (irritatingness 19rubkpvlvrad; Legitimate_Roll_2432 19ru99885seea)". Reddit r/codex. URL: https://www.reddit.com/r/codex/comments/1xipj7s/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/codex/comments/1xipj7s/)
[21] r/OpenaiCodex users (2026). "Pro 5x switch thread (benzonchan 19rv3x5go1y4k; Round_Ganache_4634 19rubqssvrjlw)". Reddit r/OpenaiCodex. URL: https://www.reddit.com/r/OpenaiCodex/comments/1xipkr0/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/OpenaiCodex/comments/1xipkr0/)
[22] Google (2026). "Introducing Gemini 4 Carbon". Google blog. URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ (Retrieved: 2026-10-31) [link](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
[23] Google (2026). "Gemini API changelog". Google AI for Developers. URL: https://ai.google.dev/gemini-api/docs/changelog (Retrieved: 2026-10-31) [link](https://ai.google.dev/gemini-api/docs/changelog)
[24] Google (2026). "Gemini app release notes". Google. URL: https://gemini.google/release-notes/ (Retrieved: 2026-10-31) [link](https://gemini.google/release-notes/)
[25] Google (2026). "Google Antigravity changelog". Google. URL: https://antigravity.google/docs/changelog (Retrieved: 2026-10-31) [link](https://antigravity.google/docs/changelog)
[26] jeremyjjj (2026). "HN comment on Gemini 4 Carbon thread". Hacker News. URL: https://news.ycombinator.com/item?id=50278504 (Retrieved: 2026-10-31 via HN Algolia) [link](https://news.ycombinator.com/item?id=50278504)
[27] quibono (2026). "How can one access Carbon?". Hacker News. URL: https://news.ycombinator.com/item?id=50288810 (Retrieved: 2026-10-31 via HN Algolia) [link](https://news.ycombinator.com/item?id=50288810)
[28] u/sultanofsubstance (2026). "Comment 19rwrg9g5q00w". Reddit r/singularity. URL: https://www.reddit.com/r/singularity/comments/1xjwqf3/ (Retrieved: 2026-10-31 via arctic-shift) [link](https://www.reddit.com/r/singularity/comments/1xjwqf3/)
[29] Brittany Shaw (El-Balad) (2026). "Google expands Gemini 4 Carbon globally to developers and subscribers". El-Balad. URL: https://www.el-balad.com/17061776 (Retrieved: 2026-10-31) [link](https://www.el-balad.com/17061776)
[30] Nerdschalk (2026). "Gemini 4 Carbon Public Release Date: What Google Has Announced". Nerdschalk. URL: https://nerdschalk.com/gemini-4-carbon-public-release-date-what-google-has-announced/ (Retrieved: 2026-10-31) [link](https://nerdschalk.com/gemini-4-carbon-public-release-date-what-google-has-announced/)
[31] Erwan | IA (2026). "Gemini 4 Carbon is scary. (And inaccessible)". YouTube (search-result metadata only). URL: https://www.youtube.com/watch?v=JHyq5qiE7iQ (Retrieved: 2026-10-31) [link](https://www.youtube.com/watch?v=JHyq5qiE7iQ)
[32] FinOpsLLM (2026). "How much Codex does ChatGPT Pro include? We priced the weekly limit in dollars". FinOpsLLM. URL: https://finopsllm.com/research/codex-usage-limits-chatgpt-pro (Retrieved: 2026-10-31) [link](https://finopsllm.com/research/codex-usage-limits-chatgpt-pro)
[33] Paweł Huryn (2026). "subscription-multipliers experiments". GitHub phuryn/experiments. URL: https://github.com/phuryn/experiments/tree/main/subscription-multipliers (Retrieved: 2026-10-31) [link](https://github.com/phuryn/experiments/tree/main/subscription-multipliers)
[34] openai/codex users (2026). "Issue search: usage/rate/weekly limit issues created since 2026-10-26 (59 results)". GitHub. URL: https://github.com/openai/codex/issues?q=is%3Aissue+%28%22usage+limit%22+OR+%22rate+limit%22+OR+weekly%29+created%3A%3E%3D2026-10-26 (Retrieved: 2026-10-31) [link](https://github.com/openai/codex/issues?q=is%3Aissue+%28%22usage+limit%22+OR+%22rate+limit%22+OR+weekly%29+created%3A%3E%3D2026-10-26)
[35] ValueRank (2026). "Plan cost routes: evidencePolicy.reportEligibilityProfile (O71 v1, E270)". Local repository file. URL: file:///home/user/valuerank/data/plan_cost_routes.json (Retrieved: 2026-10-31) [link](file:///home/user/valuerank/data/plan_cost_routes.json)
[36] ValueRank stage 1 (2026). "Stage 1 (plain web search): OpenAI ChatGPT / Codex plans, GPT-6.1 Terra". Local research file. URL: file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage1-openai-terra.md (Retrieved: 2026-10-31) [link](file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage1-openai-terra.md)
[37] ValueRank stage 2 (2026). "Stage 2 (Claude Deep Research): GPT-6.1 Terra and Gemini 4 Carbon plan allowances". Local research file. URL: file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage2/report.md (Retrieved: 2026-10-31) [link](file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage2/report.md)
[38] ValueRank stage 1 (2026). "Stage 1 (plain web search): Google AI Pro / Ultra plans, Gemini 4 Carbon". Local research file. URL: file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage1-google-carbon.md (Retrieved: 2026-10-31) [link](file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage1-google-carbon.md)
[39] ValueRank stage 3 (Silver Bullet Deep Research) (2026). "O71 stage 3 (Terra/Carbon) research plan, run manifest and raw retrieval logs". Local research file. URL: file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage3-sb-deep-research/research-plan.md (Retrieved: 2026-10-31) [link](file:///home/user/valuerank/research/2026-10-31-plan-allowances-v5-entrants/stage3-sb-deep-research/research-plan.md)

## Methodology

Run: Silver Bullet `/sb:deep-research` (FS-SILVER_DEEP_RESEARCH, AF-DECIDE), deep mode, research_type `default` [39]. All nine phases ran (scope, plan, retrieve, triangulate, outline, synthesize, critique with two cycles, refine, package). search-cli was absent and no Task or Agent tool was available, so retrieval was sequential in the lead agent through host WebSearch, WebFetch and curl via the agent proxy. Sources are registered in `sources.jsonl` (39: 34 web, 5 local documents), evidence spans in `evidence.jsonl`, and raw dumps in `raw/` (including the three SouthWindKnows screenshots in `raw/images/`). All web content was treated as data [39]. There was no sign-in, no bot-check solving and no paid service [39].

### Queries (stage 3)

1. arctic-shift, Reddit comments 2026-10-26..cutoff, full dumps: [39]
   - r/codex: 9,800 comments, from 10-26 00:26; [39]
   - r/OpenaiCodex: 1,300; [39]
   - r/ChatGPTPro: 840. [39]
   Each dump was filtered by regex for "week" + "%" + tokens/$/credits (48 hits) and for Terra plus numbers (135 hits, 109 from observers not seen in stages 1–2). Hits were then filtered strictly for token or dollar figures with a meter percentage. [39]
2. arctic-shift, posts 2026-10-26..cutoff in r/codex (661), r/OpenaiCodex (70), r/ChatGPTPro (108), r/ChatGPTCoding (100) and r/OpenAI (0 returned), filtered for priced Terra posts. [39]
3. arctic-shift, Carbon: comments since 10-28 in r/google_antigravity (1,178), r/Bard (283), r/GeminiAI (3,591), r/GoogleGeminiAI (219) and r/singularity (9,900), filtered for "carbon" plus access, usage or limit terms (109 hits). [39]
4. arctic-shift author histories after 10-28 12:00: pensuke89, IndividualPlus2011, ayudha90, el-rocho, Fickle-Ad3007. Comment id 19rrvgjzzn74w; post id 1xhhrxs. [39]
5. locdd.com (LINUX DO mirror) search.json, each with after:2026-10-25: "terra", "6.1 terra", "codex 周限", "codex 额度", "carbon", "terra 5小时", "terra 周额度", "terra plus 额度", "codex 额度 美元", "terra pro", "codex pro 周", "额度用满预估". Also "隐藏倍率", "terra 倍率" and "黑盒实测" (topics). Topics read in full: 104195 (and its 3 images), 104275, 105059, 105062. User activity for SouthWindKnows. [39]
6. api.bsky.app searchPosts (since 10-26, up to 3 pages each): "terra codex", "6.1 terra", "gpt-6.1-terra", "terra limit", "terra usage", "terra weekly", "terra plus", "terra pro", "codex weekly limit", "codex usage limit", "gemini 4 carbon", "carbon antigravity", "carbon ultra" (436 unique posts). [39]
7. Yahoo! JAPAN real-time search (public X posts): "GPT-6.1 Terra", "Terra Codex", "Terra 使用量", "Terra 制限", "Terra 週", "Terra Plus", "Terra Pro", "Codex 週間制限", "Gemini 4 Carbon", "Carbon Antigravity" (160 Terra/Carbon posts since 10-26 retained). [39]
8. HN Algolia search_by_date 2026-10-26..cutoff: "6.1 terra", "terra" codex, "terra" limit, "terra" weekly, "terra" plus, "terra" pro, gemini carbon, "carbon" antigravity, "carbon" ultra (109 hits). Items 50278504 and its parent were read. [39]
9. GitHub (WebFetch): [39]
   - Fei2411/real-api-pricing issues "terra" (15 results); issues 149, 161 and 145 read; [39]
   - openai/codex `is:issue terra created:>=2026-10-29` (11 results); [39]
   - openai/codex usage/rate/weekly limit issues created since 10-26 (3 pages, 59 results); [39]
   - #56866 re-read; [39]
   - phuryn/experiments subscription-multipliers and commits; [39]
   - cross-repo issue search "gpt-6.1-terra" with weekly or limit terms. [39]
10. OpenAI forum search.json: "terra after:2026-10-29", "terra weekly after:2026-10-28", "pro weekly after:2026-10-29", "doubled after:2026-10-29", "tokens weekly after:2026-10-28" (47 posts). [39]
11. sov2ex (V2EX): "terra 额度", "terra 周", "codex terra". [39]
12. note.com search API: "Terra Codex", "GPT-6.1 Terra 使用量", "Codex 週間制限 Terra" (no results returned). [39]
13. YouTube results pages, metadata only: "gpt-6.1 terra codex limit", "terra codex usage plus", "codex pro weekly limit terra", "gemini 4 carbon access" (77 results). [39]
14. WebSearch: [39]
    - theo Codex Pro weekly API-equivalent chart (twice); [39]
    - "Terra" Codex Pro weekly site:x.com; [39]
    - youtube GPT-6.1 Terra Codex usage limit test; [39]
    - "Gemini 4 Carbon" now available; [39]
    - macOS Codex usage menu-bar tool; [39]
    - "gpt-6.1-terra" 隐藏倍率 1.9x. [39]
15. WebFetch of pages: finopsllm, xenospectrum NerfTrack, tokensave, developersdigest, smzdm, gemini.google release notes, ai.google.dev changelog, antigravity.google changelog (via redirect), El-Balad, nerdschalk. [39]

Totals: 15 query groups, about 140 individual queries and fetches [39].

### Sources reached

- arctic-shift (Reddit comments, posts, ids and author histories); [39]
- locdd.com (LINUX DO mirror: search, topics and images) — new in stage 3; [39]
- api.bsky.app (Bluesky) — new; public.api.bsky.app is still 403; [39]
- Yahoo! JAPAN real-time search (public X posts) — new; [39]
- HN Algolia (search and items); [39]
- github.com HTML through WebFetch (issues, search, repository trees, commits); [39]
- Fei2411/real-api-pricing — new for this model; [39]
- the OpenAI community forum JSON; [39]
- sov2ex; [39]
- YouTube results pages (metadata); [39]
- WebSearch; [39]
- Google blog, Gemini API changelog, Gemini app release notes, Antigravity changelog; [39]
- finopsllm, xenospectrum, tokensave, developersdigest, smzdm, El-Balad, nerdschalk. [39]

### Sources unreachable or not usable

| Source | Result |
|---|---|
| linux.do | 403 (Cloudflare) |
| SunnyDoll's original LINUX DO post | not mirrored |
| X/Twitter direct | login wall; Theo's chart and @Nonosam2/@NimadFlow screenshots not read |
| YouTube watch pages and transcripts | 302 to consent or bot check, not circumvented |
| Zhihu API | 403 |
| Xiaohongshu | 301 redirect |
| Bilibili search API | 412 |
| public.api.bsky.app | 403 |
| mastodon.social search | empty |
| note.com search API | empty response |
| GitHub REST/GraphQL | not used (403 in stages 1–2) |
| Antigravity /changelog | redirect stub; /docs/changelog worked |
| Gemini release notes beyond the first 100k characters | not read |

## Appendix: Partition and timing reference

- Terra launch: 2026-10-26, about 18:16 UTC [36][14].
- 10-27 about 17:23 UTC: user-observed metering change (dennisvoss1978). Single observation; flagged, splits nothing [4][35].
- Day 23 global reset: announced 2026-10-28 02:42 UTC (10-27 PT). A reading that spans it is excluded [37][35].
- Day 25: Pro 100/200/500 limits doubled, 2026-10-29 (about 16:56 PT). Limit split for every Pro tier [10][35].
- Gemini 4 Carbon: announced 2026-10-28. Rollout to cyber defenders, then Fairwind partners, then consumers. No consumer date [22][38].

## Report Metadata

Run [39]: O71 stage 3 (Silver Bullet `/sb:deep-research`, FS-SILVER_DEEP_RESEARCH, AF-DECIDE), deep mode, research_type default. Date: 2026-10-31; cutoff 2026-10-31T04:10:00Z. Retrieval: host WebSearch and WebFetch plus curl, degraded (search-cli absent, no helper agents). Sources registered: 39 (34 web, 5 local). Evidence spans: 67. Output directory: research/2026-10-31-plan-allowances-v5-entrants/stage3-sb-deep-research [39].
