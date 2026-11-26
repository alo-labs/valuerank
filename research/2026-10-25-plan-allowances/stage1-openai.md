# Stage 1 (plain web search), OpenAI ChatGPT / Codex plans — 2026-10-25

Bias: almost every source is a complaint thread about fast quota drain, so the sample leans low; several reports fall
on days users flagged as accounting anomalies (Sep 8–9, Sep 26, Oct 16–17, Oct 22–24). Dollar figures are the agent's
arithmetic at API list prices.

API list prices (per 1M, input / cached / output; long context >272K in brackets): GPT-6.1 Sol $2 / $0.10 / $10 ($4 /
$0.20 / $15); GPT-6 Sol $2 / $0.20 / $10; GPT-6 Astra $10 / $1 / $50 ($20 / $2 / $75); GPT-6 Luna $0.10 / $0.01 / $0.50;
GPT-5.6 Luna $0.20 / $0.02 / $1.20. Codex credits: 25 per API dollar. Fast mode spends included usage at 2.5×,
Ultrafast at 8×. DevDay (Sep 29): Pro $500 added (≈25× Plus); Pro $200 cut from 20× to 10× for new buyers
(grandfathered 20× through Oct 29, plus a 62,500-credit grant, openai/codex#50931); Pro plans have no 5-hour window.

## GPT-6.1 Sol
1. Plus, medium/low — openai/codex#51604 (mehoney, Oct 6–7, Codex Desktop): 195,644 uncached / 9,692,800 cached /
   21,065 output, 5h +18pp → ≈$8.7/5h; 397,408 / 12,223,616 / 40,050, 5h 0→29% → ≈$8.3/5h; weekly ≈$57 (coarse).
2. Plus, medium — #51088 (Oleg-125, Oct 11): 232,120 / 14,130,560 / 55,692; "5h: fresh → 67%" → ≈$3.6/5h (meter
   direction ambiguous).
3. Pro $200 grandfathered 20×, high/xhigh — #51145 (janrysavy, Oct 3–4, two accounts, Astra 5.6–7.3% of requests):
   ≈$569/week and ≈$323/week.
4. Pro 20× grandfathered — forum 1409401 #953 (sadiqmdasif, Oct 22): "200M Tokens 97% Cached", >30% of week in 1 hour
   → ≈$105–130/week (user calls it anomalous).

## GPT-6 Astra
1. Pro $100, "ultra" — #56669 (YiwenPang, Oct 24): 3,382,725 / 171,903,616 / 726,334, weekly 100%→24% → ≈$318/week.
2. Pro $100, high — #54995 (sentrybottale, Oct 18): parent 108,956,988 / 107,904,640 / 338,002, weekly +41pp →
   ≈$330–400/week.
3. Pro $100, high, Fast — #55348 (mrak-, Oct 19): ≈146.23M total, ≈143.25M cached, 509,659 output, ≈100%→0% →
   ≈$193/week in Fast (≈$480 standard-equivalent).
4. Pro $500, mostly max, Fast — #52530 (totorofly, Oct 11): 35,609,015 / 32,288,000 / 121,060, weekly 0→7% →
   ≈$1,020/week in Fast ($1.5–2.6k standard-equivalent).
5. Pro $200 grandfathered, Fast — #52405 (genellect, Oct 1–9): Astra 57,964,605 / 2,685,801,216 / 7,767,634 plus
   GPT-6.1 Sol; 391% of weekly allowances + 44,814 credits; author priced $3,653.83 + $89.19 → ≈$800 per weekly
   allowance in Fast (≈$2,000 standard-equivalent).
6. Plus, medium — #42987 (kamo-k, Sep 9): 274,007 / 9,438,976 / 62,719, a fresh window to 1% left → ≈$15.5/5h.
7. Plus, high — #55648 (Crystal4276, Oct 20): 2,326,054 tokens, 5h 0→97% → ≈$2.5/5h (anomaly report, split estimated).
8. Pro (tier unknown), max+medium — #42987 (ppgnox, Sep 9): ≈29pp → ≈$1,700/week (before the plan cut).

## GPT-6 Luna
1. Plus, max — #49572 (yoggypap, Sep 30): 30,936,554 / 29,716,224 / 199,431 + guardian; 5h ≈0→8% → ≈$6.5–7.5/5h;
   A/B rerun ≈$5–6.3/5h.
2. Lower bound — HN 50166066 (mekpro, Oct 20): "Luna 6 on 20$ subscription… ~100$ monthly" (limit not hit).
(Not qualifying: #48919, an accounting-anomaly report.)

## GPT-5.6 Luna
1. Plus, max — #42987 (tagorr, Sep 8): 9,538,330 / 8,998,400 / 86,771, 5h 2→10% → ≈$4.9/5h.
2. Plus — HN 49803142 (Shekelphile, Sep 22): "~$150 of luna use per weekly limit" (unverified).
Context: forum 1396093 #21 (alyx, Sep 14) $/1% on mixed Astra/Luna.

## Cross-checks (aggregates, not per target model)
InventiveHQ (Oct 4, mostly GPT-6 Sol): Pro $200 new ≈$640–670/week; Pro $100 ≈$330–380/week; Plus ≈$62/week.
AICodeKing YouTube (Sep 9, model unnamed) ≈$4,900/week on Pro 20×. jrflo HN (Sep 24): $200 ≈ $2,000, $20 ≈ $100.
Thibault Sottiaux (OpenAI, X, Sep 29): new Pro 200 "will net out at half the dollar in API spend".

## Counts (model × tier; brackets = lower bound / unverified)
GPT-6.1 Sol: Plus 2, Pro $200 grandfathered 2 (+1 mixed), others 0. GPT-6 Astra: Plus 2, Pro $100 3, Pro $200
grandfathered 1 (+1 tier unknown), Pro $500 1. GPT-6 Luna: Plus 1 [+1]. GPT-5.6 Luna: Plus 1 [+1]. Business: 0.

## Unreachable
openai.com/api/pricing, chatgpt.com/codex/pricing, help.openai.com (403); Reddit (403); GitHub search API (403;
issue pages via WebFetch worked); YouTube (captcha); X (no results).
