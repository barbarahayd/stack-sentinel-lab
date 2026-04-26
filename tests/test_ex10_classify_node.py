import unittest

from stack_sentinel.agent.nodes import classify_intent_node
from stack_sentinel.llm.fake_client import FakeLLMClient


class WeirdLLM:
    def classify_intent(self, user_input: str) -> str:
        return "surprise"


class Ex10ClassifyNodeTest(unittest.TestCase):
    def test_classifies_known_intents(self):
        llm = FakeLLMClient()
        cases = [
            ("Qual o status do ticket TCK-101?", "ticket"),
            ("O build BLD-203 esta quebrado?", "build"),
            ("Como devo tratar incidente critico?", "docs"),
            ("Bom dia", "unknown"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                result = classify_intent_node({"user_input": text}, llm=llm)
                self.assertEqual(result["intent"], expected)

    def test_invalid_llm_intent_becomes_unknown_and_preserves_state(self):
        original = {"user_input": "ticket TCK-101", "context": {"keep": True}}
        result = classify_intent_node(original, llm=WeirdLLM())
        self.assertEqual(result["intent"], "unknown")
        self.assertEqual(result["context"], {"keep": True})
        self.assertNotIn("intent", original)


if __name__ == "__main__":
    unittest.main()
