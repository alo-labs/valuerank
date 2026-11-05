---
configs:
- config_name: agent
  data_files:
  - split: latest
    path: agent/latest-*
  - split: full
    path: agent/full-*
  default: true
- config_name: agent_bash_recovery_steps
  data_files:
  - split: latest
    path: agent_bash_recovery_steps/latest-*
  - split: full
    path: agent_bash_recovery_steps/full-*
- config_name: agent_bash_reliability
  data_files:
  - split: latest
    path: agent_bash_reliability/latest-*
  - split: full
    path: agent_bash_reliability/full-*
- config_name: agent_bash_reliability_no_prereq
  data_files:
  - split: latest
    path: agent_bash_reliability_no_prereq/latest-*
  - split: full
    path: agent_bash_reliability_no_prereq/full-*
- config_name: agent_praise_complaint
  data_files:
  - split: latest
    path: agent_praise_complaint/latest-*
  - split: full
    path: agent_praise_complaint/full-*
- config_name: agent_steerability
  data_files:
  - split: latest
    path: agent_steerability/latest-*
  - split: full
    path: agent_steerability/full-*
- config_name: agent_task_outcome_explicit
  data_files:
  - split: latest
    path: agent_task_outcome_explicit/latest-*
  - split: full
    path: agent_task_outcome_explicit/full-*
- config_name: agent_tool_hallucination
  data_files:
  - split: latest
    path: agent_tool_hallucination/latest-*
  - split: full
    path: agent_tool_hallucination/full-*
- config_name: document
  data_files:
  - split: latest
    path: document/latest-*
  - split: full
    path: document/full-*
- config_name: document_style_control
  data_files:
  - split: latest
    path: document_style_control/latest-*
  - split: full
    path: document_style_control/full-*
- config_name: image_edit
  data_files:
  - split: latest
    path: image_edit/latest-*
  - split: full
    path: image_edit/full-*
- config_name: image_to_video
  data_files:
  - split: latest
    path: image_to_video/latest-*
  - split: full
    path: image_to_video/full-*
- config_name: search
  data_files:
  - split: latest
    path: search/latest-*
  - split: full
    path: search/full-*
- config_name: search_factuality
  data_files:
  - split: latest
    path: search_factuality/latest-*
  - split: full
    path: search_factuality/full-*
- config_name: search_style_control
  data_files:
  - split: latest
    path: search_style_control/latest-*
  - split: full
    path: search_style_control/full-*
- config_name: text
  data_files:
  - split: latest
    path: text/latest-*
  - split: full
    path: text/full-*
- config_name: text_factuality
  data_files:
  - split: latest
    path: text_factuality/latest-*
  - split: full
    path: text_factuality/full-*
- config_name: text_style_control
  data_files:
  - split: latest
    path: text_style_control/latest-*
  - split: full
    path: text_style_control/full-*
- config_name: text_to_image
  data_files:
  - split: latest
    path: text_to_image/latest-*
  - split: full
    path: text_to_image/full-*
- config_name: text_to_video
  data_files:
  - split: latest
    path: text_to_video/latest-*
  - split: full
    path: text_to_video/full-*
- config_name: video_edit
  data_files:
  - split: latest
    path: video_edit/latest-*
  - split: full
    path: video_edit/full-*
- config_name: vision
  data_files:
  - split: latest
    path: vision/latest-*
  - split: full
    path: vision/full-*
- config_name: vision_style_control
  data_files:
  - split: latest
    path: vision_style_control/latest-*
  - split: full
    path: vision_style_control/full-*
- config_name: webdev
  data_files:
  - split: latest
    path: webdev/latest-*
  - split: full
    path: webdev/full-*
license: cc-by-4.0
dataset_info:
- config_name: agent
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: float64
  - name: session_count
    dtype: float64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 6262
    num_examples: 53
  - name: full
    num_bytes: 224234
    num_examples: 1899
  download_size: 98531
  dataset_size: 230496
- config_name: agent_bash_recovery_steps
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: float64
  - name: session_count
    dtype: float64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 6139
    num_examples: 52
  - name: full
    num_bytes: 186670
    num_examples: 1582
  download_size: 73895
  dataset_size: 192809
- config_name: agent_bash_reliability
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: int64
  - name: session_count
    dtype: 'null'
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5838
    num_examples: 53
  - name: full
    num_bytes: 34868
    num_examples: 317
  download_size: 25358
  dataset_size: 40706
- config_name: agent_bash_reliability_no_prereq
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: int64
  - name: session_count
    dtype: 'null'
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5937
    num_examples: 54
  - name: full
    num_bytes: 17473
    num_examples: 159
  download_size: 19348
  dataset_size: 23410
- config_name: agent_praise_complaint
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: float64
  - name: session_count
    dtype: float64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 6269
    num_examples: 53
  - name: full
    num_bytes: 224234
    num_examples: 1899
  download_size: 84804
  dataset_size: 230503
- config_name: agent_steerability
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: float64
  - name: session_count
    dtype: float64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 6269
    num_examples: 53
  - name: full
    num_bytes: 224234
    num_examples: 1899
  download_size: 85893
  dataset_size: 230503
- config_name: agent_task_outcome_explicit
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: float64
  - name: session_count
    dtype: float64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 6269
    num_examples: 53
  - name: full
    num_bytes: 224234
    num_examples: 1899
  download_size: 85427
  dataset_size: 230503
- config_name: agent_tool_hallucination
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: score
    dtype: float64
  - name: score_ci_lower
    dtype: float64
  - name: score_ci_upper
    dtype: float64
  - name: observation_count
    dtype: float64
  - name: session_count
    dtype: float64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 6269
    num_examples: 53
  - name: full
    num_bytes: 224234
    num_examples: 1899
  download_size: 86234
  dataset_size: 230503
- config_name: document
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5229
    num_examples: 44
  - name: full
    num_bytes: 55204
    num_examples: 464
  download_size: 32149
  dataset_size: 60433
- config_name: document_style_control
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5229
    num_examples: 44
  - name: full
    num_bytes: 55204
    num_examples: 464
  download_size: 32111
  dataset_size: 60433
- config_name: image_edit
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 13252
    num_examples: 105
  - name: full
    num_bytes: 346547
    num_examples: 2786
  download_size: 144698
  dataset_size: 359799
- config_name: image_to_video
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5660
    num_examples: 48
  - name: full
    num_bytes: 167717
    num_examples: 1436
  download_size: 75110
  dataset_size: 173377
- config_name: search
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5061
    num_examples: 42
  - name: full
    num_bytes: 92468
    num_examples: 764
  download_size: 46564
  dataset_size: 97529
- config_name: search_factuality
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 4824
    num_examples: 40
  - name: full
    num_bytes: 15964
    num_examples: 132
  download_size: 18471
  dataset_size: 20788
- config_name: search_style_control
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5061
    num_examples: 42
  - name: full
    num_bytes: 92468
    num_examples: 764
  download_size: 46548
  dataset_size: 97529
- config_name: text
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: float64
  - name: rank
    dtype: float64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 1459526
    num_examples: 11099
  - name: full
    num_bytes: 159622478
    num_examples: 1223700
  download_size: 61926624
  dataset_size: 161082004
- config_name: text_factuality
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 526845
    num_examples: 3999
  - name: full
    num_bytes: 12181802
    num_examples: 92932
  download_size: 4588770
  dataset_size: 12708647
- config_name: text_style_control
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: float64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 1459526
    num_examples: 11099
  - name: full
    num_bytes: 141155799
    num_examples: 1082110
  download_size: 55448037
  dataset_size: 142615325
- config_name: text_to_image
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 83952
    num_examples: 680
  - name: full
    num_bytes: 2514693
    num_examples: 20387
  download_size: 992361
  dataset_size: 2598645
- config_name: text_to_video
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 5601
    num_examples: 48
  - name: full
    num_bytes: 151162
    num_examples: 1311
  download_size: 71414
  dataset_size: 156763
- config_name: video_edit
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 1209
    num_examples: 10
  - name: full
    num_bytes: 7537
    num_examples: 63
  download_size: 13125
  dataset_size: 8746
- config_name: vision
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 140550
    num_examples: 1142
  - name: full
    num_bytes: 5996120
    num_examples: 48970
  download_size: 2248081
  dataset_size: 6136670
- config_name: vision_style_control
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 140550
    num_examples: 1142
  - name: full
    num_bytes: 5411225
    num_examples: 44146
  download_size: 2074398
  dataset_size: 5551775
- config_name: webdev
  features:
  - name: model_name
    dtype: string
  - name: organization
    dtype: string
  - name: license
    dtype: string
  - name: rating
    dtype: float64
  - name: rating_lower
    dtype: float64
  - name: rating_upper
    dtype: float64
  - name: variance
    dtype: float64
  - name: vote_count
    dtype: int64
  - name: rank
    dtype: int64
  - name: category
    dtype: string
  - name: leaderboard_publish_date
    dtype: string
  splits:
  - name: latest
    num_bytes: 78974
    num_examples: 643
  - name: full
    num_bytes: 3614606
    num_examples: 29808
  download_size: 1393669
  dataset_size: 3693580
---

# Arena Leaderboard Dataset

Historical snapshots of the [Arena](https://arena.ai/leaderboard) leaderboard.

## Usage

```python
from datasets import load_dataset

# Load all historical text style control data
ds = load_dataset("lmarena-ai/leaderboard-dataset", "text_style_control", split="full")

# Load the current text style control leaderboard
ds = load_dataset("lmarena-ai/leaderboard-dataset", "text_style_control", split="latest")

# Filter to overall category
ds = load_dataset("lmarena-ai/leaderboard-dataset", "text_style_control", split="latest",
    filters=[("category", "==", "overall")]
)

# Track a specific model's rating over time
ds = load_dataset("lmarena-ai/leaderboard-dataset", "text_style_control", split="full",
    filters=[("category", "==", "overall"), ("model_name", "==", "gpt-4o-2024-05-13")],
    columns=["model_name", "rating", "rank", "leaderboard_publish_date"]
)

# Load raw (non-style-controlled) text ratings
ds = load_dataset("lmarena-ai/leaderboard-dataset", "text", split="full")

# Load the current Agent Arena leaderboard
ds = load_dataset("lmarena-ai/leaderboard-dataset", "agent", split="latest")
```

## Subsets

Each arena is a separate subset, arenas with style control have an additional subset with a `_style_control` suffix .

- `text`, `text_style_control`
- `vision`, `vision_style_control`
- `search`, `search_style_control`
- `document`, `document_style_control`
- `webdev` (Code Arena)
- `text_to_image`
- `image_edit`
- `text_to_video`
- `image_to_video`
- `video_edit`
- `agent` (Agent Arena aggregate), plus per-signal subsets: `agent_bash_recovery_steps`, `agent_praise_complaint`, `agent_steerability`, `agent_task_outcome_explicit`, `agent_tool_hallucination`

## Splits

- `full`: All historically published leaderboards
- `latest`: Only the most recently published leaderboards


## Notes

- On January 9, 2024, the rating system was updated from Elo to [Bradley-Terry](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model).
- On May 16, 2025, style control was made the default for text and vision arenas and the offset was adjusted to put the style control leaderboard on the same rating scale as non style control.
- On July 23, 2025, frequency-based re-weighting was implemented.
- Search and Webdev Arena data starts from their releases on the arena.ai (then lmarena.ai) on August 7 and November 12 2025 respectively. 
- Agent Arena data starts from its release on June 4, 2026.

For a complete record of all leaderboard methodology changes, see the [Leaderboard Changelog](https://arena.ai/blog/leaderboard-changelog/).

## Schema

| Column | Type | Description |
|--------|------|-------------|
| model_name | string | Model identifier |
| organization | string | Model creator/organization |
| license | string | Model license |
| rating | float | Arena Score |
| rating_lower | float | Lower confidence bound |
| rating_upper | float | Upper confidence bound |
| variance | float | Rating variance |
| vote_count | int | Number of battles for this model |
| rank | int | Rank within this leaderboard |
| category | string | Leaderboard category (e.g., overall, coding, math) |
| leaderboard_publish_date | string | Date that this score was published (`YYYY-MM-DD`) |

Agent Arena subsets use [IPS scores](https://arena.ai/blog/agent-arena-methodology/) instead of Bradley-Terry:

| Column | Type | Description |
|--------|------|-------------|
| model_name | string | Model identifier |
| organization | string | Model creator/organization |
| license | string | Model license |
| score | float | IPS score (τ̂) |
| score_ci_lower | float | Lower 95% confidence bound |
| score_ci_upper | float | Upper 95% confidence bound |
| observation_count | int | Signal observations for this model |
| session_count | int | Distinct sessions (aggregate subset only) |
| rank | int | Rank within this leaderboard |
| category | string | Leaderboard category |
| leaderboard_publish_date | string | Date that this score was published (`YYYY-MM-DD`) |