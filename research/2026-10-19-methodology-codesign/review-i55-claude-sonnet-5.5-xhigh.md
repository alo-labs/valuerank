# Internal review I55 — Claude Sonnet 5.5 (effort xhigh) on draft r113

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r113`
- Last line of the folded copy (986 lines): `recorded with its rationale in the ledger.` (the closing fragment of the revision-history paragraph that ends "r113 (fifty-fourth internal review) makes the agent-label grammar strict … renders both bases' subset strata. Every change is recorded with its rationale in the ledger.").
- Last 12 words of the last paragraph: "subset strata. Every change is recorded with its rationale in the ledger."
- Read in full: the reviewer brief, `reviewer-prompt.md`, the folded draft (lines 1–986), `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (the I54 entry included), `review-i54-claude-sonnet-5.5-xhigh.md`, and `AGENTS.md` (as supplied).
- Checked against code and data (not only the text):
  - `valuerank/value_v3.py` (`AGENT_EFFORTS`, `_KEYED_EFFORT`, `_PLAIN_EFFORT`, `_CANDIDATE_TAIL`, `parse_agent_label`, `exact_agent_records`, `agent_record_for`, `assemble`, `check_leaf_searches`, `check_open_web`, `check_comparability`, `leaf_supplements`, `check_source_clocks`, `configurations_from_scores`, `build`), `valuerank/anchors.py` (`ONE_CONFIGURATION`, `panel_cost_influence`, `cost_influence`, `variance_allocation`), `valuerank/basket.py`, `valuerank/plan_routes.py`, `valuerank/build_scores.py` (the gates it cites), `valuerank/draft_figures.py`, `research/2026-10-23-swe-benchmarks/build_swe_tracks.py` (`select_aicd`), the commit `73f390b` diff (code, tests, data).
  - `data/scores.json`, `data/aa/coding_agents_capture.json`, `data/v3_configuration_map.json`, `data/plan_cost_routes.json`, `data/provider_claims.json`, `data/figures.json`.
  - Ran `python3 -m valuerank.draft_figures check` (exit 0) and `pytest tests/test_anchors.py tests/test_value_v3.py tests/test_draft_figures.py` (124 passed). I wrote no repository file other than this review; my probe scripts are in the session scratchpad and `git status` is clean.
- The two I54 handlings, verified:
  - Strict agent-label grammar: all six forms the draft lists (a disagreeing pair, an unknown or differently cased effort, an extra bracketed group, a keyed group with other keys, reversed order, trailing spaces) do stop the build for GPT-6 Luna (max), and the capitalised-effort, unknown-word and trailing-space forms also stop on every one of the eight real cohort labels they apply to (the mutation run in M1); the real two-form label still reads as GPT-6 Luna at max; a longer name ("GPT-6 Luna Pro", "DeepSeek V4.1 Flash" against "DeepSeek V4.1 Flash 1017") is not a candidate; running `agent_record_for` over all 29 cohort configurations returns 8 records (the draft's 8 of 9 in the max-effort ranking; 3 of 15 in the AI Coding Daily ranking) and the map holds no pin ("none today"). The guard is narrower than its wording (M1).
  - One-configuration Plan stratum: `panel_cost_influence.summarise` returns `ONE_CONFIGURATION` for two or more rows of one configuration (identified by `configurationId` or the id before "@"); the max-effort ranking's 4-row MiMo-V2.6-Pro Plan subset stratum reads "undefined (one configuration)" with costShare and varianceAllocation null and both flags false; the AI Coding Daily ranking has no subset stratum; every common-workload and displayed-table panel reads "defined"; the API stratum reads "undefined (panel too small)"; the unit test and the figure (both bases) agree with the text. Wording only (L2).
- Re-derived from data and found correct (not raised): the displayed quality of all 24 ranked rows from the leaf z-scores and the track weights (13 and 11 leaves summing to 100; 0 mismatches), the API value of all 24 rows from the frozen anchors, and the cost score, value and cost (API cost ÷ multiple) of all 77 Plan rows (0 mismatches); the exchange rates (3.04/4.06 and 2.83/3.77 from anchor ratios 297.5 and 460.1); the bar ladders and reach (54.23/64.26/65.00 and 38.0/49.2/57.2; 7/5/3 and 12/8/5); the separability counts and medians (0 of 8 at 2.84, 1 of 14 at 4.45; Plan pairs 9 and 19 with 17 and 30 same-configuration pairs counted apart); the E242 tolerances (2^(2.84 ÷ 3.04) = 1.91); the quality margins 3.8 and 5.9; the 14 of 27 and 48 of 50 assumption rows and the GPT "lower of two" donors; the cost allocations (115% / −15% and −90% / 190%); the source clocks against O59/O60; the SemiAnalysis stage dates; AGENTS.md against the draft (weights 15/11/8/5/6/15 and 21/17/12/10, O57, O58, O59–O62, the O45 binding), with no contradiction found.
- Not repeated (the ledger records them): I54 L2 (E237 on Terminal-Bench provider claims is latent: the one eligible claim is for a model outside the cohort), L4, L5 and the I49 provider-document clock note.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

**M1. The strict label guard is still a list of tail shapes. The draft's candidate definition and its claim "never silently dropped" are broader than what the code reads, and most plausible next forms are dropped without a message.**

- Issue. E267 now says: "A single-model label whose model text is a cohort model's name followed only by bracketed groups or spaces is that model's candidate, and it must read exactly under this grammar, or the build stops … so a new AA label form is read, never silently dropped." `agent_record_for` implements a narrower test: `_CANDIDATE_TAIL = (?: \((?:\{[^}]*\}|[^()]*)\))*\s*`, applied after `partition(" - ")` and a case-sensitive `startswith(name)`. A group counts only if it is parenthesised, has no nested parentheses and follows exactly one space; the separator, the name's case and the spacing must already be AA's. Anything else is "another model": `exact_agent_records` skips it, `agent_record_for` returns `None`, and the row silently loses its Coding Agent Index record. In the max-effort ranking that moves the row to the subset workload (flagged "subset cost", O17), which is what I50 H1 did to the API leader. I applied 17 perturbation classes to the 8 real cohort labels in the capture (132 labels; the effort-based classes skip DeepSeek's keyed-only label) and ran `agent_record_for`:

  | Perturbation of a real label | Build |
  |---|---|
  | trailing space; trailing tab; effort capitalised inside the brackets "(Max)"; unknown effort word "(ultra)" | stops (30 of 30) |
  | trailing newline | accepted as the exact record (8 of 8): `$` matches before "\n", so "trailing spaces all stop it" is not true for "\n" |
  | no space before the group "Luna(max)"; two spaces "Luna  (max)"; square brackets "[max]"; a curly or nested group after the effort "(max) {x}", "(max) (a (b))"; a suffix " - preview"; the fallback glued on "(max)(with fallback)"; an en dash or a doubled space around the separator; a lower-cased model name; the effort as a capitalised suffix "GPT-6 Astra XHigh"; the effort after a colon "GPT-6 Astra: max" | silently dropped (94 of 94) |

  The draft's own words classify most of these as candidates ("followed only by bracketed groups or spaces"); two implementers following the draft and the shipped code therefore disagree on them.
- Why it matters. This is the sixth consecutive round on this mechanism (I50 H1, I51 M1, I52 M1, I53 M1, I54 M1). Each fix widened a list of shapes, and the next round found a shape outside the list. The capture already shows two label styles that a new cohort label could take: the Devin Fusion CLI spells efforts as capitalised, unbracketed suffixes ("GPT-6 Astra XHigh + SWE-2 Medium", "Claude Opus 5.5 Max + GPT-6 Luna High"), and `Claude Code - Step 5 Preview ({'subagents': True})` shows a keyed non-effort group. The current guard stops on the second; a single-model label in the first style falls under the draft's last sentence ("a longer name is not a candidate") and is dropped. The likelihood of any single variant is low, but the sentence is a normative build rule that the draft says closes the class, and the failure is the one that has already changed a ranking. The owner's rule for recurring findings (E265: eliminate at the source) applies: the guard should not be a list.
- Change. Define the complement instead of the shapes:
  1. A Coding Agent Index label is classified once: mixed (contains " + "), names no cohort model, or names a cohort model and then must read exactly under the grammar (exact record, or another effort or fallback state of that model) or stop the build. "Names no cohort model" is a computed test: after Unicode normalisation, whitespace collapsing and case-folding, no cohort family name (with or without "Claude ") occurs in the label at a word boundary, or the name is continued by a longer name (the next character is alphanumeric, or "-" or "." followed by an alphanumeric, or whitespace followed by a word that is not an effort name in any case). The default for an unclassifiable label becomes stop, not drop.
  2. Replace "followed only by bracketed groups or spaces" and "never silently dropped" with that definition. If the editor prefers the minimal edit, narrow the sentence instead ("a parenthesised tail on AA's exact spacing") and delete "never silently dropped".
  3. Add a mutation fixture over the real capture: for each cohort label in `data/aa/coding_agents_capture.json` and each perturbation class in the table, the outcome is "reads as the same configuration's record" or "stops", never "dropped". Add `\Z` or `fullmatch` for the effort regexes so "\n" cannot pass.

**Low**

**L1. Five of the six stop forms the draft lists have no fixture, and the ledger calls them "probes".**

`tests/test_value_v3.py` covers the disagreeing pair (line 1840) and the real two-form label; the unknown or differently cased effort, extra group, other-key group, reversed order and trailing space are not tested (the r113 commit adds no test for them). The Normative "Release tests" paragraph, which lists the fixtures for E82 and the other contracts, does not mention the agent-label grammar at all. Add one fixture per listed form and one sentence to the release tests; the mutation fixture in M1 covers both.

**L2. The E180 and E189 sentences do not match the one-configuration rule they now sit beside.**

Output 1 says the value-variance allocation is "withheld below three rows, where the split is fixed by construction; today … the max-effort ranking's 4-row Plan subset stratum reads 'undefined (one configuration)'". Four rows is not below three; the stratum is withheld because its rows are one configuration's plan rows. E180 likewise says "Subset-workload strata get their own statistic (undefined below two rows)" and "an SD or SD ratio for cost influence needs two rows", while a Plan panel needs two configurations. The code and the data are right (`len(panel) >= 2 and len(configurations) < 2`); say "withheld below three rows, and for the plan rows of one configuration" in both places, and "two rows (two configurations on the Plan basis)" in E180's minimum-panel list.

**L3. The Plan basis's printed cost influence and allocation depend on how many plans a configuration has, the same replication E258 removed from the separability figures.**

The common-workload panel on the Plan basis is the plan rows (23 in the max-effort ranking, from 8 configurations), so a configuration with four eligible plans counts four times in SD(S_C), SD(S_Q) and Cov. From `data/scores.json` I recomputed the same statistics on one representative row per configuration: the max-effort Plan cost share is 47.8% over plan rows and 53.0% over configurations, and the cost value-variance allocation printed beside the nominal 25% (E196) is 28.2% against 68.6%; the AI Coding Daily Plan figures are 37.0% against 41.1% and −25.6% against −10.9%. E258 already treats plan-row replication as a distortion for separability ("a configuration's many plan rows no longer pull the median threshold to zero"); the headline disclosure whose purpose is to show how much the 25% weight matters has the same artefact, and the 28% a reader sees for the Plan basis is 2.4 times lower than the configuration-level figure. This is an implementation choice of E245 (O48 as recorded in AGENTS.md fixes the rows, not the panel of the disclosure statistics) and changes no score. Print the one-row-per-configuration (representative row) share and allocation beside the plan-row figures and say which is which.

## 2. Methodology design recommendations

Prioritised.

1. **Close the Coding Agent Index record at the source (M1).** Total classification of every captured label (exact, other state of a cohort model, mixed, names no cohort model, otherwise stop), printed per cohort row (`rows[].cost.codingAgent` = chosen label and class, plus the non-exact labels that name the model) so "none today" for pins and the 8 and 3 priced rows become placeholders the figures check verifies, and a mutation fixture over the real capture. This is the E225 pattern (closed registry, stop on the unknown) applied to the one input that has changed a ranking.
2. **Configuration-level companion for every Plan panel statistic that ranges over plan rows (L3).** Cost share, value-variance allocation, ordering agreement and the E189 status, each printed once over plan rows (what the table shows) and once over representative rows (what the configurations are). It costs one more panel in `panel_cost_influence` and removes a plan-count artefact from the one disclosure that argues about the owner's 25% weight.
3. **Fixture inventory in the draft.** One sentence in the release-test list naming the label-grammar fixtures (L1) and the one-configuration status fixture, so a later change cannot drop them without the draft saying a rule lost its test.

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: HAS FEEDBACK
