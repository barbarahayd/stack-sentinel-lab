import unittest

from stack_sentinel.mcp_server.registry import SimpleMCPServer
from stack_sentinel.mcp_server import tools as tool_module
from stack_sentinel.mcp_server.server import register_ticket_tool
from stack_sentinel.shared.contracts import TICKET_TOOL_NAME


class Ex04MCPTicketToolTest(unittest.TestCase):
    def test_register_ticket_tool(self):
        server = SimpleMCPServer("stack-sentinel-mcp", "test", {"domain": "incident-investigation"})
        register_ticket_tool(server)
        tools = server.list_tools()
        names = {tool["name"] for tool in tools}
        self.assertIn(TICKET_TOOL_NAME, names)
        definition = server.tools[TICKET_TOOL_NAME]
        self.assertIn("ticket_id", str(definition.input_schema))
        self.assertTrue(definition.description)
        self.assertIs(definition.handler, tool_module.fetch_ticket_context)
        self.assertIs(register_ticket_tool(server), server)


if __name__ == "__main__":
    unittest.main()
