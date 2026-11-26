# Internal review I62 — Claude Sonnet 5.5 (effort xhigh) on draft r121

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r121`
- Last line of the draft (line 174 of 174, the revision-history paragraph, 19,620 characters, beginning "Revision history: r16–r24 fixed…"). It ends: `…and widens the absence check to the registered vocabulary (it tests each registered absence statement, not every possible one). Every change is recorded with its rationale in the ledger.`
- Last 12 words of the last paragraph: "possible one). Every change is recorded with its rationale in the ledger."

What I read: `reviewer-prompt.md`; `ledger-brief.md`; `ledger.md` from "## Internal review I28" to the end (O45–O75, E247–E270, I29–I61, the O71 research outcome, O72, O73–O75, E269–E270); the root `AGENTS.md`; `review-i61-claude-sonnet-5.5-xhigh.md`; and every line of `draft-r121.md` in chunks (a folded read-copy in my scratchpad; line numbers below are those of the 174-line published file). I diffed r120 against r121 sentence by sentence (the changes are the E18 change-detection paragraph, the stage/provider sentences, the O73/O74 sentences, the E270 eligibility profile, the E44/E105 burn-evidence sentence, the IFBench and GDPval wording, the evidence-bundle sentences, the limitations sentence and the r121 history entry) and read the O71 record: `research/2026-10-25-plan-allowances/` (README, `stage1-assessment.md`, `stage1-deepseek-minimax.md`, the stage-2 report with its eligibility rules and tables, the stage-2 Anthropic and OpenAI notes) and `research/2026-10-25-plan-allowances-sb-deep-research/` (`decision-record.md`, `handoff.md`).

What I checked against data and code (it passed unless a finding says otherwise):

- `python3 -m valuerank.draft_figures check` exits 0.
- Cohort: I recomputed the near rule (F(c) − 3 on the rounded tooltip Index) from `data/aa_frontier_capture.json`: 190 points, 19 rendered vertices, 11 near points equal to the capture's 11 names; 30 cohort configurations from 13 families (8 with frontier points, 5 near-only); 9 + 16 − 4 = 21 ranked at least once; 9 in neither ranking.
- Ladders and counts: bar levels 53.27 / 63.54 / 64.94 over 9 rows (zero-based 2, 4, 6) and 38.00 / 49.24 / 58.61 over 16 (3, 7, 11); reach 7/5/3 and 13/9/5; plan rows 27 (14 assumption, 11 controlled, 2 API fallback) and 51 (48 assumption, 3 fallback); admission thresholds and 255 / 127 feasible subsets; exchange rates 3.04 / 4.06, 2.44 / 3.25, 2.83 / 3.77, 1.85 / 2.46; separability medians 2.762 / 2.763 and 4.431 / 4.425 with tolerances 1.88 / 2.19 / 2.96 / 5.26; FrontierCode cross-source (22 configurations, τ_b 0.766, mean offset 2.60, largest 11.60, so 0.55 and 2.44 points at 21%); Terminal-Bench agreement (τ_b 0.738 on 5 rows, undefined on 1).
- Engine against the specification: I recomputed the max-effort API cost scores and values from the frozen anchors (all nine rows equal the published values), GPT-6.1 Sol's quality as the weighted mean of its thirteen leaves, its GDPval transform, its Omniscience z, the Index cost reconciliation for every ranked page (relative error below 10⁻¹⁵), and the clip gate (no hold; the listed rows beyond the anchors match line 63).
- Evidence bundle: 19 artifacts, no null instant (I61 L2 is fixed); source clocks (Vals, AI Coding Daily, LiveBench, Bug Hunt captured after the cutoff from boards last updated before its day; tbench.ai and Cognition re-read unchanged).
- O71 and E269 in code and registry: the 2026-10-25 search-log entry (three stages, seven providers), `value_v3.check_o71_search`, `plan_routes.expiry_status` and `change_flagged`, the five SemiAnalysis Claude routes carrying `changeDetectedOn` 2026-10-17, the `possibly-superseded` flag on every Claude plan row, `GRADE = controlled 3 > reports 2 > assumption 1` (the O73 reading is what the comparator does), the O72 note in `evidencePolicy.o72Application`.
- Absence statements: the registered claims in `draft_figures.ABSENCE_CLAIMS`; IFBench is non-null on six AA pages, none of them a cohort configuration; MiniMax has no row and MiMo-V2.6-Flash only an `effort: default` row in the 203-row Bug Hunt scoreboard.
- The O71 verdict ("no model × tier passes") against the stage-1 assessment, the stage-2 tables and the stage-3 decision record: it holds under the stage-2 eligibility rules, which E270 now writes down.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. E139 and E270 give opposite answers on which reports O11 admits (line 53 against line 55).**

Line 53 (E139) says "O11 still admits concordant reports without a saturation requirement" and keeps "eligible delivered consumption observed, capacity not established" as a legal status, labelled "observed-usage multiple; full utilisation not established". Line 55 (E270, new) says a report counts only when its consumption is tied to a meter fraction or to exhaustion of a window, and "a lower bound does not count". A report with delivered consumption and no meter tie is admitted by the first and excluded by the second. The code follows E139's vocabulary (`CAPACITY_OBSERVED`; `concordant_pool` pools any scalar), and the O71 verdicts follow E270 (stage-2 rule 3).

Why Low: line 3 resolves it (between two editor rules the later number governs, so E270), and I found no cell today whose verdict flips on it. The nearest candidate, GPT-6.1 Sol on Plus (u/Pasto_Shouwa ≥ $65.6/week against #51604 ≈ $57/week, 1.15×), is also excluded by the one-model rule, because Pasto_Shouwa's session ran Sol High with two Luna High subagents. What is new against I61 L4 (adopted as E270): the adoption wrote the profile without amending E139, so line 53 is now a false sentence in the specification, and line 3 itself calls an unresolved clash "a defect corrected in the next revision".

Change: amend line 53 to say that E270 narrows it (a report with no meter tie is a diagnostic, not an O11 report) and keep the capacity-status vocabulary for controlled measurements and for meter-scaled reports.

**L2. E270 is not yet an executable statement of the reading the O71 verdicts applied (line 55).**

- It omits the partition-split criterion that decided the Claude and Kimi cells. The stage-2 report splits a partition only on "a provider statement, or a timestamped measurement in a public venue corroborated by other measurers"; stage 3 keeps the Claude 2026-10-17 split "user-evidenced", not provider-grade. E102 (line 53) says only "public evidence establishes the schema change". Two editors could split differently.
- It omits the Kimi rule (a report must come from the USD tier itself, stage-2 rule 7).
- "A tier the researcher infers counts provisionally" does not say what provisional does: whether it counts in the concordance test, toward the source count, or only as a flag. Stage 3 used a provisional report (K45SLE, $210–300/week) to make the Claude Pro cell fail even without #124 (1.53×), so the semantics decide a verdict. Nothing in `plan_routes.py` represents it.
- "One observer counts once, but every value the observer reports enters the range test" and "a range-valued report must pass across its whole range" cannot be stored. A report carries one scalar `multiple`, `concordant_pool` takes a list of scalars, and `check_report_independence` raises on a repeated observer. The first admitted pair would have to be encoded at a midpoint, which silently bypasses the whole-range rule.
- Line 57 still says "No extrapolation of short bursts to a billing period unless the controlled measurement establishes it", while E270 scales a meter fraction to its window and a weekly allowance to a month at 4.33. One sentence is needed on why the meter tie makes this not an extrapolation of a burst.

No route is affected today (no report route is admitted). The first admission would be the first execution.

**L3. E270's speed-mode conversion multiplies a user's figure by a provider-published usage multiplier; AGENTS.md says never to use one as the numerator (line 55).**

E270 converts Fast and Ultrafast figures with OpenAI's published 2.5× and 8×. AGENTS.md (second bullet of "Subscription allowance value-multiple evidence") says "Never use a model provider's published allowance, quota, usage multiplier, or marketing estimate as the numerator"; first-party information may establish fees and API rate cards. The user's figure stays the measured part, and a burn multiplier is closer to a rate card than to an allowance, so this is arguable. But line 3 says an editor record never overrides an owner rule, and "usage multiplier" is named. The conversion is used for one cell (GPT-6 Astra on Pro $100, ≈ $480 "Fast, standard-equivalent"), which fails with or without it: the standard-mode reports ($318 and $330–400) are 1.26× apart over the second report's range. Low; Q1.

**L4. E269's record is thinner than its sentence (line 55; `sourceEvidence.semianalysis.changeDetection`).**

- Plan scope. Every cited report concerns a Max account: NicoAica is Max 20x, push42 Max 5x, kakki-1 "Max"; Randomblock1 states neither model nor tier. The stage-3 table says "No Pro limit change in Anthropic's release notes [15]; 10-17 evidence concerns Max accounts" and keeps Claude Pro as one partition. E269 flags all five Claude routes, including Claude Opus 5.5 (max) on Claude Pro, which is the rank-1 Plan row in the max-effort ranking, and every transfer from it. I61 asked for the outcome per provider and plan; E269 records it per provider. Either record the plans each report covers and flag the Max routes, or state why a weekly-meter change presumptively covers Pro.
- Evidence left out. (i) SemiAnalysis's own X post of 2026-10-22, recorded second-hand in the Anthropic notes: an A/B test on some accounts that lowers monthly API value by about 20% (B arm: +19% five-hour window, −20% weekly budget). That is the measurer's notice about the regime the selected numbers describe, and AGENTS.md and E220 require the allocation regime to be preserved; line 53's regime sentence lists only the all-Opus and Fable shared-pool regimes. I61 L1 and its recommendation 6 raised the post; E269 does not mention it and the ledger records no decision on the recommendation. (ii) Anthropic's support bot told a user on 2026-10-20 "While we haven't made changes to how usage is calculated…". It is weak, but line 55's "no Anthropic statement" should read "no Anthropic announcement".
- Line 53 still says, for "every controlled measurement", "Its last Current day is 2026-11-05", while the five Claude routes are possibly superseded today; "or earlier on a detected change" covers it only by implication.

The effect is a label (and a blocker status in Plan interval outputs that are unevaluable today). The cost is that the record of why a label is present is incomplete.

**L5. The OpenAI "not flagged" outcome rests on where the announcements were posted, not on a documentation comparison (line 55).**

The registry reason is that OpenAI's announced Codex changes "were posted on X and the forum, not as changes to the pricing or rate-limit documentation". E18(a) is a scoped documentation diff since the measurement. The evidence bundle holds no provider-documentation artifact, so there is no baseline to diff, and the stage-2 notes say OpenAI's pricing page has no last-updated date. The honest outcome is "not evaluable". The same notes record OpenAI-announced accounting changes after 2026-10-06: Day 7 "no long-context fees on subscription usage", longer caching on Days 12, 16 and 19, and global meter resets on at least seven days; and conclude that "reports before and after ≈mid-October may belong to different accounting regimes". So Anthropic is flagged on user reports (weaker evidence) and OpenAI is not flagged on the provider's own announcements. This affects a label only, since no OpenAI Plan interval output exists, hence Low. Q2.

**L6. Two build statements in the O71 paragraph are stronger than the build (line 55).**

- "the build fails unless that search records every O71 stage in order and every cohort provider": `value_v3.O71_PROVIDERS` is a fixed seven-name tuple compared with the entry's self-declared `providers`; nothing reads the roster, and `draft_figures` removes "DeepSeek" from the printed list by name. It is correct for today's cohort. A provider that enters the cohort at a later refresh would not be demanded. This is the hand-kept-list-plus-gate pattern that took seven rounds on the Coding Agent Index (I50–I56) before the record was derived from the capture.
- "each stage recorded with its queries, reports, sources reached and sources unreachable" and "the search log (queries, sources reached and sources unreachable)": the 2026-10-25 entry has no `queries`, its stage objects hold only `stage`, `method`, `record` and `outcome`, and reached/unreachable are entry-level. The record files hold the detail. This is the unfinished half of I61 L3.

**L7. The active-rules manifest does not list "every gate, flag and rule" (line 152).**

Each ranking's manifest has 16 entries. It has none for the Plan evidence lifecycle or E18 (which fired for five routes today), the E170 valuation gate, the O59/O60 source clocks, the O69 row-date test, the O64 manifest, the E211/E216/E217/E218 freshness gates or the new O71 search gate. A reader of `scores.json` cannot see from the manifest that the change-detection stage fired. This is the manifest half of I61 L1, which the ledger does not address. Reword to "lists the gates and flags below" or add the entries.

**L8. Output 1 (line 13) still describes the Plan ranking without its API-cost rows.**

"displayed arithmetic on owner-named transfers, the O46 quota ceilings and measured multiples": 2 of 27 and 3 of 51 plan rows are API-cost fallback (Gemini 4 Argon (high) is rank 27 of 27 in the max-effort Plan ranking). The limitations paragraph now says so (line 169); I61 L7 asked for the headline too.

## 2. Methodology design recommendations

Prioritised. All use public data refreshed routinely.

1. **One versioned report-eligibility profile, in the registry and the code (L1–L3).** Put `reportEligibilityProfile` v2 in `plan_cost_routes.json`, hash it into the evidence bundle, and extend the report schema so the rules can be executed: per report `observer`, `modelExact`, `tier` and `tierBasis` (stated | inferred), `meterTie` (fraction | exhaustion | none), `values[]` (every value the observer reports, with `lo`/`hi` for a range), `speedMode`, window start and end. `concordant_pool` pools the union of values, so the whole-range rule is the ordinary max/min ≤ 1.20; the build rejects `meterTie: none`. Decide "provisional" in one line (for example: a provisional report counts in the concordance test, counts toward the two-source minimum only beside a stated-tier report, and flags the route "tier inferred"). Add the partition-split criterion and the Kimi USD-tier rule. Treat speed mode as an E102 comparability field (Fast reports pool only with Fast reports) unless the owner allows conversion (Q1). Amend E139 to say E270 narrows it. Fixtures: an observer with two values, a range-valued report, a lower bound, an inferred tier, a Fast report beside a standard one.

2. **Derive O71 coverage instead of declaring it (L6).** Generate `data/plan_allowance_cells.json` from the roster and the route registry: one record per (cohort provider, model, plan tier) with the stage outcomes, eligible report IDs, partition IDs, verdict and the profile hash. `check_o71_search` then requires every roster provider and every cell; per-stage `queries`, `reached` and `unreachable` become fields. The provider list and the "(DeepSeek sells no first-party plan)" clause become placeholders. This is I61's recommendation 2 narrowed to what the build needs; O75's cadence is unchanged.

3. **Make E18 a computable step (L4, L5, L7).** At each release capture and hash the scoped sections of each provider's plan pricing and limit pages into the evidence bundle and diff them against the previous release's. Add `providerNotices[]` (date, URL, provider, plans covered, touches metering or accounting yes/no) and a per-provider-and-plan outcome table with the evidence IDs that triggered it. Triggers: (a) a scoped diff, (b) a provider notice that touches metering (Q2), (c) at least two independent reports for that plan. List the stage in the active-rules manifest.

4. **Show how exposed a flagged route is (L4).** Print per flagged route the multiple scale k at which the row passes the median threshold, using the existing E242 arithmetic row-wise, and add a named S2 stress for flagged routes only, outside Θ and never a label (O19). Today the top six max-effort Plan rows are all Claude (63.46–64.16) and the seventh is GPT-6.1 Sol on Pro $500 (62.61). At the max-effort Plan anchors (ratio 1,219; 2.44 value points per doubling) a multiple scaled by 0.8 moves a Claude row 0.79 points, by 0.5 moves it 2.44, by 0.2 moves it 5.66, against a median threshold of 2.76 (tolerance 2.19×). So SemiAnalysis's own −20% arm leaves the order unchanged, while the roughly 5× per-token change reported in claude-code #102667 would not. Record SemiAnalysis's 2026-10-22 notice under `sourceEvidence.semianalysis.measurerNotices`.

5. **Close the I61 residuals (L7, L8).** Manifest wording or entries; one clause in Output 1 naming the API-cost Plan rows with the generated counts.

## 3. Questions for the owner

- **Q1 (L3).** May a provider-published speed-mode burn multiplier (OpenAI Fast 2.5×, Ultrafast 8×) convert a user's API-priced figure, or must Fast-mode reports pool only with Fast-mode reports so that no provider multiplier touches the numerator? The answer sets the speed-mode line of recommendation 1.
- **Q2 (L5).** Should a provider's own announcement of a change to how subscription usage is metered (OpenAI Days 7, 12, 16 and 19; not a documentation edit) make that provider's routes "possibly superseded"? If yes, the GPT SemiAnalysis routes and the GPT transfers carry the flag now.
- **Q3 (O73 with E269).** When the controlled route is flagged possibly superseded by a detected change and a concordant in-window report pair dated after the change exists for the same model and tier, does O73's precedence still hold? The comparator says the stage is not a comparator key, so the older controlled figure would win. No such pair exists today; the nearest cell, Claude Pro × Opus 5.5, is blocked only by #124, so the question would arise at a refresh.

## 4. Verdict

No Critical, High or Medium finding; eight Low. r121 implements the I61 resolutions faithfully where it implements them: the comparator does what O73 says, the E18 outcome is recorded and flows to the route flags, the stage and provider sentences are generated and checked, the evidence bundle has no null instant, and every figure and every O71 statement I could check against the data, the code and the research record holds. The Lows are a specification clash left by E270 (L1, L2), one possible owner-rule conflict (L3), a record that is thinner than the sentence it supports (L4, L5), two build claims stronger than the build (L6, L7) and a headline omission (L8). None changes a score, a rank, a label that a published claim depends on, or a gate outcome today. Under O56 the Lows, the recommendations and the questions are considered but do not make the round non-clean.

VERDICT: NO FURTHER FEEDBACK
