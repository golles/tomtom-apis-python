"""Traffic Stats test"""

import pytest

from tomtom_api.traffic import TrafficStatsApi


def test_api_not_implemented():
    """Test API not implemented ye"""
    with pytest.raises(NotImplementedError):
        TrafficStatsApi()
