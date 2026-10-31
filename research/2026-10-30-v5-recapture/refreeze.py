"""O132 workload migration: re-freeze every ranking's anchors on the v5 cohort inside the score build, then build.

    VALUERANK_NOW=<cutoff> PYTHONPATH=. python3 research/2026-10-30-v5-recapture/refreeze.py

The anchors freeze from the configurations the score build assembles (value_v3.freeze), as `python3 -m valuerank.value_v3
freeze` would from a scores.json already on the v5 cohort; the previous anchor objects are kept in previous-anchors/ for
the O12 dual run.
"""

import json

from valuerank import build_scores, quality as q, value_v3 as v

original = v.build_tracks


def refreeze_then_build(configurations, data, *, release_day):
    documents = v.load_documents(data)
    for track in q.TRACKS:
        with q.active_track(track):
            document = v.freeze(v.assemble(configurations, documents, release_day=release_day), frozen_at=release_day.isoformat())
            (data / v.track_file(v.FROZEN_FILE, track)).write_text(json.dumps(document, indent=2, ensure_ascii=False, default=v._json_default) + "\n")
    return original(configurations, data, release_day=release_day)


v.build_tracks = refreeze_then_build
build_scores.main()
