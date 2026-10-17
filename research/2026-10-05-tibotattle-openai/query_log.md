# Query log: TiboTattle and Codex

**Audit date:** 2026-10-05 (Australia/Sydney). **Web route:** Codex built-in `web__run` only. Search results served discovery; claims were checked against publisher pages, official documentation, App Store listings, or the TiboTattle homepage as scoped below.

## Exact audit queries

| Route | Exact query | Purpose and handling |
|---|---|---|
| `web__run` search | `site:tibotattle.com Codex allowance estimates` | Locate the eligible homepage surface and check its displayed state. Only the homepage can support a numeric Codex crowd allowance value. |
| `web__run` search | `"TiboTattle" Codex Reddit OR Hacker News OR community post` | Find direct developer-community product discovery; any allowance or usage quantities in such posts are excluded. |
| `web__run` search | `TiboTattle Codex tracker launch post` | Product discovery only. |
| `web__run` search | `"TiboTattle" "Codex"` | Cross-check product and community discovery leads; snippets are not evidence. |

## Direct pages opened with `web__run`

| Source ID | Page | Use in this package |
|---|---|---|
| S01 | [TiboTattle homepage](https://tibotattle.com/) | Eligible homepage-state observation; only source allowed to supply numeric Codex community allowance values. |
| S02 | [TiboTattle documentation](https://tibotattle.com/docs) | Publisher methodology and data-provenance description; not used for numeric allowance values. |
| S03 | [TiboTattle privacy overview](https://tibotattle.com/privacy) | Publisher contribution, identity, overlap, and sample caveats; not used for numeric allowance values. |
| S04 | [TiboTattle public repository](https://github.com/adamallcock/tibotattle) | Product discovery and publisher context only. |
| S37 | [Direct r/codex product-discovery post](https://www.reddit.com/r/codex/comments/1wjusve/) | Confirms a developer-authored community discovery lead links to TiboTattle and its public repo. Every allowance, token-volume, and usage/value quantity in the post is excluded. The page's relative-time label does not establish a calendar date, so publication date is unresolved. |
| S06, S08, S09 | [OpenUsage homepage](https://www.openusage.ai/), [privacy page](https://github.com/robinebers/openusage/blob/main/docs/privacy.md), and [Codex provider guide](https://github.com/robinebers/openusage/blob/main/docs/providers/codex.md) | Publisher-described account signal and local estimates. Privacy page says telemetry omits actual usage values. Homepage contains promotional mock data; excluded from any allowance claim. |
| S10 | [CodexBar repository](https://github.com/steipete/CodexBar) and [provider docs](https://github.com/steipete/CodexBar/blob/main/docs/providers.md) | Publisher-described account-specific and local methods. |
| S13-S14, S29-S30 | [CUStats homepage](https://custats.info/), [privacy page](https://custats.info/privacy), [Mac listing](https://apps.apple.com/us/app/custats-ai-usage-tracker/id6756333957?mt=12), [Go listing](https://apps.apple.com/us/app/custats-go-ai-usage-tracker/id6757679404) | Product discovery only. The current web__run capture exposed page titles but not substantive text for the CUStats homepage or privacy page. A targeted in-page search did expose the Mac listing's Codex, local-data, credential, and telemetry description; the table now relies on that listing and marks the older privacy page as dated. |
| S15-S18, S31-S32 | [SessionWatcher homepage](https://sessionwatcher.com/) and [Codex page](https://sessionwatcher.com/codex) | Product discovery and publisher-described local tracking. Its Codex FAQ says it reads local usage statistics and does not upload prompts, conversations, code, or project files; promo screenshots are excluded. |
| S19-S20 | [AIUsage repository](https://github.com/sylearn/AIUsage) and [usage/billing methodology](https://github.com/sylearn/AIUsage/blob/main/docs/USAGE_AND_BILLING.md) | Publisher-described separation between proxy pricing and local Codex logs; not an account allowance source. |
| S21 | [ccusage repository](https://github.com/ccusage/ccusage) | Local usage-report product discovery. |
| S22 | [OpenAI Codex plan help](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) | Official account-navigation context kept separate from community evidence. |
| S33 | [VibeCheck App Store listing](https://apps.apple.com/us/app/vibecheck-limits-companion/id6759708342) | Adjacent-app discovery only; synthetic examples excluded. |
| S34 | [Model Usage App Store listing](https://apps.apple.com/us/app/model-usage/id6761831599) | Adjacent-app discovery only. |
| S35 | [TokenBar Mobile App Store listing](https://apps.apple.com/us/app/tokenbar-mobile/id6760548040) | Adjacent-app discovery only. A direct page open returned an internal error; a later targeted in-page search exposed the credential/Keychain description. No allowance values are used. |
| S36 | [Codexex App Store listing](https://apps.apple.com/us/app/codexex/id6762058457) | Codex-specific companion discovery only; sample values excluded. |

## Preserved earlier search record

The pre-existing `run_manifest.json` also preserves five original discovery queries. Those entries remain attributed to the earlier package rather than being represented as searches performed during this audit. The direct homepage, docs, privacy, repository, Reddit post, and alternative product pages listed above were re-opened or revalidated in this audit with `web__run`.

## Targeted in-page checks

The exact `web__run` `find` patterns used on opened primary pages were: `Codex` (CodexBar provider docs, AIUsage repo, ccusage repo, and CUStats listing); `actual usage values` and `telemetry` (OpenUsage privacy); `non-proxy Codex` and `price frozen` (AIUsage usage/billing methodology); `provider credentials stay on the Mac` (VibeCheck); `user controls` and `usage files` (Model Usage); `Keychain` (TokenBar Mobile); `on device` and `Codex usage` (Codexex); `privacy`, `Codex`, and `Data Not Collected` (CUStats). The Codexex “Codex usage” result says quota reads stay on the device; the unsuccessful `on device` pattern itself did not match. The `price frozen` search also did not match; the methodology text separately describes proxy cost being fixed at request-time node prices. CUStats's “Codex” result exposed its current App Store publisher description; its separate homepage/privacy pages still had no readable substantive text in the capture.

Search-engine snippets, AI summaries, screenshots, interactive examples, and community-post quantities were not treated as evidence for Codex allowance values. No Edge, Chrome, CUA, command-line web request, or direct HTTP fetch was used in this audit.
