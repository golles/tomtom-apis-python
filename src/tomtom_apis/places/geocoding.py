"""Geocode API."""

from typing import Self

from ..api import BaseApi
from ..places.models import GeocodeParams, SearchResponse, StructuredGeocodeParams


class GeocodingApi(BaseApi):
    """Geocoding API.

    The Geocoding API is a powerful tool that converts addresses, such as "109 Park Row, New York, United States," into geographic coordinates (e.g.,
    "lat": 40.71226, "lon": -74.00207). Designed for machine-to-machine interaction, the TomTom Geocoding API is capable of handling requests from
    automated systems to geocode addresses that may be incomplete, incorrectly formatted, or contain typos, providing the best possible result.

    For more information, see: https://developer.tomtom.com/geocoding-api/documentation/product-information/introduction
    """

    async def get_geocode(
        self: Self,
        *,
        query: str,
        params: GeocodeParams | None = None,
    ) -> SearchResponse:
        """Get geocode.

        For more information, see: https://developer.tomtom.com/geocoding-api/documentation/geocode

        Args:
            query (str): The query string representing the address or place to geocode.
            params (GeocodeParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint=f"/search/2/geocode/{query}.json",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def get_structured_geocode(
        self: Self,
        *,
        countryCode: str,
        params: StructuredGeocodeParams | None = None,
    ) -> SearchResponse:
        """Get structured geocode.

        For more information, see: https://developer.tomtom.com/geocoding-api/documentation/structured-geocode

        Args:
            countryCode (str): The country code representing the location's country (e.g., "US" for the United States).
            params (StructuredGeocodeParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint=f"/search/2/structuredGeocode.json?countryCode={countryCode}",
            params=params,
        )

        return await response.deserialize(SearchResponse)
