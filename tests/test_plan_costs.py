import unittest

from scripts.plan_costs import (
    build_cost_fields,
    effective_cost,
    load_plan_routes,
    opencode_go_tiers,
    rank_cost_scores,
    select_best_route,
)


class PlanCostsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.routes = load_plan_routes()

    def test_opencode_go_exposes_three_value_multiple_tiers_for_one_plan(self):
        tiers = opencode_go_tiers(self.routes)

        self.assertEqual(
            [(tier["usageUsd"], tier["valueMultiple"]) for tier in tiers],
            [(15, 1.5), (30, 3.0), (60, 6.0)],
        )
        self.assertEqual({tier["planPriceUsd"] for tier in tiers}, {10})

    def test_best_route_uses_tibotattle_codex_anchor(self):
        route = select_best_route("gpt-5.5", self.routes)

        self.assertIsNotNone(route)
        self.assertEqual(route["id"], "chatgpt-pro-20x-tibotattle")
        self.assertEqual(route["valueMultiple"], 38.5)
        self.assertNotEqual(route["valueMultiple"], 70)

    def test_best_route_uses_kimi_vivace_sensitivity(self):
        route = select_best_route("kimi-k3", self.routes)

        self.assertIsNotNone(route)
        self.assertEqual(route["id"], "kimi-vivace-community-scaled")
        self.assertEqual(route["valueMultiple"], 69.3)
        self.assertEqual(route["measuredAnchorMultiple"], 24.2)

    def test_gemini_uses_highest_google_ultra_value_multiple(self):
        route = select_best_route("gemini-3.8-flash", self.routes)

        self.assertIsNotNone(route)
        self.assertEqual(route["id"], "google-ai-ultra-20x-modelled")
        self.assertEqual(route["valueMultiple"], 10.6)
        self.assertEqual(route["quotaMultipleVsPro"], 20)

    def test_google_gemini_routes_preserve_pro_and_ultra_quota_tiers(self):
        google_routes = [route for route in self.routes["routes"] if route["provider"] == "Google"]

        self.assertEqual(
            [(route["planPriceUsd"], route["quotaMultipleVsPro"]) for route in google_routes],
            [(19.99, 1), (99.99, 5), (199.99, 20)],
        )

    def test_effective_cost_divides_api_cost_by_route_multiple(self):
        route = select_best_route("glm-5.2", self.routes)

        self.assertAlmostEqual(effective_cost(6.0, route), 1.0)

    def test_models_without_verified_route_keep_api_cost_as_plan_fallback(self):
        fields = build_cost_fields(
            [
                {"id": "unlisted-model", "deepsweCost": 4.0},
                {"id": "gpt-5.5", "deepsweCost": 8.0},
            ],
            self.routes,
        )

        self.assertIsNone(fields[0]["planRoute"])
        self.assertIsNone(fields[0]["planCost"])
        self.assertEqual(fields[0]["planCostFallback"], "api")
        self.assertAlmostEqual(fields[1]["planCost"], 8.0 / 38.5)
        self.assertEqual(fields[1]["planCostFallback"], None)

    def test_rank_scores_handle_ties_with_average_rank(self):
        self.assertEqual(rank_cost_scores([10.0, 10.0, 20.0]), [75.0, 75.0, 0.0])


if __name__ == "__main__":
    unittest.main()
