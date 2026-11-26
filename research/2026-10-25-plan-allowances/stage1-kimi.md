# Stage 1 (plain web search), Kimi K3.1 Pro — 2026-10-25

Summary: 7 qualifying K3.1 Pro reports plus 3 partial ones. Only one is on the international USD tiers (Plus $19,
waximabbax); the other six are on China-region legacy CNY plans (Allegretto ¥199, Allegro ¥699), mostly from LINUX DO.
Only fcten states effort (max). Kimi enlarged the quota by about 50% between 2026-10-24 and 2026-10-25 (kojimako:
per-token charge fell to 0.65× of the first-day level), so reports from different days measure different schemas.
Prices used: K3.1 Pro API $2.00 input, $0.20 cached input, $10.00 output per 1M tokens.

Legacy CN plans: users measured week = 5 five-hour windows and month = 5 weeks (fcten's screenshot: 5-hour 100%,
7-day 20.11%, month 4.01%). New plans (Plus and above): a rolling 5-hour window, no weekly limit, and an unpublished
monthly credit pool.

## Qualifying K3.1 Pro reports
1. waximabbax (Ask HN) https://news.ycombinator.com/item?id=50222093, 2026-10-24. Plus $19 (new plan), Kimi Code CLI
   v2.3.1, K3.1 Pro Standard, effort not stated. "Fresh input: 368,203 tokens - Cached input: 1,183,744 tokens - Output:
   39,324 tokens … just $1.37 worth of usage before hitting the 5-hour limit." $1.37 per 5-hour window; no monthly figure
   (pool unpublished). Caveats: author develops a competing agent; one reply suspects a bug.
2. fcten (LINUX DO) https://linux.do/t/topic/3067144, 2026-10-23T18:33Z, follow-up 2026-10-25. Legacy Allegretto ¥199,
   Kimi Code, "K3.1 Pro · max". Test 1 (2026-10-24 00:00–02:26 CST): 1,168,113 uncached / 11,667,200 cached / 172,075
   output; 429 at 5-hour 100%, 7-day 20.11%, month 4.01% → $6.39 per window, ≈$31.8/week, ≥$159/month. Test 2
   (2026-10-25, after the increase): 1,047,419 / 13,183,744 / 148,767 at 64.85% of the window → ≈$9.59/window,
   ≈$240/month.
3. Astralyn (LINUX DO) https://linux.do/t/topic/3071240, 2026-10-25. Legacy Allegretto ¥199, Pi agent, effort not
   stated. Fitted share of the 5-hour window per 1M tokens: input 0.2810, cache read 0.001407, output 2.247 (7-day: 0.0562
   / 0.000281 / 0.449); "7d = 5 × 5h，月 = 5 × 7d". At 97.5% cache hit and uncached input 2.5× output: $11.18/window,
   $55.9/week, ≈$279/month.
4. kojimako (LINUX DO) https://linux.do/t/topic/3070992, 2026-10-24T21:57Z. Legacy Allegro ¥699, direct API calls to
   api.kimi.com/coding/v1 reading used_ratio from /usages (84 calls), effort not stated. Share of the window per 1M
   tokens (input / cache / output): 2026-10-24 0.144 / 0.00075 / 1.156; 2026-10-25 0.0936 / 0.000473 / 0.751; 7-day =
   5 windows. "5h 满额度等效国内站 API 220.4 元，单周 7d … 1,102.0 元". At the same mix in USD: $33.5/window, $167/week
   (first day: $21.7 and $108.6). A reply says full weekly use reaches only 92–95% of the monthly pool.
5. hanashiro (LINUX DO) https://linux.do/t/topic/3067915, 2026-10-24. "199 订阅" (legacy or new not stated): per 5 hours
   243M cached or 2.33M input or 0.29M output ($48.6 / $4.66 / $2.90); updated 2026-10-25 to 180M / 3.6M / 0.45M ($36 /
   $7.20 / $4.50).
6. choulei (LINUX DO, 3071240 #11), 2026-10-25. "实测5h的额度是10美元。全程用3.1pro，价格按照官方定价设置"; dashboard
   "$10.09 / 21.7M" for a full window, weekly 67% remaining at "$16.75 / 41.2M". Plan not stated (has a weekly limit, so
   legacy).
7. raymondchau (LINUX DO) https://linux.do/t/topic/3067175, 2026-10-23T19:13Z. Legacy Allegro ¥699, "kimi k3.1": 156,006
   fresh / 27,711 output / 4,776,704 cached = 12.47% of the window → ≈$12.4/window (low confidence; kojimako's rates
   predict 5.8%).

Partial: ayoka (3071240 #16; $12.20 described as one 5-hour quota, plan not stated), fenglinnet (3071240 #9; legacy
¥199, 43M tokens = 9% of the week, output not given), VincentWang (3067144 #15; legacy ¥199, 2.238M tokens = 11% of
the window, output not given). Anecdotes without numbers: HN 50212065 (johnmlussier $99 plan limit in 47 minutes;
willmorrison $100 plan one max-effort prompt; sail0rm00n $40 plan; 3princip; others).

## Kimi K3 (different model version)
ayakorin (linux.do 2620965, 2026-07-20, ¥199, one full window ≈ $10 at K3 prices); arxiv (same thread, ≈$33.7/window,
basis unclear); kojimako K3 on Allegro (¥284.6/window ≈ $42.7); SwellJoe (HN 49041078, no numbers).

## Provider-published (not user reports)
https://www.kimi.com/en/help/membership/membership-update-rules: new plans have a rolling 5-hour limit and no weekly
limit; legacy plans keep both; one monthly credit pool "deducted based on token usage". USD prices $19 / $39 / $99 /
$199 (annual $15 / $31 / $79 / $159); Max "5×", Ultra "10× Agent credits" (CN page: Ultra 28×). CN prices: Plus ¥99,
Pro ¥199, Max ¥699, Ultra ¥1,399. Model access: K3.1 Pro from Moderato/Plus up; 1M context and Highspeed from
Allegretto/Pro up. No numeric quota is published. Highspeed costs exactly 2× Standard (kojimako).

## Unreachable
LINUX DO search and /raw (Cloudflare); topic 3069671 (two ¥699 subscriptions, old vs new account; 404, likely
login-only); Reddit; GitHub search (GraphQL blocked); the YouTube description; V2EX threads 1231272, 1228735, 1228031
not opened. Queries: Hacker News Algolia (20 queries, 390 hits filtered) and 10 web searches (listed in the agent run).
