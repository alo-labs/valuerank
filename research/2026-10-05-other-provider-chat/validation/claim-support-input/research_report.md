# Other-provider AI chat allowances and trackers

**Research date:** 2026-10-05 (UTC)  
**Community report publication window:** 2026-09-05 through 2026-10-05, inclusive.  
**Scope:** consumer chat subscription plans for Perplexity, xAI/Grok, Mistral Le Chat, DeepSeek, Poe, Meta AI, the Gemini app, and standard ChatGPT chat. ChatGPT Work/Codex, Gemini CLI/Antigravity, other coding surfaces, and API billing are kept out of the chat-plan comparison.

## Executive summary

The inspected policies expose different kinds of allowance. Perplexity publishes fixed daily limits for free users while paid search/research allowances are described qualitatively [1]. Mistral lists 150 Flash answers/day for Pro and 200/day for Team [3]. xAI describes a shared paid-product weekly pool but no absolute prompt count [4]. Poe uses plan-dependent points and an account usage history [5][6]. Meta One advertises expanded AI access without a fixed amount [7]. The inspected DeepSeek chat page presents its assistant as free [8], while API pricing is separate [9]. Gemini uses plan- and workload-dependent consumer-app limits with a first-party Usage Limits screen [10]. OpenAI says ChatGPT limits vary by plan/model/system conditions and shows reset details when available [11][12].

The bounded search found first-party account meters, a third-party account-reader claim, local estimates, and a separate Codex-only community tracker, but no normalized crowdsourced dataset for consumer chat plans. AI Usage Limit Alerts claims signed-in account reads [31]; AIRadar labels ChatGPT/Gemini counters as stream-based local estimates [30]. TiboTattle advertises a Codex community view, but its homepage showed no current numeric aggregate; no Codex quota values are reported [33]. These classes are kept separate.

Prior passes retained 14 in-window discussion leads across six providers, including coding/API and product-surface-ambiguous reports that do not count as consumer-chat allowance measurements. The extension adds four in-window user reports/comments: two ChatGPT Plus reports (one surface ambiguous, one image-generation-specific) and two Gemini app reports (one plan not stated, one commenter explicitly on Google AI Pro). Each report carries only the tier stated by that author; otherwise it says “not stated.” No post supplies a normalized, representative cross-user allowance estimate. See [`community-research-addendum.md`](community-research-addendum.md), the supplemental source/evidence/claim registries, and [`community-query-log-addendum.md`](community-query-log-addendum.md). This is not proof that no other report exists.

## Introduction and method

The purpose was to identify publicly measurable consumer-chat allowances and account-level or crowd-sourced trackers outside the Claude workstream and coding-tool research. The provider set is the eight services named above, including eligible paid plans where present. ChatGPT means standard Chat only; Gemini means the consumer Gemini app. Official policy statements, product-discovery pages, API policies, tracker descriptions, and user reports are kept in separate evidence classes.

Search, open and find work used Codex built-in `web__run`; no Edge, Chrome or CUA research was used. The retrieval sequence prioritized current official plan/help pages, searched Reddit first for recent user evidence, then inspected Hacker News, developer communities, GitHub and tracker sites. Publication date and measured interval are distinct. Only community reports dated 2026-09-05 through 2026-10-05 could qualify; an older or inseparably mixed-window report cannot support a current allowance estimate. Official policy pages are policy context, not observed user measurements. API rate limits are not attributed to consumer chat subscriptions. Plan, model, region, method, sample size, reset interval and date are recorded only when stated by the inspected source.

The Silver Bullet Deep Research skill, 9-phase methodology and quality-gates references were read through the `silver-bullet` LeanCTX repository alias. This supplement applies the Ultradeep phase contract manually and records scope, plan, retrieval, triangulation, outline, synthesis, three critique/refinement checks, package decisions and validation evidence in `phase-evidence.md`. No Silver Bullet runtime/orchestrator invocation was made, so this is workflow-guided research, not a runtime-executed SB run. The bounded web searches do not exhaust private, deleted, regional, login-gated or unindexed material.

The initial 2026-10-05 CUA follow-up could not open the built-in browser (`iab`), and the proposed query strings in `query_log.md` are accurately marked **not executed during that attempt**. The primary agent later executed an expanded provider-specific search through Codex's built-in web research route, without using an external browser. Its exact queries, results, and date-filtered observations are recorded in the linked current-month addendum. The research remains bounded to indexed public material.

## Main Analysis

### Findings

### Perplexity: visible fixed free limits, flexible paid search allowances

The official plan comparison page, modified 2026-10-02, states 3 Pro Searches/day and 1 Research query/month on Standard (free). For consumer Pro and Max it describes weekly Pro Search and monthly Research limits qualitatively, not as fixed public counts; Enterprise counts do not transfer to consumer subscriptions. Computer credits use a separate meter and accounting system, and task-dependent burn prevents conversion to chat-message counts. [C-PER-1, C-PER-2, C-PER-3] [1] [2]

### Mistral Le Chat: a numeric Flash-answer allowance

Mistral’s pricing page says Pro includes 150 Flash answers/day and Team 200/day and gives relative multipliers for other actions without baseline counts. These are policy statements, not observed usage tests or a general message-equivalent. API and workspace limits are separate from Le Chat subscription limits. [C-MIS-1] [3]

### Grok: first-party weekly meter, no public absolute pool size

xAI’s consumer FAQ says paid products share a weekly pool across Chat, Imagine, Voice, Build and API, with differing compute weights; the account Usage tab shows percentage, product breakdown and reset information. The FAQ does not publish an absolute pool size or dependable messages/week conversion. This is a personal provider meter, not a public numeric quota. The FAQ was last updated 2026-08-27; community cutoff rules do not apply to provider-policy publication dates. [C-XAI-1] [4]

### Poe: points are observable per account; paid allotment varies

Poe help describes daily and/or monthly point schedules by plan, expiration/add-on rules, account balance and history. Bot/model actions consume differing points; no universal paid subscriber allocation is established. The separate usage API provides authenticated per-account history [5] [6].

### Meta AI and DeepSeek: no public numeric consumer-chat allowance in inspected material

Meta’s September 2026 Meta One announcement says paid bundles increase access to compute-intensive AI features but states no numeric allowance. DeepSeek’s public chat page presents its assistant as free; no paid consumer tier or quota policy was identified in the inspected pages. DeepSeek API pricing is excluded from chat-plan conclusions. [C-META-1, C-DS-1] [7] [8] [9]

### Gemini app and standard ChatGPT: first-party meters, variable limits

Google says Gemini app limits depend on prompt complexity, model/features and chat length, with plan-relative access and near-limit/reset notices in the app's Usage Limits screen. The policy does not state one universal prompt count. Two recent Reddit reports add individual experiences: the Sep 13 trip-planning poster's tier is not stated, while a Sep 9 commenter explicitly says Google AI Pro and reports first hitting a limit during keyboard research; neither supplies a count or controlled window. [Gemini Apps limits](https://support.google.com/gemini/answer/16275805) [10], [Sep 13 report](https://www.reddit.com/r/GeminiAI/comments/1wfhxlh/have_the_limits_lowered_yet_again/) [26], [Sep 9 comment thread](https://www.reddit.com/r/GeminiAI/comments/1wb5d55/what_is_up_with_the_limits_all_of_a_sudden/) [27]

OpenAI says ChatGPT Plus can have message caps that vary with system conditions; limits may depend on plan and model, and reset details appear in the account interface when available. One Sep 18 user explicitly says Plus but the product surface displaying the consumed limit is unclear, so the post is not treated as standard-chat evidence. A Sep 29 Plus user reports hitting an image-generation limit but provides no count/window; it is feature-specific. Neither establishes a text-chat allowance. [ChatGPT Plus limits](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) [11], [model limits and reset UI](https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt) [12], [Sep 18 report](https://www.reddit.com/r/ChatGPT/comments/1wjqvt0/usage_limits_are-insanely-low_now/) [28], [Sep 29 image report](https://www.reddit.com/r/ChatGPT/comments/1wtmoeo/first-time-hitting-the-image-generation-limit-on/) [29]

### Tracker landscape and recent community reports

Tracker discovery separates first-party provider meters, a third-party account-reader claim, local estimates, API spend dashboards and crowdsourced reports. The AI Usage Limit Alerts listing claims to read signed-in provider usage/reset data [31]. AIRadar labels ChatGPT/Gemini figures as local estimates from streamed replies [30]. OpenUsage focuses local spend/API/coding data [32]. TiboTattle’s homepage advertises optional Codex community reports and local history but showed no current aggregate [33]. No normalized consumer-chat crowd dataset was verified. Details and limitations are recorded in the [community addendum](community-research-addendum.md).

Across the prior in-window posts, the three Perplexity authors identify Pro [13] [14] [15]; Grok reports identify SuperGrok or Ultra except the `nomilk` commenter whose plan is not stated [16] [17] [18] [19]. Mistral Vibe coding is out of scope but preserves Edu Pro yearly, Pro, and Team statements; remaining commenter tiers are not stated [20]. The Sep 26 Poe author states only £20/month, so tier is not stated; the Oct 2 author states Poe Plus [23][24]. The Meta author’s plan is not stated [25]. Other current leads include a DeepSeek poster with plan not stated [22], a Mistral free-tier comment with unclear product surface [21], and a SuperGrok HN anecdote [19]. The ChatGPT authors state Plus (one surface-ambiguous, one image-generation-specific) [28][29]. The Gemini trip-planning poster’s tier is not stated; a separate commenter states Google AI Pro [26][27]. None gives a normalized representative count. The evidence log preserves each tier and excludes Vibe coding, DeepSeek API spend, Grok Build coding, Gemini CLI/Antigravity and ChatGPT Work/Codex from consumer-chat estimates. See the [post-by-post addendum](community-research-addendum.md).

## Synthesis

Across these providers, “allowance” may mean searches, answers, points, a shared compute pool, credits, a compute-based window or a qualitative increase over free access. A single messages/month comparison would erase these differences and fabricate precision. The strongest numeric policies in this set are feature-specific counts for Mistral Flash and Perplexity free search/research; Grok, Gemini and ChatGPT expose plan/model-dependent usage without one transferable count. Poe uses account-level points by plan, while inspected Meta/DeepSeek pages do not establish a public numeric paid-chat cap. [1] [3] [4] [5] [10] [11] [12]

## Counterevidence Register

| Claim at risk | Competing evidence or alternative explanation | Resolution |
|---|---|---|
| Perplexity paid users exhausted ordinary chat/search allowance | In the Sep 7 thread, commenters suspect Computer mode; other posts concern Computer credits and add-on purchases rather than included Search/Research. | Preserve feature ambiguity and separate Computer credits; do not infer a Pro Search cap. [13] [14] [15] |
| Grok users have a stable message allowance | SuperGrok and Ultra account reports differ; the HN thread mixes app questions, voice, media and Build coding, and one commenter has no stated tier. | Keep each reporter’s tier/action attached; exclude Build coding and avoid a transferable count. [16] [17] [18] [19] |
| Mistral Vibe meter is a Le Chat allowance | The detailed Vibe thread is coding-only, while the pricing page lists separate API credits; a free-tier comment does not identify a chat surface. | Exclude coding amounts from Le Chat; retain the free-tier comment as ambiguous and qualitative. [3] [20] [21] |
| DeepSeek has a measured consumer-chat cap | One poster alleges 7 messages/15 minutes and 3 edits/regenerations, but plan/model/account conditions are missing and replies dispute it. | Label plan “not stated”; retain as qualitative only. [22] |
| Poe has one universal current paid allotment | The £20/month author does not state a plan name; the separate Poe Plus author reports daily/monthly points and bought add-ons. | Keep reports separate and do not map price to plan or add-ons to included points. [23] [24] |
| Meta AI image quota indicates a Meta One limit | Original poster’s plan is not stated; replies mix free and paid references. | Do not assign a paid tier or infer a Meta One numeric limit. [25] |
| Gemini “Pro plan” is the Sep 13 poster's tier | The image alt text mentions Pro but is not clearly linked to the author’s account; a separate commenter explicitly states Google AI Pro. | Keep the first tier “not stated”; attribute AI Pro only to the Sep 9 commenter. [26] [27] |
| ChatGPT Plus reports quantify standard text chat | The Sep 18 post does not identify the surface; the Sep 29 report is image-generation-specific. | Treat both as feature/surface anecdotes, not standard chat measurements. [28] [29] |
| Tracker output is equivalent to provider quota | AIRadar labels ChatGPT/Gemini values as estimates; the extension is a listing claim; TiboTattle's homepage showed no current aggregate. | Keep first-party meter, third-party reader, local estimate and crowd-report classes separate; note unverified implementation claims. [30] [31] [33] |

## Claims-Evidence Table

| Claim ID | Claim | Evidence IDs | Status/use |
|---|---|---|---|
| C-PER-1, C-PER-2, C-PER-3 | Perplexity's free counts and paid qualitative limits; Computer credit pool is separate. | E-PER-1, E-PER-2, E-PER-3; O-E01–04 | Provider policy plus distinct user reports; no normalized paid allowance. |
| C-MIS-1 | Mistral Flash answer counts are provider-stated feature limits. | E-MIS-1; O-E09 | Policy context; Vibe posts are coding-only. |
| C-XAI-1 / O-C02 | Grok has a shared weekly pool, but user outcomes do not define a universal quantity. | E-XAI-1; O-E05–08 | First-party meter/policy plus qualitative anecdotes. |
| C-POE-1, C-POE-2 / O-C04 | Poe points vary by tier and account; recent reports conflict and one includes add-ons. | E-POE-1–2; O-E13–15 | No universal current paid allotment inferred. |
| C-META-1 / O-C05 | No numeric paid Meta One quota was identified; current user report tier is not stated. | E-META-1; O-E16–17 | Bounded policy/report finding. |
| C-DS-1 / O-C06 | DeepSeek API billing and disputed consumer-chat claims do not establish a paid chat subscription quota. | E-DS-1; E-COM-1; O-E11–12 | API policy separated; post plan not stated and claim qualitative. |
| O-C08 / O-C11 | Gemini's official app policy is plan/workload-dependent; user reports are qualitative with different plan attribution. | O-E26; O-E29–30 | Provider policy plus two unnormalized reports. |
| O-C09 / O-C10 | ChatGPT limits vary; new Plus reports do not quantify standard text chat. | O-E24, O-E25, O-E27, O-E28 | Official policy plus surface-ambiguous and image-specific anecdotes. |
| O-C12 | Provider meters, third-party reads, local estimates, API tools and crowd reports are distinct. | O-E18–23; O-E31–33 | Bounded tracker classification; no normalized chat crowd dataset verified. |

## Recommendations

For a comparable allowance study, collect consented account-meter snapshots before and after repeated tasks, recording exact plan as stated, model/feature, region, account age, task type, reset boundary and observation interval. Keep provider UI readings separate from local estimates, third-party extraction claims, API spend and crowd submissions. For Poe, capture plan point grants and per-action point costs; for Grok and Gemini, record meter changes and reset notices. First establish that a paid consumer plan and meter exist in the test region before testing Meta AI or DeepSeek. The current public anecdotes are too sparse and uncontrolled to support cross-provider numerical rankings.

## Limitations and caveats

- This is a bounded web search, not an exhaustive census of private groups, app stores, login-gated pages, or all provider regions.
- Search result pages and link-indexed leads are recorded as such; a URL in the source registry does not imply its full content was independently inspected.
- Recent community search found only a small number of inspectable leads. The absence of qualifying reports means no reliable public sample was found, not that users never report limits.
- The initial proposed query set remains marked not executed during the original CUA attempt; the later Codex built-in `web__run` search set is separately logged and was executed.
- Community timestamps shown relatively (“5 days ago”, etc.) are approximate publication-date estimates as displayed on 2026-10-05. No measured interval is inferred from those timestamps.
- Policy pages can change after this report date. Perplexity’s principal comparison page was modified Oct 2; Meta One was announced Sep 15; Mistral pricing and Poe help pages were inspected during this run; Grok FAQ’s listed update was Aug 27.
- Product scope is not interchangeable: API/workspace limits, free-tier limits, enterprise limits, promo credits, and consumer paid plans are separated.

## Bibliography

See `sources.jsonl`, `community-sources-addendum.jsonl`, and their paired evidence/claim ledgers for the full source registry; `run_manifest.json` records deduplicated coverage counts. This bibliography contains each numbered source cited in the report.

[1] Perplexity Help Center (2026). “Which Perplexity subscription plan is right for you?” Retrieved 5 October 2026. https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you (O-S01)  
[2] Perplexity Help Center (2026). “How credits work on Perplexity.” Retrieved 5 October 2026. https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity (O-S02)  
[3] Mistral AI (2026). “Pricing.” Retrieved 5 October 2026. https://mistral.ai/pricing/ (O-S10)  
[4] xAI (2026). “FAQ: Grok website/apps.” Retrieved 5 October 2026. https://docs.x.ai/grok/faq (O-S06)  
[5] Poe Help Center (2026). “Poe Purchases FAQs.” Retrieved 5 October 2026. https://help.poe.com/hc/en-us/articles/19945140063636-Poe-Purchases-FAQs (O-S15)  
[6] Poe Creator Platform (2026). “Usage API.” Retrieved 5 October 2026. https://creator.poe.com/docs/resources/usage-api (O-S20)  
[7] Meta Newsroom (2026). “Introducing Meta One.” Retrieved 5 October 2026. https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/ (O-S18)  
[8] DeepSeek (2026). “Download DeepSeek.” Retrieved 5 October 2026. https://www.deepseek.com/en/download/ (core source registry)  
[9] DeepSeek API Docs (2026). “Models & Pricing.” Retrieved 5 October 2026. https://api-docs.deepseek.com/quick_start/pricing/ (O-S12)  
[10] Google Gemini Apps Help (2026). “Gemini Apps limits and upgrades for Google AI subscribers.” Retrieved 5 October 2026. https://support.google.com/gemini/answer/16275805 (O-S28)  
[11] OpenAI Help Center (2026). “What is ChatGPT Plus?” Retrieved 5 October 2026. https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus (O-S26)  
[12] OpenAI Help Center (2026). “GPT-5.6 and GPT-6 Pro in ChatGPT.” Retrieved 5 October 2026. https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt (O-S27)  
[13] Reddit r/perplexity_ai (2026). “Out of credits after light usage?” Published 7 September 2026. https://www.reddit.com/r/perplexity_ai/comments/1w9cmjq/is_it_me_or_has_perplexity_reduced_the_amount_a/ (O-S03)  
[14] Reddit r/perplexity_ai (2026). “Perplexity Pro feature/credit complaint.” Published 9 September 2026. https://www.reddit.com/r/perplexity_ai/comments/1wbwufe/perplexity_pro_is_an_absolute_joke_now_youre/ (O-S04)  
[15] Reddit r/perplexity_ai (2026). “Computer Mode Credit Cap Reached.” Published 16 September 2026. https://www.reddit.com/r/perplexity_ai/comments/1wicl01/computer_mode_credit_cap_reached_dead_in_the_water/ (O-S05)  
[16] Reddit r/grok (2026). “Super Grok weekly limit.” Published 1 October 2026. https://www.reddit.com/r/grok/comments/1wv16o6/super_grok_weekly_limit/ (O-S07)  
[17] Reddit r/GrokBot (2026). “Increase usage limits.” Published 30 September 2026. https://www.reddit.com/r/GrokBot/comments/1wu2ax2/increase_usage_limits/ (O-S08)  
[18] Hacker News (2026). “At every Grok release I commented on here how much I love Grok.” Approximately 23–24 September 2026. https://news.ycombinator.com/item?id=49796557 (O-S09)  
[19] Hacker News (2026). “Grok 4.7 discussion.” Approximately 22 September 2026. https://news.ycombinator.com/item?id=49788838 (core source S53)  
[20] Reddit r/MistralAI (2026). “Is Mistral Pro actually worth it for heavy users?” Published 20 September 2026. https://www.reddit.com/r/MistralAI/comments/1wl9rx5/is-mistral-pro-actually-worth-it-for-heavy-users/ (O-S11; coding-only)  
[21] Reddit r/MistralAI (2026). “Mistral free tier is surprisingly useful for…” Comment dated about 23 September 2026. https://www.reddit.com/r/MistralAI/comments/1w4nawy/mistrals-free-tier-is-surprisingly-useful-for/ (core source S52)  
[22] Reddit r/DeepSeek (2026). “New limits.” Published about 30 September 2026. https://www.reddit.com/r/DeepSeek/comments/1wturc5/new-limits/ (core source S51)  
[23] Reddit r/PoeAI (2026). “Subscription: plan points changed.” Published 26 September 2026. https://www.reddit.com/r/PoeAI/comments/1wqncrp/subscription/ (O-S16)  
[24] Reddit r/ClaudeAIJailbreak (2026). “Is Poe's $20 plan worth it?” Published 2 October 2026. https://www.reddit.com/r/ClaudeAIJailbreak/comments/1wvy97d/is_poecoms_20_plan_worth_it/ (O-S17)  
[25] Reddit r/META_AI (2026). “Meta AI quota experience.” Published 7 September 2026. https://www.reddit.com/r/META_AI/comments/1wa3hny/meta_broke/ (O-S19)  
[26] Reddit r/GeminiAI (2026). “Have the limits lowered yet again?” Published 13 September 2026. https://www.reddit.com/r/GeminiAI/comments/1wfhxlh/have_the_limits_lowered_yet_again/ (O-S31)  
[27] Reddit r/GeminiAI (2026). “What is up with the limits all of a sudden?” Comment dated 9 September 2026. https://www.reddit.com/r/GeminiAI/comments/1wb5d55/what_is_up_with_the_limits_all_of_a_sudden/ (O-S32)  
[28] Reddit r/ChatGPT (2026). “Usage limits are insanely low now.” Published 18 September 2026. https://www.reddit.com/r/ChatGPT/comments/1wjqvt0/usage_limits_are_insanely_low_now/ (O-S29)  
[29] Reddit r/ChatGPT (2026). “First time hitting the image generation limit on ChatGPT.” Published 29 September 2026. https://www.reddit.com/r/ChatGPT/comments/1wtmoeo/first_time_hitting_the_image_generation_limit_on/ (O-S30)  
[30] AIRadar (2026). “AIRadar” repository. Retrieved 5 October 2026. https://github.com/risewithvj/AIRadar (O-S21)  
[31] Chrome Web Store (2026). “AI Usage Limit Alerts.” Listing updated 22 July 2026; retrieved 5 October 2026. https://chromewebstore.google.com/detail/ai-usage-limit-alerts/nfnpdgcjkggjhkhedkkfhppeeaeopdbo?hl=en (O-S33)  
[32] OpenUsage (2026). “OpenUsage.” Retrieved 5 October 2026. https://openusage.sh/ (O-S25)  
[33] TiboTattle (2026). “Homepage.” Retrieved 5 October 2026. https://tibotattle.com/ (O-S34)

## Methodology appendix: coverage and boundaries

**Search coverage.** Official pages were inspected for Perplexity, Mistral, xAI, Poe, Meta, DeepSeek, Google Gemini and OpenAI ChatGPT. The supplemental pass searched Reddit first by provider, then Hacker News and developer/app sources. Current-window community items were date-gated to Sep 5–Oct 5, 2026. Directly inspected pages, search-indexed leads and discovery-only/historical entries remain distinct in the source registries.

**Query themes.** Queries used provider names combined with `limits`, `quota`, `usage limit`, `weekly limit`, `messages`, `reset`, `subscription`, `allowance tracker`, and `usage tracker`. The exact expanded queries and outcome notes are in the supplemental query log; the initial package records query families rather than a full browser-history export.

**Evidence rule.** Current numeric community evidence requires an in-window publication date, separately identified measurement interval, plan and model/action context, described method and a quantity that can be checked. Disputed, vague, old, mixed-window or unqualified statements remain qualitative/discovery evidence. First-party published policy is reported as policy and carries its own page/update date. The evidence ledger records direct quotation or concise paraphrase, locator/URL, dates, confidence, and intended use.

**Ultradeep workflow record.** The workflow references were accessible via LeanCTX after registering the repository alias in this agent session. The 9-phase workflow, critique loops and validation results are documented in `phase-evidence.md`; the runtime orchestrator itself was not invoked. No HTML/PDF was generated because the assigned deliverables are Markdown and JSON/JSONL. No claim of exhaustive coverage is made.

## Report Metadata

- Run ID: 2026-10-05-other-provider-chat
- Workflow ID: WF-SILVER-DEEP-RESEARCH
- Atomic flow: AF-DECIDE
- Flow step: FS-SILVER_DEEP_RESEARCH
- Mode: ultradeep
- Research type: default
- Community window: 2026-09-05 through 2026-10-05 inclusive
- Search route: Codex built-in web__run as required by the user
- Search-cli status: Not used; retrieval was restricted to web__run
- Silver Bullet runtime/orchestrator invoked: No; documented phase contract applied manually
