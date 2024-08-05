"""Geofencing API tests"""

import pytest

from tomtom_api.tracking_logistics import GeofencingApi


def test_api_not_implemented():
    """Test API not implemented yet"""
    with pytest.raises(NotImplementedError):
        GeofencingApi()
