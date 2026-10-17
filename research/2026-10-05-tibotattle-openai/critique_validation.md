# Critique and validation record

**Audit date:** 2026-10-05. **Assigned scope:** `/Users/shafqat/valuerank/research/2026-10-05-tibotattle-openai/`.

## Research phases

| Phase | Status | Evidence / limitation |
|---|---|---|
| Scope | Complete | Locked the rule that numeric Codex crowd allowance values may come only from TiboTattle's homepage; set other app research to discovery/capability only. Retained the one-month empirical cutoff in the manifest. |
| Plan | Complete | Preserved the existing source map and added direct homepage, docs, privacy, community-discovery, and alternative-product checks. Exact audit queries are in `query_log.md`. |
| Retrieve | Complete for the homepage and key publisher pages | Reopened the homepage, docs, privacy overview, repository, direct community post, official OpenAI help, publisher repositories, and App Store listings using Codex built-in `web__run` only. CUStats homepage/privacy body text was not readable; targeted in-page searches did expose current App Store listing text for CUStats and several adjacent apps. |
| Triangulate | Complete for the central finding | Compared the homepage's visible loading text with the docs/privacy description of community estimates and sample provenance. The direct Reddit post confirms product discovery only; its numerical content is excluded. |
| Synthesize | Complete | The report distinguishes community aggregate, account-specific provider signal, and local token/cost estimate. It states no observed Codex allowance value rather than inferring absence or using another source. |
| Critique | Complete | Removed an unverified prior availability label, flagged the homepage demo as illustrative, corrected sharing-default wording, and retained date ambiguity for the direct Reddit post. |
| Refine/package | Complete | Added `query_log.md`, `citations.md`, and this review record; updated the source/evidence/claim ledgers and manifest. |

## Independent checks performed

- Homepage capture opened on 2026-10-05 via `web__run`: allowance-panel state is “Checking allowance estimates” / “Checking for published allowance estimates…”. Separate daily activity is also in a checking state. No numeric community allowance value or sample count was visible.
- The page's separate interactive allowance visualization is explicitly labelled illustrative and not live account data, so it is excluded.
- The existing S01-S36 sequence was preserved and S37 was appended for the newly opened direct community discovery post. The source inventory therefore contains 37 source records/URLs; S05, S23, and S24 are search-discovery artifacts, not substantive evidence.
- The report table contains eleven product rows: TiboTattle, OpenUsage, CodexBar, CUStats, SessionWatcher, AIUsage, ccusage, VibeCheck, Model Usage, TokenBar Mobile, and Codexex.
- Evidence items E01-E02 are the only entries marked admissible for a numeric Codex allowance, and both point to S01 with `numeric_allowance_value: null`. The new Reddit item E26 and all alternative-app evidence remain inadmissible.
- Source S37 is used only for product discovery. Its relative-time label does not establish a calendar publication date, so it is not used for an empirical recency claim.
- The report now states the actual sharing-default disclosure and labels sample-identity/overlap caveats as publisher descriptions, not independently verified facts.

## Critique findings and remaining limitations

- The central status is a retrieval-time snapshot. A later homepage render may publish data, and this result does not show that a value has never existed.
- The app set is bounded discovery, not an exhaustive app-store or worldwide census. Publisher pages can change.
- CUStats homepage and standalone privacy captures did not expose substantive text. Its current Mac App Store listing did expose the product description through a targeted search; the table now relies on that listing and clearly dates the older privacy record.
- The direct community post includes quantitative claims, but none are extracted or cited in this package; its calendar publication date is unresolved.
- Earlier audit attempts encountered local routing and language-dispatch issues. They are superseded by the completed package and routed validation recorded below; the skill was not unavailable.
- No Codex account, local usage logs, private workspace data, or independent contribution database was inspected.

## Ultradeep completion update

The documented phases and skill were accessed using the registered `silver-bullet` LeanCTX root and `ctx_read(repo="silver-bullet")`. The manual Ultradeep artifacts are in [ultradeep/](ultradeep/); three adversarial critique cycles are in [ultradeep/critique.md](ultradeep/critique.md). The automated `/sb:deep-research` command was not invoked.

- SB phase gate: exit 0; all 9 phases passed.
- Report validator: exit 0; all required checks passed; recommended Counterevidence Register and Claims-Evidence Table sections were added after an initial warning.
- Claim-support validator: exit 0 on a temporary copy; 10 supported claims, zero unsupported factual claims. The original legacy ledgers remain unchanged.
- Source/evidence/claim field, hash, and cross-reference audit: passed for 37 sources, 28 evidence rows, and 10 claims.
- Citation verifier: exit 0 in non-strict mode, 15/17 URLs verified, one generic-short-title flag, and one HTTP 403. Citation [5] retains the source ledger's page title, which the heuristic flags because it contains “guide” and has fewer than five words. Citation [12] is the official OpenAI Help Center URL; its HTTP 403 is a validator accessibility result, not a claim that the page content was unavailable in the built-in web review. The non-strict validator passed with warnings; exact output is in [ultradeep/validation/verify_citations.log](ultradeep/validation/verify_citations.log).

The package exceeds the Ultradeep preferred source budget of 30 by seven, while remaining under the configured maximum of 40. This exception preserves the prior audit trail and bounded app coverage; the inventory and treatment are documented in the workflow record. There were zero user-reported allowance datapoints, so no plan tier was omitted; future datapoints must state the exact tier or `not stated`.
