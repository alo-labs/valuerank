# MiMo-V2.6-Flash reasoning effort (owner decision O135, read 2026-10-30)

AA plots MiMo-V2.6-Flash (`https://artificialanalysis.ai/models/mimo-v2-6-flash`) without an effort. O135 takes it at the
effort Xiaomi documents as the default, as O66 did for Kimi K3.1 Pro (`../../2026-10-25-board-reread/kimi-search.md`).

## Xiaomi's API documentation

Read 2026-10-30T22:23:55Z to 22:24:15Z. `platform.xiaomimimo.com/docs/...` redirects to `mimo.mi.com/docs/...`. Saved pages
are in `mimo/`. The quotes below are from the pages' rendered text.

1. **OpenAI-compatible Chat Completions.** https://mimo.mi.com/docs/en-US/api/chat/openai-api (`mimo/openai-api.html`).
   The request has no `reasoning_effort` parameter. It has a `thinking` object: "This parameter is used to control whether
   the model enables the chain of thought." Its `type` field reads: "Whether to enable the chain of thought.
   mimo-v2.6-flash , mimo-v2.6-pro , mimo-v2.6-pro-ultraspeed : default enabled Available options: enabled , disabled".
2. **Anthropic-compatible Messages.** https://mimo.mi.com/docs/en-US/api/chat/anthropic-api
   (`mimo/api_chat_anthropic-api.html`). `thinking`: "Configuration for enabling model's extended thinking." Its `type`
   field reads: "mimo-v2.6-flash , mimo-v2.6-pro , mimo-v2.6-pro-ultraspeed : default enabled Available options: enabled ,
   disabled". There is no budget or effort field.
3. **Responses API.** https://mimo.mi.com/docs/en-US/api/chat/responses (`mimo/api_chat_responses.html`). It says:
   "Reasoning level control : reasoning.effort controls model reasoning. none disables thinking; Every other level enables
   thinking with identical behavior — The reasoning intensity is not differentiated at this stage." The `reasoning.effort`
   field reads: "Custom tuning of reasoning effort is currently unsupported. When set to none , reasoning is disabled; all
   other valid values map to enabled reasoning. The value minimal is mapped to low . Values xhigh , max and ultra are mapped
   to high . mimo-v2.6-flash , mimo-v2.6-pro , mimo-v2.6-pro-ultraspeed : default enabled Available options: none ,
   minimal , low , medium , high , xhigh , max , ultra".
4. Further context:
   - The model-update log (https://mimo.mi.com/docs/en-US/updates/model) describes mimo-v2.6-flash (released 2026-09-22) as
     a "Full-modality, high-intelligence, low-cost reasoning model".
   - The hyper-parameter guide (`mimo/api_guidance_model-hyperparameters.html`) says that in thinking mode temperature and
     top_p are fixed at 1.0 and 0.95.
   - The V2.6 release note (`mimo/news_latest_v2-6.html`) gives no effort levels.

## Finding

Xiaomi documents one reasoning mode for MiMo-V2.6-Flash. Thinking is either **enabled** or **disabled**, and **enabled is
the default** on all three APIs. There is no graded effort ladder:

- The Responses API accepts effort labels from `minimal` to `ultra`.
- Every label except `none` gives the same, undifferentiated reasoning. The labels are normalised to low/medium/high, and
  `xhigh`, `max` and `ultra` map to `high`.

Under O135, AA's plotted configuration is therefore **MiMo-V2.6-Flash with thinking enabled, the provider default**. This
is also its only reasoning setting.

This differs from O66. Moonshot documents distinct levels (low, high, max) with max the default. Xiaomi documents only
on/off.

A third-party model registry (pi.dev, found by web search, not official) lists Xiaomi's endpoint with
`supportsReasoningEffort: false` and only off/high thinking levels. That is consistent with the above but is not relied on.

## Which board rows are this configuration

| Board | Row | Status | Basis |
|---|---|---|---|
| AI Coding Daily | **"MiMo-V2.6 Flash (High)"**: OpenCode, tested 2026-10-02 ("4 weeks ago" at the 2026-10-30T22:21:52Z read), total 53.29, Laravel 17.83, React-TS 17.5, Bug Finding 7.81, Edge-case 10.15; **non-bug leaf 45.48**; $0.04/prompt | **exact** | This is the board's only MiMo-V2.6-Flash row. "High" is a thinking-enabled level, and Xiaomi documents every enabled level as identical (it maps xhigh, max and ultra to high). The row does not name the provider route behind OpenCode. |
| Bug Hunt | "MiMo-V2.6-Flash - mean of 3": Claude Code via OpenRouter, effort `default`, 23.3/105, dated 2026-09-22 | plausible (owner check) | The run used the route's default without asserting a reasoning state. The owner's notes say the dial is "untested rather than known-inert" on Flash. If OpenRouter passes Xiaomi's default through, this is thinking enabled, but the board does not show that. |
| Vals Vibe Code v1.1 / Code Migration v1.1 | `xiaomi/mimo-v2.6-flash`: 78.96 ±4.045 / 39.552 ±3.537 | plausible (as 2026-10-25) | Vals records reasoning, reasoning_effort and compute_effort as null. Its model page (read 2026-10-30) states no reasoning setting. |
| LiveBench 2.0, tbench.ai | none | absent | No MiMo-V2.6-Flash row. |
