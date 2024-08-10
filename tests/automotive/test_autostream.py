"""Auto Stream test"""

import pytest

from tomtom_api.automotive import AutoStreamApi


def test_api_not_implemented():
    """Test API not implemented ye"""
    with pytest.raises(NotImplementedError):
        AutoStreamApi()
