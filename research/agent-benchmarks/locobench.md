# LoCoBench Executive Summary for ValueRank

**Date:** 2026-06-20
**Benchmark:** LoCoBench — Long-Context LLM Evaluation in Complex Software Engineering
**Source:** arXiv:2509.09614 (Salesforce AI Research, Sep 2025)
**Data downloaded:** 250MB zip from Google Drive → 8,000 evaluation scenarios + 1,000 synthetic codebases across 10 languages

---

## Critical Finding: Zero Overlap with ValueRank's 13 Models

**None of ValueRank's 13 models were tested in LoCoBench.** The paper evaluated 13 *older-generation* models (GPT-4o, GPT-4.1, GPT-5, o3, o4-mini, Claude Sonnet 3.7, Claude Sonnet 4, Gemini 2.5 Pro/Flash). All pre-date the models in ValueRank's current lineup.

**The downloaded data.zip contains evaluation inputs (scenarios, codebases, test suites), not model results.** Results exist only as published numbers in the arXiv paper.

## Closest Model Approximations

| ValueRank Model | Best LoCoBench Proxy | Generational Gap | Confidence |
|---|---|---|---|
| Gemini 3.1 Pro (#1) | Gemini-2.5-Pro | ~1 gen behind | ⚠️ Directional |
| GPT-5.5 (#2) | GPT-5 | ~0.5 gen behind | ⚠️ Directional |
| MiMo-V2.5-Pro (#3) | — | No proxy | ❌ No data |
| MiniMax M3 (#4) | — | No proxy | ❌ No data |
| GPT-5.4 (#5) | GPT-5 | ~0.5 gen behind | ⚠️ Directional |
| Kimi K2.6 (#6) | — | No proxy | ❌ No data |
| Claude Opus 4.8 (#7) | claudesonnet4 | Different tier (Sonnet vs Opus) + gen | ⚠️ Weak |
| Gemini 3.5 Flash (#8) | Gemini-2.5-Flash | ~1 gen behind | ⚠️ Directional |
| DeepSeek V4-Pro (#9) | — | No proxy | ❌ No data |
| GLM 5.1 (#10) | — | No proxy | ❌ No data |
| Claude Opus 4.7 (#11) | claudesonnet3.7 | Different tier + gen | ⚠️ Weak |
| GPT-5.4 Mini (#12) | gpt5mini | ~0.5 gen behind | ⚠️ Directional |
| Claude Sonnet 4.6 (#13) | claudesonnet4 | ~0.5 gen behind | ⚠️ Directional |

**Bottom line:** Only 7 of 13 ValueRank models even have a rough proxy. The other 6 (MiMo, MiniMax, Kimi, DeepSeek, GLM) have zero data because LoCoBench tested only OpenAI, Anthropic, Google, and Meta models.

---

## Full LoCoBench Leaderboard (13 Models, LCBS 0–5 Scale)

### Overall Rankings (Table 7a)

| Rank | Model | LCBS | Success Rate | SE Overall | Func. Overall | **Quality Overall** | LC Overall |
|---|---|---|---|---|---|---|---|
| 1 | Gemini-2.5-Pro | 2.312 | 99.88% | 0.375 | 0.356 | **0.768** | 0.523 |
| 2 | Gemini-2.5-Flash | 2.307 | 99.98% | 0.373 | 0.358 | **0.741** | 0.565 |
| 3 | GPT-5 Mini | 2.293 | 100.00% | 0.376 | 0.371 | **0.745** | 0.479 |
| 4 | Claude Sonnet 4 | 2.288 | 99.56% | 0.379 | 0.348 | **0.762** | 0.492 |
| 5 | GPT-5 | 2.286 | 100.00% | 0.367 | 0.383 | **0.732** | 0.492 |
| 6 | Claude 3.7 Sonnet | 2.285 | 99.79% | 0.377 | 0.347 | **0.773** | 0.477 |
| 7 | GPT-4.1 Mini | 2.222 | 100.00% | 0.359 | 0.365 | **0.739** | 0.435 |
| 8 | o3-mini | 2.215 | 100.00% | 0.355 | 0.368 | **0.726** | 0.455 |
| 9 | GPT-4.1 | 2.197 | 100.00% | 0.352 | 0.364 | **0.720** | 0.451 |
| 10 | o3 | 2.154 | 100.00% | 0.342 | 0.385 | **0.722** | 0.343 |
| 11 | o4-mini | 2.148 | 99.70% | 0.353 | 0.360 | **0.705** | 0.394 |
| 12 | GPT-4o Mini | 2.075 | 100.00% | 0.341 | 0.360 | **0.680** | 0.345 |
| 13 | GPT-4o | 2.073 | 100.00% | 0.339 | 0.362 | **0.678** | 0.349 |

### Code Quality Assessment (20% of LCBS — 3 sub-metrics)

The **Quality Overall** column above is the score most relevant to ValueRank's code quality dimension. It aggregates:

1. **Security Analysis Score** — vulnerability detection in generated code
2. **Average Issues Found** (inverted) — fewer issues = higher score
3. **Code Style Adherence** — naming conventions, formatting, documentation

| Rank | Model | Quality Overall | Best among |
|---|---|---|---|
| 1 | Claude 3.7 Sonnet | **0.773** | Quality champion |
| 2 | Gemini-2.5-Pro | **0.768** | Overall #1 but 2nd on quality |
| 3 | Claude Sonnet 4 | **0.762** | Newer Claude slightly worse on quality |
| 4 | GPT-5 Mini | **0.745** | Best OpenAI on quality |
| 5 | Gemini-2.5-Flash | **0.741** | Flash trades quality for speed |
| 6 | GPT-4.1 Mini | **0.739** | |
| 7 | GPT-5 | **0.732** | Newer GPT worse than Mini on quality |
| 8 | o3-mini | **0.726** | |
| 9 | o3 | **0.722** | Reasoning model ≠ better quality |
| 10 | GPT-4.1 | **0.720** | |
| 11 | o4-mini | **0.705** | |
| 12 | GPT-4o Mini | **0.680** | |
| 13 | GPT-4o | **0.678** | Oldest model, worst quality |

**Key insight:** Functional correctness (pass rate) does NOT predict code quality. o3 has the highest functional score (0.385) but ranks 9th on quality. Claude 3.7 Sonnet has the highest quality (0.773) but only 6th on functional correctness. This mirrors the Sabra et al. finding.

### Performance by Difficulty Level (Context Length Scaling)

| Model | Easy (10K-100K) | Medium (100K-200K) | Hard (200K-500K) | Expert (500K-1M) | Δ Easy→Expert |
|---|---|---|---|---|---|
| Gemini-2.5-Pro | 2.278 | 2.302 | 2.329 | 2.339 | **+2.7%** |
| Gemini-2.5-Flash | 2.291 | 2.299 | 2.319 | 2.317 | +1.1% |
| GPT-5 Mini | 2.263 | 2.284 | 2.311 | 2.314 | +2.3% |
| Claude Sonnet 4 | 2.309 | 2.289 | 2.283 | 2.269 | **−1.7%** |
| GPT-5 | 2.254 | 2.268 | 2.298 | 2.323 | +3.1% |
| Claude 3.7 Sonnet | 2.326 | 2.299 | 2.256 | 2.262 | **−2.8%** |
| o3 | 2.086 | 2.149 | 2.187 | 2.195 | +5.2% |

**Key insight:** Google and OpenAI models **improve** with longer context. Anthropic models **degrade**. Gemini-2.5-Pro is the only model that peaks at Expert (1M tokens). Claude 3.7 Sonnet starts strongest at Easy but falls to 6th at Expert.

### Security Analysis Scores (Task-Specific)

| Rank | Model | Security Analysis Score |
|---|---|---|
| 1 | GPT-5 Mini | **2.351** |
| 2 | Gemini-2.5-Pro | **2.343** |
| 3 | GPT-5 | **2.336** |
| 4 | Gemini-2.5-Flash | **2.325** |
| 5 | Claude 3.7 Sonnet | **2.322** |
| 6 | Claude Sonnet 4 | **2.307** |
| 7 | GPT-4.1 Mini | **2.226** |
| 8 | o3-mini | **2.214** |
| 9 | o3 | **2.197** |
| 10 | GPT-4.1 | **2.191** |
| 11 | o4-mini | **2.131** |

### Performance by Programming Language (Total Scores)

| Model | Python | C++ | Java | C | C# | JS | TS | Go | Rust | PHP |
|---|---|---|---|---|---|---|---|---|---|---|
| Gemini-2.5-Pro | **2.788** | 2.074 | 2.326 | 2.064 | 2.419 | 2.268 | 2.203 | 2.338 | 2.002 | 2.641 |
| Gemini-2.5-Flash | 2.752 | **2.106** | 2.329 | 2.086 | 2.418 | 2.274 | **2.248** | 2.292 | 2.039 | 2.573 |
| GPT-5 Mini | **2.799** | 2.039 | **2.329** | 2.050 | 2.414 | **2.280** | 2.189 | 2.264 | **2.088** | 2.476 |
| Claude Sonnet 4 | 2.677 | 2.065 | **2.331** | 2.054 | **2.424** | 2.314 | 2.154 | 2.311 | 1.997 | 2.553 |
| GPT-5 | 2.669 | 2.001 | 2.281 | 2.022 | 2.335 | 2.244 | 2.098 | 2.249 | 2.044 | 2.516 |
| Claude 3.7 Sonnet | 2.663 | 2.100 | 2.314 | **2.062** | 2.364 | 2.245 | 2.162 | **2.298** | 2.000 | **2.641** |

---

## What the Downloaded Data Contains

The 250MB `data.zip` is the **evaluation harness**, not results:

```
data/
├── output/
│   ├── scenarios/          # 8,000 evaluation task JSONs
│   │   ├── python_*_001.json
│   │   ├── cpp_*_002.json
│   │   └── ...             # 10 languages × 8 task categories × 4 difficulties
│   └── validation/
│       └── test_suites/    # 8,000 test suite JSONs (compilation, unit, integration, security tests)
└── generated/
    └── <lang>_<domain>_<difficulty>_<id>/   # 1,000 synthetic codebases
        └── <project>/
            ├── src/
            ├── tests/
            └── docs/
```

**Each scenario JSON contains:**
- `task_category` (one of 8): architectural_understanding, cross_file_refactoring, feature_implementation, bug_investigation, multi_session_development, code_comprehension, integration_testing, security_analysis
- `difficulty` (easy/medium/hard/expert) → maps to context length ranges
- `context_length` (actual token count)
- `task_prompt` (the prompt given to the model)
- `ground_truth` (expected solution)
- `evaluation_criteria` (rubric for automated scoring)
- `context_files` (list of source files forming the codebase context)

**To run this benchmark against ValueRank's 13 models, you would need to:**
1. Install LoCoBench (`pip install -e .`)
2. Configure API keys for each model
3. Run `locobench evaluate --model <model> --config-path config.yaml`
4. Results saved to `evaluation_results/<model>_evaluation_results.json`

---

## Recommendation for ValueRank

### What LoCoBench adds that other benchmarks don't
- **Long-context quality** — the only benchmark testing code quality at 10K–1M token scales
- **4 dimensions, 17 metrics** — LCBS = 5.0 × (0.40·SE + 0.30·FC + 0.20·CQ + 0.10·LCU)
- **Code Quality sub-dimension (20%)** specifically measures Security, Issues Found, Style — overlapping with Sonar's Reliability, Security, and Maintainability

### What it doesn't give you
- ❌ No data for 6/13 ValueRank models (MiMo, MiniMax, Kimi, DeepSeek, GLM, and technically all are newer gens)
- ❌ Code quality is only 20% of the score (not a pure quality benchmark)
- ❌ Uses regex/radon-based analysis, not SonarQube's full 550-rule SonarWay profile
- ❌ Synthetic codebases, not real-world code

### Actionable next steps
1. **Run LoCoBench on all 13 ValueRank models** — the harness is ready, just needs API keys and ~$50–100 in compute
2. **Extract just the Code Quality (20%) sub-score** for ValueRank's quality dimension
3. **Combine with Sonar LLM Leaderboard data** (which has some ValueRank-adjacent models) for broader coverage
4. **The 0-overlap models (MiMo, MiniMax, Kimi, DeepSeek, GLM)** would need to be evaluated via the StetsonMathCS suite or SonarQube directly, as neither LoCoBench nor any other existing benchmark covers them

---

*Report generated from arXiv:2509.09614 paper data + 250MB downloaded evaluation dataset*
*Paper models: 13 (all pre-ValueRank generation)*
*ValueRank models with data: 0 direct / 7 approximate / 6 no proxy*
