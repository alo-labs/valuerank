# Artificial Analysis total-cost frontier capture

Observed on 2026-10-08 through the Codex built-in browser at [Artificial Analysis models](https://artificialanalysis.ai/models?total-cost=intelligence-vs-total-cost).

The chart selected was **Intelligence Index vs. Total Cost**, under the Cost section. Its title was **Intelligence Index vs. Cost to Run Artificial Analysis Intelligence Index**. The x-axis and tooltips said **Cost to Run Intelligence Index (USD, Log Scale)**. The chart still measures total cost to run the Intelligence Index, despite the site's default comparison and summary charts now featuring weighted cost per task. These values must not be relabelled as cost per task.

After the public model-selector action **Select all**, the selector displayed **691 of 691 models**. The resulting total-cost SVG contained **173 plotted model circles**. Its rendered Pareto path contained **14 vertices**. Each vertex was matched to a rendered circle within 0.001 pixels, then hovered using browser mouse input. The visible tooltip supplied the exact variant name, two-decimal USD cost, and rounded integer Intelligence Index score. Public rendered model anchors supplied the exact links. The capture did not read embedded page payloads or use direct HTTP fetching.

## Current frontier

| Order | Public model name | Total cost (USD) | Intelligence Index displayed |
| --- | --- | ---: | ---: |
| 1 | GPT-6 Luna (low) | 10.63 | 22 |
| 2 | GPT-6 Luna (medium) | 31.17 | 30 |
| 3 | GPT-6 Luna (high) | 47.85 | 33 |
| 4 | GPT-6 Luna (xhigh) | 66.81 | 35 |
| 5 | MiMo-V2.6-Flash | 109.41 | 38 |
| 6 | GPT-6 Luna (max) | 122.05 | 38 |
| 7 | MiMo-V2.6-Pro | 206.66 | 46 |
| 8 | GPT-6.1 Sol (medium) | 361.37 | 48 |
| 9 | GPT-6.1 Sol (high) | 521.32 | 50 |
| 10 | GPT-6.1 Sol (xhigh) | 662.28 | 51 |
| 11 | GPT-6.1 Sol (max) | 1,081.55 | 52 |
| 12 | Claude Opus 5.5 (high with fallback) | 2,172.43 | 54 |
| 13 | Claude Opus 5.5 (xhigh with fallback) | 4,056.65 | 56 |
| 14 | Claude Opus 5.5 (max with fallback) | 8,708.20 | 58 |

The 14 public names match the prior 2026-10-07 inventory named in the task assignment. This establishes unchanged frontier membership; it does not establish that all earlier raw metric values are unchanged.

The frontier represents **five model families**, with **14 configurations**: GPT-6 Luna (five effort settings), MiMo-V2.6-Flash, MiMo-V2.6-Pro, GPT-6.1 Sol (four effort settings), and Claude Opus 5.5 (three effort settings, each with fallback). A ValueRank inclusion delta must compare exact variants against the site's current model records; an additional effort setting is not a newly introduced model family.

## Precision and evidence limits

Intelligence Index numbers in this capture are the rounded integers displayed by the chart tooltip. MiMo-V2.6-Flash and GPT-6 Luna (max) both display 38, while the public Pareto path places GPT-6 Luna (max) higher; this follows the chart owner's rendered frontier and is not a Pareto reconstruction using the rounded values. The JSON preserves the path, matched circle IDs, and SVG coordinates to make that distinction explicit.

Only the 173 models with both plotted coordinates contribute visible chart points. Selecting 691 catalog entries does not imply 691 cost/index measurements. Intelligence Index v4.3.2 remains the version stated in the page's Intelligence Index description.

The current ValueRank mapping and source-builder edits belong to other agents. This capture makes no claim that those edits or production inclusion are complete.
