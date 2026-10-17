# Query and source coverage log

**Run date:** 2026-10-05. Browser: built-in browser only. The browser's full query-history export was unavailable, so this is a query-family log reconstructed from the executed search sequence and inspected result set; it is not a verbatim query transcript.

## Initial CUA browser attempt (2026-10-05)

The expected built-in `iab` browser was unavailable in the current CUA session. `cua.createBrowserTab('iab', …)` returned “Browser is not available”; browser inventory exposed only Edge extension sessions. Because this task requires the built-in browser and prohibits substituting an external browser, I did not run the new search queries in another browser. Therefore the following are the exact proposed query strings for the requested provider-by-provider recheck, **not executed queries and not evidence of negative search results**:

| Route | Exact proposed query | Execution | Outcome |
|---|---|---|---|
| Reddit / Perplexity | `site:reddit.com Perplexity ("usage limit" OR quota OR reset OR "Pro searches") after:2026-09-04` | Not executed | Built-in browser unavailable; no inference about results |
| Reddit / Grok | `site:reddit.com Grok ("usage limit" OR quota OR reset OR weekly OR SuperGrok) after:2026-09-04` | Not executed | Built-in browser unavailable; no inference about results |
| Reddit / Mistral | `site:reddit.com Mistral ("usage limit" OR quota OR reset OR points OR "Le Chat") after:2026-09-04` | Not executed | Built-in browser unavailable; no inference about results |
| Reddit / DeepSeek | `site:reddit.com DeepSeek ("usage limit" OR quota OR reset OR messages OR points) after:2026-09-04` | Not executed | Built-in browser unavailable; no inference about results |
| Reddit / Poe | `site:reddit.com Poe ("usage limit" OR quota OR reset OR points OR messages) after:2026-09-04` | Not executed | Built-in browser unavailable; no inference about results |
| Reddit / Meta AI | `site:reddit.com ("Meta AI" OR "Meta One") ("usage limit" OR quota OR reset OR messages OR allowance) after:2026-09-04` | Not executed | Built-in browser unavailable; no inference about results |
| Hacker News / all six | `site:news.ycombinator.com (Perplexity OR Grok OR Mistral OR DeepSeek OR Poe OR "Meta AI") after:2026-09-04 (limit OR quota OR usage OR reset OR points)` | Not executed | Built-in browser unavailable; no inference about results |
| Developer forums / all six | `(Perplexity OR Grok OR Mistral OR DeepSeek OR Poe OR "Meta AI") (usage limit OR quota OR reset OR points) after:2026-09-04 (GitHub OR forum OR tracker)` | Not executed | Built-in browser unavailable; no inference about results |

These query strings target paid-consumer plan observations, account meters, reset windows, action/point counts, and submitted tracker datasets. Any matching posts would still require page-level inspection for publication date, separately identifiable measurement interval, exact plan/model/action, and a reported method. Free, API, and enterprise sources would remain excluded from paid-consumer measurement evidence.

## Query families and order

1. **Official policy, all providers:** provider name + `subscription plan`, `usage limits`, `quota`, `weekly limit`, `messages`, `credits`, `points`, `reset`, `allowance`; official help/pricing pages prioritized.
2. **Reddit first, provider by provider:** `site:reddit.com` plus provider name and terms `limits`, `quota`, `usage`, `reset`, `messages`, `weekly`; focused recent-result checks attempted for Perplexity, Grok, Mistral, DeepSeek, Poe, and Meta AI.
3. **Hacker News second:** provider name + limit/usage; one relevant Grok 4.7 thread/comment inspected.
4. **GitHub/developer communities third:** `site:github.com` plus `AI usage tracker`, `Grok`, `Perplexity`, `quota`; inspected one local browser extension README, with two additional developer-tool search leads retained as unverified discovery-only sources.
5. **Tracker search:** `allowance tracker`, `usage tracker`, `Grok Perplexity limits`, followed by tracker product/about pages for TokenKarma and WeeklyUsage.

## Source counts and handling

- Core registry contains **54 distinct URLs**. The later community addendum adds 25 source records; seven URLs overlap, for **72 unique URLs** across both registries. Status is explicit: opened pages, opened redirects, signed-out observations, indexed links, search-result-only leads, and older discovery-only pages are not conflated.
- Official policy sources are policy context even if a page's update date predates the community cutoff. They do not count as community measurements.
- Current community window: publication on or after **2026-09-05** through **2026-10-05**. Community publication date and measured interval are separate fields in `sources.jsonl` and `evidence.jsonl`.
- The initial package inspected three in-window community leads (DeepSeek Reddit, Mistral Reddit comment, HN Grok). The later addendum records 11 additional current-window Reddit/HN reports, including unverified account-specific numeric claims; none supports a reproducible, normalized cross-account plan allowance estimate.
- The inspected Grok Reddit report dated 2026-08-27 is pre-cutoff and discovery-only. No older community report is used to estimate current allowance. No mixed-window report was used.
- API documentation for xAI, Mistral, DeepSeek, and Poe was marked as a separate surface. Enterprise Perplexity limits were not applied to consumer plans.

## Coverage gaps

- Perplexity/Poe/Meta/Grok/Mistral/DeepSeek search indexing may omit posts, private communities, region-specific posts, deleted items, and account-gated content. The searches are not exhaustive.
- The initial Reddit result coverage was uneven. The Oct 5 supplemental search subsequently found recent Perplexity, Grok, Poe, Meta, and Mistral posts; those findings and query-level boundaries are in [`community-query-log-addendum.md`](community-query-log-addendum.md) and [`community-research-addendum.md`](community-research-addendum.md).
- Relative dates displayed by sites are approximate and recorded as approximate. They represent publication date as seen on the run date, not measured usage interval.
- No claim is made that no qualifying reports or trackers exist anywhere. The result is limited to the pages and result sets inspected.

## Workflow note

Documented Deep Research Ultradeep phases were followed in a degraded browser-led sequence: scope, retrieval, date-gated triage, triangulation, synthesis and limitations. Silver Bullet was unavailable and was not invoked or retried. Deep Research skill core file was read; detailed methodology/quality-gate reference files could not be retrieved through the routed file-read mechanism. No unsupported claim of exhaustive Ultradeep execution is made.

## Subsequent provider-specific follow-up (2026-10-05)

The initial CUA browser route was unavailable, but the expanded research was later executed using Codex's built-in web research route, consistent with the built-in-browser-only instruction. Reddit was searched first provider-by-provider, followed by Hacker News, official policy pages, app/repository searches, and developer sources. The exact executed query set and result notes are in [`community-query-log-addendum.md`](community-query-log-addendum.md); the current-window reports, allowance caveats, and tracker findings are summarized in [`community-research-addendum.md`](community-research-addendum.md).

The addendum records 11 current-window Reddit/HN allowance discussions with publication and reported measurement intervals separated. Several include disputed or account-specific numeric statements, but none yields a reproducible normalized allowance across users. The expanded search also identified personal quota tools for Grok, Perplexity, Poe, and multiple providers; no independently verifiable shared crowd database was established. This is a bounded finding, not an exhaustive proof of absence.
