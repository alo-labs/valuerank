# Stage 2 queries and sources (2026-10-31)

## Queries run
### Reddit (arctic-shift API, via curl, paginated)
1. Comment search, body "terra", 2026-10-26 .. 2026-10-31T04:10Z, by subreddit:
   - r/codex (620 comments; stage 1 stopped at 500)
   - r/ChatGPTPro (14)
   - r/OpenAI (93)
   - r/ChatGPT (37)
   - r/OpenaiCodex (43)
   - r/ClaudeCode (18)
   - r/CodexAutomation (0)
   Each result set was filtered by regex for weekly / %, pro tiers, token counts and $ figures.
2. All posts, same window, paginated:
   - r/codex (661)
   - r/ChatGPTPro (108)
   - r/OpenAI (428)
   - r/ChatGPTCoding (100)
   Titles were filtered for usage / limit / allowance / weekly / tokens / doubling.
3. Post search "terra" in r/OpenaiCodex, r/ClaudeCode and r/CodexAutomation.
4. Full comment threads (link_id) read:
   - Plan, meter and Terra-test threads: 1xgcjjb, 1xgriu5, 1xgq393, 1xgpxyf, 1xhl958, 1xjir5f, 1xhhf0z, 1xjgqsp,
     1xjxeew, 1xipj7s (741 comments), 1xj0axr, 1xjtpa4, 1xjjzut, 1xizol3, 1xixihf, 1xjnmmr, 1xjpbos, 1xisode,
     1xgquok
   - Pro-tier and doubling threads: 1xipn3v, 1xiwomg, 1xji2t0, 1xhxrhi, 1xj0hit, 1xjrpxi, 1xjymbe, 1xixah3,
     1xiv3vu
   - Carbon thread: 1xipi3p
5. Author histories since 2026-10-26: pensuke89, IndividualPlus2011, ayudha90, xter418, SlipperyBandicoot,
   facciocosevedogente3, el-rocho (0), dennisvoss1978 (0).
6. Carbon: comment search body "carbon", 2026-10-28 .. cutoff, in r/google_antigravity (30), r/Bard (28),
   r/GoogleGeminiAI (0) and r/GeminiAI (0). Posts 1xipi3p, 1xhufsn and 1xhvg8f fetched by id.
7. Images (i.redd.it): vq41c2lk8zxh1, vbczcoi4b0yh1, wb1ft0765nyh1, 2d8ez71jtlyh1.

### GitHub (WebFetch of github.com HTML)
8. openai/codex #56866, re-read; no comments newer than stage 1.
9. Issue search `is:issue terra created:>=2026-10-28` (16 results).
10. Issue #58477 read.
11. Issue search `terra sol billed OR "shows up as sol" OR headless created:>=2026-10-26` (38 results, nothing
    relevant).
12. Issue search `author:HoYin1600p` (0 results).

### OpenAI community forum (search.json and topic JSON)
13. Searches:
    - `terra after:2026-10-28`
    - `terra weekly`
    - `terra pro after:2026-10-27`
    - `terra usage after:2026-10-27`
    - `terra tokens after:2026-10-26`
    - `usage limit doubled after:2026-10-28`
    - `weekly limit after:2026-10-29`
14. Topics read in full from the post numbers given:
    - 1403525 (#110 on, Days 23–25)
    - 1403897 (#38 on)
    - 1389878 (Codexometer, #84 on)
    - 1409900 (Terra announcement, all)

### Hacker News (Algolia search_by_date, 2026-10-27 .. cutoff)
15. "terra weekly", "terra limit", "terra usage", "terra pro", "terra quota", "terra tokens", "6.1 terra".
16. "gemini 4 carbon", "carbon antigravity", "carbon access" (2026-10-29 .. cutoff).

### Japanese and Chinese sources
17. Qiita API: "Terra 使用量", "Terra Codex", "Terra 週", "Terra Pro", each with created:>2026-10-27. Articles read
    via API: e7eaa2343139211ab790 (Day 23), 57c096af2643066816d3 (Synthorai API comparison, API-only),
    35c21534ec128884360c.
18. Zenn search "Terra Codex".
19. sov2ex (V2EX): "terra 额度", "terra 周限", "terra pro", "terra codex 用量".

### Google AI developer forum (search.json)
20. "carbon after:2026-10-29", "gemini 4 carbon access", "carbon ultra".

### WebSearch
21. "Terra" Codex Pro weekly limit percent tokens API equivalent October 2026 (extended)
22. GPT-6.1 Terra Codex 使用量 週間 リミット 実測 トークン
23. "6.1 Terra" "Pro" usage "weekly" tokens reddit OR github OR x.com
24. "gpt-6.1-terra" rate limit "%" "5h" OR "weekly" usage tokens cached
25. Gemini 4 Carbon available Gemini app Google AI Ultra subscribers rollout (extended)

### WebFetch
26. blog.laozhang.ai Terra vs Sol Codex measurement
27. gemini.google/release-notes
28. antigravity.google/docs/models
29. one.google.com/about/google-ai-plans
30. theaicareerlab.com Carbon availability article

Totals: 30 query groups; about 110 individual queries and fetches.

## Reached
- Reddit via arctic-shift: comment, post and link_id searches, author history and post ids.
- i.redd.it images.
- github.com issue pages and issue search (through WebFetch).
- OpenAI community forum (search.json and topic JSON).
- HN Algolia.
- Qiita API.
- Zenn search API.
- sov2ex.
- Google AI developer forum.
- WebSearch.
- blog.laozhang.ai.
- gemini.google release notes.
- antigravity.google docs.
- one.google.com plans page.
- theaicareerlab.com.

## Unreachable or not attempted
- LINUX DO search.json: 403 (Cloudflare); not pursued.
- Bluesky public searchPosts: 403.
- X / Twitter: not attempted (login wall). Tibo's posts were taken from forum quotes.
- GitHub REST/GraphQL API: not used; stage 1 found it returns 403 in this session. HTML pages through WebFetch
  worked.
- Python urllib to arctic-shift: 403 (missing user agent); curl worked.
- r/codex post 1xjir5f (K_NODE, "studying weekly capacity"): removed by moderators, body unavailable.
- pullpush: not used (its index ends around 2026-10-10, per stage 1).
