0. Read check

Read all 14 parts, in order, through the GitHub connector at commit fc9c5bf76f55b640a84d973ac526f3c7fa25ac2f. Each response reached the supplied part’s end. Part 13 ends mid-sentence; part 14 supplies its continuation.

First line:

ValueRank methodology — draft r168

Final sentence of each part, in order (Markdown table delimiters omitted):

> Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

> Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

> These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status.

> Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

> Fixtures: two concordant reports 41 days apart, neither admitted earlier, where the older one leaves the partition and the route is diagnostic; a model with a current controlled measurement and a lapsed report pair, where the controlled route stays and the report route is diagnostic; a transfer from a lapsed report donor, which is diagnostic.

> The build counts its rows among the Plan rows resting on an owner assumption, by kind (marked †, E242).

> Cross-source agreement (E229, amending E125): AA's leaf is compared with tbench.ai's matched rows (Kendall τ_b on their common panel, per ranking, with the mean offset tbench.ai minus AA beside it, since a rank correlation cannot see a uniform level shift; today τ_b 0.74 and offset +1.7 points on 5 rows in the max-effort ranking and undefined (panel too small) on the AI Coding Daily ranking's 1), and a row whose leaf is a tbench.ai gap fill is marked "harness-mixed" (today, max-effort ranking: none; AI Coding Daily ranking: none)

> Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

> Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

> The current ladders are in Output 3 and scores.json barCurrency.

> Each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

> Release tests: Omniscience vector above; Bug Hunt vector above; Index reconciliation (C_6 + C_HLE-Diamond + C_Omniscience + C_CritPt v2 reproduces AA's total within the E209 tolerance, the task counts taken from the registered v5 evaluations; the residual never enters C_W); Coding Agent Index fixtures (E82): the scored cost equals AA's pooled per-task-attempt mean × 290 (v2.0, O50); the raw telemetry sum and sum ÷ mean are preserved as diagnostics without requiring equality to 290 (fixture with unequal telemetry coverage, where mean × 290 differs from the sum and the row still scores and passes completeness); completeness has two predicates: a Coding Agent Index cost is complete when AA's missing- or declined-task markers are absent (O27), and an Index SDLC component cost also needs its row's Index reconstruction to pass (E209); aggregate/component exclusivity (an exactly reconciled decomposition leaves basket cost unchanged); repetition invariance (averaging extra evaluation repetitions does not multiply workload cost); workload migration changes W's hash and invalidates unreviewed Plan transport; basket persistence (a new cohort row with missing costs does not change W's hash); single clip predicate (all gate consumers call one function, with integer-boundary fixtures for several cohort sizes); split invariance (partitioning an execution family into accounting subcomponents leaves its pass cost and C^match unchanged; splitting a quality reporting leaf never creates or duplicates an execution-family weight — E55); kernel completeness (every stochastic input has executable parameters); price tests (E23): uniform price scaling cancels in Plan cost; arbitrary category-price changes cancel when measured consumption is proportional to the target-workload token vector; otherwise category repricing changes Plan cost by (p·x / p·u) and triggers a transport identification recheck (two-category fixture with different measured and target mixes); restoring a missing leaf moves correctly from S0 to S1; transfers-off never silently becomes API fallback in an interval output or a scenario panel (E167); a tighter quota cannot increase computed capacity; window-semantics fixtures above; adding an unrelated row cannot change common-panel diagnostics except via declared cohort-dependent quantities; a frozen bar does not force its setter as the answer (at freeze at least two population configurations reach H on displayed quality; E192), and each bar result publishes its count of R_W configurations that can qualify (E198a); cheapest fixtures (non-provisional and provisional singletons, unique cheapest, equal-cost tie → both in K_r; no self-comparison); interior-witness possible-frontier fixture (E43); completeness statuses (an AA declined- or missing-task marker → confirmed incomplete; an Index reconstruction that misses AA's total → unresolved; otherwise confirmed complete; the Coding Agent Index cost equals the per-task metric × 290); completeness (an AA-marked incomplete component fails FullCost and removes the row from R_W without changing its displayed score); session-start fixture (a schedule whose second burst starts a new session after the first session ends is feasible; capacity results carry a feasible schedule); interval decision statuses (an unresolved solve is never certified); widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic.

Last complete sentence:

Each capture publishes the rendered-frontier entrants and exits against the previous capture, and the reconciliation report lists every frontier and near row with its rank status.

The part then ends with this sentence fragment:

Today the capture, the latest under Intelligence Index v5.0 (the 2026-10-31 capture was the first, O132), was taken at 2026-11-01T05:53:05Z, before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

> Revision history: omitted from this review copy (not normative); it is in draft-r168.md in the same folder of the repository.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

The monthly research clocks lack an explicit empty-admission-window status. Issue: E308 defines a cell’s new-report window as the release envelope truncated at that cell’s latest staged search. O167 permits the monthly three-stage search to be 31 calendar days old. Consequently, a permitted release can have a cell whose searchedThrough precedes the envelope’s lower endpoint:

𝑠
=
date
⁡
(
𝑉
)
−
31
⟹
[
date
⁡
(
𝑉
)
−
30
,
𝑠
]
=
∅
.
s=date(V)−31⟹[date(V)−30,s]=∅.

The draft specifies the two endpoints and their governing clocks, but does not explicitly say how to represent this valid empty window. Earlier-admitted reports remain a separate population under O127; they do not make the new-report window nonempty. This follows from the report-window and research-clock rules in part 5. Why it hurts the objective: an empty interval could be rendered as an ordinary date range or interpreted by an extractor as invalid evidence configuration. Either outcome makes the Plan research’s actual coverage harder to audit. This is a boundary-state specification issue, not an argument against monthly research or the owner’s evidence rules. Concrete change: add a nullable interval plus an explicit status:

text
newReportWindow:
  start: releaseDate - 30 days
  end: searchedThrough
  status: nonempty | empty-search-predates-envelope

When end < start, admit no new reports through that cell’s staged-search record, preserve eligible earlier-admitted reports, and publish the empty-window explanation. Add a fixture at exactly 31 days. What is new relative to the ledger: this is the boundary interaction between O167’s permitted 31-day monthly clock and E308’s fixed lower endpoint—not a request to reverse O161, O164 or O167.

2. Methodology design recommendations

Specify and test the empty-window state above. Prioritise this small implementation clarification. It needs no additional data collection, does not change scores, and leaves every owner decision intact. Test these three cases together:
Latest cell search	New-report window	Earlier-admitted reports
Release date minus 30 days	One calendar date	Process separately under O127
Release date minus 31 days	Empty	Process separately under O127
Recent freshness check, but no new staged cell search	Unchanged by the freshness check	Process separately under O127
This makes explicit the distinction already intended in part 5: freshness checks can satisfy the release-time clock without extending report discovery.

I have no further material design recommendation against the stated objective within the binding policies. In particular, I would not reopen the already-decided cohort, weighted headline, subset-row treatment, Plan assumptions, or published-record interval target merely because another ranking philosophy is possible.

The draft’s central limitation is already stated rather than concealed: its Plan ranking currently provides exploratory arithmetic, not an identified answer to target-workload Plan economics. Its distinction between displayed ranking, interval claims, task-sampling scenarios and specification stresses is therefore important and should remain intact.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK