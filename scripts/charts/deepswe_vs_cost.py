import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "artifacts" / "charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Data: Agent, DeepSWE Score, Total Cost (USD)
data = [
    ("Claude Code - Fable 5 (max)\n(fallback)", 0.6608, 11.75),
    ("Codex - GPT-5.5 (xhigh)", 0.6431, 5.07),
    ("Codex - GPT-5.5 (medium)", 0.5664, 2.75),
    ("Claude Code - Opus 4.8 (max)", 0.5575, 7.70),
    ("Claude Code - Opus 4.8 (medium)", 0.4926, 3.26),
    ("Claude Code - Opus 4.7 (max)", 0.4012, 5.64),
    ("Opencode - Opus 4.7 (medium)", 0.3953, 2.93),
    ("Cursor CLI - GPT-5.5 (medium)", 0.3717, 2.01),
    ("Cursor CLI - Opus 4.7 (medium)", 0.3156, 2.68),
    ("Claude Code - Sonnet 4.6 (medium)", 0.2891, 1.97),
    ("Claude Code - GLM-5.2", 0.2861, 6.47),
    ("Claude Code - Opus 4.7 (medium)", 0.2743, 1.68),
    ("Claude Code - Qwen3.7 Plus\n(thinking)", 0.1917, 6.23),
    ("Claude Code - GLM-5.1", 0.1858, 4.33),
    ("Claude Code - Kimi K2.6", 0.1652, 1.18),
    ("Cursor CLI - Composer 2.5", 0.1593, 0.08),
    ("Cursor CLI - Composer 2.5 Fast", 0.1593, 0.55),
    ("Gemini CLI - Gemini 3.1 Pro\n(high)", 0.1416, 2.00),
    ("Claude Code - DeepSeek V4 Pro\n(high)", 0.0855, 0.27),
]

# Color mapping by provider
provider_colors = {
    "Claude Code": "#6B46C1",  # Purple
    "Codex": "#2563EB",        # Blue
    "Cursor CLI": "#059669",   # Green
    "Opencode": "#DC2626",     # Red
    "Gemini CLI": "#D97706",   # Amber
}

def get_provider(name):
    for key in provider_colors:
        if key in name:
            return key
    return "Other"

labels = [d[0] for d in data]
scores = [d[1] * 100 for d in data]  # Convert to percentage
costs = [d[2] for d in data]
colors = [provider_colors.get(get_provider(l), "#888") for l in labels]

fig, ax = plt.subplots(figsize=(14, 9))

# Scatter plot with log x-axis
for i, (label, score, cost, color) in enumerate(zip(labels, scores, costs, colors)):
    ax.scatter(cost, score, c=color, s=120, zorder=5, edgecolors='white', linewidths=0.8)

# Annotate points
for i, (label, score, cost) in enumerate(zip(labels, scores, costs)):
    # Offset annotations to reduce overlap
    x_offset = 0
    y_offset = 1.2
    ha = 'center'

    # Adjust offsets for overlapping points
    if "Composer 2.5" == label.split("\n")[0].strip()[-9:]:
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

    ax.annotate(label.split("\n")[0],
                (cost, score),
                textcoords="offset points",
                xytext=(x_offset * 40, y_offset * 4),
                fontsize=7.5,
                ha=ha,
                alpha=0.85,
                arrowprops=dict(arrowstyle='-', color='gray', alpha=0.3, lw=0.5) if abs(y_offset) > 2 else None)

ax.set_xscale('log')

# Format x-axis as dollar amounts
def dollar_formatter(x, pos):
    if x >= 1:
        return f'${x:.0f}'
    elif x >= 0.1:
        return f'${x:.2f}'
    else:
        return f'${x:.2f}'

ax.xaxis.set_major_formatter(ticker.FuncFormatter(dollar_formatter))
ax.set_xticks([0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 15])
ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())

ax.set_xlabel('Mean Total Cost per Task (USD, log scale)', fontsize=12, fontweight='bold')
ax.set_ylabel('DeepSWE Benchmark Score (pass@1 %)', fontsize=12, fontweight='bold')
ax.set_title('Artificial Analysis Coding Agent: DeepSWE Performance vs. Total Cost',
             fontsize=14, fontweight='bold', pad=15)

ax.grid(True, alpha=0.3, which='both')
ax.set_axisbelow(True)

# Legend
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                          markersize=10, label=provider)
                   for provider, color in provider_colors.items()]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
          framealpha=0.9, edgecolor='gray')

# Add quadrant reference lines
ax.axhline(y=30, color='gray', linestyle='--', alpha=0.25, linewidth=0.8)
ax.axvline(x=3, color='gray', linestyle='--', alpha=0.25, linewidth=0.8)
ax.text(0.06, 63, '← Lower Cost', fontsize=8, color='gray', alpha=0.6)
ax.text(12, 63, 'Higher Cost →', fontsize=8, color='gray', alpha=0.6, ha='right')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'deepswe_vs_total_cost.png', dpi=150, bbox_inches='tight')
plt.savefig(OUTPUT_DIR / 'deepswe_vs_total_cost.pdf', bbox_inches='tight')
print(f"Chart saved to {OUTPUT_DIR / 'deepswe_vs_total_cost.png'} and {OUTPUT_DIR / 'deepswe_vs_total_cost.pdf'}")
