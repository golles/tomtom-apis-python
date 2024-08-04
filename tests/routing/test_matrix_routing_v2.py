"""Matrix Routing V2 tests"""

import pytest

from tomtom_api.routing import MatrixRoutingApiV2


def test_api_not_implemented():
    """Test API not implemented yet"""
    with pytest.raises(NotImplementedError):
        MatrixRoutingApiV2()
