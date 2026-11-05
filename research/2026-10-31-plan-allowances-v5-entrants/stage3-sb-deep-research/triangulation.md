# DR-TRIANGULATE: cross-checks (O71 stage 3)

Admiralty grades are in `sources.jsonl` (reliability_code). Every candidate report is user-generated (C–D). Concordance between independent observers is what O11 relies on, so each check below is a check of independence and comparability.

## T1. New Plus 5-hour Terra report: SouthWindKnows (LINUX DO, via the locdd mirror) [3]
- **Observer and tier.** The post title states "Codex 20$ Plus Terra". The account is a USD Plus subscription. The UI is in Chinese, but the tier is not a regional one.
- **Model purity.**
  - The Codex usage for 2026-10-27 (CST) is gpt-6.1-terra at 56.98M tokens and $4.70, plus codex-auto-review at 0.57M tokens and $0.00.
  - The 5-hour panel's "used" figure, 57.54M tokens and $5, equals that sum to the token: 56.98M + 0.57M = 57.54M.
  - Auto-review has been free since Day 2.
  - The window is therefore Terra-only in priced terms.
- **Meter.** The 5-hour window was 77% used at 11:19 CST (03:19 UTC, 2026-10-27). The tool reads this from the official meter; the meter's 5-hour panel shows "remaining 23%".
- **Dollars.** The tool priced the window at $4.70.
  - Feasibility check at list prices ($1 / $0.05 / $5): the reported cache-hit rate is 98% (97.5–98.5%).
  - That implies $2.78–2.81 for cached input, with the remaining $1.89–1.92 explained by 0.60–1.30M uncached input and 0.12–0.26M output.
  - Output is then 0.2–0.5% of tokens, comparable to pensuke89's 0.1%.
  - The figure is therefore consistent with list pricing.
  - Limitation: the tool's per-model split of input and output is not shown.
- **Value.**
  - Point: $4.70 / 0.77 = $6.10 per 5h.
  - Range, allowing for whole-percent meter rounding (76.5–77.5%) and cent rounding: **$6.06–6.15 per 5h**.
  - The tool's own full-window estimate is "7473.23 万 · $6".
- **Timing.**
  - 03:19 UTC on 10-27, about 9 hours after launch.
  - Before the 17:23 UTC change that dennisvoss1978 reported, and before the Day 23 reset (10-28 02:42 UTC).
  - Not on an accounting-fault day.
  - Same period as pensuke89's readings.
- **Concordance.**
  - Tokens per meter point are 747k, against pensuke89's 768k (58% for 44.55M) [1]. That is 3% apart, at a similar cache share (98% against 98.2%).
  - Dollars per 5h: $6.06–6.15, against $5.28–5.51 [1] and $5.33 [2]. The ratio is 6.15 / 5.28 = 1.16, and the bound test is 6.06 ≤ 1.20 × 5.33 = 6.40.
- **Independence.** A different person on a different platform (LINUX DO, not r/codex) with a different tool (a macOS usage app, not a DeepSeek log sum).

## T2. Settling the #56866 discrepancy: same-account Terra/Sol ratios
Absolute tokens per point are not comparable across accounts, because the cache share and the output share differ. The Terra/Sol ratio measured on one account cancels the mix to first order. The provider claims "2X more usage than 6.1 Sol" and "half GPT-6.1 Sol's credit rate" [14][15].

| Observer | Basis | Terra/Sol tokens per point | Source |
|---|---|---|---|
| IndividualPlus2011 | $ per 5h, $5.33 vs $7.8, at half the price | 1.37 | [2] |
| el-rocho | same task and account, medium: 321k vs 225k per 1% | 1.43 | [4] |
| dennisvoss1978, after the ~10:23 PT update | CLI: 480k vs 369k per 1% | 1.30 | [4] |
| pensuke89 | weekly $34.33 vs "$45-50 with sol" (derived) | 1.37–1.53 | [1] |
| SouthWindKnows | 74.7M measured vs Sol "about 60M" from memory | ≈1.25 | [3][11] |
| dennisvoss1978, before the update | CLI: 191k vs 369k per 1% | **0.52** | [4] |

- **Result.** Five observers agree on a ratio of 1.25–1.53, not 2.0. The meter charges Terra about 1.4× more than its list-price share relative to Sol. In dollar terms, a Plus 5-hour window holds about 0.65–0.75× as much Terra as Sol.
- **Applied to the Plus 5h anchors.** The Sol anchors are $7.8 [2] and $8.3–8.7 (mehoney, 2026-10-25 run). The ratio puts el-rocho's run at **$5.6–6.2 per 5h** and dennisvoss1978's post-update run at **$5.1–5.7**. Both sit inside the priced cluster.
- **Why the GitHub readings looked 2–3× faster.** The gap was in tokens per point, which reflects the price per token of each run's mix. It was not in dollars per point.
- **The one outlier** is dennisvoss1978's pre-update CLI reading (implied about $2.0–2.3 per 5h, ratio 0.52). It fits two things:
  - his own observation of a metering change at about 17:23 UTC on 10-27;
  - HoYin1600p's unverified report that headless-CLI Terra is billed as Sol [6]. If it were, the ratio would be about 0.7.
- **Counter-observation.** pensuke89's and SouthWindKnows's app or tool readings, taken before 17:23 UTC, are concordant. So the faster pre-update rate was not universal. It may have been specific to the CLI or to some accounts. Chinese users on 10-27 also report "fast drain this morning, slower now" (09:06 UTC) [12].
- **Verdict on the discrepancy.** Mostly settled. The 10-28 reading (el-rocho) and the post-update reading (dennisvoss1978) agree with the priced reports once each is normalised to the same account's Sol rate. One pre-update CLI reading remains unexplained, and it carries no token split.

## T3. Claims about meter weighting (unverified, single-source)
- **SunnyDoll [12]** quotes her own LINUX DO post: a ChatGPT Team black-box test on 10-25..26, updated 10-27, gives Terra a "hidden multiplier as high as 1.9x". The text is truncated. The plan is Team, outside the cohort, and the original post is not mirrored. If the multiplier is read as a meter weight of 1.9× on Terra's list share, the Terra/Sol token ratio would be about 1.05, which conflicts with the 1.25–1.53 found above. Unresolved; context only.
- **WindGoesOn [13]** claims that GPT-6-series cache reads are metered at double rate. There is no data. pensuke89 and SouthWindKnows both ran at about 98% cache, so the claim cannot be tested with present reports. It does not change any verdict.
- **KiteRunner [11]** says Terra is "less than 30% cheaper than Sol" after weighting. That is consistent with T2 (a dollar ratio of 0.65–0.75 means 25–35% cheaper per unit of work at equal tokens).

## T4. Weekly and Pro candidates: why none qualifies
- **Plus weekly.**
  - pensuke89's $34.33 and IndividualPlus2011's $32 are both derived from 5-hour figures. Stage 2 established this, and pensuke89 confirms it [1].
  - SouthWindKnows's weekly panel shows 27%, 102M tokens and $15 (about $55.6 per week). The week began on 10-26 at about 05:19 UTC, before Terra launched (10-26 about 18:16 UTC), and the 44.5M tokens used on 10-26 (CST) predate Terra. The week is mixed-model and is excluded.
  - DreamRiver's "a week only holds 30-odd dollars" [11] gives no plan, basis or fraction.
  - Meter-only readings (TimeMachine [12], SlipperyBandicoot, facciocosevedogente3) carry no tokens.
- **Pro (both partitions).**
  - RealVovaPutin (Pro $200, 1B tokens ≈ 88% weekly; model unstated; no split; spans the launch) [7]: no Terra figure.
  - Theo's chart has Terra line items for Pro, but X is unreachable and the Fei2411 transcription gives no Terra figure [8].
  - benzonchan (Pro $100, mixed Terra/Sol, no tokens) [21].
  - Legitimate_Roll_2432 and others: Sol [20].
  - KiteHasWind ("terra ultra" emptied a weekly limit in 2 hours; plan and tokens unstated).
  - TimeMachine (30% of a Pro week, no tokens) [12].
  - None is priceable as Terra-only.

## T5. Carbon availability
- **Primary sources** [22][23][24][25]:
  - the blog keeps the staged rollout (cyber defenders, then Fairwind partners, then everyone else);
  - the API changelog (to Oct 30) has no Carbon;
  - the app release notes' newest entry is dated 10-13;
  - the Antigravity changelog to v2.28.2 (Oct 29) has no Carbon.
- **Users and press:**
  - HN 10-29 [27];
  - r/singularity on 10-31 02:51 UTC: "The Gemini team largely still can't access Carbon" [28];
  - nerdschalk's API-key check [30];
  - YouTube titles dated 10-29/30, e.g. "(And inaccessible)" [31].
- **Contrary claim.** El-Balad (10-28) [29] says Pro and Ultra subscribers can use Carbon in Antigravity and the Gemini app. It cites no Google source, contradicts the primary blog and changelogs, and appears to reuse Argon-launch wording. Rejected.
- **HN jeremyjjj [26]** ("available on Pro in Antigravity now … separate weekly limit") replies to a comment about Argon, and a later reply says "Still not seeing it". It is not evidence of Carbon access.
