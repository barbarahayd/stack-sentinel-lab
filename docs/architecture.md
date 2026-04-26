# Arquitetura do Stack Sentinel

```text
Usuario
  ↓
Agent / Graph
  ↓
MCP Client
  ↓
MCP Server
  ↓
Mock API / Dados locais
```

## Responsabilidades

- **Mock API**: simula sistemas internos.
- **MockServiceClient**: chama a mock API.
- **MCP Server**: registra tools, resources e prompts.
- **MCP Client**: chama capabilities do servidor.
- **Agent**: classifica intenção, roteia fluxo, busca contexto e gera resposta final.
- **FakeLLM**: torna os testes determinísticos.

