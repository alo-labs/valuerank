0. Read check

Read both listed parts through their ends at commit d3a478e2d45071810c58271131a7bb67b5d61955. This review covers only those parts.

Part	First line	Last 12 words
13	## Governance	build for a re-capture of both (scores.json `aaStateReconciliation`, E322, on reviewer 87);
14	a point without a captured page is captured within the window, its common revision unverified. **Cohort capture age (E211)**: the AA chart and catalog capture that defines the cohort is at most 7 days old at the release cutoff. The refresh gate fails on an older capture, and on any near-frontier family that is neither rostered nor deferred by a dated, reasoned roster decision. Every plotted point in the capture keeps its exact model name, effort, fallback state and direct AA owner link, with the capture's observation time, so unscored rows keep them in the reconciliation inventory too. Each capture publishes the rendered-frontier entrants and exits against the previous capture, and the reconciliation report lists every frontier and near row with its rank status. Today the capture, the latest under Intelligence Index v5.0 (the 2026-10-31 capture was the first, O132), was taken at 2026-11-01T05:53:05Z, before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant; O65 had moved it from 2026-10-23T06:26:23Z and O47 from 2026-10-21T05:24:16Z). Its chart selects 89 catalog models and plots 82, far fewer than v4.3.2's. Against the previous capture (2026-10-30), on the rendered frontier no vertex entered or left. In the cohort, GPT-6.1 Terra at five efforts, GPT-6.1 Sol at low and Gemini 4 Carbon joined, and DeepSeek V4.1 Flash 1017, Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro, MiniMax-M3.1-Flash, GPT-5.6 Luna at low, Claude Haiku 5.5 at max and xhigh, Claude Sonnet 5.5 at xhigh and Claude Opus 5.5 at medium left the plotted frontier and near set and remain in this release's cohort as retained configurations under O145 (reviewer 88), no longer on or within the near gap of the rendered v5 frontier (O51); the 2026-10-23 capture's near set had grown by DeepSeek V4.1 Flash 1017 and MiniMax-M3.1-Flash, both then new to the chart; the capture's comparison record is in data/aa_frontier_capture.json. **Tariff applicability (E141)**: each price record carries observed_at, effective_from, effective_until (only where publicly established), tariff_status (standard / promotional / grandfathered), applicability_conditions, scheduled_refresh_at (the next known effective boundary, refreshed on schedule independently of page diffs) and a source evidence ID; a release uses the prices applicable at its declared valuation timestamp (a mismatch with the prices AA applied is resolved by E170); a promotion with an unknown end keeps the applicable price in the primary ranking, flagged "promotional tariff", with a named S2 standard-tariff branch only where the standard tariff is publicly documented and the consumption ledger supports repricing; an AA note that its cost omits a tariff component (at O106 the Claude Haiku 5.5 rows: AA's note that their higher long-context pricing is not reflected in AA cost figures; the rows carrying one are listed in scores.json rows[].aaCostCaveat) is shown on the row as "AA cost caveat". Unknown boundaries stay unknown (no assumed dates).	it is in draft-r171.md in the same folder of the repository.

Source locators below refer to the two connector-read files and their named rules. The connector supplied their full text but no citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

The independent-source agreement bootstrap should distinguish configuration resampling from model-identity resampling.

Issue: Part 14, “Independent-source checks” (E62/E66/E71), specifies “model-row bootstrap intervals.” The cohort can contain multiple efforts of one model, as the same part explicitly describes. The wording does not distinguish resampling configuration rows independently from resampling model identities with their efforts together.

Why it hurts the objective: These procedures answer different sensitivity questions. Independent configuration resampling can repeatedly separate sibling efforts whose benchmark behavior shares a model identity. Consequently, the displayed interval can depend on how many efforts a model contributes, not just on how consistently independent evidence agrees with ValueRank. This is a limited concern because the draft already labels these intervals descriptive matched-panel sensitivity rather than inferential confidence or ranking certification.

Concrete change: Define the current procedure explicitly as a configuration-row bootstrap. Whenever the matched panel contains repeated model identities, publish a model-identity cluster-bootstrap companion that resamples each identity with all its matched efforts together. Print both the number of configurations and the number of distinct model identities. If every identity contributes one row, state that the two procedures coincide.

Source: part 14, “Independent-source checks” and “Cohort capture age.” What is new relative to the ledger: This concerns the resampling unit of the independent-evidence agreement diagnostic—not task-sampling uncertainty, benchmark-noise kernels, or the policy allowing multiple efforts to rank.

2. Methodology design recommendations

Specify the agreement diagnostic’s resampling unit and add a clustered companion only when needed. Preserve the existing point estimates and rankings. For a matched panel partitioned into 
𝐺
G exact AA model identities:

Draw 
𝐺
G model identities with replacement.

Carry every matched configuration of each sampled identity into the replicate, keeping the paired quality and value observations together.

Recompute each already-defined 
𝜏
𝑏
τ
b
	​

 statistic using the existing treatment of ties and undefined statistics.

Publish the resulting interval beside the configuration-row interval, labelled “model-identity cluster-resampling sensitivity.”

Report the fraction of replicates with undefined 
𝜏
𝑏
τ
b
	​

; do not silently discard those replicates without disclosure.

When 
𝐺
G is too small for useful resampling, publish the point estimate, configuration count and identity count without implying that an interval establishes general agreement.

This uses the exact model identities and matched observations already required by the draft. It needs no additional benchmark runs, model-to-model evidence transfer, private data or change to owner-set weights. Source: part 14, E62/E66/E71’s paired agreement statistics and E211’s exact model-name inventory.

3. Questions for the owner

None.

4. Verdict

The reviewed governance and limitations sections are materially sound. The remaining recommendation is a low-severity clarification and sensitivity companion for one descriptive diagnostic; it does not challenge the cohort, exact-variant evidence rules, Plan numerator policy or release framework.

VERDICT: HAS FEEDBACK