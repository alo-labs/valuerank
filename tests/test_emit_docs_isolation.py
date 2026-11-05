"""The emitter must read every input from the ``data`` directory it is given,
never from the real repository, so a temporary copy fully controls the output."""

import json

from valuerank import emit_docs


def edit(repo_copy, name, change):
    path = repo_copy / "data" / name
    document = json.loads(path.read_text())
    change(document)
    path.write_text(json.dumps(document))


def test_plan_routes_are_read_from_the_given_data_directory(repo_copy, pinned_clock):
    def change(routes):
        routes["asOf"] = "2031-01-01"
        routes["routes"][0]["planLabel"] = "Renamed fixture plan"

    edit(repo_copy, "plan_cost_routes.json", change)

    emit_docs.main(root=repo_copy, data=repo_copy / "data")

    raw = (repo_copy / "raw-data.md").read_text()
    assert "Route evidence as of 2031-01-01." in raw and "| Renamed fixture plan |" in raw
    assert "**Subscription evidence policy** (as of 2031-01-01;" in (repo_copy / "methodology.md").read_text()


def test_frontier_inventory_is_read_from_the_given_data_directory(repo_copy, pinned_clock):
    edit(repo_copy, "aa_reconciliation_inventory.json", lambda document: document.__setitem__("observedAt", "2026-10-06T00:00:00Z"))

    emit_docs.main(root=repo_copy, data=repo_copy / "data")

    assert "Observed 2026-10-06T00:00:00Z" in (repo_copy / "README.md").read_text()


def test_plan_policy_copy_states_the_claude_shared_plan_assumption(repo_copy, pinned_clock):
    # Owner decision 2026-10-18 (Option 2): the Claude shared routes carry Opus 5.5's measured multiples,
    # and the generated copy must name them as an applied assumption with the model-specific caution.
    emit_docs.main(root=repo_copy, data=repo_copy / "data")

    methodology = (repo_copy / "methodology.md").read_text()
    assert "- Claude: User authorizes (2026-10-18, Option 2) applying Opus 5.5's measured SemiAnalysis Claude plan multiples" in methodology
    assert "Fable 5.1 measured 12.4-12.7x" in methodology
