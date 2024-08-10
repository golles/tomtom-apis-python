"""Matrix Routing V2 test"""

import pytest

from tomtom_api.routing import MatrixRoutingApiV2


def test_api_not_implemented():
    """Test API not implemented ye"""
    with pytest.raises(NotImplementedError):
        MatrixRoutingApiV2()
