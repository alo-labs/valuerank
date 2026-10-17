# Asia providers and tracker apps — delta retrieval

Retrieved 2026-10-07 through Codex built-in browser (CUA IAB). Target reporting and measurement window: 2026-09-07 through 2026-10-07. This bounded pass found additional independent leads and two verified tracker applications, but **zero additional qualifying API-priced subscription observations**. This is a retrieval result, not proof that none exist.

## Query angles and outcomes

| Angle | Query actually visited | Outcome |
|---|---|---|
| Reddit ZAI monetary usage | `site:reddit.com ZAI GLM coding plan "$" usage September 2026` | Opened GLM-5.3-Flash promotion thread; independent 10B-token anecdote below. |
| Reddit Kimi monetary usage | `site:reddit.com "Kimi K3" "usage" "$"` | Opened detailed K3-only $200-plan weekly ledger; isolated July/August windows excluded. |
| Reddit Alibaba plan cost | `site:reddit.com Qwen coding plan API cost September 2026` | Page initially exposed only search header; no result accepted from this query. |
| HN developer community cost | `site:news.ycombinator.com Kimi GLM "usage" "cost"` | Opened HN GLM subscription report; direct timestamp contradicts search-engine September date. |
| Tracker discovery | `Kimi GLM Qwen subscription usage tracker dashboard` | Verified AIUsage repository and SessionWatcher Kimi guide. |
| Chinese measurement vocabulary | `GLM Kimi Coding Plan 实测 额度 API 费用 2026 9月` | Plan-comparison/official quota results; no qualifying user API-valued ledger located. |
| Exact Qwen variant | `site:reddit.com "Qwen3.8" "plan"` | Opened Qwen3.8-Max token-exhaustion report; direct date August 9, missing API valuation. |

## New independent evidence and exclusions

| Source / report date | Tier and fee mapping | Model variant | Measurement period / observed amount | API-valued numerator | Decision / credibility |
|---|---|---|---|---|---|
| [ByteNomadOne Reddit comment](https://www.reddit.com/r/ZaiGLM/comments/1wmtdt9/comment/pbbydx4/), displayed 15 days ago at retrieval (approximately Sep 22; exact datetime not captured) | Monthly plan; named tier unknown; fee unknown | Thread is GLM-5.3-Flash; commenter does not explicitly isolate every token to that variant | Says 10B tokens used during free promotional timeframe; start/end and input/output/cache split unknown | None stated | Exclude. Actual user token anecdote, but unpriced and insufficient tier/window/model isolation. Do not multiply 10B by any generic rate. |
| [Phylliida Kimi ledger](https://www.reddit.com/r/kimi/comments/1vnl28x/kimi_code_has_reduced_weekly_usage_limits_to_37/), displayed 2 months ago; exact report datetime not captured | Self-reported $200 plan; named tier unknown; monthly frequency not independently established | Explicitly exclusive K3; exact context variant unknown | Jul19–26: $674.23 at 100%; Jul26–Aug2: $663.46 at100%; Aug2–9: $424.50 at100%. Post also labels $93.77 at38.85% as Aug2–9, creating internal period ambiguity | Those amounts are user-reported API-priced estimates accompanied by input/cache/output token counts; raw ledger and rate card not independently reproduced | Exclude all from target window. Stronger quantification than generic quota claims, but dated windows are July/August. Estimated future $241/$250 weekly capacity is an extrapolation, not measured usage. |
| [leobuskin HN purchase report](https://news.ycombinator.com/item?id=49297537), direct `.age` title `2026-08-14T11:48:31`; Google snippet said Sep15 | $18 purchase upgraded to $80 plan, named tier unknown | Post says GLM5.2; later discussion about GLM5.3 does not justify variant transfer | [Comment 49300483](https://news.ycombinator.com/item?id=49300483): 200M tokens about20% weekly usage on $80 plan. [Comment 49299853](https://news.ycombinator.com/item?id=49299853): two agents used18% in approximately8h, author says no proper statistics snapshot | None stated | Exclude. August date, variant mismatch and no API price; direct source outranks search-engine date. Do not convert token total without split. |
| [xandie985 Qwen report](https://www.reddit.com/r/Qwen_AI/comments/1vjtav6/using_qwen_38_max_on_qwen_cloud_felt_like_scam/), direct post `time datetime` `2026-08-09T15:50:00.840Z` | Tier unknown; post says5k credits (two2.5k weekly allocations); fee missing. Another commenter reports $20 subscription but cannot attach that fee to OP | Title identifies Qwen3.8 max; context variant unknown | 35M tokens within30min, credits exhausted; describes two weeks of credits | None stated | Exclude. August date and no API-priced numerator. Search snippet displayed1 month ago while direct source displayed2 months and exact August date. First-person usage credible as a report, unreproduced. |

The ZAI thread itself advertises unlimited Flash usage in promotional hours and double quota in other harnesses until Oct7. These are provider/promotion quota claims, not measured API-valued numerators. [Thread](https://www.reddit.com/r/ZaiGLM/comments/1wmtdt9/glm53flash_unlimited_usage_on_zcode_extended/).

## Tracker-app discovery (existence separate from crowd data)

| Application | Directly inspected evidence | Provider relevance | Public measured allowance data? |
|---|---|---|---|
| [AIUsage](https://github.com/sylearn/AIUsage) | README describes dashboard for subscriptions, quotas, costs and accounts; Kimi is in12+ provider list. Usage Stats includes per-model trends and time periods; OpenCode cost is read from local `opencode.db`, prepriced with models.dev. | Kimi explicit in supported provider list; GLM/Qwen appear in marketing/upstream model-access description. Do not claim dedicated GLM/Qwen subscription integration from that text. | No public plan-grouped API-valued allowance aggregate or individual report exposed in inspected README. Local tracking capability alone does not supply a numerator. |
| [SessionWatcher Kimi guide](https://sessionwatcher.com/guides/best-kimi-usage-trackers) | Guide states Kimi usage, limits and costs as provider reports them, with local logs; accepts Kimi Code login, coding key or Moonshot key; Pro Annual/Lifetime include Kimi. | Verified Kimi integration. Page links Qwen tracking guide, but dedicated Qwen page not inspected. | No public crowd aggregate or user measurement ledger in inspected page. Treat app existence as verified; qualifying allowance observations absent from this inspected surface. |

## Chinese-source lead register

[wmpeng/codingplan](https://github.com/wmpeng/codingplan) surfaced with Sep24 search date and description of domestic plan comparison, GLM5.2 and invitation discount. Repository not opened in this bounded pass; no measurement accepted. [QQ News comparative review](https://news.qq.com/rain/a/20260422A0485K00) surfaced as Apr22 story about an engineer using1B tokens/day across7 providers; outside target window and not opened, no numerator accepted. Official Kimi/BigModel quota documentation and generic plan comparisons in the same results were excluded as allowance numerators.

## Limitations and carry-forward

This delta does not revalidate the pre-existing ZAI Lite $102.17/$18 observation or old Kimi Allegretto $7.20-at20% anecdote. Their earlier caveats remain. Search dates proved unreliable twice; exact visible source dates should govern eligibility. No fee denominator is independently mapped for the new candidates because none supplies an eligible numerator. No tokens-only or quota-only claim was converted into API value.

Further useful work would inspect in-window app-issued screenshots or user exports from AIUsage/OpenCode, and exact Kimi plan/variant reports dated Sep7–Oct7. A screenshot must identify the tier, period and pricing basis; a tracker-supported-provider list alone cannot establish measured allowance.
