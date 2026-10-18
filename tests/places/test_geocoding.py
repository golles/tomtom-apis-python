"""Geocoding tests."""

from collections.abc import AsyncGenerator

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.places import GeocodingApi
from tomtom_apis.places.models import ResultType, SearchResponse, StructuredGeocodeParams


@pytest.fixture(name="geocoding_api")
async def fixture_geocoding_api() -> AsyncGenerator[GeocodingApi]:
    """Fixture for GeocodingApi."""
    options = ApiOptions(api_key=API_KEY)
    async with GeocodingApi(options) as geocoding:
        yield geocoding


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/geocoding/get_geocode.json"], indirect=True)
async def test_deserialization_get_geocode(geocoding_api: GeocodingApi) -> None:
    """Test the get_geocode method."""
    response = await geocoding_api.get_geocode(
        query="De Ruijterkade 154 Amsterdam",
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert len(response.results) == 1
    assert response.results[0]
    assert response.results[0].type
    assert response.results[0].type == ResultType.POINT_ADDRESS
    assert response.results[0].position
    assert round(response.results[0].position.lat, 5) == 52.37727
    assert round(response.results[0].position.lon, 5) == 4.90943


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/geocoding/get_structured_geocode.json"], indirect=True)
async def test_deserialization_get_structured_geocode(geocoding_api: GeocodingApi) -> None:
    """Test the get_structured_geocode method."""
    response = await geocoding_api.get_structured_geocode(
        countryCode="NL",
        params=StructuredGeocodeParams(
            streetName="De Ruijterkade",
            streetNumber="154",
            postalCode="1011 AC",
            municipality="Amsterdam",
        ),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert len(response.results) == 1
    assert response.results[0]
    assert response.results[0].type
    assert response.results[0].type == ResultType.POINT_ADDRESS
    assert response.results[0].position
    assert round(response.results[0].position.lat, 5) == 52.37727
    assert round(response.results[0].position.lon, 5) == 4.90943


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/geocoding/get_geocode_address_range.json"], indirect=True)
async def test_deserialization_get_geocode_address_range(geocoding_api: GeocodingApi) -> None:
    """Test the get_geocode method with an address range result."""
    response = await geocoding_api.get_geocode(
        query="1 State Highway 392 San Jon NM",
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert len(response.results) == 1
    assert response.results[0].type == ResultType.ADDRESS_RANGE
    assert response.results[0].addressRanges
    assert response.results[0].addressRanges.rangeLeft == "1 - 1"
    assert response.results[0].addressRanges.rangeRight is None
    assert round(response.results[0].addressRanges.from_.lat, 5) == 35.21552
    assert round(response.results[0].addressRanges.to.lon, 5) == -103.32879
