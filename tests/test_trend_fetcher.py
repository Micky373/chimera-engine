import unittest

from skills.trend_fetcher import fetch_trends


class TestTrendFetcher(unittest.TestCase):
    def test_fetch_trends_contract(self):
        """Defines the expected contract for `fetch_trends`.

        This test is expected to fail until `fetch_trends` is implemented
        to return the defined schema.
        """
        expected_keys = {"trends"}

        result = fetch_trends("twitter")
        self.assertIsInstance(result, dict)
        self.assertTrue(expected_keys.issubset(set(result.keys())))
