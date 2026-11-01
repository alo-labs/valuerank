0. Read check

Both listed parts were opened through the GitHub connector at commit 5917e61757433bf61ca45bbb5cb030200bb8f863 and read to their ends, in order.

Part 3 — draft-r172-part-3-of-14.md

First line: “## Cost (25% of the value score)”

Last 12 words: “cost per task, not AA's 7:2:1 blended price, not total Index cost.”

Part 4 — draft-r172-part-4-of-14.md

First line: “- Matched-cost diagnostic (diagnostic only). C_i^match = Σ_{g∈G} ω_g P_ig over canonical execution families g (E55; e.g. FrontierCode, Terminal-Bench as executed by AA): quality-weighted complete benchmark passes (E24), with P_ig = cost of one complete deployment-equivalent pass of family g for configuration i (Σ of its accounting subcomponents; published task count × mean cost per attempted task) and frozen diagnostic weights ω_g (Σ ω_g = 1, from the quality weights of the leaves that reference g, fixed with the panel before ranks are examined); a quality leaf references exactly one execution family; model API token charges only (input, cache read/write, reasoning, output × the primary price list; sandbox, environment-setup and verifier compute excluded; E17); where a source cannot separate retry or harness tokens the leaf is not priced for that row; tbench.ai cost columns are never joined.”

Last 12 words: “for other Claude models; the transfers keep their assumption label and caution.”

Scope: the findings below concern the normative wording in these two parts, not an assertion that the implementation currently produces incorrect results. Cross-referenced rules are treated as defined elsewhere. The connector returned the complete text but supplied no citation identifiers; source locations are therefore identified by part and named paragraph rather than fabricated citation tokens.

1. Findings by severity
Critical

None.

High

None.

Medium

The frozen-workload rule and the reconstruction-failure rule prescribe different responses to the same refresh event. Issue: Part 3’s “Admission and persistence” paragraph says that if rounded AA fields cause many reconstruction failures, “the admitted set would change,” changing the workload hash and stopping release as a migration. The same paragraph subsequently says that membership is frozen and that later “withdrawn or failed evidence” invokes row-level handling without changing the workload or its hash. These are distinguishable policies, but the text does not supply the distinguishing predicate. For example, an existing component whose reconstruction starts failing after AA changes its reporting precision is both failed evidence under the persistence rule and the explicit trigger for the earlier migration rule. Why it hurts the objective: the workload determines what the dollar figures mean. A routine refresh must deterministically preserve that workload, hold publication, or initiate an explicit migration—not leave the choice dependent on which sentence an implementer follows. Concrete change: separate initial admission, refresh of an existing workload, and proposed migration into explicit states. During refresh, retain the admitted set and hash; update evidence statuses and apply the established eligibility rules. If widespread reconstruction failure additionally requires a release hold, specify that as a separate gate with a machine-testable condition. Re-enumerate components only for a proposed migration, not as an implicit consequence of failed reconstruction. Source: Part 3, “Admission and persistence (E26),” especially the E209 rounding-failure example and the final persistence sentences.

Part 4 retains release-cutoff report-window instructions that conflict with the adopted per-cell search-window rule. Issue: Part 4 expressly defines the counting window as [V − 30 days, V] and later repeats concordance “within the 30-day window.” The supplied decision ledger says O161 ends a cell’s report window at its latest staged search; E308 distinguishes the release envelope from that cell window. This is not a recommendation to revisit O161. The new finding is that the operative measurement-object paragraph still gives a different executable instruction. A precedence rule can resolve the conflict, but a reader implementing the locally stated procedure can select a different initial report set. Why it hurts the objective: initial report admission can change the independent-source count, all-reports concordance result, pooled multiple, and selected route. It also affects whether evidence discovered through an incomplete search interval is treated as comprehensively researched. Concrete change: replace the local [V − 30 days, V] counting instruction with a direct reference to the authoritative cell-window rule, naming its endpoint explicitly. Distinguish:

first admission through the cell’s discovery window;

continued eligibility of previously admitted evidence under O127;

evidence age and scoped changes evaluated at the release cutoff.

Source: Part 4, “Measurement objects (E111),” “pooled-evidence clocks (E151),” and “Report set (E107)”; compared with supplied ledger O161 and E308.

Low

None.

2. Methodology design recommendations

These are implementation clarifications for the two findings, not proposals to change the owner’s scoring, cohort, evidence-transfer, or Value Multiple policies.

Priority 1 — Make workload persistence a tested state transition

Publish or encode three operations:

Operation	Component set	Evidence panel	Permitted result
Initial admission	Enumerated under E140	Constructed from current complete evidence	Create a workload
Refresh	Frozen	Recomputed evidence statuses	Score, flag, exclude from interval eligibility, or hold under an explicit gate
Proposed migration	Explicitly reconsidered	Constructed for the proposed workload	Apply migration and anchor requirements before activation

Add a regression fixture in which an admitted component becomes unresolved solely because the source changes reporting precision. Assert that:

its evidence status changes;

the active workload’s component set and hash do not silently change;

any release hold has a specific gate identifier;

any replacement workload remains a proposal until its migration requirements pass.

This preserves Part 3’s public-data approach while removing the ambiguity between evidence deterioration and workload redesign.

Priority 2 — Use one report-admission predicate throughout Part 4

For each model–plan cell, give the authoritative discovery-window object an identity and reference it from every report-selection paragraph. Keep separate fields for:

the window’s start and end;

the latest staged-search completion;

each report’s observation date;

first-admission release;

current lifecycle status;

current scoped-change flags.

A useful regression fixture places the latest staged search before 
𝑉
V, with one report inside the cell window, one in the subsequent unsearched gap, and one previously admitted report now outside the discovery window. Assert their treatment under O161, O127, and release-cutoff change detection separately.

This implements already-adopted distinctions; it does not add another research stage or alter the two-report requirement.

3. Questions for the owner

None. The two issues can be resolved by making the existing policy transitions explicit; neither requires reopening a binding owner decision.

4. Verdict

VERDICT: HAS FEEDBACK