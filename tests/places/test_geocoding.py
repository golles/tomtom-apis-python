"""Geocoding test"""

import pytest

from tests.const import API_KEY
from tomtom_api.api import ApiOptions
from tomtom_api.places import GeocodingApi
from tomtom_api.places.models import ResultType, StructuredGeocodeParams


@pytest.fixture(name="geocoding_api")
async def fixture_geocoding_api():
    """Fixture for GeocodingApi"""
    options = ApiOptions(api_key=API_KEY)
    async with GeocodingApi(options) as geocoding:
        yield geocoding


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/geocoding/get_geocode.json"], indirect=True)
async def test_deserialization_get_geocode(geocoding_api: GeocodingApi):
    """Test the get_geocode method"""
    response = await geocoding_api.get_geocode(
        query="De Ruijterkade 154 Amsterdam",
    )

    await geocoding_api.close()

    assert response
    assert len(response.results) == 1
    assert response.results[0]
    assert response.results[0].type
    assert response.results[0].type == ResultType.POINT_ADDRESS
    assert response.results[0].position
    assert response.results[0].position.lat == 52.37727
    assert response.results[0].position.lon == 4.90943


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/geocoding/get_structured_geocode.json"], indirect=True)
async def test_deserialization_get_structured_geocode(geocoding_api: GeocodingApi):
    """Test the get_structured_geocode method"""
    response = await geocoding_api.get_structured_geocode(
        countryCode="NL",
        params=StructuredGeocodeParams(
            streetName="De Ruijterkade",
            streetNumber="154",
            postalCode="1011 AC",
            municipality="Amsterdam",
        ),
    )

    await geocoding_api.close()

    assert response
    assert len(response.results) == 1
    assert response.results[0]
    assert response.results[0].type
    assert response.results[0].type == ResultType.POINT_ADDRESS
    assert response.results[0].position
    assert response.results[0].position.lat == 52.37727
    assert response.results[0].position.lon == 4.90943
