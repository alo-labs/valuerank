# DR-PLAN: research plan (deep mode)

## Mode rationale
Deep mode was set by the owner. Two features of the evidence make it necessary:
- The evidence is user-generated and has low credibility (C–E).
- Stage 1 left a metering discrepancy that could invalidate the only passing cell.

The deep budget applies: 25–35 sources, 2 critique cycles.

## Tooling and degradation
- **search-cli:** absent. `command -v search` returned nothing.
- **Helper agents:** no Task/Agent tool is available, so retrieval runs sequentially in the lead agent, as in the 2026-10-25 run.
- **Host tools used instead:**
  - WebSearch and WebFetch;
  - curl through the agent proxy to arctic-shift (Reddit), HN Algolia, api.bsky.app, locdd.com search.json and topic JSON, Yahoo! JAPAN real-time search (public X posts), YouTube result pages (metadata only), and sov2ex;
  - the OpenAI community forum search.json;
  - GitHub HTML through WebFetch.

## Source classes and planned queries
1. **Reddit (arctic-shift):** full comment dumps since 2026-10-26 for r/codex (9,800), r/OpenaiCodex and r/ChatGPTPro. Posts in 5 subreddits. Google subreddits since 10-28 for Carbon. Author histories of the key observers after 10-28. Then regex filters for weekly or Pro readings that carry tokens or dollars.
2. **LINUX DO through the locdd.com mirror** (linux.do returns 403). Searches: "terra", "terra 5小时", "terra 周额度", "terra plus 额度", "codex 额度 美元", "terra pro", "codex pro 周", "隐藏倍率". Then full topics and screenshots.
3. **Bluesky** through api.bsky.app (public.api.bsky.app returns 403). 13 queries.
4. **X** through Yahoo! JAPAN real-time search. 10 queries: Terra, Codex weekly limits, Carbon.
5. **HN Algolia:** 9 queries, 2026-10-26..cutoff.
6. **GitHub:** Fei2411/real-api-pricing issues mentioning "terra"; openai/codex issue searches (Terra since 10-29; usage/rate/weekly since 10-26, 3 pages); #56866 re-read; phuryn/experiments; cross-repo issue search for "gpt-6.1-terra".
7. **OpenAI forum:** 5 searches after 10-28/29.
8. **Blogs and aggregators** (for cross-checks only): finopsllm, tokensave, developersdigest, xenospectrum NerfTrack, smzdm.
9. **YouTube** result metadata (watch pages redirect, so they are not used).
10. **Carbon availability:** Gemini API changelog, Gemini app release notes, Antigravity changelog, news searches, and the contrary El-Balad claim.

## Priority
1. Weekly Terra readings, Plus then Pro (both partitions).
2. New Plus 5h readings.
3. Discrepancy: cross-model calibration (Terra versus Sol on the same account), timing of the reported 10-27 metering change, CLI versus app, and claims about cache-read weighting.
4. Carbon availability.

## Discrepancy test design
Absolute tokens per 1% depend on the cache share, so stage 3 compares Terra with Sol on the same account and task. Under list-proportional metering, Terra should give 2× Sol's tokens per meter point. The test is whether independent observers agree on the measured ratio. If they do, the GitHub readings are consistent with the dollar-priced reports once each account's mix is accounted for.
