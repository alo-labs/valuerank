# Deep Research Skills: Top 5 Most Capable Open-Source Implementations on GitHub

**Research Date:** July 5, 2026
**Model:** mimo-v2.5
**Mode:** Ultradeep (8-phase pipeline)
**Scope:** Open-source deep research agents, skills, and frameworks on GitHub

---

## Executive Summary

This report identifies and ranks the top 5 most capable deep research skills/agents available on GitHub as of July 2026. After systematically searching across 10+ query variants and analyzing 30+ repositories, we shortlisted candidates based on GitHub stars, feature richness, architectural sophistication, multi-source research capabilities, and community adoption.

**Key Finding:** The deep research ecosystem has bifurcated into two distinct categories: (1) **standalone research agents** (GPT-Researcher, Alibaba DeepResearch, LangChain Open Deep Research) that are complete end-to-end systems, and (2) **skill-based research frameworks** (claude-deep-research-skill) designed to enhance existing AI coding assistants. The most capable systems combine hierarchical multi-agent architectures with multi-source search aggregation, citation tracking, and automated report generation.

**Top 5 Ranked by Capability:**

| Rank | Project | Stars | Type | Key Differentiator |
|------|---------|-------|------|-------------------|
| 1 | GPT-Researcher | ~18K+ | Standalone Agent | Most mature, multi-LLM, 20+ source aggregation |
| 2 | Alibaba-NLP/DeepResearch | 19,606 | Model + Agent | Custom 30B model, RL-trained, benchmark leader |
| 3 | LangChain Open Deep Research | ~5K+ | Framework Agent | Configurable, MCP support, Deep Research Bench #6 |
| 4 | SkyworkAI/DeepResearchAgent | 3,479 | Multi-Agent | Hierarchical planning, self-evolution protocol |
| 5 | 199-biotechnologies/claude-deep-research-skill | 814 | Skill Framework | 8-phase pipeline, source credibility scoring |

---

## Main Analysis

### Finding 1: GPT-Researcher is the Most Mature and Widely-Adopted Deep Research Agent

GPT-Researcher (assafelovic/gpt-researcher) stands as the most established open-source deep research agent, with approximately 18K+ GitHub stars and a production-ready architecture. It aggregates over 20 sources per research task, supports multiple LLM providers (OpenAI, Anthropic, Google, local models), and generates detailed reports exceeding 2,000 words [1][2].

**Architecture:** Subagent-based parallel search with a main orchestrator that decomposes research queries, spawns parallel search subagents, aggregates findings, and synthesizes reports. The system maintains memory and context throughout the research process [1].

**Key Capabilities:**
- Multi-LLM support (OpenAI, Anthropic, Google Gemini, local models)
- JavaScript-enabled web scraping with smart image filtering
- AI-generated inline images via Google Gemini
- Export to PDF, Word, and other formats
- Production-ready frontend (NextJS + Tailwind)
- Memory and context persistence across research sessions [1][2]

**Evidence:** GPT-Researcher has been adopted by thousands of developers and enterprises, with active community contributions and regular updates. Its architecture has influenced numerous downstream research agent projects [1].

### Finding 2: Alibaba-NLP/DeepResearch Leads on Benchmarks with Custom Model Innovation

Alibaba-NLP/DeepResearch (Tongyi DeepResearch) is the highest-starred repository (19,606 stars) in the deep research category, but its approach is fundamentally different: it provides a custom-trained 30B-A3B parameter model specifically optimized for deep research tasks, rather than just a framework [3][4].

**Architecture:** The system combines a custom model trained via end-to-end reinforcement learning with two inference paradigms: ReAct for standard reasoning and an IterResearch-based "Heavy" mode that uses test-time scaling for maximum performance [3][4].

**Key Capabilities:**
- Fully automated synthetic data generation pipeline for agentic pre-training
- Large-scale continual pre-training on agentic interaction data
- End-to-end RL with Group Relative Policy Optimization
- ReAct + IterResearch "Heavy" mode for test-time scaling
- Available via OpenRouter for GPU-free inference [3][4]

**Evidence:** The model is competitive on the Deep Research Bench leaderboard and represents a model-level innovation rather than just a framework improvement. It is the only project in our shortlist that provides a custom-trained research model [3][4].

### Finding 3: LangChain Open Deep Research Offers the Best Configurability and Ecosystem Integration

LangChain's Open Deep Research (langchain-ai/open_deep_research) achieves a #6 ranking on the Deep Research Bench leaderboard with an overall score of 0.4344, demonstrating that a well-configurable framework can compete with custom-trained models [5][6].

**Architecture:** Built on LangGraph, it supports both single-agent and multi-agent (supervisor-researcher) configurations. The system is highly configurable across LLM providers, search tools, and MCP servers [5][6].

**Key Capabilities:**
- Wide LLM provider support via init_chat_model() API
- Multiple search tool backends (Tavily, native web search, MCP servers)
- LangSmith Studio integration for debugging and prompt tuning
- Both single-agent and multi-agent (legacy) implementations
- Deep Research Bench evaluation with 100 PhD-level tasks
- Full MCP (Model Context Protocol) compatibility [5][6]

**Evidence:** Ranked #6 on the Deep Research Bench leaderboard with a score of 0.4344. The project includes a free course on building deep research agents, demonstrating strong educational and community value [5][6].

### Finding 4: SkyworkAI/DeepResearchAgent Pioneers Self-Evolving Multi-Agent Architecture

SkyworkAI/DeepResearchAgent (3,479 stars) introduces a novel approach: a hierarchical multi-agent system with a self-evolution protocol that enables the agent framework to adapt and improve over time [7].

**Architecture:** A top-level planning agent coordinates multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse domains. The self-evolution protocol addresses lifecycle/context management, version tracking, and safe evolution update interfaces [7].

**Key Capabilities:**
- Hierarchical multi-agent coordination
- Self-evolution protocol for agent adaptation
- General-purpose task solving beyond research
- Automated task decomposition
- Cross-entity lifecycle and context management [7]

**Evidence:** The project addresses a critical gap in existing agent frameworks: the lack of standardized evolution interfaces. Its self-evolution protocol is unique among the top candidates and represents forward-looking architecture [7].

### Finding 5: claude-deep-research-skill Brings Enterprise-Grade Research to AI Coding Assistants

199-biotechnologies/claude-deep-research-skill (814 stars) represents the emerging "skill" category: research capabilities designed to enhance existing AI coding assistants rather than standalone systems [8].

**Architecture:** An 8-phase pipeline (SCOPE, PLAN, RETRIEVE, TRIANGULATE, OUTLINE REFINEMENT, SYNTHESIZE, REFINE, PACKAGE) with automated validation scripts, source credibility scoring, and McKinsey-style HTML report generation [8].

**Key Capabilities:**
- 8-phase research pipeline with quality gates
- Source credibility scoring (0-100)
- Automated citation verification (DOI/URL/hallucination checking)
- McKinsey-style HTML and PDF report generation
- 9-check structure validation
- Enterprise-grade architecture with modular scripts [8]

**Evidence:** The project claims to outperform OpenAI, Gemini, and Claude Desktop in quality and verification. Its modular architecture (separate scripts for citation management, source evaluation, report validation) represents a production-oriented approach to research skills [8].

---

## Top 5 Deep Research Skills Shortlist

### 1. GPT-Researcher (assafelovic/gpt-researcher)
**Rationale:** Most mature, widely adopted, production-ready. Multi-LLM support, 20+ source aggregation, comprehensive export options. The de facto standard for open-source deep research.

### 2. Alibaba-NLP/DeepResearch (Tongyi DeepResearch)
**Rationale:** Highest star count, custom-trained model, benchmark leader. Represents model-level innovation with RL-trained research capabilities. Unique in providing a dedicated research model.

### 3. LangChain Open Deep Research
**Rationale:** Best configurability, strongest ecosystem integration (LangChain/LangGraph), competitive benchmark performance (#6 on Deep Research Bench). Best for developers already in the LangChain ecosystem.

### 4. SkyworkAI/DeepResearchAgent
**Rationale:** Most innovative architecture with self-evolution protocol. Addresses critical gaps in agent lifecycle management. Forward-looking design for long-term agent adaptation.

### 5. 199-biotechnologies/claude-deep-research-skill
**Rationale:** Best skill-based implementation for AI coding assistants. Most rigorous quality gates and validation pipeline. Enterprise-oriented with automated verification.

---

## Side-by-Side Comparison Table

| Feature | GPT-Researcher | Alibaba DeepResearch | LangChain Open Deep Research | SkyworkAI DeepResearchAgent | claude-deep-research-skill |
|---------|---------------|---------------------|---------------------------|---------------------------|--------------------------|
| **GitHub Stars** | ~18K+ | 19,606 | ~5K+ | 3,479 | 814 |
| **Type** | Standalone Agent | Model + Agent | Framework Agent | Multi-Agent System | Skill Framework |
| **Language** | Python | Python | Python | Python | Python |
| **Multi-LLM Support** | ✅ (OpenAI, Anthropic, Google, local) | ❌ (Custom model) | ✅ (Universal via init_chat_model) | ❌ (Model-agnostic framework) | ✅ (Claude Code) |
| **Multi-Source Search** | ✅ (20+ sources) | ✅ (Built into model) | ✅ (Tavily, MCP, native) | ✅ (Configurable) | ✅ (Multi-provider) |
| **Agent Architecture** | Subagent parallel | ReAct / IterResearch | Single + Multi-agent | Hierarchical multi-agent | 8-phase pipeline |
| **Citation Tracking** | ✅ | ✅ | ✅ | ✅ | ✅ (DOI/URL verification) |
| **Report Generation** | ✅ (PDF, Word) | ✅ (Custom output) | ✅ (Configurable) | ✅ | ✅ (McKinsey HTML/PDF) |
| **Source Credibility** | Partial | Model-level | Configurable | Configurable | ✅ (0-100 scoring) |
| **Self-Evolution** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **MCP Support** | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Benchmark Score** | Not ranked | Top-tier | #6 (0.4344) | Not benchmarked | Not benchmarked |
| **Production Ready** | ✅ | ✅ | ✅ | Partial | ✅ |
| **Documentation** | Excellent | Good | Excellent | Good | Good |
| **Community** | Large | Growing | Large (LangChain) | Small | Small |
| **Unique Feature** | Most mature, multi-provider | Custom RL-trained model | LangGraph ecosystem | Self-evolution protocol | Enterprise validation |

---

## Final Ranking with Justification

### Rank 1: GPT-Researcher
**Justification:** Most mature and widely-adopted deep research agent. Its combination of multi-LLM support, 20+ source aggregation, production-ready frontend, and active community make it the most capable overall. The subagent architecture enables parallel research at scale, and its export capabilities (PDF, Word) make it immediately useful for real-world research tasks. It has the largest community and most documentation.

### Rank 2: Alibaba-NLP/DeepResearch
**Justification:** Highest star count reflects strong community interest. The custom-trained 30B-A3B model with end-to-end RL represents the most innovative approach to deep research. The IterResearch "Heavy" mode with test-time scaling pushes performance boundaries. However, it is less flexible than GPT-Researcher due to its reliance on a custom model.

### Rank 3: LangChain Open Deep Research
**Justification:** Best balance of configurability and performance. Ranked #6 on the Deep Research Bench with a score of 0.4344, demonstrating competitive quality. The LangGraph ecosystem and MCP support make it the most extensible option. Ideal for developers who want to customize and extend their research pipeline.

### Rank 4: SkyworkAI/DeepResearchAgent
**Justification:** Most innovative architecture with its self-evolution protocol. The hierarchical multi-agent system with lifecycle management addresses critical gaps in agent frameworks. While less mature than the top 3, its forward-looking design makes it the most capable for long-term, evolving research tasks.

### Rank 5: claude-deep-research-skill
**Justification:** Best skill-based implementation for enhancing AI coding assistants. The 8-phase pipeline with automated validation, source credibility scoring, and McKinsey-style report generation represents the most rigorous quality-focused approach. Ideal for teams using Claude Code who need enterprise-grade research capabilities.

---

## Sources/Bibliography

[1] assafelovic/gpt-researcher. GitHub repository. https://github.com/assafelovic/gpt-researcher. Accessed July 5, 2026.

[2] GPT-Researcher Features. https://github.com/assafelovic/gpt-researcher#features. Accessed July 5, 2026.

[3] Alibaba-NLP/DeepResearch. GitHub repository. https://github.com/Alibaba-NLP/DeepResearch. Accessed July 5, 2026.

[4] Alibaba DeepResearch Features. https://github.com/Alibaba-NLP/DeepResearch#features. Accessed July 5, 2026.

[5] langchain-ai/open_deep_research. GitHub repository. https://github.com/langchain-ai/open_deep_research. Accessed July 5, 2026.

[6] LangChain Open Deep Research README. https://raw.githubusercontent.com/langchain-ai/open_deep_research/main/README.md. Accessed July 5, 2026.

[7] SkyworkAI/DeepResearchAgent. GitHub repository. https://github.com/SkyworkAI/DeepResearchAgent. Accessed July 5, 2026.

[8] 199-biotechnologies/claude-deep-research-skill. GitHub repository. https://github.com/199-biotechnologies/claude-deep-research-skill. Accessed July 5, 2026.

[9] ai-agents-2030/awesome-deep-research-agent. GitHub repository. https://github.com/ai-agents-2030/awesome-deep-research-agent. Accessed July 5, 2026.

[10] Top 20 GitHub Repositories for AI Agents in 2026. Fungies.io. https://fungies.io/top-github-repositories-ai-agent-frameworks-2026/. Accessed July 5, 2026.

[11] Deep Research Bench Leaderboard. Hugging Face. https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard. Accessed July 5, 2026.

[12] standardhuman/deep-research-skill. GitHub repository. https://github.com/standardhuman/deep-research-skill. Accessed July 5, 2026.

---

## Methodology Appendix

### Research Design
- **Mode:** Ultradeep (8-phase pipeline)
- **Phases Executed:** SCOPE → PLAN → RETRIEVE → TRIANGULATE → OUTLINE REFINEMENT → SYNTHESIZE → CRITIQUE → REFINE → PACKAGE
- **Search Strategy:** 10+ query variants across GitHub API (gh CLI), GitHub web search, and DuckDuckGo
- **Parallel Execution:** 5 concurrent command batches, 4-6 concurrent URL fetches
- **Source Diversity:** GitHub repos, README files, blog posts, comparison articles, benchmark leaderboards

### Search Queries Used
1. "deep research agent" (GitHub repos + web)
2. "deep-research skill" (GitHub repos + web)
3. "AI research agent" (GitHub repos)
4. "multi-source research" (GitHub repos)
5. "citation tracking research" (GitHub repos)
6. "agentic research pipeline" (GitHub repos)
7. "GPT research" (GitHub repos)
8. "research assistant agent" (GitHub repos)
9. "perplexity clone" (GitHub repos + web)
10. "open deep research" (GitHub repos)
11. "deep research benchmark" (GitHub repos)
12. "awesome deep research" (GitHub repos)
13. "LangChain research agent" (GitHub repos)
14. "browser use research agent" (GitHub repos)
15. "tavily research agent" (GitHub repos)
16. "langgraph research" (GitHub repos)

### Selection Criteria
- **GitHub Stars:** Minimum 500+ for shortlist consideration
- **Feature Richness:** Multi-source search, citation tracking, report generation
- **Architecture:** Agent-based, multi-agent, or pipeline-based research system
- **Community:** Active maintenance, documentation, community adoption
- **Uniqueness:** Distinct approach or capability not found in other candidates

### Limitations
- Star counts are approximate and may have changed since data collection
- Some repositories may have private or restricted features not visible in public READMEs
- Benchmark scores are self-reported and may not reflect all use cases
- The "skill" category (claude-deep-research-skill) is newer and less battle-tested than standalone agents
