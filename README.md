# Stack Sentinel Lab

Laboratorio da Semana 3 para construir, em camadas, o **Stack Sentinel**: um agente que investiga tickets, builds, documentacao operacional e saude de servicos usando um servidor MCP didatico e um fluxo inspirado em LangGraph.

## Como rodar

Use sempre os comandos abaixo a partir da raiz do repositorio:

```bash
python run.py doctor
python run.py mock-api
python run.py test ex00
python run.py test all
python run.py demo
```

No Windows, se `python` nao funcionar:

```bash
py run.py doctor
```

## Contratos que nao devem ser alterados

Os alunos podem implementar o corpo das funcoes indicadas nos enunciados dos exercicios, mas nao devem alterar:

- nomes de arquivos e modulos;
- nomes de funcoes publicas;
- parametros das funcoes;
- tipos e chaves dos dicionarios retornados;
- nomes das tools, resources e prompts;
- IDs dos dados mockados usados nos testes;
- arquivos em `tests/`, exceto se o professor pedir explicitamente.

## Sequencia de exercicios

- Ex00: validar setup, imports e dados.
- Ex01: explorar mock service e health check.
- Ex02: criar `fetch_ticket_context`.
- Ex03: criar MCP server minimo.
- Ex04: registrar primeira tool MCP.
- Ex05: criar e registrar tool de build.
- Ex06: criar resources MCP.
- Ex07: criar prompt MCP.
- Ex08: criar grafo minimo.
- Ex09: definir `AgentState`.
- Ex10: criar node de classificacao.
- Ex11: configurar routing condicional.
- Ex12: consultar ticket via MCP no node.
- Ex13: consultar build via MCP no node.
- Ex14: usar resource/prompt no fluxo.
- Ex15: gerar resposta final.
- Ex16: integracao ponta a ponta.

## LLM real opcional

Os exercicios obrigatorios usam `FakeLLMClient`, porque ele torna os testes deterministicos e nao depende de chave, rede ou custo.

Se voce ja tiver uma chave pronta e quiser experimentar uma LLM real, existe o scaffolding opcional em:

```text
stack_sentinel/llm/provider_client.py
```

Essa trilha nao e necessaria para passar nos testes. Ao implementar uma LLM real, preserve o contrato de `classify_intent`: retornar apenas `ticket`, `build`, `docs` ou `unknown`.

