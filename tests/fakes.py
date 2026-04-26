from typing import Any, Dict

from stack_sentinel.mcp_server.registry import SimpleMCPServer


class FakeMockServiceClient:
    def __init__(self):
        self.paths = []
        self.ticket_ids = []
        self.build_ids = []
        self.doc_slugs = []

    def get_json(self, path: str) -> Dict[str, Any]:
        self.paths.append(path)
        if path == "/health":
            return {"ok": True, "service": "stack-sentinel-mock-api"}
        return {"ok": False, "error": "unexpected path"}

    def get_ticket(self, ticket_id: str) -> Dict[str, Any]:
        self.ticket_ids.append(ticket_id)
        if ticket_id == "TCK-101":
            return {
                "ok": True,
                "data": {
                    "id": "TCK-101",
                    "summary": "Usuarios relatam erro 500 ao tentar login no portal.",
                    "severity": "high",
                    "service": "auth-service",
                    "status": "open",
                    "build_id": "BLD-203",
                    "title": "Erro 500 no login do portal",
                },
            }
        return {"ok": False, "error": "not found"}

    def get_build(self, build_id: str) -> Dict[str, Any]:
        self.build_ids.append(build_id)
        if build_id == "BLD-203":
            return {
                "ok": True,
                "data": {
                    "id": "BLD-203",
                    "status": "failed",
                    "service": "auth-service",
                    "branch": "main",
                    "failed_step": "integration-tests",
                    "log_excerpt": "test_login_with_mfa returned HTTP 500 instead of 200",
                },
            }
        return {"ok": False, "error": "not found"}

    def get_doc(self, slug: str) -> Dict[str, Any]:
        self.doc_slugs.append(slug)
        docs = {
            "incident-response": {
                "slug": "incident-response",
                "title": "Incident Response Guide",
                "content": "Identifique impacto, severidade, evidencias e proximo passo.",
            },
            "severity-policy": {
                "slug": "severity-policy",
                "title": "Severity Policy",
                "content": "critical, high, medium, low",
            },
        }
        if slug in docs:
            return {"ok": True, "data": docs[slug]}
        return {"ok": False, "error": "not found"}


class BrokenMockServiceClient(FakeMockServiceClient):
    def get_json(self, path: str) -> Dict[str, Any]:
        self.paths.append(path)
        return {"ok": False, "error": "service unavailable"}


def configured_fake_server() -> SimpleMCPServer:
    from stack_sentinel.mcp_server.registry import PromptDefinition, ResourceDefinition, ToolDefinition
    from stack_sentinel.shared.contracts import (
        BUILD_TOOL_NAME,
        INCIDENT_RESPONSE_RESOURCE,
        INCIDENT_TRIAGE_PROMPT,
        TICKET_TOOL_NAME,
    )

    server = SimpleMCPServer(
        name="stack-sentinel-mcp",
        description="fake configured server",
        metadata={"domain": "incident-investigation", "version": "0.1.0"},
    )
    server.register_tool(
        ToolDefinition(
            name=TICKET_TOOL_NAME,
            description="fake ticket tool",
            input_schema={"required": ["ticket_id"]},
            handler=lambda ticket_id: {
                "ok": True,
                "id": ticket_id,
                "summary": "Usuarios relatam erro 500 ao tentar login no portal.",
                "severity": "high",
                "service": "auth-service",
                "status": "open",
                "build_id": "BLD-203",
            },
        )
    )
    server.register_tool(
        ToolDefinition(
            name=BUILD_TOOL_NAME,
            description="fake build tool",
            input_schema={"required": ["build_id"]},
            handler=lambda build_id: {
                "ok": True,
                "id": build_id,
                "status": "failed",
                "service": "auth-service",
                "branch": "main",
                "failed_step": "integration-tests",
                "log_excerpt": "HTTP 500",
            },
        )
    )
    server.register_resource(
        ResourceDefinition(
            uri=INCIDENT_RESPONSE_RESOURCE,
            name="Incident Response Guide",
            description="fake resource",
            handler=lambda: {
                "ok": True,
                "uri": INCIDENT_RESPONSE_RESOURCE,
                "title": "Incident Response Guide",
                "content": "Identifique impacto, severidade, evidencias e proximo passo.",
            },
        )
    )
    server.register_prompt(
        PromptDefinition(
            name=INCIDENT_TRIAGE_PROMPT,
            description="fake prompt",
            arguments=["user_question", "available_context"],
            handler=lambda user_question, available_context: (
                "Resuma o problema, cite severidade, sugira proximo passo e nao invente dados."
            ),
        )
    )
    return server
