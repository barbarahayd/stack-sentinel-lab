import unittest

from stack_sentinel.mcp_server.resources import list_doc_resources, read_doc_resource
from stack_sentinel.shared.contracts import INCIDENT_RESPONSE_RESOURCE, SEVERITY_POLICY_RESOURCE
from tests.fakes import FakeMockServiceClient


class Ex06ResourcesTest(unittest.TestCase):
    def test_list_resources_contains_required_uris(self):
        uris = {item["uri"] for item in list_doc_resources()}
        self.assertIn(INCIDENT_RESPONSE_RESOURCE, uris)
        self.assertIn(SEVERITY_POLICY_RESOURCE, uris)

    def test_read_resource(self):
        client = FakeMockServiceClient()
        result = read_doc_resource(INCIDENT_RESPONSE_RESOURCE, client=client)
        self.assertTrue(result["ok"])
        self.assertEqual(result["uri"], INCIDENT_RESPONSE_RESOURCE)
        self.assertIn("Incident Response", result["title"])
        self.assertIn("severidade", result["content"])
        self.assertEqual(client.doc_slugs, ["incident-response"])

    def test_read_unknown_resource_returns_controlled_error(self):
        result = read_doc_resource("docs://missing", client=FakeMockServiceClient())
        self.assertFalse(result["ok"])
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
