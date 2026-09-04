# ValueRank Periodic Ranking Refresh: DeepSWE v1.1 and Artificial Analysis v4.1.1

## Executive Summary

This refresh answers: what is the most current, source-backed ValueRank ranking of frontier models when the current DeepSWE Best roster is the cohort gate and benchmark coverage is maximized without mixing incompatible versions or filling missing cells?

The answer is a 21-model ranking observed on 2026-09-04 UTC. The live DeepSWE v1.1 page reports 113 tasks, a 21-of-28 model view, and an update date of September 3, 2026 [1]. Its current roster adds GPT-6 Astra and Gemini 3.8 Flash near the top, with recent reruns and pricing corrections recorded in the official changelog [2]. DeepSWE's public methodology identifies the mini-swe-agent harness, 91 repositories, five languages, original tasks, and behavioral verifiers [3].

Artificial Analysis has changed the identity of its comparable index since ValueRank v1.3.1. The current v4.1.1 definition uses GDPval-AA v2, tau3 Banking, Terminal-Bench v2.1, SciCode, AA-LCR, HLE, GPQA Diamond, CritPt, and split Omniscience accuracy/non-hallucination components [4]. The v4.1 release changed GDPval, Terminal-Bench, and tau benchmark definitions, while removing saturated IFBench [5]; v4.1.1 subsequently changed grading for HLE, AA-LCR, and Omniscience [6]. Therefore, old v1.3.1 scores are historical and not numerically comparable.

All 21 models have current values for the ten AA component fields, AA Intelligence Index, and AA total evaluation cost. Speed is the only candidate field with an honest gap: the selected GPT-6 Astra xhigh page reports N/A [17]. ValueRank retains the full 21-model cohort, drops Speed from the primary score, preserves the null and 20-of-21 coverage in the audit matrix, and uses 13 zero-gap dimensions. No neutral, median, family, legacy-version, or silently substituted values are used.

The resulting top five are Gemini 3.8 Flash, GLM-5.3 Flash, GPT-5.6 Sol, GPT-6 Astra, and Grok 4.6. The result reflects a deliberate production-value tradeoff: Cost is a normalized composite of AA total evaluation cost and DeepSWE average cost, while Quality Score removes Cost so capability remains visible separately.

## Introduction

ValueRank is a rank-normalized synthesis for production model selection, not a new benchmark. The refresh has three constraints: use the newest defensible model roster, maximize comparable benchmark data, and keep evidence provenance strong enough that a later refresh can reproduce or challenge every decision.

The product cohort is DeepSWE Best because that is the existing ValueRank inclusion rule. Artificial Analysis is used as the cross-model measurement layer because it publishes a current, multi-evaluation index and model-page payloads. Benchmark-owner materials are used to interpret definitions and version changes, not to splice incompatible leaderboard numbers into the AA matrix. Terminal-Bench's official release says v2.1 contains 89 tasks and corrected 28 of 89 tasks [7]; its repository specifies five trials for leaderboard submissions [8]. These facts matter for interpretation, but the published ValueRank component remains the AA v4.1.1 measurement for comparability.

## Main Analysis

### 1. The current DeepSWE roster is materially broader and fresher

The current page exposes 21 Best rows from 28 model configurations, compared with the 18-model DeepSWE roster used by the previous ValueRank snapshot. The observed table has 113 tasks and is dated September 3, 2026 [1]. The changelog provides a release-aware explanation for the shift: GPT-6 Astra was added September 3, Gemini 3.8 Flash September 1, and several prior models were rerun after token-count or pricing corrections [2].

The extraction preserves each displayed effort, pass@1, uncertainty, average cost, output-token count, and agent-step count. The three highest DeepSWE rows are GPT-6 Astra at 74% plus or minus 3% and 6.52 dollars average cost, Gemini 3.8 Flash at 74% plus or minus 1% and 2.36 dollars, and Claude Opus 5 at 74% plus or minus 4% and 11.84 dollars. This is a current leaderboard observation, not a claim that the models are statistically ordered within the overlapping uncertainty intervals.

### 2. AA v4.1.1 is a benchmark-identity migration, not a simple data append

The Artificial Analysis methodology page identifies the current Intelligence Index as v4.1.1 and lists nine evaluations [4]. Its component weights are 20% GDPval-AA v2, 14% tau3 Banking, 16% Terminal-Bench v2.1, 8% SciCode, 6% AA-LCR, 12% HLE, 6% GPQA Diamond, 6% CritPt, 8% Omniscience Accuracy, and 4% Omniscience Non-Hallucination. The last two are one source evaluation split into two measurable components.

The version transition is consequential. AA's v4.1 announcement upgrades GDPval to v2, Terminal-Bench Hard to v2.1, tau2 Telecom to tau3 Banking, and removes IFBench after saturation [5]. The v4.1.1 note records grading changes for HLE, AA-LCR, and Omniscience [6]. Mixing v1.3.1's legacy IFBench, Terminal-Bench Hard, or tau2 Telecom with the new fields would make the apparent coverage larger while making the score less interpretable. The refresh therefore carries forward the current definitions only and documents legacy dimensions as excluded by version.

### 3. The current component matrix is complete across the 21-model cohort

The first-party AA pages were scraped using effort-specific URL candidates and decoded from the page's currentModel payload. This matters because visible label scraping can misread a version token such as v2.1 as a score. The new extractor reads the structured model object, captures the raw fractions, records the selected URL and variant, and keeps supplemental fields separate.

The resulting coverage is 21 of 21 for GDPval-AA v2, tau3 Banking, Terminal-Bench v2.1, SciCode, AA-LCR, HLE, GPQA Diamond, CritPt, Omniscience Accuracy, Omniscience Non-Hallucination, AA Intelligence Index, and AA total evaluation cost [4]. Representative payload checks show GPT-6 Astra xhigh at Intelligence Index 60.9931 and AA evaluation cost 2004.1186 dollars [17], Gemini 3.8 Flash high at 58.6792 and 825.8333 dollars [18], and Claude Opus 5 max at 63.0532 and 3836.0545 dollars [19]. The complete machine-readable matrix, rather than a hand-copied table, is the score input.

### 4. The maximum defensible model count is 21, with Speed explicitly supplemental

The selected GPT-6 Astra xhigh AA page reports Speed N/A [17]. The other 20 selected pages expose numeric speed. Retaining Speed as a primary dimension would either exclude GPT-6 Astra, violating the current DeepSWE cohort goal, or require an imputation, violating the zero-gap rule. The chosen decision keeps all 21 models, drops Speed from the primary score, and preserves the missing field and its exact reason in coverage_matrix.json.

This is a narrower primary score but a broader product cohort. It also avoids giving a false impression that the current AA page measured a speed value for GPT-6 Astra. Speed remains available for a separate 20-model speed-versus-quality visualization, with N/A shown as a coverage fact rather than converted into a rank.

### 5. The ValueRank composite separates production cost from capability

For each model, AA Intelligence Index total evaluation cost and DeepSWE average cost per task are each normalized against the highest current cohort value. Their average is the raw Cost composite; lower is better and is then rank-normalized. This retains both source quantities instead of treating either a benchmark-evaluation cost or a single model price as the complete operational cost story.

The AA data API documents benchmark, pricing, performance, and time-series routes [20]. No API key is stored or required for this refresh: public first-party page payloads are captured locally, and the extraction path is recorded. The cost output contains the two normalized components, the composite, and the score dimension so a future refresh can detect a changed cost definition.

### 6. Supplemental fields increase future research capacity without contaminating the current score

The AA pages also expose partial fields including MLCR, Harvey, APEX-Agents, MMMU-Pro, AnalystAgent, AutomationBench, EnterpriseOpsGym, ITBench SRE, and Briefcase. The coverage matrix records availability, missing model names, and role for each field. Incomplete supplemental values are not converted into score dimensions. This is the correct place to maximize collected data: preserve it for a future cohort or specialized view while keeping the current primary ranking comparable.

Independent owner sources confirm why these fields need careful interpretation. The tau owner leaderboard publishes its own banking and knowledge results [9], while the Sierra repository documents the original task/harness lineage [10]. The HLE owner leaderboard is a separate benchmark-owner view [11]; SciCode's repository identifies a scientific coding evaluation project [12]; the GPQA paper establishes the graduate-level scientific reasoning task family [13]; AA-LCR describes a 100-question, seven-document-type long-context evaluation [14]; and the GDPval paper provides the realistic knowledge-work provenance [15]. These sources triangulate definitions and provenance but do not replace AA's current cross-cohort values.

## Synthesis

The refresh produces a ranking that is current in two different senses: the model roster is live and the AA benchmark identity is current. The most important synthesis insight is that coverage expansion is not synonymous with quality. A larger table can be less rigorous if it combines legacy and current definitions or fills a missing cell. The 21-model, 13-dimension result maximizes the current complete cohort while making the sole dropped field visible.

The current overall leader is Gemini 3.8 Flash at 69.4, followed by GLM-5.3 Flash at 65.6, GPT-5.6 Sol at 61.3, GPT-6 Astra at 61.0, and Grok 4.6 at 60.8. GPT-6 Astra's DeepSWE result is tied at the top, but its AA speed gap is excluded rather than hidden. Claude Opus 5 leads the quality-oriented part of the cohort more strongly than its overall position because its cost penalty is high. These are rank-relative observations, not absolute claims of model quality.

The main product recommendation is to publish v1.4.0 with the 21-model cohort, 13 zero-gap dimensions, AA+DeepSWE Cost, and a visible supplemental coverage appendix. Future refreshes should repeat the same sequence: freeze the current DeepSWE roster, record benchmark identity/version, resolve model variants, build coverage before scoring, preserve nulls, and only then regenerate the publication.

## Limitations

- DeepSWE and Artificial Analysis use different tasks, harnesses, sampling, and cost accounting; the synthesis is decision support, not a unified benchmark.
- Rank normalization preserves ordering but discards magnitude. A one-point rank difference and a large raw-score difference can receive the same adjacent spacing.
- DeepSWE uncertainty intervals overlap for several leading models. The ranking should not be read as a definitive significance test.
- AA model pages can expose multiple reasoning efforts and default redirects. The selected URL, model slug, and effort are recorded for every row.
- Speed is available for 20 of 21 models and is intentionally coverage-only in v1.4.0.
- Supplemental fields are not all comparable across the cohort and therefore remain outside the primary score.
- Web pages are time-sensitive. The values in this report are an observed 2026-09-04 snapshot and should be refreshed before reuse.

## Recommendations

1. Publish the generated v1.4.0 root docs and site from the 21-model, 13-dimension zero-gap score.
2. Keep the selected AA page URL and currentModel extraction snapshot alongside the machine-readable matrix so variant drift is detectable.
3. Keep Speed and all partial supplemental fields in the coverage appendix; add them to a primary score only after a future cohort has complete, definition-compatible coverage.
4. Treat v1.3.1 and v1.4.0 as separate benchmark-version snapshots; do not chart them as a continuous score series without an explicit bridge study.
5. On the next periodic refresh, rerun the search-cli probe and record the actual provider route; this run used the available structured retrieval and first-party pages because the executable did not resolve on the host.

## Counterevidence Register

| Potential challenge | Evidence and resolution |
|---|---|
| A source leaderboard may rank models differently from AA. | Owner leaderboards such as tau are separate measurement surfaces [9]; AA is retained as the comparable cross-cohort source, not treated as universally authoritative. |
| GPT-6 Astra could be excluded because Speed is missing. | The user goal prioritizes the current DeepSWE roster; the page reports Speed N/A [17], so Speed is dropped and the model retained with a visible null. |
| Old dimensions could increase the number of score columns. | AA v4.1 explicitly changes benchmark identities [5]; legacy dimensions are not mixed into v1.4.0. |
| The API could provide a more direct data route. | The API documentation is recorded [20], but no key is available in the repository; public first-party page payloads are sufficient and auditable for this snapshot. |

## Claims-Evidence Table

| Claim | Evidence ids | Status |
|---|---|---|
| The current DeepSWE page has 113 tasks, 21 visible Best models, and a September 3, 2026 update. | E1 | supported |
| DeepSWE adds GPT-6 Astra and Gemini 3.8 Flash in the current changelog window. | E3 | supported |
| AA v4.1.1 defines the current nine-evaluation index and ten split components. | E5, E6 | supported |
| AA v4.1 changed GDPval, Terminal-Bench, and tau benchmark identities. | E7 | supported |
| All current primary AA fields except numeric Speed have 21-of-21 coverage. | E26, E27 | supported |
| GPT-6 Astra's selected AA page reports Speed N/A. | E23 | supported |
| The v1.4 score retains 21 models and 13 zero-gap dimensions with no neutral fills. | E29 | supported |
| The current top five are Gemini 3.8 Flash, GLM-5.3 Flash, GPT-5.6 Sol, GPT-6 Astra, and Grok 4.6. | E30 | supported |
| Cost averages normalized AA evaluation cost and normalized DeepSWE average cost. | E31 | supported |

## Bibliography

[1] DeepSWE Best leaderboard. https://deepswe.datacurve.ai/
[2] DeepSWE changelog. https://deepswe.datacurve.ai/changelog/
[3] DeepSWE technical overview. https://deepswe.datacurve.ai/blog/deepswe/
[4] Artificial Analysis Intelligence Index methodology. https://artificialanalysis.ai/methodology/intelligence-benchmarking/
[5] Artificial Analysis Intelligence Index v4.1. https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-1/
[6] Artificial Analysis Intelligence Index v4.1.1. https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-1-1/
[7] Terminal-Bench 2.1 release. https://www.tbench.ai/news/terminal-bench-2-1/
[8] Terminal-Bench 2.1 official repository. https://github.com/harbor-framework/terminal-bench-2-1/
[9] tau benchmark leaderboard. https://taubench.com/leaderboard/
[10] Sierra tau benchmark repository. https://github.com/sierra-research/tau2-bench/
[11] Humanity's Last Exam owner leaderboard. https://labs.scale.com/leaderboard/humanitys_last_exam
[12] SciCode official repository. https://github.com/scicode-bench/SciCode/
[13] GPQA paper. https://arxiv.org/abs/2311.12022
[14] AA-LCR announcement. https://artificialanalysis.ai/articles/announcing-aa-lcr/
[15] GDPval paper. https://arxiv.org/abs/2510.04374
[16] Artificial Analysis model directory. https://artificialanalysis.ai/models/
[17] Artificial Analysis GPT-6 Astra xhigh. https://artificialanalysis.ai/models/gpt-6-astra-xhigh/
[18] Artificial Analysis Gemini 3.8 Flash high. https://artificialanalysis.ai/models/gemini-3-8-flash/
[19] Artificial Analysis Claude Opus 5 max. https://artificialanalysis.ai/models/claude-opus-5/
[20] Artificial Analysis data API documentation. https://artificialanalysis.ai/data-api/docs/

## Methodology

The refresh followed the Silver-Bullet Deep Research sequence: scope the decision, plan first-party retrieval lanes, retrieve source pages and local snapshots, triangulate benchmark-version claims, outline findings, synthesize, run three critique-oriented checks, and package a decision record and handoff. The implementation sequence then decoded current AA payloads, built the coverage matrix, applied the zero-gap score gate, generated docs/site, and ran static/JSON/research validation.

The full machine-readable source registry is in sources.jsonl. Atomic evidence is in evidence.jsonl. The reproducible extraction/scoring scripts and JSON outputs are under .refresh/v1.4. The final score uses rank normalization with exact-tie averaging, AA+DeepSWE cost normalization, and weights recorded in scores.json.

## Report Metadata

- Workflow: WF-SILVER-DEEP-RESEARCH
- Atomic flow: AF-DECIDE
- Flow step: FS-SILVER_DEEP_RESEARCH
- Mode: ultradeep
- Research type: default
- Observed date: 2026-09-04 UTC
- Repository commit at source baseline: a2edc36d8451cdeef253eebacbc4202b2b3c1a06
- Publication output: ValueRank v1.4.0
- Search route: host search/search-cli probe unresolved; structured context-mode search and first-party web retrieval used and recorded in run_manifest.json
