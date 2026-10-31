# Stage 1 (plain web search), DeepSeek and MiniMax — 2026-10-25

## DeepSeek (DeepSeek-V4.1-Flash-1017, max)
No first-party subscription (re-confirmed): https://api-docs.deepseek.com/quick_start/pricing lists per-token and
per-request billing only; the 1017 release note (https://api-docs.deepseek.com/news/news261017) mentions no plan;
thinking effort low / high / max (default high). deepseekv4pro.com's "DeepSeek Coding Plan $19.90/month" is not a
DeepSeek domain (reseller or impersonator). Third-party plans carrying V4.1 Flash (not first-party): OpenCode Go,
Alibaba Model Studio TokenPlan, Command Code. API (per 1M, off-peak / peak): cache hit $0.003 / $0.006, miss $0.15 /
$0.30, output $0.60 / $1.20. Qualifying user reports: 0 (no plan).

## MiniMax (MiniMax-M3.1-Flash; GA 2026-10-19, Preview on plans from ≈2026-09-27)
API: $0.15 input / $0.60 output / $0.015 cache read per 1M; effort low…max, default max.
M Plan (replaced Token Plan ≈2026-09-29/30; https://platform.minimax.io/docs/m-plan/intro, faq, usage-rules,
token-plan-notice): Go $22 (¥49) 1×, Explore $55 (¥119) 3×, Build $132 (¥469) 7.5× (international) / 12× (CN docs).
5-hour and weekly windows; no absolute allowance published; usage deducted "at the corresponding endpoint price"
("1,000 Credits = $1, equivalent to the API Platform's pay-as-you-go list price"). Legacy Token Plan subscribers keep
their price and text limits (Plus→Go/Explore/Build, Max→Explore/Build, Ultra→Build). Legacy Token Plan figures seen
via third parties: Plus ≈1.7B, Max 5.1B, Ultra 12.5B M3 tokens/month (≈50K tokens per call); IT之家 2026-06-05: Ultra
¥469 ≈7.1B tokens/month, 1,000 credits = ¥7.

User reports for M3.1 Flash (r/MiniMax_AI via RSS; ranges = all uncached as input … as output):
- R1 u/Illustrious-Many-782, 2026-09-28 (1wsdzvg): legacy Token Plan Max ($50→$55), M3.1-Flash-Preview, OpenCode:
  "The five-hour limit with 97% cache hit rate appears to be roughly 300M tokens" → ≈$5.7–9.8 per window.
- R2 u/AwayTeamRedShirt, 2026-10-05/06 (same thread): "lowest tier token plan" (≈$12/month annual): "a touch under 200M
  with 91% cache", then "about 130 mil per five hour window" → ≈$5.4–13.5, then ≈$3.5–8.8 per window.
- R3 u/Money-String4165, 2026-10-16/17 (1x6p4d6): "$50 plan" (legacy Max): "2.5b over 7 days @ 94.3% cache rate",
  "probably 95%ish" of the week → ≈$60–127 per week.
- R4 (weak) u/nnayrdev, 2026-10-09 (1wu9utz): M Plan, tier not stated, dashboard model "M3": "11M tokens at 44% usage of
  WEEKLY limit" (cache excluded) → ≈$3.9–15.5 per week.
Directional only (10-20, after M2.7 traffic moved to M3.1 Flash): No_Monk_4905, Ok_Bug1610, Pleasant_Thing_2874,
NinjaWK report much faster limit hits; Active-Resort3043 (10-01, Explore) "half day and I am 60% usage".
Older / other models: u/mattiasso 2026-06-05 (Plus, M3-512k: one 5-hour window $9.88 discounted, $19.75 list);
sugarw0000kie, vodkavn, Evening_Rip1006, Emiliya_Tyan, purize420, NinjaWK (M2.7), HN ignoramous (estimate from provider
figure), mahonzhan/awesome-coding-plan (CN Plus ¥49, M2.7: 60M tokens per 5 hours ≈ ¥108.60).

Counts: M3.1-Flash(-Preview) on legacy Token Plan 3 (Max ×2, lowest tier ×1), M Plan unnamed tier 1 (weak), named
Go/Explore/Build after GA 0.

## Unreachable
Reddit JSON (403; RSS worked, rate-limited); linux.do, Zhihu (403); web.archive.org (reset); GitHub search (blocked);
X; a CSDN post (404).
