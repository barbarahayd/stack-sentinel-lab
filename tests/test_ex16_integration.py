import unittest

from stack_sentinel.agent.graph import run_stack_sentinel_flow
from stack_sentinel.agent.state import create_initial_state
from stack_sentinel.clients.mcp_client import MCPClient
from stack_sentinel.llm.fake_client import FakeLLMClient
from tests.fakes import configured_fake_server


class Ex16IntegrationTest(unittest.TestCase):
    def test_ticket_flow(self):
        state = create_initial_state("Qual o status do ticket TCK-101?")
        result = run_stack_sentinel_flow(state, FakeLLMClient(), MCPClient(configured_fake_server()))
        self.assertEqual(result["intent"], "ticket")
        self.assertIn("TCK-101", result["final_answer"])

    def test_build_flow(self):
        state = create_initial_state("O build BLD-203 esta quebrado?")
        result = run_stack_sentinel_flow(state, FakeLLMClient(), MCPClient(configured_fake_server()))
        self.assertEqual(result["intent"], "build")
        self.assertIn("BLD-203", result["final_answer"])

    def test_docs_flow(self):
        state = create_initial_state("Como devo tratar incidente critico?")
        result = run_stack_sentinel_flow(state, FakeLLMClient(), MCPClient(configured_fake_server()))
        self.assertEqual(result["intent"], "docs")
        self.assertIn("proximo passo", result["final_answer"].lower())

    def test_unknown_flow(self):
        state = create_initial_state("Qual a capital da Franca?")
        result = run_stack_sentinel_flow(state, FakeLLMClient(), MCPClient(configured_fake_server()))
        self.assertEqual(result["intent"], "unknown")
        self.assertIn("nao consegui", result["final_answer"].lower())

    def test_flow_preserves_user_input(self):
        question = "Qual o status do ticket TCK-101?"
        state = create_initial_state(question)
        result = run_stack_sentinel_flow(state, FakeLLMClient(), MCPClient(configured_fake_server()))
        self.assertEqual(result["user_input"], question)


if __name__ == "__main__":
    unittest.main()
