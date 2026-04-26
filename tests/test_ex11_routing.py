import unittest

from stack_sentinel.agent.graph import route_by_intent


class Ex11RoutingTest(unittest.TestCase):
    def test_routes_by_intent(self):
        self.assertEqual(route_by_intent({"intent": "ticket"}), "fetch_ticket")
        self.assertEqual(route_by_intent({"intent": "build"}), "fetch_build")
        self.assertEqual(route_by_intent({"intent": "docs"}), "fetch_docs")
        self.assertEqual(route_by_intent({"intent": "unknown"}), "fallback")
        self.assertEqual(route_by_intent({"intent": None}), "fallback")
        self.assertEqual(route_by_intent({}), "fallback")
        self.assertEqual(route_by_intent({"intent": "ticket "}), "fallback")


if __name__ == "__main__":
    unittest.main()
