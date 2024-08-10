"""O/D Analysis API test"""

import pytest

from tomtom_api.traffic import ODAnalysisApi


def test_api_not_implemented():
    """Test API not implemented ye"""
    with pytest.raises(NotImplementedError):
        ODAnalysisApi()
