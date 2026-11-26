# Stage 1 (plain web search), Anthropic Claude plans — 2026-11-05

Scope: user reports of API-list-priced consumption tied to a meter fraction or to exhausting a window, for Claude
Opus 5.5, Sonnet 5.5 and Haiku 5.5 on Claude Pro, Max 5x (renamed "Max" 2026-10-30) and Max 20x (renamed "Ultra"
2026-10-30). Report window: measured at least partly in 2026-10-02 .. 2026-11-01T06:10Z. Priority: 2026-10-25 .. 11-01.
Rules: data/plan_cost_routes.json evidencePolicy.reportEligibilityProfile (O71 v1). Recorded reports compared against
data/plan_reports.json (provider Anthropic) by observer and URL.

## Summary

- **One clean new admitting report.** jbdamask (X, 2026-10-28) gives Max 20x, Opus 5.5 only (eight agents), 36% of the
  weekly limit in under 20 hours. The token table prices at $831 at Opus 5.5 list, which gives ≈$2,308/week
  ($2,277–2,341 with integer rounding). The week is "last week" relative to 2026-10-28, so about 10-19..10-26, inside
  the 10-17..10-30 Max 20x partition.
- **One more new candidate needs a researcher-applied price.** deepfoundationdesign (anthropics/claude-code #106322,
  2026-10-31) gives Max 5x, `claude-opus-5-5` for effectively all requests. Week 10-28 → 10-31: 3.19B cache read,
  24.2M cache write and 5.9M output at 64% of the week. That prices at $877–950, which gives ≈$1,360–1,495/week.
  Uncached input is not reported, so these figures are a slight undercount.
- **Many new candidates fail on one rule each.** The commonest failures are an unstated model (simon83, HN), an
  unstated tier (tait143, sammysanchan) and a mixed model (badcookies 97.6–98% Opus, Coriatel 98% Opus, Thraetaona
  "very little Fable", BoboThePirate, EthanRCT, rbartoli). Others are derived fits (lambdita, perfektcrash,
  Fast-and-Pythonic), a span across the 10-17 split (Fast-and-Pythonic) or a lower bound (daniel-sousa-me, malrobot).
- **Ultra after 10-30 (new partition).** Coriatel reports $307 at 38% (98% Opus 5.5), which gives ≈$808/week, much
  lower than any pre-split Max 20x figure. Further readings dated after the cutoff are in the separate table below:
  WojtekVoy, z4k3ru, BoboThePirate's Ultra week, CalypsoTheKitty and Eth66.
- **Sonnet 5.5 and Haiku 5.5: still no single-model, meter-tied report on any tier.** Only model-weight fits exist,
  and these are derived figures that count as cross-checks only. lambdita's fresh-Pro header fit puts a Sonnet 5.5 API
  dollar at 1.36× the quota of an Opus 5.5 API dollar, and Haiku 5.5 (≤100K-token prompts) at 1.76×.
  Fast-and-Pythonic's Pro 5-hour fit gives ≈$0.23 of Sonnet 5.5 per 5h point against ≈$0.42 of Opus 5.5.
- **O11 verdict: no cell passes.** The only cell with two non-provisional single-model reports in one partition is
  Opus 5.5 × Max 20x × week (10-17..10-30): jbdamask and the recorded NicoAica "after". They fail the 1.20 margin by
  about 11×.
- **New caveat for every transcript-priced report.** An HN thread of 2026-10-29 (gist by flamerix-ai) shows that
  Claude Code's `agent_summary` status-label calls do not appear in the local transcripts. simon83 estimated them at
  ≈16% of his true total, and an Anthropic engineer (edwinarbus) put the telemetry-wide average at about 2% of
  list-price cost. Ledger-priced figures can therefore understate meter-counted spend by 2–16%.

Prices used for researcher pricing (per 1M tokens): Opus 5.5 input $4, output $20, cache read $0.20, 5-min write $5,
1-h write $8. Sonnet 5.5 is $2 / $10 with cache read $0.10 (after about 2026-10-08). Haiku 5.5 (≤100K prompt) is
$0.10 / $0.50 / $0.01. Where only the total cache write is given, both write prices are shown as a range. Reporters'
own dollar figures are quoted as given.

Partitions applied (evidencePolicy.partitionSplits, Anthropic):
- Claude family limit splits fall at 2026-10-09 and 2026-10-17T13:00Z.
- Max 20x has an extra limit split at 2026-10-30 (rename to Ultra; five-hour limit removed; weekly limit stated
  unchanged).
- Max 5x and Pro have no split at 10-30 (rename only).
- The 2026-10-07 credit event is typed credit and does not split the partitions.

Opus 5.5 partitions in the window are therefore:
- **P1:** 09-22..10-09
- **P2:** 10-09..10-17T13Z
- **P3:** 10-17T13Z.. (to 10-30 for Max 20x; open for Pro and Max 5x)
- **P4:** Max 20x/Ultra from 10-30

## Candidate table

Abbreviations:
- "MS" means the weekly meter source.
- NEW / REC means new or already recorded in data/plan_reports.json.
- Q means qualifies (Y/N).

### Inside the window

| # | Plan | Unit | Model | Observer | URL | Date UTC (measured) | Token split | Meter movement | $ at API list (prices) → per unit | NEW/REC | Q | Reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Max 20x | week | Opus 5.5 (all eight agents) | jbdamask | https://x.com/jbdamask/status/2115515191039545712 | posted 2026-10-28T18:45Z; "last week", <20h (≈10-19..10-26) | cache reads 2,449M ($490); cache writes new context 27M ($136); cache rebuilds 35M ($176); output+input 1.5M ($29) | weekly +36% in <20h ("burned 36% of my Max 20x weekly limit in less than 20 hours") | $831 (reporter's table; consistent with $0.20 read / $5 5-min write) → $2,308/week (35.5–36.5%: $2,277–2,341). With all writes at 1-h $8 it would be ≈$1,015 → ≈$2,820 | NEW | Y | Single model, exact tier, meter fraction, P3. Caveat: logs summed by Claude "counting each request once"; no exact dates. |
| 2 | Max 5x | week | `claude-opus-5-5` "for effectively all requests" | deepfoundationdesign | https://github.com/anthropics/claude-code/issues/106322 | 2026-10-28 22:00Z → 2026-10-31 ≈01:13Z | 7,089 requests; output 5.9M; cache read 3.19B; cache write 24.2M; input not reported | "64% after 2 days" (warning screenshot) | Researcher-priced: $638.00 + $121.00–193.60 + $118.00 = $877.0–949.6 → $1,370–1,484/week (63.5–64.5%: $1,360–1,495) | NEW | Y (researcher-priced; slight undercount) | Single model, exact tier, meter fraction, P3 (no Max 5x split at 10-30). Earlier rows: Sep 30→Oct 7 no warning at 3.46B / 26.9M / 6.1M (lower bound ≈$949–1,029); Oct 14→21 and Oct 21→28 reached the limit but give only output and the reporter's own weighting, so they cannot be repriced. |
| 3 | Max 20x | week | not stated ("tasked Opus" to write the script) | simon83 | https://news.ycombinator.com/item?id=50286504 ; https://news.ycombinator.com/item?id=50289476 | 2026-10-29 (week ending 10-29) | none | quota 98% (resets 10-29); "1% of weekly limit is worth about $20" | "$1,970" transcripts + "~$380" hidden status-label calls → $2,010/week ($2,398 incl. hidden); own figure "about $2,000" | NEW | N | Model unstated. |
| 4 | Max 20x | 5h | not stated | simon83 | same (50289476) | 2026-10-29 | none | "1% of the 5h window is worth about $5.20" | → ≈$520 / 5h | NEW | N | Model unstated. |
| 5 | Max (tier unstated) | week | `claude-opus-5-5` "for every call in the window" | tait143 | https://github.com/anthropics/claude-code/issues/106385 | 2026-10-29 09:34–13:49Z | 53.4M processed from scratch (cache writes), 34.1M cache read, 0.38M output | ≈14% (7.7% old week + 6.3% new week; "range 11-15%") across the 08:00 EDT weekly reset | "about $281" (agents ≈$273, main ≈$8.5) → ≈$2,007/week ($1,873–2,555) | NEW | N | Tier unstated ("Max plan", before the rename). Cell "Claude Max (tier unstated)" only. A per-period meter split is given but per-period dollars are not. |
| 6 | Max 20x | week | "primarily Opus 5.5, very little Fable" | Thraetaona | https://github.com/anthropics/claude-code/issues/105240 | reset 2026-10-27 → exhausted 2026-10-28 | input 19.5M; output 38.8M; cache write 113.9M; cache read ≈4.9B | 0 → 100% (exhaustion) | Researcher-priced as all Opus: $78 + $776 + $569.5–911.2 + $980 = $2,403–2,745 /week | NEW | N | Mixed (some Fable); plan-level only. |
| 7 | Max 20x | week | 97.6% Opus 5.5 by $ (Fable 1.6%, Sonnet 0.8%) | badcookies | https://www.reddit.com/r/ClaudeAI/comments/1xjiwiq/ | posted 2026-10-30; "last few weeks", undated | none | three accounts at 100% | "2278 / 2281 / 2386" per reset → $2,278–2,386/week | NEW | N (borderline) | Mixed (2.4% other models); weeks undated (P2/P3 unknown); "Est. API Cost" priced by Claude, price basis unstated. |
| 8 | Max 5x | week | 98% Opus 5.5 by $ | badcookies | same | same | none | three accounts at 100% | "1179 / 1187 / 1153" → $1,153–1,187/week | NEW | N (borderline) | As #7. |
| 9 | Pro | week | not split for Pro (new accounts) | badcookies | same | ≈late Oct (new accounts) | none | "230 … 95" and "105 … 41" | $242 and $256/week; "Pro … roughly 5hr limit is worth $35 and weekly $240" | NEW | N | Model mix not stated for Pro; 5h figure is derived ("roughly"). |
| 10 | Max 20x | week | mixed ("had a mix of models, subagent usage") | BoboThePirate | https://www.reddit.com/r/ClaudeCode/comments/1xm1378/_/19s1w4nvxshkx/ | 3 weeks before 10-31 (Sat 08:00 resets: ≈10-10..10-31) | none | "several usage % measurements per week" | "$2030 +- $30" per week | NEW (different URL from recorded bobothepirate-max20x) | N | Mixed. The last week spans 10-30 and the first spans 10-17. |
| 11 | Ultra (ex-Max 20x) | week | "98% Opus 5.5" | Coriatel | https://github.com/anthropics/claude-code/issues/106274 | reset 2026-10-31 01:00Z → comment 2026-11-01 | 2,600 requests | 38% | "$307 API-equivalent at Opus 5.5 list prices, measured with ccusage" → $808/week ($797–819) | NEW | N (borderline) | 2% other model. P4 (post-10-30 Ultra). Also "Oct 4–24 … $1,900–2,300 … all within the weekly limit": no meter fraction, so a lower bound. |
| 12 | Max 20x | week | Opus 5.5 main, Fable 5.1 and Sonnet 5.5 subagents | EthanRCT | https://github.com/anthropics/claude-code/issues/103376 | 2026-10-11 05:00 → 10-15 14:22Z; 2026-10-18 05:00 → 10-19 03:16Z | 2.63M out / 25.76M write / 1,929.5M read; 343K / 7.47M / 299.4M | 0→60%; 0→54% | as Opus: $567–645 → $946–1,074/week (P2); $104–127 → $193–234/week (P3) | NEW | N | Mixed. Comments (justanotheruseer, kreaddis-julien, consolelogreece, philogical) give weighted tokens only, no dollars; philogical withdrew his data. |
| 13 | Pro | 5h | Opus 5.5 (fit from windows ≥90% one model) | Fast-and-Pythonic | https://github.com/anthropics/claude-code/issues/104967 | 2026-10-15..25, 12 windows | none | 5h window rise fitted to $ | "about $0.42 of Opus 5.5" per point → ≈$42 / 5h | NEW | N | Spans the 10-17 split; regression fit, not per-window readings. |
| 14 | Pro | 5h | Sonnet 5.5 (fit) | Fast-and-Pythonic | same | same | none | same | "about $0.23 of Sonnet 5.5" per point → ≈$23 / 5h | NEW | N | Spans the split; Sonnet weight comes only from three mixed windows (reporter: "may well be off"). |
| 15 | Pro | week | not stated (Opus 5.5 and Sonnet 5.5 account) | Fast-and-Pythonic | same | mid-Oct | none | weekly point | "$4.45 at API prices in mid-September and $2.31 in mid-October" → ≈$231/week | NEW | N | Model mix unstated; single figure undated within mid-Oct. |
| 16 | (plan "Padrão", unstated) | 5h / week | `claude-opus-5-5` 100% | sammysanchan | https://x.com/sammysanchan/status/2115218215127208052 | 2026-10-27 16:29–21:29 BRT window | 5h window: in 771; out 315.9K; cache read 154.8M; cache write 999K | 5h 76% → 99%; weekly 10% → 27% (week from 27/10) | 80.5M ($54.16) → 156.1M ($95.26): $95.26 at 99% → ≈$96/5h; Δ$41.10 / 17 weekly pts → ≈$242/week | NEW | N | Tier unstated; the 5h and weekly deltas are mutually inconsistent. |
| 17 | Pro | week, 5h | not stated | SchachiOnReddit | https://www.reddit.com/r/ClaudeAI/comments/1xntrrs/ | "last week" (≈10-28..11-04) | none | 14% → 27% → 40% → 100% (exhaustion, day 2) | "$236.59" at 100% → $237/week; "about $33 per 5h window" | NEW | N | Model unstated; yearly-billed Pro. This week (after cutoff): 14% $26.74, 27% $55.81. |
| 18 | Max 5x | week | not stated | Unlikely-Peace1268 | https://www.reddit.com/r/ClaudeAI/comments/1xj7z30/_/19rv967bzzb7o/ | 2026-10-30 | none | weekly +3–4% | "$55 of api usage during 1 session" → $1,375–1,833/week | NEW | N | Model unstated. |
| 19 | Max 5x | week | not stated | FaithlessnessFun2639 | https://www.reddit.com/r/ClaudeCode/comments/1xhfch4/ | 2026-10-26..27 (Sun 09:00 reset) | 1.66B tokens, 9.9M output, 97–98% cache reads | 73% in two days | not priced (split incomplete) | NEW | N | Model unstated; split incomplete. |
| 20 | Max 5x | week, 5h | Opus 5.5, Sonnet, Fable | rbartoli (Riccardo Bartoli) | https://x.com/rbartoli/status/2115218617071476827 ; https://rblab.com/what-a-claude-max-window-is-worth-in-api-dollars/ | May–Oct 2026 | 55% cache reads / 31% writes / 13% output of spend | 40 5h lockouts; 4 weekly lockouts | 5h median before lockout: October "$169" (all months "$155", range $65–385); weekly lockouts "$2.0–2.5k", one "$1.2k"; Max 20x lockouts "$605 and $760" | NEW | N | Mixed models; per-period values are monthly medians, not single dated windows. |
| 21 | Max 5x | week, 5h | not stated (Fable share 43.5% of a week mentioned) | Fuduntu | https://github.com/anthropics/claude-code/issues/99330 | 2026-10-03 (5x); 09-24 / 09-30 (20x) | none | 5x: 5h exhausted; week 18%. 20x: 5h exhausted; week 100% | 5x: "≈ $158" / 5h; "18% after ≈ $211" → $1,172/week. 20x: "≈ $508" / 5h; "≈ $1,827" per week (09-30, before window) | NEW | N | Model mix unstated (Fable used); 20x readings before the window. |
| 22 | Max 20x | week | Opus 5.5 (effort high) | mikemozgii | https://github.com/anthropics/claude-code/issues/103240 | ≈10-11..10-18 | 10.4B read, 160M write, 21.5M output, ~33,000 requests | "about 70% … after a few days" | as Opus: $2,080 + $800–1,280 + $430 = $3,310–3,790 | NEW | N | Token period is not tied to the 70% reading (spans a reset and probably 10-17). |
| 23 | Max 20x | week, 5h | "regardless of the models" | daReallG | https://www.reddit.com/r/ClaudeCode/comments/1xb6zkj/_/19rfoy3mx7zhf/ | 2026-10-21 | none | "One full 20x session roughly equates to 25% of the weekly" | "$500ish" / 5h; "$2000 … per weekly" | NEW | N | Mixed or unstated model; vague. |
| 24 | (unstated, multiple accounts) | week | "all opus" (version unstated) | Tartooth | https://www.reddit.com/r/ClaudeCode/comments/1xe2fxk/_/19rl656wfpxkz/ | 2026-10-24 | none | "projected … for the full weekly limit"; "at 100% usage" | "$1150 projected"; "~$2600-$3200" in prior weeks | NEW | N | Tier unstated; version unstated; projection. |
| 25 | Max 5x | week | not stated | daniel-sousa-me | https://www.reddit.com/r/ClaudeAI/comments/1xfs5q8/_/19rojyqgpcm3k/ | 2026-10-25 | none | "less than 30%" | "$300 … (as reported by /usage)" → >$1,000/week | NEW | N | Lower bound; model unstated. |
| 26 | Max 20x | month | "mostly Opus 5.5" | malrobot | https://www.reddit.com/r/ClaudeAI/comments/1xhvgyp/_/19rsooqw0zd4w/ | October | ≈5B tokens | weeks end at "~40-50%" | "$2,757 of API spend" for October | NEW | N | No meter fraction tied to the dollars (lower bound); mixed. |
| 27 | Pro | week | not stated | realNyarime | https://x.com/realNyarime/status/2114886352823292146 | week to 2026-10-27 | 890M tokens (CC Switch) | none | "约200+美元" | NEW | N | No meter fraction; model unstated. |
| 28 | Max 5x | week | Opus 5.5 | UPedrolli46470 | https://x.com/UPedrolli46470/status/2114886181683106279 | 2026-10-27 | "一周40亿" (4B tokens), "能跑5天" | none | none | NEW | N | No dollars, no split, no meter fraction. |
| 29 | Pro | week | Opus 5.5 medium | albrxt | https://x.com/albrxt/status/2115207720563519990 | 2026-10-27 | none | "consume 8% of weekly limit in 2h" | none | NEW | N | No dollars. |
| 30 | Pro | 5h | not stated | Potential-Beat2841 | https://www.reddit.com/r/ClaudeCode/comments/1xb0xpu/_/19recycybpn36/ | 2026-10-20 | none | "about 25% of my 5h window on Pro" | "$35.52 at API prices" → ≈$142 / 5h | NEW | N | Model unstated; "about". |
| 31 | (unstated) | 5h | not stated | Little-Cricket-1051 | https://www.reddit.com/r/ClaudeAI/comments/1xguw7r/_/19rque4a4yjup/ | Oct 7–22 vs Oct 25–27 | none | exhausted 5h windows | "October 7–22 median was $26.73, versus $16.54 on October 25–27" | NEW | N | Plan and model unstated. |
| 32 | Pro (fresh account) + one Ultra | week, 5h | per-model weights | lambdita | https://www.reddit.com/r/ClaudeCode/comments/1xki1qr/ | posted 2026-10-31 | header fit: quota = S × (input + 1.25×write + 0.025×read + 5×output); S Opus 5.5 = 1, Sonnet 5.5 = 0.68, Haiku 5.5 = 0.044 | thousands of readings | "Pro … Full week ~$280"; "Ultra … ~$2.8k" at an assumed "typical Claude Code mix ~$5.6 per 1M quota units" | NEW | N | Derived (assumed mix); cross-check only. Says "No recent nerf … flat since the 09-28 resets". |
| 33 | Ultra | week | per-model fit | perfektcrash | https://www.reddit.com/r/ClaudeCode/comments/1xmwjcx/ | posted 2026-11-03 | per 1%: Opus output 660k, input 3M, read 170M, write 4.6M | fitted | "roughly $1,200 to $3,700 … roughly $2,400" (example mix) | NEW | N | Derived example mix, not a measured week; mostly after cutoff. |
| 34 | Max 5x | 5h | mixed (Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / Fable 5.1) | lucthesloth | https://github.com/anthropics/claude-code/issues/105240 | 12 5h limit hits 10-25..10-31 | weighted tokens per window | 5h exhaustions | none (reporter weighting only) | NEW | N | Mixed; no dollars. |
| 35 | Ultra | week | Opus share 84–96% of requests | clem-pxp | https://github.com/anthropics/claude-code/issues/106274 | 10-29 23:00Z → 11-01 22:00Z | 2.1B tokens, 10M output | 76% | none | NEW | N | No split, no dollars; mixed; spans 10-30. |
| 36 | Max 20x | week | not stated | captinjack99 | https://github.com/anthropics/claude-code/issues/104750 | 10-15..10-24 | cache reads/writes by week (Opus + Sonnet) | 85–86%, 42–43% | none (output omitted by the reporter) | NEW | N | Mixed; output not recorded, so it cannot be priced. |

### Already recorded, seen again

| Observer | URL | Status |
|---|---|---|
| daakkast | r/ClaudeCode 1xcwfob/19rit8ed1txuq | ALREADY RECORDED; no new figures |
| PELORA-MARKETING | r/ClaudeCode 1wz3e35/pgm006k | ALREADY RECORDED |
| leaflavaplanetmoss | r/ClaudeCode 1x1esxn/peuarxu | ALREADY RECORDED |
| K45SLE | r/ClaudeCode 1xb70h0/19resfcjmw52b | ALREADY RECORDED |
| Planyy | r/ClaudeCode 1x6p448/pgxgq8h | ALREADY RECORDED |
| NicoAica, kakki-1 | anthropics/claude-code #102667 | ALREADY RECORDED; comments from 10-24 on (rethyria, maks-chipurnov, kcs0116, qcihdtm) carry meter percentages only, no dollars or tokens |
| Theo (pingdotgg) | HN item 50003496 quoting ts-rust README | ALREADY RECORDED |
| wokey.ai | X @WoKey_AI 2114872928210919856 (via Fei2411 #143): Max 20x ≈$1,600/week, Pro ≈$157/week, "约 −6%" | ALREADY RECORDED as aggregator (reseller); not countable |

### After the cutoff (measured wholly after 2026-11-01T06:10Z; not for this release)

| Plan | Unit | Model | Observer | URL | Date | Figures |
|---|---|---|---|---|---|---|
| Ultra | week | "primarily Opus 5.5" | WojtekVoy | https://github.com/anthropics/claude-code/issues/105240 | 2026-11-02 | ≈2% → 99% by 13:16 Warsaw; 1,373 requests, 0.75M output, 416.52M read, 7.41M write → researcher-priced $135–158 (input not given) → ≈$140–163 per 100%. Local logs only; looks anomalous. |
| Ultra | week | not stated | z4k3ru | https://www.reddit.com/r/ClaudeAI/comments/1xlqmtr/_/19s1auva9uk1s/ | ≈2026-11-01..02 | 30% on day 2; output 2,319,366, input 8,556, cache write 15,310,572, cache read 480,323,593; "$200.24" → ≈$667/week |
| Ultra | week | mixed | BoboThePirate | https://www.reddit.com/r/ClaudeCode/comments/1xm1378/_/19s1w4nvxshkx/ | week from 2026-10-31 | "I'll run out at about $1600 API equivalent" (20% below the prior $2,030) |
| Ultra | week | Opus 5.5 + Fable 5.1 | CalypsoTheKitty | https://www.reddit.com/r/ClaudeCode/comments/1xmwjcx/_/19s33ylh4xt0k/ | "last week" to ≈11-02 | "used my full weekly Ultra usage … the token price was $1,600"; mixed; spans 10-30 |
| Ultra | week | not stated | k0rdax | https://www.reddit.com/r/ClaudeCode/comments/1xljnf5/_/19s0s4ie44ujl/ | 10-29 → 11-01 | ccusage "$739 → $423", no meter figure |
| Ultra | week | Opus 5.5 | Eth66 | https://github.com/anthropics/claude-code/issues/105240 | 2026-11-01 22:40Z | 26% in ≈29h; no tokens or dollars |
| Pro | week, 5h | not stated | SchachiOnReddit (this week) | https://www.reddit.com/r/ClaudeAI/comments/1xntrrs/ | 2026-11-04 | "14% $26.74", "27% $55.81" |

## Per-cell O11 verdicts

Two independent non-provisional admitting reports in one partition are required, with the largest lower bound
≤ 1.20 × the smallest upper bound. The tables combine recorded and new reports. Reports measured wholly before
2026-10-02 are not counted.

### Opus 5.5

| Plan × unit | Partition | Admitting reports (range, $) | Verdict |
|---|---|---|---|
| Pro × week | P1 (to 10-09) | none inside the window (NTRYourWaifu, kanzakichiya and the r/ClaudeCode ≈09-24 report all predate 10-02) | FAIL (0) |
| Pro × week | P2 (10-09..10-17) | ganpei777 1,266 | FAIL (1) |
| Pro × week | P3 (10-17..) | none admitting. K45SLE 210–300 is provisional; badcookies, SchachiOnReddit and Fast-and-Pythonic fail | FAIL (0 + 1 provisional) |
| Pro × 5h | any | none admitting. K45SLE 42 is provisional; Fast-and-Pythonic 42 spans the split; others have model or plan unstated | FAIL |
| Max 5x × week | P1 | muscgab 750–830; unlabelled /usage screenshot 1,920 (week of 09-29) | FAIL: 1,920 > 1.2 × 830 = 996 |
| Max 5x × week | P3 | deepfoundationdesign 1,360–1,495 (NEW, researcher-priced) | FAIL (1). It would pair with badcookies 1,153–1,187 (1,360 ≤ 1.2 × 1,187 = 1,424), but badcookies is mixed and undated |
| Max 5x × 5h | any | none (Fuduntu and rbartoli have model unstated or mixed) | FAIL |
| Max 20x × week | P1 | Kanttz 2,484–2,920 (weeks undated, report 10-02); leaflavaplanetmoss 1,140 (≈10-02..09); Theo 2,446–2,600 (two weeks ≤10-13, may span 10-09) | FAIL: 2,484 > 1.2 × 1,140 = 1,368 (and Theo's partition is uncertain) |
| Max 20x × week | P2 | NicoAica "before" 1,294–1,681 | FAIL (1) |
| Max 20x × week | P3 (10-17..10-30) | jbdamask 2,277–2,341 (NEW); NicoAica "after" 182–212 | FAIL: 2,277 > 1.2 × 212 = 254 |
| Max 20x × 5h | P1 | Kanttz 662–754 | FAIL (1) |
| Max 20x × 5h | P2/P3 | none (simon83 model unstated; daReallG mixed) | FAIL |
| Ultra × week | P4 (from 10-30) | Coriatel ≈808 (borderline 98% Opus); not a cell for this release per the brief | n/a, no weekly cell opens |

### Sonnet 5.5 and Haiku 5.5

No admitting report on any plan or unit, so every Sonnet 5.5 and Haiku 5.5 cell FAILS with 0 reports. The only
evidence is derived model-weight fits, which count as cross-checks only:
- lambdita: Sonnet 5.5 1.36× and Haiku 5.5 1.76× the quota of Opus 5.5 per API dollar.
- Fast-and-Pythonic: Sonnet 5.5 ≈$0.23 per Pro 5h point.
- perfektcrash: an Ultra week holds about 110M Sonnet output tokens against 66M Opus.

## Queries run

**Web search** (WebSearch, standard and extended):
- "Opus 5.5 weekly limit percent API cost Max 20x"
- "Claude Ultra plan weekly limit API equivalent dollars November 2026"
- "Fei2411 real-api-pricing Data issue Claude Opus 5.5 weekly"
- "reddit ClaudeCode "Opus 5.5" "weekly" "%" "API" dollars ccusage Max"
- ""Sonnet 5.5" weekly limit percent "$" API equivalent Pro OR Max ccusage"
- ""Haiku 5.5" usage limit percent Claude Pro weekly tokens"
- ""Opus 5.5" "of my weekly" "$" API reddit"
- "Claude Code usage exploded 8x Anthropic weekly limit October 2026 ccusage dollars percent"
- "Claude Pro weekly limit worth dollars API Opus 5.5 measured "per 1%""
- "site:x.com Claude Max weekly limit "Opus 5.5" API equivalent percent"
- ""Sonnet 5.5" Claude Pro "weekly" usage measured dollars per percent ccusage Sonnet only"

**GitHub** (REST search API through gh; issue pages through WebFetch):
- Fei2411/real-api-pricing issue list, pages 1–2. Read issues #143, #148, #156, #163, #170, #131, #134.
- anthropics/claude-code, created 2026-10-15..11-05, matching each of "weekly", "usage", "limit", "quota" and
  ""API" "%"". That gave 758 issues; bodies were filtered for $ and %.
- Read in full: #104967, #106385, #104750, #105305, #105437, #105646, #106322, #104072, #103406, #105240 (with
  comments), #105125, #106274 (with comments), #106733, #105621, #103376 (with comments), #105162, #106598, #107134,
  #102667 (comments from 10-24), #99330, #103240.
- Cross-repo searches: "per 1%" weekly; "API-equivalent" weekly; "ccusage" "weekly"; "seven_day"; "Ultra" "weekly" "%".

**Hacker News** (Algolia `search_by_date`, comments since 2026-10-02):
- Queries: "weekly limit", "Max 20x", "Ultra weekly", "Claude Pro weekly", "API equivalent", "API prices",
  "Sonnet 5.5", "Haiku 5.5", "ccusage", "Opus 5.5 usage", "five hour limit", "weekly usage".
- Story 50284255 was read in full.

**Reddit** (Arctic Shift API mirror, 2026-10-02..11-05):
- Comment full-text search in r/ClaudeCode ("weekly", "API", "ccusage", "equivalent", "API price", "API cost"), in
  r/ClaudeAI ("weekly", "ccusage", "equivalent", "per 1%", "API price", "API cost") and in r/Anthropic ("weekly",
  "API", "ccusage").
- Post search for "weekly" and "API" in each of the three subreddits.
- That gave ≈2,350 unique items, filtered for $, % and plan or limit terms.

**X**:
- Specific posts cited by Fei2411 issues were read through the api.fxtwitter.com mirror: jbdamask, sammysanchan,
  UPedrolli46470, albrxt, rbartoli, runes_leo, realNyarime.
- jbdamask's and sammysanchan's images were downloaded from pbs.twimg.com and read.

**Blogs**: rblab.com (rbartoli) and buttondown.com/botfarm. The botfarm post is dated 2026-03-20, outside the window.

## Venues unreachable or incomplete

- **reddit.com direct.** JSON redirects to login and the page returns 403. pullpush.io returns 521.
  redlib.catsarch.com returns 429. Reddit was read only through Arctic Shift, which is full-text search, so phrasing
  outside the query terms may be missed.
- **Arctic Shift coverage gaps.**
  - Each query stops at 2,000 results. r/ClaudeAI "weekly" comments reach back only to 2026-10-23. r/ClaudeCode
    "weekly" and "API" reach back to ≈10-06.
  - "ccusage" returned 0 hits in r/ClaudeCode and r/ClaudeAI comments (full-text index quirk).
  - The second batch was stopped by the session time limit, so these queries were not run: r/ClaudeAI "API cost"
    beyond page 2; r/ClaudeCode posts "usage" / "limit" / "API"; "Opus 5.5" comments in r/codex, r/Anthropic and
    r/ClaudeCode.
- **GitHub repo endpoints.** The REST repo endpoints for Fei2411/real-api-pricing and anthropics/claude-code are not
  enabled for this session, and attaching the repo was denied. Issues were read through the search API (bodies) and
  WebFetch (rendered pages, comments summarised by the fetch model). Comment quotes from WebFetch should be
  re-verified verbatim in stage 2.
- **X.** There is no X search (no login). Only posts linked from other venues were read, through api.fxtwitter.com.
- **SemiAnalysis.** No new SemiAnalysis or cellcog material was searched beyond the recorded item.
- **Pre-10-25 items found in this pass.** Several are NEW although dated before the previous search (EthanRCT #103376,
  Fuduntu #99330, mikemozgii #103240, captinjack99 #104750, daReallG, Tartooth, Fast-and-Pythonic #104967). None
  qualifies.
