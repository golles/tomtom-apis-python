"""Traffic Stats tests"""

import pytest

from tomtom_api.traffic import TrafficStatsApi


def test_api_not_implemented():
    """Test API not implemented yet"""
    with pytest.raises(NotImplementedError):
        TrafficStatsApi()
