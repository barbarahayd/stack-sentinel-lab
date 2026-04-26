import unittest

from stack_sentinel.mcp_server.prompts import incident_triage_prompt


class Ex07PromptsTest(unittest.TestCase):
    def test_incident_triage_prompt_contains_required_instructions(self):
        prompt = incident_triage_prompt(
            user_question="Como tratar incidente critico?",
            available_context="critical: impacto financeiro relevante",
        )
        lower = prompt.lower()
        self.assertIn("resum", lower)
        self.assertIn("severidade", lower)
        self.assertIn("proximo passo", lower)
        self.assertIn("nao invent", lower)
        self.assertIn("como tratar incidente critico", lower)
        self.assertIn("critical", lower)


if __name__ == "__main__":
    unittest.main()
