"""Premium Geocoding tests"""

import pytest

from tests.const import API_KEY
from tomtom_api.api import ApiOptions
from tomtom_api.places import PremiumGeocodingApi
from tomtom_api.places.models import ResultType


@pytest.fixture(name="premium_geocoding_api")
async def fixture_premium_geocoding_api():
    """Fixture for PremiumGeocodingApi."""
    options = ApiOptions(api_key=API_KEY)
    async with PremiumGeocodingApi(options) as premium_geocoding:
        yield premium_geocoding


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/premium_geocoding/get_geocode.json"], indirect=True)
async def test_deserialization_get_geocode(premium_geocoding_api: PremiumGeocodingApi):
    """Test the get_geocode method."""

    response = await premium_geocoding_api.get_geocode(
        query="De Ruijterkade 154 Amsterdam",
    )

    await premium_geocoding_api.close()

    assert response
    assert len(response.results) == 2
    assert response.results[0]
    assert response.results[0].type
    assert response.results[0].type == ResultType.POINT_ADDRESS
    assert response.results[0].position
    assert response.results[0].position.lat == 30.23966941103544
    assert response.results[0].position.lon == -97.78704138350255
