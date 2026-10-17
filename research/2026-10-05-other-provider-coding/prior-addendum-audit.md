# Prior community addendum audit

**Audited:** 2026-10-05  
**Files reviewed:** `community-sources-addendum.jsonl`, `community-evidence-addendum.jsonl`, `community-claims-addendum.jsonl`, `community-query-log-addendum.md`, and `run_manifest.json`.

## Independently verified counts

| Measure | Verified | Interpretation |
|---|---:|---|
| Community source JSONL rows | 21 | 19 direct source records (`A01`–`A19`) plus two bounded search-outcome records (`AQ01`–`AQ02`). |
| Direct source records | 19 | This is the “19-source” count in the assignment brief. |
| Bounded search-outcome records | 2 | These are not posts or direct source pages; keep them distinct from direct sources. |
| Community evidence rows | 13 | `E01`–`E13`. |
| Community claim rows | 9 | `A-C01`–`A-C09`; the earlier manifest’s 9-claim count is correct. |
| Exact query rows | 22 | `Q01`–`Q22`; all query IDs are unique. |
| Core + community source URL rows | 60 | 39 core rows plus 21 community rows. |
| Unique URLs across both source sets | 58 | Two duplicate URLs were independently identified: the Cursor Sep 30 mixed-cycle report and the Google AI Plus report. |

The project manifest’s `source_records: 21` is the raw supplement row count, not the number of direct posts/pages. It should not be summarized as “21 community reports.” The 19-direct-source, 2-search-outcome split above reconciles the manifest with the 19-source description.

## Structural checks

`validate-coding-provider-package.js` was run against the existing files through the installed `lean-ctx` script route. It parsed the JSONL files; verified unique source, evidence, and claim IDs; checked every evidence-to-source and claim-to-evidence reference; counted exact query rows; and recomputed the URL overlap totals. Result: **PASS, zero errors**. See `coding-provider-validation.log.md` for the recorded command and result.

The old manifest said `source_ids_unique`, `evidence_ids_unique`, `claim_ids_unique`, and `crosswalks_manually_checked` were true, but no reproducible validator/log was in that package. Those assertions were therefore self-reported until this recheck. The new script verifies structural consistency; it does not certify the truth of a user’s account, screenshot, plan, or usage claim.

## Content and date audit

- The Sep 30 Cursor Ultra report explicitly covers Sep 2–30. The addendum correctly excludes its cumulative figures because it does not isolate Sep 5–30.
- The Sep 6 Copilot quota-wipe post’s quantified events occurred on Aug 11 and Sep 2; the addendum correctly excludes those amounts and keeps the Oct 1 update qualitative.
- The Sep 10 Copilot “first couple weeks” interval could include Sep 1–4; its exclusion is appropriate.
- The paid Devin report in `r/windsurf` is labeled as Devin, not current Windsurf plan evidence. That product boundary is correct.
- The Oct 4 Pro+ discussion is a question from an employer-provided account with a reported 7,000 monthly credits. Its replies give different account allocations and periods. It is discussion context, not a plan-normalized consumption estimate.
- The Google AI Plus, Antigravity diagnostic, non-coding Gemini, and tracker-project records are explicitly scoped or excluded in the claims; they should not be pooled with coding-plan consumption.
- `E01` bundles the Cursor forum poster’s Sep 5 usage and later Sep 15–16 commenters’ percentage-jump anecdotes in one evidence row. Those are separate people and should remain described as separate observations in synthesis; the older row does not preserve commenter-level plan/model fields.
- Several claims summarize anecdotes with low or very-low confidence. The package appropriately does not turn them into provider quota figures. Reporter identity and raw account exports are not independently verified.

## Audit disposition

The earlier 19-direct-source / 13-evidence / 22-query totals reconcile. The completed coding-provider Ultradeep package has a separate, recorded validation pass: the nine-phase Silver Bullet gate, report contract, citation verification, claim-support check, and custom package validator all passed. The Silver Bullet skill and workflow were available through the registered LeanCTX root; the `/sb ultradeep` orchestration command itself was not invoked. The MCP `ctx_execute` capacity failure is recorded as a separate sandbox execution limit; the supported local LeanCTX route ran the validators successfully.

The old E01 aggregation remains a content-level limitation: it combines distinct Cursor commenters without commenter-level plan/model fields. Do not treat that row as one user's observation or use it to establish a single tier's usage. The new coding-provider supplement uses one evidence row per distinct user/plan/measurement class where the source allows separation. Keep the prior manifest's historical validation flags distinct from the new reproducible checks, and preserve all limitations above.
