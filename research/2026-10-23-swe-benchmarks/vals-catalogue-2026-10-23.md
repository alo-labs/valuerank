# Vals AI benchmark catalogue and ValueRank fit (captured 2026-10-23)

Machine-readable catalogue: `vals-catalogue-2026-10-23.json`. Raw captures: `vals-capture/<slug>.json`, plus the pages (`_pages/`), model pages (`_models/`) and JS bundles (`_js/`). Coverage is counted over the 29 configurations in `cohort-2026-10-23.json`.

- **Exact (E):** the same model version at the same effort as AA.
- **Plausible (P):** AA shows no effort label and Vals ran the model in reasoning mode at null or max (MiMo-V2.6-Pro/Flash, MiniMax-M3.1-Flash), or the Vals record has no effort and AA's effort equals the effort Vals usually uses for that model.
- Results are never transferred across efforts or releases.

## Headline

- **Benchmarks:** Vals publishes 61 distinct benchmark pages: 37 active and 24 archived or superseded. 36 of the active ones are in the site's selector, which matches its "36 independent AI benchmarks"; the 37th is SAFE-Teen, shown as active on the index. `/benchmarks/snap` is an alias of `public-benefits-bench`. Every page and JSON was fetched (HTTP 200).
- **No JSON for two pages:** `rsi_index` and `mental-health` (SAFE-Teen) have no `benchmark_view` JSON. Their data were taken from JS bundles. SAFE-Teen has no single overall score.
- **One effort per model:** Vals runs each model at one effort, almost always the maximum (Gemini 4 Argon at high). Only two other efforts appear: Claude Opus/Sonnet 5.5 at high on archived Terminal-Bench 2.1, and Opus 5.5 at xhigh on VCB 1-100.
- **16 configurations are absent everywhere.** Of the 29 cohort configurations, 16 have no exact or plausible record on any Vals board: GPT-6 Luna low, medium, high and xhigh; GPT-6.1 Sol medium, high and xhigh; GPT-6 Astra high and xhigh; Claude Haiku 5.5 low, medium, high and xhigh; Claude Opus 5.5 medium; Claude Sonnet 5.5 xhigh; and GPT-5.6 Luna low. Claude Opus 5.5 high and xhigh each appear on one board only: Terminal-Bench 2.1 (archived) and VCB 1-100.
- **A ceiling of 11 ranked configurations.** Under O52, adding any current Vals board as a required leaf caps the ranked set at 11 of 29: 8 exact (Claude Haiku 5.5 max, Claude Opus 5.5 max, Claude Sonnet 5.5 max, DeepSeek V4.1 Flash 1017 max, Gemini 4 Argon high, GPT-6 Astra max, GPT-6 Luna max, GPT-6.1 Sol max) plus 3 plausible. Among non-composite boards, the ceiling is reached only on Vibe Code Bench v1.1, TB4, EMB v1.1, Finance Agent v2.1, Legal Research, HLAB-Vals-1.1 and Tax Agent Bench. Joint coverage falls quickly as boards are added:
  - VCB v1.1 + Code Migration v1.1: 8 exact + 2 plausible (no MiniMax).
  - Plus CyberBench or ProgramBench: 7 + 2 (no DeepSeek 1017).
  - Plus SWE-bench Multimodal instead: 7 + 1.
  - Plus VCB 1-100 instead: 3 exact.
- **Fallback qualifier.** The exact matches for Claude Opus/Sonnet 5.5 depend on reading AA's "max with fallback" as Vals' `compute_effort: max`. Vals has no fallback qualifier, and each record carries a note saying so. If the owner treats "with fallback" as a different configuration, those matches become plausible.

## All benchmarks by ValueRank relevance

Columns:
- **E/P:** exact and plausible counts over the 29 configurations.
- **Top:** the board's best overall score. A trailing `xN` means N models are tied at the top.
- **Arch:** archived or superseded.

| Relevance | Slug | Name | Ver | Updated | Arch | Models | Top | E | P |
|---|---|---|---|---|---|---|---|---|---|
| SWE/DevOps | `code-migration-v1-1` | Code Migration v1.1 | 1.1 | 2026-10-20 |  | 28 | 86.88 | 8 | 2 |
| SWE/DevOps | `terminal-bench-4` | Terminal-Bench 4.0 | 4.0 | 2026-10-22 |  | 54 | 65.15 | 8 | 3 |
| SWE/DevOps | `vibe-code` | Vibe Code Bench v1.1 | 1.1 | 2026-10-20 |  | 118 | 92.39 | 8 | 3 |
| SWE/DevOps | `cyber` | CyberBench v1.1 | 1.1 | 2026-10-12 |  | 47 | 80.36 | 7 | 2 |
| SWE/DevOps | `programbench` | ProgramBench | 1 | 2026-10-12 |  | 64 | 18.50 | 7 | 2 |
| SWE/DevOps | `swebench-multimodal` | SWE-bench Multimodal | 1 | 2026-10-16 |  | 20 | 70.21 | 7 | 1 |
| SWE/DevOps | `vcb-1-100` | Vibe Code Bench 1-100 | 1.0 | 2026-10-17 |  | 26 | 33.98 | 4 | 0 |
| SWE/DevOps | `skillsbench` | SkillsBench | 1 | 2026-09-27 |  | 35 | 69.80 | 0 | 0 |
| SWE/DevOps | `code-migration` | Code Migration | 1 | 2026-10-18 | yes | 79 | 69.83 | 8 | 2 |
| SWE/DevOps | `terminal-bench-2-1` | Terminal-Bench 2.1 | 2.1 | 2026-09-28 | yes | 76 | 87.64 | 3 | 2 |
| SWE/DevOps | `swebench` | SWE-bench | 1 | 2026-09-01 | yes | 88 | 97.00 | 0 | 0 |
| SWE/DevOps | `terminal-bench` | Terminal-Bench 1.0 | 1.0 | 2026-01-12 | yes | 47 | 63.75 | 0 | 0 |
| SWE/DevOps | `terminal-bench-2` | Terminal-Bench 2.0 | 2.0 | 2026-06-04 | yes | 67 | 73.20 | 0 | 0 |
| general professional work | `emb-v1-1` | EMB v1.1 | 1.1 | 2026-10-20 |  | 32 | 76.73 | 8 | 3 |
| general professional work | `fabv2-1` | Finance Agent v2.1 | 2.1 | 2026-10-22 |  | 30 | 67.85 | 8 | 3 |
| general professional work | `hlab` | HLAB-Vals-1.1 | 1.1 | 2026-10-22 |  | 27 | 27.08 | 8 | 3 |
| general professional work | `legal_research` | Legal Research Bench | 1 | 2026-10-22 |  | 84 | 55.29 x3 | 8 | 3 |
| general professional work | `tax_agent_bench` | Tax Agent Bench | 1 | 2026-10-20 |  | 75 | 49.66 | 8 | 3 |
| general professional work | `medcode` | MedCode | 1 | 2026-10-13 |  | 107 | 63.57 | 7 | 2 |
| general professional work | `medscribe` | MedScribe | 1 | 2026-10-13 |  | 109 | 91.43 | 7 | 2 |
| general professional work | `sage` | SAGE | 1 | 2026-10-08 |  | 91 | 56.10 | 7 | 2 |
| general professional work | `public-benefits-bench` | Public Benefits Bench v1.1 | 1.1 | 2026-10-12 |  | 50 | 76.93 | 6 | 2 |
| general professional work | `legal_bench` | LegalBench | 1 | 2026-10-13 |  | 151 | 88.56 | 1 | 0 |
| general professional work | `emb` | EMB | 1 | 2026-10-20 | yes | 77 | 76.67 | 8 | 2 |
| general professional work | `fabv2` | Finance Agent (v2) | 2 | 2026-10-20 | yes | 81 | 65.40 | 8 | 2 |
| general professional work | `hlab-v1` | Harvey's Legal Agent Benchmark v1 | 1 | 2026-10-18 | yes | 81 | 25.42 | 8 | 2 |
| general professional work | `case_law_v2` | CaseLaw v2 | 2 | 2026-05-04 | yes | 54 | 79.31 | 0 | 0 |
| general professional work | `finance_agent` | Finance Agent v1.1 | 1.1 | 2026-06-04 | yes | 51 | 64.37 | 0 | 0 |
| general professional work | `public-benefits-bench-v1` | Public Benefits Bench v1 | 1 | 2026-06-09 | yes | 13 | 71.65 | 0 | 0 |
| general professional work | `tax_eval_v2` | TaxEval v2 | 2 | 2026-09-01 | yes | 145 | 80.38 | 0 | 0 |
| reliability/hallucination | `claimbench` | ClaimBench | 1 | 2026-10-20 |  | 23 | 100.00 x5 | 5 | 0 |
| long context | `corp_fin_v2` | CorpFin v2 | 2 | 2026-08-12 | yes | 134 | 73.19 | 0 | 0 |
| science/knowledge | `biomysterybench` | BioMysteryBench | 1 | 2026-10-20 |  | 28 | 81.11 | 7 | 1 |
| science/knowledge | `ioi` | IOI | 2 | 2026-10-20 |  | 45 | 100.00 x2 | 7 | 2 |
| science/knowledge | `mysterymechanism` | MysteryMechanism | 1 | 2026-10-20 |  | 28 | 53.15 | 7 | 2 |
| science/knowledge | `proof_bench` | ProofBench v1.1 | 1.1 | 2026-10-20 |  | 53 | 100.00 x4 | 7 | 2 |
| science/knowledge | `terminal-bench-science` | Terminal-Bench-Science | 0.1 | 2026-10-21 |  | 42 | 62.86 | 7 | 2 |
| science/knowledge | `aime` | AIME | 1 | 2026-04-16 | yes | 96 | 98.12 | 0 | 0 |
| science/knowledge | `gpqa` | GPQA Diamond | 1 | 2026-09-01 | yes | 138 | 95.45 | 0 | 0 |
| science/knowledge | `ioi-v1` | IOI v1 | 1 | 2026-08-09 | yes | 62 | 91.67 | 0 | 0 |
| science/knowledge | `lcb` | LiveCodeBench | 1 | 2026-09-01 | yes | 143 | 90.52 | 0 | 0 |
| science/knowledge | `math500` | MATH 500 | 1 | 2026-01-09 | yes | 60 | 96.40 | 0 | 0 |
| science/knowledge | `medqa` | MedQA | 1 | 2026-04-16 | yes | 95 | 96.52 | 0 | 0 |
| science/knowledge | `mgsm` | MGSM | 1 | 2026-01-09 | yes | 75 | 95.20 | 0 | 0 |
| science/knowledge | `mmlu_pro` | MMLU Pro | 1 | 2026-09-01 | yes | 138 | 92.38 | 0 | 0 |
| science/knowledge | `mmmu` | MMMU Pro | 1 | 2026-09-01 | yes | 93 | 90.64 | 0 | 0 |
| not relevant | `finance_index` | Vals Finance Index | 1 | 2026-10-22 |  | 30 | 65.59 | 8 | 3 |
| not relevant | `vals_index` | Vals Index | 2.2 | 2026-10-22 |  | 26 | 70.85 | 8 | 3 |
| not relevant | `science_index` | Vals Science Index | 1.0 | 2026-10-21 |  | 22 | 65.09 | 7 | 1 |
| not relevant | `srebench` | SRE Bench | 1 | 2026-10-14 |  | 35 | 56.87 | 7 | 2 |
| not relevant | `robo_bench` | Robo-bench | 1 | 2026-10-13 |  | 7 | 28.33 | 4 | 0 |
| not relevant | `rsi_index` | Vals RSI Index | 1.1 | 2026-10-15 |  | 25 | 37.31 | 4 | 0 |
| not relevant | `cua_bench` | CUA-bench | 1 | 2026-10-13 |  | 9 | 19.17 | 3 | 0 |
| not relevant | `time_horizon_index` | Time Horizon Index: KSP | 1 | 2026-10-07 |  | 13 | 91.33 | 3 | 0 |
| not relevant | `mental-health` | SAFE-Teen | n/s | 2026-10-13 |  | 17 | n/a | 0 | 5 |
| not relevant | `poker_agent` | Agent Poker Bench | 1 | 2025-12-23 |  | 17 | 1131.83 | 0 | 0 |
| not relevant | `vals_router_index` | Vals Router Index | 1.0 | 2026-10-20 |  | 27 | 69.24 | 0 | 11 |
| not relevant | `voice-code-bench` | VoiceCodeBench | 1 | 2026-09-24 |  | 20 | 67.67 | 0 | 0 |
| not relevant | `web_search` | Vals Web Search Index | 1 | 2026-10-21 |  | 9 | 49.08 | 0 | 0 |
| not relevant | `mortgage_tax` | MortgageTax | 1 | 2026-09-01 | yes | 98 | 72.06 | 0 | 0 |
| not relevant | `vals_multimodal_index` | Vals Multimodal Index | 1.2 | 2026-08-11 | yes | 33 | 74.15 | 0 | 0 |

No Vals board measures instruction following, so that category has no rows. The only long-context board, CorpFin v2, is archived as saturated and covers no cohort model.

## Recommendation for ValueRank

### Decisive constraint (O52)
Vals publishes one effort per model, so every Vals board is structurally missing the lower-effort GPT and Claude rows. Making any Vals board a required leaf would cut the ranked set to at most 11 of 29 configurations, and 3 of those 11 would rest on a plausible match rather than an exact one. Vals' boards therefore cannot be balanced against configurations ranked under O52 unless one of two things happens:
- the owner accepts dropping the 16 to 18 lower-effort rows from the ranking; or
- Vals runs those efforts.

Asking Vals to run them is an open route: each Vals model page states the effort it used, which suggests it chooses a single effort per model deliberately.

**Recommendation:** do not make any Vals board a required ranked leaf now. Keep the strongest boards as candidates and as indicative values (O41-style) for the max-effort rows.

### SWE/DevOps candidates (in order)
1. **Vibe Code Bench v1.1 (`vibe-code`)**: 8 exact + 3 plausible, the coverage ceiling.
   - For: private and fresh; the same OpenHands harness for every model row; 118 models; the closest Vals board to end-to-end application building.
   - Against: a compressed top (cohort range 73.9-92.4) and an unpublished task count.
   - This is the best single Vals SWE candidate.
2. **Code Migration v1.1 (`code-migration-v1-1`)**: 8 exact + 2 plausible (no MiniMax-M3.1-Flash).
   - For: private; a uniform Pi harness; a wide spread (cohort 39.6-86.9); realistic porting and re-implementation work.
   - Together with VCB v1.1 it keeps 8 exact + 2 plausible jointly.
   - v1 (`code-migration`) is superseded; do not mix the two versions.
3. **CyberBench v1.1 (`cyber`)**: 7 exact + 2 plausible (no DeepSeek V4.1 Flash 1017, no MiniMax).
   - Reproducing and patching OSS-Fuzz crashes is genuine engineering work, but narrow (memory safety in native code).
   - A secondary option.
4. **SWE-bench Multimodal (`swebench-multimodal`)**: 7 exact + 1 plausible.
   - Real issue resolution in front-end repositories, but public (contamination risk), a single run, and 20 models.
   - A secondary option.
5. **Vibe Code Bench 1-100 (`vcb-1-100`)**: a strong long-horizon maintenance design, but only 4 exact matches (Opus 5.5 at xhigh only, no GPT-6.1 Sol or Luna). Watch it for coverage growth.

### Not recommended as new SWE leaves
- **Terminal-Bench 4.0 (`terminal-bench-4`):** the same task set as ValueRank's existing AA-run Terminal-Bench 4.0 leaf.
  - At most it could act as a lower-priority gap-filler for max-effort rows under the leaf's source order (another party ran the same version on the exact configuration).
  - Its harness differs (Mini-SWE-agent, avg@3), so mixing sources inside the leaf adds harness variance.
  - Vals documented MiMo-V2.6-Flash exploiting git history on one TB4 task (vals.ai/blogs/mimo-reward-hacking).
- **ProgramBench:** at the floor (top 18.5%).
- **SkillsBench:** has no cohort model at all, only the unsuffixed DeepSeek V4.1 Flash; stale.
- **SWE-bench Verified, LiveCodeBench, Terminal-Bench 1.0/2.0/2.1:** archived or saturated, with no post-August cohort model (TB2.1 has a few).
- **IOI v2:** algorithmic and at the ceiling.
- **SRE Bench:** binary reverse engineering, not site reliability or DevOps.

### Other relevance groups
- **General professional work:** Finance Agent v2.1, EMB v1.1, Legal Research Bench, HLAB-Vals-1.1 and Tax Agent Bench each reach the 8 exact + 3 plausible ceiling.
  - They are agentic, private professional-work boards that overlap ValueRank's existing general-professional leaves (GDPval-AA, AA-Briefcase, AutomationBench-AA).
  - They add no configuration coverage. Consider them only if the owner wants to broaden that 20% leaf, and only under the same 11-configuration ceiling.
  - MedCode, MedScribe, SAGE, LegalBench and Public Benefits Bench are domain-specific or short-form; not recommended.
- **Reliability/hallucination:** ClaimBench verifies claims against 10-K filings.
  - It is saturated (5 systems at 100%), aimed at small decision models, and has only 5 exact matches.
  - It is no substitute for AA-Omniscience.
- **Long context:** CorpFin v2 is archived (saturated) and covers no cohort model; AA-LCR stays the leaf.
- **Instruction following:** Vals has no board in this category.
- **Science/knowledge:** none recommended.
  - BioMysteryBench, MysteryMechanism, Terminal-Bench-Science and ProofBench v1.1 (top score 100) are science boards, outside SWE scope; ValueRank's science leaf already holds SciCode and HLE-type evaluations.
  - GPQA, MMLU-Pro, MMMU, AIME, MATH 500, MGSM and MedQA are archived as saturated.
- **Not relevant:**
  - Composites, which would double-count their components: Vals Index v2.2, Finance, Science, RSI, Router, Web Search and Multimodal indexes.
  - Game, robotics and voice boards: CUA-bench, Time Horizon KSP, Poker Agent, Robo-bench, VoiceCodeBench. CUA-bench and Robo-bench also run each model in its vendor's own agent, so their harness is not uniform.
  - SAFE-Teen (teen safety; no single score; no effort recorded).

### Capture gaps
- Task counts are not stated in the page text for Vibe Code Bench v1.1, SkillsBench, LegalBench, HLAB v1, MedQA, MGSM, SAGE, BioMysteryBench and IOI v1. Those entries say so.
- Vals publishes no per-model run date, only each board's `updated` date.
- The `-range` keys are labelled "Claude Opus 5.5 (CVP)" and "Claude Sonnet 5 (Cyber Range)". They are access variants and are not mapped.
