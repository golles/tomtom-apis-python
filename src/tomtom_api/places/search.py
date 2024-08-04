"""Search API"""

from tomtom_api.api import BaseApi, BaseParams, BasePostData
from tomtom_api.places.models import PlaceByIdParams, PlaceByIdResponse, PoiCategoriesParams, PoiCategoriesResponse, SearchResponse


class SearchApi(BaseApi):
    """
    The Search service of the Search API consists of the several endpoints

    See: https://developer.tomtom.com/search-api/documentation/search-service/search-service
    """

    async def get_search(
        self,
        *,
        query: str,
        params: BaseParams | None = None,
    ) -> SearchResponse:
        """
        The generic, default service is Fuzzy Search which handles the most fuzzy of inputs containing any combination of Indexes abbreviation values. See the Indexes abbreviation values section at the bottom of this page.

        See: https://developer.tomtom.com/search-api/documentation/search-service/fuzzy-search
        """

        reponse = await self.get(
            endpoint=f"/search/2/search/{query}.json",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)

    async def get_poi_search(
        self,
        *,
        query: str,
        params: BaseParams | None = None,
    ) -> SearchResponse:
        """
        If your search use case only requires POI results, you may use the Points of Interest endpoint for searching. This endpoint will only return POI results.

        See: https://developer.tomtom.com/search-api/documentation/search-service/points-of-interest-search
        """

        reponse = await self.get(
            endpoint=f"/search/2/poiSearch/{query}.json",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)

    async def get_category_search(
        self,
        *,
        query: str,
        params: BaseParams | None = None,
    ) -> SearchResponse:
        """
        If your search use case only requires POI (Points of Interest) results filtered by category, you may use the Category Search endpoint. This endpoint will only return POI results which are categorized as specified.

        See: https://developer.tomtom.com/search-api/documentation/search-service/category-search
        """

        reponse = await self.get(
            endpoint=f"/search/2/categorySearch/{query}.json",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)

    async def get_geometry_search(
        self,
        *,
        query: str,
        params: BaseParams | None = None,
    ) -> SearchResponse:
        """
        The Geometry Search endpoint allows you to perform a free form search inside a single geometry or many of them. The search results that fall inside the geometry/geometries will be returned. The service returns POI results by default. For other result types, the idxSet parameter should be used. To send the geometry you will use a POST or GET request with json as a string value for the geometryList parameter.

        See: https://developer.tomtom.com/search-api/documentation/search-service/geometry-search
        """

        reponse = await self.get(
            endpoint=f"/search/2/geometrySearch/{query}.json",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)

    async def get_nearby_search(
        self,
        *,
        params: BaseParams | None = None,
    ) -> SearchResponse:
        """
        If your use case is only retrieving POI (Points of Interest) results around a location, you may use the Nearby Search endpoint. This endpoint will only return POI results. It does not take in a search query parameter.

        See: https://developer.tomtom.com/search-api/documentation/search-service/nearby-search
        """

        reponse = await self.get(
            endpoint="/search/2/nearbySearch/.json",
            params=params,
        )

        return await reponse.deserialize(SearchResponse)

    async def post_search_along_route(
        self,
        *,
        query: str,
        params: BaseParams,
        data: BasePostData,
    ) -> SearchResponse:
        """
        The Along Route Search endpoint allows you to perform a fuzzy search for POIs along a specified route. This search is constrained by specifying a detour time-limiting measure. To send the route points you will use a POST request whose body will contain the route parameter in JSON format. The minimum number of route points is 2.

        See: https://developer.tomtom.com/search-api/documentation/search-service/along-route-search
        """

        reponse = await self.post(
            endpoint=f"/search/2/searchAlongRoute/{query}.json",
            params=params,
            data=data,
        )

        return await reponse.deserialize(SearchResponse)

    async def get_autocomplete(
        self,
        *,
        query: str,
        params: BaseParams | None = None,
    ) -> dict:
        """
        The Autocomplete API enables you to make a more meaningful Search API call by recognizing entities inside an input query and offering them as query terms.

        See: https://developer.tomtom.com/search-api/documentation/autocomplete-service/autocomplete
        """

        reponse = await self.get(
            endpoint=f"/search/2/autocomplete/{query}.json",
            params=params,
        )

        return await reponse.dict()

    async def get_geometry_filter(
        self,
        *,
        params: BaseParams | None = None,
    ) -> dict:
        """
        The Geometry Search endpoint allows you to perform a free form search inside a single geometry or many of them. The search results that fall inside the geometry/geometries will be returned. The service returns POI results by default. For other result types, the idxSet parameter should be used. To send the geometry you will use a POST or GET request with json as a string value for the geometryList parameter.

        See: https://developer.tomtom.com/search-api/documentation/search-service/geometry-search
        """

        reponse = await self.get(
            endpoint="/search/2/geometryFilter.json",
            params=params,
        )

        return await reponse.dict()

    async def post_geometry_filter(
        self,
        *,
        params: BaseParams | None = None,
        data: BasePostData,
    ) -> dict:
        """
        The Geometry Search endpoint allows you to perform a free form search inside a single geometry or many of them. The search results that fall inside the geometry/geometries will be returned. The service returns POI results by default. For other result types, the idxSet parameter should be used. To send the geometry you will use a POST or GET request with json as a string value for the geometryList parameter.

        See: https://developer.tomtom.com/search-api/documentation/search-service/geometry-search
        """

        reponse = await self.post(
            endpoint="/search/2/geometryFilter.json",
            params=params,
            data=data,
        )

        return await reponse.dict()

    async def get_additional_data(
        self,
        *,
        params: BaseParams | None = None,
    ) -> dict:
        """
        The Geometries Data Provider returns sets of coordinates that represent the outline of a city, country, or land area. The service supports batch requests of up to 20 identifiers.

        See: https://developer.tomtom.com/search-api/documentation/additional-data-service/additional-data
        """

        reponse = await self.get(
            endpoint="/search/2/additionalData.json",
            params=params,
        )

        return await reponse.dict()

    async def get_place_by_id(
        self,
        *,
        params: PlaceByIdParams | None = None,
    ) -> PlaceByIdResponse:
        """
        The Place by Id service endpoint provides detailed information about the Place found by its identifier (entityId). Currently, Place by Id supports all types by ids.

        See: https://developer.tomtom.com/search-api/documentation/place-by-id-service/place-by-id
        """

        reponse = await self.get(
            endpoint="/search/2/place.json",
            params=params,
        )

        return await reponse.deserialize(PlaceByIdResponse)

    async def get_poi_categories(
        self,
        *,
        params: PoiCategoriesParams | None = None,
    ) -> PoiCategoriesResponse:
        """
        The POI Categories service endpoint provides a full list of POI categories and subcategories together with their translations and synonyms.

        See: https://developer.tomtom.com/search-api/documentation/poi-categories-service/poi-categories
        """

        reponse = await self.get(
            endpoint="/search/2/poiCategories.json",
            params=params,
        )

        return await reponse.deserialize(PoiCategoriesResponse)
