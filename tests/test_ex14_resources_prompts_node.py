import unittest

from stack_sentinel.agent.nodes import fetch_docs_node
from stack_sentinel.clients.mcp_client import MCPClient
from tests.fakes import configured_fake_server


class Ex14ResourcesPromptsNodeTest(unittest.TestCase):
    def test_fetch_docs_node_updates_context_with_resource_and_prompt(self):
        client = MCPClient(configured_fake_server())
        state = {"user_input": "Como devo tratar incidente critico?"}
        result = fetch_docs_node(state, client)
        self.assertTrue(result["context"]["resource"]["ok"])
        self.assertTrue(result["context"]["prompt"]["ok"])
        self.assertIn("Incident Response", result["context"]["resource"]["title"])
        self.assertIn("nao invente", result["context"]["prompt"]["content"])
        self.assertIsNone(result.get("error"))
        self.assertIn("resource", result["context"])
        self.assertIn("prompt", result["context"])


if __name__ == "__main__":
    unittest.main()
