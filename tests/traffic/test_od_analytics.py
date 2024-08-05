"""O/D Analysis API tests"""

import pytest

from tomtom_api.traffic import ODAnalysisApi


def test_api_not_implemented():
    """Test API not implemented yet"""
    with pytest.raises(NotImplementedError):
        ODAnalysisApi()
