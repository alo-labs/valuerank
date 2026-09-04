#!/usr/bin/env python3
"""Fetch and normalize the pinned official LiveBench release for ValueRank.

The release is pinned deliberately: LiveBench is a moving leaderboard, while a
ValueRank publication needs a reproducible snapshot.  The script keeps the
official task rows and cost-per-successful-task values for the current DeepSWE
cohort, derives the published category/overall means, and records hashes for
the fetched source files.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
RELEASE = "2026_06_25"
BASE_URL = "https://livebench.ai"
URLS = {
    "table": f"{BASE_URL}/table_{RELEASE}.csv",
    "cost": f"{BASE_URL}/cost_{RELEASE}.csv",
    "categories": f"{BASE_URL}/categories_{RELEASE}.json",
}

# LiveBench uses "IF" in the release JSON; the publication uses the full
# label so the field is self-explanatory outside the source repository.
CATEGORY_LABELS = {
    "Reasoning": "Reasoning",
    "Coding": "Coding",
    "Agentic Coding": "Agentic Coding",
    "Mathematics": "Mathematics",
    "Data Analysis": "Data Analysis",
    "Language": "Language",
    "IF": "Instruction Following",
}

COHORT_MAP = {
    "gpt-6-astra": None,
    "gemini-3.8-flash": "gemini-3.8-flash-high",
    "claude-opus-5": "claude-opus-5-max-effort",
    "gpt-5.6-sol": "gpt-5.6-sol-max",
    "claude-fable-5": "claude-fable-5-max-effort",
    "glm-5.3": "glm-5.3",
    "kimi-k3": "kimi-k3",
    "grok-4.6": "grok-4.6",
    "gpt-5.6-luna": "gpt-5.6-luna-max",
    "gpt-5.5": "gpt-5.5-xhigh",
    "gemini-3.7-flash": "gemini-3.7-flash-high",
    "glm-5.3-flash": "glm-5.3-flash",
    "deepseek-v4-pro": "deepseek-v4-pro",
    "claude-opus-4.8": "claude-opus-4-8-max-effort",
    "qwen3.8-max": "qwen3.8-max",
    "muse-spark-1.2": "muse-spark-1.2-xhigh",
    "claude-sonnet-5": "claude-sonnet-5-xhigh-effort",
    "deepseek-v4-flash": "deepseek-v4-flash",
    "gemini-3.6-flash": "gemini-3.6-flash-high",
    "glm-5.2": "glm-5.2",
    "gemini-3.5-flash": "gemini-3.5-flash-high",
}


def fetch(url: str) -> tuple[bytes, dict[str, str]]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ValueRank/1.4 official-source-refresh"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read()
        return payload, {
            "url": url,
            "status": str(response.status),
            "contentType": response.headers.get("Content-Type", ""),
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        }


def number(value, label: str) -> float | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text or text.lower() in {"n/a", "na", "null", "-", "—"}:
        return None
    for token in ("$", "%"):
        text = text.replace(token, "")
    try:
        parsed = float(text)
    except ValueError as exc:
        raise ValueError(f"non-numeric LiveBench value for {label}: {value!r}") from exc
    if not math.isfinite(parsed):
        raise ValueError(f"non-finite LiveBench value for {label}")
    return parsed


def mean(values: list[float], label: str) -> float:
    if not values:
        raise ValueError(f"empty LiveBench category: {label}")
    if any(not math.isfinite(value) for value in values):
        raise ValueError(f"non-finite LiveBench category: {label}")
    return round(sum(values) / len(values), 6)


def pareto_ids(rows: dict[str, dict]) -> list[str]:
    usable = [
        row for row in rows.values()
        if row.get("matched") and row.get("overallScore") is not None and row.get("costPerSuccessfulTaskUsd") is not None
    ]
    frontier = []
    for row in usable:
        dominated = any(
            other["modelId"] != row["modelId"]
            and other["costPerSuccessfulTaskUsd"] <= row["costPerSuccessfulTaskUsd"]
            and other["overallScore"] >= row["overallScore"]
            and (
                other["costPerSuccessfulTaskUsd"] < row["costPerSuccessfulTaskUsd"]
                or other["overallScore"] > row["overallScore"]
            )
            for other in usable
        )
        if not dominated:
            frontier.append(row)
    return [row["modelId"] for row in sorted(frontier, key=lambda row: row["costPerSuccessfulTaskUsd"])]


def main() -> int:
    deepswe = json.loads((REFRESH / "deepswe.json").read_text())
    cohort = [(item["slug"], item["displayName"]) for item in deepswe["models"]]
    if len(cohort) != 21:
        raise ValueError("LiveBench mapping expects the complete 21-model DeepSWE cohort")
    if set(COHORT_MAP) != {model_id for model_id, _ in cohort}:
        raise ValueError("LiveBench cohort mapping does not exactly match DeepSWE v1.4")

    table_bytes, table_source = fetch(URLS["table"])
    cost_bytes, cost_source = fetch(URLS["cost"])
    category_bytes, category_source = fetch(URLS["categories"])
    table_rows = list(csv.DictReader(io.StringIO(table_bytes.decode("utf-8-sig"))))
    cost_rows = list(csv.DictReader(io.StringIO(cost_bytes.decode("utf-8-sig"))))
    categories_source = json.loads(category_bytes)
    if not table_rows or not cost_rows:
        raise ValueError("LiveBench source files returned no rows")
    expected_categories = set(CATEGORY_LABELS)
    if set(categories_source) != expected_categories:
        raise ValueError(f"unexpected LiveBench categories: {sorted(categories_source)}")
    task_categories = {
        CATEGORY_LABELS[key]: list(tasks) for key, tasks in categories_source.items()
    }
    expected_tasks = {task for tasks in task_categories.values() for task in tasks}
    missing_tasks = expected_tasks - set(table_rows[0])
    if missing_tasks:
        raise ValueError(f"LiveBench table is missing tasks: {sorted(missing_tasks)}")
    cost_key = "cost_per_successful_task"
    if cost_key not in cost_rows[0]:
        raise ValueError(f"LiveBench cost file is missing {cost_key}")
    table_by_model = {row.get("model"): row for row in table_rows}
    cost_by_model = {row.get("model"): row for row in cost_rows}
    if None in table_by_model or None in cost_by_model:
        raise ValueError("LiveBench source contains an empty model key")

    models: dict[str, dict] = {}
    missing_models = []
    for model_id, display_name in cohort:
        livebench_model = COHORT_MAP[model_id]
        table_row = table_by_model.get(livebench_model) if livebench_model else None
        cost_row = cost_by_model.get(livebench_model) if livebench_model else None
        record = {
            "modelId": model_id,
            "name": display_name,
            "livebenchModel": livebench_model,
            "matched": bool(table_row and cost_row),
            "tasks": {},
            "categoryScores": {},
            "overallScore": None,
            "instructionFollowingScore": None,
            "costPerSuccessfulTaskUsd": None,
        }
        if not record["matched"]:
            missing_models.append(display_name)
            models[model_id] = record
            continue
        for task in sorted(expected_tasks):
            record["tasks"][task] = number(table_row.get(task), f"{model_id}.{task}")
        for category, tasks in task_categories.items():
            values = [record["tasks"].get(task) for task in tasks]
            if any(value is None for value in values):
                raise ValueError(f"incomplete LiveBench category for {model_id}: {category}")
            record["categoryScores"][category] = mean(values, f"{model_id}.{category}")
        record["overallScore"] = mean(list(record["categoryScores"].values()), f"{model_id}.overall")
        record["instructionFollowingScore"] = record["categoryScores"]["Instruction Following"]
        record["costPerSuccessfulTaskUsd"] = number(
            cost_row[cost_key], f"{model_id}.{cost_key}"
        )
        if record["costPerSuccessfulTaskUsd"] is None or record["costPerSuccessfulTaskUsd"] <= 0:
            raise ValueError(f"missing/non-positive LiveBench cost for {model_id}")
        models[model_id] = record

    if len(missing_models) != 1 or missing_models != ["GPT-6 Astra"]:
        raise ValueError(f"unexpected LiveBench cohort coverage: {missing_models}")
    observed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    document = {
        "schemaVersion": "valuerank-livebench-v1",
        "release": RELEASE,
        "observedAt": observed_at,
        "source": {
            "publisher": "LiveBench",
            "homepage": BASE_URL + "/",
            "repository": "https://github.com/livebench/new-livebench",
            "releaseDate": "2026-06-25",
            "urls": URLS,
            "files": {
                "table": table_source,
                "cost": cost_source,
                "categories": category_source,
            },
        },
        "categories": task_categories,
        "cohortN": len(cohort),
        "matchedN": len(cohort) - len(missing_models),
        "missingModels": missing_models,
        "models": models,
    }
    document["pareto"] = pareto_ids(models)
    (REFRESH / "livebench.json").write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "release": RELEASE,
        "cohortN": document["cohortN"],
        "matchedN": document["matchedN"],
        "missingModels": document["missingModels"],
        "pareto": document["pareto"],
        "output": ".refresh/v1.4/livebench.json",
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
