from skills.trend_fetcher import fetch_trends


def test_fetch_trends_contract():
    """Test defines the expected contract for fetch_trends.

    This test should fail until `fetch_trends` is implemented to return
    the defined schema.
    """
    # Expected shape according to specs/technical.md
    expected_keys = {"trends"}

    result = fetch_trends("twitter")
    assert isinstance(result, dict)
    assert expected_keys.issubset(set(result.keys()))
