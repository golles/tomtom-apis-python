"""Notifications test"""

import pytest

from tomtom_api.tracking_logistics import NotificationsApi


def test_api_not_implemented():
    """Test API not implemented ye"""
    with pytest.raises(NotImplementedError):
        NotificationsApi()
