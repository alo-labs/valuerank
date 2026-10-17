"""``reconcile`` accepts the data directory so callers can reconcile a copy."""

import json
from datetime import datetime, timezone

from valuerank import aa_reconciliation


def test_reconcile_reads_the_inventory_from_the_given_data_directory(repo_copy, pinned_clock):
    inventory_path = repo_copy / "data" / "aa_reconciliation_inventory.json"
    document = json.loads(inventory_path.read_text())
    document["observedAt"] = "2026-10-16T00:00:00Z"
    inventory_path.write_text(json.dumps(document))
    now = datetime.fromisoformat(pinned_clock.replace("Z", "+00:00"))

    report = aa_reconciliation.reconcile(now, data=repo_copy / "data")

    assert report["inventoryPath"] == "data/aa_reconciliation_inventory.json"
    assert report["ageDays"] == round((now - datetime(2026, 10, 16, tzinfo=timezone.utc)).total_seconds() / 86400, 3)
    assert report["status"] == "reconciled"
