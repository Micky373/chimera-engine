from skills.skill_publish_post import publish_post


def test_publish_post_contract():
    """Test defines expected contract for publish_post.

    This should fail until `publish_post` returns the expected structure.
    """
    input_payload = {"channel": "twitter", "content": "hello", "metadata": {}}
    result = publish_post(input_payload)
    assert isinstance(result, dict)
    assert "id" in result and "status" in result
