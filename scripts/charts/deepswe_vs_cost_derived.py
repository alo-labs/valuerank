import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "artifacts" / "charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# DeepSWE token data per task (from extracted page data)
# Format: (agent_label, deepswe_reward, input_tokens, cache_write_tokens, cache_read_tokens, output_tokens, model_slug)
# Source: AA dataset (token counts available)
deep_swe_data = [
    ("Claude Code - Fable 5 (max)", 0.6608, 2882482, 1492465, 0, 238348, "claude-fable-5"),
    ("Claude Code - Opus 4.8 (max)", 0.5575, 2952438, 1374227, 0, 172540, "claude-opus-4-8"),
    ("Claude Code - Opus 4.8 (medium)", 0.4926, 2573893, 1012210, 0, 101529, "claude-opus-4-8"),
    ("Codex - GPT-5.5 (xhigh)", 0.6431, 4432420, None, None, 58037, "gpt-5-5"),
    ("Codex - GPT-5.5 (medium)", 0.5664, 3102171, None, None, 24316, "gpt-5-5"),
    ("Claude Code - Opus 4.7 (max)", 0.4012, 3168915, 1532932, 0, 117585, "claude-opus-4-7"),
    ("Opencode - Opus 4.7 (medium)", 0.3953, 2741621, 1024505, 0, 87481, "claude-opus-4-7"),
    ("Cursor CLI - GPT-5.5 (medium)", 0.3717, 3665129, None, None, 103390, "gpt-5-5"),
    ("Cursor CLI - Opus 4.7 (medium)", 0.3156, 2683041, 994739, 0, 54416, "claude-opus-4-7"),
    ("Claude Code - Sonnet 4.6 (medium)", 0.2891, 3349626, 1705652, 0, 118018, "claude-sonnet-4-6"),
    ("Claude Code - GLM-5.2", 0.2861, 2407627, 0, 0, 42222, "glm-5-2"),
    ("Claude Code - Opus 4.7 (medium)", 0.2743, 3168915, 1532932, 0, 117585, "claude-opus-4-7"),
    ("Claude Code - Qwen3.7 Plus (thinking)", 0.1917, 2654779, 1131149, 0, 29130, "qwen3-7-plus"),
    ("Claude Code - GLM-5.1", 0.1858, 3107875, 735057, 0, 110836, "glm-5-1"),
    ("Claude Code - Kimi K2.6", 0.1652, 1860507, 0, 0, 74079, "kimi-k2-6"),
    ("Cursor CLI - Composer 2.5", 0.1593, 1873649, 965924, 0, 15039, "composer-2-5"),
    ("Cursor CLI - Composer 2.5 Fast", 0.1593, 1873649, 965924, 0, 15039, "composer-2-5-fast"),
    ("Gemini CLI - Gemini 3.1 Pro (high)", 0.1416, 3722760, None, None, 13927, "gemini-3-1-pro"),
    ("Claude Code - DeepSeek V4 Pro (high)", 0.0855, 1678390, 131760, 0, 14869, "deepseek-v4-pro"),
]

# DeepSWE v1 models MISSING from AA dataset (score + avg cost from DeepSWE page)
# Source: https://deepswe.datacurve.ai/blog/deepswe (v1, May 26, 2026)
# Note: Token counts not available; using avg cost directly
deepswe_v1_only = [
    ("Codex - GPT-5.4 (xhigh)", 0.56, 5.65, "gpt-5-4"),
    ("Gemini CLI - Gemini 3.5 Flash (medium)", 0.28, 7.34, "gemini-3-5-flash"),
    ("Codex - GPT-5.4 Mini (xhigh)", 0.24, 2.82, "gpt-5-4-mini"),
    ("Claude Code - MiMo V2.5 Pro", 0.19, 2.82, "mimo-v2-5-pro"),
    ("Gemini CLI - Gemini 3 Flash", 0.05, 0.60, "gemini-3-flash"),
]

# ALL DeepSWE official models (v1 + v1.1) for diamond markers
# Source: https://deepswe.datacurve.ai/ leaderboard + blog
deepswe_official_all = [
    # v1.1 models (from leaderboard, June 24, 2026)
    ("DeepSWE: Fable 5 [max]", 0.70, 21.63, "claude-fable-5"),
    ("DeepSWE: GPT-5.5 [xhigh]", 0.67, 7.23, "gpt-5-5"),
    ("DeepSWE: Opus 4.8 [max]", 0.59, 13.22, "claude-opus-4-8"),
    ("DeepSWE: GPT-5.4 [xhigh]", 0.52, 5.65, "gpt-5-4"),
    ("DeepSWE: GLM-5.2 [max]", 0.44, 3.92, "glm-5-2"),
    ("DeepSWE: Gemini 3.5 Flash [med]", 0.37, 7.34, "gemini-3-5-flash"),
    ("DeepSWE: Kimi K2.7 Code", 0.31, 2.82, "kimi-k2-7"),
    ("DeepSWE: Sonnet 4.6 [high]", 0.30, 5.52, "claude-sonnet-4-6"),
    ("DeepSWE: Gemini 3.1 Pro [high]", 0.12, 9.48, "gemini-3-1-pro"),
    # v1 models (from blog, May 26, 2026)
    ("DeepSWE v1: GPT-5.5 [xhigh]", 0.70, 21.63, "gpt-5-5"),
    ("DeepSWE v1: GPT-5.4 [xhigh]", 0.56, 5.65, "gpt-5-4"),
    ("DeepSWE v1: Opus 4.7 [max]", 0.54, 13.22, "claude-opus-4-7"),
    ("DeepSWE v1: Sonnet 4.6 [high]", 0.32, 5.52, "claude-sonnet-4-6"),
    ("DeepSWE v1: Gemini 3.5 Flash [med]", 0.28, 7.34, "gemini-3-5-flash"),
    ("DeepSWE v1: GPT-5.4 Mini [xhigh]", 0.24, 2.82, "gpt-5-4-mini"),
    ("DeepSWE v1: Kimi K2.6", 0.24, 2.82, "kimi-k2-6"),
    ("DeepSWE v1: MiMo V2.5 Pro", 0.19, 2.82, "mimo-v2-5-pro"),
    ("DeepSWE v1: GLM-5.1", 0.18, 0.60, "glm-5-1"),
    ("DeepSWE v1: Gemini 3.1 Pro", 0.10, 9.48, "gemini-3-1-pro"),
    ("DeepSWE v1: DeepSeek V4 Pro", 0.08, 0.60, "deepseek-v4-pro"),
    ("DeepSWE v1: Gemini 3 Flash", 0.05, 0.60, "gemini-3-flash"),
]

# Official API pricing per MTok (USD) - as of July 2026
# For Anthropic: cache write = 1.25x input, cache read = 0.1x input
# For OpenAI: no separate cache pricing in data
# For DeepSeek: cache hit = 0.1x input
# For Cursor Composer: Standard and Fast tiers with separate cache_hit pricing
model_pricing = {
    "claude-fable-5": {"input": 10.0, "cache_write": 12.5, "cache_hit": 1.0, "output": 50.0},       # Verified: Anthropic official
    "claude-opus-4-8": {"input": 5.0, "cache_write": 6.25, "cache_hit": 0.50, "output": 25.0},     # Verified: Anthropic official
    "claude-opus-4-7": {"input": 5.0, "cache_write": 6.25, "cache_hit": 0.50, "output": 25.0},     # Verified: Anthropic official
    "claude-sonnet-4-6": {"input": 3.0, "cache_write": 3.75, "cache_hit": 0.30, "output": 15.0},   # Verified: Anthropic official
    "gpt-5-5": {"input": 5.0, "cache_write": 5.0, "cache_hit": 0.50, "output": 30.0},              # Verified: OpenAI official
    "gpt-5-4": {"input": 2.50, "cache_write": 2.50, "cache_hit": 0.25, "output": 15.0},           # Verified: OpenRouter
    "gpt-5-4-mini": {"input": 0.75, "cache_write": 0.75, "cache_hit": 0.075, "output": 4.50},     # Verified: OpenRouter
    "glm-5-2": {"input": 1.40, "cache_write": 1.40, "cache_hit": 0.26, "output": 4.40},           # Verified: OpenRouter + multiple sources
    "glm-5-1": {"input": 1.40, "cache_write": 1.40, "cache_hit": 0.26, "output": 4.40},           # Verified: AA model page
    "qwen3-7-plus": {"input": 0.40, "cache_write": 0.04, "cache_hit": 0.08, "output": 1.16},      # Verified: AA model page
    "kimi-k2-6": {"input": 0.95, "cache_write": 0.95, "cache_hit": 0.16, "output": 4.00},         # Verified: Moonshot official + multiple sources
    "deepseek-v4-pro": {"input": 0.435, "cache_write": 0.435, "cache_hit": 0.003625, "output": 0.87},  # Verified: DeepSeek official
    "gemini-3-1-pro": {"input": 2.00, "cache_write": 2.00, "cache_hit": 0.20, "output": 12.00},    # Verified: Google official (≤200k prompts)
    "gemini-3-5-flash": {"input": 1.50, "cache_write": 1.50, "cache_hit": 0.15, "output": 9.00},   # Verified: Google AI Studio
    "gemini-3-flash": {"input": 0.15, "cache_write": 0.15, "cache_hit": 0.01875, "output": 0.60},  # Verified: Google AI Studio
    "mimo-v2-5-pro": {"input": 0.435, "cache_write": 0.435, "cache_hit": 0.0435, "output": 0.87},  # Verified: OpenRouter
    "composer-2-5": {"input": 0.50, "cache_write": 0.50, "cache_hit": 0.20, "output": 2.50},       # Verified: Cursor docs + multiple sources
    "composer-2-5-fast": {"input": 3.00, "cache_write": 3.00, "cache_hit": 0.35, "output": 15.0},  # Verified: Cursor docs + multiple sources
}

# Calculate DeepSWE-specific cost for each agent
results = []

# Process AA dataset models (cost derived from token counts)
for label, reward, input_tok, cache_write, cache_read, output_tok, model in deep_swe_data:
    pricing = model_pricing.get(model)
    if not pricing:
        continue

    # Convert per MTok to per token
    input_price = pricing["input"] / 1_000_000
    cache_write_price = pricing["cache_write"] / 1_000_000
    cache_hit_price = pricing["cache_hit"] / 1_000_000
    output_price = pricing["output"] / 1_000_000

    # Cost = input × input_price + cache_write × cache_write_price + cache_read × cache_hit_price + output × output_price
    cost = (input_tok * input_price +
            (cache_write or 0) * cache_write_price +
            (cache_read or 0) * cache_hit_price +
            output_tok * output_price)

    results.append({
        "label": label,
        "reward": reward,
        "cost": cost,
        "model": model,
        "source": "AA (derived)",
    })

# Process DeepSWE v1-only models (cost from DeepSWE page directly)
for label, reward, avg_cost, model in deepswe_v1_only:
    results.append({
        "label": label,
        "reward": reward,
        "cost": avg_cost,
        "model": model,
        "source": "DeepSWE v1 (avg cost)",
    })

# Process ALL DeepSWE official models (for diamond markers)
deepswe_results = []
for label, reward, avg_cost, model in deepswe_official_all:
    deepswe_results.append({
        "label": label,
        "reward": reward,
        "cost": avg_cost,
        "model": model,
    })

# Color mapping by provider
provider_colors = {
    "claude": "#6B46C1",  # Purple
    "gpt": "#2563EB",     # Blue
    "cursor": "#059669",  # Green
    "opencode": "#DC2626",  # Red
    "gemini": "#D97706",  # Amber
    "glm": "#059669",     # Green (Z.ai)
    "qwen": "#0891B2",    # Cyan (Alibaba)
    "kimi": "#C026D3",    # Fuchsia (Moonshot)
    "deepseek": "#16A34A",  # Green (DeepSeek)
}

def get_provider(model):
    if model.startswith("claude"):
        return "Claude Code"
    elif model.startswith("gpt"):
        return "Codex/OpenAI"
    elif model.startswith("glm"):
        return "GLM (Z.ai)"
    elif model.startswith("qwen"):
        return "Qwen (Alibaba)"
    elif model.startswith("kimi"):
        return "Kimi (Moonshot)"
    elif model.startswith("deepseek"):
        return "DeepSeek"
    elif model.startswith("gemini"):
        return "Gemini (Google)"
    else:
        return "Other"

def get_color(model):
    if model.startswith("claude"):
        return "#6B46C1"
    elif model.startswith("gpt"):
        return "#2563EB"
    elif model.startswith("glm"):
        return "#059669"
    elif model.startswith("qwen"):
        return "#0891B2"
    elif model.startswith("kimi"):
        return "#C026D3"
    elif model.startswith("deepseek"):
        return "#16A34A"
    elif model.startswith("gemini"):
        return "#D97706"
    elif model.startswith("mimo"):
        return "#F59E0B"  # Amber for Xiaomi
    else:
        return "#888888"

labels = [r["label"] for r in results]
scores = [r["reward"] * 100 for r in results]  # Convert to percentage
costs = [r["cost"] for r in results]
colors = [get_color(r["model"]) for r in results]

# DeepSWE official data
deepswe_labels = [r["label"] for r in deepswe_results]
deepswe_scores = [r["reward"] * 100 for r in deepswe_results]
deepswe_costs = [r["cost"] for r in deepswe_results]
deepswe_colors = [get_color(r["model"]) for r in deepswe_results]

fig, ax = plt.subplots(figsize=(14, 9))

# Scatter plot with log x-axis - AA dataset (circles)
for i, (label, score, cost, color) in enumerate(zip(labels, scores, costs, colors)):
    ax.scatter(cost, score, c=color, s=120, zorder=5, edgecolors='white', linewidths=0.8, marker='o')

# Scatter plot - DeepSWE official (diamonds)
for i, (label, score, cost, color) in enumerate(zip(deepswe_labels, deepswe_scores, deepswe_costs, deepswe_colors)):
    ax.scatter(cost, score, c=color, s=100, zorder=4, edgecolors='white', linewidths=0.8, marker='D', alpha=0.7)

# Annotate points
for i, (label, score, cost) in enumerate(zip(labels, scores, costs)):
    # Offset annotations to reduce overlap
    x_offset = 0
    y_offset = 1.2
    ha = 'center'

    # Adjust offsets for overlapping points
    if "Composer 2.5" in label and "Fast" not in label:
        y_offset = -2.5
    if "Kimi" in label:
        y_offset = -2.5
    if "DeepSeek" in label:
        y_offset = -2.5
    if "Sonnet" in label:
        y_offset = -2.5
    if "Opus 4.7 (medium)" in label and "Opencode" not in label and "Cursor" not in label:
        y_offset = 3.5
    if "GLM-5.2" in label:
        x_offset = 0.1
        y_offset = 2.0
    if "GLM-5.1" in label:
        y_offset = -2.5
    # New v1-only models
    if "GPT-5.4 (xhigh)" in label:
        y_offset = 2.0
    if "Gemini 3.5 Flash" in label:
        y_offset = -2.5
    if "GPT-5.4 Mini" in label:
        y_offset = 2.0
    if "MiMo" in label:
        y_offset = -2.5
    if "Gemini 3 Flash" in label:
        y_offset = 2.0

    ax.annotate(label.split("\n")[0],
                (cost, score),
                textcoords="offset points",
                xytext=(x_offset * 40, y_offset * 4),
                fontsize=7.5,
                ha=ha,
                alpha=0.85,
                arrowprops=dict(arrowstyle='-', color='gray', alpha=0.3, lw=0.5) if abs(y_offset) > 2 else None)

ax.set_xscale('log')
ax.invert_xaxis()

# Format x-axis as dollar amounts
def dollar_formatter(x, pos):
    if x >= 1:
        return f'${x:.0f}'
    elif x >= 0.1:
        return f'${x:.2f}'
    elif x >= 0.01:
        return f'${x:.3f}'
    else:
        return f'${x:.4f}'

ax.xaxis.set_major_formatter(ticker.FuncFormatter(dollar_formatter))
ax.set_xticks([0.01, 0.05, 0.1, 0.5, 1, 2, 5, 10, 20])
ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())

ax.set_xlabel('DeepSWE Cost per Task (USD, log scale) - Derived from Token Counts', fontsize=12, fontweight='bold')
ax.set_ylabel('DeepSWE Benchmark Score (pass@1 %)', fontsize=12, fontweight='bold')
ax.set_title('Artificial Analysis Coding Agent: DeepSWE Performance vs. Derived Cost',
             fontsize=14, fontweight='bold', pad=15)

ax.grid(True, alpha=0.3, which='both')
ax.set_axisbelow(True)

# Legend
from matplotlib.lines import Line2D
legend_providers = [
    ("Claude Code", "#6B46C1"),
    ("Codex/OpenAI", "#2563EB"),
    ("Cursor Composer", "#059669"),
    ("GLM (Z.ai)", "#059669"),
    ("Qwen (Alibaba)", "#0891B2"),
    ("Kimi (Moonshot)", "#C026D3"),
    ("DeepSeek", "#16A34A"),
    ("Gemini (Google)", "#D97706"),
    ("MiMo (Xiaomi)", "#F59E0B"),
]
legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                          markersize=10, label=provider)
                   for provider, color in legend_providers]
# Add marker style legend
legend_elements.append(Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',
                              markersize=10, label='AA dataset'))
legend_elements.append(Line2D([0], [0], marker='D', color='w', markerfacecolor='gray',
                              markersize=10, label='DeepSWE official (v1+v1.1)'))
ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
          framealpha=0.9, edgecolor='gray')

# Add note about data sources
ax.text(0.98, 0.02, "Cost derived from official API token pricing\nAA models: token counts × pricing\nDeepSWE v1-only: avg cost from DeepSWE page",
        transform=ax.transAxes, fontsize=8, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

# Add quadrant reference lines
ax.axhline(y=30, color='gray', linestyle='--', alpha=0.25, linewidth=0.8)
ax.axvline(x=10, color='gray', linestyle='--', alpha=0.25, linewidth=0.8)
ax.text(0.99, 63, '← Lower Cost', fontsize=8, color='gray', alpha=0.6, ha='right')
ax.text(0.01, 63, 'Higher Cost →', fontsize=8, color='gray', alpha=0.6, ha='left')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'deepswe_vs_derived_cost.png', dpi=150, bbox_inches='tight')
plt.savefig(OUTPUT_DIR / 'deepswe_vs_derived_cost.pdf', bbox_inches='tight')

# Print summary table
print("\n=== DeepSWE Cost Summary ===\n")
print(f"{'Agent':<45} {'Score':>8} {'Cost':>10} {'Source':<20}")
print("-" * 85)
for r in sorted(results, key=lambda x: -x["reward"]):
    print(f"{r['label']:<45} {r['reward']*100:>7.1f}% ${r['cost']:>8.2f} {r['source']:<20}")

print(f"\nChart saved to {OUTPUT_DIR / 'deepswe_vs_derived_cost.png'} and {OUTPUT_DIR / 'deepswe_vs_derived_cost.pdf'}")
print(f"Total models: {len(results)} ({len(deep_swe_data)} from AA + {len(deepswe_v1_only)} from DeepSWE v1)")
