# Stage 2: deeper, differently phrased multi-source pass (2026-11-26)

## How it was run

- The `anthropic-skills:deep-research` skill was loaded through the Skill tool. Its procedure spawns researcher and report-writer subagents with an Agent tool; this session (itself a subagent) has no Agent tool, so no researcher or writer could be started. Stage 2 was therefore run as one researcher following the skill's `researcher.md` instructions (short queries, fetch the full page behind every snippet, three-section notes with a source on every claim, gaps stated). This is the same degraded mode the 2026-10-31 record used ("no helper agents could be started"). The skill's report writer was not run; the synthesis is the top-level `README.md`.
- Where stage 1 was the plain search tool and provider pages, stage 2 swept the places end users post meter readings, by machine, with different phrasing: dollar and percentage patterns in whole subreddits rather than keyword searches. The scripts are in `tools/` (stdlib Python plus curl).

## Sweeps and counts (window 2026-10-30 to 2026-11-27 unless noted)

| Source | How | What was read | Outcome |
|---|---|---|---|
| Reddit posts, via Arctic Shift | `tools/as_dump.py`, every post of a subreddit, ascending, 100 per page | r/ClaudeCode 5,302; r/ClaudeAI 9,531; r/codex 2,399; r/ChatGPTPro 518; r/OpenAI 2,203; r/ChatGPTCoding 546; r/ChatGPT 4,859; r/google_antigravity 1,546; r/AntigravityGoogle 367; r/GeminiAI 3,981; r/Bard 312; r/Anthropic 1,175; r/claude 3,033; r/MetaAI 3,176; r/MuseCode 48 (2026-10-02 on); r/XiaomiMiMo 0 and r/muse_ai 0 (empty) = 38,996 posts | `tools/rd_scan.py` kept posts with a dollar figure, a percentage, a window word, a model and a plan word (about 20-30 per large subreddit); each read by hand. New reports: sunaurus, MRC2021, AnshulJ999, hhspiny, WuM1ha1nho, gianfrugo, IndividualPlus2011, ubelai, mcD0m (plus seen-and-not-counted ones, below) |
| Reddit comments, via Arctic Shift body search | `tools/as_cbody_days.py` | r/codex 896 comments (8 terms, 10-30 to 11-27); r/ClaudeCode 991 (4 terms, one-day windows 11-01 to 11-27); r/google_antigravity 1,796 and r/AntigravityGoogle 236 (terms Neon, Carbon, weekly, 5h; 11-10 to 11-27) | `tools/c_scan.py` candidates read; found the IndividualPlus2011 follow-ups, the perfektcrash and Noob_Kid replies, the 2026-11-23 Google quota-reset thread. r/ClaudeAI comments were started and stopped (the mirror rate-limited), r/ChatGPTPro comments not run |
| Reddit threads read in full | `comments/tree` for each report thread | 11 comment trees archived (`../archive/reddit/*.comments.json`) | quoted in `reports.json` |
| Hacker News, Algolia | `tools/hn_harvest.py`, 12 queries x comments and stories since 2026-10-30 | 1,695 unique items | 7 matched the dollar/percent/plan filter; none was a priced meter reading (mceachen, PaulStatezny and pseudosavant read: no meter fraction) |
| Bluesky search API | `tools/bsky.py`, 8 queries (one failed with HTTP error) | 341 posts | 11 with a dollar and a percentage: price announcements and a mirror of Theo's tweet; Theo's X post found this way |
| X, via fxtwitter | status ids found in a Reddit comment, a web article and a Reddit post | 2 posts (theo 2119960608816988596, PawelHuryn 2123650574373605874) with their images | both archived; X search itself unavailable |
| Google AI developer forum (Discourse JSON) | `tools/disc_harvest.py`, 27 search queries, then 8 more | about 700 topic ids collected; the topic-JSON fetches were mostly refused by the forum's rate limit ("You've performed this action too many times", 437 of 442 files in the first folder, all of the second), so the full-text scan found nothing it could be trusted for; a gentler blurb-level search (`tools/disc_blurbs.py`, 5 queries, 63 posts) found no dollar-priced quota reading | the forum threads that mattered were fetched singly: 196351 (Yiji_Kong, M_B4), 202301 (Neon), 205526, 205405, 198430; **the forum was not swept to completion** |
| OpenAI developer community (Discourse) | same | 16 queries, 51 topic ids (all fetches rate-limited); blurb search 5 queries, 36 posts, none priced; the tail of the "Codex Rate Limit Discussion Thread" (1409401, 1,048 posts) read for 300 posts, 2026-09-13 to 2026-11-25: two dollar mentions, none a meter reading | no report |
| LINUX DO, via the locdd.com mirror | `tools/disc_harvest.py`, 20 queries (99 topic ids, topic fetches mostly refused) and `tools/disc_blurbs.py` 5 queries (23 posts) | one priced item: StarOcean (topic 108781, Pro, Fable 5.2, "10-odd dollars" of cache writes took over half the five-hour limit): vague, not counted |
| aiplans.dev, Atlas ADE | sitemap, report and guide pages | the x2v report (1,148 bytes, hash identical to the 2026-11-05 copy); Atlas ADE's usage-burn page (Ultra, derived fit: "a full Ultra week is worth roughly $1,200 to $3,700 of Opus 5.5") | x2v recorded; Atlas not counted (derived) |
| Short WebSearch queries | 4 more, phrased differently from stage 1 | Theo/Huryn/Antigravity-reset follow-ups | see `../stage1/queries-websearch.md` queries 31-37 |

## Notes in the skill's format (the questions that drove the sweep)

### Which end-user reports of API-priced plan usage exist for 2026-10-02 to 2026-11-26 beyond those on file?

Takeaway: fifteen observers with byte-exact archives (three of them, Theo, IndividualPlus2011 and Yiji_Kong, were already on file with earlier reports), plus four queued GitHub reports that cannot be archived byte-exactly. The Claude Ultra Opus 5.5 week now has three direct readings at $2.1-2.8k; Fable 5.2, Sonnet 5.5, Haiku 5.5, GPT-6.2 Sol, Gemini 4 Neon and Gemini 4 Carbon each have a first reading; no GPT-6.2 Astra, GPT-6.1 Terra, GPT-6 Luna, Pro 100/200/500, Muse Ember or MiMo-V2.6-Flash reading exists.

Cited findings: see `../reports.json` (34 records) and the cell table in `../README.md`.

Inferences: Yiji_Kong's 3.00x for Carbon implies the same dollar bucket as his Argon figure on Ultra 5x (recorded as inferred, not counted). The Ultra 20x pool in published-price dollars (ubelai: about $204-212 per five hours and $816 per week for Carbon Low at the $2/$10 price) is four times the Ultra 5x Argon reading ($49.2-$50.0 per five hours; $199.9-$200.1 per week), as the 5x/20x tiers imply.

Gaps: GitHub issue pages (unreachable), the Google and OpenAI forums (rate-limited, partial), r/ClaudeAI comments, X search, V2EX, Zhihu.

### Did any registered-type change happen after 2026-11-05?

Takeaway: yes, 21 change records in `../changes.json` (13 benign, 6 unclear, 2 adverse). The adverse ones are an announced credit-expiry rule (purchased usage credits only) and one observer's measured 17% cut to GPT-6.2 Sol's Plus allowance. The December shared ChatGPT/Codex allowance is still announced, not in force.

Gaps: provider statements for the two user-detected limit changes (OpenAI Sol 6.2 on Plus; Google AI Pro weekly pool $105 to $120) were not found.
