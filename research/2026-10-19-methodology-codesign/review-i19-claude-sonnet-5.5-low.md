# Internal review I19 — Claude Sonnet 5.5, effort low, on draft r78

(Saved from the subagent's report; the reviewer read all 967 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r78`
Last 12 words of the last line (the final sentence is folded onto lines 966–967): "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."

I read all 967 lines in three chunks and the condensed ledger. I checked the I15–I18 and "Owner decision (2026-10-21)" sections of `ledger.md` and the current `AGENTS.md`. The AGENTS.md text quoted in my brief is stale. The repository version now carries the two-thirds admission wording, so I raise no point on it.

I also re-derived by hand or by script:
- The ladder positions floor((n−1)k/4) for n = 2, 3, 4, 22 and 35.
- The bar-currency counts of 18, 27 and 10 of 35.
- The E203 count of 17.
- The kernel fixture. Uniform gives 91.47%, and a simulation of arcsine gave 86.76%, matching the draft's ≈86.7%.
- The Omniscience, Bug Hunt and E221 u* vectors.
- The exchange-rate and influence formulas.
- The Clopper–Pearson closed forms.
- The population counts 37, 36, 35, 34 and 33.

All of these hold.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. The price-record freshness limit is looser than the valuation-basis gate assumes (E216 against E141/E170/O29).
- **Passage:** E216 allows price records up to 45 days old at the cutoff. The draft itself says this limit "binds the price records in practice", because the model-page snapshot is capped at 14 days by E211 and E217.
- **Conflict:** E170 sorts every cost observation by comparing its basis with "the price records in force at V". E141's `scheduled_refresh_at` only covers boundaries that are already known.
- **Why it hurts:** The gate exists to catch the event O29 describes, a provider tariff changing between AA's valuation and V. A record captured 30–45 days before V cannot show an unannounced change in that interval. The gate then returns outcome 1 ("compatible as captured") while the real answer is outcome 2, 3 or 4. The row would carry no "AA cost at superseded price" flag, and it could earn an interval label that the gate was meant to deny. The 7-day caps on the chart and snapshot show that fresh capture is cheap. Price pages are the cheapest artifact to refetch.
- **New argument:** I18/I12 settled that the 45 days is enforced. They did not address whether a 45-day record can support a claim about prices in force at V.
- **Change:** Give the price records the 7-day gate (E211/E217) at V. Alternatively, require a price-page probe, recorded with its hash, at the search cutoff. A probe that finds a difference triggers the gate. Keep 45 days only for the AA model-page snapshot, if at all.

M2. The Terminal-Bench row-selection rule is unstable under unrelated submissions, and it has no source-change rule (leaf table, E225).
- **Passage:** The preference order is Terminus 2, mini-SWE-agent, OpenHands, "then any other agent in ascending code-point order of its name".
- **Why it hurts:**
  - For a configuration with none of the three named agents, the leaf comes from whichever agent sorts first alphabetically. A new tbench.ai submission by another agent for the same model and effort, with a name that sorts earlier, silently switches the leaf row. Nothing about the model has changed, and the value score moves.
  - The draft handles the same problem for Bug Hunt. E206 publishes a harness switch as a "leaf-source change with both values". Nothing equivalent is stated for Terminal-Bench.
  - Alphabetical order is also arbitrary with respect to the comparability goal of E125's "harness-mixed" marker.
  - The leaf carries 10% of quality.
- **Not verified:** I did not count how many cohort rows currently fall into the alphabetical tail.
- **Change:**
  - (a) Replace the open tail with a closed, dated, versioned preference list of the agents actually observed on the leaderboard for cohort rows. Add a newly observed agent only through a registry update, never by sort order.
  - (b) State that a change in the selected row, whether from a new submission or from a registry update, is published as a leaf-source change with both values and its score effect, as E206 does.
  - (c) Print, per release, the count of rows by selected agent.

**Low**

L1. The evidence-age clock is stated two ways.
- **Passage:** The "Assumptions" paragraph (about line 364) says age runs from "the measurement window's end, else the source publication date".
- **Conflict:** E194 and E151 define a three-step date: window end, else report date, else publication date.
- **Why it hurts:** A report whose report date differs from its publication date gets two different ages under the two readings. Since E212's strict thresholds turn on single days, two builds could disagree.
- **Change:** Say "the E194 observation date" in that sentence.

L2. The kernel-check design does not test competitors one at a time.
- **Passage:** The draft discloses that independently varying competitor components "switch together and are not exhaustively checked". With a frozen-level bar, the registered groups are only candidate and competitors, so G ≤ 2 and A has at most 4 assignments.
- **Why it hurts:** The label wording ("supported under all registered role-group kernel checks") is honest. The check is still weak where it matters most. The event is not monotone in each competitor's kernel. The worst case for the candidate can be one cheap competitor on arcsine and the others on uniform, and the group-level corners never produce it.
- **Change:** Add to A the single-competitor flips for the k = 3 competitors with the highest qualify-and-cheaper-than-candidate frequency. That adds at most 2k assignments, is enumerable and needs no new data. Alternatively, state in the label table that the label is not robust to per-competitor kernel choices. Whichever is chosen, publish the competitors that were flipped.

## 2. Methodology design recommendations
1. Implement M1 first. It affects the integrity of the O29 gate, and the fix is a capture-policy change that needs no new methodology.
2. Implement M2 next. It is a short rule change plus one published table, and it removes a score-moving behaviour that nothing in the evidence explains.
3. Apply L1 and L2 as drafting fixes.

I found no new structural gaps beyond what the ledger already records. The coverage-restricted and full-coverage universes, which would help the "confirmed cheapest" output, were rejected in I8 M4, I16 R2 and I18 R1. I do not repeat them.

## 3. Questions for the owner
None.

## 4. Verdict
VERDICT: HAS FEEDBACK
