"""Auto Stream tests."""

import pytest

from tomtom_apis.automotive import AutoStreamApi


def test_api_not_implemented() -> None:
    """Test API not implemented yet."""
    with pytest.raises(NotImplementedError):
        AutoStreamApi()
