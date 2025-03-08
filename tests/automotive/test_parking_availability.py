"""Parking Availability test."""

from collections.abc import AsyncGenerator

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.automotive import ParkingAvailabilityApi
from tomtom_apis.automotive.models import ParkingAvailabilityParams, ParkingAvailabilityResponse


@pytest.fixture(name="parking_availability_api")
async def fixture_parking_availability_api() -> AsyncGenerator[ParkingAvailabilityApi]:
    """Fixture for ParkingAvailabilityApi."""
    options = ApiOptions(api_key=API_KEY)
    async with ParkingAvailabilityApi(options) as fuel_prizes:
        yield fuel_prizes


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["automotive/get_parking_availability.json"], indirect=True)
async def test_deserialization_get_parking_availability(parking_availability_api: ParkingAvailabilityApi) -> None:
    """Test the get_fuel_prize method."""
    response = await parking_availability_api.get_parking_availability(
        params=ParkingAvailabilityParams(parkingAvailability="00000000-0003-1d9a-0009-20d4467654e2")
    )

    assert response
    assert isinstance(response, ParkingAvailabilityResponse)
    assert response.statuses
    assert response.statuses[0]
    assert response.statuses[0].current
    assert response.statuses[0].current.updatedAt.isoformat() == "2021-12-12T11:29:00+00:00"
