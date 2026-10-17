# Coding-provider supplement research plan

## Retrieval plan

1. Audit the existing community addendum instead of carrying its stated totals forward. Count JSONL records and query rows, verify uniqueness and every evidence/source and claim/evidence reference, then classify direct sources versus bounded search-outcome records.
2. Search date-scoped Reddit communities for Copilot, Cursor, Windsurf/Codeium, Kimi Code, Z.AI/GLM, Ollama Cloud, and OpenCode Go. Search Hacker News for the same providers and coding-plan allowance terms. Search developer forums and GitHub for current quota/reporting tools.
3. Open sources that are used. Record the publisher’s post date and the reported interval separately. Use exact plan language from the user/report; use `not stated` when absent.
4. Open first-party current quota and meter pages for policy context, and tracker/app documentation for the metering method. Do not use a tool’s synthetic sample as user data.
5. Triangulate each community observation against first-party plan semantics only to classify the evidence; do not “correct” the author’s plan or convert the account reading into an allowance estimate.
6. Draft claims only from linked evidence. Exclude mixed-window observations and product-transition reports from current provider estimates; retain a bounded explanation in the audit.
7. Critique category boundaries, cutoff handling, source diversity, plan specificity, provider coverage, and app claims. Run another targeted search where a material gap remains.
8. Package the report, source/evidence/claim ledgers, query log, phase log, critique, and validator output within this directory.

## Source route and stop rules

- Primary route: `web__run` search/open/find only. No external browser or direct HTTP fetch.
- Search English-language, publicly indexed pages. A search returning no eligible result supports only a bounded “not surfaced” statement.
- Stop promoting a result when it is pre-cutoff, its measurement period is not separable, its plan is implied rather than stated, the named product is a different service, or the source is synthetic/secondary without a user account observation.
- Store policy, user meter, local log, and API-rate-equivalent evidence in separate evidence rows.

## Planned output files

- `coding-provider-sources-addendum.jsonl`
- `coding-provider-evidence-addendum.jsonl`
- `coding-provider-claims-addendum.jsonl`
- `coding-provider-query-log.md`
- `coding-provider-research-addendum.md`
- `coding-provider-ultradeep-phase-log.md`
- `coding-provider-critique.md`
- `coding-provider-validation.log.md`
- `validate-coding-provider-package.js`

The existing core package and earlier community addendum remain intact; the manifest will point to this separate coding-provider supplement and the prior-addendum audit.
