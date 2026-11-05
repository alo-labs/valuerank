# Stage 1 (plain web search), OpenAI ChatGPT / Codex plans · GPT-6.1 Terra — 2026-10-31

Bias: GPT-6.1 Terra launched on 2026-10-26, so the usable window is only 2026-10-26..2026-10-31 (cutoff
2026-10-31T04:10:00Z). Almost every source is a launch-week complaint thread ("Terra burns usage faster than Sol"), so
the sample leans low. Nearly all of it is Plus. Two users' clean token-plus-meter measurements dominate the result.
Launch week also had a reset (Day 23), a Pro limit doubling (Day 25), and a user-observed metering shift on Oct 27
(item 4). Dollar figures are the agent's arithmetic at API list prices unless marked "author's".

Prices used (per 1M tokens, ≤272K context): GPT-6.1 Terra **$1.00 input / $0.05 cached input / $5.00 output**, plus
$1.25 cache write. Source: `data/aa/aa_v432_snapshot.json` (AA capture 2026-10-30T22:23:33Z, all five Terra
variants: `price1mInputTokens` 1, `cacheHitPrice` 0.05, `price1mOutputTokens` 5, `releaseDate` 2026-10-26). The
same prices appear in `data/price_records.json` ("launched 2026-10-26 at standard rates"), HN 50249523 (6thbit, Oct
26, quoting OpenAI's table), and Qiita Takuya__ (Oct 28). Codex credits are 25/1.25/125 per 1M (dennisvoss1978,
#56866), which is 25 credits per API dollar. Prices for the comparison models in a mixed report (from the 2026-10-25
file): GPT-6.1 Sol $2 / $0.10 / $10; GPT-6 Luna $0.10 / $0.01 / $0.50.

Plan facts found on this pass (they bear on partitions; not edited into any data file):
- **Day 25, 2026-10-29: Pro limits doubled.** The text is Tibo's X post, quoted in forum topic 1403525 #117 (VeitB):
  "doubling all usage limits for all Pro 100/200/500 tiers and Business Premium, effective today … won't be reducing
  usage limits for Pro 200". This is a provider-documented limit change on every Pro tier. It is not yet in
  `partitionSplits`. Plus is not affected.
- **Day 23: a global reset.** By the day count (Day 7 = Oct 11) it falls on 2026-10-27. Tibo's post is time-stamped
  "2:42 AM - 28 Oct 2026" in the viewer's timezone (1403525 #110). It is not yet in `partitionSplits`. A reading that
  spans it is excluded under O112.
- Codex pricing page, per Qiita Takuya__ (Oct 28): Plus local messages per 5h are 35–285 for Terra and 15–160 for
  Sol. "Pro has no 5-hour limit."
- Plus and Pro have had GPT-6.1 Terra since Oct 26. Free and Go do not have it (openai/codex#58247).

## GPT-6.1 Terra — candidate reports

1. **Plus, effort unstated — pensuke89, r/codex 1xgcwoq** (post Oct 26 23:37 UTC; comments 19rpkdemtj84g Oct 27
   02:03 and 19rq2uvffez8h Oct 27 08:57; "a $20 Plus sub" is stated in the last comment). Method: the author has a
   DeepSeek model sum the session token logs and price them against the % left. Terra was the only model ("terra
   100%", "terra-only").
   - Screenshot a36xb2t05zxh1: total 44,552,133 tokens, of which 43,758,336 cache read (98.2%), 45,459
     output+reasoning, and therefore 748,338 uncached. That used **58% of the 5h window**.
   - Agent's arithmetic: $0.748 + $2.188 + $0.227 = **$3.16**, so **≈$5.45 per 5h**. The author's figures are $3.1937
     and $5.51 per 5h.
   - Earlier readings: Oct 26 at 27% used, $5.28 per 5h (screenshot 9y7q534hdwxh1); "5h, terra-only $5.47"
     (tceyage93xxh1).
   - The author also gives "Weekly, terra-only ceiling $34.33" but does not show how it was derived.
   - Report range: **$5.28–5.51 per 5h**.
   - Qualifies for **Plus 5h**: exact model, author-stated tier, one model, inside the window, Oct 26–27 is not a fault
     day, and the readings predate both the Day 23 reset and the Oct 27 ~10:23 PT shift in item 4.
   - The weekly $34.33 does not qualify, because its weekly-meter basis is not shown. It is listed only as a
     cross-check.
2. **Plus, xhigh — IndividualPlus2011, r/codex 1xhhrxs**, "Allowance table update" (Oct 28 07:44 UTC).
   - Measured on a fresh context on a Plus account, with context capped at 272K. The author's table gives **GPT-6.1
     Terra $5.33 per 5h**, $32 per week, $137 per month, a ratio of 6.85× the $20 price. Sol 6.1 was re-checked as
     unchanged at $7.8 per 5h.
   - The author states the effort (XHigh) for the session described.
   - Raw token readings are not published. The value is the observer's own measurement, not an aggregate.
   - The weekly figure is exactly 6.0× the 5h figure for every model in the table, so it is derived, not separately
     measured.
   - Qualifies for **Plus 5h** at $5.33, a point value. The weekly figure is derived and does not qualify.
   - Independence: on Oct 26 this author said they had "not tested Terra yet" (19rpedjaoy02q). This is a separate
     account and a separate measurement from item 1, though the two authors comment on each other's threads.
3. **Plus (stated in the author's Oct 26 comment; the tier is carried over, so it is provisional), medium —
   el-rocho, openai/codex#56866** (comment of Oct 28).
   - A controlled A/B test on the same task: Terra moved the **5h meter 40→56% (+16pp) for ≈5.14M tokens** (321k
     tokens per 1%). Sol 6.1 moved it 56→71% for ≈3.38M tokens.
   - The cached/uncached/output split is not given. The author says both runs were "heavily cached".
   - $ range (90–99.7% cached, 0.1–2% output): $0.29–1.25 per 16pp, so **≈$1.8–7.8 per 5h**. At item 1's mix it is
     ≈$2.3 per 5h.
   - Does not qualify: the consumption cannot be priced (no split), and the tier is carried over. It sits in the range
     test only as provisional.
   - Note that its tokens-per-1% is 2.4× lower than item 1's.
4. **Plus, xhigh, standard speed — dennisvoss1978, openai/codex#56866** (comment of Oct 27). CLI session files:
   - Before "a ChatGPT update ~10:23 PT", Terra moved the **5h meter 9→19% for 1.91M input tokens** in 5 minutes
     (session 01a17e5d…).
   - After the update, Terra moved it **22→26% for 1.92M input tokens** (01a17e66…).
   - Sol moved it 0→9% for 3.32M tokens.
   - In the desktop app, a 15-minute run used 14% of the 5h window, against 15% for Sol. On launch evening, one Terra
     session drained the whole 5h window in about 70 minutes, with no token count.
   - The cached split and output are not given. Input only, at 90–99.7% cached: before the update ≈$1.0–2.8 per 5h,
     after it ≈$2.5–6.9 per 5h, plus unknown output.
   - Does not qualify: no split and no output count. The author also observes a mid-day metering shift. It is a single
     observation, not provider-documented, and under O99 it splits nothing; it is flagged.
5. **"Pro Plan" (tier unstated), mixed — Emotional-Cut2952, r/codex 1xhx3ab** (Oct 28).
   - **90% of a "5-hour session limit"** in a 35–40 minute task. The orchestrator was Sol 6.1, with 5 Terra and 2
     Luna subagents.
   - Screenshot 5xipeh2f89yh1 gives cached / uncached / output tokens:
     - Terra: 26,100,736 / 617,376 / 105,083, which is $2.45.
     - Sol 6.1: 16,117,888 / 185,533 / 70,412, which is $2.69.
     - Luna (version unstated, at GPT-6 Luna prices): 9,873,408 / 326,061 / 69,845, which is $0.17.
   - Total ≈$5.30, so ≈$5.9 per 5h at plan level.
   - Does not qualify: three models and an unstated tier. In addition, Pro plans reportedly have no 5h window, so the
     plan itself is doubtful.
6. **Plus, high — HoshiEstrellas, openai/codex#57627** (Oct 28). After opening imported sessions, the 5h meter showed
   0% remaining and the weekly meter 80% remaining, while all 55 `token_count` events showed zero tokens. Does not
   qualify: this is an accounting anomaly with no consumption to price.

Meter-only anecdotes. They have no token counts, so they are not priceable and not counted as candidates; they are
context only:
- applejacks6969 (1xgk82f, Oct 27, Plus): one 18-minute turn used 35% of the 5h window.
- ayudha90 (1xgcjjb, Oct 26, Plus): max used 33% of 5h in 18 minutes, plus 6% at high.
- mesolimbic-bliss (1xgup59, Oct 27, Plus, medium): 80% of 5h in about 10 minutes.
- VeryFrickenCool (Oct 27): 67%→30% session in 10 minutes.
- deadcoder0904 (Oct 26, high): 100%→77%.
- Working-Freedom5553 ("100 euro plan", Oct 27, two Terras at medium): 100%→45% in 3 hours.
- ezcax ($100 plan, "ultra", Oct 27): 10% in 30 minutes.
- EclecticAcuity (1xh7nt5, Oct 27, Plus): 20% of the weekly meter, mixed with Sol reviews.
- ALIEN_POOP_DICK (1xjxeew, Oct 31, Pro $200): "entire week's quota"; their ≈$3,125 per 7 days is not
  Terra-specific.

Not Terra 6.1 (excluded):
- veemorfe-netizen #55281: dated Oct 19, before the launch, so the model was GPT-5.6 Terra.
- Blizz606 #56866 body: GPT-5.6 Terra.
- sean-poulter #58154: gpt-5.6-terra.

## Counts (GPT-6.1 Terra × tier; candidates / qualifying)
- Plus 5h: 5 candidates (items 1, 2, 3, 4, 6) / **2 qualifying** (items 1 and 2).
- Plus weekly: 2 candidates (items 1 and 2, each derived or method not shown) / 0 qualifying.
- Pro $100: 0 / 0. Pro $200: 0 / 0. Pro $500: 0 / 0.
- Pro with tier unstated: 1 candidate (item 5, mixed) / 0 qualifying.

## Queries
1. WebSearch "GPT-6.1 Terra" Codex usage limit
2. WebSearch "gpt-6.1-terra" codex weekly limit percent tokens
3. WebSearch "Terra" Codex Plus 5-hour limit API-equivalent dollars measured October 2026
4. WebSearch "6.1 Terra" Pro weekly usage percent tokens Codex
5. HN Algolia search_by_date (comments and stories since 2026-10-01): "GPT-6.1 Terra", "gpt-6.1-terra", "Terra codex",
   "Terra limits", "Terra usage", "Terra plus"
6. GitHub openai/codex issue search (WebFetch): `terra created:>=2026-10-26` (pages 1 and 2), `terra limit
   created:>=2026-10-26`, `terra usage created:>=2026-10-26`, `usage limit created:>=2026-10-26`, `terra
   updated:>=2026-10-26 created:<2026-10-26`
7. GitHub issue pages read: #56866, #56669, #55281, #57627, #58098, #58128, #58154, #58312, #58477
8. OpenAI community search.json: `terra after:2026-10-25`, `terra limit after:2026-10-25`, `"6.1 terra" usage`, `terra
   weekly after:2026-10-25`, `terra codex after:2026-10-25`, `terra pro usage after:2026-10-25`
9. Forum topics read: 1409900 (Terra announcement), 1403525 (28 days of shipping, Days 22–25), 1389878 (Codexometer),
   1409401 (Codex rate-limit thread; no Terra posts after Oct 26)
10. Reddit via arctic-shift: posts and comments with "terra" since 2026-10-26 in r/codex (all 500 comments paged),
    r/ChatGPTPro, r/OpenAI, r/ChatGPT, r/ChatGPTCoding, r/singularity, r/LocalLLaMA. Post IDs fetched: 1xhhrxs,
    1xgcwoq, 1xhx3ab, 1xgk82f, 1xgup59, 1xgcjjb, 1xgq307, 1xhhzme, 1xizol3, 1xjxeew, 1xh7nt5, 1xgsy6j, 1xh02z1.
    Comments of 1xhhrxs and 1xgcwoq. Screenshots from i.redd.it: 9y7q534hdwxh1, tceyage93xxh1, a36xb2t05zxh1,
    5xipeh2f89yh1, 3wkamlyjepyh1.
11. V2EX via sov2ex: "terra codex", "terra 额度"; replies to topic 1252304
12. Qiita API: `Terra created:>2026-10-25`; article 043e006af3ed3ea09b5e (Takuya__) read
13. LINUX DO search.json "terra after:2026-10-25"
14. Bluesky searchPosts "GPT-6.1 Terra" limit
15. smartscope.blog Terra vs Sol Codex test (WebFetch)

Query count: 15 query groups, 52 individual queries and fetches.

Reached: HN Algolia; GitHub issue search and issue pages via WebFetch; OpenAI community forum JSON; arctic-shift
Reddit mirror (a few post searches returned 422 timeouts; the comment searches worked); i.redd.it images; sov2ex and
V2EX API; Qiita API; WebSearch; smartscope.blog.

Unreachable: GitHub REST and GraphQL via gh/curl (403, repository not attached to the session); LINUX DO (403,
Cloudflare challenge, not attempted further); Bluesky public API (403); X (not attempted; no login). OpenAI pricing
and help pages were not needed, since the prices come from the AA snapshot.

## O11 assessment (two independent reports concordant within 20%: largest lower bound ≤ 1.20 × smallest upper bound)
- **Plus, 5h window: met.**
  - Admitting reports: pensuke89 [$5.28, $5.51] and IndividualPlus2011 [$5.33, $5.33].
  - Largest lower bound $5.33 ≤ 1.20 × smallest upper bound $5.33 = $6.40.
  - The provisional item 3 [$1.8, $7.8] and the unpriceable item 4 do not break the range test.
  - Resulting allowance ≈$5.3–5.5 API-$ per 5h. Under O82 a 5h figure does not convert to a billing period.
  - Caveats: both admitting readings fall in launch week (Oct 26–28). Item 2's raw readings are unpublished. Items 3
    and 4 show a meter rate 2–3× faster per token, which hints at metering variance that stage 2 should re-check.
- **Plus, weekly: not met.** No qualifying weekly measurement. The cross-check values $34.33 (pensuke89, method not
  shown) and $32 (IndividualPlus2011, 6× the 5h figure) agree with each other.
- **Pro $100: not met** (0 reports). **Pro $200: not met** (0). **Pro $500: not met** (0).
- Any future Pro measurement must also respect the provider-documented **2026-10-29 Pro limit doubling**. It is a
  partition split for every Pro tier, so readings before and after Oct 29 do not pool.
