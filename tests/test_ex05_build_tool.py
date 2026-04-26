import unittest

from stack_sentinel.mcp_server.registry import SimpleMCPServer
from stack_sentinel.mcp_server.server import register_build_tool
from stack_sentinel.mcp_server.tools import fetch_build_status
from stack_sentinel.shared.contracts import BUILD_TOOL_NAME
from tests.fakes import FakeMockServiceClient


class Ex05BuildToolTest(unittest.TestCase):
    def test_fetch_build_status(self):
        client = FakeMockServiceClient()
        result = fetch_build_status("BLD-203", client=client)
        self.assertTrue(result["ok"])
        self.assertEqual(result["id"], "BLD-203")
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["failed_step"], "integration-tests")
        self.assertIn("log_excerpt", result)
        self.assertEqual(client.build_ids, ["BLD-203"])

    def test_fetch_build_missing(self):
        result = fetch_build_status("BLD-999", client=FakeMockServiceClient())
        self.assertFalse(result["ok"])
        self.assertIn("error", result)

    def test_register_build_tool(self):
        server = SimpleMCPServer("stack-sentinel-mcp", "test")
        register_build_tool(server)
        self.assertIn(BUILD_TOOL_NAME, {tool["name"] for tool in server.list_tools()})
        self.assertIn("build_id", str(server.tools[BUILD_TOOL_NAME].input_schema))


if __name__ == "__main__":
    unittest.main()
