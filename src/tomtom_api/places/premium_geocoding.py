"""Premium Geocode API"""

from tomtom_api.api import BaseApi

from .models import PremiumGeocodeParams, SearchResponse


class PremiumGeocodingApi(BaseApi):
    """
    The TomTom Premium Geocoding API is a forward geocoding service that returns highly accurate address coordinates along with expanded address features required for last-mile delivery, such as the closest parking points, floor numbering, and building entrances. This enables, for example, address verification, route planning, and front-door navigation. The highly accurate data that comes with premium geocoding allows delivery couriers to get to the customer's door much quicker compared to the standard single-point geocoded location available in regular geocoding. The Premium Geocoding API is currently only available in the USA.


    See: https://developer.tomtom.com/premium-geocoding-api/documentation/product-information/introduction
    """

    async def get_geocode(
        self,
        *,
        query: str,
        params: PremiumGeocodeParams | None = None,
    ) -> SearchResponse:
        """
        The TomTom Premium Geocoding API is a forward geocoding service that returns highly accurate address coordinates along with expanded address features required for last-mile delivery, such as the closest parking points, floor numbering, and building entrances (data not provided by standard geocoding). This enables, for example, address verification, route planning, and to-the-door navigation. Premium geocoding therefore guides couriers to the customer's door for faster and more successful deliveries, compared to the standard geocoded location available in regular geocoding.

        See: https://developer.tomtom.com/premium-geocoding-api/documentation/geocode
        """

        reponse = await self.get(
            endpoint=f"/search/2/premiumGeocode/{query}.json",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)
