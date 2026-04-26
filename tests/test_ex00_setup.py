import unittest

from stack_sentinel.data_loader import find_by_id, find_doc, find_service, load_collection
from stack_sentinel.mock_api.server import resolve_mock_route


class Ex00SetupTest(unittest.TestCase):
    def test_data_files_load(self):
        self.assertGreaterEqual(len(load_collection("tickets")), 6)
        self.assertGreaterEqual(len(load_collection("builds")), 6)
        self.assertGreaterEqual(len(load_collection("docs")), 4)

    def test_required_fixture_ids_exist(self):
        self.assertEqual(find_by_id("tickets", "TCK-101")["service"], "auth-service")
        self.assertEqual(find_by_id("builds", "BLD-203")["status"], "failed")
        self.assertEqual(find_service("auth-service")["status"], "degraded")
        self.assertIn("Incident Response", find_doc("incident-response")["title"])

    def test_mock_api_routes_resolve(self):
        status, payload = resolve_mock_route("/health")
        self.assertEqual(status, 200)
        self.assertTrue(payload["ok"])

        status, payload = resolve_mock_route("/tickets/TCK-101")
        self.assertEqual(status, 200)
        self.assertEqual(payload["data"]["id"], "TCK-101")


if __name__ == "__main__":
    unittest.main()

