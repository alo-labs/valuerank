# Codex allowance tracking and crowdsourced alternatives

## Executive Summary

The Codex-built-in web capture of TiboTattle's homepage on 2026-10-05 showed a checking/loading message in its community allowance panel; no numeric community series or sample count was visible [1]. This is only a statement about that page capture, not proof that TiboTattle has never published estimates. The homepage is the sole allowed source for a numerical Codex crowdsourced allowance value, and the separate interactive examples are explicitly illustrative rather than live account data [1]. The publisher describes its chart as an API-price-equivalent estimate, not an official plan allowance or bill [2]. The reviewed tracker landscape includes TiboTattle and ten adjacent products, but most describe account-specific signals or local token/cost summaries rather than public crowd aggregates [5]–[11], [13]–[16]. No user-reported numerical allowance datapoint is included; any future datapoint must name the exact plan tier or say “not stated.”

## Introduction

This report answers two bounded questions: what Codex community allowance value could be read from TiboTattle's homepage during the one-month observation window, and what other apps expose related usage information? The eligible empirical window is 2026-09-05 through 2026-10-05 inclusive. Under the governing source rule, only a numeric series published on the canonical TiboTattle homepage may support a Codex crowdsourced allowance amount. Reddit, Hacker News, provider posts, repositories, app-store screenshots, search snippets, and third-party trackers cannot be substituted for that figure.

Three kinds of measurements must remain distinct. A crowd aggregate combines submissions across installations; a provider/account signal displays an individual user's account state; and a local estimate summarizes logs or applies API prices to observed tokens. An API-price equivalent is not itself a subscription plan's bill or quota. This distinction governs the comparisons below [2], [3], [5], [7], [10], [11], [12].

## Main Analysis

### TiboTattle homepage observation

The page capture showed “Checking allowance estimates” and “Checking for published allowance estimates…” in the community “Pro 20x-equivalent allowance” panel. The daily activity panel was also checking. No numeric community allowance series or sample count was visible. The separate interactive demonstration is labeled illustrative, not live account data, and was excluded [1]. The defensible result is therefore “no numeric value visible in the captured state,” rather than “no value exists” or “TiboTattle has never published one.”

“Pro 20x-equivalent week” is the chart's comparison basis. It is not an individual user's plan tier and it is not an observed allowance datapoint. This review contains zero user-reported numerical allowance observations. If a future report adds one, its exact tier must accompany the datapoint; when the source does not identify a tier, the field must read “not stated.”

### Meaning and limits of the aggregate

TiboTattle's documentation describes account/rate-limit and local session inputs and presents the public result as an API-price-equivalent estimate [2]. Its privacy page describes eligible contributions and notes that a contribution source is an installation/account track rather than a unique verified person; separate installations may overlap, and a daily view may rely on a single source [3]. The product says prompts and responses are not included [3]. These are publisher disclosures. They do not independently verify submissions or demonstrate that the contributors represent Codex users generally. Consequently, even when a figure becomes visible, it should be reported with the publisher's label and sample context, not as an official OpenAI allowance or a population estimate.

### Comparable trackers and what they measure

The discovery set contains eleven products, counting TiboTattle and ten adjacent apps. It is a bounded set, not a census. OpenUsage describes local-first monitoring on its homepage [4], calls to account-specific Codex usage endpoints, and separately calculated local daily cost and token tiles from session rollouts [5]. Its privacy document says anonymous telemetry excludes actual usage values [6]. CodexBar describes account-specific provider reads and a local CLI fallback, while its session cost summaries come from local records [7].

CUStats describes personal Codex monitoring in its app listings, with local data handling claims attributed to the developer; demonstration figures were excluded [8]. SessionWatcher describes account-specific status and reset views and local token/cost context [9]. AIUsage separates proxy request pricing from local Codex session JSONL and does not infer a subscription account's cost [10]. ccusage reads local agent usage records and generates token/cost reports [11]. These tools can help a user inspect their own activity, but the reviewed sources do not present them as public Codex crowd allowance distributions.

The expanded discovery set includes VibeCheck, Model Usage, TokenBar Mobile, and Codexex. Their app-store listings describe companion or provider-account monitors, local credential handling, or user-controlled usage endpoints [13], [14], [15], [16]. Those descriptions establish that the products exist and how their publishers characterize them; they do not demonstrate a crowdsourced Codex allowance chart. The direct developer-authored r/codex post is only a discovery lead. No allowance, token-volume, or usage/value quantity from that post is used [17].

OpenAI's help page directs users to their own Codex usage dashboard or CLI /status and says limits vary by plan [12]. That is official account-navigation guidance, not a community report and not a universal numerical allowance.

## Claims-Evidence Table

The E01-style evidence labels in this table are preserved parent-package IDs; [legacy-id-crosswalk.md](legacy-id-crosswalk.md) maps them to the hashed IDs in this Ultradeep ledger.

| Finding | Evidence | Interpretation |
|---|---|---|
| No numeric crowd value was visible in this homepage capture | E01, E02 | Retrieval-time observation only |
| The chart is API-price-equivalent | E02, E03 | Publisher-defined estimate, not official plan value |
| Sample overlap and small daily samples are possible | E04, E27 | Publisher privacy/method disclosure, not independent audit |
| Similar products use account-specific or local signals | E05–E12, E17, E22–E25 | Capability descriptions attributed to publishers |
| Discovery includes eleven products | E05–E11, E16–E18, E22–E25 | Count of this report's bounded discovery set only |

## Counterevidence Register

| Potential counterevidence | Treatment |
|---|---|
| A numeric value may exist in another homepage route, may load after this capture, or may appear later. | The conclusion is limited to the captured homepage state and does not assert historical or future absence. |
| A direct TiboTattle developer post or search result could contain an allowance quantity. | Excluded for numerical value purposes because the user designated the homepage as the only eligible Codex crowd source. |
| A personal OpenAI dashboard or tracker could show a user's remaining quota. | Kept as an account-specific signal; it is not a crowdsourced population result. |
| A demo may show plausible numbers. | Excluded because product pages label them illustrative, not live account data. |

## Synthesis

The homepage-only rule means the current result is no usable numerical Codex crowd allowance datapoint in the captured page state. Third-party account trackers and local cost calculators may provide useful personal instrumentation, but their readings answer different questions. Combining them with a TiboTattle API-price-equivalent aggregate would create a misleading composite. Likewise, OpenAI's account dashboard can answer a user's personal limit question, but it cannot stand in for a crowdsourced distribution [1]–[3], [5]–[12].

The result should be refreshed before being used in a subscription ranking because the homepage may publish or load a series later. A new capture should record the observation date, chart label, sample count if displayed, aggregation period, and the homepage URL. Do not extract demo values. If user reports are incorporated into a separate evidence stream, record each source's exact plan tier or mark it “not stated,” and retain the date within the required one-month window.

## Limitations

The main observation is time-sensitive and may reflect asynchronous loading. It establishes only what was visible in one page capture. Product methods and privacy statements are self-reported; the software was not installed and no account was connected. Some CUStats pages exposed loading placeholders or headings without substantive answers; those entries are coverage records, not support. App-store and search discovery can miss products, so the eleven-product list is not exhaustive. Older product dates and app release metadata were used only for discovery, never to infer an allowance value.

No user-reported allowance datapoint is included, so this report has no plan-tier value to attach. The chart phrase “Pro 20x-equivalent” is a comparison basis, not a report of a user's plan. The report does not estimate any missing allowance quantity and does not assert that the homepage has never published one.

## Recommendations

1. Refresh the TiboTattle homepage immediately before using its crowd series in a ValueRank calculation.
2. Accept Codex crowd numbers only from that homepage, retaining the exact chart label, timestamp, visible sample information, and source URL.
3. Keep crowd aggregates, account-specific signals, and local log/API-price estimates in separate columns or data classes.
4. Exclude illustrative demo figures and discovery-source quantities from empirical allowance calculations.
5. For every future user datapoint, record exact plan tier; if the report omits it, write “not stated.” Apply the 2026-09-05 to 2026-10-05 window relative to this run and refresh the cutoff for future runs.
6. Treat tracker coverage as a discovery sample and verify any candidate from its own publisher documentation before describing its data source.

## Bibliography

[1] TiboTattle. (2026). "TiboTattle homepage." TiboTattle, accessed 2026-10-05. https://tibotattle.com/
[2] TiboTattle. (2026). "Documentation." TiboTattle, accessed 2026-10-05. https://tibotattle.com/docs
[3] TiboTattle. (2026). "Privacy." TiboTattle, accessed 2026-10-05. https://tibotattle.com/privacy
[4] OpenUsage. (2026). "OpenUsage homepage." OpenUsage, accessed 2026-10-05. https://www.openusage.ai/
[5] OpenUsage developers. (2026). "OpenUsage Codex provider guide." GitHub, accessed 2026-10-05. https://github.com/robinebers/openusage/blob/main/docs/providers/codex.md
[6] OpenUsage developers. (2026). "Privacy policy." GitHub, accessed 2026-10-05. https://github.com/robinebers/openusage/blob/main/docs/privacy.md
[7] CodexBar developers. (2026). "Provider documentation." GitHub, accessed 2026-10-05. https://github.com/steipete/CodexBar/blob/main/docs/providers.md
[8] CUStats developers. (2026). "CUStats AI Usage Tracker for Mac." Apple App Store, accessed 2026-10-05. https://apps.apple.com/us/app/custats-ai-usage-tracker/id6756333957?mt=12
[9] SessionWatcher. (2026). "Codex product page." SessionWatcher, accessed 2026-10-05. https://sessionwatcher.com/codex
[10] AIUsage developers. (2026). "Usage and billing methodology." GitHub, accessed 2026-10-05. https://github.com/sylearn/AIUsage/blob/main/docs/USAGE_AND_BILLING.md
[11] ccusage developers. (2026). "ccusage repository and README." GitHub, accessed 2026-10-05. https://github.com/ccusage/ccusage
[12] OpenAI. (2026). "Using Codex with your ChatGPT plan." OpenAI Help Center, accessed 2026-10-05. https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
[13] VibeCheck developer. (2026). "VibeCheck Limits Companion." Apple App Store, accessed 2026-10-05. https://apps.apple.com/us/app/vibecheck-limits-companion/id6759708342
[14] Model Usage developer. (2026). "Model Usage." Apple App Store, accessed 2026-10-05. https://apps.apple.com/us/app/model-usage/id6761831599
[15] TokenBar Mobile developer. (2026). "TokenBar Mobile." Apple App Store, accessed 2026-10-05. https://apps.apple.com/us/app/tokenbar-mobile/id6760548040
[16] Codexex developer. (2026). "Codexex." Apple App Store, accessed 2026-10-05. https://apps.apple.com/us/app/codexex/id6762058457
[17] TiboTattle developer. (2026). "r/codex TiboTattle product-discovery post." Reddit, accessed 2026-10-05. https://www.reddit.com/r/codex/s/FG2HF6XwnG

## Methodology

This package was prepared on 2026-10-05. Codex built-in web__run was the only browser/research retrieval interface used in this audit. The TiboTattle homepage is the only admissible source for numerical Codex crowd allowance values. Search artifacts and the direct Reddit post are discovery-only. Evidence and claims are preserved in the adjacent JSONL ledgers, and the original package files remain at the parent directory. The exact search trail is in the parent query_log.md; the page-specific references are in the parent citations.md.

## Report Metadata

- Research date: 2026-10-05
- Empirical window: 2026-09-05 to 2026-10-05 inclusive
- Research mode: Ultradeep artifact/critique workflow
- Source inventory: 37 records; preferred budget: 30 (exceeded by seven to preserve source history and bounded app coverage); configured maximum: 40
- User-reported allowance datapoints included: 0
- Plan-tier status: no datapoints to classify; future entries require exact tier or “not stated”
- Automated /sb:deep-research command: not invoked; workflow artifacts were assembled against the documented phases
- Built-in browser policy: Codex web__run only
- Citation verifier: non-strict pass with warnings; 15 of 17 links verified, one generic-short-title flag, one HTTP 403 (see validation/verify_citations.log)
- Legacy package: ../report.md, ../sources.jsonl, ../evidence.jsonl, ../claims.jsonl, ../citations.md, ../query_log.md
