# Deep Research Skills: Capability Analysis and Ranking

**Model:** deepseek-v4-flash
**Research Date:** 2026-07-05
**Mode:** UltraDeep

---

## Executive Summary

This report evaluates and ranks the most capable open-source deep research agents on GitHub (July 2026). From 30+ candidates across systematic GitHub search and README analysis, we shortlisted 5 top-tier tools evaluated across 12 feature dimensions, community health metrics, benchmark performance, and architectural sophistication.

**GPT Researcher (28K⭐)** ranks #1 overall — most feature-complete with multi-agent support (LangGraph + AG2), MCP server/client, export to PDF/Word/MD/HTML, inline AI image generation, and 3,000+ commits. **STORM (29.8K⭐)** leads in academic rigor (NAACL 2024, EMNLP 2024) with a 4-module pipeline and 10+ search engine integrations. **Alibaba DeepResearch (19.6K⭐)** achieves SOTA benchmarks via RL-trained models and dual-mode inference (ReAct + IterResearch). **langchain-ai/open_deep_research (11.9K⭐)** offers the most flexible MCP-native architecture. **dzhng/deep-research (19.3K⭐)** provides the simplest TypeScript implementation for rapid prototyping.

---

## Top 5 Shortlist

| Rank | Tool | Stars | Language | Key Strength |
|------|------|-------|----------|-------------|
| 1 | **GPT Researcher** | 28.1K | Python | Feature completeness, maturity, multi-agent, MCP |
| 2 | **STORM** | 29.8K | Python | Academic rigor, modularity, methodology |
| 3 | **Alibaba DeepResearch** | 19.6K | Python | SOTA benchmarks, RL-trained models |
| 4 | **langchain/open_deep_research** | 11.9K | Python | LangGraph flexibility, MCP-native |
| 5 | **dzhng/deep-research** | 19.3K | TypeScript | Simplicity, easy deploy |

## Side-by-Side Comparison

| Feature | GPT Researcher | STORM | Alibaba DR | langchain/odr | dzhng/dr |
|---------|---------------|-------|-----------|--------------|---------|
| Multi-LLM | ✅ Any | ✅ litellm | ✅ OpenRouter | ✅ LangChain | ✅ Custom |
| Search Engines | ✅ Web+local | ✅ 10+ engines | ✅ WebAgent | ✅ Tavily+MCP | ✅ SERP |
| Multi-Agent | ✅ LangGraph+AG2 | ✅ Co-STORM | ✅ Agent family | ✅ LangGraph | ❌ |
| MCP | ✅ Both | ❌ | ❌ | ✅ Full | ❌ |
| Web UI | ✅ NextJS | ✅ Streamlit | ✅ ModelScope | ✅ LangGraph Studio | ❌ CLI |
| Export | PDF, Word, MD, Docx, HTML | MD | JSON/JSONL | MD | MD |
| Image Gen | ✅ Gemini | ❌ | ❌ | ❌ | ❌ |
| Local RAG | ✅ | ✅ VectorRM | ❌ | ❌ | ❌ |
| Iterative Deep | ✅ Planner/Exec | ✅ Multi-perspective | ✅ ReAct+IterResearch | ✅ Agent loop | ✅ Breadth/Depth |
| Docker | ✅ | ✅ | ✅ | ✅ | ✅ |
| Benchmarks | Partial | ✅ FreshWiki | ✅ GAIA, BrowseComp, HLE | ✅ DR Bench | ❌ |
| Academic Paper | ❌ (inspired) | ✅ NAACL+EMNLP 2024 | ✅ 18+ papers | ✅ Blog | ❌ |
| Commits | 3,005 | 238 | 300 | 216 | 77 |
| Community | ✅ Discord | ❌ | ❌ | ✅ LangChain | ❌ |

## Final Ranking

1. **GPT Researcher (92/100)** — Best overall. Unmatched feature completeness, maturity, and integration ecosystem.
2. **STORM (85/100)** — Best structured reports. Uniquely validated methodology with modular architecture.
3. **Alibaba DeepResearch (82/100)** — Best benchmarks. RL-trained SOTA but highest barrier to entry.
4. **langchain/open_deep_research (78/100)** — Most flexible. MCP-native LangGraph architecture, strong for ecosystem users.
5. **dzhng/deep-research (65/100)** — Best for prototyping. Simplest codebase but most limited feature set.

---

## Sources

1. https://github.com/assafelovic/gpt-researcher
2. https://github.com/stanford-oval/storm
3. https://github.com/Alibaba-NLP/DeepResearch
4. https://github.com/dzhng/deep-research
5. https://github.com/langchain-ai/open_deep_research
6. https://github.com/MiroMindAI/MiroThinker
7. https://docs.gptr.dev/
8. https://arxiv.org/abs/2402.14207 (STORM, NAACL 2024)
9. https://www.arxiv.org/abs/2408.15232 (Co-STORM, EMNLP 2024)
10. https://blog.langchain.dev/open-deep-research/
11. https://github.com/assafelovic/gptr-mcp
12. https://github.com/mshumer/OpenDeepResearcher
13. https://github.com/SkyworkAI/DeepResearchAgent
14. https://github.com/webfuse-com/awesome-autoresearch
15. https://github.com/ai-agents-2030/awesome-deep-research-agent
16. https://github.com/khoj-ai/khoj
17. https://arxiv.org/pdf/2603.15726 (MiroThinker)
18. https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard

## Methodology

8-phase ultra-deep pipeline: SCOPE → PLAN → RETRIEVE (gh CLI + curl + ctx_fetch_and_index) → TRIANGULATE → OUTLINE REFINEMENT → SYNTHESIZE → CRITIQUE → REFINE → PACKAGE. 20 sources indexed, 34 evidence items persisted, 34 claims verified.
