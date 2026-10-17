# Parent verification and retrieval delta

Date: 2026-10-07. All website inspection used Codex's built-in browser. This document records actual checks, not planned searches.

## Independent omission verification

Read the actual repository files through the read-only `inspection.cjs verify-code` helper. Confirmed both 25-record AA input arrays contain no MiMo/Xiaomi identity; capture iterates only that array, metrics iterate only extraction entries, and scoring iterates only the metrics dictionary. Confirmed the primary cohort requires eligible Bug Hunt and exact AA DeepSWE overlap. The Pareto comparator uses weighted `qualityScore` and normalized `costComposite`. The omission audit's direct implementation conclusion is supported; current external coverage cannot be inferred from absent records.

## Live AA frontier

[AA model comparison](https://artificialanalysis.ai/models), Intelligence Index v4.3.2, observed October 7. Selected **Intelligence Index vs. Total Cost**, whose heading explicitly reads “Intelligence Index vs. Cost to Run Artificial Analysis Intelligence Index.” Added the exact **MiMo-V2.6-Flash** model to the default selected group, producing 25 of 691 selected models. Both exact MiMo labels appeared. Read-only inspection of the rendered SVG showed two Xiaomi orange (`#ff6900`) points at `(186.68751209838456,115.6965212887548)` and `(80.86128454494647,165.7217992977967)`; both coordinate pairs occur as vertices of the chart's rendered Pareto path. This independently confirms both plotted MiMo models lie on the displayed AA total-cost frontier. Coordinates are browser geometry, not monetary or score values. No precision inferred from pixel coordinates and no exhaustive all-691 frontier reconstruction claimed.

## Personal Pro ledger and publication

Directly inspected [maintainer's round-two JSON](https://github.com/FeiZhuLulu/real-api-pricing/blob/main/data/research/mimo-token-plan-panel-round2-2026-09-23.json). It explicitly identifies the maintainer's own **Lite recurring monthly** account, **mimo-v2.6-pro**, collected September 23, usage day September 22, cached input 67,848,448, fresh input 4,479,135, output 1,388,760, total 73,716,343 tokens. Used credits 2,190,625,116; monthly pool 4.1 billion. These are user-reported measurements. Referenced screenshots were not available in the public JSON and account authenticity is not independently verified.

[File history](https://github.com/FeiZhuLulu/real-api-pricing/commits/main/data/research/mimo-token-plan-panel-round2-2026-09-23.json) shows original publication **September 23** in [commit 305af0b](https://github.com/FeiZhuLulu/real-api-pricing/commit/305af0b84eea908d729370fad757a23705d1ffff), then October 2 wording changes in b2e3542. This resolves the publication-date gap: the report is after the September 22 launch. The day's intraday timing is unpublished. The exact newly launched model attribution supports use on launch day, but a precise after-launch timestamp is not established.

[Official launch](https://mimo.xiaomi.com/mimo-v2-6) and [current MiMo home/model pricing](https://mimo.mi.com/) establish Pro API prices in dollars per million tokens: cache $0.0036, fresh input $0.435, output $0.87. These first-party rates value the actual user token numerator; first-party allowance claims are not used.

[Official Token Plan fees](https://platform.xiaomimimo.com/token-plan) show regular monthly Lite $6, Standard $16, Pro $50, Max $100; annual monthly equivalents $5.28/$14.08/$44/$88, and a first-purchase discount. The reporter's actual paid fee or discount is not disclosed. Therefore $3.4008993378 / $6 = 0.5668165563× is a **partial-day consumption comparison against the regular monthly fee**, not an established full monthly allowance multiple or the reporter's actual paid-fee multiple. Full-pool extrapolation (~1.06×) uses a quota fraction and remains outside the accepted actual-use numerator.

## Second client sample: excluded from model-level value

Directly inspected [round-three client JSON](https://github.com/FeiZhuLulu/real-api-pricing/blob/main/data/research/mimo-client-sample-round3-2026-09-23.json). Same maintainer, collected September 23; 35,724,368 tokens over two tasks (cached 33,940,224; input 1,168,949; output 615,195). Client label `mimo/kimi desktop` is explicitly unconfirmed as to exact client/model version; plan tier and paid fee are absent. This is not another independent user and cannot be attributed to exact Pro or Flash. The decision withdrew the 32-row measured-mix extrapolation and returned to standardized workload conversion; it did not retract the original day's measured tokens. Neither set of synthetic quota conversions is admitted as measured allowance.

## Four additional executed search angles and inspected outcomes

1. Google `site:news.ycombinator.com "MiMo" "plan" after:2026-09-22`. Inspected strongest personal trial lead [bscphil comment 49990357](https://news.ycombinator.com/item?id=49990357) in discussion 49984923, October 7: personal V2.6 Pro trial and a coding mistake. **Tier unknown**; no token/API-dollar measurement. Excluded. Other result snippets were not treated as inspected evidence.
2. Google `site:nodeseek.com "MiMo" "Token Plan" after:2026-09-22`. Visible result page explicitly reported no matching documents, including the relaxed unquoted query. This is an indexed-search gap, not proof that NodeSeek contains no reports.
3. Google `site:x.com "MiMo" "token plan" "usage" after:2026-09-22`. Inspected [Jaciezyt September 30 thread](https://x.com/Jaciezyt/status/2104965172205060528) and visible [October 1 reply](https://x.com/qp2sUr0AFZAn7wx/status/2105307221425017210). They discuss subscription/API price differences and MiMo's small discount; **tier unknown**, no actual measured API numerator. Excluded.
4. Google `MiMo token plan usage tracker API cost measurement after:2026-09-22 site:github.com`. Inspected [Tokdash](https://github.com/JingbiaoMei/tokdash): local client logs and bundled API-price database; supports MiMo Code. No public MiMo user/plan allowance ledger established from the inspected README. Other tracker results (CodexBar, token-monitor, ai-usage-widget) are leads only, not independently verified crowd-data sources.

Together with the retrieval agent's five executed searches and Chinese retrieval's three independent search angles, the combined run has **12 executed focused search angles**, plus direct source and author-comment follow-ups. This count does not claim exhaustive Internet coverage.

## Other direct follow-ups

Re-inspected [Reddit Flash/Pro probe](https://www.reddit.com/r/opencode/comments/1wn27ra/mimo_26_flash_vs_pro_latency_mimo_token_plan/) and author's visible replies. Dashboard before/after and OpenCode token reporting are affirmed, but **the author's purchased tier remains unknown**. The all-tier tables price published quotas, not reported consumed API-dollar values. Another commenter Tristsin states a $5 token-plan purchase but offers latency/connectivity observations, no API-priced use. Do not combine commenters into one measurement.

Inspected [linked vendor-price tracker](https://ai-vendor-price-tracking.all-the.rest/de/mimo/): comparison values approximately 0.99×/1.00×/1.10×/1.19×, sourced to Xiaomi price list and OpenCode request-pattern documentation. These are published-credit-pool conversions with estimated request counts, without a personal account measurement. Excluded from actual-use value multiples.

Independently inspected [snmtg1008 October 5 comment](https://github.com/deepseek-ai/deepseek-harness/discussions/8589#discussioncomment-18753426): exact `xiaomi-token-plan-cn`, `mimo-v2.6-pro`, 433 steps/432 calls/48m37s. **Tier unknown**, no monetary/token ledger or paid fee. The Chinese retrieval's exclusion is supported.

## Adversarial critique evidence

- Skeptic: resolve provider quota versus actual-user measurement. The daily Pro ledger is retained as partial consumption; all-tier tables and external tracker projections are excluded.
- Technical reviewer: resolve publication, denominator, double counting, and exact variant. Original September 23 commit and official regular fee verified; paid fee remains unknown. Second-client record has unidentified model and is the same maintainer, so it supplies no independent Pro/Flash observation.
- Decision red team: resolve frontier-axis mismatch and absence-as-rejection mistake. Live AA total-cost frontier checked separately; repository source roster failure independently traced. No full-month allowance inferred, no Flash borrowing, no zero substituted for missing allowance.

Residual limitations: no independently reproduced screenshots/account ledger; no exact intraday launch/sample ordering; no actual paid Lite fee; no measured full-month Xiaomi allowance; no qualified Flash numeric observation; indexed and publicly accessible community coverage only.

Parent additionally re-opened Linux.do 2949201 and V2EX 1245963: the former directly confirms September 25, CommandCode Goat/OpenCode Go, exact Flash and personal 67.54 purchase; the latter directly confirms K3v1Nz's retrospective gifted MiMo Coding Plan experiments without exact dates/model/tier or API-valued use. Their exclusion descriptions are supported by the primary pages.
