# Plan allowance user reports — Google AI Pro / AI Ultra, Gemini 4 Argon (research date 2026-10-25)

Scope: new end-user reports beyond the two already in `stage1-google.md` (A = Muhammed_Alpler t/190608, ≈$8.47/week, High;
B = Faheem_Anis1 t/191879, ≈$12.3/week, Low). Pricing used: Argon API $2.00 input / $0.10 cached / $10.00 output per 1M
(introductory, to 2026-11-30). Sources searched: discuss.ai.google.dev (search.json + /raw), Reddit via the arctic-shift
mirror (r/google_antigravity, r/GeminiAI, r/GoogleGeminiAI; posts and comments since 2026-10-10), Hacker News Algolia
(comments since 2026-10-12), antigravity.google docs, web search (EN/JA). All dates below are 2026 and inside the
preferred window unless labelled.

## More AI Pro Argon measurements (token counts + weekly/5-hour meter %)?

### Takeaway
One new qualifying AI Pro report: u/ansofteng (Reddit, 2026-10-16), Argon Medium, typed token split against "7% weekly",
giving ≈$8.40/week. It agrees with report A (≈$8.47/week, High) to within 1%, so AI Pro now meets the "two independent
reports within 20%" rule at ≈$8.4–8.5/week (≈$36–37/month). Report B (≈$12.3/week, Low) stays ≈46% higher, an outlier.
Many further Pro reports give only percentages.

### Cited Findings
- **NEW qualifying report C.** u/ansofteng, comment in r/GeminiAI thread "Got Gemini 4 Argon in AntiGravity (Paid Pro
  Plan)", 2026-10-16 00:38Z: "1 prompt, 7% weekly usage gone. … EDIT: Token usage for the prompt (you can just ask
  antigravity to calculate this and it will make python scripts): # 1. Gemini 4 Argon (Medium) … Input Tokens: 188,039 /
  Cache Read Tokens: 1,206,506 / Output Tokens: 9,100 / Total: 1,403,645 tokens across 12 turns (86.52% cache hit rate)." —
  [Reddit comment ph0hzk4](https://www.reddit.com/r/GeminiAI/comments/1x6zv2f/comment/ph0hzk4/) (thread by u/faithfull_3,
  [post 1x6zv2f](https://www.reddit.com/r/GeminiAI/comments/1x6zv2f/), 2026-10-15 22:42Z: "Got Gemini 4 Argon in
  AntiGravity (Paid Pro Plan)").
  - Arithmetic: 188,039 × $2 + 1,206,506 × $0.10 + 9,100 × $10 (per 1M) = $0.376 + $0.121 + $0.091 = **$0.588**;
    $0.588 / 0.07 = **≈$8.40/week**. If the meter shows whole percents (6.5–7.5%), the range is ≈$7.84–9.04/week.
  - Caveats: the commenter does not state their own tier (the thread is about paid Pro, and on 2026-10-16 the
    weekly-only Argon meter was the Pro arrangement, so Pro is inferred); the token counts came from a script the agent
    wrote over its own logs, not from a Google meter; one prompt over 12 turns; measured before the 2026-10-17 reset
    that users say made Argon cheaper per request (see question 3); Antigravity surface (app vs CLI) not stated.
- Agreement check with the known reports: C ≈$8.40 vs A ≈$8.47 (High, 2026-10-19), a 0.8% gap → agree within 20%. C vs B
  ≈$12.3 (Low, 2026-10-23): B is 46% higher → no agreement. A and C are independent (different authors, platforms and
  days). — [t/190608](https://discuss.ai.google.dev/t/190608), [t/191879](https://discuss.ai.google.dev/t/191879)
- Percentage-only Pro reports (no tokens, do not qualify):
  - u/Alive-Rough1432, 2026-10-16: "Gemini 4 Argon (High) usage on 20$ pro Weekly usage is 1% per minute … the game took 50
    minute 4 seconds, it drained 54% of the usage" — [Reddit 1x76dms](https://www.reddit.com/r/google_antigravity/comments/1x76dms/)
  - u/Pasto_Shouwa, 2026-10-17: Argon Medium in Antigravity on "Gemini AI Pro" "burnt 66% of its usage to finish the three
    tasks" (19 min); follow-up 2026-10-18: Argon High "burnt 68%, as apparently now the usage of Gemini 4 Argon was
    greatly increased" — [Reddit 1x89weu](https://www.reddit.com/r/GeminiAI/comments/1x89weu/), [comment phfm4i2](https://www.reddit.com/r/GeminiAI/comments/1x89weu/comment/phfm4i2/)
  - u/tamale, 2026-10-18: "two prompts in agy on medium effort and used 70% of my weekly usage in about 10 minutes" —
    [Reddit 1x8tyj9](https://www.reddit.com/r/google_antigravity/comments/1x8tyj9/)
  - u/DasInternaut, 2026-10-18: Argon Medium for design, Flash for implementation: "I have 98.68% weekly Argon usage
    remaining"; also "a couple of projects in OpenCode using a Gemini API key and what I'm seeing, usage wise, roughly
    matches what I see in Agy CLI" — [comment phjf46v](https://www.reddit.com/r/google_antigravity/comments/1x8tyj9/comment/phjf46v/)
  - u/khyzro, 2026-10-17 (Pro): first sprint "around 45 minutes, and my weekly usage went down from 100% to 37%"; after a
    reset, "dropped from 100% to 62% in 58 minutes" — [comment phad785](https://www.reddit.com/r/GeminiAI/comments/1x861k6/comment/phad785/)
  - u/TrickyPlastic, 2026-10-17 ($20): "I used 60% of my weekly quota on two plans" — [comment phaqr0e](https://www.reddit.com/r/google_antigravity/comments/1x7h6gi/comment/phaqr0e/)
  - u/IPerduMyUsername, 2026-10-16: "On medium I got like 3 hrs work out of it for 7% usage"; u/haz3lnut, 2026-10-20 (Pro):
    "only 7% weekly consumed"; u/Swiss_Robear, 2026-10-15: "20% or my Argon weekly usage (on medium)";
    u/ManufacturerHuman937, 2026-10-15: "on low it spent... 1%" — [ph3dlne](https://www.reddit.com/r/google_antigravity/comments/1x76dms/comment/ph3dlne/), [phtdjay](https://www.reddit.com/r/google_antigravity/comments/1x7h6gi/comment/phtdjay/), [ph07eaz](https://www.reddit.com/r/google_antigravity/comments/1x70nez/comment/ph07eaz/), [ph022ri](https://www.reddit.com/r/GeminiAI/comments/1x6zv2f/comment/ph022ri/)
  - u/Kramy, 2026-10-20 (Pro): "burned 14% of my 5hr with one query … Argon 4 High" (~1.5 h of agent work) —
    [comment phv8zbf](https://www.reddit.com/r/google_antigravity/comments/1xamsp4/comment/phv8zbf/)
  - u/Empty-Excuse-1434, 2026-10-15 (student Pro): "my 5 hour usage equated to around 5% weekly usage" —
    [Reddit 1x6f72n](https://www.reddit.com/r/google_antigravity/comments/1x6f72n/)
  - Forum: Trav_Isman, 2026-10-19: "I had 100% rate limit and … within one response the rate limit capped out" —
    [t/190273](https://discuss.ai.google.dev/t/190273); TTCR (paid Pro, agy CLI), 2026-10-20: Gemini group "Weekly 99.73%
    … Five Hour 100%" yet Argon High "Individual quota reached" — [t/190935](https://discuss.ai.google.dev/t/190935)
- Gemini app (not a coding surface; context only): u/Nug__Nug, 2026-10-14 (Pro): one SVG prompt each on Argon High /
  Low / Medium used 19% / 15% / 17% of the 5-hour limit, versus 1% for 3.8 Flash High —
  [Reddit 1x5lh4g](https://www.reddit.com/r/GeminiAI/comments/1x5lh4g/); u/LongLiveSpud, 2026-10-14: "Same prompt, new
  chats: ~5% right after launch (3 tests), 16–23% ~12h later (4 tests)" — [Reddit 1x5lz1u](https://www.reddit.com/r/GeminiAI/comments/1x5lz1u/)

### Inferences
- Treating A and C as the qualifying pair, AI Pro's Argon weekly quota is ≈$8.4–8.5/week at introductory API prices
  (≈$36–37 per 30 days). B (≈$12.3) could reflect a later, looser quota (it was measured 2026-10-23, after the reported
  2026-10-17 reset and on the day of the pool-merge incident), Low thinking, or LiteLLM token accounting; the data do not
  separate these.
- Percentage-only reports are consistent with a small weekly pool: roughly 1% per minute of continuous High agent work,
  and one to three substantial prompts per week.
- Thinking level: across A (High, $8.47), C (Medium, $8.40) and B (Low, $12.3), the dollar quota does not clearly fall with
  higher thinking. If anything Low gives more API-dollars per week. With three points this is weak evidence. The
  Gemini-app test (19/17/15% for High/Medium/Low) suggests per-prompt meter cost varies only modestly by level.

### Gaps
- No second token-level Low or Medium report, so level-dependence cannot be tested properly.
- C's tier is inferred, not stated. The screenshot in u/Myshic's post (weekly Argon maximum differs from other Gemini
  models, [1x70nez](https://www.reddit.com/r/google_antigravity/comments/1x70nez/)) could not be read.
- Reddit comment trees were sampled (≤100 comments per thread). The 349-comment launch thread 1x708ez was only partly
  covered.

## Any AI Ultra Argon measurements?

### Takeaway
None found. Every Ultra report is percentage- or time-only, so Ultra has zero qualifying reports. Users consistently say
Ultra's Argon allowance runs out in about 1–4 days of heavy High use.

### Cited Findings
- u/Ok_Regret72, 2026-10-20, "Argon High draining my 5x Ultra plan": less than a day after the weekly refresh, after
  "around an hour of 7 chats with 6 of those having 3 sub agents each and around 6 more hours of constant heavy work in a
  single chat … EVERY chat and sub agent was on Gemini 4 Argon High" (meter value only in an image) —
  [Reddit 1xamsp4](https://www.reddit.com/r/google_antigravity/comments/1xamsp4/)
- u/prime416, 2026-10-15 ("$200 plan"): "I never hit the five hour breaker, yet I used 50% in two days" —
  [comment pgy5gh1](https://www.reddit.com/r/google_antigravity/comments/1x6qfc3/comment/pgy5gh1/); u/Eduardo1502
  ("200 usd ultra"): "using low or medium because if not my quota would be depleted in 3-4 days" —
  [comment pgxkquu](https://www.reddit.com/r/google_antigravity/comments/1x6qfc3/comment/pgxkquu/); u/samirsss (Ultra
  $200, 2026-10-15): asks Google to "possibly double what the current Weekly allocations are" —
  [Reddit 1x6qfc3](https://www.reddit.com/r/google_antigravity/comments/1x6qfc3/)
- u/AutomateEverything0, 2026-10-16 (Ultra $100): "burning through a weekly in 2 days" —
  [Reddit 1x79g0m](https://www.reddit.com/r/google_antigravity/comments/1x79g0m/); u/Simple-Ad-2981, 2026-10-15 (Ultra
  top tier): "weekly pool is completely drained in two days, Claude is at 0%, Gemini is sitting at 9%" —
  [Reddit 1x6yj04](https://www.reddit.com/r/google_antigravity/comments/1x6yj04/); u/Celestial_Adr23, 2026-10-16:
  Ultra weekly allowance "evaporates in a single afternoon of real work" — [Reddit 1x7h6gi](https://www.reddit.com/r/google_antigravity/comments/1x7h6gi/)
- Jack_Shi, 2026-10-24: "I tried google ai ultra (paid the $100) and cancelled it … I originally thought that google
  would have super high usage limits … that turned out not to be the case (even on introductory pricing)" —
  [t/191975](https://discuss.ai.google.dev/t/191975)
- Hiryu_Arashi, 2026-10-25 (Ultra, AI Studio rather than Antigravity): limit hit "after sending only around ten prompts in
  each session", starting about three days earlier — [t/192066](https://discuss.ai.google.dev/t/192066)
- Secondary and unverified: SmartScope reports the $100 Ultra plan gets five times Pro's quota and $200 gets twenty times,
  and that a burst of work can take the Ultra 5-hour meter to 0% while the weekly meter is above 80%. It says its
  evidence is official documentation plus one user's screen recording —
  [SmartScope](https://smartscope.blog/en/blog/antigravity-argon-five-hour-quota-ultra-2026/). The "5x Ultra" wording in
  1xamsp4 matches the tier naming.

### Inferences
- If the 5×/20× multipliers held for Argon, the Pro anchor of ≈$8.4/week would imply roughly $42/week (Ultra $100) and
  $170/week (Ultra $200). This is an extrapolation from an unverified secondary claim and does not count as a report.

### Gaps
- No Ultra report gives token counts or API dollars against a meter percentage. Ultra users' screenshots, such as the one
  in 1xamsp4, are images that could not be read.

## Did Google change Argon quotas between 2026-10-13 and 2026-10-25?

### Takeaway
Yes, the allocation changed, and users report the effective quota moving. Google staff confirmed only the structural
change: Argon reached paid Pro in Antigravity on about 2026-10-15/16 with a separate weekly-only quota. Users then
reported a weekly reset at the Pro launch, another reset on 2026-10-17 with lighter per-request burn, and a brief merge
of Argon into the general Gemini pool on 2026-10-23 that was reverted within hours. Google's docs say limits follow
available capacity and may change. No numeric changelog entry was found.

### Cited Findings
- Staff (chunduriv), 2026-10-16 02:23Z: "Gemini 4 Argon is now available to paid Pro plan subscribers. As part of Pro,
  we've rolled out a separate weekly-only Argon quota on top of your existing Gemini quota for 3.8 Flash" — [t/188900
  #10](https://discuss.ai.google.dev/t/188900); same text 2026-10-16 00:07Z — [t/189734](https://discuss.ai.google.dev/t/189734).
  At launch (2026-10-13) Argon in Antigravity was Ultra-only — [t/188901](https://discuss.ai.google.dev/t/188901).
- Staff (Ambati_Rajendra), 2026-10-20: "rate limits and quotas are tracked independently per model group rather than
  pooled"; "Gemini 4 Argon: Available in the Antigravity CLI for non-trial Google AI Pro, Google AI Ultra, and Enterprise
  plans" — [t/190935](https://discuss.ai.google.dev/t/190935)
- Antigravity plans doc (fetched 2026-10-25): "The baseline rate limits are primarily determined by available capacity
  … the rate limits correlate with the amount of work done by the agent … Usage limits for this service are subject to
  modification." — [antigravity.google/docs/plans](https://antigravity.google/docs/plans). Models doc: Argon "Not
  available in Antigravity IDE. Available in the Antigravity App, Antigravity CLI, and IDE extensions" —
  [antigravity.google/docs/models](https://antigravity.google/docs/models)
- u/SimpleObvious4048, 2026-10-16: "They added Argon to AG and AG CLI and refreshed the weekly usage as well" —
  [Reddit 1x756ar](https://www.reddit.com/r/google_antigravity/comments/1x756ar/)
- u/Specialist_Data_5403, 2026-10-17: "Today Argon's usage limit in antigravity got reset, and in my opinion it now uses
  far less quota per request. I made 3 requests using Argon low, and it ate about 6% of weekly quota, which yesterday
  would translate to about 10-15%" — [Reddit 1x861k6](https://www.reddit.com/r/GeminiAI/comments/1x861k6/); in the same
  thread u/Pokeasss: "There was a reset. And it reset twice in one hour last evening"; u/TheBuzzer4625kHz: hit the weekly
  limit "8 hours ago … and now I found it back to 100%"; u/khyzro: 63% in 45 min before the reset, 38% in 58 min after.
  Contrary view: u/Pasto_Shouwa (2026-10-18) thought usage had "greatly increased" ([phfm4i2](https://www.reddit.com/r/GeminiAI/comments/1x89weu/comment/phfm4i2/)).
- 2026-10-23 pool merge: u/Proper_Future_146, "Wait, is Argon really counting towards the general quota now on AI Pro??"
  ([Reddit 1xdb1j6](https://www.reddit.com/r/GeminiAI/comments/1xdb1j6/)); u/chr0m: "still had 79% left … now it seems to
  be just mixed in with the normal pool", then 11:59Z "The separate quota randomly reappeared in agy for me";
  u/Specialist_Data_5403: "now they reset and look like before the merge"; u/Matt__2701: "a few hours later, back to how
  it was"; u/Clear-Complaint-322, 2026-10-24: still a separate Argon limit. Same day, an unexpected Claude-pool reset was
  reported ([Reddit 1xdbn4o](https://www.reddit.com/r/google_antigravity/comments/1xdbn4o/)).
- Harness effect: DeSinc, 2026-10-25 (Pro, VS Code extension): follow-ups "instantly burn 3% … (likely the entire chat thus
  far got cache-busted)", with mid-turn drops "upwards of ten whole percent at a time"; "Confirmed this does not happen in
  Antigravity IDE" — [t/192044](https://discuss.ai.google.dev/t/192044). u/Charming_Ad9480, 2026-10-16: Antigravity
  "Cache hit rates are actually disgusting, 86 - 93%" — [comment ph43ncg](https://www.reddit.com/r/google_antigravity/comments/1x7h6gi/comment/ph43ncg/)
- API caching caveat (context): iseixas, 2026-10-13: gemini-4-argon on AI Studio/Vertex returned cachedContentTokenCount
  "0, 0, 0" for an identical 36k prefix; explicit caching returns 400; staff: "We are looking into the implicit caching
  behavior" — [t/189019](https://discuss.ai.google.dev/t/189019). u/DirectionOriginal456, 2026-10-15: "Over 115 million
  tokens I've got 19% cache hits" on the Argon API — [comment pgvvl7r](https://www.reddit.com/r/GeminiAI/comments/1x5yymj/comment/pgvvl7r/)
- No numeric quota change appeared in the Antigravity changelog (the page is client-rendered and returned no content to a
  plain fetch) or in any staff post found.

### Inferences
- Pro's Argon allocation was not stable: two or more resets (≈10-16, 10-17) and a several-hour pool merge (10-23).
  Report C (10-16), A (10-19) and B (10-23) fall in different regimes, which may explain why B is higher. Combined with the
  capacity-dependent wording in the docs, any $/week figure should be labelled time-specific.
- Cache-read pricing in A, B and C assumes cache reads are worth $0.10/1M. Where the harness busts the cache (VS Code
  extension) or caching misbehaves, the meter is charged more per useful token, so the same weekly pool is worth fewer
  API-dollars at nominal rates. A, B and C used Antigravity's own surfaces or LiteLLM, not the VS Code extension.

### Gaps
- No official statement quantifying the 10-17 or 10-23 changes. No @antigravity X posts were retrieved, and Japanese and
  Chinese searches returned only news rewrites (pasqualepillitteri.it, SmartScope) with no user measurements.

## Summary table (tier → qualifying reports, normalised $/week at Argon introductory API prices)

| Tier | Qualifying reports | $/week | ≥2 agree within 20%? |
|---|---|---|---|
| Google AI Pro ($19.99) | A Muhammed_Alpler, 2026-10-19, High, forum t/190608 | ≈$8.47 | **Yes: A and C** (0.8% apart) → ≈$8.4–8.5/week (≈$36–37/30 days) |
| | C u/ansofteng, 2026-10-16, Medium, Reddit ph0hzk4 (tier inferred from thread) | ≈$8.40 (≈$7.8–9.0) | |
| | B Faheem_Anis1, 2026-10-23, Low, forum t/191879 | ≈$12.3 (≈$11.4–13.4) | outlier, +46% vs A/C |
| Google AI Ultra ($100 / $200 variants) | none | — | **No** (0 reports; percentage/time-only anecdotes of a weekly pool lasting ≈1–4 days on High) |
