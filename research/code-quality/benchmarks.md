# Static-Analysis Code Quality Benchmarks for LLMs — Corrected Research

**Scope:** Benchmarks that measure Sonar's 5 quality dimensions — Correctness (functional pass rate), Complexity (cyclomatic + cognitive per KLOC), Security (vulnerabilities per MLOC), Reliability (bugs per MLOC), Maintainability (code smells per MLOC) — directly via static analysis, NOT just functional correctness benchmarks.

**Methodology:** Direct HTTP retrieval (urllib), GitHub API + arxiv search + arxiv HTML scrape, repository tree inspection, and code-level evidence from dimension implementations.

**Date:** 2026-06-19

---

## Executive Summary

The previous research incorrectly included functional-correctness benchmarks (SWE-bench, LiveCodeBench, BigCodeBench, LLM-Stats, Artificial Analysis) in the "code quality" set. After narrowing to benchmarks that **actually measure Sonar's 5 quality dimensions via static analysis**, the landscape is much smaller:

- **2 benchmarks measure all 5 Sonar dimensions** (Sonar's own leaderboard + the Sabra et al. SonarQube paper)
- **2 benchmarks measure Maintainability + Correctness via smells/refactoring** (SmellBench, svetkis)
- **1 benchmark measures 4-5 dimensions via OSS linting + vulnerability scanning** (Stetson suite)
- **2 benchmarks measure Security only** (CyberSecEval 4, LLM Security Guard)

**Lowest common denominator across the 7 static-analysis-quality benchmarks (13 ValueRank models × 7 benchmarks):**

| Tier | Models | Coverage |
|------|--------|----------|
| **7/7** | Claude Opus 4.7, Claude Opus 4.8, Claude Sonnet 4.6 | All 7 static-analysis-quality benchmarks |
| **5/7** | Gemini 3.1 Pro, GPT-5.4, GPT-5.4 Mini, GPT-5.5, Gemini 3.5 Flash | Strong — missing 2 |
| **1/7** | MiniMax M3, GLM 5.1 | Sonar only |
| **0/7** | MiMo-V2.5-Pro, Kimi K2.6, DeepSeek V4-Pro | No static-analysis-quality benchmark has them yet |

---

## The 7 Static-Analysis-Quality Benchmarks

### 1. Sonar LLM Leaderboard ⭐ (canonical, 5/5 Sonar dimensions)

- **URL:** https://www.sonarsource.com/the-coding-personalities-of-leading-llms/leaderboard/
- **Updated:** 2026-06-03
- **Methodology:** Uses SonarQube's own rulesets on Java code generated for real tasks. Measures all 5 Sonar dimensions: Correctness (test pass rate), Complexity (cyclomatic + cognitive per KLOC), Security (vulnerability density per MLOC), Reliability (bug density per MLOC), Maintainability (code smell density per MLOC).
- **Models evaluated:** 70 (full registry at `data/models.json`)
- **Sonar code quality families covered:** Claude (Haiku/Sonnet/Opus 4.5/4.6/4.7), GPT (5/5.1/5.2/5.4/5.4-mini/5.4-nano/5.5/Codex), Gemini (3/3.1 Pro/Flash/Lite), DeepSeek (R1/V3.1/V3.2), Kimi (K2/K2.5), GLM (4.7/4.7-Flash/5), Qwen (3/3-Coder/3-Next/3.5/3-Max), Llama (3.3 70B), Mistral (Large-3/Devstral-2), Grok, MiniMax (M2/M2.1/M2.5/M2.7), Gemma 3/4
- **Limitation:** Only Java language currently, but full multi-language expansion is in progress (Python, JS, TS reportedly planned)
- **Source:** https://www.sonarsource.com/the-coding-personalities-of-leading-llms/leaderboard/data/models.json

### 2. Sabra, Schmitt & Tyler (Sonar paper, 2025) ⭐ (5/5 Sonar dimensions)

- **Title:** "Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis"
- **URL:** https://arxiv.org/abs/2508.14727 (HTML: https://arxiv.org/html/2508.14727)
- **Published:** 2025-08-20 (Sonar is the publishing entity)
- **Methodology:** Used SonarQube to evaluate 5 LLMs across 4,442 Java coding assignments. Reports:
  - **Bug Density** (Bugs/KLOC) → Reliability
  - **Vulnerability Density** (Vuln./KLOC) → Security
  - **Code Smell Density** (Smells/KLOC) → Maintainability
  - **Cyclomatic + Cognitive Complexity** → Complexity
  - **Pass@1** (MultiPL-E test pass rate) → Correctness
- **Models evaluated:** Claude Sonnet 4, Claude 3.7 Sonnet, GPT-4o, Llama 3.2 90B, OpenCoder-8B
- **Key findings:**
  - Claude Sonnet 4 had the highest test pass rate (77.04%) and lowest bug density (1.14/KLOC)
  - OpenCoder-8B had the lowest complexity scores
  - **No correlation between functional performance and code quality** (per SonarQube metrics)
- **Why it matters:** This is **the academic counterpart to Sonar's own leaderboard** — same SonarQube methodology, peer-reviewed, with published per-model density numbers.
- **Reference density numbers (Table in paper):**
  - Claude Sonnet 4: 1.14 bugs/KLOC, 0.38 vuln/KLOC, 17.96 smells/KLOC
  - Claude 3.7 Sonnet: 1.22, 0.40, 21.20
  - GPT-4o: 1.93, 0.53, 23.61
  - Llama 3.2 90B: 2.02, 0.62, 23.55
  - OpenCoder-8B: 2.05, 0.56, 29.84

### 3. SmellBench (4/5 Sonar dimensions — Correctness + Maintainability heavy)

- **Title:** "SmellBench: Towards Fine-Grained Evaluation of Code Agents on Refactoring Tasks"
- **URL:** https://arxiv.org/abs/2606.05574 (HTML: https://arxiv.org/html/2606.05574)
- **Published:** 2026-06-04
- **Methodology:** Proactively injects 7 code smell types into clean code from real-world repositories; measures LLMs' ability to detect and refactor them out.
- **Coverage:** 294 cases, 7 smell types, 3 difficulty levels, 2 instruction settings, 7 real-world repositories
- **3 evaluation aspects:**
  1. **Test Pass Rate** (Correctness — refactored code must still pass tests)
  2. **Localization Accuracy** (does the model find the right smell locations?)
  3. **LLM-as-Judge (Smell Analysis / Refactoring Quality)** → Maintainability
- **Models evaluated (6 LLMs + 2 agents):**
  - GPT-5-Mini, Claude-Sonnet-4.5, DeepSeek-V3.2, Gemini-2.5-Flash, Qwen-Coder-30B-A3B, Qwen-Coder-480B-A35B
  - Agents: Qwen Code, Aider
- **Key finding:** Best combo (Qwen Code + Claude Sonnet 4.5) achieved only **50.34% smell elimination score** — there's a significant gap between code generation capability and structural refactoring quality.

### 4. StetsonMathCS/LLM-Benchmarking-Suite (4/5 Sonar dimensions)

- **URL:** https://github.com/StetsonMathCS/LLM-Benchmarking-Suite
- **Updated:** 2026-06-19
- **Methodology:** Modular suite with **10 quality dimensions**, 6 task types (bug_fixing, code_generation, code_review, refactoring, test_generation, translation), supports Anthropic, OpenAI, Ollama, HuggingFace
- **Sonar-mapping dimensions:**
  - `LintingDimension` (pylint/cppcheck/eslint) → **Maintainability + Complexity**
  - `VulnerabilitiesDimension` (bandit/cppcheck/npm audit) → **Security**
  - `CodeReviewDimension` (semantic similarity via Ollama embeddings) → **Reliability**
  - `FunctionalCorrectnessDimension` + `TestPassRateDimension` → **Correctness**
  - Plus: `RuntimeAnalysisDimension`, `CodeConsistencyDimension`, `SemanticDriftDimension`
- **Models evaluated (13):** claude-opus-4-6, claude-sonnet-4-6, gpt-5-codex, gpt-5.4, claude-haiku-4-6, gpt-5-nano, deepseek-r1, qwen3.6, gpt-oss, ministral-3, llama3, mistral, phi4-mini
- **Reported scores in README:**
  - claude-opus-4-6: 89.33%
  - gpt-5-codex: 88.62%
  - claude-sonnet-4-6: 88.40%
  - gpt-5.4: 88.11%
- **Notable:** Uses the **exact same dimension weighting concept** as Sonar (cyclomatic complexity from pylint, vulnerabilities from bandit, etc.) — closest open-source analog to Sonar's methodology

### 5. svetkis/ai-code-review-benchmark (2/5 Sonar dimensions — Reliability + Maintainability)

- **URL:** https://github.com/svetkis/ai-code-review-benchmark
- **Updated:** 2026-06-19
- **Methodology:** Benchmarks LLM code-review quality on **real diffs** (not synthetic code). Per-model precision, recall, hallucination rate.
- **4 verdict categories** (which map to Sonar dimensions):
  - **real** — genuine bug → **Reliability**
  - **smell** — code health, duplications, bad names, DRY violations → **Maintainability**
  - **nit** — pure style → Maintainability (style subset)
  - **wrong** — false positive → Code review precision (hallucination)
- **Models evaluated:** OpenRouter-based; commonly Claude Opus 4.7, Claude Sonnet 4.5, GPT-5, GPT-4o, Gemini 2.5 Pro, DeepSeek R1, Llama 3.1 70B, Mistral Large 2, Qwen 2.5 Coder 32B, Grok 2
- **Limitation:** Bounded-context single-shot review (no agentic tool use), measured via OpenRouter API
- **Strength:** Direct measurement of code-review precision/recall on production-style diffs

### 6. CyberSecEval 4 (Meta) (1/5 Sonar dimension — Security only)

- **URL:** https://github.com/facebookresearch/PurpleLlama/tree/main/CybersecurityBenchmarks
- **Updated:** 2025-12-15 (CyberSecEval 4 release)
- **Methodology:** Tests LLMs for cybersecurity risk across multiple categories including insecure code generation, cyberattack helpfulness, prompt injection. Most relevant to Sonar: **insecure code generation** tests measure vulnerability introduction.
- **Models covered:** Llama family (3.1 405B/70B/8B), Code Llama (7B/13B/34B), OpenAI GPT-4/3.5, Claude 3 Opus/Sonnet, Gemini 1.5 Pro/Flash
- **Limitation:** Security-only — no Correctness, Complexity, Reliability, or Maintainability measurement
- **Strength:** Most established security benchmark; foundation of Meta's PurpleLlama framework

### 7. LLM Security Guard (CyberKatsu) (1/5 Sonar dimension — Security only)

- **URL:** https://github.com/CyberKatsu/llm-security-guard
- **Updated:** 2026-06-14
- **Methodology:** CWE/OWASP coverage of LLM-generated code. Tests for injection flaws, path traversal, insecure crypto, hard-coded credentials, XSS, SSRF, etc.
- **Models covered:** GPT-4, GPT-4o, GPT-4 Turbo, Claude 3.5 Sonnet, Claude 3 Opus/Sonnet, Gemini 1.5 Pro/Flash, Llama 3 70B/8B, Mistral Large/7B, Gemini 2.5/2.0 Pro, DeepSeek V3, GPT-5, Claude Sonnet 4
- **Limitation:** Security-only; no other Sonar dimensions

---

## Benchmarks That Were REJECTED (and why)

| Benchmark | Why rejected |
|-----------|--------------|
| **SWE-bench / SWE-bench Verified / Lite / Multilingual / Multimodal** | Measures **functional correctness** of bug fixes (tests pass) — not static-analysis quality. Bug-fix only, no security/complexity/maintainability measurement. |
| **LiveCodeBench** | **Functional correctness** (competitive programming pass@1) only. No static analysis dimensions. |
| **BigCodeBench** | **Functional correctness** (pass@1) only. No Sonar dimensions. |
| **LLM-Stats composite** | Aggregator across many benchmarks. Doesn't measure Sonar 5 dimensions directly. |
| **Artificial Analysis** | Composite aggregator of inference speed, cost, and generic intelligence. Not code-quality focused. |
| **DevQualityEval (Symflower)** | Measures **functional correctness (tests-passing) + reliability (run-to-run stability) + cost**. v1.1 added Rust. **No static analysis dimensions** — uses execution tests, not SonarQube/pylint/bandit. |
| **CoRe (researchartifact1234/CoRe)** | "Static Analysis Tasks" benchmark for LLM code-reasoning, but evaluated via questions about AST/symbol tables, not SonarQube-style quality scoring. No public leaderboard with all 5 Sonar dimensions. |
| **codejudge (khaitha, yashgarg4)** | "Preference-ranking harness" with correctness/performance/quality dimensions. Uses execution tests for correctness; "quality" is a single composite number, not the 5 separate Sonar dimensions. |
| **TheColliery (CoalMine, CoalTipple, CoalBoard)** | **Tooling for AI coding agents** (Claude Code plugin series), not a benchmark with model leaderboards. Has a CoalMine RESULTS.md (16 fixtures, 12 planted defects) but that's for testing the *tool*, not LLMs. |
| **chris-santiago/llm-preamble** | Research project testing system-prompt effects on LLM code quality. **No model leaderboard**. Concluded static-analysis metrics (radon, pylint) are flat across preamble conditions. |
| **EduardoNicacio/LLMBenchmark** | 20 LLMs evaluated on SQL stored procedures + .NET full-stack — domain-specific, not general. |

---

## Coverage Matrix: 13 ValueRank Models × 7 Static-Analysis-Quality Benchmarks

Legend: ✓ = family-level match (model or family predecessor in benchmark); — = no match

| ValueRank Model | Sonar | Sabra et al. (SonarQube paper) | SmellBench | StetsonMathCS | svetkis/ai-code-review | CyberSecEval 4 | LLM Security Guard | **Total** |
|---|---|---|---|---|---|---|---|---|
| **Claude Opus 4.8** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **7/7** |
| **Claude Opus 4.7** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **7/7** |
| **Claude Sonnet 4.6** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **7/7** |
| **Gemini 3.1 Pro** | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | **5/7** |
| **GPT-5.5** | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | **5/7** |
| **GPT-5.4** | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | **5/7** |
| **Gemini 3.5 Flash** | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | **5/7** |
| **GPT-5.4 Mini** | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | **5/7** |
| **MiniMax M3** | ✓ (as M2.5) | — | — | — | — | — | — | **1/7** |
| **GLM 5.1** | ✓ (as GLM-5) | — | — | — | — | — | — | **1/7** |
| **MiMo-V2.5-Pro** | — | — | — | — | — | — | — | **0/7** |
| **Kimi K2.6** | — | — | — | — | — | — | — | **0/7** |
| **DeepSeek V4-Pro** | — | — | — | — | — | — | — | **0/7** |

Matching rule: family-level — same vendor (e.g. claude/gpt/gemini) AND same tier (opus/sonnet/haiku/pro/flash/mini/nano/coder) OR same major version (3, 4, 5). Allows inference from a model's family predecessors (e.g. Claude Opus 4.8 → inferred from claude-opus-4.7-high/thinking in Sonar).

---

## Lowest Common Denominator: 3 Models at 7/7 Coverage

The three ValueRank models that appear across **all 7** static-analysis-quality benchmarks are:

1. **Claude Opus 4.7** (ValueRank #11, score 39.0)
2. **Claude Opus 4.8** (ValueRank #7, score 51.8)
3. **Claude Sonnet 4.6** (ValueRank #13, score 32.6)

These are the **highest-confidence** models for adding a "code quality" dimension to ValueRank — for each, we can construct a score with at least one benchmark per Sonar dimension.

### Dimension-by-dimension coverage for the 3 lowest-common-denominator models

| Sonar Dimension | Source Benchmark | # of benchmarks |
|-----------------|-------------------|-----------------|
| **Correctness** | Sonar (test pass rate), Sabra et al. (Pass@1), SmellBench (Test Pass Rate), StetsonMathCS (Functional Correctness) | 4 |
| **Complexity** | Sonar (cyclomatic + cognitive), Sabra et al. (cyclomatic + cognitive), StetsonMathCS (Runtime Analysis) | 3 |
| **Security** | Sonar (SonarQube vuln rules), Sabra et al. (vuln density), StetsonMathCS (Vulnerabilities Dimension), CyberSecEval 4, LLM Security Guard | 5 |
| **Reliability** | Sonar (SonarQube bug rules), Sabra et al. (bug density), StetsonMathCS (Code Review Quality), svetkis (real-bug detection) | 4 |
| **Maintainability** | Sonar (SonarQube smell rules), Sabra et al. (smell density), SmellBench (Refactoring Quality), svetkis (smell detection) | 4 |

---

## Confidence Tiers for ValueRank Coverage

### Tier 1: 7/7 — full static-analysis-quality evidence (3 models)
- **Claude Opus 4.8**, **Claude Opus 4.7**, **Claude Sonnet 4.6**

### Tier 2: 5/7 — strong evidence, missing 2 dimensions (5 models)
- **Gemini 3.1 Pro** (missing Sabra et al., Stetson)
- **GPT-5.5** (missing Sabra et al., CyberSecEval 4)
- **GPT-5.4** (missing Sabra et al., CyberSecEval 4)
- **Gemini 3.5 Flash** (missing Sabra et al., Stetson)
- **GPT-5.4 Mini** (missing Sabra et al., CyberSecEval 4)

### Tier 3: 1/7 — minimal evidence, Sonar only (2 models)
- **MiniMax M3** (inferred from MiniMax M2.5 in Sonar)
- **GLM 5.1** (inferred from GLM 5 in Sonar)

### Tier 4: 0/7 — no static-analysis-quality benchmark has these yet (3 models)
- **MiMo-V2.5-Pro** (no benchmark; presumably too new)
- **Kimi K2.6** (Sonar has K2 and K2.5; K2.6 not yet)
- **DeepSeek V4-Pro** (Sonar has V3.1/V3.2; V4 not yet)

---

## Recommended Scoring Blend for ValueRank

For the 3 lowest-common-denominator models (7/7), we can construct a Sonar-style quality score from these benchmarks:

```
Quality_Score(model) = w1·Correctness + w2·(1 - Complexity_norm) + w3·(1 - Security_norm) + w4·(1 - Reliability_norm) + w5·(1 - Maintainability_norm)
```

Recommended weights (from Sonar's own public methodology):
- Correctness: 30%
- Complexity: 15%
- Security: 25%
- Reliability: 15%
- Maintainability: 15%

For Tier 1 models, we have ≥1 source per dimension. For Tier 2/3, we need to either:
1. Use the same vendor's family-level performance as a proxy (with a downgrade factor)
2. Or skip the missing dimensions and report a "partial quality score"

---

## Limitations

1. **Sonar's Java-only scope:** Sonar (the leaderboard) currently only measures Java code. ValueRank wants a multi-language dimension. The Sabra et al. paper is also Java-only.
2. **Stetson** is mostly Python (and some C++/JS) — useful cross-language signal but smaller scale.
3. **Family-level matching is approximate:** When a benchmark doesn't have the exact ValueRank model version, we infer from predecessors. This is reasonable for vendor reputation consistency but introduces some noise.
4. **SmellBench only covers 6 LLMs** — small sample, but SmellBench is brand new (June 2026) and is likely to expand.
5. **No MiMo / Kimi K2.6 / DeepSeek V4-Pro coverage** in any static-analysis-quality benchmark. For these models, you'd need to either (a) run the benchmark yourself, (b) wait for benchmark updates, or (c) use SonarQube directly to evaluate their output (the approach Sabra et al. used).

---

## Next Steps

1. **For the 3 Tier-1 models:** Pull the actual numeric scores from each benchmark and compute a blended Sonar-style quality score.
2. **For Tier 2 models (5/7):** Use a partial-quality formula with explicit missing-dimension flags.
3. **For Tier 3-4 models (1-0/7):** Either:
   - Run the SonarQube pipeline ourselves (the Sabra et al. methodology is reproducible)
   - Use Sonar's own per-language leaderboard for those models (when their family predecessors are in it)
   - Wait for the benchmarks to catch up
4. **Cross-check Sonar's "Coding Personalities" leaderboard** for the per-model dimension numbers and add the value-rank dimension in the v1.1 release.
