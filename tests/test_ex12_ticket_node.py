import unittest

from stack_sentinel.agent.nodes import fetch_ticket_node
from stack_sentinel.clients.mcp_client import MCPClient
from tests.fakes import configured_fake_server


class Ex12TicketNodeTest(unittest.TestCase):
    def test_fetch_ticket_node_updates_context(self):
        client = MCPClient(configured_fake_server())
        state = {"user_input": "Qual o status do ticket TCK-101?", "ticket_id": None}
        result = fetch_ticket_node(state, client)
        self.assertEqual(result["ticket_id"], "TCK-101")
        self.assertEqual(result["context"]["id"], "TCK-101")
        self.assertEqual(result["context"]["service"], "auth-service")
        self.assertIsNone(result.get("error"))

    def test_fetch_ticket_node_uses_existing_ticket_id(self):
        client = MCPClient(configured_fake_server())
        state = {"user_input": "sem id no texto", "ticket_id": "TCK-101"}
        result = fetch_ticket_node(state, client)
        self.assertEqual(result["context"]["id"], "TCK-101")

    def test_fetch_ticket_node_handles_missing_ticket_id(self):
        client = MCPClient(configured_fake_server())
        result = fetch_ticket_node({"user_input": "sem ticket aqui"}, client)
        self.assertIn("error", result)
        self.assertIsNone(result.get("context"))


if __name__ == "__main__":
    unittest.main()
