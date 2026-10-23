"""Evidence grades for the multi-page site (methodology v3).

Public entry points
-------------------
``GRADES``                         ordered grade names, best to worst (``measured`` .. ``assumption``).
``route_grade(evidence_class)``    grade of one subscription route from its ``evidenceClass``.

Grading rules (docs/site-data-contract.md, "Evidence grades"):

* Every scored quality leaf and basket cost is an owner or Artificial Analysis measurement of the exact
  configuration (provider claims never enter a v3 score), so a ranked configuration is ``measured`` and one
  without observed leaves is ``missing``.
* Plan routes: ``controlled_account_workload_projection`` is ``measured``; ``user_reported_projection`` is
  ``estimate``; ``user_assumption`` and any unknown class are ``assumption``. A selected route is graded from
  the engine's evidence grade for that model (an owner-named transfer is an assumption even when its donor
  route is a measurement).
"""

from __future__ import annotations

GRADES = ("measured", "claim", "estimate", "assumption")

_ROUTE_GRADES = {
    "controlled_account_workload_projection": "measured",
    "user_reported_projection": "estimate",
    "user_assumption": "assumption",
}


def route_grade(evidence_class: str | None) -> str:
    """Grade a subscription route; unknown evidence classes are conservatively ``assumption``."""

    return _ROUTE_GRADES.get(evidence_class, "assumption")
