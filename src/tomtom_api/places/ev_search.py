"""EV Search AP"""

from tomtom_api.api import BaseApi

from .models import EvSearchByIdParams, EvSearchNearbyParams, SearchResponse


class EVSearchApi(BaseApi):
    """
    EV Search is a REST API limited to and optimized for electric vehicle station POI category. It provides complete EV POI data including static location information (lat/long), address, opening hours, access restrictions, technical specs of the charging station (connector type, voltage, power, current, current type), etc. as well as dynamic availability status. Wide range of EV specific filters (including dynamic availability) allows for narrowing the search results to match the personal preference (like charging power or access type) of the driver or the technical specification of the electric vehicle (connector type).

    See: https://developer.tomtom.com/ev-search-api/documentation/product-information/introduction
    """

    async def get_ev_search_nearby(
        self,
        *,
        params: EvSearchNearbyParams | None = None,
    ) -> SearchResponse:
        """
        The EV Search Nearby endpoint provides information about the nearest charging stations based on a given coordinate system and radius. If provided (using optional request parameters), the response can be filtered by connector type, availability status, etc.

        See: https://developer.tomtom.com/ev-search-api/documentation/ev-search-api/ev-search-nearby
        """

        reponse = await self.get(
            endpoint="/search/2/evsearch",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)

    async def get_ev_search_by_id(
        self,
        *,
        params: EvSearchByIdParams | None = None,
    ) -> SearchResponse:
        """
        The EV Search by Id endpoint provides detailed information about a specific charging station, such as its location, availability status, and the attached connectors.

        See: https://developer.tomtom.com/ev-search-api/documentation/ev-search-api/ev-search-by-id
        """

        reponse = await self.get(
            endpoint="/search/2/evbyid",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)
