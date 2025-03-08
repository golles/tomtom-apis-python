"""Fuel prices test."""

from collections.abc import AsyncGenerator

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.automotive import FuelPricesApi
from tomtom_apis.automotive.models import FuelPricesResponse, FuelPrizeParams


@pytest.fixture(name="fuel_prizes_api")
async def fixture_fuel_prizes_api() -> AsyncGenerator[FuelPricesApi]:
    """Fixture for FuelPricesApi."""
    options = ApiOptions(api_key=API_KEY)
    async with FuelPricesApi(options) as fuel_prizes:
        yield fuel_prizes


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["automotive/get_fuel_prize.json"], indirect=True)
async def test_deserialization_get_fuel_prize(fuel_prizes_api: FuelPricesApi) -> None:
    """Test the get_fuel_prize method."""
    response = await fuel_prizes_api.get_fuel_prize(params=FuelPrizeParams(fuelPrice="1:2622f89a-6300-11ec-8d12-a0423f39b5a2"))

    assert response
    assert isinstance(response, FuelPricesResponse)
    assert response.fuels
    assert response.fuels[0]
    assert response.fuels[0].updatedAt.isoformat() == "2021-12-12T11:29:14+00:00"
