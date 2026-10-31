# Stage 1 (plain web search), Anthropic Claude plans — 2026-10-25

Counts of qualifying reports (model × tier): Opus 5.5 Pro 4 (+1 outlier), Max 5x 2 (weak), Max 20x 6 (+2 partial);
Sonnet 5.5 and Haiku 5.5: 0 on every tier (meter percentages without dollars, or Opus-pool extrapolations by price
ratio, which is ValueRank's existing assumption). Independent Max 20x reports land at about $2.0k–2.6k per week
(≈$8.9k–11.2k per month), close to SemiAnalysis's $11,726/month (≈$2.7k/week).

Prices used by reporters (per 1M: input / output / cache read / 5-min write / 1-h write): Opus 5.5 $4 / $20 / $0.20 /
$5 / $8; Sonnet 5.5 $2 / $10, cache read $0.20 (cut to $0.10 about 2026-10-08); Haiku 5.5 $0.10 / $0.50 / $0.01
(≤100K-token prompts).

Main source: GitHub Fei2411/real-api-pricing community "[Data]" issues (Claude Code transcripts deduplicated by
message.id against the official seven_day / five_hour meters).

## Opus 5.5 — Pro ($20)
1. Issue #52 (NTRYourWaifu), 2026-09-22..27, two accounts, /api/oauth/usage polled every 5 min: 1,396.81M tokens
   (cache read 1,366.51M, 1-h write 20.81M, 5-min write 2.78M, output 6.69M) = +183 weekly points; $587.52 → $3.21 per
   point ≈ $321/week; high and xhigh efforts both ≈ $3.2/point.
2. X @kanzakichiya (≈2026-09-30, ccusage screenshot): Opus 5.5 Medium; $92.14 + $116.11 = $208.25 for 22% + 47% → ≈$302/week
   (ccusage weeks not aligned with resets).
3. Reddit u/hakanavgin, 2026-10-07: "$236 … = 83% of the weekly limit … cap ~$285 … $170 = 65% … ~$261 … ~$270/week,
   roughly $1,150/month" (mostly Opus 5.5, effort not stated).
4. Reddit r/ClaudeCode (≈2026-09-24; URL not recovered): one 5-hour window = 151,193,723 tokens = 13.333% of the week →
   ≈$40.48/window, ≈$304/week (weak: token split estimated in comments).
5. Outlier: issue #124 (ganpei777), 2026-10-09..13, 0% → 100% of the week, Opus 5.5 99.99%, 4,072.2M tokens (cache read
   4,029.7M) → $1,266.15, $12.66/point (≈4× the others; cause unknown).

## Opus 5.5 — Max 5x ($100)
1. Issue #98 (muscgab), 2026-10-03, controlled headless run, Opus 5.5 medium, cache off: window 68% → 95%, "1% ≈ $0.68";
   weekly $7.54–9.76/point → "$750–830 per week (no cache)"; with a 97% cache-read workload ≈ $1,040–1,150/week
   (back-solved cache weight).
2. Community /usage screenshot, week of 2026-09-29 (origin unlabelled): $366.96 = 19% of the week → ≈$1,920/week
   (possibly a lower bound).

## Opus 5.5 — Max 20x ($200)
1. Issue #96 (Kanttz), 2026-10-02, 2,941 statusline samples: week A 0% → 94% = $2,423.48 (5-min writes) / $2,745.03
   (1-h) → ≈$2,578/week; week B 0% → 39% = $968.60 → ≈$2,484/week; 36-window fit $662 (5-min) / $754 (1-h) per window.
2. Theo / pingdotgg ts-rust README, 2026-10-08: "~$24,047 of API spend over 2 weeks … between 925% and 983% of my $200
   plan weekly limits" → $2,446–2,600 per weekly limit.
3. Reddit u/Last_Lab_3627, 2026-09-27 (Tokscale): "$450 … 22% of my weekly limit … roughly $2k".
4. Reddit u/Delicious-Shower8401, 2026-09-26: "one full weekly limit on Max 20x. The $2,175 is the API-equivalent".
5. Reddit u/leaflavaplanetmoss, 2026-10-09: "~70% of the 20x Max weekly usage … ~$800 at API list prices" → ≈$1,140/week
   (low outlier; Max effort).
6. X @MiaAI_lab (≈2026-09-23): xHigh, $482.63 = "~75% of my 5h limit" → ≈$630–645/window (tier inferred).
Partial: issue #65 (mixed models, ≈$1,410/week), u/Fun-Freedom-2313 (≈$2,725 in a week, no meter).
Aggregate (reseller, commercial interest): wokey.ai week 10-12..19 — Max 20x $1,643/week (17 accounts), Pro $170/week
(474 accounts).

## Sonnet 5.5 and Haiku 5.5
Sonnet 5.5: meter percentages only (u/uzih, u/oxmannnn, u/mikemarcin, u/mohaziz999, u/S1d519, u/Mysterious_Self_3606,
u/AntixMars, u/BoredErica); issue #96 week B has Sonnet 5.5 medium as 22% of a mixed week, and the meter tracked list
price across models (R² 0.935 price-weighted vs 0.80 raw tokens). Haiku 5.5: issue #124 (9 calls), AI Dive dev.to (140
tasks, $0.54, meter unmoved, tier unstated), u/No_Complex4623 (percent only).

## Caveats
Cache-read weighting is disputed (31–65% of list back-solved by some reporters; list price fits best for Kanttz); 1-h vs
5-min write pricing moves totals ≈12%; A/B tests (one account in three ≈20% lower limits); effort changes burn rate,
not dollars per point (#52).

## Unreachable
GitHub search APIs (403); github.com via curl (403; WebFetch worked); reddit.com (403; pullpush mirror used, index ends
≈2026-10-13); X posts (only repo transcriptions); SemiAnalysis beyond the methodology (paywall).
