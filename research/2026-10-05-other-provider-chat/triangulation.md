# Triangulation — DR-TRIANGULATE

## Source grading (Silver Bullet Admiralty-style)

Grades describe the reliability of the source for the specific claim, not the truth of an allowance estimate.

| Source IDs | Reliability | Authority | Bias flags | Use |
|---|---|---|---|---|
| O-S01, O-S02, O-S06, O-S10, O-S15, O-S18, O-S26–O-S28 | A2 | primary | commercial, single_perspective | Official provider policy is authoritative for the provider's published terms; a single official source does not independently measure account outcomes. |
| O-S12, O-S13 | A2 | primary | commercial, single_perspective | Official API policy only; excluded from consumer-chat quota conclusions. |
| S51–S53, O-S03–O-S19, O-S29–O-S32 | D3; D4 where the thread itself disputes or obscures the claim | unknown | single_perspective | First-person or commenter account claim, not independently logged; preserve the user's own tier or “not stated.” |
| O-S20, O-S33 | B2 | primary | commercial, single_perspective | Official Poe account-usage docs / extension listing establish stated feature description, not cross-account validity. |
| O-S21–O-S25, O-S34 | B2 | primary | commercial, single_perspective | Project README/homepage establishes what maintainers say the app does; no runtime/security audit here. |
| Core editorial tracker and product discovery entries | C3 | tertiary | commercial, single_perspective | Discovery leads only; not treated as provider quota evidence. |

`A2` means a single high-authority source; `D3` means a weak/unverified source with a plausible but unconfirmed claim; `D4` marks a disputed or poorly scoped anecdote. Grades are manual pre-triage following the SB rubric. The `source_evaluator.py` network evaluator was not run because the user's retrieval constraint requires built-in `web__run` only.

## Claim triangulation

| Claim | Independent source check | Conclusion |
|---|---|---|
| Perplexity paid search allowance | Provider plan page + separate credits help + current Reddit reports. | Official terms remain qualitative; user reports mainly concern Computer credits and cannot be normalized. |
| Grok weekly usage | xAI FAQ + Reddit account reports + two HN discussions. | Shared pool is provider-stated; user burn reports vary by tier/action and give no transferable amount. |
| Mistral Le Chat | Mistral pricing + free-tier comment + Vibe coding report. | Flash cap is provider policy; Vibe numbers are coding-only; free-tier comment has unclear surface. |
| DeepSeek consumer chat | Official consumer page + API pricing + disputed Sep 30 post + Sep 29 API-spend discussion. | No paid consumer tier found; one disputed user claim has plan not stated; API spend is separate. |
| Poe points | Official purchases FAQ and user usage API + two current reports. | Plan-specific point schedule; one report does not state tier and another states Poe Plus but includes add-ons. |
| Meta AI | Meta One announcement + one image-generation report. | No numeric paid allowance found; reporter tier not stated. |
| Gemini app | Official limits page + current posts. | Compute/workload-dependent first-party limit; two anecdotes are unnormalized and one poster tier is not stated. |
| ChatGPT standard chat | OpenAI Plus/model help pages + two user reports. | Limits vary; a surface-ambiguous Plus anecdote and image-generation report do not establish standard text-chat allowance. |

No multi-account crowd data independently confirms the anecdotes. A named plan in a post is reported as a user statement, not provider verification.
