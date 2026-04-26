from typing import Callable, List

from stack_sentinel.agent.state import AgentState
from stack_sentinel.clients.mcp_client import MCPClient
from stack_sentinel.llm.base import LLMClient


Node = Callable[[AgentState], AgentState]


class SimpleGraph:
    def __init__(self):
        self.nodes: List[Node] = []

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)

    def run(self, state: AgentState) -> AgentState:
        current = state
        for node in self.nodes:
            current = node(current)
        return current


def compile_minimal_graph() -> SimpleGraph:
    """Contrato do Ex08: cria um grafo minimo executavel."""
    raise NotImplementedError("Ex08 ainda nao implementado")


def route_by_intent(state: AgentState) -> str:
    """Contrato do Ex11: retorna a rota a partir de state['intent']."""
    raise NotImplementedError("Ex11 ainda nao implementado")


def run_stack_sentinel_flow(state: AgentState, llm: LLMClient, mcp_client: MCPClient) -> AgentState:
    """Contrato do Ex16: executa o fluxo final ponta a ponta."""
    raise NotImplementedError("Ex16 ainda nao implementado")
