from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List


ToolHandler = Callable[..., Dict[str, Any]]
ResourceHandler = Callable[[], Dict[str, Any]]
PromptHandler = Callable[..., str]


@dataclass
class ToolDefinition:
    name: str
    description: str
    input_schema: Dict[str, Any]
    handler: ToolHandler


@dataclass
class ResourceDefinition:
    uri: str
    name: str
    description: str
    handler: ResourceHandler


@dataclass
class PromptDefinition:
    name: str
    description: str
    arguments: List[str]
    handler: PromptHandler


@dataclass
class SimpleMCPServer:
    name: str
    description: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    tools: Dict[str, ToolDefinition] = field(default_factory=dict)
    resources: Dict[str, ResourceDefinition] = field(default_factory=dict)
    prompts: Dict[str, PromptDefinition] = field(default_factory=dict)

    def register_tool(self, definition: ToolDefinition) -> None:
        self.tools[definition.name] = definition

    def register_resource(self, definition: ResourceDefinition) -> None:
        self.resources[definition.uri] = definition

    def register_prompt(self, definition: PromptDefinition) -> None:
        self.prompts[definition.name] = definition

    def list_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema,
            }
            for tool in self.tools.values()
        ]

    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self.tools:
            return {"ok": False, "error": f"unknown tool: {name}"}
        return self.tools[name].handler(**arguments)

    def list_resources(self) -> List[Dict[str, Any]]:
        return [
            {"uri": resource.uri, "name": resource.name, "description": resource.description}
            for resource in self.resources.values()
        ]

    def read_resource(self, uri: str) -> Dict[str, Any]:
        if uri not in self.resources:
            return {"ok": False, "error": f"unknown resource: {uri}"}
        return self.resources[uri].handler()

    def list_prompts(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": prompt.name,
                "description": prompt.description,
                "arguments": prompt.arguments,
            }
            for prompt in self.prompts.values()
        ]

    def get_prompt(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self.prompts:
            return {"ok": False, "error": f"unknown prompt: {name}"}
        return {"ok": True, "name": name, "content": self.prompts[name].handler(**arguments)}

