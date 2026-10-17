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
