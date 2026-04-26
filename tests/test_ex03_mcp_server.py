import unittest

from stack_sentinel.mcp_server.registry import SimpleMCPServer
from stack_sentinel.mcp_server.server import create_mcp_server


class Ex03MCPServerTest(unittest.TestCase):
    def test_create_server_minimal_contract(self):
        server = create_mcp_server()
        self.assertIsInstance(server, SimpleMCPServer)
        self.assertEqual(server.name, "stack-sentinel-mcp")
        self.assertTrue(server.description)
        self.assertEqual(server.metadata["domain"], "incident-investigation")
        self.assertEqual(server.metadata["version"], "0.1.0")
        self.assertEqual(server.list_tools(), [])
        self.assertEqual(server.list_resources(), [])
        self.assertEqual(server.list_prompts(), [])


if __name__ == "__main__":
    unittest.main()
