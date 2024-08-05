"""Geocode API"""

from tomtom_api.api import BaseApi
from tomtom_api.places.models import GeocodeParams, SearchResponse, StructuredGeocodeParams


class GeocodingApi(BaseApi):
    """
    The Geocoding API is a powerful tool that converts addresses, such as "109 Park Row, New York, United States," into geographic coordinates (e.g., "lat": 40.71226, "lon": -74.00207). Designed for machine-to-machine interaction, the TomTom Geocoding API is capable of handling requests from automated systems to geocode addresses that may be incomplete, incorrectly formatted, or contain typos, providing the best possible result.

    See: https://developer.tomtom.com/geocoding-api/documentation/product-information/introduction
    """

    async def get_geocode(
        self,
        *,
        query: str,
        params: GeocodeParams | None = None,
    ) -> SearchResponse:
        """
        In many cases, the complete Search service might be too much. For instance, if you are only interested in traditional Geocoding, Search can also be exclusively accessed for address look-up. The Geocoding is performed by hitting the Geocode endpoint with just the address or partial address in question. The Geocoding index will be queried for everything above the street level data.

        See: https://developer.tomtom.com/geocoding-api/documentation/geocode
        """

        reponse = await self.get(
            endpoint=f"/search/2/geocode/{query}.json",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)

    async def get_structured_geocode(
        self,
        *,
        countryCode: str,
        params: StructuredGeocodeParams | None = None,
    ) -> SearchResponse:
        """
        Search can also be exclusively accessed for structured address look up. The geocoding index will be queried for everything above the street level data. No POIs (Points of Interest) will be returned. Note that the geocoder is very tolerant of typos and incomplete addresses. It will also handle everything from exact street addresses, street, or intersections, and higher level geographies such as city centers, counties, states, etc.

        See: https://developer.tomtom.com/geocoding-api/documentation/structgeo
        """

        reponse = await self.get(
            endpoint=f"/search/2/structuredGeocode.json?countryCode={countryCode}",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)
