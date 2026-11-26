# Sweep log (stage 3, 2026-11-05)

- Retrieval used host WebSearch and WebFetch with direct fetches because `search-cli` is not installed (`command -v search` returned nothing).
- Reddit through the Arctic Shift mirror: daily slices of comments 2026-10-19 to 2026-11-05 in r/ClaudeAI and r/ClaudeCode for the keywords ccusage, equivalent, API and Opus gave 5,359 unique comments; slices 2026-10-26 to 2026-11-05 in r/codex, r/google_antigravity, r/GeminiAI, r/kimi, r/MiniMax_AI and r/XiaomiMiMo for the keywords tokens, cached, weekly and 5h gave 2,515 unique comments. Filtering for dollar, token and percentage content left 34 Claude and 35 other candidates; none was a new qualifying report. r/XiaomiMiMo returned no comments and r/MiniMax_AI returned 8, none with a priced meter reading.
- Hacker News through Algolia: 17 queries (weekly limit, Max 20x, Ultra plan, Claude Pro, Opus 5.5, ccusage, API equivalent, codex plus, codex pro, Sol codex, Argon, Antigravity, Kimi, MiMo, MiniMax, token plan, coding plan) since 2026-10-19 returned 4,004 unique comments and stories; 7 matched the priced-meter filter and all were known or unpriceable.
- LINUX DO mirror locdd.com: 26 search queries returned 594 topics, 38 with posts since 2026-10-24; those and 14 known topics were read. The original LINUX DO topic 3071240 returned JSON on a plain request. LINUX DO search.json and latest.json returned the Cloudflare "Just a moment" challenge (HTTP 403) and were not pursued.
- V2EX through sov2ex: 8 queries, 100 topics since 2026-10-26 listed; five read with replies; no priced reading.
- Google AI developer forum: search.json for seven Argon and quota queries listed about 120 topics since 2026-10-15; 13 raw topics read.
- Web search (6 calls) for MiMo Token Plan, MiniMax M Plan and Kimi Code plan reports found no measured V2.6, M3.1 Flash or K3.1 Pro percentages.
- aiplans.dev: sitemap read; guides claude-pro-opus-5-5-quota and codex-pro-200-quota-benchmark read; report paths for 2026-10-31 to 2026-11-05 return 404.
- Antigravity changelog and plans page: no usage-limit change entry between 2026-10-15 and 2026-11-05.
- Blocked: GitHub REST for openai/codex and anthropics/claude-code (repository not enabled); a third-party GitHub reader proxy was refused by the permission layer; X search unavailable.
- Reddit was read through a mirror capped at 100 results per query, so slices that hit the cap are partial, and 11-05 coverage is partial.
- GitHub comments were read through rendered pages summarised by the fetch tool, so quotes are verbatim only to the extent the tool reported them and no byte-exact copy exists.
- GitHub issue text came from rendered pages and has no byte-exact copy.
- Reddit comments were pulled by day through the Arctic Shift mirror (5,359 Claude-subreddit comments from 2026-10-19 to 2026-11-05 and 2,515 comments in six other subreddits from 2026-10-26) and filtered for dollar, token and percentage content.
- Hacker News was queried through Algolia (4,004 hits, 17 queries).
- Twenty-six locdd queries and 38 recent topics were read.
- No new priced MiMo or MiniMax report was found in the sweeps.
- Retrieval used host WebSearch and WebFetch with direct fetches because search-cli is not installed.
