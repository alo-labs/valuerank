"""The emitter patches the committed publication in place, so running it twice
must leave every output byte-identical: no drifting indentation, no leaked
newlines. This runs the real stage as a subprocess inside a temporary copy."""

import subprocess
import sys

import pytest

PUBLICATION_OUTPUTS = ("README.md", "methodology.md", "scores.md", "raw-data.md", "site/index.html")


def run_emit(root):
    completed = subprocess.run(
        [sys.executable, "-m", "valuerank.emit_docs"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    return {name: (root / name).read_bytes() for name in PUBLICATION_OUTPUTS}


@pytest.mark.integration
def test_running_the_emitter_twice_is_a_fixed_point(repo_copy, pinned_clock):
    first = run_emit(repo_copy)
    second = run_emit(repo_copy)

    drifted = [name for name in PUBLICATION_OUTPUTS if first[name] != second[name]]
    assert drifted == [], f"second emitter run changed: {drifted}"
