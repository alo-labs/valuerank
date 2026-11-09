import unittest
import xml.etree.ElementTree as ET

from render_pareto import render_chart

def point(name, cost, quality, frontier, full, kind="published"):
    return dict(configuration=name, track="common", basis="api", cost=cost,
                quality=quality, onFrontierAmongPlotted=frontier,
                onFullTrackParetoSet=full, dominatedBy=[], source="data/scores.json", kind=kind)

class ChartTest(unittest.TestCase):
    def setUp(self):
        self.a = point("Alpha <max>", 1, 60, True, False)
        self.b = point("Beta high", 10, 70, True, True)
        self.c = point("Gamma", 100, 65, False, False)
        self.data = {"pareto": {"apiCommon": [self.a, self.b, self.c],
                    "planCommonPublished": [point("Alpha <max>", 10, 60, True, True)],
                    "planCommonWhatIf": [point("Alpha <max>", 1, 60, True, True, "what-if")],
                    "apiMain": [self.a], "apiAicd": [self.b]},
                    "configurations": []}

    def test_api_chart_is_valid_svg_and_shows_record_status(self):
        svg = render_chart(self.data, "api-common")
        root = ET.fromstring(svg)
        self.assertTrue(root.tag.endswith("svg"))
        self.assertIn("Alpha &lt;max&gt;", svg)
        self.assertIn("log scale", svg)
        self.assertIn("2026-11-01T06:10:00Z", svg)
        self.assertIn("not on full-track Pareto set", svg)
        self.assertIn("dominated", svg)
        self.assertIn("frontier-step", svg)
        self.assertIn("data/scores.json", svg)

    def test_plan_chart_marks_what_if_and_fallback(self):
        svg = render_chart(self.data, "plan-common")
        ET.fromstring(svg)
        self.assertIn('class="fallback-link"', svg)
        self.assertIn('class="fallback-marker"', svg)
        self.assertIn("owner-stated, unmeasured", svg)
        self.assertIn("what-if", svg)

    def test_scenario_preserves_grades_of_unchanged_points(self):
        a = dict(point("A", 10, 60, True, True, "what-if"), id="a")
        b = dict(point("B", 3, 70, True, True, "what-if"), id="b")
        self.data["pareto"]["planCommonPublished"] = [dict(a, cost=10), dict(b, cost=30)]
        self.data["pareto"]["planCommonWhatIf"] = [a, b]
        self.data["configurations"] = [{"tracks": {"common": {"row": {"id": "a", "plan": {"grade": "controlled"}}}}}]
        svg = render_chart(self.data, "plan-common")
        self.assertIn("frontier; full-track Pareto set · controlled", svg)
        self.assertEqual(svg.count('class="fallback-marker"'), 1)

    def test_close_points_get_separate_numbered_markers(self):
        self.data["pareto"]["apiCommon"] = [self.a, dict(self.a, configuration="Near")]
        svg = render_chart(self.data, "api-common")
        self.assertIn('class="marker-leader"', svg)

    def test_by_track_chart_identifies_separate_tracks(self):
        svg = render_chart(self.data, "api-by-track")
        ET.fromstring(svg)
        self.assertIn("Max-effort", svg)
        self.assertIn("AI Coding Daily", svg)

if __name__ == "__main__":
    unittest.main()
