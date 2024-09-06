"""Reverse Geocode API"""

from ..api import BaseApi
from ..models import LatLon
from ..places.models import CrossStreetLookupParams, ReverseGeocodeParams, ReverseGeocodeResponse


class ReverseGeocodingApi(BaseApi):
    """
    The TomTom Reverse Geocoding API gives users a tool to translate a coordinate (for example: 37.786505, -122.3862) into a human-understandable
    street address, street element, or geography. Most often, this is needed in tracking applications where you receive a GPS feed from the device or
    asset and you want to know the address.

    See: https://developer.tomtom.com/reverse-geocoding-api/documentation/product-information/introduction
    """

    async def get_reverse_geocode(
        self,
        *,
        position: LatLon,
        params: ReverseGeocodeParams | None = None,
    ) -> ReverseGeocodeResponse:
        """
        The TomTom Reverse Geocoding API gives users a tool to translate a coordinate (for example: 37.786505, -122.3862) into a human-understandable
        street address, street element, or geography. Most often, this is needed in tracking applications where you receive a GPS feed from the
        device or asset and you want to know the address.

        See: https://developer.tomtom.com/reverse-geocoding-api/documentation/reverse-geocode
        """

        reponse = await self.get(
            endpoint=f"/search/2/reverseGeocode/{position.to_comma_seperate()}.json",
            params=params,
        )

        return await reponse.deserialize(ReverseGeocodeResponse)

    async def get_cross_street_lookup(
        self,
        *,
        position: LatLon,
        params: CrossStreetLookupParams | None = None,
    ) -> ReverseGeocodeResponse:
        """
        This endpoint returns address information and coordinates for a position to the nearest intersection. There may be times when you need to
        translate a coordinate (for example: 37.786505,-122.3862) into a human-understandable street address. Most often this is needed in tracking
        applications where you receive a GPS feed from the device or an asset, and wish to know the position and address information of the nearest
        intersection/crossroad to its initial position.

        See: https://developer.tomtom.com/reverse-geocoding-api/documentation/cross-street-lookup
        """

        reponse = await self.get(
            endpoint=f"/search/2/reverseGeocode/crossStreet/{position.to_comma_seperate()}.json",
            params=params,
        )

        return await reponse.deserialize(ReverseGeocodeResponse)
