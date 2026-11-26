# Plan-allowance research for the 2026-11-26 cohort (three stages, O164 / O167 / O165 / O196 / O198)

Run on 2026-11-26 (UTC 03:09 to 04:08) for the 45-configuration cohort in `research/2026-11-26-recapture/cohort.json` (14 models: Claude Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5; GPT-6.2 Sol, GPT-6.2 Astra, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Astra, GPT-6 Luna; Gemini 4 Neon, Gemini 4 Carbon; Muse Ember; MiMo-V2.6-Flash). Research only: nothing under `valuerank/`, `tests/`, `data/` or any draft was touched. The "my reading" statements apply O11, O82, O86, O87 and O165 myself and are for the reviewer to verify.

Inputs read first: `AGENTS.md` (plan research rules), `data/plan_reports.json`, `data/plan_cost_routes.json` (`evidencePolicy.searchLog`, `announcedChanges`, `partitionSplits`), the 2026-10-25 and 2026-11-05 records and the 2026-11-11 OpenCode Go record. This worktree was cut at an older commit than the one holding the 2026-11-26 cohort and data files, so those four files were read from commit `bc33443` of the main line (`git show`).

## 1. The three stages

| Stage | Method | Queries / volume | Reached | Unreachable or partial |
|---|---|---|---|---|
| 1. Plain web search | WebSearch tool (standard mode), then every claim opened with curl or WebFetch; provider pages archived | 37 searches (`stage1/queries-websearch.md`) and about 70 direct page fetches | Anthropic help centre, pricing and API pricing pages, release notes; OpenAI help centre, release notes, Codex pricing page, API pricing; Antigravity docs (models, plans), Google AI plans page, Gemini API pricing; Meta Muse Code docs and product page, Meta Model API docs; Xiaomi MiMo docs; aiplans.dev; secondary coverage | github.com and api.github.com (session proxy: "GitHub access to this repository is not enabled"); claudeissues.com (egress proxy 502); thenewstack.io, androidauthority.com, androidheadlines.com (403); fourweekmba.com (challenge page); developer.meta.com blog (503); reddit.com direct (403) |
| 2. Deeper pass (`anthropic-skills:deep-research`; no Agent tool in this session, so one researcher followed its `researcher.md`) | structured sweeps: 38,996 Reddit posts in 17 subreddits (two empty), 3,919 Reddit comments (body search), 1,695 Hacker News items, 341 Bluesky posts, X via fxtwitter, Google AI and OpenAI forums, LINUX DO mirror, aiplans.dev (`stage2/README.md`) | see `stage2/README.md` | Reddit (Arctic Shift mirror), Hacker News (Algolia), Bluesky, X post JSON, the Google forum (single threads), OpenAI community thread 1409401 (tail) | the Google forum, OpenAI community and LINUX DO topic fetches were mostly refused by rate limits, so those three were **not swept to completion**; r/ClaudeAI and r/ChatGPTPro comments not swept; X search, V2EX, Zhihu, YouTube not used |
| 3. Third pass, run through Perplexity (perplexity skill driver), **Silver Bullet Deep Research unavailable** | same prompt to Claude Sonnet 5.5, GPT-6.2 Sol and Kimi K3 (Search on, Thinking on, driver verification line valid for each) | 3 runs (`stage3/`) | open-web search; every page it named was re-fetched | the models could not open Reddit, GitHub, X or the forums; Gemini and GLM panel members not run; several of their claims were wrong or unverifiable (`stage3/README.md`) |

## 2. Reports (O165 archive, window 2026-10-02 .. 2026-11-26)

`reports.json` has 34 records. **30 records from 15 observers have byte-exact saved copies** (SHA-256 and fetch instant in `archive/MANIFEST.sha256`; the manifest was re-verified after writing, 0 mismatches). Three of the observers (Theo, IndividualPlus2011, Yiji_Kong) were on file with earlier reports. **Counted under my reading of O11 as eligible records: 15 records from 9 observers** (the rest are derived, mixed, synthetic or spanning a split; each record's `reading.why` says why).

| Cell (plan x model, unit) | New eligible records (observer, date, API-priced $) |
|---|---|
| Ultra (Max 20x) x Opus 5.5, week | WuM1ha1nho 2026-11-16 $2,000-$2,800 (typical $2,600); gianfrugo 2026-11-14 $2,600 ($1,780 at 68%); MRC2021 2026-11-12 $2,098 (Opus medium) |
| Ultra x Fable 5.2, week (Fable meter, at most half the week) | MulletIQ 2026-11-14 $560-$720 (0% to 8% for $50.28); MRC2021 2026-11-12 $1,130 of the whole bar (= $565 for the half-week cap) |
| Ultra x Sonnet 5.5, week | MRC2021 $2,074 (Sonnet high) |
| Max 5x x Opus 5.5, week / month | sunaurus 2026-11-08 $1,250-$1,815 per week; Huryn 2026-11-19/20 $4,520-$4,760 per month |
| Max 5x x Fable 5.2, month | Huryn $2,560-$2,900 on a whole-week basis ($1,360 with the half-week cap) |
| Pro x Opus 5.5, 5h | AnshulJ999 2026-11-10 $36.3-$44 |
| Pro x Fable 5.2, 5h | AnshulJ999 2026-11-10 $19.1 (inside the closed launch week) |
| Plus x GPT-6.2 Sol, 5h | IndividualPlus2011 2026-11-24 $9.75 (launch-day reading $11.75, not counted) |
| Ultra 5x x Gemini 4 Neon, month | Huryn $2,530-$2,630 (his note: counts read 10-38% low, "likely 28-41x") |
| Ultra 20x x Gemini 4 Carbon, 5h / week | ubelai 2026-11-11 $203.9-$211.8 per five hours (Carbon Low), $815.7-$817.2 per week, at the $2/$10/$0.10 introductory price (twice as much at the 2026-12-01 price) |

Recorded but not counted (derived, mixed-model, synthetic single-token-class, spanning splits, a non-cohort model, or the cache of a closed window): hhspiny (Max, Opus/Sonnet/Haiku 5.5 per five hours, one token class at a time: Opus $66-$131, Sonnet $49-$95, Haiku $37-$72), Theo (Ultra, $14,662 a month of Opus 5.5 and $3,021 of Fable 5.2 from Aug 11 to Nov 9, crosses five splits), WuM1ha1nho's Sonnet and Fable figures (credit-table derived), MulletIQ's earlier Opus week $2,494, x2v (Pro, headless `claude -p`, $26-$44 per five hours), deepturned180isdeep (Plus, GPT-6.1 Sol and GPT-6 Luna, weekly share derived from a ratio), Yiji_Kong (Ultra 5x, Carbon 3.00x of the Argon bucket, inferred $49.2-$50.0), mcD0m (Google AI Pro, $30 per five hours and $105 then $120 per week for Hydrogen and Flash, non-cohort models).

Seen and set aside, with the reason (full list in `reports.json` where recorded): Schachi (Pro, model unstated, 2026-11-04); pussy_beast (Plus, model unstated, "$10 per five hours, $50 per week", 2026-11-23); StarOcean (LINUX DO, Pro, Fable 5.2, "ten-odd dollars" took over half a five-hour limit, vague); Noob_Kid and Machine2024 (limit-shrink claims, mixed or tier unstated); ProfessionalJackals (Pro 100, $1,120 a week, model unstated); JaredReabow (Pro 500, observed use, no limit reached); Atlas ADE (derived fit, Ultra Opus week "$1,200 to $3,700"); the Wokey tracker (aggregator, mixed models: Claude Pro $163, Max $844, Ultra $1,570 a week; Codex Plus $44, Pro 200 $1,095 a week); InventiveHQ (2026-10-04, Pro 100/200, GPT-6 Sol, already seen on 2026-11-05); Huryn's ChatGPT Pro $100 (GPT-6.1 Sol 10.25x) and Muse Code High (Muse Spark 1.3, 9.3x), both "measured Oct 1", outside the window and, for Muse, not Muse Ember.

### The queued post-cutoff reports

| Report | Result |
|---|---|
| douflou, anthropics/claude-code #106375 (Max, Opus 5.5 medium, 2026-11-03: $20.46 moved the five-hour meter 16 to 26% through the terminal, $19.83 through `claude -p` 26 to 45%; weekly 3 points per about $40) | The page could not be fetched byte-exact: github.com and api.github.com are refused by the session proxy, and an attempt to attach the repository was denied by the permission layer (not worked around). WebFetch returned the comment text; saved as `archive/github-rendered/...106375-douflou.rendered.md`, **not byte-exact, not counted** (O165). Tier not stated either. |
| ricardoraposo, #97074 (Max 20x/Ultra, Opus 5.5 low) | Not retrievable: the visible part of the thread (21 of 143 items) did not contain the comment; `...97074-ricardoraposo.NOT-FOUND.md` records that. **Not counted.** |
| smaug42, #105621 (Pro, Opus 5.5, 2026-11-02: about $32 for 16% of the five-hour window and 3% of the week) | WebFetch rendering saved (also JCorners68's "Max", 26% of a session in under a minute); not byte-exact, **not counted**; also about four times every other Pro reading. |
| sergiokapone, #101937 (Pro, 2026-10-27, $13-$14 for a five-hour window) | WebFetch rendering saved; mixed models (Opus 5.5, Haiku 4.5, one Sonnet 5.5 request) and not byte-exact: **not counted.** |
| x2v, aiplans.dev 2026-11-04 (Pro, Opus 5.5 medium, headless) | **Archived byte-exact** (`archive/aiplans-atlas/aiplans-claude-pro-opus55-2026-11-04.md`, fetched 2026-11-26T03:14:32Z, 1,148 bytes, SHA-256 `512bb066...`, identical to the 2026-11-05 copy), with the guide page and the artifact shell. Headless entrypoint: the five-hour meter runs about 1.95x faster than interactive (douflou), so I do not count it. |

## 3. Cells (model x plan), outcome under my reading of O11

A cell "has a qualifying report" only with at least two independent, concordant, eligible reports in one partition (O11, O86 margin 1.20, O82, O87). **Ultra and Max here are Max 20x and Max 5x**: Max 20x has its own partition from 2026-10-30 (rename), Max 5x and Pro continue the partition opened at 2026-10-17T13:00Z.

| Cell | Result |
|---|---|
| Fable 5.2 x Ultra x week | **Passes**: MulletIQ $560-$720 (Fable meter) and MRC2021 $1,130 of the whole bar, i.e. $565 at the half-week cap: the largest lower bound ($565) is within 1.20 of the smallest upper bound ($565). Two independent observers. (If the reviewer compares MRC2021's whole-bar figure with MulletIQ's Fable-limit figure without halving, it fails; the convention is the owner's.) |
| Opus 5.5 x Ultra x week | **Borderline**: WuM1ha1nho [$2,000-$2,800], gianfrugo [$2,600], MRC2021 [$2,098]. Every pair passes O86; the three together miss the margin by 3% (largest lower bound $2,600 vs 1.20 x smallest upper bound $2,098 = $2,518). Theo ($3,421) and MulletIQ's $2,494 are excluded (spans / earlier measurement). |
| Opus 5.5 x Max 5x x month | **Passes only if a weekly reading is pooled into the month at 52/12**: sunaurus $1,250-$1,815 a week = $5,417-$7,865 a month, Huryn $4,520-$4,760; largest lower bound $5,417 vs 1.20 x $4,760 = $5,712. As separate weekly and monthly cells each has one report. |
| Sonnet 5.5 x Ultra x week | one eligible report (MRC2021): no. Sonnet 5.5 x Max 5x: hhspiny's five-hour readings only (single-token-class synthetic): no. |
| Haiku 5.5, any plan | hhspiny only (synthetic): no. |
| Opus 5.5 x Pro x 5h | AnshulJ999 $36.3-$44 only eligible new report; x2v excluded (headless), K45SLE $42 on file is provisional: no. |
| Fable 5.2 x Pro x 5h; Fable 5.2 x Max 5x x month | one report each (AnshulJ999, closed launch week; Huryn): no. |
| GPT-6.2 Sol x Plus x 5h | one observer (IndividualPlus2011) with two readings that differ by 17%: no. |
| Gemini 4 Neon x Ultra 5x x month | one report (Huryn): no. Neon x Pro, x Ultra 20x: none. |
| Gemini 4 Carbon x Ultra 20x x 5h / week | one observer (ubelai): no. Carbon x Ultra 5x: inferred only. Carbon x Pro: available since 2026-11-23, no reading. |
| GPT-6.2 Astra (every plan), GPT-6.1 Sol (Pro 100/200/500, Plus new), GPT-6.1 Terra (new), GPT-6 Astra (new), GPT-6 Luna (new), every Pro 100/200/500 cell | no new eligible report. The 2026-10-31 Terra x Plus x 5h cell (three reports, O82 bars conversion) is unchanged. |
| Muse Ember x any Muse Code tier | no report of any kind; allowances are prompt counts and multiples (10-50 prompts per five hours on Everyday; High 5x, Power 20x, Maximum 80x), never a numerator. |
| MiMo-V2.6-Flash x Token Plan tiers | no report; the O46 quota ceiling stands; plan terms unchanged since 2026-10-23. |
| OpenCode Go x GPT-6 Luna, Claude Haiku 5.5, MiMo-V2.6-Flash | published dollar limits unchanged ($15, $15, $60 on Go): section 6. |

## 4. Changes since 2026-11-05 (`changes.json`, 21 records: 13 benign, 6 unclear, 2 adverse; O196 direction)

| Provider | Changes (date; type; direction) |
|---|---|
| Anthropic | Fable 5.2 on Claude plans (2026-11-09; availability; benign); launch offers: Pro week of Fable and 1-3 Fable resets for Max/Ultra (2026-11-09 to 2026-11-16 and to 2027-03-08; reset; benign, Pro part expired); Fable 5.2 API price $8/$40 vs $10/$50 (2026-11-09; price; unclear, factor 0.8; Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 $0.10/$0.50 unchanged); usage credits bought from 2026-12-07 expire after 12 months (announced, not in force; credit; **adverse**, purchased credits only, plan allowances untouched); user-claimed weekly-limit shrink on Max 5x and unnamed tiers in early to mid November (limit; unclear: sunaurus, Machine2024 and Noob_Kid claim it, WuM1ha1nho, perfektcrash and the Wokey tracker see none on Ultra). Plan prices unchanged (Pro $20/$17 annual, Max $100, Ultra $200). |
| OpenAI | GPT-6.2 Astra and Sol in Work and Codex (2026-11-17; availability; benign); API price Astra $8/$40 (-20% vs GPT-6 Astra $10/$50, cached -60%), Sol $2/$10 unchanged (price; unclear, factor 0.8); metering: Fast 2x for GPT-6.2 (2.5x for 6.1 and 6), Ultrafast 6x included (8x for GPT-6 Astra and GPT-6.1 Sol), credits 3x to 2027-02-28; Ultrafast on Pro 200 for GPT-6.2 Sol in Codex only, Pro 500 both, Pro 100 none (2026-11-17; metering; benign); chat-tab GPT-6.2 (2026-11-23; availability; benign); the December shared ChatGPT/Codex allowance is **still announced, not in force**, help article "Updated: yesterday", no sizes, "a small group of users may see the usage changes before December" (metering; unclear); one observer measured GPT-6.2 Sol on Plus falling from $11.75 to $9.75 per five hours (2026-11-24; limit; **adverse**, measured factor 0.83, unannounced, one observer). No new Pro 100/200/500 limit change after the registered 2026-10-29 doubling. |
| Google | Gemini 4 Carbon to AI Ultra (2026-11-10; availability; benign); Gemini 4 Neon launched for AI Pro and Ultra (2026-11-18; benign); Antigravity quota reset for all (2026-11-17; reset; benign); caching gain "22%" with a reset (2026-11-21; metering; benign); Carbon to paid AI Pro in Antigravity plus a quota reset (2026-11-23; availability; benign); Pro shared Gemini weekly pool $105 to $120 with the $15 Argon pool merged (2026-11-23; limit; unclear, user-detected; a user then reports 45% of the week gone in one session); announced for 2026-11-30 / 2026-12-01: Carbon and Argon API price $2/$10 to $4/$20, and Argon, Gemini 3.8 Flash, GPT-OSS-120b and Claude 4.6 leave Antigravity (price; unclear, factor 2). Google AI Ultra stays split in 5x ($99.99) and 20x ($199.99). The YouTube Premium Family perk change of 2026-11-18 is not a registered type. |
| Meta | Muse Ember available in Muse Code, listed in all four subscription plans in the docs (Everyday $5, High $15, Power $50, Maximum $200); developer.meta.com's product page omits Ember from Everyday (conflict); no consumer Muse plan documented with Ember (2026-11-09; availability; benign). |
| Xiaomi | Team Token Plan added (2-seat minimum, same per-seat prices and credits; not a Plan-basis plan); individual Lite $6 / Standard $16 / Pro $50 / Max $100 and 4.1B / 11B / 38B / 82B credits unchanged (availability; benign). |
| OpenCode | Section 6 (limit; benign for GLM-5.3 and Kimi K3.1 Pro; cohort models unchanged). |

## 5. New-model plan availability on 2026-11-26

- **Claude Fable 5.2**: on Max and Ultra inside the weekly pool, up to 50% of the weekly limit (a separate Fable meter; it draws the pool faster); on Pro and Team standard seats only through pay-as-you-go usage credits (the free week to 2026-11-16 has ended). Source: Claude help "Claude Fable models on your plan" and the pricing page ("Fable, paid with usage credits" on Pro).
- **GPT-6.2 Sol and GPT-6.2 Astra**: in ChatGPT Work and Codex on Plus and Pro 100/200/500 (and Business, Enterprise, Edu); not in regular Chat (a chat-tuned GPT-6.2 Sol is, since 2026-11-23). OpenAI's Plus estimates: Astra 6-50, Sol 17-180 local messages per five hours. Ultrafast: Pro 500 both, Pro 200 Sol in Codex only.
- **Gemini 4 Neon**: Google AI Pro (paid), Ultra and Enterprise in Antigravity (default model) and in the Gemini app for Pro and Ultra; not on Free or Google AI Plus. **Gemini 4 Carbon**: Ultra since 2026-11-10; paid AI Pro in Antigravity since 2026-11-23 (the Gemini app page still lists it under Ultra); Argon is leaving on 2026-11-30.
- **Muse Ember**: Muse Code subscription plans (all four tiers per the docs); API pay-as-you-go. No Meta consumer plan is documented to include it.
- **MiMo-V2.6-Flash**: all MiMo Token Plan tiers (individual and team); also on OpenCode Go at $60 a month on the Go plan.

## 6. OpenCode Go (O198)

Page re-fetched 2026-11-26T03:10:58Z, SHA-256 `40c238db6cfc8ae3dcb3ecef1c309af1e1a376bebd2ca12cf7b85228a971379c` (78,448 bytes; `opencode-go/raw/`). The Go page no longer prints the per-model limit table; the limits are in the model list API it links to (saved, `d49d1038...`). Against the 2026-11-11 page: **no cohort model's monthly dollar limit or fee changed and no cohort model was added or removed** (GPT-6 Luna $15, Claude Haiku 5.5 $15, MiMo-V2.6-Flash $60 on Go; prices per million tokens identical). Non-cohort changes: GLM-5.3 $15 to $200, Kimi K3.1 Pro $15 to $60, LongCat free to paid $60, Qwen4 Max and six decision/embedding models added, GLM-5.2, LongCat-2.0, MiMo-V2.5 and MiMo-V2.5-Pro removed, Go Teams 2-member minimum. Details and the per-row table: `opencode-go/README.md`, `opencode-go/go-limits-comparison.json`.

## 7. What I could not reach (also in section 1)

github.com issue pages and `api.github.com` (so no byte-exact copy of any GitHub report; the attach-repository request was denied and was not worked around); the experiment repository behind Huryn's figures (`phuryn/experiments`); claudeissues.com and other egress-blocked hosts; X search and the original X posts of Varun Mohan (Antigravity reset and Carbon-on-Pro statements were read through 9to5google, a Reddit quote and two outlets); Google's own Carbon launch post (dated from secondary coverage); the Google AI developer forum, the OpenAI community and LINUX DO full-text (rate limited, partial); r/ClaudeAI and r/ChatGPTPro comments; V2EX; the Wayback copy of any page. Silver Bullet Deep Research is unavailable here; stage 3 is Perplexity (three models).

## 8. Notes for the reviewer

- Theo's tweet says "Fable 5.5" while his chart says Fable 5.2; his measurement span (2026-08-11 to 2026-11-09) predates Fable 5.2, so I recorded the Fable figure as derived.
- Huryn gives the month, not the week, and does not say how he converted; his repository was unreachable. He flags his own Neon figure as an undercount.
- Allowances measured through different entrypoints differ (headless `-p` and the Agent SDK meter the five-hour window about 1.95x faster than the interactive terminal, douflou, not archived); x2v used `-p`.
- Antigravity meters Argon and Carbon at 3.00x of their published price (Yiji_Kong, ubelai); the published price doubles on 2026-12-01. ubelai's dollars are at the introductory price.
- The Fable "50% of the weekly limit" ceiling makes the Fable figures of MulletIQ (the Fable meter) and MRC2021 (the whole bar) differ by a factor of two in definition, not in measurement.
- Two limit changes rest on one observer each (OpenAI Sol 6.2 on Plus, Google AI Pro pool) and neither is acknowledged by its provider; both stay out of `partitionSplits` until a second source appears (O79).

## 9. Files

`reports.json` (report records), `changes.json` (change records), `opencode-go/` (page, hashes, comparison), `archive/` (all saved pages, `MANIFEST.sha256`, `MANIFEST.tsv`, `github-rendered/` for the four non-byte-exact GitHub items), `stage1/queries-websearch.md`, `stage2/README.md` and `stage2/tools/`, `stage3/` (prompt and the three outputs), `searchlog-entry.json` (a proposed `searchLog` entry, not written into `data/`).
