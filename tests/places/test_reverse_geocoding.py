"""Reverse Geocoding tests."""

from collections.abc import AsyncGenerator

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import LatLon, ViewType
from tomtom_apis.places import ReverseGeocodingApi
from tomtom_apis.places.models import CrossStreetLookupParams, ReverseGeocodeParams, ReverseGeocodeResponse


@pytest.fixture(name="reverse_geocoding_api")
async def fixture_reverse_geocoding_api() -> AsyncGenerator[ReverseGeocodingApi]:
    """Fixture for ReverseGeocodingApi."""
    options = ApiOptions(api_key=API_KEY)
    async with ReverseGeocodingApi(options) as reverse_geocoding:
        yield reverse_geocoding


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/reverse_geocoding/get_reverse_geocode.json"], indirect=True)
async def test_deserialization_get_reverse_geocode(reverse_geocoding_api: ReverseGeocodingApi) -> None:
    """Test the get_reverse_geocode method."""
    response = await reverse_geocoding_api.get_reverse_geocode(
        position=LatLon(
            lat=37.8328,
            lon=-122.27669,
        ),
        params=ReverseGeocodeParams(
            returnSpeedLimit=False,
            radius=10000,
            allowFreeformNewLine=False,
            returnMatchType=False,
            view=ViewType.UNIFIED,
        ),
    )

    assert response
    assert isinstance(response, ReverseGeocodeResponse)
    assert response.addresses
    assert response.addresses[0]
    assert response.addresses[0].address
    assert response.addresses[0].address.country
    assert response.addresses[0].address.country == "United States"


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/reverse_geocoding/get_cross_street_lookup.json"], indirect=True)
async def test_deserialization_get_cross_street_lookup(reverse_geocoding_api: ReverseGeocodingApi) -> None:
    """Test the get_cross_street_lookup method."""
    response = await reverse_geocoding_api.get_cross_street_lookup(
        position=LatLon(
            lat=37.8328,
            lon=-122.27669,
        ),
        params=CrossStreetLookupParams(
            limit=1,
            radius=10000,
            allowFreeformNewLine=False,
            view=ViewType.UNIFIED,
        ),
    )

    assert response
    assert isinstance(response, ReverseGeocodeResponse)
    assert response.addresses
    assert response.addresses[0]
    assert response.addresses[0].address
    assert response.addresses[0].address.countrySubdivisionName == "California"
