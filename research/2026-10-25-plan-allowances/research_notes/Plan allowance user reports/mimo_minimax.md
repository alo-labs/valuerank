# Plan allowance user reports: Xiaomi MiMo Token Plan and MiniMax M Plan (stage 2 sweep, 2026-10-25)

Scope: new end-user reports not already in `stage1-mimo.md`, `stage1-deepseek-minimax.md` or
`research/2026-10-23-mimo-token-plans/`. Window 2026-09-25 to 2026-10-25 (older labelled).
Prices per 1M tokens: MiMo-V2.6-Pro $0.0036 cache hit / $0.435 miss / $0.87 output; MiniMax-M3.1-Flash $0.015 cache
read / $0.15 input / $0.60 output.

Method and coverage. Arctic Shift Reddit archive (comment search by subreddit and keyword, 2026-09-25 to
2026-10-24T04:47Z, about 950 unique comments from r/opencode, r/opencodeCLI, r/MiniMax_AI, r/hermesagent,
r/openclaw, r/LocalLLaMA, r/CLine, r/ChatGPTCoding, r/vibecoding; r/MiniMax_AI posts since 2026-10-10); r/MiniMax_AI
comments RSS (to 2026-10-25T12:23Z); MiniMax docs (m-plan intro, faq, usage-rules, token-plan-notice, release notes);
codingplan.fyi / wmpeng/codingplan; mahonzhan/awesome-coding-plan; web search (English and Chinese).
Unreachable: GitHub search (REST search is blocked for this session; GraphQL 403), linux.do (Cloudflare challenge),
HN Algolia (returned non-JSON), Arctic Shift for r/LocalLLaMA / r/ClaudeCode keyword "mimo" (empty or rate-limited),
Zhihu / Xiaohongshu / Bilibili not attempted after stage-1 failures. Result: no new qualifying report for either
provider. The sweep did turn up a few weak or near-miss items, a community estimate table, and evidence on the
allowance change after M3.1-Flash GA.

## MiMo: new V2.6-Pro / V2.6-Flash reports, and do users confirm the Credits-per-token table?

### Takeaway
No new qualifying MiMo report was found. No in-window user gives model, tier, date and typed tokens or Credits against
the monthly meter beyond the two stage-1 items: TheVoyant (Max, one day) and AppleHuman8535 (Lite, weak). V2.6-Flash
still has zero first-party plan reports. No new user independently confirms the Credits-per-token table. The only
user-side checks are still ConsiderationNo9952 (2026-09) and TheVoyant's ledger, both already recorded.

### Cited Findings
- Near miss, already in stage 1: Houssein_ (r/openclaw, 2026-10-14 03:27Z): "I got the same token plan yesterday, and
  by day two, I've already used 29% of my allowance (around 3–4 billion tokens), even though I'm using the cheapest
  model." The tier is not named (stage 1 inferred Standard), the model is "the cheapest" (probably V2.6-Flash), and
  "3–4 billion" reads as Credits rather than tokens: 29% of 11B is 3.19B. Not priceable without a model and token
  split — [Reddit](https://www.reddit.com/r/openclaw/comments/1u2wdo4/comment/pgmbow6/)
- Reseller, not first-party: Lap202pro (r/opencode, 2026-10-19): "Have been using Mimo-v2.6-pro and have gotten a ton
  of stuff done the past 3 days for like 16% usage". This is OpenCode Go's meter, not Xiaomi's —
  [Reddit](https://www.reddit.com/r/opencode/comments/1x9yov3/comment/phpi8rc/)
- Reseller, not first-party: OpenCode Go users report a per-model dollar cap. Sparrowy (2026-10-05): "Mimo-V6-Pro has
  $15 limit". VickWildman (same day): "Mimo 2.6 Pro only allows $15, you have used more than 50% of that and
  therefore more than 50% of your monthly allowance." This describes OpenCode Go ($10 per month), not the Xiaomi
  Token Plan, so it does not count for MiMo tiers —
  [Reddit](https://www.reddit.com/r/opencode/comments/1wy907r/comment/pe0owbv/)
- Directional, no numbers: Ok-Satisfaction-5236 (r/opencodeCLI, 2026-10-01, $16 Standard): "The amount of usage I got
  with MiMo 2.5 was fantastic with the $16 plan … MiMo 2.6 is unusable right now" —
  [Reddit](https://www.reddit.com/r/opencodeCLI/comments/1wughtd/comment/pdan6uq/)
- Directional, Flash on the first-party plan, no numbers: Winter-Bit2411 (r/opencode, 2026-09-27): "I gave a try to
  MiMo 2.6 Flash using their token plan (official API) and I did not feel I should ever get back using it." —
  [Reddit](https://www.reddit.com/r/opencode/comments/1wroplu/comment/pcec113/)
- Older, V2.5 era (out of window, not verified beyond the search snippet): 80aj.com, 2026-09-04, "小米 token plan
  实测：34元 Lite 套餐用 Pro 模型两天耗掉一半额度" (Lite, Pro model, half the quota in two days) —
  [80aj.com](https://www.80aj.com/2026/09/04/xiaomi-token-lite-pro-test/)
- Official terms re-checked (unchanged): Lite / Standard / Pro / Max = 41亿 / 110亿 / 380亿 / 820亿 Credits a month.
  mimo-v2.6-pro costs 2.5 / 300 / 600 Credits per cache-hit, cache-miss and output token. Beijing 00:00–08:00 burns
  at 0.8× — [MiMo Token Plan (zh-CN)](https://mimo.mi.com/docs/zh-CN/price/token-plan);
  [codingplan.org summary](https://codingplan.org/plans/xiaomi)
- Aggregator, no measurement: codingplan.fyi lists MiMo as "MiMo文本Credits订阅，当前2个LLM，夜间00–08点UTC+8享0.8消耗"
  and gives no MiMo token estimates —
  [wmpeng/codingplan README](https://github.com/wmpeng/codingplan)

### Inferences
- The MiMo cells in the assessment stay as they were after stage 1. V2.6-Pro on Max has one report (TheVoyant, about
  $80–105 per month extrapolated from one day). V2.6-Pro on Lite has one weak report (about $4.60). Every other
  tier, and V2.6-Flash on every tier, has none. No cell reaches two reports.
- The Credits peg is arithmetic on Xiaomi's own tables (1B Credits ≈ $1.45 of V2.6-Pro). Every priceable fragment
  sits at or below the quota ceiling. The ceiling ($5.95 / $15.95 / $55.10 / $118.90 per month at peak, all Pro) is a
  provider claim, and it is a stronger basis than any concordance test the sparse user data could support.

### Gaps
- No dashboard screenshot with tokens and % of monthly Credits for Standard or Pro on V2.6-Pro was found in the
  reachable sources. The likely places are V2EX, linux.do and GitHub issues of XiaomiMiMo/MiMo-Code, which could not
  be searched in this session (linux.do is behind Cloudflare; GitHub search is blocked).
- No V2.6-Flash plan report exists in any reachable source. Users who try Flash on the plan describe quality, not
  quantity.

## MiniMax: reports on named M Plan tiers (Go / Explore / Build) for M3.1-Flash after GA, and did MiniMax change the allowance?

### Takeaway
No qualifying post-GA report on a named M Plan tier was found. Post-GA comments come from legacy Token Plan holders
and give times to exhaustion ("5-hour limit in ~30 minutes"), not tokens. One new weak pre-GA item exists
(ConsiderationNo9952: "lite ~1+B/wk"). A community aggregator publishes model-specific estimates per tier, but they are
derived from samples and assumptions, not reported by users. MiniMax's docs show no change to M Plan allowances after
GA. The effective change users felt came from M2.5/M2.7 traffic being rerouted to M3.1-Flash on 2026-10-19, and from
legacy Token Plan auto-renewals being switched off.

### Cited Findings
- New weak report, pre-GA (model probably M3 or M3.1-Flash-Preview, not stated): ConsiderationNo9952 (r/opencode,
  2026-10-17 08:09Z): "i find minimax - lite ~1+B/wk, and the multipliers of the other plans seem be proportional to
  that". The tier name "lite" is not a MiniMax tier name (legacy tiers were Plus/Max/Ultra, plus a $10 Starter), so
  it most likely means the lowest tier. No cache split or meter percentage is given —
  [Reddit](https://www.reddit.com/r/opencode/comments/1x7wata/comment/ph9n1m4/)
  - Priced at M3.1-Flash rates for 1.0B tokens: 97% cache / 2.5% miss / 0.5% output ≈ $21.3; 95 / 4.5 / 0.5 ≈ $24.0;
    90 / 9 / 1 ≈ $33.0 → **≈ $21–33 per week** (lower bound, "1+B").
- Post-GA, legacy plan, no token count: Ok_Bug1610 (r/MiniMax_AI, 2026-10-20), on a "$200/year MiniMax Token Plan":
  "MiniMax M2.5 and M2.7 now get routed to MiniMax-M3.1-Flash as of 10/19 and it eats through my 5-hour limits in ~30
  minutes". Before that: "I averaged just under ~1 billion tokens per day (~80% cache) and on average I didn't even hit
  my 5-hour or weekly limits" on M2.7, "because it allowed literally 20x the quota" —
  [Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1x6p4d6/comment/19re6xfrt9bwl/);
  [Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1xag1vb/comment/phx3vou/)
- Post-GA, legacy "$10 plan", percent and time only: vaughnwilliams (r/MiniMax_AI, 2026-10-20): "m3.1 flash … 70% of
  the 5 hour allowance gone in an hour, using m2.7 for the same tasks id have used maybe 10% at most" —
  [Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1x8z12w/comment/phudhfb/)
- Post-GA, legacy plan: NinjaWK (2026-10-20): "Burned through 5 hours limit in under 1 hour, from my existing M2.7
  setting, which got routed to M3.1-Flash". He also said his legacy plan had, "with M3 migration 15x weekly quota
  instead of 10x 5 hours" — [Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1x6p4d6/comment/phx5smm/);
  [Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1x6p4d6/comment/19reiic2noebm/)
- Post-GA, "$20 subscription" (probably Go at $22 or the legacy Plus), count only: No_Monk_4905 (r/MiniMax_AI post,
  2026-10-20): "my $20 subscription reached the 5 hours limit 3 times today". He added on 10-24: "the new version 3.1
  flash is using more tokens than normal" —
  [Reddit post 1xag1vb](https://www.reddit.com/r/MiniMax_AI/comments/1xag1vb/);
  [RSS comment](https://www.reddit.com/r/MiniMax_AI/comments/1xed4rt/minimax_hermes_unendliches_denken/19rldfz3g4gx0/)
- Post-GA, provider figure repeated, not a measurement: dark_bits (r/LocalLLaMA, 2026-10-19): "the token plan for
  minimax has a limit of 1.7B tokens per month for only $24 (or at least it used to be back then)" —
  [Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x9uzv9/comment/phsairs/)
- Pre-GA tier comparison, no numbers: brocolongo (2026-10-12), after upgrading from legacy Plus to Explore: "I feel plus
  has the same token usage as explore and also I used to have unlimited weekly, now after upgrading is not unlimited
  anymore" — [Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1x41frf/comment/pfi1z6u/)
- Community estimate, not a user report: codingplan.fyi (page updated 2026-10-21; repo README dated 2026-10-24) gives
  "正式M3.1 Flash" (the GA M3.1 Flash) per 5h / week / month as Go 44.44M / 444.36M / 1,777.4M, Explore 133.31M /
  1,333.08M / 5,332.3M, and Build 533.23M / 5,332.3M / 21,329.2M tokens. Its stated method: "社区样本推算，按输入缓存
  命中率 95%、输出占全部 Token 的 0.5%计算；Go 五小时约 4,444 万 Token，Explore、Build 分别按 Go 的 3 倍、12 倍估算。周参考量按
  五小时的 10 倍". It also says the weights "新增输入、输出、缓存读取按 1、4、0.2" are "不是官方公布的订阅扣减规则" —
  [codingplan.fyi MiniMax](https://codingplan.fyi/platforms/minimax/);
  [wmpeng/codingplan](https://github.com/wmpeng/codingplan)
  - Priced at M3.1-Flash rates with its own mix (95% cache, 4.5% miss, 0.5% output): Go ≈ $1.07 per 5h, ≈ $10.7 per
    week; Explore ≈ $3.20 per 5h, ≈ $32 per week; Build (12×, the CN multiple) ≈ $12.8 per 5h, ≈ $128 per week. At
    the international 7.5× for Build: ≈ $8.0 per 5h, ≈ $80 per week. These numbers are derived. They are not
    independent measurements.
- Promotion that clouds post-GA measurement: "截至 2026-10-25，所有订阅用户在 MiniMax Code 内使用 M3.1 Flash
  不限量。该活动不包含 Code Free，也未承诺外部工具 API 不限量" —
  [codingplan.fyi](https://codingplan.fyi/platforms/minimax/). A user confirms it: eggplantpot (2026-10-19): "Unsure on
  cost since I have the unlimited offer" — [Reddit post 1xa5xo2](https://www.reddit.com/r/MiniMax_AI/comments/1xa5xo2/).
  There is also a first-month half-price offer (Go / Explore / Build ¥24.5 / ¥59.5 / ¥234.5) until 2026-10-31 —
  [wmpeng/codingplan](https://github.com/wmpeng/codingplan)
- Official docs (read 2026-10-25): M Plan publishes only the multiples (Go 1x, Explore 3x, Build 7.5x international)
  and the windows ("the 5-hour window lasts 5 hours, and the weekly window lasts 7 days … The two windows reset
  independently"). "MiniMax-M3.1-Flash-Preview has been retired. Requests using the old name are now served by
  MiniMax-M3.1-Flash." No absolute allowance is given and no post-GA allowance change is announced. Release notes list
  only "Oct. 19, 2026 MiniMax M3.1 Flash" —
  [M Plan overview](https://platform.minimax.io/docs/m-plan/intro); [FAQ](https://platform.minimax.io/docs/m-plan/faq);
  [Usage](https://platform.minimax.io/docs/m-plan/usage-rules);
  [Release notes](https://platform.minimax.io/docs/release-notes/models.md)
- Legacy Token Plan terms: keeping the plan keeps "historical Token Plan discounts and additional benefits (such as ∞
  limits and 150% weekly limit)" as long as auto-renewal stays on; upgrading drops them —
  [Existing Token Plan subscribers](https://platform.minimax.io/docs/m-plan/token-plan-notice). Maddy186 (2026-10-23)
  says the legacy $10 plan was "cancelled … without notice"
  ([Reddit post 1xdh3dp](https://www.reddit.com/r/MiniMax_AI/comments/1xdh3dp/)). basil_0408 (10-24) replied: "They
  did turn off auto-renewal after the new plan dropped and sent an email to let u know"
  ([Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1xdh3dp/minimax_cancelled_my_legacy_token_plan_without/19rkf0fp0bhya/))
- Post-GA routing complaint: pblocz (2026-10-25) says M3 requests seem routed to M3.1 Flash, and the plans page "only
  mentions M3.1 Flash now" —
  [Reddit](https://www.reddit.com/r/MiniMax_AI/comments/1xds9sd/m3_from_minimax_doesnt_sound_like_m3_anymore_did/19rmrlnxvo15s/)

### Inferences
- Nothing published shows MiniMax changing M Plan allowances at or after GA. The jump in burn rate users report after
  2026-10-19 is explained by the forced move from M2.5/M2.7, which users say had about 20× the quota per token, to
  M3.1-Flash. The new model's heavier thinking adds to it. That is a change in model mix, not a documented quota cut.
  It cannot be ruled out that the per-token deduction for M3.1-Flash (GA) differs from the Preview's, because MiniMax
  does not publish deduction weights.
- Post-GA measurement is also distorted by the MiniMax Code unlimited promotion, which runs to 2026-10-25 and covers
  the client only, and by the first-month half-price offer. Reports dated 2026-10-19..25 from inside MiniMax Code are
  not meter-bound.
- codingplan.fyi's Go figure (≈ $1.07 per 5h, ≈ $10.7 per week) can be set against the legacy Token Plan reports from
  stage 1. R2 was the lowest legacy tier at ≈ $3.5–13.5 per 5h; R1 was legacy Max at ≈ $5.7–9.8 per 5h. The
  aggregator is several times lower per window than those, but the tiers differ (legacy Plus or Max versus new Go).
  The aggregator's "weekly = 10 × 5h" also conflicts with NinjaWK's legacy "15x weekly". Neither can be used for a
  concordance test.

### Gaps
- No report for a named Go, Explore or Build tier after 2026-10-19 gives tokens (typed or totals) against a percentage
  of the 5-hour or weekly window. Most post-GA posters are legacy Token Plan holders.
- No official statement exists on M3.1-Flash deduction weights or on any GA-time change to them. The CN multiple for
  Build (12×) versus the international one (7.5×) remains a regional difference, not a change.

## Summary table: model × tier → qualifying reports (normalised at API list price)

| Model | Tier | Qualifying reports (this sweep + stage 1) | Normalised value | ≥2 within 20%? |
|---|---|---|---|---|
| MiMo-V2.6-Pro | Lite ($6) | AppleHuman8535 (weak, stage 1) | ≈ $4.60 per period | No (1) |
| MiMo-V2.6-Pro | Standard ($16) | none (Houssein_ near miss: 29% ≈ 3.2B Credits, model probably Flash) | — | No (0) |
| MiMo-V2.6-Pro | Pro ($50) | none | — | No (0) |
| MiMo-V2.6-Pro | Max ($100) | TheVoyant one-day ledger (stage 1) | ≈ $80–105 per month (extrapolated) | No (1) |
| MiMo-V2.6-Flash | all tiers | none | — | No (0) |
| MiniMax-M3.1-Flash (GA) | M Plan Go ($22) | none. Estimate only: codingplan.fyi ≈ $1.07 per 5h / ≈ $10.7 per week (not a user report) | — | No (0) |
| MiniMax-M3.1-Flash (GA) | M Plan Explore ($55) | none. Estimate only: ≈ $3.2 per 5h / ≈ $32 per week | — | No (0) |
| MiniMax-M3.1-Flash (GA) | M Plan Build ($132) | none. Estimate only: ≈ $8–12.8 per 5h / ≈ $80–128 per week (7.5× or 12×) | — | No (0) |
| MiniMax-M3.1-Flash(-Preview) | legacy Token Plan, lowest tier | stage-1 R2 (≈ $3.5–13.5 per 5h); new weak ConsiderationNo9952 (≥ ≈ $21–33 per week, model unstated) | windows differ (5h versus week) | No |
| MiniMax-M3.1-Flash(-Preview) | legacy Token Plan Max | stage-1 R1 (≈ $5.7–9.8 per 5h), R3 (≈ $60–127 per week) | windows differ | No |

Bottom line: no MiMo or MiniMax model × tier reaches two independent reports agreeing within 20%. The sweep added no
qualifying report.
