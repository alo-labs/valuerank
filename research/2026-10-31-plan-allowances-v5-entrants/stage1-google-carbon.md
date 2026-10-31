# Stage 1 (plain web search), Google AI Pro / Ultra plans · Gemini 4 Carbon — 2026-10-31

Summary: no candidate reports and no qualifying reports on any tier. Google announced Gemini 4 Carbon on 2026-10-28
(AA release date 2026-10-28) but has not released it on any consumer or developer surface. Access is limited to "a
subset of cyber defenders" and, later, trusted Fairwind Program partners. Google AI Pro and Ultra subscribers,
Antigravity, the Gemini app and the Gemini API do not offer it as of the 2026-10-31T04:10Z cutoff. A Carbon allowance
reading on a first-party plan is therefore not possible inside the report window. Only three days of the window
(Oct 28–31) postdate the announcement anyway.

Bias note: every Carbon thread found is launch-day discussion (benchmarks, naming, and complaints that the model is
unavailable). The only Carbon-plus-plan text is speculation that its quota will be tighter than Argon's. The sample
contains no measurements, so it leans neither high nor low. Pullpush's Reddit index ends around 2026-10-10, before the
announcement, so Reddit coverage after the release comes from arctic-shift only. GitHub search, LINUX DO and Bluesky
were unreachable. Dollar figures would be the agent's arithmetic at API list prices, but none were computable.

## Prices used (none applied; for later stages)
Gemini 4 Carbon API, Standard, per 1M tokens:
- Introductory: $2.00 input / $0.10 cached (95% off input) / $10.00 output. Source: Google blog "Introducing Gemini 4
  Carbon", https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/,
  2026-10-28: "will launch at the same introductory price as Argon at $2 per million input tokens and $10 per million
  output tokens, with cached input tokens priced at 95% off input token price". The blog gives no end date for the
  introductory period. Argon's ends 2026-11-30.
- After the introductory period: $4.00 / $0.20 / $20.00 (blog footnote). AA lists $4 / $20 with a $0.20 cache-hit price
  (research/2026-10-30-v5-recapture/aa-v5-pages.json; data/price_records.json review note: "AA lists Gemini 4 Carbon at
  USD 4 / 20 … with no introductory rate found").
- Discrepancy for later stages: Google states an introductory $2 / $10 that applies "at launch". Carbon is not yet
  launched to developers, so no rate is in force. AA's $4 / $20 is the post-introductory rate.
- Google's API pricing page (https://ai.google.dev/gemini-api/docs/pricing, fetched 2026-10-31) and API models page do
  not list Carbon. Both list Argon, which confirms they rendered.

## Provider-documented plan inclusion and quotas (context, not reports)
- Google blog (2026-10-28): "Starting this week, we will make Carbon available to a subset of cyber defenders and will
  gradually phase access to additional trusted partners through our Fairwind Program … before making Carbon available
  to developers, businesses, and consumers via our product surfaces as soon as possible". Section heading: "Coming soon
  to developers, businesses, and consumers". The post names no plan (AI Pro, Ultra), no surface (Antigravity, Gemini
  app, CLI) and no quota.
- These pages, fetched 2026-10-31, do not mention Carbon:
  - antigravity.google/docs/models (lists Argon)
  - antigravity.google/docs/plans
  - Gemini Apps limits help page (support.google.com/gemini/answer/16275805)
  - Gemini CLI quota page (redirect only)
- No Carbon quota is documented for any tier.
- Third-party signal, not provider documentation: Th0rgal/orb PR #1428 (2026-10-29) adds `gemini-4-carbon-eap` and an
  Antigravity "Carbon EAP quota" pool (`gemini-eap`: `agy-model*` / `*carbon*`) separate from the regular Gemini and Argon
  pools. This suggests an early-access Antigravity pool exists for allow-listed accounts. The PR gives no plan, no meter
  fraction and no token figures.

## Candidate reports
None. No post found ties Gemini 4 Carbon consumption on Google AI Pro or Ultra to a meter fraction or to window
exhaustion, or even to a token count.

## Near-misses (no data)
1. HN item 50277212 (__jl__, 2026-10-28) and 50277567 (Imustaskforhelp, 2026-10-28) state that "nobody can access it".
2. r/google_antigravity 1xhvwe6, comment 19rsqdti3kzur (gpt872323, 2026-10-28T20:39Z): "Anyone got access to it yet even
   ultra doesn't". This is direct user confirmation that Ultra lacks Carbon.
3. Same thread, 19rskzqiwofpf (One-Satisfaction3318, 2026-10-28): "It costs 7 dollars for an average task in aa testing,
   expect pretty limited usage once it releases". Speculation only.
4. r/google_antigravity 1xj84e4 (Far_Management_7991, 2026-10-30) is about Argon, not Carbon. The author attributes a
   claimed "20x reduction in usage" for Argon to Carbon's "imminent release". Comment 19rw56n1lznxe (mrproiss1) asks
   whether Carbon "would finish the limits easily". Neither has Carbon data.
5. Google AI forum t/196611 (Yuvraj_Negy, 2026-10-29) and t/194996 #3 (Nxrdy_cars, 2026-10-29): Jio-partner AI Pro
   users are excluded from Argon and ask whether Carbon will be excluded too. No usage figures.
6. r/google_antigravity 1xjbc2s ("Argon carbon high is allegedly actually slightly cheaper than 3.8 flash on a cost per
   task basis", 2026-10-30): the post was removed and the title carries no data.
7. Announcement and analysis posts with no usage data:
   - V2EX topic 1252699 (2026-10-28, 0 replies)
   - Qiita: picnic 51e7ca3afa44cdde25a1, bysuAPI 7e7968f61f20e0c06d5d ("API: coming soon"), yoxi957 429f78bf7597d8a5c3cf
   - Zenn: densan_techblog 665380308ade9c, sugawara_ai ai-news-20261029 ("でもまだ使えない理由")
   - Latent Space AINews ("launches for cyber defenders")

Out of scope, noted for the Argon stage: many r/google_antigravity 1xj84e4 comments (2026-10-29/30) report much smaller
Argon meter movement per task. For example, Godge1080p reports ">1 hour, up to 10 agents … 10% of my quota on medium".
Others report no change. This may be an undocumented Argon allowance change around 2026-10-29 and an E18 candidate. It
was not investigated here.

## Queries
WebSearch:
1. "Gemini 4 Carbon" quota Antigravity
2. "Gemini 4 Carbon" pricing AI Pro Ultra limit
3. Gemini 4 Carbon available Antigravity Ultra subscribers rollout
4. "Gemini 4 Carbon" usage limit OR "rate limit" OR "weekly limit" (extended)
5. "Carbon" Fairwind Program Gemini access cyber defenders
6. gemini-4-carbon quota OR limit antigravity OR gemini-cli (github.com only)
7. linux.do Gemini 4 Carbon 额度 OR 用量 OR Antigravity
8. "Gemini 4 Carbon" Antigravity "Ultra" access usage "%" x.com OR bsky.app

Hacker News (hn.algolia.com):
9. search_by_date "Gemini 4 Carbon" (15 hits); items 50276792, 50288019 and 50252509 scanned for quota, limit, access,
   Antigravity, Ultra and AI Pro

Google AI developer forum (discuss.ai.google.dev search.json):
10. "gemini 4 carbon"
11. carbon quota
12. carbon antigravity
13. carbon order:latest
14. carbon #antigravity
15. t/196611.json and t/194996.json read

GitHub:
16. api.github.com search/issues "gemini-4-carbon"
17. api.github.com search/issues "Gemini 4 Carbon"
18. gh search issues ×3 (including carbon in google-gemini/gemini-cli since 2026-10-01)

Reddit:
19. pullpush comments "gemini 4 carbon"
20. pullpush submissions "gemini 4 carbon"
21. pullpush comments carbon in r/google_antigravity after 2026-10-28
22. pullpush comments "carbon limit"
23. pullpush comments "carbon antigravity"
24. arctic-shift comments body "gemini 4 carbon"
25. arctic-shift posts title carbon in r/Bard, r/GoogleGeminiAI, r/google_antigravity
26. arctic-shift posts in r/google_antigravity with query carbon; comments read for 1xhvwe6 and 1xj84e4

LINUX DO:
27. search.json "gemini 4 carbon"
28. search.json carbon 额度

V2EX:
29. API v2 search carbon
30. sov2ex "gemini 4 carbon"

Bluesky (public searchPosts):
31. "gemini 4 carbon"
32. "gemini 4 carbon" quota

Qiita and Zenn:
33. Qiita API "Gemini 4 Carbon"
34. Zenn search "Gemini 4 Carbon"

Official and other pages (WebFetch / curl):
35. Google Carbon blog post
36. Gemini API pricing page
37. Gemini API models page
38. antigravity.google/docs/models
39. antigravity.google/docs/plans
40. Gemini CLI quota page
41. Gemini Apps limits help page
42. Th0rgal/orb PR #1428
43. Qiita bysuAPI article

## Reached / Unreachable
Reached:
- Google blog
- Google AI developer forum (search and topic JSON)
- Hacker News (Algolia)
- Reddit via arctic-shift (posts by subreddit and comments by link_id)
- Reddit via pullpush (reachable, but its index ends around 2026-10-10, before Carbon's release)
- sov2ex (V2EX)
- Qiita API
- Zenn
- ai.google.dev pricing and models pages
- antigravity.google docs
- Gemini Apps help page
- GitHub PR page, through WebFetch
- WebSearch

Unreachable:
- GitHub issue search (API 403: session is repository-bound; GraphQL is blocked)
- LINUX DO (403)
- Bluesky public search (403)
- V2EX API v2 search (404)
- arctic-shift full-text comment search (400: needs subreddit or author) and title searches (422: timeout)
- pullpush query 21 (429)
- X posts were not fetched
- Gemini CLI quota page (redirect stub only)

## O11 assessment
- Google AI Pro: 0 candidates, 0 qualifying. Not met: no pair of reports, and Carbon is not offered on the plan.
- Google AI Ultra: 0 candidates, 0 qualifying. Not met: no pair of reports. A user confirms Ultra lacks access
  (2026-10-28).
- No tier has two independent reports concordant within 20% (largest lower bound ≤ 1.20× smallest upper bound).
  Gemini 4 Carbon has no Google first-party plan allowance evidence inside the 2026-10-01..2026-10-31 window. It cannot
  have any until Google ships Carbon to consumer surfaces.
