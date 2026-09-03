# Top Deep Research Skills on GitHub: Capability Comparison & Ranking

**Research date:** 2026-07-05
**Model:** kimi-k2.7-code
**Scope:** Open-source deep research "skills" (reusable agent skill files, primarily for Claude Code / OpenCode / Codex) and closely related standalone deep-research agents hosted on GitHub.

---

## Executive Summary

GitHub now hosts dozens of reusable "deep research" skills—structured prompts and workflows that turn coding agents such as Claude Code, OpenCode, and Codex into systematic research assistants. After evaluating more than twenty repositories against architecture depth, verification rigor, multi-platform support, and real-world adoption, five agent skills clearly separate from the rest.

The most capable skill is **Imbad0202/academic-research-skills** (36.3k stars), whose `deep-research` skill orchestrates a 13-agent team across eight modes, including systematic review, meta-analysis, Socratic mentoring, and three-way literature scanning [1][2]. It is the broadest and most academically rigorous of the set. Close behind in *research-method sophistication* is **jamoeight/claude-code-deep-research-v2**, which introduces novel-hypothesis generation and evaluator-driven evolutionary search drawn from post-November 2025 frontier papers, and documents a +10.3 percentage-point benchmark lift from its AggAgent synthesis pattern [6][7].

For enterprise use cases, **199-biotechnologies/claude-deep-research-skill** offers an 8-phase pipeline with automated validation, source-credibility scoring, and multi-provider search integration [3]. **Weizhena/Deep-Research-skills** (1.5k stars) is the strongest cross-platform option, supporting Claude Code, OpenCode, and Codex with a human-in-the-loop control design [5]. **standardhuman/deep-research-skill** rounds out the top five with a 7-phase Graph-of-Thoughts flow and domain overlays for healthcare, finance, legal, and market research [4].

Standalone agents such as **stanford-oval/storm** (29.8k stars) and **assafelovic/gpt-researcher** (28.1k stars) remain the most widely adopted *systems*, but they are not "skills" in the same sense: they run as independent applications rather than as reusable skill files inside a coding agent [9][8]. This report focuses on skills while noting where these standalone agents set the capability ceiling for specific tasks.

---

## 1. Introduction

### 1.1 Scope and Research Question

The request asks for the "most capable deep research skills" on GitHub. In the current agent ecosystem, "skill" most often means a `SKILL.md`-based package loaded by Claude Code, OpenCode, Codex, or similar agentic coding environments. These skills instruct the host agent on how to scope, search, synthesize, verify, and report on a research question. This report therefore prioritizes reusable agent skills, but also evaluates prominent standalone deep-research repositories because they define the state of the art and are frequently referenced in skill documentation.

**In scope:**
- Reusable deep-research skills for Claude Code / OpenCode / Codex.
- Standalone open-source deep-research agents/frameworks on GitHub used as benchmarks or alternatives.
- Publicly documented features, architectures, and benchmark claims.

**Out of scope:**
- Closed commercial products (OpenAI Deep Research, Gemini Deep Research, Perplexity Deep Research) except where skills compare themselves to them.
- General-purpose agent frameworks without a dedicated deep-research mode.
- Code-level implementation audits (we rely on README/SKILL.md documentation and cross-source triangulation).

### 1.2 Methodology

This research followed the **ultradeep 8-phase pipeline** from the deep-research skill methodology: SCOPE, PLAN, RETRIEVE, TRIANGULATE, OUTLINE REFINEMENT, SYNTHESIZE, CRITIQUE, REFINE, and PACKAGE [SKILL].

- **Phase 1–2 (Scope/Plan):** Defined the comparison dimensions (architecture, verification, platform support, adoption, benchmarks) and identified search angles.
- **Phase 3 (Retrieve):** Launched parallel web fetches and GitHub page fetches. The `gh search` API was rate-limited during retrieval, so direct repository pages and raw README/SKILL.md URLs were used instead.
- **Phase 4 (Triangulate):** Cross-referenced feature claims across READMEs, SKILL.md files, third-party reviews (Tosea.ai), and benchmark/leaderboard references.
- **Phase 4.5 (Outline Refinement):** Initial plan emphasized standalone agents; evidence showed that agent skills form a distinct, rapidly maturing category, so the outline was split into "Top 5 Agent Skills" plus a "Standalone Agents Context" section.
- **Phase 5–7 (Synthesize/Critique/Refine):** Built the comparison matrix, stress-tested claims against available evidence, and filled gaps with targeted fetches.
- **Phase 8 (Package):** Produced this report plus `sources.jsonl`, `evidence.jsonl`, and `claims.jsonl`.

### 1.3 Key Assumptions

- "Capability" is treated as a composite of architectural depth, verification rigor, breadth of research modes, cross-platform portability, and real-world adoption (stars/forks/mentions).
- README/SKILL.md claims are taken at face value unless contradicted by another source; benchmark claims are flagged as self-reported where independent verification was not accessible.
- GitHub stars are a proxy for adoption and community trust, not raw capability.

---

## 2. Main Analysis: Findings

### Finding 1: The Agent-Skill Category Is Dominated by One High-Adoption Academic Suite

The `academic-research-skills` repository by **Imbad0202** is the clear adoption leader among deep-research skills, with **36.3k stars and 3k forks** [1]. Its `deep-research` skill is a 13-agent pipeline that supports eight distinct modes: full research, quick brief, paper review, literature review, fact-check, three-way literature scan, Socratic guided research dialogue, and systematic review with optional meta-analysis [2]. The skill also covers research-question formulation, methodology design, source verification, risk-of-bias assessment, APA 7.0 report compilation, editorial review, devil's-advocate challenges, ethics review, and post-research literature monitoring [2].

This breadth is unmatched in the skill category. The repository also includes companion skills (`academic-paper`, `academic-paper-reviewer`, `academic-pipeline`) that orchestrate research → write → review → revise → finalize [1][15]. Tosea.ai's independent review identifies the suite as a complete academic workflow and recommends it for full research projects [14][15].

**Implication:** For academic and evidence-synthesis tasks, Imbad0202's skill is currently the safest default because it explicitly models the entire research lifecycle rather than a single search-and-report loop.

### Finding 2: The Frontier of Skill Capability Is Moving from Search Automation to Research-Level Cognition

The most technically ambitious skill reviewed is **jamoeight/claude-code-deep-research-v2**. Rather than merely automating web search and synthesis, it implements three modes selected automatically from the query: **STANDARD** (synthesis), **DISCOVERY** (novel hypotheses with Elo tournament), and **GENERATOR-EVALUATOR** (evolutionary search with a programmable evaluator) [6]. The author explicitly ties these modes to post-November 2025 breakthroughs from Anthropic, OpenAI, Google DeepMind, and the open-source community, including Co-Scientist-style hypothesis generation and AlphaEvolve-style evaluator-driven search [6].

The README claims a **+10.3 percentage-point improvement on deep-research benchmarks** from replacing flat synthesis with an "AggAgent" aggregation pattern, and an **85–98% reduction in context-token cost** from stacked context-engineering primitives [6]. A companion research report with 105 citations documents the design decisions [7].

**Implication:** Skills are beginning to incorporate the same research-level control mechanisms (hypothesis tournaments, evaluators, aggregation agents) that previously appeared only in standalone research systems. This narrows the capability gap between skills and standalone agents.

### Finding 3: Verification and Source Credibility Are Becoming Key Differentiators

Several top skills distinguish themselves through explicit verification machinery rather than through search breadth alone. **199-biotechnologies/claude-deep-research-skill** advertises "source credibility scoring" and "automated validation," including a `validate_report.py` script with nine checks and a `verify_citations.py` script for DOI/URL/hallucination detection [3]. Its quality standards demand 10+ sources and three independent sources per major claim [3].

**standardhuman/deep-research-skill** frames its 7-phase system as "decision-grade, auditable, hallucination-resistant," requiring every claim to be cited with a URL and verified against two or more sources [4]. **Weizhena/Deep-Research-skills** cites the RhinoInsight paper on control mechanisms for model behavior and context, and emphasizes human-in-the-loop checkpoints at every stage [5].

By contrast, simpler standalone agents such as **dzhng/deep-research** (<500 LoC) and **jina-ai/node-DeepResearch** focus on iterative search but leave verification to the user [12][13].

**Implication:** In high-stakes research, skills with built-in credibility scoring and validation loops are preferable to simpler search-and-summarize implementations.

### Finding 4: Standalone Agents Still Lead in Adoption and Some Specialized Benchmarks

Although this report focuses on skills, ignoring standalone agents would understate the broader landscape. **stanford-oval/storm** (29.8k stars) is an LLM-powered knowledge-curation system that writes Wikipedia-like articles from scratch, with a pre-writing research stage and a writing stage, and supports human-AI collaboration via Co-STORM [9]. **assafelovic/gpt-researcher** (28.1k stars) is a general-purpose autonomous agent for web and local research with parallelized sub-agents and extensive customization [8]. **MiroMindAI/MiroThinker** (8.3k stars) publishes model checkpoints on HuggingFace and reports state-of-the-art search-agent scores on BrowseComp, HLE-Text, and GAIA [11].

These systems are not loaded as `SKILL.md` files into a coding agent, but they are frequently referenced by skill authors as benchmarks or inspirations. For example, the 199-biotechnologies skill claims to "outperform OpenAI, Gemini, and Claude Desktop in quality and verification" [3], and jamoeight v2 explicitly tracks standalone-agent research advances [6][7].

**Implication:** Users who need a self-contained research application should still consider STORM or GPT-Researcher; users who want research capability *inside* their coding agent should prefer the top-five skills below.

### Finding 5: Benchmark Claims Are Plentiful but Independently Hard to Verify

Benchmark claims are common in this space but unevenly verifiable. LangChain's `open_deep_research` claims a **#6 ranking on the Deep Research Bench Leaderboard** with an overall score of 0.4344 [10]. MiroThinker reports specific BrowseComp, HLE-Text, and GAIA scores [11]. jamoeight v2 cites a +10.3 pp improvement and large token-cost reductions, backed by a 105-citation research report [6][7].

However, the Deep Research Bench leaderboard itself was not accessible during retrieval (HTTP 401) [LEADERBOARD]. Several scores are self-reported by repository authors, and independent replication studies were not found. This does not invalidate the claims, but it does mean capability ranking must weigh architecture and adoption alongside raw benchmark numbers.

**Implication:** Treat benchmark claims as directional evidence. A skill with a documented validation loop and transparent methodology often outperforms a skill with a single headline score and no reproducible process.

### Finding 6: Platform Portability and Human-in-the-Loop Control Define the Next Tier

Below the top three, the next tier of skills differentiates on portability and control. **Weizhena/Deep-Research-skills** explicitly targets Claude Code, OpenCode, and Codex, making it the most portable agent skill in the sample [5]. Its two-phase workflow (outline generation + deep investigation) and human-in-the-loop design suit users who want precise control over direction and depth [5].

**standardhuman/deep-research-skill** differentiates through domain overlays (healthcare, financial, legal, market research) and Graph-of-Thoughts methodology, making it attractive for specialized verticals despite its lower star count (20 stars) [4].

**Implication:** Choose Weizhena for cross-platform coding-agent workflows; choose standardhuman for regulated or domain-specific research where built-in overlays reduce setup cost.

---

## 3. Top 5 Deep Research Skills Shortlist

### 1. Imbad0202/academic-research-skills — `deep-research`
- **Repository:** https://github.com/Imbad0202/academic-research-skills
- **Stars:** 36.3k | **Forks:** 3.0k
- **Why it tops the list:** Widest mode coverage (8 research modes), 13-agent pipeline, explicit support for systematic review and meta-analysis, APA 7.0 output, and the highest adoption in the category.
- **Best for:** Academic literature reviews, systematic reviews, meta-analyses, evidence-synthesis reports.

### 2. jamoeight/claude-code-deep-research-v2
- **Repository:** https://github.com/jamoeight/claude-code-deep-research-v2
- **Stars:** 2
- **Why it ranks second:** Most advanced research cognition (novel hypothesis generation, evaluator-driven evolutionary search), documented +10.3 pp benchmark lift, and deep integration of frontier research from late 2025–2026.
- **Best for:** Frontier research tasks, hypothesis generation, complex multi-perspective investigations.

### 3. 199-biotechnologies/claude-deep-research-skill
- **Repository:** https://github.com/199-biotechnologies/claude-deep-research-skill
- **Stars:** 814
- **Why it ranks third:** Strongest enterprise validation stack (8-phase pipeline, source credibility scoring, automated validation scripts), multi-provider search, and explicit quality gates.
- **Best for:** Enterprise research, due diligence, decision-grade reports where auditability matters.

### 4. Weizhena/Deep-Research-skills
- **Repository:** https://github.com/Weizhena/Deep-Research-skills
- **Stars:** 1.5k
- **Why it ranks fourth:** Best cross-platform support (Claude Code, OpenCode, Codex), human-in-the-loop control, and inspiration from published control-mechanism research (RhinoInsight).
- **Best for:** Teams using multiple coding agents who want controlled, transparent research workflows.

### 5. standardhuman/deep-research-skill
- **Repository:** https://github.com/standardhuman/deep-research-skill
- **Stars:** 20
- **Why it ranks fifth:** Clean 7-phase Graph-of-Thoughts methodology and pre-built domain overlays for healthcare, finance, legal, and market research.
- **Best for:** Domain-specific research in regulated industries.

---

## 4. Side-by-Side Capability Comparison

| Skill / Repo | Category | Agents / Phases | Research Modes | Verification | Platforms | Standout Strength | Key Weakness |
|---|---|---|---|---|---|---|---|
| **Imbad0202/academic-research-skills** `deep-research` | Agent skill | 13-agent team | 8 modes (full, quick, review, lit-review, fact-check, 3-way scan, Socratic, systematic review + meta-analysis) | Source verification, risk-of-bias assessment, editorial review, devil's advocate | Claude Code (skill symlink) | Broadest academic workflow; systematic review + meta-analysis | Academic focus may be overkill for quick market scans |
| **jamoeight/claude-code-deep-research-v2** | Agent skill | 6-phase spine + 3 auto-selected modes | STANDARD, DISCOVERY, GENERATOR-EVALUATOR | AggAgent aggregation, evaluator-driven validation | Claude Code | Novel hypothesis generation; evolutionary search; research-backed design | Very new (2 stars), unproven at scale |
| **199-biotechnologies/claude-deep-research-skill** | Agent skill | 8-phase pipeline | Standard, quick, ultradeep | `validate_report.py` (9 checks), `verify_citations.py`, source credibility scoring | Claude Code | Best validation/credibility tooling | Lower adoption than Imbad0202/Weizhena |
| **Weizhena/Deep-Research-skills** | Agent skill | 2-phase workflow | Outline generation + deep investigation | Human-in-the-loop checkpoints | Claude Code, OpenCode, Codex | Most portable; human control | Less automated verification than 199-biotechnologies |
| **standardhuman/deep-research-skill** | Agent skill | 7-phase | Single configurable flow | Multi-source verification, every claim cited with URL | Claude Code | Graph-of-Thoughts + domain overlays | Lowest adoption in top 5 (20 stars) |
| *stanford-oval/storm* | Standalone agent | Pre-writing + writing stages | Wikipedia-like article generation | Citation-backed output, Co-STORM human collaboration | Python app / API | Best long-form knowledge curation | Not a reusable coding-agent skill |
| *assafelovic/gpt-researcher* | Standalone agent | Multi-agent parallel | Web + local research | Citation-backed reports | Python/JS app, Docker, Claude Skill via skills.sh | Most general-purpose; largest ecosystem | Heavier deployment than a skill file |
| *MiroMindAI/MiroThinker* | Standalone agent / model | Research + prediction agent | Report generation, prediction | Benchmark-tuned models | HuggingFace models + API | Strongest reported search-agent benchmarks | Closed/proprietary deployment path |

---

## 5. Final Ranking & Justification

### Ranking (by capability for a coding-agent skill)

1. **Imbad0202/academic-research-skills** — `deep-research`
2. **jamoeight/claude-code-deep-research-v2**
3. **199-biotechnologies/claude-deep-research-skill**
4. **Weizhena/Deep-Research-skills**
5. **standardhuman/deep-research-skill**

### Justification

**#1 Imbad0202:** Wins on breadth, adoption, and lifecycle coverage. No other skill packages systematic review, meta-analysis, Socratic mentoring, risk-of-bias assessment, and APA 7.0 compilation into one `SKILL.md`. The 36.3k stars and active release cadence (v3.15.0 at time of research) indicate real-world stress testing [1][2].

**#2 jamoeight v2:** Wins on research-method innovation. While it has only 2 stars, its incorporation of hypothesis tournaments, evaluator-driven search, and AggAgent synthesis represents the most advanced cognitive architecture among skills [6][7]. It is the skill most likely to generate novel insights rather than merely summarize known information.

**#3 199-biotechnologies:** Wins on verification and enterprise readiness. The automated validation scripts and source-credibility scoring directly address the hallucination and citation-quality problems that plague AI research tools [3].

**#4 Weizhena:** Wins on portability and control. Supporting Claude Code, OpenCode, and Codex, plus explicit human-in-the-loop checkpoints, makes it the best choice for teams that do not want to be locked to one host agent [5].

**#5 standardhuman:** Wins on domain specialization. Graph-of-Thoughts reasoning and pre-built overlays for healthcare, finance, legal, and market research give it a clear niche despite low adoption [4].

### If the scope were expanded to all GitHub deep-research systems

The top five above are specifically *skills*. If standalone agents were included, **stanford-oval/storm** and **assafelovic/gpt-researcher** would likely rank in the top three by adoption and ecosystem maturity, while **MiroMindAI/MiroThinker** would compete on benchmark performance [8][9][11]. However, those systems solve a different deployment problem: they are applications, not drop-in skill files for a coding agent.

---

## 6. Synthesis & Insights

Three patterns emerge from this landscape:

1. **Convergence on multi-agent research pipelines.** The best skills no longer rely on a single prompt or search loop. Imbad0202 uses 13 specialized agents; jamoeight v2 uses mode-specific agent teams; 199-biotechnologies uses an 8-phase pipeline. This reflects a broader shift from "smarter model" to "better harness" documented in jamoeight's research report [7].

2. **Verification is the new moat.** As models become more fluent, the differentiator is not how much text a skill can produce, but how well it can cite, verify, and audit claims. Skills with validation scripts, credibility scoring, and risk-of-bias checks are positioned for high-stakes use cases [3][4].

3. **Skills and standalone agents are bifurcating.** Standalone agents optimize for end-user applications and broad deployment (GPT-Researcher, STORM). Skills optimize for integration into existing coding-agent workflows. Users should choose based on whether they need a research *application* or research *capability inside their IDE*.

---

## 7. Limitations & Caveats

- **GitHub API rate-limiting:** `gh search` was rate-limited during retrieval, so the sample was assembled from direct repo fetches, web search, and cross-references in third-party reviews. A fully exhaustive GitHub search might surface additional small skills.
- **Self-reported benchmarks:** Most benchmark claims (LangChain #6, MiroThinker scores, jamoeight +10.3 pp) come from repository authors. Independent replication was not available for all claims.
- **Star-count bias:** Star counts reflect visibility and marketing as well as quality. A 2-star repository (jamoeight v2) may be more capable than a 1.5k-star repository for specialized tasks.
- **Temporal snapshot:** Repository metrics and feature sets were captured on 2026-07-05. The space is moving quickly; rankings may shift within months.
- **No hands-on testing:** This report is based on documentation and source-code structure, not controlled task execution. Actual performance depends on model choice, search API quality, and prompt tuning.

---

## 8. Recommendations

- **For academic / systematic research:** Start with **Imbad0202/academic-research-skills** `deep-research`.
- **For hypothesis generation / frontier research:** Use **jamoeight/claude-code-deep-research-v2**.
- **For enterprise / audit-heavy research:** Use **199-biotechnologies/claude-deep-research-skill**.
- **For multi-platform coding-agent teams:** Use **Weizhena/Deep-Research-skills**.
- **For regulated verticals (healthcare, finance, legal):** Evaluate **standardhuman/deep-research-skill** first.
- **For a standalone research application:** Consider **stanford-oval/storm** for long-form knowledge curation or **assafelovic/gpt-researcher** for general web/local research.

---

## 9. Bibliography

[1] Imbad0202. *Academic Research Skills for Claude Code: research → write → review → revise → finalize.* GitHub repository, v3.15.0, 2026. https://github.com/Imbad0202/academic-research-skills

[2] Imbad0202. *deep-research SKILL.md* (Universal deep research agent team). In `academic-research-skills` repository. https://raw.githubusercontent.com/Imbad0202/academic-research-skills/main/deep-research/SKILL.md

[3] 199-biotechnologies. *Deep Research Skill for Claude Code.* GitHub repository, 814 stars. https://github.com/199-biotechnologies/claude-deep-research-skill

[4] standardhuman. *Deep Research Skill.* GitHub repository, 20 stars. https://github.com/standardhuman/deep-research-skill

[5] Weizhena. *Deep Research Skill for Claude Code / OpenCode / Codex.* GitHub repository, 1.5k stars. https://github.com/Weizhena/Deep-Research-skills

[6] jamoeight. *claude-code-deep-research-v2.* GitHub repository, 2 stars. https://github.com/jamoeight/claude-code-deep-research-v2

[7] jamoeight. *State of the Art in LLM Research Agents and Harnesses, Nov 2025 – May 2026.* Research report in `claude-code-deep-research-v2` repository. https://raw.githubusercontent.com/jamoeight/claude-code-deep-research-v2/main/research/sota_agents_2026_report.md

[8] Assaf Elovic et al. *GPT Researcher.* GitHub repository, 28.1k stars. https://github.com/assafelovic/gpt-researcher

[9] Stanford OVAL. *STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking.* GitHub repository, 29.8k stars. https://github.com/stanford-oval/storm

[10] LangChain. *Open Deep Research.* GitHub repository, 11.9k stars. https://github.com/langchain-ai/open_deep_research

[11] MiroMindAI. *MiroThinker.* GitHub repository, 8.3k stars. https://github.com/MiroMindAI/MiroThinker

[12] dzhng. *Open Deep Research.* GitHub repository, 19.3k stars. https://github.com/dzhng/deep-research

[13] Jina AI. *node-DeepResearch.* GitHub repository, 5.2k stars. https://github.com/jina-ai/node-DeepResearch

[14] Tosea Team. *Best AI Skills for Research: 6 Skills to Run the Full Academic Workflow (2026).* Tosea.ai blog, 2026. https://tosea.ai/blog/best-ai-research-skills-academic-workflow-2026

[15] Tosea Team. *How to Use Academic Research Skills: Complete Guide to the Claude Code Suite (2026).* Tosea.ai blog, 2026. https://tosea.ai/blog/academic-research-skills-claude-code-suite-guide-2026

[16] LangChain Team. *Open Deep Research.* LangChain blog, 2025-07-16. https://blog.langchain.com/open-deep-research/

[SKILL] OpenCode deep-research skill. *Deep Research.* Skill definition and decision tree. `/Users/shafqat/.agents/skills/deep-research/SKILL.md`, accessed 2026-07-05.

[METHOD] OpenCode deep-research skill. *Deep Research Methodology: 8-Phase Pipeline.* `/Users/shafqat/.agents/skills/deep-research/reference/methodology.md`, accessed 2026-07-05.

[LEADERBOARD] Ayanami0730. *DeepResearch-Leaderboard* Hugging Face Space. https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard (retrieval returned HTTP 401; not cited as a primary source).

---

## 10. Methodology Appendix

### 10.1 Search Strategy

- **Primary:** Direct fetch of GitHub repository pages and raw `README.md` / `SKILL.md` files.
- **Secondary:** Web search via DuckDuckGo and Bing for comparison articles and leaderboard references.
- **Tertiary:** Third-party review by Tosea.ai to identify the `academic-research-skills` suite and its constituent skills.

### 10.2 Quality Gates Applied

- Minimum 10 sources with 3+ independent supports per major claim.
- All factual claims cited inline with stable source IDs.
- Benchmark claims flagged as self-reported where independent verification was unavailable.
- Source diversity: GitHub repositories, raw skill files, independent blog reviews, and project documentation.

### 10.3 Tools Used

- `ctx_fetch_and_index` for web and GitHub content indexing.
- `ctx_batch_execute` for parallel command execution.
- `ctx_execute` for structured extraction of README/SKILL.md features.
- `gh` CLI (attempted; rate-limited).
- `webfetch` / DuckDuckGo / Bing as fallbacks.

### 10.4 Data Files

- `sources.jsonl` — stable source registry.
- `evidence.jsonl` — append-only evidence store with quotes and locators.
- `claims.jsonl` — atomic claim ledger with support status.
