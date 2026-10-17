"""The emitter must read every input from the ``data`` directory it is given,
never from the real repository, so a temporary copy fully controls the output."""

import json

from valuerank import emit_docs


def test_plan_routes_are_read_from_the_given_data_directory(repo_copy, pinned_clock):
    routes_path = repo_copy / "data" / "plan_cost_routes.json"
    document = json.loads(routes_path.read_text())
    document["asOf"] = "2031-01-01"
    routes_path.write_text(json.dumps(document))

    emit_docs.main(root=repo_copy, data=repo_copy / "data")

    assert "Plan route evidence as of 2031-01-01" in (repo_copy / "README.md").read_text()


def test_frontier_inventory_is_read_from_the_given_data_directory(repo_copy, pinned_clock):
    inventory_path = repo_copy / "data" / "aa_reconciliation_inventory.json"
    document = json.loads(inventory_path.read_text())
    document["observedAt"] = "2026-10-06T00:00:00Z"
    inventory_path.write_text(json.dumps(document))

    emit_docs.main(root=repo_copy, data=repo_copy / "data")

    assert "Observed 2026-10-06T00:00:00Z" in (repo_copy / "README.md").read_text()


def test_plan_policy_copy_states_the_claude_shared_plan_multiples(repo_copy, pinned_clock):
    # Owner decision 2026-10-18 (Option 2): the Claude shared routes carry Opus 5.5's measured multiples,
    # and the generated copy must name them as an applied assumption with the model-specific caution.
    emit_docs.main(root=repo_copy, data=repo_copy / "data")

    readme = (repo_copy / "README.md").read_text()
    assert "common Claude multiples (Pro 58.9×; Max $100 57.25×; Max $200 58.63×)" in readme
    assert "Fable 5.1" in readme and "owner-authorized" in readme


def test_plan_policy_copy_omits_the_claude_sentence_when_no_shared_route_exists(repo_copy, pinned_clock):
    routes_path = repo_copy / "data" / "plan_cost_routes.json"
    document = json.loads(routes_path.read_text())
    document["routes"] = [route for route in document["routes"] if not route["id"].endswith("common-opus55-assumption")]
    routes_path.write_text(json.dumps(document))

    emit_docs.main(root=repo_copy, data=repo_copy / "data")

    assert "common Claude multiples" not in (repo_copy / "README.md").read_text()
