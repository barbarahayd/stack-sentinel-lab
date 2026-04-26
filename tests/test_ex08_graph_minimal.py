import unittest

from stack_sentinel.agent.graph import SimpleGraph, compile_minimal_graph


class Ex08GraphMinimalTest(unittest.TestCase):
    def test_minimal_graph_runs(self):
        graph = compile_minimal_graph()
        self.assertIsInstance(graph, SimpleGraph)
        result = graph.run({"user_input": "ping"})
        self.assertEqual(result["final_answer"], "ping")
        self.assertEqual(result["user_input"], "ping")
        self.assertGreaterEqual(len(graph.nodes), 1)


if __name__ == "__main__":
    unittest.main()
