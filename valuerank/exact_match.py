"""Exact-configuration matching for independently executed leaves (Terminal-Bench 4.0, Bug Hunt).

AGENTS.md forbids transferring results between reasoning efforts or model
versions. A leaf value counts for a ranked configuration only when the
evaluated model is the same model and its effort is the configuration's effort.

AA labels most configurations with an effort. A few reasoning models have a
single unlabeled reasoning mode on AA; for those the evaluated setting that is
documented as that same mode (the verified effort ceiling, or the thinking
toggle switched on) is recorded here as an explicit equivalence with its
evidence, never inferred.
"""

from __future__ import annotations

import re

# Evaluated settings equivalent to AA's single unlabeled reasoning mode, with the evidence.
EFFORT_EQUIVALENTS = {
    "qwen3.8-max": ({"max"}, "AA lists one reasoning mode; Bug Hunt records max as the verified effort ceiling"),
    "mimo-v2-6-pro": ({"enabled"}, "AA lists one reasoning mode; Bug Hunt records the verified binary thinking toggle"),
    "mimo-v2-6-flash": ({"enabled"}, "AA lists one reasoning mode; thinking toggle switched on"),
}

# tbench.ai leaderboard base names (effort removed) mapped to ValueRank model ids. O33: a family ranked at several
# efforts names every configuration; the effort match below still picks only the row for the configuration's own effort.
TB4_BASE_NAMES = {
    "Opus 5.5": "claude-opus-5-5",
    "Sonnet 5.5": ("claude-sonnet-5-5", "claude-sonnet-5-5-xhigh", "claude-sonnet-5-5-high", "claude-sonnet-5-5-medium", "claude-sonnet-5-5-low"),
    "Haiku 5.5": ("claude-haiku-5-5", "claude-haiku-5-5-max", "claude-haiku-5-5-high", "claude-haiku-5-5-medium", "claude-haiku-5-5-low"),
    "Opus 5": "claude-opus-5",
    "Sonnet 5": "claude-sonnet-5",
    "Opus 4.8": "claude-opus-4.8",
    "Fable 5": "claude-fable-5",
    "Fable 5.1": "claude-fable-5-1",
    "GPT-6 Astra": "gpt-6-astra",
    "GPT-6.1 Sol": ("gpt-6.1-sol", "gpt-6.1-sol-xhigh", "gpt-6.1-sol-high", "gpt-6.1-sol-medium", "gpt-6.1-sol-low"),
    "GPT-6 Sol": "gpt-6-sol",
    "GPT-6 Luna": "gpt-6-luna",
    "GPT-5.6 Sol": "gpt-5.6-sol",
    "GPT-5.6 Luna": "gpt-5.6-luna",
    "GPT-5.5": "gpt-5.5",
    "GLM-5.3": "glm-5.3",
    "GLM-5.3-Flash": "glm-5.3-flash",
    "Grok 4.7": "grok-4.7",
    "Grok 4.6": ("grok-4.6", "grok-4.6-xhigh"),
    "Gemini 4 Argon": "gemini-4-argon",
    "Gemini 3.8 Flash": "gemini-3.8-flash",
    "Gemini 3.7 Flash": "gemini-3.7-flash",
    "Qwen3.8-Max-0902": "qwen3.8-max",
    "Kimi K3": "kimi-k3",
    "DeepSeek V4 Pro": "deepseek-v4-pro",
    "DeepSeek V4 Flash": "deepseek-v4-flash",
    "Muse Spark 1.3": ("muse-spark-1-3", "muse-spark-1-3-xhigh"),
}

# Pre-registered agent preference: vendor-neutral harnesses first, never best-of-agent.
TB4_AGENT_PREFERENCE = ("Terminus 2", "mini-SWE-agent", "OpenHands")

EFFORT_SUFFIX = re.compile(r"^(?P<base>.*?)\s+\((?P<effort>[^()]*)\)$")


def tb4_model_ids(base: str) -> tuple[str, ...]:
    """The ValueRank configurations a tbench.ai base name can belong to (one, or a family ranked at several efforts)."""

    ids = TB4_BASE_NAMES.get(base, ())
    return (ids,) if isinstance(ids, str) else ids


def split_effort(name: str) -> tuple[str, str | None]:
    """'Opus 5.5 (max)' -> ('Opus 5.5', 'max'); a name without a parenthesised suffix has no effort."""

    match = EFFORT_SUFFIX.match(name.strip())
    if not match:
        return name.strip(), None
    return match.group("base").strip(), match.group("effort").strip().casefold()


def efforts_match(model_id: str, configuration_effort: str | None, evaluated_effort: str | None) -> bool:
    """True when the evaluated effort is the ranked configuration's effort (or its documented equivalent)."""

    evaluated = (evaluated_effort or "").casefold() or None
    if configuration_effort is not None:
        return evaluated == configuration_effort.casefold()
    if evaluated is None:
        return True  # both unlabeled: the same single-mode configuration on both sides
    equivalents, _evidence = EFFORT_EQUIVALENTS.get(model_id, (set(), ""))
    return evaluated in equivalents


def select_tb4_row(model_id: str, configuration_effort: str | None, rows: list[dict]) -> dict | None:
    """The tbench.ai row for this exact configuration, chosen by the pre-registered agent preference."""

    candidates = []
    for row in rows:
        base, effort = split_effort(row["model"])
        if model_id in tb4_model_ids(base) and efforts_match(model_id, configuration_effort, effort):
            candidates.append(row)
    if not candidates:
        return None

    def preference(row):
        agent = row.get("agent") or ""
        rank = TB4_AGENT_PREFERENCE.index(agent) if agent in TB4_AGENT_PREFERENCE else len(TB4_AGENT_PREFERENCE)
        return rank, agent

    return min(candidates, key=preference)


def bug_hunt_matches(model_id: str, configuration_effort: str | None, record: dict | None) -> bool:
    """A Bug Hunt record counts only when the owner matched it and its effort is the configuration's effort."""

    if not record or record.get("matched") is not True or record.get("fixedOf105") is None:
        return False
    return efforts_match(model_id, configuration_effort, record.get("effort"))
