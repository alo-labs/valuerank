from __future__ import annotations

from inspect_ai import Task, task
from inspect_ai.model import ModelInfo, get_model, set_model_info
from inspect_ai.solver import generate

from complex_constraints.dataset import load_samples
from complex_constraints.scorer import rubric_scorer

DEFAULT_HF_REPO = "surgeai/ComplexConstraints"
DEFAULT_JUDGE_MODEL = "google/gemini-3.5-flash"


def _register_family(model_name: str, family: str) -> None:
    """Tell Inspect that `model_name` belongs to `family` (e.g. gemini-3-pro).

    Capability detection (Model.model_family) looks the model up by its bare
    name, without the provider prefix, so register under both forms.
    """
    names = {model_name}
    if "/" in model_name:
        names.add(model_name.split("/", 1)[1])
    for name in names:
        set_model_info(name, ModelInfo(family=family))


@task
def complex_constraints(
    hf_repo: str | None = DEFAULT_HF_REPO,
    task_pack: str | None = None,
    limit: int | None = None,
    judge_model: str = DEFAULT_JUDGE_MODEL,
    model_family: str | None = None,
    judge_model_family: str | None = None,
) -> Task:
    """Single-turn text prompt; model answers in one completion, then each
    rubric criterion is graded independently by an LLM judge.

    Pass `task_pack=<dir>` to run a local offline pack instead of the Hugging
    Face dataset.

    Inspect detects model capabilities (e.g. mapping --reasoning-effort to
    Gemini's thinkingConfig.thinkingLevel) from the model name. When a model is
    served under a nonstandard name (e.g. through a proxy), pass
    `model_family` / `judge_model_family` (e.g. `-T model_family=gemini-3-pro`)
    to tell Inspect what it actually is.
    """
    if model_family:
        _register_family(str(get_model()), model_family)
    if judge_model_family:
        _register_family(judge_model, judge_model_family)

    return Task(
        dataset=load_samples(hf_repo=hf_repo, task_pack=task_pack, limit=limit),
        solver=generate(),
        scorer=rubric_scorer(judge_model=judge_model),
    )
