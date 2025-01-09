"""Search API."""

from typing import Self

from ..api import BaseApi, BaseParams
from ..models import Language
from ..places.models import (
    AdditionalDataParams,
    AdditionalDataResponse,
    AutocompleteParams,
    AutocompleteResponse,
    CategorySearchParams,
    Geometry,
    GeometryFilterData,
    GeometryFilterResponse,
    GeometryPoi,
    GeometrySearchParams,
    GeometrySearchPostData,
    NearbySearchParams,
    PlaceByIdParams,
    PlaceByIdResponse,
    PoiCategoriesParams,
    PoiCategoriesResponse,
    PoiSearchParams,
    SearchAlongRouteData,
    SearchAlongRouteParams,
    SearchParams,
    SearchResponse,
)


class SearchApi(BaseApi):
    """Search API.

    The Search service of the Search API consists of the following endpoints:

    For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/search-service
    """

    async def get_search(
        self: Self,
        *,
        query: str,
        params: SearchParams | None = None,
    ) -> SearchResponse:
        """Get search.

        For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/fuzzy-search

        Args:
            query (str): The query string representing the address or place to geocode.
            params (SearchParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint=f"/search/2/search/{query}.json",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def get_poi_search(
        self: Self,
        *,
        query: str,
        params: PoiSearchParams | None = None,
    ) -> SearchResponse:
        """Get POI search.

        For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/points-of-interest-search

        Args:
            query (str): The query string representing the address or place to geocode.
            params (PoiSearchParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint=f"/search/2/poiSearch/{query}.json",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def get_category_search(
        self: Self,
        *,
        query: str,
        params: CategorySearchParams | None = None,
    ) -> SearchResponse:
        """Get category search.

        For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/category-search

        Args:
            query (str): The category or search term to look for (e.g., "restaurant", "hospital").
            params (CategorySearchParams | None, optional): Additional parameters for the category search. Defaults to None.

        Returns:
            SearchResponse: The response containing the category-based search results.
        """
        response = await self.get(
            endpoint=f"/search/2/categorySearch/{query}.json",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def get_geometry_search(
        self: Self,
        *,
        query: str,
        geometryList: list[Geometry],
        params: GeometrySearchParams | None = None,
    ) -> SearchResponse:
        """Get category search.

        For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/geometry-search

        Args:
            query (str): The query string representing the address, category, or place to search for.
            geometryList (list[Geometry]): A list of geometric shapes defining the search area.
            params (GeometrySearchParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: The response containing search results within the specified geometry.
        """
        response = await self.get(
            endpoint=f"/search/2/geometrySearch/{query}.json?geometryList={str(geometryList)}",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def post_geometry_search(
        self: Self,
        *,
        query: str,
        params: GeometrySearchParams | None = None,
        data: GeometrySearchPostData,
    ) -> SearchResponse:
        """Post category search.

        For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/geometry-search

        Args:
            query (str): The query string representing the address, category, or place to search for.
            params (GeometrySearchParams | None, optional): Additional parameters for the geometry search. Defaults to None.
            data (GeometrySearchPostData): The geometric data (e.g., polygons, circles) that defines the search area.

        Returns:
            SearchResponse: The response containing search results within the specified geometry.
        """
        response = await self.post(
            endpoint=f"/search/2/geometrySearch/{query}.json",
            params=params,
            data=data,
        )

        return await response.deserialize(SearchResponse)

    async def get_nearby_search(
        self: Self,
        *,
        lat: float,
        lon: float,
        params: NearbySearchParams | None = None,
    ) -> SearchResponse:
        """Get nearby search.

        For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/nearby-search

        Args:
            lat (float): The latitude of the location to search around.
            lon (float): The longitude of the location to search around.
            params (NearbySearchParams | None, optional): Additional parameters for the nearby search. Defaults to None.

        Returns:
            SearchResponse: The response containing the search results for nearby places.
        """
        response = await self.get(
            endpoint=f"/search/2/nearbySearch/.json?lat={lat}&lon={lon}",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def post_search_along_route(
        self: Self,
        *,
        query: str,
        maxDetourTime: int,
        params: SearchAlongRouteParams | None = None,
        data: SearchAlongRouteData,
    ) -> SearchResponse:
        """Post search along route.

        For more information, see: https://developer.tomtom.com/search-api/documentation/search-service/along-route-search

        Args:
            query (str): The query string representing the category, address, or place to search for along the route.
            maxDetourTime (int): The maximum allowable detour time (in seconds) from the route.
            params (SearchAlongRouteParams | None, optional): Additional parameters for the search along the route. Defaults to None.
            data (SearchAlongRouteData): Data defining the route and other search criteria.

        Returns:
            SearchResponse: The response containing search results along the specified route.
        """
        response = await self.post(
            endpoint=f"/search/2/searchAlongRoute/{query}.json?maxDetourTime={maxDetourTime}",
            params=params,
            data=data,
        )

        return await response.deserialize(SearchResponse)

    async def get_autocomplete(
        self: Self,
        *,
        query: str,
        language: Language,
        params: AutocompleteParams | None = None,
    ) -> AutocompleteResponse:
        """Get autocomplete.

        For more information, see: https://developer.tomtom.com/search-api/documentation/autocomplete-service/autocomplete

        Args:
            query (str): The query string for which to get autocomplete suggestions.
            language (Language): The language in which to return the autocomplete suggestions.
            params (AutocompleteParams | None, optional): Additional parameters for the autocomplete request. Defaults to None.

        Returns:
            AutocompleteResponse: The response containing autocomplete suggestions based on the query.
        """
        response = await self.get(
            endpoint=f"/search/2/autocomplete/{query}.json?language={language}",
            params=params,
        )

        return await response.deserialize(AutocompleteResponse)

    async def get_geometry_filter(
        self: Self,
        *,
        geometryList: list[Geometry],
        poiList: list[GeometryPoi],
        params: BaseParams | None = None,  # No extra params.
    ) -> GeometryFilterResponse:
        """Get geometry filter.

        For more information, see: https://developer.tomtom.com/search-api/documentation/filters-service/geometry-filter

        Args:
            geometryList (list[Geometry]): A list of geometric shapes (e.g., polygons, circles) used for filtering the results.
            poiList (list[GeometryPoi]): A list of points of interest (POIs) used for filtering the results.
            params (BaseParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            GeometryFilterResponse: The response containing the results filtered by the provided geometry and POIs.
        """
        response = await self.get(
            endpoint=f"/search/2/geometryFilter.json?geometryList={str(geometryList)}&poiList={str(poiList)}",
            params=params,
        )

        return await response.deserialize(GeometryFilterResponse)

    async def post_geometry_filter(
        self: Self,
        *,
        params: BaseParams | None = None,  # No extra params.
        data: GeometryFilterData,
    ) -> GeometryFilterResponse:
        """Post geometry filter.

        For more information, see: https://developer.tomtom.com/search-api/documentation/filters-service/geometry-filter

        Args:
            params (BaseParams | None, optional): Additional parameters for the request. Defaults to None.
            data (GeometryFilterData): Data defining the geometric shapes and POIs for the filter.

        Returns:
            GeometryFilterResponse: The response containing the filtered results based on the provided geometry and POIs.
        """
        response = await self.post(
            endpoint="/search/2/geometryFilter.json",
            params=params,
            data=data,
        )

        return await response.deserialize(GeometryFilterResponse)

    async def get_additional_data(
        self: Self,
        *,
        geometries: list[str],
        params: AdditionalDataParams | None = None,
    ) -> AdditionalDataResponse:
        """Get additional data.

        For more information, see: https://developer.tomtom.com/search-api/documentation/additional-data-service/additional-data

        Args:
            geometries (list[str]): A list of geometry identifiers for which to retrieve additional data.
            params (AdditionalDataParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            AdditionalDataResponse: The response containing the additional data for the specified geometries.
        """
        response = await self.get(
            endpoint=f"/search/2/additionalData.json?geometries={','.join(geometries)}",
            params=params,
        )

        return await response.deserialize(AdditionalDataResponse)

    async def get_place_by_id(
        self: Self,
        *,
        params: PlaceByIdParams | None = None,
    ) -> PlaceByIdResponse:
        """Get place by id.

        For more information, see: https://developer.tomtom.com/search-api/documentation/place-by-id-service/place-by-id

        Args:
            params (PlaceByIdParams | None, optional): Parameters including the place ID for the request. Defaults to None.

        Returns:
            PlaceByIdResponse: The response containing details of the place identified by the provided ID.
        """
        response = await self.get(
            endpoint="/search/2/place.json",
            params=params,
        )

        return await response.deserialize(PlaceByIdResponse)

    async def get_poi_categories(
        self: Self,
        *,
        params: PoiCategoriesParams | None = None,
    ) -> PoiCategoriesResponse:
        """Get poi categories.

        For more information, see: https://developer.tomtom.com/search-api/documentation/poi-categories-service/poi-categories

        Args:
            params (PoiCategoriesParams | None, optional): Optional parameters for the request. Defaults to None.

        Returns:
            PoiCategoriesResponse: The response containing the list of POI categories.
        """
        response = await self.get(
            endpoint="/search/2/poiCategories.json",
            params=params,
        )

        return await response.deserialize(PoiCategoriesResponse)
