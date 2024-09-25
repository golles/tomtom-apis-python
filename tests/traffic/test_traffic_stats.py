"""Traffic Stats tests."""

import pytest

from tomtom_apis.traffic import TrafficStatsApi


def test_api_not_implemented() -> None:
    """Test API not implemented yet."""
    with pytest.raises(NotImplementedError):
        TrafficStatsApi()
