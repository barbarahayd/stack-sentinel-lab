from typing import Any, Dict

from stack_sentinel.mcp_server.registry import SimpleMCPServer


class MCPClient:
    """Cliente MCP didatico que chama um SimpleMCPServer em memoria."""

    def __init__(self, server: SimpleMCPServer):
        self.server = server

    def list_tools(self):
        return self.server.list_tools()

    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        return self.server.call_tool(name, arguments)

    def list_resources(self):
        return self.server.list_resources()

    def read_resource(self, uri: str) -> Dict[str, Any]:
        return self.server.read_resource(uri)

    def list_prompts(self):
        return self.server.list_prompts()

    def get_prompt(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        return self.server.get_prompt(name, arguments)

