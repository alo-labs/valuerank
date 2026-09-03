# Dispatch Mechanics — multi-ai-deep-research

How to actually launch N parallel LLM processes for deep research. The mechanism depends on your harness, not the task type.

---

## The 4 dispatch mechanisms (in order of preference)

### Mechanism 1: Native `task` tool with pre-configured subagent types (preferred-if-available)

If your harness supports custom subagent types via `task(subagent_type="my-agent", prompt="...")`, use it. Set up the agents in your config first:

```jsonc
// ~/.config/opencode/opencode.jsonc
{
  "agent": {
    "ocg-minimax-m3": { "mode": "subagent", "model": "opencode-go/minimax-m3" },
    "ocg-qwen3.7-max": { "mode": "subagent", "model": "opencode-go/qwen3.7-max" }
  },
  "permission": {
    "task": { "ocg-*": "allow" }
  }
}
```

Then in your session: `task(subagent_type="ocg-minimax-m3", description="deep-research", prompt="...")`.

**Important constraint (as of 2026-06):** The `task` tool's `Parameters` schema does **not** include a `model` field. The model is resolved at *config time*, not at call time. To multi-model fan out, the user must pre-define one subagent_type per model in `opencode.json`.

**Host-config caveat:** Some OpenCode harnesses restrict the `task` tool's `subagent_type` enum to defaults like `["explore", "general"]`. If you see `Unknown agent type: ocg-...`, your harness's `permission.task` allow-list is too narrow — widen it or use Mechanism 2.

### Mechanism 2: `opencode run --model <provider/model>` (default)

When the `task` tool rejects custom subagent types, or when you want a no-config-fan-out, dispatch each model as a primary `build` agent with a `--model` flag:

```bash
OUT=./.runs/multi-ai-deep-research/$(date +%Y%m%d-%H%M%S)
mkdir -p "$OUT"

MODE="ultradeep"  # or from --mode argument
RESEARCH_QUESTION="<user's question>"

# Create the deep-research prompt for each model
PROMPT="You are a deep-research agent. Follow the deep-research skill methodology.

FIRST: Read the deep-research skill files:
- /Users/shafqat/.agents/skills/deep-research/SKILL.md
- /Users/shafqat/.agents/skills/deep-research/reference/methodology.md

MODE: ${MODE}

RESEARCH QUESTION: ${RESEARCH_QUESTION}

Follow the 8-phase pipeline (SCOPE, PLAN, RETRIEVE, TRIANGULATE, OUTLINE REFINEMENT, SYNTHESIZE, CRITIQUE, REFINE, PACKAGE) in ${MODE} mode.

Write your findings to: ${OUT}/<model-slug>-report.md

Output contract:
- Executive Summary
- Main Analysis with cited findings
- Sources/Bibliography (complete)
- Methodology Appendix"

# Dispatch to each model in parallel
for model in opencode-go/minimax-m3 opencode-go/qwen3.7-plus opencode-go/deepseek-v4-flash; do
  slug=$(echo "$model" | cut -d/ -f2)
  npx -y opencode-ai run \
    --model "$model" \
    --title "deep-research-${slug}" \
    --dangerously-skip-permissions \
    "$PROMPT" \
    > "$OUT/${slug}.md" 2> "$OUT/${slug}.err" &
done

wait
echo "Outputs in $OUT/"
```

**Notes:**
- `$slug` sanitizes the model name so filenames don't contain slashes
- `--y` in `npx -y opencode-ai run` skips the install prompt
- `--dangerously-skip-permissions` is fine for **read-only** research tasks
- **Timeout:** set explicit `timeout` on bash tool (e.g., 900000ms for 15 min per model)
- Check the model's CWD for stray `*.md` files after dispatch

### Mechanism 3: HTTP SDK with `client.session.promptAsync()`

If you have an OpenCode server running, use the SDK:

```javascript
const sessions = await Promise.all(models.map(async (m) => {
  const session = await client.session.create({ agent: "build" });
  await client.session.promptAsync({
    path: { id: session.id },
    body: { model: { providerID: m.provider, modelID: m.model }, parts: [{ type: "text", text: prompt }] }
  });
  return { model: m, session: session.id };
}));
```

**Known bug (2026-06):** Issue #18615 reports that even with explicit `model` and `agent` in the body, OpenCode may override them with the agent's built-in fallback chain. Workaround: pass model on the server side via config, or use Mechanism 2.

### Mechanism 4: Direct HTTP to provider API

Skip the OpenCode layer entirely; call each provider's API directly with the same prompt. Highest control, but you lose MCP access and have to manage auth per provider.

---

## Parallel vs sequential dispatch

| Mode | Pros | Cons | When to use |
|------|------|------|-------------|
| **Parallel** (concurrent processes) | Fastest wall-time = `max(per_model_time)` | MCP port collision if multiple share a port; harder to debug | Independent tasks; no shared state; sub-5-min per model |
| **Sequential** (one at a time) | Predictable; no port issues; clean logs | Slowest wall-time = `N × per_model_time` | Long-running tasks (10+ min each); shared MCPs |

**Recommended default:** parallel for research tasks (each model runs independently, no shared state). Sequential if you hit MCP port collisions.

---

## Auth / credentials

Each model needs API credentials. The auth model varies by harness:

| Harness | Auth mechanism |
|---------|----------------|
| OpenCode Go (`opencode-go/*`) | `opencode auth login` (cached locally on first use) |
| Anthropic (`anthropic/*`) | `ANTHROPIC_API_KEY` env var |
| OpenAI (`openai/*`) | `OPENAI_API_KEY` env var |
| Google (`google/*`) | `GOOGLE_API_KEY` env var |
| Local Ollama | no auth, just `http://localhost:11434/v1` |

Run `opencode providers` to see configured providers and their auth status.

---

## Choosing the right mechanism

| If you have... | Use... |
|----------------|--------|
| OpenCode harness with `task` tool that accepts custom subagent_types AND you've pre-defined them in `opencode.json` | Mechanism 1 |
| OpenCode harness but `task` tool rejects custom types OR you want zero-config fan-out | Mechanism 2 |
| An OpenCode server running (`opencode serve`) | Mechanism 3 |
| A different harness entirely (supported hosts with no OpenCode) | Mechanism 4 |
| Multiple MCPs that share ports | Mechanism 2 sequential |
| Time-critical interactive session (<5 min budget for total run) | Mechanism 2 parallel |
| Models from different providers (e.g., OpenAI + Anthropic + local) | Mechanism 4 for cross-provider coverage |
