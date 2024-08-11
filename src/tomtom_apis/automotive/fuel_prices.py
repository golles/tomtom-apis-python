"""Fuel Prices API"""

from ..api import BaseApi
from ..automotive.models import FuelPricesResponse, FuelPrizeParams


class FuelPricesApi(BaseApi):
    """
    The Fuel Prices API provides information about the current price of the fuel available at the selected station. The data is refreshed every 10 minutes, but the frequency of change can differ from a few times a day to a few times a month depending on the country or the brand of the gas station. Using this API makes it possible to make better price-conscious decisions while selecting a suitable gas station.

    See: https://developer.tomtom.com/fuel-prices-api/documentation/product-information/introduction
    """

    async def get_fuel_prize(
        self,
        *,
        params: FuelPrizeParams | None = None,
    ) -> FuelPricesResponse:
        """
        In many cases, the complete Search service might be too much. For instance, if you are only interested in traditional Geocoding, Search can also be exclusively accessed for address look-up. The Geocoding is performed by hitting the Geocode endpoint with just the address or partial address in question. The Geocoding index will be queried for everything above the street level data.

        See: https://developer.tomtom.com/fuel-prices-api/documentation/fuel-prices-api/fuel-price
        """

        reponse = await self.get(
            endpoint="/search/2/fuelPrice.json",
            params=params,
        )

        return await reponse.deserialize(FuelPricesResponse)
