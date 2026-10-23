# Internal review I28 — Claude Sonnet 5.5 (effort low) on draft r87

## 0. Read check
First line: "# ValueRank methodology — draft r87".
Last line (1075 of the folded copy) is only "(E95, E101)."; it ends the Known limitations paragraph. The last 12 words of that paragraph are: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
I read all 1075 lines, the ledger brief, ledger sections I25–I27 and O39–O44, and AGENTS.md. I also checked `data/plan_cost_routes.json` to see whether a rule is executable. I did not run web searches: the 2026 sources (AA pages, SemiAnalysis, Bug Hunt, tbench.ai) are not verifiable from my knowledge, so I cite the repository files instead.

## 1. Findings by severity

**Critical**
None.

**High**

H1. The closed source list (E239) conflicts with AGENTS.md's "exhaustive search". It also lets the registry decide which frontier family goes unranked.
- Where: the Cohort section says a missing leaf needs a search log of an "exhaustive search". E239 then says a fill counts only from a registered source and "each logged search covers every registered source", so "whether a leaf is missing is a deterministic function of the registry".
- AGENTS.md makes the logged exhaustive search the only way a frontier family goes unranked. It also says a manually maintained roster or a missing supplementary benchmark "must not silently exclude a frontier model".
- A search limited to registered sources is not exhaustive. A third party that ran FrontierCode 1.1, DeepSWE v1.1 or Terminal-Bench 4.0 on the exact configuration, but is not in the registry, would leave a frontier family listed instead of ranked. The draft would be deterministic but would not follow the owner's rule.
- Fix: keep the closed list for what may fill a leaf. Add a required open-web discovery step to every search log for a listed frontier or near family: queries, dates, and each unregistered candidate found. For each candidate, record either a dated registry addition or a dated rejection with a reason (different benchmark version, different effort, not the exact configuration, no published method). The build should fail on a listed frontier or near family whose log has no open-web step, or has an unresolved candidate.

H2. The common-GPT and MiMo Plan assumptions are not specified in the draft, and the implementation behaves differently from the draft's comparator rule.
- `data/plan_cost_routes.json` (line 20) says the common ChatGPT route takes "the lower reported model-conditional figure per plan". For Plus that is GPT-6 Astra's 8.1x, although GPT-6.1 Sol was measured at 10.55x on the same plan.
- The draft says only "common GPT multiple". Its comparator key 3 selects the larger multiple, and it says a SemiAnalysis per-(plan, model) measurement "replaces any owner-named transfer for that model". Read literally, GPT-6.1 Sol would take 10.55x, or the larger donor would be picked. Two faithful implementers diverge.
- The lower-figure rule appears nowhere in the draft or the ledger (I grepped both).
- Effort is unaddressed. The route key includes effort, and case (1) of E106 excludes effort mismatches. The draft never says at which effort SemiAnalysis measured Opus 5.5, GPT-6.1 Sol or Astra. It also never says how an effort-unlabelled model-level measurement attaches to five effort-specific GPT-6.1 Sol rows, or to Opus 5.5 (max). AGENTS.md says not to transfer between reasoning efforts.
- MiMo 1.5× is listed (line 428) among "model-to-model transfers … with donor measurement identified", yet line 432 says it has no donor measurement and ages from its authorisation date. It is also absent from AGENTS.md. The data file records it as "User instruction in this chat on October 8, 2026" with numerator "unavailable".
- Fix:
  - State the common-GPT rule exactly: donor set, lower-of selection, and whether a model with its own measurement keeps it.
  - State how an effort-unlabelled measurement binds to efforts, and the measured effort of each donor.
  - Move MiMo 1.5× out of the "transfer" list into its own class, "owner assumption without a measurement", with its origin.
  - Make the comparator state that the lower-of rule overrides key 3 for this class.

**Medium**

M1. Stale text contradicts the adopted wording on separability direction.
- The Outputs section says the noise bands "are labelled with the independent-task approximation and its conservative direction". The same section says the direction "is not established", which is the I27 M3 outcome. O42's ledger entry also calls the threshold "conservative".
- If a band is labelled conservative, a reader infers that real separability is at least as good, which the draft denies. This also misleads on the Plan basis, where 20 of 31 rows rest on transfers whose error is omitted.
- Fix: replace "conservative direction" with "direction not established". See Q1 for how to reconcile O42.

M2. The Plan-evidence change detection that O40 needs has no captured baseline.
- E238 and I25 M3 say the SemiAnalysis article is not captured and no hash is published, so it is pinned only by URL and transcribed figures. O40 now requires that an exact measurement added later replaces a transfer at once. That requires detecting additions. E159 says rebuilds must reproduce the scores without consulting live pages, and the controlled measurements are the only Plan numerators for Anthropic and OpenAI. This argument is new because O40 postdates M3.
- Fix: retain a permitted capture of the figures table (or at minimum a normalised extract and its hash) in the bundle at selection and at each release. Define "added after selection" as a new (plan, model) row in that normalised table. A hash-only comparison would suffice as detection.

M3. "Ranked" has two meanings.
- A cohort row is "a ranked configuration" (line 169). Muse Wonder Full is "ranked" but has no value score and no rank. O43 and AGENTS.md use "ranked".
- That row still sits in the bar population and moves the ladder (H_k positions use n = 32). It can never compete on cost. A faithful reader of "ranked configurations only" could include or exclude it.
- Fix: rename the term (for example "full-benchmark row" versus "scored row") and state explicitly that the bar population includes costless rows by choice. Add a one-line sensitivity of the ladder with that row removed.

**Low**

L1. S1T uses a plug-in binomial SE, which is exactly 0 at p = 0 or 1 (and clipping at the boundary shifts the median). Use a Wilson or Jeffreys-type SD for any leaf at or near a boundary.

L2. The anchor version string v3-2026-10-21 stayed fixed across three pre-release re-freezes with different anchor values (O33, O36 changed the low anchors). Nothing external was published, so no harm today. For the future, append a content hash or serial to the version ID.

## 2. Methodology design recommendations (prioritised)

1. Replace the Plan separability caveat with a neutral transfer tolerance. This is an Owner decision challenge to O35's "no Fable-based diagnostic", but the recommended design does not use Fable.
   - On the Plan basis, print for each row that rests on a transfer the factor by which its multiple could be wrong before the row leaves its noise band: 2^(threshold ÷ value points per cost doubling). With about 3.35 points and 2.02 points per doubling, that is about 3.2×.
   - Mark such rows in the band column ("band excludes transfer error").
   - This makes the 20-of-31 transfer dependence visible per row. It is a tolerance, not a donor-error estimate.
2. Add a public submission path for end-user usage reports. A GitHub issue template with required fields: plan tier, date, window, exact model and effort, API-priced estimate, optional receipts. The current search found Reddit and X unreachable from the build environment, and the non-Anthropic/OpenAI report channel yielded one route (SuperGrok Heavy). Reports in the 30-day window are the only path to a measured route for those providers. Without a channel, every such Plan row will stay on assumptions or API fallback.
3. Split the draft into a normative core and a "dormant machinery" appendix. The appendix would hold the E54, E80, E105, E115, E39 capacity machinery, E210, S1M and the rules E235 indexes, each with its activation condition. A public methodology of this length (1,075 dense lines, most describing rules that cannot fire today) is hard to audit. This also keeps the live rules (O36, O38, O39, O42, O44) from being buried.
4. Report the headline bar's dependence on the cohort composition in the headline sentence. The frozen headline bar is 55.3 and the frontier-families bar is 61.0, a gap larger than the 4.5-point noise margin. Both bars are already published (E199), so this is a wording change rather than a new calculation.

## 3. Questions for the owner
Q1. O42 calls the band threshold "conservative", but O39 and the I27 outcome say the net direction is not established. Which governs the wording? I recommend "direction not established", labelling the thresholds as an independent-task approximation only. If you keep "conservative", the draft should say in which respect (it widens the gap relative to correlated tasks, but omitted sources point the other way).
Q2. What is the origin of MiMo 1.5×? If it is neither an end-user report nor a SemiAnalysis measurement, AGENTS.md's numerator rules do not cover it. Should AGENTS.md record it, or should it be dropped to API fallback?
Q3. For the common-GPT assumption, should GPT-6.1 Sol and GPT-6 Astra each keep their own measured figures where the route's effort matches, or does the "lower reported figure for every GPT model" rule override them?

## 4. Verdict
VERDICT: HAS FEEDBACK
