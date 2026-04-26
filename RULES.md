# Regras para prompts dos alunos

Inclua estas regras em qualquer prompt usado para gerar codigo durante os exercicios.

```text
Voce esta editando o Stack Sentinel Lab.

Regras obrigatorias:
1. Nao altere assinaturas de funcoes publicas.
2. Nao renomeie arquivos, modulos, classes, funcoes, tools, resources ou prompts.
3. Nao edite testes.
4. Nao remova dados mockados existentes.
5. Nao mude contratos de entrada e saida.
6. Nao introduza dependencias externas sem autorizacao do professor.
7. Implemente apenas o exercicio atual.
8. Preserve os contratos de exercicios futuros.
9. Se precisar criar helper interno, mantenha-o pequeno e local ao modulo.
10. Rode python run.py test exNN depois da alteracao.
11. Se usar LLM real, mantenha a mesma interface do LLMClient e nao torne os testes dependentes de rede ou chave.
```

## Contratos principais

- `fetch_ticket_context(ticket_id: str) -> dict`
- `fetch_build_status(build_id: str) -> dict`
- `create_mcp_server() -> SimpleMCPServer`
- `classify_intent_node(state: AgentState, llm: LLMClient) -> AgentState`
- `route_by_intent(state: AgentState) -> str`
- `fetch_ticket_node(state: AgentState, mcp_client: MCPClient) -> AgentState`
- `fetch_build_node(state: AgentState, mcp_client: MCPClient) -> AgentState`
- `final_answer_node(state: AgentState) -> AgentState`

## Formatos de saida esperados

Tools devem retornar dicionarios com `ok: bool`.

Quando a operacao funcionar, inclua `ok: True` e os campos normalizados do dominio.

Quando a operacao falhar de forma controlada, inclua:

```python
{
    "ok": False,
    "error": "mensagem curta e util"
}
```

Nunca retorne excecoes cruas como resposta para o usuario final.

