"""Geofencing API tests."""

import pytest

from tomtom_apis.tracking_logistics import GeofencingApi


def test_api_not_implemented() -> None:
    """Test API not implemented yet."""
    with pytest.raises(NotImplementedError):
        GeofencingApi()
