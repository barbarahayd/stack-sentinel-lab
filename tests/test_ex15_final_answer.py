import unittest

from stack_sentinel.agent.nodes import final_answer_node


class Ex15FinalAnswerTest(unittest.TestCase):
    def test_ticket_answer_contains_summary_evidence_and_next_step(self):
        state = {
            "intent": "ticket",
            "context": {
                "ok": True,
                "id": "TCK-101",
                "summary": "Usuarios relatam erro 500 ao tentar login no portal.",
                "severity": "high",
                "service": "auth-service",
                "status": "open",
                "build_id": "BLD-203",
            },
            "error": None,
        }
        result = final_answer_node(state)
        answer = result["final_answer"].lower()
        self.assertIn("resumo", answer)
        self.assertIn("evid", answer)
        self.assertIn("proximo passo", answer)
        self.assertIn("tck-101", answer)

    def test_unknown_answer_uses_fallback(self):
        result = final_answer_node({"intent": "unknown", "context": None, "error": "sem rota"})
        self.assertIn("nao consegui", result["final_answer"].lower())

    def test_build_answer_contains_build_evidence(self):
        state = {
            "intent": "build",
            "context": {
                "ok": True,
                "id": "BLD-203",
                "status": "failed",
                "service": "auth-service",
                "branch": "main",
                "failed_step": "integration-tests",
                "log_excerpt": "HTTP 500",
            },
        }
        answer = final_answer_node(state)["final_answer"].lower()
        self.assertIn("bld-203", answer)
        self.assertIn("integration-tests", answer)
        self.assertIn("proximo passo", answer)

    def test_docs_answer_uses_resource_and_prompt_context(self):
        state = {
            "intent": "docs",
            "context": {
                "resource": {"ok": True, "title": "Incident Response Guide", "content": "Classifique severidade."},
                "prompt": {"ok": True, "content": "Nao invente dados e sugira proximo passo."},
            },
        }
        answer = final_answer_node(state)["final_answer"].lower()
        self.assertIn("incident response", answer)
        self.assertIn("proximo passo", answer)


if __name__ == "__main__":
    unittest.main()
