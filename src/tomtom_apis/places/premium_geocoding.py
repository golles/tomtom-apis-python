"""Premium Geocode API."""

from typing import Self

from ..api import BaseApi
from .models import PremiumGeocodeParams, SearchResponse


class PremiumGeocodingApi(BaseApi):
    """Premium Geocoding API.

    The TomTom Premium Geocoding API is a forward geocoding service that returns highly accurate address coordinates along with expanded address
    features required for last-mile delivery, such as the closest parking points, floor numbering, and building entrances. This enables, for example,
    address verification, route planning, and front-door navigation. The highly accurate data that comes with premium geocoding allows delivery
    couriers to get to the customer's door much quicker compared to the standard single-point geocoded location available in regular geocoding. The
    Premium Geocoding API is currently only available in the USA.

    For more information, see: https://developer.tomtom.com/premium-geocoding-api/documentation/product-information/introduction
    """

    async def get_geocode(
        self: Self,
        *,
        query: str,
        params: PremiumGeocodeParams | None = None,
    ) -> SearchResponse:
        """Get geocode.

        For more information, see: https://developer.tomtom.com/premium-geocoding-api/documentation/geocode

        Args:
            query (str): The query string representing the address or place to geocode.
            params (PremiumGeocodeParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint=f"/search/2/premiumGeocode/{query}.json",
            params=params,
        )

        return await response.deserialize(SearchResponse)
