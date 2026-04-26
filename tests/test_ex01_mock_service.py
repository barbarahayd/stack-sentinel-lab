import unittest

from stack_sentinel.clients.mock_service_client import MOCK_ENDPOINTS, check_mock_service_health
from tests.fakes import BrokenMockServiceClient, FakeMockServiceClient


class Ex01MockServiceTest(unittest.TestCase):
    def test_endpoints_contract(self):
        self.assertEqual(MOCK_ENDPOINTS["tickets"], "/tickets/{ticket_id}")
        self.assertEqual(MOCK_ENDPOINTS["builds"], "/builds/{build_id}")
        self.assertEqual(MOCK_ENDPOINTS["docs"], "/docs/{slug}")

    def test_health_check_returns_true(self):
        client = FakeMockServiceClient()
        self.assertTrue(check_mock_service_health(client))
        self.assertEqual(client.paths, ["/health"])

    def test_health_check_returns_false_on_unhealthy_response(self):
        self.assertFalse(check_mock_service_health(BrokenMockServiceClient()))


if __name__ == "__main__":
    unittest.main()
