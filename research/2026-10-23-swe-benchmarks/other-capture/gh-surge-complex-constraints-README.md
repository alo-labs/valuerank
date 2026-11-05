# ComplexConstraints Harness

This repo is an eval harness for the [ComplexConstraints benchmark](https://surgehq.ai/blog/complexconstraints-a-benchmark-for-entangled-instruction-following),
published by [Surge AI](https://www.surgehq.ai).

The full dataset is published on [HuggingFace](https://huggingface.co/datasets/surgeai/ComplexConstraints):
75 expert-crafted prompts (`CIF-001`–`CIF-075`), each paired with 10–40 rubric
criteria (1,559 total). You can use this harness to run ComplexConstraints on
your own models, or to reproduce the published
[leaderboard](https://surgehq.ai/benchmarks/complex-constraints).

## Running An Eval

This harness is a `uv` package, built with the [Inspect AI](https://inspect.aisi.org.uk) framework.

To run an eval: set your provider API keys, then run an `inspect eval` command:

```bash
# can also set these in `.env` (copy `.env.example`)
export ANTHROPIC_API_KEY=...
export OPENAI_API_KEY=...
export GEMINI_API_KEY=...

# evaluate all 75 tasks
uv run inspect eval src/complex_constraints/task.py --model anthropic/claude-opus-4-8

# pick the judge, cap tasks, and raise concurrency
uv run inspect eval src/complex_constraints/task.py \
  --model anthropic/claude-opus-4-20250514 \
  -T judge_model=google/gemini-3.5-flash \
  -T limit=10 \
  --max-connections 8
```

The model answers each prompt in a single completion (no tools, no agent), and
an LLM judge then grades each rubric criterion independently — it sees only the
response and one criterion at a time.

The scorer reports two metrics per model: `all_pass/mean` (every rubric
criterion satisfied — the leaderboard-style task pass rate) and
`mean_criteria/mean` (average fraction of criteria satisfied per response).

Useful Inspect flags:

- `--epochs N` — runs each task N times for variance
- `--limit N` — caps the number of tasks
- `inspect eval-retry` — resumes a failed run
- `inspect view` — opens the log viewer with full per-sample transcripts

Inspect infers model capabilities from the model name, so a model served under a nonstandard name (through a proxy, say) can silently lose them: `--reasoning-effort` stops mapping to Gemini's `thinkingConfig.thinkingLevel` and the run still looks fine. Pass `-T model_family=gemini-3-pro` (or `-T judge_model_family=...`) to tell Inspect what the model actually is.

## Pass@K / Pass^K

Run multiple epochs with Inspect's score reducers to compute Pass@K and Pass^K in the same run:

```bash
uv run inspect eval src/complex_constraints/task.py --model ... \
  --epochs 5 --epochs-reducer "mean,pass_at_5,at_least_5"
```

This reports, per metric key: `all_pass/mean` (Pass@1), `all_pass/pass_at_5` (Pass@5, the unbiased [Codex-paper estimator](https://arxiv.org/pdf/2107.03374)), and `all_pass/at_least_5` (Pass^5, all 5 runs pass).

## Offline single-task check

To smoke-test without keys, run the task against a local pack with Inspect's
mock model (no network, no judge calls):

```bash
# Inspect chdirs into the task file's directory, so pass task_pack as an
# absolute path ($PWD expands before the CLI runs).
uv run inspect eval src/complex_constraints/task.py \
  -T task_pack="$PWD/task_packs/sample" \
  --model mockllm/model -T judge_model=mockllm/model
```

The committed `task_packs/sample/` holds two synthetic placeholder tasks, with differing rubric counts to exercise the loader.

Structural tests (no network/keys) run via:

```bash
uv run python tests/test_offline.py
```
