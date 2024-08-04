"""Auto Stream tests"""

import pytest

from tomtom_api.automotive import AutoStreamApi


def test_api_not_implemented():
    """Test API not implemented yet"""
    with pytest.raises(NotImplementedError):
        AutoStreamApi()
