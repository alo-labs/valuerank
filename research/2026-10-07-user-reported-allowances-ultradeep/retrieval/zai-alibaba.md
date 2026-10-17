# Z.AI / Alibaba-Qwen current-window user-measurement search

## Scope

- Report-date window: **2026-09-07 through 2026-10-07 inclusive**.
- Ranked variants, checked against the current authoritative [model roster](/Users/shafqat/valuerank/research/2026-10-06-value-multiples/roster-coverage/model-coverage.csv):
  - GLM-5.3 — ValueRank model ID `glm-5.3`.
  - Qwen3.8 Max — ValueRank model ID `qwen3.8-max`.

The search is for personal end-user usage measured and valued at API rates. Provider-published quotas, caps, and marketing claims do not supply the numerator.

## Parent-inspected GLM Max post: strong near miss

The parent inspected the Reddit post [“Burning through 2.5+ billion tokens daily of glm-5.3[1m] on GLM Max plan”](https://www.reddit.com/r/ZaiGLM/comments/1wpnomp/burning_through_25_billion_tokens_daily_of/), shown as 12 days old.

- Its screenshot reports usage for **2026-09-24–2026-09-26**: 2.66B total tokens, including 2.55B GLM-5.3 and 103.37M GLM-5.3 Flash.
- The caption says 600–700M tokens were used before a five-hour window reached 100%, with about five such windows in a day.
- The OP identifies an active legacy GLM Max yearly plan costing $288/year, bought the previous Christmas.
- **Strong measured-usage near miss; no Value Multiple.** There are no input/output/cache token splits or user API-priced cost, and the usage combines GLM-5.3 with GLM-5.3 Flash. An exact ranked GLM-5.3 numerator cannot be reconstructed.
- The screenshot interval is 2026-09-24–26, not a whole-last-month measurement.

## Parent-inspected Z.ai Coding Plan Lite report: provider/plan-level evidence

The parent opened the Reddit report by `dontWORRYimASIAN` at the [direct post link](https://www.reddit.com/r/ZaiGLM/comments/1wstrqy/lite_plan_18mo_gave_me_102_of_api_usage_568x_a_1/). It displayed **8 days old on 2026-10-07**, approximately 2026-09-29, so the report date is within the window. This source was supplied and inspected by the parent; it was not found or opened in this child run.

- The author reports Z.ai Coding Plan Lite at **$18/month**, subscribed approximately one month earlier.
- The screenshot interval is **2026-08-29–2026-09-29** and reports 637.8M tokens, 44.5K plan credits, 9,047 calls, and a 90.7% input-cache-hit rate. The interval straddles the 2026-09-07 measurement cutoff.
- The author estimates about **$102.17 in API-priced usage** and says they first used GLM-5.3 Flash heavily, then transitioned to GLM-5.3. No per-model usage or API-priced split is given.
- **Eligible as a user-reported provider/plan-level measurement because the report date is in-window.** The arithmetic $102.17 / $18 = **5.68×** describes the author's reported API-price estimate relative to the stated fee; the token-price calculation is not independently reproducible from the post.
- Do not apply 5.68× to the ranked GLM-5.3 row: the reported use mixes GLM-5.3 Flash and GLM-5.3 and lacks per-model token splits. The usage interval also includes dates before the rolling cutoff, so it is not a fully in-window measurement.
- This is the screenshot's 2026-08-29–2026-09-29 interval, not the whole last month.


## Parent-inspected Reddit near misses: new Coding Plans and GLM comparisons

### New Coding Plans versus legacy v1

The parent inspected [this Reddit discussion](https://www.reddit.com/r/ZaiGLM/comments/1wx4xag/how_do_new_coding_plans_compare_to_legacy_v1/), shown as **3 days old on 2026-10-07** (approximately 2026-10-04). It was not found or opened in this child run.

- The OP claims legacy Max v1 usage above 50B tokens/month. A commenter claims the new Max quota is 4B/week or 16B/month and estimates FlashX at 2.5×. These are allowance/quota or value claims, not API-priced measurements of personal usage; they are excluded from the numerator.
- A Pro commenter reports approximate personal use of **700M GLM-5.3 tokens plus 120M GLM-5.3 Flash tokens that week**, with 20% of the allowance remaining. This is a measured-usage report, but gives no API-priced dollar total or matched plan-fee evidence, so it does not support a Value Multiple. The model use is mixed and cannot be assigned to the exact ranked GLM-5.3 row.

### Opus 5.5 versus GLM 5.3

The parent inspected [this Reddit discussion](https://www.reddit.com/r/ZaiGLM/comments/1wwfs66/opus_55_vs_glm_53/), shown as **4 days old on 2026-10-07** (approximately 2026-10-03). It was not found or opened in this child run.

- The thread includes API-equivalence claims such as $500+, $8,000–$10,000, and $300 on an $18 plan.
- These are unsubstantiated or secondary claims in the discussion, not the post author's own measured subscription use priced at API rates. They are excluded from the numerator.


## Browser blocker for this child search

The CUA inventory listed browser ID `4` as `Codex In-app Browser` (type `iab`), but both browser selections failed:

- `cua.getBrowser({id:"4"})` → `Browser is not available: 4`.
- `cua.getBrowser({id:"iab"})` → `Browser is not available: iab`.

The browser could not be bound, so no search page was opened. No fallback browser or search method was used.

## Exact query status

| Source order | Exact query status in this child run | Inspection result |
|---|---|---|
| Reddit, first | No query submitted. | No posts inspected by this child run. |
| Hacker News | Not reached; no query submitted. | No posts inspected by this child run. |
| Relevant developer communities | Not reached; no query submitted. | No discussions inspected by this child run. |

## Qualification status

Only the Coding Plan Lite report supports a **reported provider/plan-level 5.68× estimate**, eligible by report date but limited by its cutoff-straddling interval and unreproduced API-price estimate. None of the other parent-inspected threads supports a model-specific API-priced numerator matched to a plan fee: the GLM Max and Pro-comment reports lack priced value or fee evidence, while new-plan allowance and API-equivalence claims are excluded. No Qwen3.8 Max result was assessed.
