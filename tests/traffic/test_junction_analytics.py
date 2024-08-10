"""Junction Analytics test"""

import pytest

from tomtom_api.traffic import JunctionAnalyticsApi


def test_api_not_implemented():
    """Test API not implemented ye"""
    with pytest.raises(NotImplementedError):
        JunctionAnalyticsApi()
