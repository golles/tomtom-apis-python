"""Junction Analytics tests"""

import pytest

from tomtom_api.traffic import JunctionAnalyticsApi


def test_api_not_implemented():
    """Test API not implemented yet"""
    with pytest.raises(NotImplementedError):
        JunctionAnalyticsApi()
