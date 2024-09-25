"""Reverse Geocode API."""

from typing import Self

from ..api import BaseApi
from ..models import LatLon
from ..places.models import CrossStreetLookupParams, ReverseGeocodeParams, ReverseGeocodeResponse


class ReverseGeocodingApi(BaseApi):
    """Reverse Geocoding API.

    The TomTom Reverse Geocoding API gives users a tool to translate a coordinate (for example: 37.786505, -122.3862) into a human-understandable
    street address, street element, or geography. Most often, this is needed in tracking applications where you receive a GPS feed from the device or
    asset and you want to know the address.

    For more information, see: https://developer.tomtom.com/reverse-geocoding-api/documentation/product-information/introduction
    """

    async def get_reverse_geocode(
        self: Self,
        *,
        position: LatLon,
        params: ReverseGeocodeParams | None = None,
    ) -> ReverseGeocodeResponse:
        """Get reverse geocode.

        For more information, see: https://developer.tomtom.com/reverse-geocoding-api/documentation/reverse-geocode

        Args:
            position (LatLon): The latitude and longitude of the location to reverse geocode.
            params (ReverseGeocodeParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            ReverseGeocodeResponse: The response containing the reverse geocode results.
        """
        response = await self.get(
            endpoint=f"/search/2/reverseGeocode/{position.to_comma_separated()}.json",
            params=params,
        )

        return await response.deserialize(ReverseGeocodeResponse)

    async def get_cross_street_lookup(
        self: Self,
        *,
        position: LatLon,
        params: CrossStreetLookupParams | None = None,
    ) -> ReverseGeocodeResponse:
        """Get cross street lookup.

        For more information, see: https://developer.tomtom.com/reverse-geocoding-api/documentation/cross-street-lookup

        Args:
            position (LatLon): The latitude and longitude of the location for the cross street lookup.
            params (CrossStreetLookupParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            ReverseGeocodeResponse: The response containing the cross street lookup results.
        """
        response = await self.get(
            endpoint=f"/search/2/reverseGeocode/crossStreet/{position.to_comma_separated()}.json",
            params=params,
        )

        return await response.deserialize(ReverseGeocodeResponse)
