"""O/D Analysis API tests."""

import pytest

from tomtom_apis.traffic import ODAnalysisApi


def test_api_not_implemented() -> None:
    """Test API not implemented yet."""
    with pytest.raises(NotImplementedError):
        ODAnalysisApi()
