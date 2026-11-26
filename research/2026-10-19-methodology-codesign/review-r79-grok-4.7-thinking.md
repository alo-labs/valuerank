I'll read the fourteen draft parts in order through the GitHub connector, starting with part 1.
The fourteen parts are in. I’ll check a few load-bearing public facts the draft relies on before writing the review.
0. Read check

The draft's first line is # ValueRank methodology — draft r161.

applying O145 moved the release cutoff (O65) and re-captured every source.

a configuration missing a leaf after the search is listed, not ranked (O36).

on the Plan basis the workload question is the M_W identification status.

the transfers keep their assumption label and caution.

A schema change moves the route to the possibly-superseded stage.

Domain validity is separate from evidence completeness.

field automationBenchPartialScore) | 10% | 10% | 10% | %, 0–100 |

repetitions are not a bias.

not described as target-workload support.

displayed margin to H beside its interval statuses.

neither may produce a confirmed, definite or certified-possible result).

Every cost check reads C_W, never the Index diagnostic.

the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

draft-r161.md in the same folder of the repository.

1. Findings by severity

Critical

None.

High

The frontier-families bar and anchor diagnostics do not exclude one-release retention. E187/E199 are supposed to recompute bars and anchors from frontier and near-frontier rows only. The draft then says every cohort row carries such a reason, including an O145 "left cohort" reason, so both diagnostics range over the whole cohort and equal the primary outputs. That is exactly when the diagnostic is needed: retained rows such as DeepSeek V4.1 Flash 1017, Gemini 4 Argon and MiMo-V2.6-Pro are inside the leading rankings and can set H and the anchors, while the sensitivity that should show the frontier-only answer is defined to match the contaminated one. The objective is value among frontier configurations, not among models AA has already dropped from the plotted frontier. Change: E199/E187 populations are rows whose inclusion reason is on the rendered frontier or inside the near gap. "Left cohort" stays in the ranking under O145, flagged, and is excluded from those two diagnostics. Publish the excluded IDs and the bar and exchange-rate deltas beside the headline bar.

The leading ranking's family-coverage sentence cannot be true on the draft's own lists. Part 1 defines 9 families as the 27 configurations on or near the v5 frontier. Part 2 says the max-effort ranking is 9 configurations from 9 of those 9 families. The same section puts DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high) and MiMo-V2.6-Pro in that ranking, and part 14 says those configurations left the rendered frontier and the near gap. They are retained families, not members of the 9. Nine rows cannot both be those retained families and be one row from each of the current 9. A buyer cannot tell which frontier families the default ranking covers. Change: replace that sentence with a generated family table (family, inclusion reason, primary, rankings in which it is ranked, missing leaves). Fail the E265 check if a "N of the N families" claim does not match that table.

Owner decision challenge to O133. The AI Coding Daily ranking still issues interval and scenario labels while its mandatory workload cross-check is τ_b 0.35 on 20 configurations, below the pre-registered 0.5 warning, and its admitted basket has no coding-agent unit (Coding Agent Index 7 of 20, threshold 14). Those labels are the public "cheapest above a bar" answer. They are computed on Index SDLC token cost that the draft's own test says does not order like cost per resolved Terminal-Bench task. O133 disclosed the pending units; it did not have this firing statistic as a reason to keep labels. Change: while E41's headline warning is firing, that ranking publishes displayed-record and scenario frequencies but authorises no confirmed, definite, or scenario-supported label. O12 is unchanged; this is not a release hold.

Medium

Plan admission can use a report window the search did not cover. The cutoff is 2026-11-01T06:10:00Z and the all-provider three-stage search is 2026-10-25, which the draft counts as 7 days and therefore legal under E218. The window still runs through 2026-11-01, and the summary says reports after the search cutoff were not searched. Only GPT-6.1 Terra and Gemini 4 Carbon were searched again on 2026-10-31. A concordant pair dated 26–31 October cannot be admitted because it was never looked for, so O11's "current window" is partly fictional. Change: a cell is admissible only for reports dated on or before that cell's three-stage search date, and the published window end is that date. Alternatively, fail the release unless every cohort model × plan cell has a three-stage search dated on date(V).

Owner decision challenge to using one cross-harness quality vector for labels (O10, O53). AI Coding Daily names a different harness per model, and Bug Hunt's estimand is model plus harness. The registered harness-stress branch is unevaluable while no model is listed under two tbench.ai agents, so the 10-point AI Coding Daily leaf can move a label by a harness effect the methodology cannot measure. Change: a leaf whose harness is chosen per model may change a displayed rank, but a label event uses only within-harness comparisons for that leaf (rows on a different harness are not cheaper-than witnesses for it). Keep the cross-harness table as the diagnostic that already exists.

Low

"Possibly superseded or expired" overstates the age table. SemiAnalysis's last Current day is 2026-11-05 and hard expiry is 2027-01-05, so the 21 and 60 flagged rows are change-flagged, not expired. Say "possibly superseded".

"Lacks every ranking's set" fights the next sentence, which correctly excludes a configuration only when it lacks both leading sets. The common-leaf ranking ranks 8 of the 12 "excluded" configurations. Say "both leading rankings".

Realised cost influence is 75% of value variance on the max-effort API basis and −65% on the AI Coding Daily API basis, against a nominal 25%. E196 already prints this. The remaining harm is that a negative allocation means the cost term offsets quality rather than penalising price, so "25% cost" does not describe the order. Add one headline sentence when the allocation is negative or above 50%: the order is not a 25/75 blend in variance terms. Do not change β (O2).

Artificial Analysis's public v5 index is the nine evaluations the draft uses, including FrontierCode 2.0 and Terminal-Bench-Science, and not GDPval-AA or AA-LCR as costed index components. OpenAI's help center does say that from December, Plus, Pro and Business will share one token allowance across ChatGPT and Codex, with Instant chat excluded and no per-plan sizes. The draft's "flags nothing until the effective release" treatment matches that page.
openai
+1

2. Methodology design recommendations

Fix the frontier-only sensitivity first. Let F be the ranked rows with inclusion reason on-frontier or near-gap, excluding left-cohort. Recompute H_k as the displayed quality at position floor((|F|−1)k/4), and rebuild the exchange rate from F's measured references, with the same ln 2 padding. Print both beside the frozen O145-inclusive bar. Do not replace the frozen bar without an O12 re-freeze.

Gate labels on the workload cross-check. If τ_b(C_W, d_ib) < 0.5 on a panel of at least 8, set that ranking's interval and scenario label fields to withheld and point to diagnostics.workloadCrossCheck. Keep the attribution that drops one basket component at a time, so a later admission of the Coding Agent Index can clear the warning without a methodology edit.

Close the report-window gap. Store searchDate(model, plan) from the staged log. A report counts toward O11 only if its E194 date is in [V−30 days, searchDate] and searchDate is at most 7 days before V. Cells with no such search still fail the build (E278).

Generate a family coverage table from the roster rather than prose counts: family, reason, primary effort, max-effort status, AI Coding Daily status, common-leaf status, missing leaves. That is the artifact a buyer needs in order to see that the default ranking is a top-effort slice, not the cost frontier.

For any leaf with a per-model harness, define the label witness set as rows whose recorded harness equals the candidate's. Ordinal ranks can stay mixed, labelled model+harness, until E19 becomes evaluable.

3. Questions for the owner

Should E199 keep including O145 "left cohort" rows on purpose? If yes, the diagnostic should be renamed, because it does not answer a frontier-only bar. If no, the exclusion in finding 1 stands.

4. Verdict

VERDICT: HAS FEEDBACK