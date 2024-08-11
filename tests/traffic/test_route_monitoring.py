"""Route Monitoring tests"""

import pytest

from tomtom_apis.traffic import RouteMonitoringApi


def test_api_not_implemented():
    """Test API not implemented yet"""
    with pytest.raises(NotImplementedError):
        RouteMonitoringApi()
