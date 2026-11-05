# DR-SCOPE: O71 stage 3 for GPT-6.1 Terra and Gemini 4 Carbon (Silver Bullet Deep Research, deep mode)

Date: 2026-10-31. `date -u` gave Sat Oct 31 05:52 UTC 2026. Release cutoff: 2026-10-31T04:10:00Z. Report window: 2026-10-01..2026-10-31.

## Bounded question
1. **GPT-6.1 Terra** (OpenAI, released 2026-10-26; API $1 input / $0.05 cached / $5 output per 1M tokens), on ChatGPT Plus, Pro $100, Pro $200 and Pro $500 in Codex. Find actual end-user reports of the API-list-price allowance per unit (5-hour, week, month), with these constraints:
   - Pro plans have no 5-hour window.
   - Pro readings before and after the Day 25 doubling (2026-10-29) are separate partitions.
   - A reading that spans the Day 23 global reset (2026-10-27 PT, announced 2026-10-28 02:42 UTC) is excluded.
2. **Gemini 4 Carbon** (Google, announced 2026-10-28). Confirm whether it was available on any Google consumer plan (AI Plus, AI Pro, AI Ultra; Gemini app, Antigravity) as of the cutoff, and record any allowance reports.

Then judge each model × tier × unit cell against O11: two independent, non-provisional reports, with the largest lower bound ≤ 1.20 × the smallest upper bound (O86).

## Extend, not repeat
Stages 1 and 2 are in `../stage1-openai-terra.md`, `../stage1-google-carbon.md`, `../stage2/report.md` and `../stage2/research_notes/`. They found:
- two concordant Plus 5-hour Terra reports: pensuke89 at $5.28–5.51 per 5h and IndividualPlus2011 at $5.33 per 5h;
- no weekly or Pro report;
- an unsettled discrepancy with openai/codex #56866, whose meter readings implied a meter 2–3× faster per token.

Stage 3 priorities, in order:
1. weekly and Pro readings;
2. source classes not yet reached (LINUX DO via a mirror, Bluesky via an alternate API host, X via Japanese real-time search, YouTube result metadata, the Fei2411 community dataset, note.com);
3. settling the discrepancy.

## Eligibility profile (data/plan_cost_routes.json, evidencePolicy.reportEligibilityProfile, O71 v1 E270)
- API-priced consumption must be tied to a meter fraction or to window exhaustion. A figure without a meter fraction is only a lower bound.
- A 5-hour figure pools only with other 5-hour figures (O82).
- A week converts to a month at 4.33 weeks.
- Exact model and tier are required. A tier or model that the researcher infers counts as provisional.
- The report must cover one model, at least partly inside the window, not on an accounting-fault day (OpenAI: 2026-10-16/17).
- One observer counts as one report.
- Ranges are compared on bounds (O86).
- Speed modes are converted to standard at the provider multiplier.
- Partition splits follow `partitionSplits`: OpenAI Pro 100/200/500 limit change on 2026-10-29; OpenAI resets on 10-27 and earlier.

## In scope
End-user reports dated 2026-10-26 (Terra launch) or 2026-10-28 (Carbon announcement) up to the cutoff. Also in scope: provider statements about Terra metering, and evidence about Carbon availability.

## Out of scope
- Other models, except as cross-model calibration for the Terra meter (Sol on the same account).
- Business, Team and Enterprise plans, except as context.
- Editing any file outside this folder.
- Committing.
- Signing in, solving bot checks, or using paid services.

## Assumptions
- A1 (high, user-confirmed): the API list prices above apply.
- A2 (high, user-confirmed): the eligibility profile is the operative reading of O11.
- A3 (medium, implicit): a reporter's usage tool prices tokens at list unless shown otherwise. Where the tool's split is partial, feasibility at list prices is checked.
- A4 (medium): a mirror of a forum (locdd.com for LINUX DO) faithfully reproduces post text and images. Checked by matching timestamps and onebox references to linux.do.
