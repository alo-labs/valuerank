# DR-CRITIQUE: adversarial review (deep mode, two cycles)

Run: `2026-10-17-value-ranking-sites-landscape`. Reviewed against `scope.md`, `research-plan.md`, `triangulation.md`, `outline.md`, `research_report.md` (9,881 words), `claims.jsonl` (64 claims), `evidence.jsonl` (218 rows), `sources.jsonl` (91 sources), `retrieval/lead-scan.md` and `validation/*.log`. No new retrieval was done and no URL was re-fetched.

**ID conventions.** `claims.jsonl` uses 16-hex claim ids, not `C<n>`. In `claim_id` I give the triangulation number (`C1`..`C21`, `X1`..`X12` for the conflicts register) where one exists, and add the first eight hex characters of the claims.jsonl id plus its line number where a specific claim row is at issue (for example `845a1889 / claims.jsonl:7`). `evidence_ids` are eight-character evidence prefixes where I could read them; otherwise I name the source by display number (`S<n>`, the bibliography number).

---

## Cycle 1: skeptic

### Narrative

**1. Steelman against the central verdict (A1).** The strongest case against "no other site combines benchmark quality with subscription-plan cost at the model level" is that the verdict turns on the word "combine", and the report's own evidence contains two partial counterexamples. RemakeBench pairs per-round quality evidence for four models with an average-cost column that includes subscription CLIs and marks provider estimates (S54, evidence 1032adb2 and 53a223b7), next to a cross-vendor plan allowance table (S53). Klu ranks a subscription-only model on its quality index with the plan prices in a footnote (c1866a94, S18). The report resolves both as "not an aggregate, so not a combination". That is a defensible reading, but it is a definition chosen after the fact, and it happens to be the definition under which ValueRank is unique. A hostile reader would say: "RemakeBench already puts plan-priced cost beside measured quality per model; ValueRank adds a division." The "bounded negative" label hides that the boundary is definitional, not only a matter of search depth.

The search behind the negative is also thinner than "about fifty sites examined" suggests. `retrieval/lead-scan.md` named roughly fifteen further pages that are plan-comparison or coding-agent cost pages (aizolo, vortenza, altaitools, tech-insider, docs.bswen, aionx, morphllm, tembo, discretestack, neura.market, aiven, yourgpt, llmleaderboard.in, fast.io, felloai). A grep of `sources.jsonl`, `evidence.jsonl` and `retrieval/*.jsonl` finds none of them. The scope names Copilot and Cursor as in-scope plan comparisons; the report mentions neither, and `evidence.jsonl` mentions Cursor only twice. The research plan names Hacker News, Reddit and X as a source class; none was retrieved, although A3 ("plan comparisons exist mostly as posts, forums and trackers") is a claim about exactly those venues. The triangulation outcome for C1 ("PASS-AB for the AA boundary") credits the AA statement that its own coding-agent index excludes plan pricing. That shows a boundary for AA only; it says nothing about other sites. The remaining support is "at least eight C pages that lack the feature", which is absence on pages the search happened to find.

**2. Contradiction hunt.**

- *Derived numbers.* Table 3 and Recommendation 1 rest on a "3.7 times" spread across four Max 20x measurements. The ratio is arithmetically right (6,547 / 1,751 is 3.74 when ml0x's monthly figure is divided by 4), and the report labels the weekly conversions as its own. The problem is conceptual: ml0x is one seat's consumed workload over 2026-07-29 to 2026-08-28, priced at Opus 5 list rates. It is not an allowance measurement, and the report itself calls it a lower bound-style, cache-dominated single-user figure. It is also higher than SemiAnalysis's figure for the plan's full monthly limit ($26,187 versus $11,726, 2.2 times), which cannot be the same quantity at the same prices. The period also predates the 13 September expiry of the temporary 50% weekly increase that the report cites, so it may sit under a different limit regime. Putting it in the same range as Wokey and RemakeBench makes the "spread" look like measurement disagreement when it is mostly a difference in what is measured. The ranges then drive the Recommendation 1 tolerance-band argument.
- *"Most aggregators inherit AA data".* The Executive Summary, F2, the Claims-Evidence Table ("Confirmed") and the Synthesis all say or imply this. The report's own Table 2 lists 12 sites; only Klu, WhatLLM and Dervity are documented as taking AA's cost, and AI Model Comparison and Analytical Insider use the AA index for quality. BenchLM, Model Price Watch, TokenCost, CostGoat, KickLLM, Swfte and LLM Stats are described as list-price or own-composite arithmetic. By the report's own table, seven of twelve do not inherit AA. The Counterevidence Register then says "AA dominates but is not alone", which contradicts the "Confirmed" outcome.
- *LiveBench cost basis.* The report says LiveBench publishes a "measured cost-per-successful-task view" and that ValueRank ingests it as such. The evidence (6e694250, S90) is a directory listing of file names (`cost_2026_06_25.csv`) plus ValueRank's own field name `costPerSuccessfulTaskUsd`. Nothing quoted from LiveBench says the file is per successful task. The claim verifier flagged this claim `needs_review` (score 0.2, "number mismatch, year mismatch"; claims.jsonl:7). The report nonetheless uses it to "resolve" conflict X5 in favour of an A2 source and in F3/Recommendation 4 to say the two bases "already differ in what they mean".
- *D-grade relays and Chinese-language primary.* Hedged consistently in most places, but F7 opens with "A Chinese financial-media report states that on 30 June SuperCLUE 'for the first time' released...", while the claim verifier gave 0.15 and `needs_review` (claims.jsonl:56). That is likely a lexical-overlap artefact of a Chinese source, but nobody has checked, so the support status is unknown, not good.
- *SemiAnalysis grade.* S50 is graded B2 and carries "PASS-AB" for C11 and C21, but the stored evidence rows for its methodology and key findings are labelled "fetch summary, not verbatim" at confidence 0.65 to 0.7, and the page is partly paywalled. The cache statement in the evidence is "costs almost nothing on some plans and may not move the meter at all"; the report generalises to "the sources agree that cache reads barely count against plan meters". The grade rests on the source's reputation, not on what was read.

**3. Missing stakeholders and source classes.**

- *Enterprise buyers.* Enterprise TCO consultancies are excluded by scope, but per-seat business and enterprise plans, committed-spend discounts and batch or cached pricing are not "consultancies". They change the API basis (list price is rarely what a large buyer pays) and the plan basis (Team and Enterprise tiers). Only Wokey's Team Premium line touches it.
- *Open-weight and self-hosting cost.* Hardware and GPU benchmarks are out of scope, but open-weight models in the aggregators are priced by a hosted provider whose price can differ several-fold from another provider's. The report never says which provider's price each aggregator uses, or that ValueRank's API basis is the AA run cost for one provider's endpoint.
- *Non-English markets.* Beyond SuperCLUE (one press story) the report has no Japanese, Korean, European or Indian coverage (the plan promised "European comparisons"; `lead-scan.md` names an India-focused leaderboard, unread). Chinese vendors sell their own coding subscriptions, which is the plan-cost world A1 is about; none was checked.
- *Benchmark owners' own statements.* AA's methodology is read, and the report notes its self-description. What is missing is any owner statement about downstream reuse: AA's terms of use or attribution rules for derived sites, and whether AA or LiveBench allow the redistribution that a pinned-snapshot site depends on. ValueRank's single-upstream risk is described as accuracy risk, not licence risk.
- *ValueRank as commissioning party.* The report flags the conflict of interest on S91 and hedges "alone" claims, which is good. It still uses ValueRank's internal documents (project instructions designating SemiAnalysis; an internal site audit) inside Recommendations 1 and 8 and in F3 while the Limitations section says these are "not part of the external evidence". There is no inverse test (what a reader would lose by using ValueRank instead of AA plus Wokey), so the conclusion tilts toward the commissioner.

**4. Failure modes if the recommendations are wrong.**

- *Plan formula and reasoning tokens.* ValueRank's plan cost is AA run cost divided by the model's highest eligible Value Multiple, then by the Index. The report spends F2 and F3 showing that list-price formulas mis-price reasoning tokens, but never applies the same test to ValueRank's own formula. The numerator (AA cost) is built from AA's token mix and live cache-hit rates. The divisor (a SemiAnalysis multiple) is built from a plan's full limit priced at list rates with a different token mix, in which cached reads cost almost nothing. For a reasoning-heavy model the AA cost is dominated by output tokens, while the plan meter cost of those same tokens may be very different from the cache-heavy mix that makes the multiple large. Dividing one by the other assumes the multiple is workload-independent, which the report's own evidence says it is not ("model-specific and workload-shaped"). "Highest eligible" also selects the most favourable plan per model, a systematic upward bias on value that the report does not discuss. Recommendation 3 tells ValueRank to state the unit; it does not tell it to test the formula.
- *Uniqueness is wrong.* Recommendation 7 has the right hedge. Recommendation 2 adds a watch on RemakeBench but gives no trigger: no definition of what observation would end the "alone" claim (an aggregate score, a quality-adjusted plan column, a second site doing the division). Without that, the watch cannot fail.
- *Reproducibility.* All plan figures are dated weekly snapshots from sites that change daily or weekly, and no archived copies are recorded. A reader re-checking in a month will not find the pages the report describes.

### Cycle 1 deltas

```json
[
  {
    "cycle": 1,
    "delta_type": "decision_risk",
    "claim_id": "C1 (A1 verdict; Table 6; Exec Summary para 2; Rec 7)",
    "description": "The A1 'bounded negative' depends on a definition of 'combine' (quality aggregate plus plan cost) that excludes RemakeBench (quality evidence per model plus subscription-CLI-priced cost per model plus a plan allowance table) and Klu (subscription-only model on the quality index with plan prices in a footnote). The report treats both as non-combinations without saying the test is definitional. The AA boundary evidence (74d45988) shows only AA's own scope.",
    "evidence_ids": ["1032adb2", "53a223b7", "c1866a94", "74d45988", "S53", "S54", "S18"],
    "severity": "high",
    "loopback": true,
    "proposed_fix": "In Exec Summary para 2, Table 6 and F8, state the test explicitly: 'no site joins an aggregate quality measure to a plan-derived cost at the model level and ranks on it'. Add a 'partial combinations' row naming RemakeBench (per-model cost with subscription CLIs beside quality evidence, no aggregate) and Klu (subscription-only model, plan prices in footnote). Re-grade the C1 outcome from 'PASS-AB for the AA boundary' to 'BOUNDED-NEGATIVE, definition-dependent'. Drop the implication that the AA statement supports absence elsewhere."
  },
  {
    "cycle": 1,
    "delta_type": "missing_source_class",
    "claim_id": "C1 / C9 (A3) / scope in-scope items 1-2",
    "description": "Sources the lead scan discovered were never read or dispositioned (aizolo, vortenza, altaitools, tech-insider, docs.bswen, aionx, morphllm, tembo, discretestack, neura.market, aiven, yourgpt, llmleaderboard.in, fast.io, felloai), yet the report says 'about fifty sites and projects were examined'. Copilot and Cursor plans (named in scope) have no coverage. The planned community class (Hacker News, Reddit, X) is absent, though A3 is a claim about posts and forums. Absence claims therefore rest on an unrepresentative page set.",
    "evidence_ids": ["retrieval/lead-scan.md", "research-plan.md", "S44", "S55", "S56"],
    "severity": "high",
    "loopback": true,
    "proposed_fix": "Either (a) run a bounded DR-REFINE retrieval pass over the plan-comparison and coding-agent-cost pages listed in lead-scan.md plus Copilot, Cursor, Gemini and one forum sweep, and record each as read, unreadable or irrelevant; or (b) add a 'Discovered but not read' table to Limitations listing each unread page, and reword 'about fifty sites examined' to the number actually registered. Also soften A1 and A3 verdicts to say which plan families (Copilot, Cursor, Gemini, Chinese coding plans) were not checked."
  },
  {
    "cycle": 1,
    "delta_type": "unsupported_inference",
    "claim_id": "X1 / Table 3 / Rec 1 (Max 20x spread of about 3.7 times)",
    "description": "The 3.7x spread mixes an allowance measurement (Wokey, RemakeBench, SemiAnalysis) with one seat's consumed workload (ml0x) priced at Opus 5 list rates over 2026-07-29 to 08-28, before the Sept 13 limit change. ml0x's $26,187 per month is 2.2 times SemiAnalysis's figure for the full monthly limit, so the two cannot be the same quantity at the same prices. Calling the range a spread of 'measurements' of 'allowance' overstates disagreement and then drives the Recommendation 1 tolerance band and the Exec Summary '$2,700 to $6,500 per week'.",
    "evidence_ids": ["S51", "S50", "S52", "S53", "S46"],
    "severity": "high",
    "loopback": true,
    "proposed_fix": "Split Table 3 into 'allowance measurements' (Wokey, RemakeBench, SemiAnalysis) and 'consumed-workload evidence' (ml0x). Compute the allowance spread without ml0x (about 1,751 to 2,930 per week, 1.7 times, still with different dates and models) and report ml0x as an upper-envelope consumption datapoint with its own caveats (model priced, cache rate, pre-Sept-13 regime). Update Exec Summary para 3, Recommendation 1 and the Claims-Evidence row accordingly."
  },
  {
    "cycle": 1,
    "delta_type": "decision_risk",
    "claim_id": "C20 / C21 / F8 / Rec 1 and Rec 3 (ValueRank plan formula)",
    "description": "The report shows that list-price formulas mis-price reasoning tokens but never tests ValueRank's own plan formula on the same grounds. AA cost uses AA's token mix and live cache rates; the SemiAnalysis multiple uses a plan's full limit at list rates with a cache-dominated mix. Dividing one by the other assumes the multiple is workload-independent, which the report's own evidence contradicts (model-specific, cache-dominated). 'Highest eligible' multiple selects the most favourable plan per model, an upward bias not discussed. The numerator source is partly paywalled and known mostly through a secondary summary.",
    "evidence_ids": ["S50", "S46", "S52", "S51", "S91", "cabcc834"],
    "severity": "high",
    "loopback": true,
    "proposed_fix": "Add a subsection to F8 ('Does the borrowed formula survive reasoning-heavy models?') stating the token-mix mismatch between AA cost and the plan multiple, the max-over-plans bias, and the dependence on one secondary-reported numerator. Add a recommendation: publish a sensitivity row for the plan basis (multiple varied across the Wokey/RemakeBench/SemiAnalysis range) and flag models whose AA cost is dominated by output tokens. State this as the main decision risk in the Exec Summary."
  },
  {
    "cycle": 1,
    "delta_type": "unsupported_inference",
    "claim_id": "C21 / C11; claims.jsonl:41 (c869804a); F4 paragraph after Table 3",
    "description": "S50 is graded B2 and carries PASS-AB, but its stored evidence rows are fetch summaries (confidence 0.65 to 0.7) and the page is partly paywalled. The verbatim cache quote says reads cost 'almost nothing on some plans and may not move the meter at all'; the report generalises to 'the sources agree that cache reads barely count against plan meters', and uses that to explain why multiples are large. The claim verifier scored this claim 0.6 with an entity mismatch.",
    "evidence_ids": ["S50", "S51", "S52", "c869804a"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Reword F4 and Recommendation 3 to 'on some plans (Anthropic; not established for OpenAI or others)'. In triangulation C21, downgrade the PASS-AB rating to 'PASS-AB, partial read' and note that the evidence is a tool summary of a partly paywalled page."
  },
  {
    "cycle": 1,
    "delta_type": "contradiction",
    "claim_id": "C3 / Exec Summary para 1 / Claims-Evidence row 3 / Synthesis 'Dependence and correlation'",
    "description": "'Most aggregators inherit AA data' is marked Confirmed, but the report's own Table 2 (12 sites) shows only Klu, WhatLLM and Dervity taking AA cost and two more using the AA index for quality (AI Model Comparison, Analytical Insider). Seven sites (BenchLM, Model Price Watch, TokenCost, CostGoat, KickLLM, Swfte, LLM Stats) use list-price or own composites. The Counterevidence Register's 'AA dominates but is not alone' contradicts the Confirmed outcome.",
    "evidence_ids": ["5930df3e", "c86d76a2", "S18", "S39", "S42", "S29", "S31", "S38", "S34"],
    "severity": "medium",
    "loopback": true,
    "proposed_fix": "Replace 'most' with the count: 'five of twelve aggregators in Table 2 take AA cost or the AA index (Klu, WhatLLM, Dervity, AI Model Comparison, Analytical Insider); the others use list-price arithmetic or own composites'. Change the Claims-Evidence outcome to 'Partly confirmed' and add an 'AA-derived' column to Table 2."
  },
  {
    "cycle": 1,
    "delta_type": "unsupported_inference",
    "claim_id": "845a1889 / claims.jsonl:7; X5; F3 (LiveBench)",
    "description": "The statement that LiveBench publishes a measured cost-per-successful-task view rests on a directory listing (file names only) and on ValueRank's own field name costPerSuccessfulTaskUsd. No LiveBench text says what the cost file measures. The claim verifier marked it needs_review (0.2). The report still uses it to resolve conflict X5 in favour of an A2 source, to list LiveBench as 'measured cost, A2' in Table 5, and in Recommendation 4 as a unit to label.",
    "evidence_ids": ["6e694250", "S90", "S5", "S21"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Reword to 'LiveBench release data includes a cost file; what it measures is not documented in the retrieved text, and ValueRank ingests it as cost per successful task'. Lower the Table 5 grade for this cell to C and mark X5 'resolved for existence of a cost file, open for its definition'."
  },
  {
    "cycle": 1,
    "delta_type": "unsupported_inference",
    "claim_id": "C16 / 1fb549f9 / claims.jsonl:56 (SuperCLUE quadrant); F7",
    "description": "F7 opens with the SuperCLUE quadrant as a reported fact. The claim verifier gave the claim 0.15 and needs_review, probably a lexical artefact of a Chinese-language source but unchecked. Other places in the report hedge correctly (secondary-only), so prose and register disagree on how firmly the claim is held. The quoted Chinese text in evidence is clear, so a native-language spot check would settle it cheaply.",
    "evidence_ids": ["S81", "S78", "S76"],
    "severity": "low",
    "loopback": false,
    "proposed_fix": "Add 'reported by Jingji Cankao Bao (via Eastmoney)' to the first F7 sentence and note in Limitations that the claim verifier could not match the Chinese source (needs_review) and that a manual translation check was done against the quoted paragraph. Keep the secondary-only label in Table 5."
  },
  {
    "cycle": 1,
    "delta_type": "unsupported_inference",
    "claim_id": "C12 (A4) / 5de8bae5 / claims.jsonl:50; Table 4; Exec Summary para 4",
    "description": "'No per-number evidence class was found' rests on one search log of three queries and a GitHub topic page (S87, confidence 0.55). Table 4 omits uncertainty and integrity practices that the report's own evidence shows exist: Terminal-Bench 95% confidence intervals and canary string, Scale's score +/- intervals, SWE-bench's Verified/Bash-only splits. These are provenance signals of a kind, so 'unmatched' may be narrower than it sounds. The A4 refutation ('common among the better sites') is also circular, defining 'better' by having the practices.",
    "evidence_ids": ["S87", "S9", "S20", "S10"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Add an 'uncertainty or integrity markers' row to Table 4 (Terminal-Bench, Scale, SWE-bench). Replace 'common among the better sites' with the count: 'dated pages 6 of about 20 aggregators examined; variant labels in 5'. Phrase the evidence-class negative as 'not found in three searches and one topic listing' in the Exec Summary."
  },
  {
    "cycle": 1,
    "delta_type": "unsupported_inference",
    "claim_id": "e9efe8ad / claims.jsonl:60; Exec Summary para 1; F2 point 1",
    "description": "'Value leaders therefore differ by formula' is stated generally in the Exec Summary but demonstrated for two sites, and the report concedes 'leader names for only two sites'. Klu's 'best value' is simply the cheapest listed model, so it is not a different formula producing a different leader; it is a different definition of value.",
    "evidence_ids": ["S18", "S29"],
    "severity": "low",
    "loopback": false,
    "proposed_fix": "In the Exec Summary change to 'leaders can differ by formula (two sites compared)'. In F2 describe Klu's 'best value' as 'lowest listed price', not a ratio."
  },
  {
    "cycle": 1,
    "delta_type": "missing_source_class",
    "claim_id": "scope (out-of-scope list) / F2 / F8",
    "description": "Enterprise and negotiated pricing (committed-spend discounts, batch and cache pricing, per-seat business tiers) and open-weight models priced by different hosting providers are not covered. The report never states which provider's price each aggregator uses, or that ValueRank's API basis is one provider's AA run cost.",
    "evidence_ids": ["S29", "S31", "S38", "S35"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Add to Limitations: 'List prices differ by provider for open-weight models and by contract for large buyers; the report did not compare provider choice across aggregators.' Add a row to Table 2 for 'provider used' where stated, and mark unknown otherwise."
  },
  {
    "cycle": 1,
    "delta_type": "missing_source_class",
    "claim_id": "F7 / research-plan search strategy item 8",
    "description": "Non-English coverage is one Chinese press story plus failed fetches of OpenCompass and HELM. The plan promised European comparisons; the lead scan found an India-focused leaderboard. No Japanese or Korean source and no Chinese vendor coding-subscription pricing (the plan-cost family relevant to A1) was checked.",
    "evidence_ids": ["S81", "S76", "S77", "S80", "retrieval/lead-scan.md"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Either run one bounded retrieval over Chinese vendor coding-plan pricing and a European or Indian leaderboard, or state in the F7 heading and Limitations that non-US coverage is 'China-only, one secondary source' and that A1 was not tested for non-US plan families."
  },
  {
    "cycle": 1,
    "delta_type": "missing_source_class",
    "claim_id": "C19 / F8 (AA dependence) / Rec 5",
    "description": "The report describes AA's single-upstream risk as an accuracy and version risk. It does not examine AA's (or LiveBench's) terms of use, attribution or redistribution rules, which determine whether a pinned-snapshot site can legally republish or derive from their data. This is a source class (benchmark owners' own statements about reuse) that the plan listed and the report skipped.",
    "evidence_ids": ["S1", "S2", "S15", "S5"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Add one retrieval item or a Limitations line: 'Owners' reuse terms were not reviewed.' Add to Recommendation 5 a step to confirm AA's terms for derived rankings and snapshot redistribution."
  },
  {
    "cycle": 1,
    "delta_type": "decision_risk",
    "claim_id": "C20; Rec 1; Rec 8; F3 parenthetical; Limitations",
    "description": "Commissioner conflict is flagged on S91, but the report also leans on ValueRank internal documents (project instructions designating SemiAnalysis; an internal site audit; 'the worked plan example planned for the site') inside Recommendations 1, 3 and 8 while the Limitations section says these are 'not part of the external evidence'. Recommendations thus partly rest on material the reader cannot check. No inverse test asks what a reader would lose by using ValueRank instead of AA plus Wokey.",
    "evidence_ids": ["S91", "cabcc834", "AGENTS.md (internal)"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Mark each recommendation clause that uses internal material with '(internal context)'. Add a short 'Where ValueRank is weaker than the alternatives' paragraph to F8 (smaller roster, single upstream, plan basis from one secondary-reported analyst, no live refresh) so the comparison is not one-sided."
  },
  {
    "cycle": 1,
    "delta_type": "decision_risk",
    "claim_id": "Rec 2; Rec 7",
    "description": "The watch on RemakeBench and Wokey has no falsification criteria and no archive policy. Nothing defines what observation would end the 'only site found' claim, and the weekly plan figures cannot be re-checked later because no archived copies are recorded.",
    "evidence_ids": ["S53", "S54", "S52"],
    "severity": "low",
    "loopback": false,
    "proposed_fix": "Add to Recommendation 2 an explicit trigger list: an aggregate score, a quality-adjusted plan column, or any second site dividing plan allowance by a quality index. Add 'archive each cited page (date-stamped copy or snapshot link) at refresh' to Recommendation 6."
  }
]
```

---

## Cycle 2: reviewer (editor's read)

### Narrative

The report is well organised, hedged in most places and long enough for deep mode (9,881 words; the Executive Summary is 351 words and the Introduction 485, both inside the assembly guide). It follows `reference/report-assembly.md` in substance, with three departures: Limitations comes after Recommendations (the guide puts it before), the Counterevidence Register and Claims-Evidence Table are extra sections, and the file name is `research_report.md` rather than the dated convention. None of these needs repair unless the downstream packager expects the convention.

The editorial problems are of four kinds.

1. **A recommendation that contradicts the body.** The Introduction, F8 and Table 7 say ValueRank's API basis is AA's *total cost to run the Intelligence Index* (the quantity ValueRank's project rules use to select models). Recommendation 4 says the API basis uses *AA's average cost per Index task* and then says that figure "does not count failures". Both halves are wrong or at least unsupported. Total cost and cost per task are different AA quantities. And AA's spend includes the cost of failed attempts; what it lacks is division by the number of successes. The recommendation is to publish a disclosure, so the wrong definition would be published.
2. **Inferences stated as findings.** Recommendation 1 says the Max 20x spread "is larger than many of the rank gaps a plan-based list would present"; the report contains no ValueRank rank-gap data. Recommendation 8 introduces a second uniqueness claim ("an opening... which no site was found to serve" for buyers of coding-agent subscriptions) with no search aimed at it. Table 7's audience and funding cells ("analysts; funding unknown", "researchers", "decision makers and analysts") are mostly unevidenced, and ValueRank's own cell uses the internal audit that Recommendation 8 says found audiences were not separated.
3. **Counts that do not agree.** "At least ten aggregators" (Exec Summary), "at least eleven" (F2, Table 6, Claims-Evidence Table) and a 12-site Table 2 (counting WhatLLM and Dervity separately). Recommendation 5 says "Four of the aggregators" and cites three sources. The Exec Summary cites [36] for AA's total cost view while F3 cites [17], which the bibliography labels "GLM-5 model page". "About fifty sites" matches no table.
4. **Bibliography quality.** Of 91 entries, 42 begin "(n.d.)" and 49 give a bare year, even though `sources.jsonl` holds a publisher for all 91 and a full `published` date for 49. No entry shows an author or publisher, and the registry has no authors (`authors` is empty on all 91). The format `(year). [Title](url)` makes news items, vendor blogs, arXiv papers and the baseline (S91, published 2026-10-08, publisher Ālo Labs) look alike. A reader cannot tell a C3 vendor blog from a B2 methodology page or see which entries are search-snippet relays; the "(n.d.)" entries include several the text relies on (S1, S2, S3, S6, S7, S27). The pass of `validate_report.py` on "Bibliography" did not check content.

One validator note: `verify_claim_support.log` reports 0% unsupported, but only 44 of 64 claims are fully supported, 18 are partial and 2 are needs_review (the two core ones are the LiveBench cost basis and the SuperCLUE quadrant). The Report Metadata block does not say so.

Do the Recommendations follow? Recommendations 2, 5 (once the count is fixed), 6 and 7 follow from the evidence. Recommendation 1's band is sound in spirit but argued from the wrong spread (cycle 1). Recommendation 3 is correct but incomplete (it asks for a unit statement, not a formula test). Recommendation 4 needs correction. Recommendation 8 does not follow.

### Cycle 2 deltas

```json
[
  {
    "cycle": 2,
    "delta_type": "contradiction",
    "claim_id": "Rec 4 vs Introduction 'Baseline' / F8 / Table 7; 7d5f868a (claims.jsonl:63)",
    "description": "Rec 4 states that ValueRank's API basis 'uses AA's average cost per Index task [15], which does not count failures'. The Introduction, F8 and Table 7 say the API basis is AA's total cost to run the Intelligence Index. These are different AA quantities (cost per task is a weighted average per task; total cost is token prices times tokens across all evaluations, repeats excluded). The phrase 'does not count failures' is also wrong in the evidence: AA's spend includes tokens used on failed attempts; the gap is that it is not divided by the number of successes.",
    "evidence_ids": ["S15", "S17", "S91", "5973dc95", "648a7645"],
    "severity": "high",
    "loopback": true,
    "proposed_fix": "Rewrite Rec 4: 'ValueRank's API basis is AA's total cost to run the Intelligence Index [17], [91]. It is a measured spend over all attempts, not a cost per correct solution; state this beside the figure and consider showing coverage beside cost [27].' Remove 'does not count failures' and the cost-per-task wording. Then check F3's sentence 'AA's cost per task... regardless of correctness' for the same slip."
  },
  {
    "cycle": 2,
    "delta_type": "presentation",
    "claim_id": "Bibliography [1]-[91]",
    "description": "42 of 91 entries read '(n.d.)' and the other 49 give only a year. No entry has an author, publisher or full date, although sources.jsonl holds publisher for all 91 and a full published date for 49 (authors are empty on all rows). The entry format cannot separate a vendor blog, a news relay, a paper and the baseline. Several load-bearing sources show '(n.d.)': S1, S2, S3, S6, S7, S27.",
    "evidence_ids": ["sources.jsonl (publisher, published fields)", "validation/validate_report.log"],
    "severity": "medium",
    "loopback": true,
    "proposed_fix": "Regenerate the bibliography as '[n] Publisher (YYYY-MM-DD or n.d.). Title. Source type, grade. URL (accessed 2026-10-17)'. Take publisher and published from sources.jsonl; where the registry has no date, use the page's own updated stamp from evidence (for example AA pages carry 'updated' stamps) or 'accessed 2026-10-17'. Add the reliability grade and mark search-snippet relays (S2, S13, S14, S49, S79) as 'via search summary'. Fix the registry first (citation_manager metadata update) so the render is not hand-edited."
  },
  {
    "cycle": 2,
    "delta_type": "presentation",
    "claim_id": "Exec Summary para 1 and 4; F2; Table 2; Table 6; Rec 5; F3; Introduction",
    "description": "Internal counts disagree: 'at least ten aggregators' (Exec Summary) versus 'at least eleven' (F2, Table 6, Claims-Evidence) versus 12 sites in Table 2; Rec 5 says 'Four of the aggregators' and cites three sources; 'about fifty sites' matches no table; AA total cost is cited as [36] in the Exec Summary and [17] in F3, and [17] is listed as 'GLM-5 model page'.",
    "evidence_ids": ["S17", "S36", "S18", "S39", "S42"],
    "severity": "low",
    "loopback": false,
    "proposed_fix": "Count once from Table 2 (12 sites, 5 AA-derived) and use that figure everywhere. Cite S36 (AA models page) for the total-cost chart or relabel S17 as 'AA model page (cost chart)'. Replace 'about fifty sites' with the number of distinct named sites in the sites register in triangulation.md."
  },
  {
    "cycle": 2,
    "delta_type": "unsupported_inference",
    "claim_id": "Rec 1 ('larger than many of the rank gaps a plan-based list would present')",
    "description": "The report contains no ValueRank rank-gap data, so it cannot say how the allowance spread compares with the gaps between models on the plan basis. The sentence is the main argument for publishing ranges.",
    "evidence_ids": ["S91"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Either remove the comparison or add a one-line computation from ValueRank's current plan-cost values ('re-ranking under the low and high multiples changes N of 16 positions') labelled as internal context, and mark it as an action for ValueRank to run, not a finding."
  },
  {
    "cycle": 2,
    "delta_type": "unsupported_inference",
    "claim_id": "Rec 8 (audience positioning); Rec 3 ('worked plan example planned for the site')",
    "description": "Rec 8 introduces a second uniqueness claim ('an opening... which no site was found to serve') about buyers of coding-agent subscriptions, with no search aimed at that audience (no Cursor, Copilot, or forum evidence). It also depends on an internal audit stated to be outside the evidence base. Rec 3 refers to a planned internal example.",
    "evidence_ids": ["S44", "S55", "S56"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Delete the 'opening' sentence or restate it as a hypothesis for a later study ('not tested here'). Remove or relabel internal references as '(internal context, not evidence)'."
  },
  {
    "cycle": 2,
    "delta_type": "unsupported_inference",
    "claim_id": "Exec Summary para 4; Table 4; Table 6 A4 row; Counterevidence 'Provenance is rare'",
    "description": "Prose and register disagree on A4. Table 4 shows dated pages at about six sites and variant labels at five among about twenty aggregators and plan sites, with most others 'not stated'. The summary says dating and variants are 'common among the better sites', and the Counterevidence Register 'narrows' A4. The word 'better' is defined by having the practice.",
    "evidence_ids": ["S29", "S35", "S38", "S18", "S53", "S55", "S3", "S6"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Report the ratio from Table 4 and let readers judge: 'Dating appears at 6 of N reviewed aggregators and plan sites; exact-variant labels at 5 of N'. Retitle the A4 verdict 'Partly refuted: present at a minority of sites, absent at most'."
  },
  {
    "cycle": 2,
    "delta_type": "presentation",
    "claim_id": "Table 5; Table 7 (audience and business-model cells)",
    "description": "Many Audience and Funding cells have no supporting evidence in the register: 'analysts; funding unknown', 'researchers', 'general; commercial', 'developers and buyers; commercial'. Table 5 'Best source grade' lumps ranges ('A1 to B3', 'B2/B3') and gives LiveBench A2 on the strength of a file listing. ValueRank's audience cell conflicts with the internal audit cited in Rec 8.",
    "evidence_ids": ["S34", "S35", "S43", "S41", "S7", "S90"],
    "severity": "low",
    "loopback": false,
    "proposed_fix": "Replace unevidenced audience cells with 'not stated on page' and keep only those with a page quote (affiliate disclosure, sponsor banner, paid tier, gateway promotion). Split lumped grade cells into one row per site."
  },
  {
    "cycle": 2,
    "delta_type": "presentation",
    "claim_id": "Report Metadata; validation/verify_claim_support.log",
    "description": "The Report Metadata block does not state claim-support results. The log shows 'unsupported_rate 0.0' but only 44 of 64 claims are fully supported, 18 are partial and 2 need review (the LiveBench cost basis and the SuperCLUE quadrant), and the partial set includes core formula claims (TokenCost blend, Model Price Watch blend, Klu best value).",
    "evidence_ids": ["validation/verify_claim_support.log", "387ac1f1", "b58443e5", "9d68b3a8"],
    "severity": "medium",
    "loopback": false,
    "proposed_fix": "Add two rows to Report Metadata: 'Claim support: 44 supported, 18 partial, 2 needs_review of 64' and 'Citations verified: 91 reachable'. List the 20 non-supported claims in Limitations, and fix wording on the TokenCost, Model Price Watch and Klu claims (check formula text against the page quote)."
  },
  {
    "cycle": 2,
    "delta_type": "presentation",
    "claim_id": "Report structure (report-assembly.md)",
    "description": "Limitations follows Recommendations (the assembly guide orders Limitations before Recommendations). Counterevidence Register and Claims-Evidence Table are extra but useful. Report file name is not the dated convention. The forward-looking sentence 'a ranking dated 2026-10-17 will be stale in months' is a forecast without hedge.",
    "evidence_ids": ["reference/report-assembly.md"],
    "severity": "low",
    "loopback": false,
    "proposed_fix": "Move Limitations and Gaps above Recommendations, or keep the order and note the departure in the Methodology Appendix. Change the forecast to 'may be stale within months, as the Epoch price-trend work suggests [70]'."
  }
]
```

---

## Stopping-rule verdict

The rule (`reference/adversarial-review.md`) is: stop when no `high` severity deltas remain or max cycles are reached. Both cycles are done, and five high-severity deltas remain.

**High-severity deltas remaining (all `loopback: true`):**

1. Cycle 1, C1 (A1 verdict is definition-dependent; RemakeBench and Klu are partial combinations).
2. Cycle 1, C1/C9 (discovered-but-unread sources; Copilot, Cursor and forum classes absent).
3. Cycle 1, X1/Table 3/Rec 1 (the 3.7x spread mixes consumed workload with allowance measurements).
4. Cycle 1, C20/C21/F8 (ValueRank's plan formula is not tested for the reasoning-token and token-mix problem the report raises against others; max-over-plans bias).
5. Cycle 2, Rec 4 versus Introduction/F8 (API basis defined as cost per task versus total cost; "does not count failures" wrong).

**DR-REFINE must loop back.** Items 3, 4 and 5 are edits to the existing analysis and need no new retrieval. Items 1 and 2 need either a bounded retrieval pass (the lead-scan pages, Copilot/Cursor/Gemini plans, one forum sweep, Chinese vendor coding plans) or an explicit narrowing of the A1 and A3 verdicts and the "examined" counts. If the refine budget does not allow retrieval, the documented blocker is: A1 stays a definition-dependent bounded negative over the registered 91 sources, and the "only site found" wording in the Executive Summary must carry that qualifier. Medium and low deltas can be handled in the same refine pass or recorded as residual risk in `decision-record.md`. Do not loop beyond one refine cycle without new retrieval.

---

## Refine disposition

DR-REFINE, 2026-10-17 (UTC). Delta ids below number the deltas in order within each cycle's JSON block (`C1-n` for cycle 1, `C2-n` for cycle 2). **fixed**: the report, claims or triangulation now carry the correction. **narrowed**: the evidence could not close the gap, so the claim was limited and the gap recorded. **blocked**: unresolvable from the store; none. Section names refer to `research_report.md` unless a file is named.

### Counts

| Severity | Deltas | Fixed | Narrowed | Blocked |
|---|---|---|---|---|
| High | 5 | 4 | 1 | 0 |
| Medium | 13 | 10 | 3 | 0 |
| Low | 6 | 6 | 0 | 0 |
| **Total** | **24** | **20** | **4** | **0** |

### Per-delta disposition

| Id | Sev | Disposition | What changed and where |
|---|---|---|---|
| C1-1 A1 depends on the meaning of "combine" | high | fixed | Definition of combine (quality measure, plan-derived cost, joined ranked figure) in Introduction; partial-combinations Table 5 in F11 naming RemakeBench ("There is no aggregate score", subscription charge recorded as zero, 58.8%-of-a-week figure for one model) and Klu (subscription-only model in a footnote); A1 row of Table 7; Executive Summary paragraph 3; Counterevidence Register; `triangulation.md` C1 re-graded from "PASS-AB for the AA boundary" to "BOUNDED-NEGATIVE, definition-dependent" and the AA statement labelled as AA's own scope only; `outline.md` item 5; claims section `partial_combinations`. |
| C1-2 Unread lead-scan pages; Copilot, Cursor and forum classes absent | high | narrowed | Second retrieval pass (S92 to S131) read ten of the fifteen named pages, Copilot and Cursor plan pages (F8), Chinese vendor plans (F8), three Hacker News items and two Reddit mirrors. Residual gaps stated in the A1 and A3 verdicts (Table 7), Limitations Table 9 and the Executive Summary: five lead-scan pages (discretestack, neura.market, aiven, yourgpt, llmleaderboard.in) and two Morph pages unread, no primary Gemini plan page, X not searched, Reddit only through mirrors. "About fifty sites" replaced by "131 sources under 99 publisher labels". |
| C1-3 3.7 times spread mixes consumption with allowance | high | fixed | F4 Table 3 holds the four allowance measurements (Wokey, Hacker News proxy, RemakeBench, SemiAnalysis): $1,751 to about $2,931 per week, 1.7 times, 35x to 59x monthly multiple; ml0x ($26,187 per month, consumed workload, 2.2 times SemiAnalysis, pre-13-September regime explains at most 1.5 times) is discussed separately; RemakeBench's "$2,136 to $2,174" shown to be rounding of 58%, and its single-account, plan-string-"Pro" caveats added; Table 3b lines up OpenAI figures by date; Executive Summary, Recommendation 1, Claims-Evidence Table, `triangulation.md` C10/X1/X2/X16 updated; claim 4d67d3f4 superseded. |
| C1-4 Plan formula not tested on the grounds applied to others | high | fixed | New F9 (workload dependence of the multiple with the direction of the bias and its Anthropic-only basis; highest-eligible-multiple selection bias; partly paywalled numerator; model-specific allowance; what follows; what the test does not show); Executive Summary names it the main decision risk; new Recommendation 2 (sensitivity test, eligibility rule, flag output-dominated models); `triangulation.md` C27; claims section `formula_test`. ValueRank's own plan-cost values are not in the corpus and were not recomputed (stated). |
| C1-5 SemiAnalysis cache statement over-generalised; S50 partial read | med | fixed | F4 Class 1 now says cache reads cost almost nothing "on some plans" and states the stored evidence is a tool summary of a partly paywalled page; Recommendation 3 limits the statement to Anthropic; `triangulation.md` C21 re-rated "PASS-AB, partial read"; claim c869804a superseded. |
| C1-6 "Most aggregators inherit AA" overstated | med | fixed | Count from Table 2: five of twelve (Klu, WhatLLM, Dervity cost; AI Model Comparison, Analytical Insider index); seven not documented as AA-derived. Executive Summary, F1, F2 (new "AA-derived" column), Synthesis "Dependence and correlation", Claims-Evidence Table ("Partly confirmed"), Counterevidence Register; `triangulation.md` C3 "PARTLY CONFIRMED". |
| C1-7 LiveBench cost basis rests on a file listing | med | narrowed | F1, F3, Table 6 ("A2 (file exists)"), Recommendation 4 and Limitations: a cost file exists; ValueRank ingests it under a field named for cost per successful task; no retrieved LiveBench text (S21, S131) says what it measures. `triangulation.md` X5 and C15 split into existence (resolved) and definition (open). Claim 845a1889 superseded. The definition could not be resolved from the store. |
| C1-8 SuperCLUE quadrant held less firmly in the register than in prose | low | fixed | F7 opens with the reporting newspaper (Jingji Cankao Bao via Eastmoney), records that the claim verifier scored the Chinese source 0.15, states the manual comparison with the quoted paragraph, and corrects the "top scores" wording to "task average scores differed by up to more than 70%"; Limitations claim-support paragraph; `triangulation.md` C16. Claim 1fb549f9 superseded; the replacement still scores needs_review because the checker is lexical and English-only (see below). |
| C1-9 A4 negative rests on one search log; Table 4 omits integrity markers | med | fixed | Table 4 rebuilt with counts over the twelve aggregators (dated nine, variant three, formula stated six, imputation policy two) and an uncertainty or integrity row (Terminal-Bench, Scale, BenchLM); Exec Summary and F5 phrase the evidence-class negative as three searches and one topic listing; BenchLM named as a partial analogue; "common among the better sites" withdrawn. The critique's proposed counts (6 dated, 5 variant) were recomputed from the register rather than adopted: they came from Table 4's illustrative list, not a tally. |
| C1-10 "Value leaders therefore differ by formula" overgeneralised | low | fixed | Executive Summary and F2 now say leaders can differ by formula (two sites compared) and describe Klu's best value as the lowest listed price; claim e9efe8ad superseded. |
| C1-11 Enterprise and open-weight pricing absent | med | narrowed | Limitations "Method limits" and F2 record that enterprise or negotiated pricing and the provider chosen for open-weight models were not compared; no new retrieval aimed at them. |
| C1-12 Non-English coverage thin | med | narrowed | F7 heading text and F8 add Chinese vendor coding plans (Zhipu, Alibaba, Kimi, DeepSeek, CodePick); A1 is stated as untested for Gemini and for European or Indian leaderboards; an India-focused leaderboard in the lead scan remains unread. |
| C1-13 Owners' reuse terms not reviewed | med | fixed | New F10 (AA terms of use, API attribution, WhatLLM note, LiveBench licence absence); the legal question and what the corpus does not say are stated; Recommendation 5 adds the confirmation step; `triangulation.md` C26 and X15; claims section `reuse_terms`. |
| C1-14 Reliance on internal documents; no inverse test | med | fixed | Every clause that uses AGENTS.md or the site audit is marked "(internal context)" (Introduction, F3, Recommendations 1, 3, 9, Limitations); F11 gains "Where ValueRank is weaker than the alternatives" (smaller roster, single upstream with unconfirmed terms, one secondary-reported numerator, no live refresh). |
| C1-15 Watch has no falsification criteria or archive policy | low | fixed | Recommendation 7 lists the three withdrawal triggers and the unread pages; Recommendation 6 adds archiving a date-stamped copy of each cited page at each refresh; Limitations records that no archives exist. |
| C2-1 Recommendation 4 contradicts the body | high | fixed | Recommendation 4 now reads: API basis is AA's total cost to run the Intelligence Index, a measured spend over all attempts, tokens spent on failed attempts included, not divided by the number of successes; "does not count failures" and the cost-per-task wording removed. F3 sentence on cost per task rewritten (a gap in the denominator, not a failure to count spend). `triangulation.md` C15. Claim 7d5f868a superseded. |
| C2-2 Bibliography lacks publisher, date, type | med | fixed | All 131 entries regenerated from `sources.jsonl` (`citation_manager.py assign-display-numbers` and `export-bibliography`, then post-processed) as publisher, date or "n.d.", linked title, source type, store grade, and flags for search-summary relays (S2, S3, S13, S14, S49, S66, S78, S79, S89, S99), unread pages (S11, S12, S28, S98) and title-only pages. Display numbers are registration order and unchanged for S1 to S91. The registry has no authors on any row. |
| C2-3 Counts disagree; wrong cite for AA total cost | low | fixed | Thirteen aggregators (twelve in Table 2 plus LM Market Cap); five of twelve AA-derived; 131 sources and 99 publisher labels replace "about fifty"; total-cost definition cited to [17] with [36]; Recommendation 5 count corrected. |
| C2-4 No rank-gap data behind Recommendation 1 | med | fixed | Comparison removed; replaced by an action for ValueRank to re-rank under the low and high multiples, marked internal context and "not a finding". |
| C2-5 Recommendation 8 "opening" claim; Recommendation 3 internal reference | med | fixed | Recommendation 9 restates the audience point as an untested hypothesis ("absent supply is not evidence of demand"); Recommendation 3 marks the planned example as internal context. |
| C2-6 Prose and register disagree on A4 | med | fixed | Same change as C1-9. |
| C2-7 Table 5 and 7 cells unevidenced; lumped grades | low | fixed | Table 8 (formerly 7) audience and funding cells keep only page-stated facts, otherwise "not stated"; Table 6 (formerly 5) splits Aider, Terminal-Bench, Vals, Klu, WhatLLM, Dervity, KickLLM, Analytical Insider and others into rows with one grade each; the grade column is defined as the best store grade. |
| C2-8 Metadata hides claim-support status | med | fixed | Report Metadata and Limitations state the counts (110 active claims: 62 supported, 43 partial, 5 needs review, 0 unsupported; 6 superseded) and the reason partial scores occur; hand comparisons recorded for the TokenCost, Model Price Watch, Klu and SuperCLUE claims. |
| C2-9 Section order; unhedged forecast | low | fixed | Limitations and Gaps now precedes Recommendations; the forecast reads "may be stale within months, as the Epoch price-trend work suggests". The dated file-name convention was not adopted (`research_report.md` is the name `run_manifest.json` registers). |

### Residual items

- Claim-support `needs_review` (5 active claims, all explained): the Alibaba Bailian plan claim and the SuperCLUE claim cite Chinese-language quotes, which the English lexical checker cannot match (the retrieval agent's English translations are in the evidence `claim` field and the SuperCLUE paragraph was compared by hand); the LiveBench README claim has no evidence row (source note only); the OpenAI date-trend claim and the "five of twelve" tally are multi-source analyst syntheses whose component claims are individually checked. No factual claim is unsupported.
- The ValueRank plan-cost values, eligibility rule and multiples used are not in the corpus, so the F9 findings are inferences about the formula and not statements about its published figures.
- Open legal question (F10): how ValueRank obtains and republishes AA data against AA's Terms of Use and Data Platform Terms. Not answered; not legal advice.
- Not read: Gemini primary plan pages, five lead-scan pages, two Morph pages, X posts, SemiAnalysis's paywalled section, AA's Data Platform Terms.
- `sources.jsonl` grades were not changed. RemakeBench's method page is graded B2 in the store; the report weighs it down for a single account, a single window and a "Pro" plan string.

### refresh_pass

Per `reference/refresh-protocol.md`, before this refine the following were re-verified from the store only (no re-fetch).

- **Entities.** Product and site names (Copilot, Cursor, Zhipu, Alibaba Bailian, Kimi, DeepSeek, RemakeBench, Wokey, Klu, BenchLM) were matched to the second-pass source rows S92 to S131; model names are reproduced as the pages state them. Analytical Insider's home page (S104) shows the site is a sales-lead service, which lowers the weight of the S33 article.
- **Numbers.** Sixty-one figures used in the new tables and text ($1,751, $2,155, $11,726, $1,949, $26,187, 14,973, 33.28, 96.4%, $1,249.83, 58%, $1,267.39 and 58.8%, $2,200, $650, $6.41, $6.70, 1,500, 7,000, 20,000, $0.01, 90,000, 468, 6,708, 694, 704 and others) were each found in an evidence quote, evidence claim or source note. Derived figures were recomputed: 11,726 divided by 4 or 4.33 gives 2,931 or 2,708; 2,931 divided by 1,751 is 1.67; 26,187 divided by 11,726 is 2.23; 1,249.83 divided by 0.575 and 0.585 gives 2,174 and 2,136; Copilot credits at $0.01 give $15, $70 and $200.
- **Hypotheses.** Single-source claims were re-listed in Limitations (Wokey ratio, RemakeBench allowance, forum measurements, Chinese plan quotas, SuperCLUE, LMArena, evidence-class absence, SemiAnalysis headline multiples, LiveBench file definition). Forecast language was hedged.
- **Store rows updated.** None.
