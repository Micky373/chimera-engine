import unittest

from skills.skill_publish_post import publish_post


class TestSkillsInterface(unittest.TestCase):
    def test_publish_post_contract(self):
        """Defines expected contract for `publish_post`.

        This should fail until `publish_post` returns the expected structure.
        """
        input_payload = {"channel": "twitter", "content": "hello", "metadata": {}}
        result = publish_post(input_payload)
        self.assertIsInstance(result, dict)
        self.assertIn("id", result)
        self.assertIn("status", result)
