# Query log: current-window Claude allowance evidence

**Run date:** 2026-10-06. **Search order:** Reddit first; then GitHub, current provider policy, and selected tracker repositories. **Audited measurement-date window:** 2026-09-06–2026-10-06 inclusive; post dates are provenance only.

## Reddit-first searches

| Exact search query | Result and disposition |
|---|---|
| `site:reddit.com/r/ClaudeCode "weekly limit" Claude September 2026 Max usage` | Returned the Sep 13 Max20 transcript/API-price report (S-C03) and related complaints; direct post metadata and body checked. |
| `site:reddit.com/r/ClaudeAI "Pro x5 plan" weekly limit September 2026 reset` | Returned Sep 23 reset discussion (S-C20); plan wording and current 50% weekly-meter statement checked in the post body. |
| `site:reddit.com/r/ClaudeCode "Opus 5.5 Medium" usage October 1 2026 limit` | Returned Oct 1 comparisons, including S-C16 and S-C17; direct Reddit JSON metadata/body checked. |
| `site:reddit.com/r/ClaudeAI "weekly limits" "pro plan" October 2026` | Returned Oct 5 post S-C18; direct Reddit JSON publication timestamp/body checked. |
| `site:reddit.com/r/ClaudeCode Claude Max weekly limit usage API cost September 2026` | Earlier Reddit-first discovery query retained from the initial search pass; located S-C03. |
| `site:reddit.com/r/ClaudeAI "weekly limit" Max 5x Max 20x September 2026` | Earlier Reddit-first discovery query retained from the initial search pass; located S-C04 and date-screened related items. |
| Reddit recent-report lead search (independent subagent) | Led to Oct 5 S-C19, Oct 1 S-C16/S-C17, Sep 23 S-C20/S-C21 and an excluded removed report. Candidate permalinks were opened directly by the primary researcher. Exact searches and date provenance are retained below. |

### Independent Reddit lead query addendum

These are the exact `web__run` search strings used in the supplemental lead pass:

1. `site:reddit.com/r/ClaudeAI "October 1, 2026" allowance usage limits`
2. `site:reddit.com/r/ClaudeAI "October 5, 2026" allowance usage limits`
3. `site:reddit.com/r/ClaudeAI "September 23, 2026" allowance usage limits`
4. `site:reddit.com/r/ClaudeAI "Thursday October 01 2026" "limit" "used"`
5. `site:reddit.com/r/ClaudeCode "Thursday October 01 2026" Claude "usage" (weekly OR quota OR limit)`
6. `site:reddit.com/r/ClaudeAI "Wednesday September 23 2026" "usage" (percent OR % OR limit)`
7. `site:reddit.com/r/Claude_reports "Thursday October 01 2026" "usage" Claude limit`
8. `site:reddit.com/r/ClaudeAI "Monday October 5 2026" limit usage`

The earlier lead pass recorded dates from indexed snippets and relative page labels; those labels are discovery metadata, not direct `created_utc` evidence. Subsequent direct Reddit JSON checks confirmed exact UTC post dates for S-C16, S-C17, and S-C20. Measurement eligibility is checked against each reported interval, not its post date.

### 6 October Reddit-first search addendum

Exact built-in web search strings run on 2026-10-06:

1. `site:reddit.com/r/ClaudeCode "October 6, 2026" (usage OR limit OR reset OR meter)`
2. `site:reddit.com/r/ClaudeAI "October 6, 2026" (usage OR limit OR reset OR meter)`
3. `site:reddit.com/r/ClaudeAI "Oct 6" "weekly limit" Claude usage`
4. `site:reddit.com/r/ClaudeCode after:2026-10-05 before:2026-10-07 Claude Code plan limit usage`

These indexed results surfaced no qualifying Oct 6 user-reported API-priced allowance report. This is bounded search coverage; it does not establish that no such report exists.

## Direct source checks

| Route | Sources checked | Purpose |
|---|---|---|
| Reddit post JSON and permalinks | S-C03–S-C07, S-C14–S-C21 | Confirm post metadata/body; distinguish publication, observation, and retrieval dates; capture plan wording exactly. S-C05 and S-C14 detailed ledger entries include full/partial or current/historical segments. |
| GitHub issue pages | S-C08–S-C09 | Confirm opening dates and classify reports as individual anomalies, not allowance estimates. |
| Official Anthropic Help Center | S-C01–S-C02 | Current plan-policy context checked 2026-10-05. |
| Tracker pages/repositories | S-C10–S-C13 | Inspect only the current public output/project descriptions for tool-discovery context; no security or privacy audit performed. |

## Date and coverage rules

- Search results are discovery leads; source posts and metadata were opened before recording findings where available.
- Reddit's `created_utc` metadata resolved exact publication times for S-C05, S-C14, S-C16, S-C17, S-C18, and S-C20. Observation dates come from each author's body and are separately labeled.
- The 2026-09-06–2026-10-06 cutoff applies to measurement interval start dates, not post dates. S11 (S-C15) and S12's 23 Aug comparator are pre-window; S12's 22 Sep point is in-window context but not API-priced.
- S-C19 was published inside the window but gives only “about a week” and no comparable tasks; it is reported as an uncontrolled hypothesis, not a measured effect.
- A separate Oct 1 candidate was removed before capture and was not ledgered. Private, deleted, login-only, unindexed, non-English, or differently worded content may also be absent. Search coverage is bounded, not exhaustive.
