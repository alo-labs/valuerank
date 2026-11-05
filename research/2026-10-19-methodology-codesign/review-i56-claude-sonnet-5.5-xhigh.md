# Internal review I56 — Claude Sonnet 5.5 (effort xhigh) on draft r114

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r114".
- Last line of the draft (the end of the revision history): "(fifty-fifth internal review) replaces the list of rejected label shapes with a complete classification: every captured label that mentions a cohort model is read, is a two-model label, or is reviewed into a register, or the build stops. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "build stops. Every change is recorded with its rationale in the ledger."
- Also read, in full: `reviewer-prompt.md`, the reviewer brief, `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (I55), `AGENTS.md`, the whole folded draft (988 lines) and the r113 to r114 source diff.
- Code and data opened to check rules and figures: `valuerank/value_v3.py` (`parse_agent_label`, `exact_agent_records`, `unclassified_agent_labels`, `agent_record_for`, `assemble`, `configurations_from_scores`, `source_clocks`), `valuerank/basket.py` (`coding_agent_component`, `admission_panel`), `valuerank/capture_coding_agents.py`, `valuerank/build_scores.py` (the `build_tracks` call), `tests/test_value_v3.py` and `tests/test_capture_coding_agents.py`, `data/aa/coding_agents_capture.json`, `data/v3_configuration_map.json`, `data/scores.json`, `data/aa_frontier_capture.json`, `data/plan_cost_routes.json`. I ran `tests/test_value_v3.py` (95 passed) and `python3 -m valuerank.draft_figures check` (exit 0).
- External pages fetched during the review (they carry the AA facts used below): `artificialanalysis.ai/agents/coding-agents`, `…/methodology/coding-agents-benchmarking`, `…/methodology/intelligence-benchmarking`.
- Probe scripts are in the session scratchpad (`…/scratchpad/i56/`), not in the repository. I wrote no repository file other than this review.

## 1. Findings by severity

### Verification of the I55 handling (before the findings)

Confirmed against code and data:

- `value_v3.unclassified_agent_labels`, the `agentLabelRegister` (empty, with its rule text) in `data/v3_configuration_map.json`, and the call in `assemble` exist as the ledger says. The effort patterns are anchored with `\Z`, so a trailing newline no longer reads. `test_no_perturbation_of_a_real_agent_label_is_silently_dropped` applies the thirteen perturbations the ledger and the draft describe to the eight real exact labels (those of the 20 ranked configurations) and passes.
- Run on the real capture with all 29 cohort configurations, the guard returns nothing: eight labels are exact records, two of the three Devin Fusion CLI labels (the ones that mention cohort models) are two-model labels, and the rest mention no cohort model.
- The grammar paragraph of the draft (efforts, order of the two effort forms, "both forms must agree", case-sensitive comparison, fallback token last) matches `parse_agent_label`.

Not confirmed: the draft's universal sentence, "a new AA label form, whatever its shape, is read or reviewed, never silently dropped". M1 below shows concrete labels that pass the build and silently move a ranked row to the subset workload.

Other checks that came out right (no finding): the 18 frontier and 11 near points recomputed from the capture's tooltips by the AGENTS.md rule; 12 families (7 and 5); the zero-based bar positions for n = 9, 15 and 32 and the ⌈n/2⌉ statement; the E77 endpoints and 0.996875; the 86.7% basket-scope weight; the 66/34 and 78/22 source shares; 3.04 value points against 4.06 quality points per cost doubling; the O45 lower-of figures in `plan_cost_routes.json`; every route naming exactly one model; the O59/O60 source clocks; AA's own description of the Intelligence Index (ten evaluations, 66 Terminal-Bench tasks, mini-swe-agent harness).

### Critical

None.

### High

None.

### Medium

**M1. E267's classification is still an open-world text heuristic; four concrete cases pass the build and silently re-price a ranked row.** The draft promises that every captured label is read or reviewed. The guard only sees records that survive the capture, collapses them by label text, and decides what a "mention" and a "two-model label" are by string tests that are narrower or different from what the draft says. I reproduced cases 1 to 3 on the real documents with the 29 cohort configurations under the max-effort track (`value_v3.assemble`; no exception in any of them); case 4 is shown by the existing capture test, and the zero-width and look-alike variants in case 2 by calling the guard directly:

1. **A single-model label whose agent name contains " + ".** `Claude Code + MCP - Opus 5.5 (Max)` (the real `Claude Code - Opus 5.5 (max)` with an agent name containing " + " and a capitalised effort). `parse_agent_label` tests " + " on the model text only and reads the model, but `unclassified_agent_labels` tests the whole label (`" + " in label`) and files it as "a label naming two models". It is neither exact nor flagged, so it is skipped. Claude Opus 5.5 (max) moves from the main workload (9a0d376cc6080f3c) to the subset workload (1453a9a0576b02ea) and its basket cost falls from 9,351.72 to 6,039.13 USD. The draft defines a two-model record only as "an agent that mixes them"; the string rule that the code uses is nowhere stated, and the two functions apply it to different parts of the label.
2. **A spelling the rule says it ignores.** `Codex - GPT6 Luna (max) ({'reasoning_effort': 'max'})`. The draft says labels are compared "ignoring case, spacing and punctuation". Read literally, "gpt6luna" matches and the label must stop the build. The code replaces runs of non-alphanumerics by one space and compares tokens (`_normalised`), so "GPT6 Luna" is not a mention and is dropped. GPT-6 Luna (max) moves to the subset workload and its cost falls from 125.72 to 79.56 USD. Removing all separators instead gives the same classification on all 24 captured labels (no false positive today). Zero-width characters and look-alike letters inside a model name are dropped the same way (`Op​us 5.5 (max)`).
3. **Two records with one label.** `assemble` builds `{item["label"]: item …}`, so a second Coding Agent Index row with the label `Codex - GPT-6.1 Sol (max)` and a different AA `id` replaces the first without a message (basket cost 1,233.11 to 2,105.80 USD in my run with a row at three times the cost). The "several exact records, pin the choice" stop cannot fire, and a pin (a label string) could not choose between them anyway. AA's row `id` is the record's identity; the label is not.
4. **A row the capture never keeps.** `capture_coding_agents.configuration_rows` keeps only objects that have `displayLabel`, `sums`, `mean` and an `id` (`tests/test_capture_coding_agents.py::test_configuration_rows_dedupe_by_id_and_require_cost_blocks` documents the skip) and records nothing about the others. A cohort-model row whose cost block AA renames never reaches the guard.

The fixture of I55 cannot see these: it mutates the text of eight labels, never the agent part, never the set of captured rows, never duplicates. E177's swing gate would name the changed capture field rather than stop (I did not run it), so nothing downstream catches the shift. This is the I50 H1 failure again (a priced row on the subset workload without a stop) and the seventh round on this mechanism because each repair enumerates shapes. Recommended change: see Recommendation 1 and 2 (close the world and add a continuity check); the minimal patch is Recommendation 4.

**M2. The draft states that the Coding Agent Index costs are "complete (no AA missing- or declined-task marker)", but the build reads no marker, and AA's page publishes safety-refusal outcomes that the capture discards.** The draft says each priced row is "complete under O27 (no AA missing- or declined-task marker)" (Capture status), and E37 names two marker forms (the chart "*" and "an explicit missing-task note"). `capture_coding_agents.configuration_record` keeps only `safety.attemptCount`, and `basket.coding_agent_component` returns `COMPLETE` unconditionally, so the claim is true by construction and never tested. AA's own payload (the fetched page's cost fields equal the 2026-10-23T05:31:41Z capture, for example 11.4227 USD per task for Opus 5.5 (max)) carries per evaluation `refusedAttemptCount`, `hardStopAttemptCount`, `recoveredAttemptCount`, `fallbackAttemptCount` and the fallback chain. For ranked max-effort rows (870 attempts each):

| Coding Agent Index row | Blocked (attempt ended) | Finished by a fallback model |
|---|---:|---:|
| Codex - GPT-6.1 Sol (max) | 15 (SWE-Atlas-QnA, of 372) | 0 |
| Codex - GPT-6 Astra (max) | 13 (SWE-Atlas-QnA, of 372) | 0 |
| Claude Code - Opus 5.5 (max) | 0 | 76 (52 of 372 and 24 of 198; fallback Claude Opus 4.8) |
| Claude Code - Sonnet 5.5 (max) | 0 | 45 |
| Claude Code - Haiku 5.5 (max) | 0 | 3 |

AA's methodology page: "A safety refusal is a provider or model declining to proceed with a task on safety grounds"; "A model refusal that ends the attempt completes with a zero score and is not re-run"; "Fallback: the agent switches to another model, often a less capable one, which completes the attempt." That is the wording of the chart marker O27 uses ("declined some tasks on safety grounds"), and O27 says a component is incomplete where "AA itself marks tasks … declined (e.g. …)". Two faithful implementers read it differently: one treats a blocked attempt as a declined task (confirmed incomplete), the other as a priced zero-score attempt (complete). The choice is not neutral. In my sensitivity run (`coding_agent_component` patched to `INCOMPLETE` for the two Codex rows) the max-effort ranking's Coding Agent Index reference panel falls from 8 to 6 rows against the threshold ⌈2·9/3⌉ = 6: still admitted, with no margin, and under the draft's own rule GPT-6.1 Sol (max) and GPT-6 Astra (max) would become "partial component" rows outside R_W and the anchor references. Scores do not change; the admission margin, the interval outputs and the counts quoted in the draft do.

The fallback column bears on AGENTS.md's rule not to transfer results across model versions. For Opus 5.5 and Sonnet 5.5 AA plots only the "with fallback" state, so E214 already treats the serving setting as the configuration; but the Opus record carries no "(with fallback)" token although 8.7% of its attempts ran on Opus 4.8, and Haiku 5.5 (max) is plotted without the qualifier on the Index chart while 3 of its Coding Agent Index attempts used a fallback. Recommended change: Recommendation 3, and an owner decision on Question 1.

### Low

**L1. The label register is weaker than its description.** The rule says each entry carries its reason, but `unclassified_agent_labels` tests `label in register` only: an empty reason passes; a registered label that nevertheless reads exact is still priced as an exact record (the register does not reach `exact_agent_records`), so "reviewed as naming a different model" does not remove it; stale entries are never reported. Fail the build on an empty reason, on a registered label that reads exact, and print unused entries.

**L2. The guard's cohort depends on the entry point.** `build_scores` passes the 29 cohort configurations; `value_v3 freeze|scenarios|dual-run` call `configurations_from_scores`, which passes only the 20 `rankingEligible` rows. `Agent - MiniMax-M3.1-Flash [max]` stops the release build and passes `freeze` (verified). No output changes (excluded rows are not anchor references), but the guarantee should not vary by command.

**L3. Presentation.** The Cost-source match bullet is one run-on of about 330 words (identity rule, grammar, classification, fixtures, derivation, pin rules). Split it into labelled sub-bullets. The r114 history entry names three classes ("read, a two-model label, or reviewed into a register") where the rule has four (it omits "another effort").

**L4. Wording.** "Claude Opus 5.5 (xhigh with fallback) and Claude Sonnet 5.5 (max with fallback) all display 56": two names, so "both" (the sentence is generated from `aa.frontierIndexTies`).

## 2. Methodology design recommendations

1. **Close the world on AA's agent rows (ends the M1 series; priority 1).** Keep a versioned manifest `data/v3_agent_labels.json`, hashed into the evidence bundle, that lists every Coding Agent Index row by AA `id` with `displayLabel`, `agentName`, AA's `isRouter` flag and one class: `exact:<configuration id>`, `router`, `other-effort:<configuration id>` or `other-model` with a reason. The build stops when the captured ids differ from the manifest, when an id's label changes, or when two ids share a label; a record is the manifest's exact row (a pin chooses among several) and must also satisfy `parse_agent_label`. This is the pattern the draft already uses for Terminal-Bench agents (E225) and sources (E239). No normalisation, " + " test or "mention" heuristic is then needed: a new row of any shape stops the build, once, until a dated manifest edit. AA's `isRouter` is true for exactly the three two-model rows today and replaces the text test. The capture should record every flight object that carries a `displayLabel`, with the reason for any it does not keep (no `sums`, no `mean`, no `id`). Keep the thirteen-perturbation test as a regression test, not as the guarantee.
2. **Continuity check (cheap, shape-independent).** A ranked configuration that had an exact Coding Agent Index record in the previous release's evidence bundle and has none now stops the build unless the manifest records a withdrawal. This catches every rename, spelling or capture-drop case without anticipating its form.
3. **Capture and publish AA's safety outcomes (M2).** Add per evaluation `refusedAttemptCount`, `hardStopAttemptCount`, `recoveredAttemptCount`, `fallbackAttemptCount`, the fallback chain's model names, and `rewardHacking.flaggedAttemptCount`, plus the row's `isUnavailable`, `isRouter` and `hasTieredPricing` (the last is true for the Haiku 5.5 (max) row, which matches the draft's AA cost caveat). Print a "blocked and fallback attempts" column beside each Coding Agent Index cost; record the owner's answer on blocked attempts in O27's text; state in the draft how fallback-finished attempts relate to the "(with fallback)" qualifier; publish the admission margin (reference panel against threshold) as a figure so a one-row change is visible.
4. **If Recommendation 1 is declined, minimal patches** (all four are small): apply the " + " test to the model text only, as `parse_agent_label` does, or use `isRouter`; compute the mention test on the string with all non-alphanumerics removed after NFKC normalisation and removal of format characters; stop in `assemble` when two records share a label; list dropped rows at capture.
5. **Stopping rule for this mechanism.** From here, accept a further finding on agent labels only if it names a label that passes the closed-manifest check. Without the manifest every round can find another shape; with it, the question is closed.

## 3. Questions for the owner

1. For the Coding Agent Index cost, does a **blocked** attempt (a safety refusal that ends the attempt; AA scores it zero and prices it up to the refusal) count as a "declined" task under O27, so that the row is a confirmed-incomplete component? If yes, GPT-6.1 Sol (max) and GPT-6 Astra (max) become partial-component rows in the max-effort ranking and its admission panel is 6 of 6 required; if no, the draft adds one sentence recording AA's methodology as the reason.
2. Are you content that an unregistered AA agent row (any shape) stops the refresh until a one-line manifest entry is added, as an unregistered Terminal-Bench agent already does (E225)? If not, Recommendation 4 is the fallback and the seventh-round risk remains.

## 4. Verdict

VERDICT: HAS FEEDBACK
