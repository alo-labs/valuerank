# Decision record (AF-DECIDE rollup): plan-allowance reports, stage 3, 2026-11-05

Workflow WF-SILVER-DEEP-RESEARCH, mode deep, research_type default. Output directory `/home/user/valuerank/research/2026-11-05-plan-allowances/stage3-sb-deep-research`. Full argument in `research_report.md`; evidence in `sources.jsonl`, `evidence.jsonl`, `claims.jsonl`; raw copies hashed in `raw/MANIFEST.sha256`.

## Decision

1. **At the 2026-11-01T06:10Z cutoff, no provider x plan x window cell passes O11.** Stage 3 adds no second non-provisional, concordant report to any cell and reaches the same verdict as stage 2. Stage 3 changes the evidence base in three ways: one dollar correction, two observer-identity corrections, and one refuted change claim.
2. **Corrections to the existing record (apply):**
   - Oleg-125 (openai/codex #51088): upper bound $7.4 is wrong; the comment says 67% of the 5h allowance was **consumed**, so the range is about **$3.58 to $3.69** per 5-hour window.
   - moondrinker-allegretto and astralyn-allegretto are one observer and one thread (locdd 103607 mirrors LINUX DO 3071240; the "DolphinLover" coefficient thread is the same topic).
   - Faheem_Anis1 (Google forum t/191879) and Ultimitehand (r/google_antigravity 1xdghgq) report identical data: one Google AI Pro observation, not two.
   - Stage 2 described xu62u4u6 (#51088, 10-28) as "model and plan not given"; the comment states ChatGPT Plus and names gpt-6-astra and gpt-5.6-sol. It stays excluded as mixed-model.
3. **Do not record a Kimi 5-hour partition split** on the claim that the legacy window doubled around 10-27 to 10-29: the primary coefficient record is unchanged through 11-03 (legacy Allegretto only).
4. **Open as candidates, not decisions:** a Google AI Pro/Ultra change near 2026-10-21 to 2026-10-22 (third-party blog only; Google's page shows none), and an OpenAI Pro allowance shrink around 2026-11-04 to 2026-11-05 (user tallies only). Both belong in the O167 freshness check.
5. **Queue for the next release (after cutoff, not counted now):** douflou (Max 5x, interactive and SDK), ricardoraposo (Ultra weekly), x2v (Pro, headless), plus Pro, Max and Ultra readings dated 11-02 to 11-04.

## Provider x plan x window table

Model is Opus 5.5 for Anthropic rows unless stated. "Cutoff" is 2026-11-01T06:10Z; rows after it are labelled and never count for the November release. Dollar ranges are my arithmetic at stage-1 list prices with +-0.5 point meter rounding, unless the reporter's own figure is stated. Qualifies: yes, provisional, or no.

| Provider x plan x window | Report URL | Date | $ range | Qualifies | Correction to existing record |
|---|---|---|---|---|---|
| Anthropic Max 20x week | https://x.com/jbdamask/status/2115515191039545712 | posted 2026-10-28 (week about 10-19..10-27) | $2,277-2,341 ($831 at 36%) | yes | none; text and table image re-read; entrypoint unstated |
| Anthropic Max 5x week | https://github.com/anthropics/claude-code/issues/106322 | 2026-10-28 22:00Z to about 10-31 | $1,360-1,495 (researcher-priced, input missing, slight undercount) | yes | none; Nov 1 98% comment has no tokens |
| Anthropic Max 20x week (model unstated) | https://news.ycombinator.com/item?id=50289476 | 2026-10-29 | about $2,000 (reporter) | no (model unstated) | none |
| Anthropic Max 20x 5h (model unstated) | https://news.ycombinator.com/item?id=50289476 | 2026-10-29 | about $520 | no | none |
| Anthropic Ultra week | https://github.com/anthropics/claude-code/issues/106274 | reset 2026-10-31 02:00Z, comment 11-01 | $797-819 ($307 at 38%) | provisional (98% Opus, P4) | reset is 02:00Z, not 01:00Z (confirms stage 2) |
| Anthropic Ultra week (after cutoff) | https://github.com/anthropics/claude-code/issues/97074 | 2026-11-03 | $1,560-3,087 (interactive uncached $2,060); `sdk-ts` 1.14-1.32x faster | provisional (controlled, low effort) | none |
| Anthropic Max (5x) 5h (after cutoff) | https://github.com/anthropics/claude-code/issues/106375 | 2026-11-02/03 | about $204 interactive; about $104 via SDK | provisional (tier by rename inference) | none |
| Anthropic Max (5x) week (after cutoff) | https://github.com/anthropics/claude-code/issues/106375 | 2026-11-02/03 | about $1,333 ($1,143-1,600) | provisional | none |
| Anthropic Pro 5h (after cutoff) | https://aiplans.dev/reports/claude-pro-opus55-2026-11-04.md ; https://claude.ai/artifact/DcK5UbxR1SmkgDn38QtBo2 | 2026-11-04 | $25.0-33.3 at list (author: $26-29 output-heavy, $44 mix) | provisional (headless `claude -p`, one account, synthetic) | new: not in stage 1 or 2 |
| Anthropic Pro week (after cutoff) | same | 2026-11-04 | $229-458 (author $185-320) | provisional (3 meter points) | new |
| Anthropic Pro 5h | https://github.com/anthropics/claude-code/issues/101937 (sergiokapone) | 2026-10-27 | $14.1-17.7 (reporter $13-14) | provisional (plus 22 Haiku 4.5 requests, 1 Sonnet 5.5 request) | proposal: stage 2 had "no"; not counted toward an Opus-only cell |
| Anthropic Pro 5h (after cutoff) | https://github.com/anthropics/claude-code/issues/105621 (smaug42) | 2026-11-02 | $194-206 | provisional (anomalous, about 6x other Pro) | none |
| Anthropic Pro week (after cutoff) | https://github.com/anthropics/claude-code/issues/105621 (smaug42) | 2026-11-02 | $914-1,280 | provisional (anomalous) | none |
| Anthropic Pro (tier placeholder) 5h | https://github.com/anthropics/claude-code/issues/101937 (leolim031) | 2026-10-14 | $41-48 and $57-64 | no (plan stated as "[PLAN]") | new: missed by stages 1 and 2 |
| Anthropic "Max" 5h | https://github.com/anthropics/claude-code/issues/105621 (JCorners68) | 2026-10-30 | about $18-23 | no (tier ambiguous, single request) | none |
| Anthropic Sonnet 5.5, Haiku 5.5 x all plans | none found | | | no (0 reports) | none (agrees with stages 1 and 2) |
| OpenAI Plus x GPT-6.1 Sol 5h | https://github.com/openai/codex/issues/55210 (jitendersingh0411) | readings 2026-10-25 and 10-31 | $2.78-7.84 (points $7.5 and $2.9) | yes (soft: two readings 2.6x apart; 7-minute vs 30-minute narrative unreconciled) | none |
| OpenAI Plus x GPT-6.1 Sol 5h | https://github.com/openai/codex/issues/51088 (Oleg-125) | 2026-10-11 (split day, no clock time) | **$3.58-3.69** | yes (model named in comment header) | **recorded $3.6-7.4 corrected to $3.58-3.69** |
| OpenAI Plus x mixed Astra and Sol 5h | https://github.com/openai/codex/issues/51088 (xu62u4u6) | 2026-10-28 | not priceable (about 9.56M tokens, 0% to 99%) | no (mixed models, no split) | stage 2 said plan and model unstated; plan is Plus, two models named |
| OpenAI Plus x GPT-6.1 Terra 5h | https://www.reddit.com/r/codex/comments/1xgcwoq/limits_decreased_when_using_61_terra/ (pensuke89) | 2026-10-27 | $5.50 per 5h; $34.33 per week | yes (already recorded) | none; 10-27 is a reset day (O112 check) |
| OpenAI Pro 200 x GPT-6 Astra week | https://aiplans.dev/reports/codex-models-2026-10-28.json | 2026-10-28 | $592-1,184 (point $789) | provisional (20x vs 10x unstated) | none; recomputed from JSON ledger |
| OpenAI Pro 200 x GPT-6 Astra week | https://aiplans.dev/reports/codex-models-2026-10-30.json | 2026-10-30 | $978-1,630 (point $1,222) | provisional (same account, upgrade owner-reported) | none; ratio 1.55 does not confirm or refute the doubling |
| OpenAI Pro 200 x GPT-6.1 Sol week | https://aiplans.dev/reports/codex-models-2026-10-30.json | 2026-10-30 | at least $481 | no (lower bound only) | none |
| OpenAI Pro 100, Pro 500 x any | https://github.com/openai/codex/issues/59194 and related issues | 2026-11-02..11-04 | no tokens (8% weekly in 2h on Astra) | no | none |
| OpenAI Business/Team 1x Codex 5h and 7d | https://www.locdd.com/t/topic/104275 (quote of a LINUX DO post) | 2026-10-25..26 test, quoted 10-27 | not priceable | no (original not located) | new lead |
| OpenAI Pro 100/200 week, post-reset tallies | https://www.locdd.com/t/topic/106945 | 2026-11-05 | about $1,200 (Pro 200), about $640 (Pro 100), $1,100 Sol vs $600 Astra | no (no token split; after cutoff) | change signal for O167 |
| Google AI Ultra 5x 5h (Argon, Antigravity) | https://discuss.ai.google.dev/t/196351 | 2026-10-28 | $49.2-50.0 at $2/$10/$0.10 | yes | none; at the $4/$20 post-introductory price double it |
| Google AI Ultra 5x week (Argon, Antigravity) | https://www.reddit.com/r/google_antigravity/comments/1xfnvds/ | 2026-10-26 | $199.9-200.1 | yes | confirms stage 2: tier stated, not provisional; his $150/5h is derived and does not count |
| Google AI Ultra 5x week (Gemini web app meter) | https://discuss.ai.google.dev/t/196351 (post 5) | 2026-10-29 | $29.7-36.0 | provisional (weak; tokens estimated from characters) | none |
| Google AI Pro week (Argon) | https://discuss.ai.google.dev/t/190608 | 2026-10-19 | $8.47 | yes | pre-change side of the candidate 10-21/22 split |
| Google AI Pro week (Argon) | https://discuss.ai.google.dev/t/191879 and https://www.reddit.com/r/google_antigravity/comments/1xdghgq/ | Reddit 2026-10-23, forum copy stamped 10-26 | $11.4-13.4 ($12 reported) | yes (one observation) | **Faheem_Anis1 and Ultimitehand are one report** |
| Google AI Ultra (tier unstated) 5h | https://www.reddit.com/r/GeminiAI/comments/1xig0er/usage_limits/ | 2026-10-29 | about $273 (450M tokens at 96% cache, 29% used) | no (tier and split unstated) | none |
| Google AI Ultra headless vs interactive | https://discuss.ai.google.dev/t/198073 | 2026-11-04 | no dollars; 307 vs 418 ppm; cold 1,294 ppm | no | entrypoint caveat extends to Google |
| Kimi Allegretto (legacy 199 CNY, CN) 5h | https://www.locdd.com/t/topic/103915 (SunnyDoll) | 2026-10-26 | $9.0-20.8 | yes (locdd identity caveat) | none |
| Kimi Allegretto 5h | https://www.locdd.com/t/topic/103915 (PaperPlane) | 2026-10-26 | $22.7-34.7 | provisional (approximate) | none |
| Kimi Allegretto 5h | https://www.locdd.com/t/topic/104985 (SunnyDoll/KiteRunner) | 2026-10-29 | $32.2-41.8 | provisional (tier inferred from a separate post) | confirms stage 2 |
| Kimi Allegretto 5h (derived) | https://linux.do/t/topic/3071240 (Astralyn) | updated 2026-11-03 | about $15.0 at a 2.5/0.5/97 mix (51.0M tokens) | no (derived) | coefficients unchanged 10-25 to 11-03: **no 5h doubling** |
| Kimi Allegretto week | https://www.locdd.com/t/topic/104222 (TimeMachine) | 2026-10-27 | $62-261 | provisional (week may span the 10-26 reset) | none |
| Kimi Allegro (legacy 699 CNY) week | https://www.locdd.com/t/topic/103774 | 2026-10-25 | $185-191 | provisional (spans the 10-24 split) | none |
| Kimi new Max (699 CNY) 5h and month | https://www.locdd.com/t/topic/106583 | 2026-11-04 | estimates only | no (derived, after cutoff) | none |
| Kimi Plus (USD) 5h and month | https://www.reddit.com/r/kimi/comments/1xl4r76/guys_wanna_hear_a_joke/ | 2026-11-01/02 | $0.22-1.62 per 5h; $1.7-13.0 per month (reporter $12.42) | no (after cutoff, lower bound) | none |
| Kimi moondrinker-allegretto and astralyn-allegretto | https://www.locdd.com/t/topic/103607 ; https://linux.do/t/topic/3071240 | 2026-10-25 | derived $48.6-55.9 per week | no (derived) | **one observer, one thread** |
| Xiaomi MiMo Token Plan x all tiers | none new (Reddit, locdd, V2EX, web search) | | | no | none; O46 ceilings remain |
| MiniMax M Plan and legacy Token Plan x all tiers | none new | | | no | none |

## Alternatives considered

- Treat after-cutoff Claude reports as admitted for the November release: rejected; the cutoff rule and the instability of the post-10-30 meter (Ultra weekly spans $667 to $3,087) argue against it.
- Count Faheem_Anis1 and Ultimitehand as two Google Pro reports: rejected; the cell would then pass 11.4 against 1.2 x 12.0 only by double counting.
- Split Kimi partitions at 10-27/29: rejected on the primary retest.
- Split Google partitions at 10-21/22 now: deferred; needs primary confirmation. If confirmed, the Pro pre-change cell would hold Alpler and the provisional ansofteng, and still fail the two-non-provisional rule.

## Evidence summary

Sources 37, evidence rows 132; primary ledgers recomputed for jbdamask, deepfoundationdesign, Oleg-125, jitendersingh0411, aiplans (both days), Yiji_Kong, jamie950315, Faheem/Ultimitehand, Astralyn and x2v. Reddit sweep: 5,359 Claude-subreddit comments and 2,515 other-subreddit comments filtered; Hacker News 4,004 hits; locdd 38 recent topics.

## Tradeoffs and risks

- Plus x Sol x 5h passes only if Oleg-125's split-day reading is placed after the 2026-10-11 price split and jitendersingh0411 is kept as one wide range. Counted as two points ($7.5 and $2.9), the cell fails (7.41 > 1.2 x 3.69).
- Headless and SDK entrypoints drain meters 1.14 to 1.95 times faster on Claude and at least 1.36 times on Google; most in-window reports state no entrypoint, so allowance values may be understated.
- Google dollar figures use introductory Argon pricing that ends 2026-11-30; at $4/$20 they double.
- List-priced value per meter point depends on cache share (x2v rows $26.2 to $32.7 per 5h; Kimi legacy $9 to $42), so the 1.20 margin will fail across observers with different mixes.

## Confidence and remaining gaps

Confidence is high for the Oleg-125 correction, the Faheem/Ultimitehand identity, the mirror identity and the jbdamask, deepfoundationdesign, aiplans, Yiji_Kong and jamie950315 arithmetic; medium for the Kimi no-doubling finding; low for the Google quota-raise date and the OpenAI Pro shrink. Gaps: X search, Zhihu, YouTube, Bluesky, r/ChatGPTPro, unread GitHub comment threads, byte-exact GitHub copies, original of the Team 1x test.

## Blocked or limited sources

- linux.do search and latest endpoints: Cloudflare "Just a moment" challenge (403); recorded as blocked and not automated. Topic 3071240 returned content on a plain request.
- GitHub REST and GraphQL for openai/codex and anthropics/claude-code: repository not enabled; issue pages read through the fetch tool only. A third-party reader proxy for GitHub was refused by the permission layer.
- X search: unavailable (login); fxtwitter used for linked posts.
- Arctic Shift: 100-result cap, intermittent 422 and timeouts.

## Downstream handoff route

`silver-ensure-docs` then `silver-validate` per the standard composition chain; the ValueRank owner applies the record corrections in `plan_reports.json` and decides the Google and OpenAI change-detection checks (O167). See `handoff.md`.
