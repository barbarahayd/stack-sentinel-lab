import unittest

from stack_sentinel.agent.state import create_initial_state, update_state


class Ex09StateTest(unittest.TestCase):
    def test_initial_state_contract(self):
        state = create_initial_state("Qual o status do ticket TCK-101?")
        self.assertEqual(state["user_input"], "Qual o status do ticket TCK-101?")
        for key in ["intent", "ticket_id", "build_id", "context", "error", "final_answer"]:
            self.assertIn(key, state)
            self.assertIsNone(state[key])

    def test_update_state_does_not_mutate_original(self):
        state = {"user_input": "x", "intent": None}
        updated = update_state(state, intent="ticket")
        self.assertIsNone(state["intent"])
        self.assertEqual(updated["intent"], "ticket")

    def test_initial_state_does_not_trim_user_input(self):
        text = "  Qual o status do ticket TCK-101?  "
        state = create_initial_state(text)
        self.assertEqual(state["user_input"], text)


if __name__ == "__main__":
    unittest.main()
