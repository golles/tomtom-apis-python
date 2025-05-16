"""Fuel Prices API."""

from typing import Self

from tomtom_apis.api import BaseApi
from tomtom_apis.automotive.models import FuelPricesResponse, FuelPrizeParams


class FuelPricesApi(BaseApi):
    """Fuel Prices API.

    For more information, see: https://developer.tomtom.com/fuel-prices-api/documentation/product-information/introduction
    """

    async def get_fuel_prize(
        self: Self,
        *,
        params: FuelPrizeParams | None = None,
    ) -> FuelPricesResponse:
        """Get fuel prize.

        For more information, see: https://developer.tomtom.com/fuel-prices-api/documentation/fuel-prices-api/fuel-price

        Args:
            params (FuelPrizeParams | None, optional): Additional parameters to filter the fuel prices query. Defaults to None.

        Returns:
            FuelPricesResponse: The response containing the fuel prices data.
        """
        response = await self.get(
            endpoint="/search/2/fuelPrice.json",
            params=params,
        )

        return await response.deserialize(FuelPricesResponse)
