import unittest

from stack_sentinel.mcp_server.tools import fetch_ticket_context
from tests.fakes import FakeMockServiceClient


class Ex02TicketToolTest(unittest.TestCase):
    def test_ticket_existing(self):
        client = FakeMockServiceClient()
        result = fetch_ticket_context("TCK-101", client=client)
        self.assertTrue(result["ok"])
        self.assertEqual(result["id"], "TCK-101")
        self.assertEqual(result["severity"], "high")
        self.assertEqual(result["service"], "auth-service")
        self.assertEqual(result["status"], "open")
        self.assertIn("summary", result)
        self.assertEqual(result["build_id"], "BLD-203")
        self.assertEqual(client.ticket_ids, ["TCK-101"])
        self.assertNotIn("description", result)

    def test_ticket_missing(self):
        result = fetch_ticket_context("TCK-999", client=FakeMockServiceClient())
        self.assertFalse(result["ok"])
        self.assertIn("error", result)

    def test_ticket_empty_id_is_controlled_error(self):
        result = fetch_ticket_context("", client=FakeMockServiceClient())
        self.assertFalse(result["ok"])
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
