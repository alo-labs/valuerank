# Triangulation and source assessment

## Source grading

| Source | Grade | Evidence class | Use and limit |
|---|---|---|---|
| S02 OpenCode Go docs | A1 | Provider plan, catalog, route tariff | One first-party page directly joins plan fee, exact model label, per-model limit, reset share, and per-token price; no independent provider disclosure is needed to establish its own advertised contract. |
| S03 Ollama pricing | A1 | Provider subscription credits and model tariffs | One first-party page joins tier pricing/credits/reset and route-level per-token tariff; Team is a shared pool. |
| S04–S06, S13–S14 Z.AI/ZCode docs | A1 | Plan price, quota formula, API price, time-bound promotions | Cross-page arithmetic is independently recomputable from the provider's quota formula and separate API tariff; quarterly price remains unknown. |
| S07 DeepSeek change log | A1 | Version / alias identity | Dated primary announcement provides the V4 Flash to V4.1 Flash alias mapping; it does not set third-party subscription caps. |
| S08 Alibaba plan/docs | A1 | Exact-model plan access and opaque conversion | Exact Qwen3.8 Max plan is identified, but model/token/reasoning/tool credit charge has no public coefficient; no API equivalent is calculated. |
| S09–S12 project research packages | B1 | Current-window research and evidence boundary | Preserve date window, official policies, community reports, and TiboTattle homepage-only constraint. Community anecdotes are not the numeric route denominator. |
| S01 roster files | A1 | Exact roster identity | Project raw data and README are the source of model IDs, efforts, and 13+12 coverage. |

## Cross-checks and adjudication

OpenCode's single source page supplies both plan limits and matching route tariffs; calculations use the same page, with API-equivalent token totals recomputed under the published profile. Ollama likewise publishes the credits, terms, reset rules, and model-rate table together. These are auditable within-provider comparisons; they are not independent third-party confirmations of service delivery.

Z.AI conversion is triangulated across plan pricing, official credits/reset and multiplier docs, and a separate Z.AI API tariff. Its published model token ranges use high cache-hit assumptions that do not equal the three report profiles, so those ranges are not substituted. Standard peak, all-off-peak, current all-day campaign, and separate Flash overnight windows are kept distinct.

DeepSeek's alias notice establishes the target of its own direct API name but does not identify the backend used by third-party subscription catalog rows. OpenCode lists V4 Flash and V4.1 Flash separately with distinct Go caps; Ollama lists V4.1 Flash only. All eight adjacent tier rows are retained in `route-exceptions.csv` and excluded from the ValueRank V4 Flash row because the exact 0731 variant is not verified. Z.AI's GLM-5.2 redirect is also excluded from the GLM-5.2 cohort row.

Current-window community reports can show real account-meter observations, but they are user- and workload-specific and commonly lack a normalized token mix. They are not cross-provider plan allowance denominators. The TiboTattle homepage showed no numeric series; no alternative crowd source is substituted for OpenAI/Codex.
