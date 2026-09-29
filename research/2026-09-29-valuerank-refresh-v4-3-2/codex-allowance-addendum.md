# Codex plan allowance addendum — 2026-09-30

## Result

The shared 38× ChatGPT Pro 20x route overstated the current reduced allowance for the exact ranked variants with model-specific measurements. The route file now assigns **28.3× to GPT-6 Astra** and **37.0× to GPT-5.6 Sol**. The estimates remain community-observed and low-medium confidence.

The Reddit post reports the following on a $20 Plus account, using six five-hour windows per week:

| Model in the post | Monthly API-equivalent | Plus value multiple | Pro 20x estimate | ValueRank mapping |
|---|---:|---:|---:|---|
| GPT-6 Luna | $167 | 8.35× | 16.7× | Not in the current ranked cohort |
| GPT-6 Sol / Terra Sol | $283 | 14.15× | 28.3× | Not in the current ranked cohort |
| GPT-6 Astra | $283 | 14.15× | 28.3× | `gpt-6-astra` |
| GPT-5.6 Sol | $370 | 18.5× | 37.0× | `gpt-5.6-sol` |

The normalization is:

```text
Pro 20x multiple = Plus monthly API-equivalent × 20 ÷ $200
                 = 2 × Plus value multiple
```

The OpenAI Codex pricing page publishes Pro 20x as 20 times Plus usage and supplies per-model local-message ranges per five-hour period. It also says actual usage varies with task size, context, model, and local versus cloud use. The Reddit source measures one account, excludes long context, and uses its own six-windows-per-week assumption; its API-equivalent figures are therefore not guaranteed plan values.

## Plan and pricing scope

OpenAI's current Pro tier help page says eligible legacy Pro 200 accounts retain their previous included allowance through **2026-10-29**, after which they move to a lower allowance. This addendum models the current reduced Pro 20x tier and excludes that temporary legacy allowance. The help page's banner says new sign-ups and upgrades are paused while its FAQ says new Pro 200 subscriptions are available with lower usage, so this record does not make a definitive availability claim.

GPT-5.6 Sol's $370 monthly estimate uses promotional API pricing. OpenAI's API pricing page says that promotion is available at least through **2026-11-21**; recheck the route before that date.

GPT-6 Luna and GPT-6 Sol are kept as source context because those exact model IDs are outside the current ranked cohort. GPT-5.6 Luna is not mapped from the GPT-6 Luna observation. The older 38× cross-model community estimate remains provisional for GPT-5.6 Luna and GPT-5.5, for which this post provides no direct measurement.

## Sources

- [Community measurement: “Allowance for GPT 6 Luna, Sol and Astra - measured”](https://www.reddit.com/r/codex/comments/1wp0v6x/allowance_for_gpt_6_luna_sol_and_astra_measured/)
- [OpenAI Codex pricing and usage estimates](https://learn.chatgpt.com/docs/pricing)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI Pro tier terms](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [OpenAI GPT-5.6 and GPT-6 Pro usage policy](https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)

## Related plan-cost mapping correction

The ranked Claude Opus 5.5 model (`claude-opus-5-5`) was eligible for Claude Max 20x but absent from the route's model ID list, so its Plan Costs value had fallen back to API cost. Anthropic's current pricing page lists Max 5x and Max 20x plan access, and its Opus 5.5 page identifies Max as an eligible plan. The route now includes the exact Opus 5.5 model ID. Its existing 40× route multiple remains an independent high-water estimate with low-medium confidence; it is not a measured Opus 5.5 allowance.

- [Anthropic Claude pricing](https://claude.com/pricing)
- [Anthropic Claude Opus 5.5 availability](https://www.anthropic.com/claude/opus)
