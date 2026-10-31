0. Read check

Part 13 (research/2026-10-19-methodology-codesign/perplexity/parts-r154/draft-r154-part-13-of-13.md) was opened through the GitHub connector and read to its end.

First line (a single very long paragraph, quoted in excerpt with the elision marked — the line is one continuous markdown paragraph): "an AA note that its cost omits a tariff component (today on the Claude Haiku 5.5 rows: its higher long-context pricing is not reflected in AA cost figures; scores.json rows[].aaCostCaveat) is shown on the row as "AA cost caveat". Unknown boundaries stay unknown (no assumed dates). Valuation-basis gate (E170…) […] …a new article changes nothing until the owner selects it (AGENTS.md; Plan cost, E238)."

Last 12 words of the part: "copy (not normative); it is in draft-r154.md in the same folder of the repository."

The part closes with the Revision-history stub, which is the document's stated end. No listed part failed to read.

1. Findings by severity

Critical

None.

High

Owner decision challenge (O112): the meter-reset exclusion makes the report-based replacement path structurally impossible for OpenAI, and the draft concedes it. The Known limitations state that OpenAI's global meter resets arrive roughly every two days, that only a reading whose window lies wholly between two resets counts, and that therefore "OpenAI's flagged routes are unlikely to be replaced by a report pair (O78, O93) before they are demoted at 121 days." The consequence chain is material to the Plan ranking's objective: a stale or fault-window OpenAI measurement keeps its official Plan score, competes as a blocker that denies other rows labels under E228/O118/O119, and has no evidence path out — for up to 121 days. Meanwhile O75 burns all three search stages over every cell each release, including OpenAI cells that cannot pass by construction. Recommended change: amend O112 so the exclusion applies only to readings whose usage cannot be separated at documented reset instants. Specifically: (a) admit a reading that reports per-reset-window usage, treating each sub-window (wholly between resets) as a valid reading — concordance under O86 is then evaluated on like-for-like per-window figures, never extrapolated to a billing period, which respects O82's no-conversion rationale; and (b) record the reset instants from the provider's public status/usage surfaces as typed change records (O99-style) so the decomposition is reproducible from public data. If the owner will not amend the exclusion, define the exit explicitly: shorten the demotion clock or allow provider-announcement re-scoping (O77 records) for rows whose replacement is structurally impossible.

Medium

Plan evidence health is disclosed only in Known limitations, not at the point of consumption. The draft's own arithmetic: 27 max-effort plan rows, of which 2 are on API fallback and 21 flagged possibly-superseded or expired — leaving roughly 4 rows on a current route (and 4 of 51 in the AI Coding Daily ranking). The lifecycle table (E212) and the manifest entry count flagged rows, but a reader of the Plan ranking table itself sees only per-row flags. This hurts the objective because the Plan headline is a full-utilisation Value Multiple whose evidentiary base is mostly stale, and the reader must find that in a limitations section rather than beside the ranking. Recommended change: a one-line evidence banner rendered from the build (E265-style) above each Plan table: counts by lifecycle stage (current / possibly-superseded / expired / demoted / API fallback), fault-window count, and the count eligible to earn labels. Everything needed is already computed for the manifest.

The AI Coding Daily ranking is published with no coding-agent cost component in its basket. The draft states the Coding Agent Index v2.0 is pending there (3 of 16) and the O116 FrontierCode chart-total stand-in is not admitted (5 of 16, below the O57 two-thirds admission threshold counted within the ranking). AA's cost metric is the only harness-level coding-agent cost measure in the design — it is the pooled per-task-attempt pay-per-token API cost, including cache-write and discounted cached-input pricing — so its absence means a ranking named for AI coding daily carries no coding-agent execution cost at all. The draft discloses this and O116 governs the stand-in, so this is a surfacing and trigger recommendation, not a challenge to O53/O116: print a ranking-level cost-coverage chip (admitted components; rows priced per component; coding-agent coverage share) in the ranking's header rather than only in limitations, and set an owner-review trigger if coding-agent cost coverage remains below the O57 threshold for a defined number of consecutive releases.
artificialanalysis
+1

The primary independence diagnostic is vacuous in both rankings. Leave-AA-out is reported "not identifiable" whenever independent quality weight is under 40% — today 34% in max-effort and 22% in AI Coding Daily. So in both published rankings the leave-AA-out check never runs, and the matched-panel checks (E62/E66/E71) on small panels are the only cross-source evidence. This weakens the objective's defensibility: cohort selection (AA's rendered frontier) and most quality and cost evidence come from the same source, and the check that would quantify that dependence reports nothing. Recommended change: add an always-runnable partial variant — drop the single largest AA-executed leaf and report rank and value-order τ_b on affected rows (the quality analogue of E172's leave-one-component-out cost family) — and publish the independent-weight share as a standing per-ranking field with the 40% threshold named, so readers can see whether the check is active.

Low

τb 0.67 on 4 configurations (E274) is statistically indistinguishable from noise. With n = 4 (six pairs), even a perfect τ = 1.0 fails a two-tailed test at α = 0.05 under the exact permutation distribution; approximate significance is explicitly unreliable for N ≤ 10, and exact small-sample significance must come from permutation enumeration or critical-value tables. The draft labels it "descriptive check only," which contains the harm, but publishing a bare point estimate invites misreading. Recommended change: print the exact permutation p-value (trivially computable by complete enumeration at this n) for E274 and the E62/E66/E71 matched-panel statistics, or print "n too small" below a stated floor (e.g., n < 8). Model-row bootstrap intervals on tiny panels are likewise unstable; exact permutation is the better tool at these sizes.
spss-tutorials
+1

The E176 metering comparability caveat's factor of 1.10 is a bare constant. Two rows whose basket costs lie within a factor of 1.10 on different token-metering bases get a caveat, with no stated derivation. Recommended change: document the rationale or report firing rates at 1.05 / 1.10 / 1.25 as a small sensitivity, so the caveat's meaning is auditable like the other thresholds in the draft.

The staged search's reach bias is recorded but not compensated. Reddit (direct), X, and YouTube were unreachable and LINUX DO only via a mirror, so "no concordant pair" for Kimi, Xiaomi and MiniMax "partly reflects where the search could look" — the draft says so. Recommended change: add at least one routinely reachable primary channel per major provider to the staged search (e.g., provider forums with public RSS or searchable archives), and print per-provider search reach beside the Plan table so users can weight negative outcomes. (This is separate from the OpenAI structural impossibility in the High finding.)

2. Methodology design recommendations

Prioritised, all implementable from public data refreshed by the existing build:

Meter-window decomposition for reset-spanning readings (pairs with High finding 1). For a report spanning resets at instants t₁…t_k recorded as typed change records, admit sub-readings of usage within each (tᵢ, tᵢ₊₁); evaluate O86 concordance on per-window figures pooled across reporters; never convert a sub-window figure to a billing period (O82 respected). Fallback if not adopted: a defined exit for structurally unreplaceable rows — shorter demotion clock or O77-announcement re-scoping for the affected provider.

Plan evidence banner. One rendered line per Plan table with lifecycle-stage counts, fault-window count, API-fallback count, and label-eligible count; sourced from the same data as the E212 manifest entry.

Partial leave-one-leaf-out quality diagnostic. Drop the highest-weight AA-executed leaf per ranking; publish rank τ_b and value-order τ_b on affected rows, plus the standing independent-weight share field (max-effort 34%, AI Coding Daily 22% today) against the named 40% threshold. This complements, not replaces, the E62/E66/E71 matched-panel statistics.

Ranking-level cost-coverage chip and trigger. Print each ranking's admitted cost components, rows priced per component, and coding-agent coverage share in the ranking header; flag for owner review when a pending component stays below the O57 admission threshold for a fixed number of releases.

Exact permutation p-values for all published τb statistics (E274 agreement; E62/E66/E71 matched-panel checks). Complete enumeration is exact and cheap at these panel sizes, and is the standard small-sample correction.
spss-tutorials
+1

Document or sensitize the E176 1.10 factor, as above.

3. Questions for the owner

Under O112, would a reading decomposed into per-reset sub-windows (each wholly between resets, never converted to a billing period) count as admissible as written, or does the whole-reading exclusion need an explicit amendment for recommendation 1 to be legal?

Should the AI Coding Daily ranking's continued publication be conditioned on its coding-agent cost coverage reaching the O57 threshold within a set number of releases, or must both rankings always publish regardless of cost-basket coverage (this determines whether recommendation 4's trigger is a hold or only a flag)?

Given O112 makes report-pair replacement structurally impossible for OpenAI, is a shorter demotion clock or provider-announcement re-scoping acceptable for those rows, or should the stale-blocker state (denying others' labels for up to 121 days) stand as designed?

4. Verdict

VERDICT: HAS FEEDBACK