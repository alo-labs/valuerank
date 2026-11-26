# Stage 3: third pass through Perplexity (Multi-AI Research), 2026-11-26

**Run through the perplexity skill's driver (`scripts/ask.mjs`, headless Chromium, signed-in session not shown here), Silver Bullet Deep Research unavailable.** The same prompt (`prompt.md`: Part A plan changes since 2026-11-05 with source URL, date and a cut/raise/unclear effect; Part B end-user meter-to-dollar reports in the window; the model-by-plan cells; no estimating) was sent to three models in a fresh thread each, Search mode, Thinking on. The driver's verification line was present and valid for each run:

| Model | Driver line | Output |
|---|---|---|
| Claude Sonnet 5.5 | `verified model: Sonnet 5.5 \| thinking: true \| mode: search` | `out-sonnet55.md` (4,455 chars; "I ran one round of searches and opened none of the pages in full") |
| GPT-6.2 Sol | `verified model: GPT-6.2 Sol \| thinking: true \| mode: search` | `out-sol62.md` (16,021 chars) |
| Kimi K3 | `verified model: Kimi K3 Thinking \| thinking: true \| mode: search` | `out-kimik3.md` (26,328 chars) |

The order followed the skill's standing order for the models available (Sonnet, Sol, Kimi; no GLM or Gemini run, Grok not used). Gemini 4 Carbon, GPT-6.2 Astra, Claude Opus 5.5 and Fable 5.2 are "upgrade items" on this account and were not selectable. Screenshots and session thread links are not kept. Nothing from these answers was taken on trust: each claim used in this record was re-fetched.

## What stage 3 added that stages 1 and 2 had not found

| Item | Found by | Check | Used as |
|---|---|---|---|
| MulletIQ (Merijn), Ultra, Fable 5.2 weekly Fable meter 0% to 8% for $50.28 on 2026-11-14, about $630 a week (range $560-$720); Opus 5.5 week $2,494 from an earlier measurement | Sol | page fetched and archived (`../archive/stage3-found/mulletiq-fable-52-usage-limits.html`) | two report records (`mulletiq-ultra-fable52-wk` eligible; `mulletiq-ultra-opus55-wk-earlier` not) |
| Theo's X post of 2026-11-10 (Ultra, Opus 5.5 $14,662 a month, Fable 5.2 $3,021) | Sonnet (snippet only; it could not open it) and stage 2 | fxtwitter JSON, the chart image and a Bluesky mirror archived | two report records |
| (not found by stage 3) Pawel Huryn's X post of 2026-11-20 (Claude Max Opus 5.5 46.4x, Fable 5.2 27.3x, Google AI Ultra Neon 25.8x) | stage 2, through a Reddit comment that links it | fxtwitter JSON and the chart image archived | three report records |
| Carbon on paid Google AI Pro in Antigravity from 2026-11-23, quota reset, and the 22% caching gain of 2026-11-21 | Sol and Kimi (9to5google, techcityauthority) | both pages fetched and archived | change records |
| Muse Ember "available today on Muse Code and Meta Model API", 2026-11-09 (Meta research blog) | Sol | fetched and archived | change record |
| OpenAI Ultrafast rules for GPT-6.2 on Pro 200 / Pro 500 (help 20001275) | Sol | fetched and archived; agrees with help 9793128 | change record |
| Claude usage credits bought from 2026-12-07 expire after 12 months | Kimi | help article 12429409 fetched and archived; the statement is verbatim | change record (adverse, credits only) |
| MiMo Team Token Plan (2-seat minimum) | Kimi | Xiaomi team doc fetched and archived | change record |
| Wokey tracker (Claude Pro $163, Max $844, Ultra $1,570 a week; Codex Plus $44, Pro 200 $1,095 a week, week 11-16 to 11-23, 5-14 accounts, mixed models) | Kimi | both pages archived | aggregator: cross-check only, not a report |

## Claims in the three answers that did not hold or could not be checked

- Sonnet and Sol said the 2026-11-11 OpenCode Go page could not be found. It is on file (`research/2026-11-11-opencode-go/`), and the diff is in `../opencode-go/README.md`.
- Kimi reconstructed the OpenCode Go diff from third-party captures as "GLM-5.3 reduced from $500/$1,000 to $200/$400 ... apparent cut". The archived 2026-11-11 page has GLM-5.3 at $15 / $120 / $20, so the real change is a rise. Kimi's reconstruction is wrong.
- Kimi quoted MiMo credits of 60M (Lite) to 1.6B (Max) from "the release note"; the archived individual-plan page and the 2026-10-23 record say 4.1B / 11B / 38B / 82B. Not used.
- Sol's quotes of a MiMo FAQ "updated 2026-11-19": the FAQ URL returns the same 9,351-byte JavaScript shell as the platform.xiaomimimo.com page (identical SHA-256), so the text could not be verified. The 0.8x off-peak coefficient is on the archived subscription page.
- Kimi's "Muse Ember added since Nov 3" (onehuman.io) and "Gemini app: Argon hidden for some Pro users" (Google support thread) were not fetched; not used.
- Kimi's list of r/ClaudeCode posts included one (1xy4zwk) it could not open; it is archived here from the mirror.
- Kimi flagged SemiAnalysis (2026-10-05) and perfektcrash (2026-11-03): both already handled (SemiAnalysis is the O40 selected article; perfektcrash is a derived fit).

## Reached and not reached in stage 3

Reached: Perplexity's search over the open web; every page above was then opened directly. Not reached: any page Perplexity could not open itself (it said so for Reddit, GitHub, X and the forums), Wayback, Silver Bullet Deep Research (not available in this environment), Gemini and GLM panel members (not run).
