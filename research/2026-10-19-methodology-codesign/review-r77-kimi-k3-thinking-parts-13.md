Both parts are read. Before finalizing, I'll quickly verify one external fact I want to build a recommendation on: how ChatGPT plan allowances reset and are structured.
0. Read check

Part 13 (draft-r159-part-13-of-14.md) — read to its end via the GitHub connector at the pinned commit.

First line: ## Governance

Last 12 words: "…the 2026-10-23 capture's near set had grown by DeepSeek V4.1 Flash 1017 and MiniMax-M3.1-Flash, both then new to the chart;" — i.e., the part ends mid-sentence at its split boundary, which matches part 14's opening; nothing was truncated.

Part 14 (draft-r159-part-14-of-14.md) — read to its end via the GitHub connector at the pinned commit.

First line: note that part 14 begins with one very long logical line (a single unbroken paragraph running from the AA-frontier-capture sentence through the SemiAnalysis-watch paragraph, ending "…(AGENTS.md; Plan cost, E238)."). Its opening words are: the capture's comparison record is in data/aa_frontier_capture.json. **Tariff applicability (E141)**: each price record carries observed_at, effective_from, effective_until…

Last 12 words: "…Revision history: omitted from this review copy (normative); it is in draft-r159.md in the same folder of the repository."

Both parts were read to their ends. The review below covers only what parts 13–14 state; rules these parts cite from elsewhere in the draft are treated as defined.

1. Findings by severity

Critical

None.

High

The OpenAI Plan routes are structurally un-replaceable under O112/O131, and the section itself may rest on a contestable factual premise. Known limitations state that OpenAI's meter resets "come about every two days," that a reading spanning one is excluded (O112), and that O112 stands (O131) — so OpenAI's flagged routes "keep blocking labels until… demotion," with a fresh controlled measurement or a provider announcement as the only exits. Two problems. First, this makes the largest provider's Plan rows permanently stale or diagnostic, hollowing out the Plan basis (O1 ranks Plan buyers separately — half the product). Second, public documentation describes OpenAI allowances as per-model rolling windows on their own clocks, not a single global reset ("limits are attached to individual models… each counter runs on its own clock… nothing resets globally"; weekly periods start with the first request after reset). If the observed ~2-day resets are rolling per-user events rather than global ones, then "a reading spanning the provider's global meter reset" (O112) may be excluding readings that never actually span any user-visible discontinuity. Recommended change: reconcile the reset mechanism against primary evidence, then admit an "intra-window allowance observation" class: a report that observes cap exhaustion plus the displayed "resets at" time within one inter-reset window directly measures the per-window allowance with no duration conversion (compatible with O82 — a measured cap is an allowance, not a converted duration). Two concordant such reports for one model and plan then admit as a pair. This does not alter O112; it makes O112-satisfying evidence practically obtainable.
felloai

The official Plan ordering is dominated by flagged evidence, with no currency display in these parts. Part 14's own figures: 21 of 27 max-effort and 60 of 67 AI Coding Daily plan rows rest on routes flagged possibly superseded or expired, and 12 of 67 sit on acknowledged-fault-window measurements — while the lifecycle table keeps their official score "unchanged" through every flagged stage. The disclosed mitigations (flags, the measured-only view) leave the headline ordering visibly mixing "value" with "evidence vintage," which is exactly what a public ranking's credibility rests on. Recommended change (display-only, no rejection of the keep-ranked policy): print a per-ranking evidence-currency figure (share of plan rows on Current-stage evidence) beside each Plan ranking, and the per-row evidence age in whole UTC days that E212's fixtures already compute. This is new versus the rejected items, which concerned removing or down-weighting rows; nothing here changes comparability or eligibility.

Medium

A pre-announced, dated provider change is coming that the draft does not pre-position for. OpenAI has announced that from December 2026, Plus/Pro/Business allowances merge into one shared ChatGPT+Codex token pool, with remaining usage and reset times shown in Settings → Usage, and Pro allowances were doubled on 2026-10-30 — exactly the typed "limit"/"metering" records O77/O99/O101 are built to catch. The flagging machinery is complete, but two estimand gaps are not pre-registered: (a) after the merge, the standing row disclaimer "the multiple values the measured workload's API-equivalent consumption only (other plan features are not valued)" understates what changed — the pool itself becomes chat-shared, so a workload-only multiple on a shared-pool fee values a strictly smaller share of what the cash buys; (b) whether the merged meter is one "meter family" under O113 (flagging every OpenAI plan route at once) should be settled before the split/flag event, not improvised at it.
openai
+2

The two-ranking agreement statistic is published on a panel of 4. E274's τ_b between the two rankings' API value orders reads "defined" at E180's floor of 3 shared configurations, with today's panel of 4. At n=4, τ_b takes only a handful of values and carries enormous sampling error; printing it, even as "descriptive," invites over-reading in a public artifact. (This complements, and is not repeated in, the E62 checks, which do publish bootstrap intervals.) Recommended change: either suppress the statistic below ~8 shared configurations or attach an exact permutation/bootstrap interval; the E62 machinery already exists to reuse.

Report-search reachability is systematically biased by provider region. The draft records that Reddit was read only via an indexed mirror, X returned HTTP 402, YouTube pages were unreachable, and LINUX DO — where many Kimi, Xiaomi and MiniMax user reports live — was read only via a mirror. So "no concordant pair" outcomes for those providers partly measure where the search could look, biasing which providers can ever upgrade off API fallback (O73). Recommended change: expose a per-cell search-coverage line (targets reached/unreachable) on the plan row itself, not only in the registry log, and add directly reachable sources for those user bases (LINUX DO direct, V2EX, Hacker News comment trees, Discord mirrors).

Low

Scenario-engine reproducibility block is incomplete. A published RNG seed and draw order do not reproduce draws across RNG library versions (streams are implementation- and version-specific). Publish the generator, library and version alongside the seed per release.

Single-evaluator dependence stays unpublished at the headline level. Leave-AA-out is "not identifiable" at 34%/22% independent weight, so no published sensitivity exists for dependence on AA-run leaves; the draft should print E62(b)'s quality-substitution τ_b with its interval as the standing headline robustness marker in the meantime.

E212's "Report out of window (O32)" row mixes trigger and action in one trigger cell (window exit, partition rebuild, and the admittedOn carve-out). Splitting "trigger" from "treatment" would make the lifecycle table mechanically checkable.

2. Methodology design recommendations

Intra-window allowance observations (top priority). Admit report r = (consumed amount U_r, cap-hit indicator, displayed reset timestamp, inter-reset window containment). Require U-measurement containment wholly between two consecutive resets per the reporter's own UI; score concordance on U per window under the existing O86 common-value rule; type it in the registry as per_window_allowance and let it pair-concord with only the same type. Implementable from public, routinely refreshable evidence (users see reset times and remaining usage in Settings → Usage ).
openai
+1

Evidence-currency display. Per ranking: currency = rows_Current / rows_total, plus per-row age_days = date(V) − date(observation) (already defined; fixtures exist in E212). Display-only; no gate.

December shared-pool pre-registration (dated owner item). Record the announced shared ChatGPT+Codex allowance as a typed "metering" change (O99) on a named meter family (O113) effective at the announced date; decide in advance that all OpenAI plan routes flag together, and revise the row disclaimer to state the workload-only multiple now prices consumption out of a chat-shared pool.
openai
+1

E274 publication rule. Publish the cross-ranking τ_b only when shared configurations ≥ 8, else print the exact CI; reuse the E62 bootstrap.

Search-coverage accounting per cell. coverage(cell) = reached_sources / target_sources printed with each no-pair outcome; treat < a threshold as disclosing that the outcome is search-limited.

Independent-weight build-out. Track "independent executed-leaf share" toward the 40% leave-out threshold as a roadmap metric; admit additional independently executed leaves only per the O49 process (owner decision, as these parts require).

RNG pinning. Add (generator, library, version) to the published scenario reproducibility record.

3. Questions for the owner

On your dated OpenAI references: are the ~2-day resets globally synchronized or rolling per-user windows? The answer determines whether O112 as written excludes obtainable evidence and whether recommendation 1 admits pairs without amendment.

For the announced December shared ChatGPT/Codex pool: will one meter family (O113) cover all plans, and will the estimand disclaimer be revised before that effective date rather than at the following release?

Is there any evidence-currency floor below which you would lead the Plan view with the measured-only ordering? (Determines whether recommendation 2 stays display-only or needs a gate.)

4. Verdict

VERDICT: HAS FEEDBACK