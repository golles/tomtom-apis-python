"""Routing tests."""

from collections.abc import AsyncGenerator

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import Language, LatLon, ViewType
from tomtom_apis.places import SearchApi
from tomtom_apis.places.models import (
    AdditionalDataResponse,
    Address,
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
    Poi,
    PoiCategoriesParams,
    PoiCategoriesResponse,
    Points,
    PoiSearchParams,
    RelatedPoisType,
    SearchAlongRouteData,
    SearchAlongRouteParams,
    SearchParams,
    SearchResponse,
    SortByType,
)


@pytest.fixture(name="search_api")
async def fixture_search_api() -> AsyncGenerator[SearchApi]:
    """Fixture for SearchApi."""
    options = ApiOptions(api_key=API_KEY)
    async with SearchApi(options) as search:
        yield search


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_search.json"], indirect=True)
async def test_deserialization_get_search(search_api: SearchApi) -> None:
    """Test the get_search method."""
    response = await search_api.get_search(
        query="pizza",
        params=SearchParams(
            lat=37.337,
            lon=-121.89,
            categorySet=["7315"],
            view=ViewType.UNIFIED,
            relatedPois=RelatedPoisType.OFF,
            minFuzzyLevel=1,
            maxFuzzyLevel=2,
        ),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_poi_search.json"], indirect=True)
async def test_deserialization_get_poi_search(search_api: SearchApi) -> None:
    """Test the get_poi_search method."""
    response = await search_api.get_poi_search(
        query="pizza",
        params=PoiSearchParams(
            lat=37.337,
            lon=-121.89,
            view=ViewType.UNIFIED,
            relatedPois=RelatedPoisType.OFF,
        ),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_category_search.json"], indirect=True)
async def test_deserialization_get_category_search(search_api: SearchApi) -> None:
    """Test the get_category_search method."""
    response = await search_api.get_category_search(
        query="pizza",
        params=CategorySearchParams(
            lat=37.337,
            lon=-121.89,
            categorySet=["7315"],
            view=ViewType.UNIFIED,
            relatedPois=RelatedPoisType.OFF,
        ),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_geometry_search.json"], indirect=True)
async def test_deserialization_get_geometry_search(search_api: SearchApi) -> None:
    """Test the get_geometry_search method."""
    response = await search_api.get_geometry_search(
        query="pizza",
        geometryList=[
            Geometry(
                type="POLYGON",
                vertices=[
                    "37.7524152343544, -122.43576049804686",
                    "37.70660472542312, -122.43301391601562",
                    "37.712059855877314, -122.36434936523438",
                    "37.75350561243041, -122.37396240234374",
                ],
            ),
            Geometry(
                type="CIRCLE",
                position="37.71205, -121.36434",
                radius=6000,
            ),
            Geometry(
                type="CIRCLE",
                position="37.31205, -121.36434",
                radius=1000,
            ),
        ],
        params=GeometrySearchParams(
            categorySet=["7315"],
            view=ViewType.UNIFIED,
            relatedPois=RelatedPoisType.OFF,
        ),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/post_geometry_search.json"], indirect=True)
async def test_deserialization_post_geometry_search(search_api: SearchApi) -> None:
    """Test the post_geometry_search method."""
    response = await search_api.post_geometry_search(
        query="pizza",
        params=GeometrySearchParams(
            categorySet=["7315"],
            view=ViewType.UNIFIED,
            relatedPois=RelatedPoisType.OFF,
        ),
        data=GeometrySearchPostData(
            geometryList=[
                Geometry(
                    type="POLYGON",
                    vertices=[
                        "37.7524152343544, -122.43576049804686",
                        "37.70660472542312, -122.43301391601562",
                        "37.712059855877314, -122.36434936523438",
                        "37.75350561243041, -122.37396240234374",
                    ],
                ),
                Geometry(
                    type="CIRCLE",
                    position="37.71205, -121.36434",
                    radius=6000,
                ),
                Geometry(
                    type="CIRCLE",
                    position="37.31205, -121.36434",
                    radius=1000,
                ),
            ]
        ),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_nearby_search.json"], indirect=True)
async def test_deserialization_get_nearby_search(search_api: SearchApi) -> None:
    """Test the get_nearby_search method."""
    response = await search_api.get_nearby_search(
        lat=48.872263,
        lon=2.299541,
        params=NearbySearchParams(radius=1000, limit=100),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/post_search_along_route.json"], indirect=True)
async def test_deserialization_post_search_along_route(search_api: SearchApi) -> None:
    """Test the post_search_along_route method."""
    response = await search_api.post_search_along_route(
        query="pizza",
        maxDetourTime=600,
        params=SearchAlongRouteParams(
            categorySet=["7315"],
            view=ViewType.UNIFIED,
            sortBy=SortByType.DETOUR_OFFSET,
            relatedPois=RelatedPoisType.OFF,
        ),
        data=SearchAlongRouteData(
            route=Points(
                points=[
                    LatLon(lat=37.52768, lon=-122.30082),
                    LatLon(lat=37.52952, lon=-122.29365),
                    LatLon(lat=37.52987, lon=-122.2883),
                    LatLon(lat=37.52561, lon=-122.28219),
                    LatLon(lat=37.52091, lon=-122.27661),
                    LatLon(lat=37.52277, lon=-122.27334),
                    LatLon(lat=37.52432, lon=-122.26833),
                    LatLon(lat=37.5139, lon=-122.25621),
                    LatLon(lat=37.49881, lon=-122.2391),
                    LatLon(lat=37.49426, lon=-122.2262),
                    LatLon(lat=37.48792, lon=-122.20905),
                    LatLon(lat=37.48425, lon=-122.18374),
                    LatLon(lat=37.47642, lon=-122.1683),
                    LatLon(lat=37.4686, lon=-122.15644),
                    LatLon(lat=37.46981, lon=-122.15498),
                    LatLon(lat=37.4718, lon=-122.15149),
                ]
            ),
        ),
    )

    assert response
    assert isinstance(response, SearchResponse)
    assert response.results
    assert len(response.results) > 3


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_place_by_id.json"], indirect=True)
async def test_deserialization_get_place_by_id(search_api: SearchApi) -> None:
    """Test the test_get_place_by_id method."""
    response = await search_api.get_place_by_id(
        params=PlaceByIdParams(entityId="528009004256119"),
    )

    assert response
    assert response.results
    assert len(response.results) == 1
    assert response.results[0]
    assert response.results[0].poi
    assert response.results[0].poi.name == "Amsterdam Central"


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_autocomplete.json"], indirect=True)
async def test_deserialization_get_autocomplete(search_api: SearchApi) -> None:
    """Test the get_autocomplete method."""
    response = await search_api.get_autocomplete(query="pizza", language=Language.EN_US)

    assert response
    assert isinstance(response, AutocompleteResponse)
    assert response.results
    assert len(response.results) > 2


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_geometry_filter.json"], indirect=True)
async def test_deserialization_get_geometry_filter(search_api: SearchApi) -> None:
    """Test the get_geometry_filter method."""
    response = await search_api.get_geometry_filter(
        geometryList=[
            Geometry(type="CIRCLE", position="40.80558, -73.96548", radius=100),
            Geometry(
                type="POLYGON",
                vertices=[
                    "37.7524152343544, -122.43576049804686",
                    "37.70660472542312, -122.43301391601562",
                    "37.712059855877314, -122.36434936523438",
                    "37.75350561243041, -122.37396240234374",
                ],
            ),
        ],
        poiList=[
            GeometryPoi(
                poi=Poi(name="S Restaurant Toms"),
                address=Address(freeformAddress="2880 Broadway, New York, NY 10025"),
                position=LatLon(lat=40.80558, lon=-73.96548),
            ),
            GeometryPoi(
                poi=Poi(name="Yasha Raman Corporation"),
                address=Address(freeformAddress="940 Amsterdam Ave, New York, NY 10025"),
                position=LatLon(lat=40.80076, lon=-73.96556),
            ),
        ],
    )

    assert response
    assert isinstance(response, GeometryFilterResponse)
    assert response.results
    assert len(response.results) > 0


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/post_geometry_filter.json"], indirect=True)
async def test_deserialization_post_geometry_filter(search_api: SearchApi) -> None:
    """Test the post_geometry_filter method."""
    response = await search_api.post_geometry_filter(
        data=GeometryFilterData(
            geometryList=[
                Geometry(type="CIRCLE", position="40.80558, -73.96548", radius=100),
                Geometry(
                    type="POLYGON",
                    vertices=[
                        "37.7524152343544, -122.43576049804686",
                        "37.70660472542312, -122.43301391601562",
                        "37.712059855877314, -122.36434936523438",
                        "37.75350561243041, -122.37396240234374",
                    ],
                ),
            ],
            poiList=[
                GeometryPoi(
                    poi=Poi(name="S Restaurant Toms"),
                    address=Address(freeformAddress="2880 Broadway, New York, NY 10025"),
                    position=LatLon(lat=40.80558, lon=-73.96548),
                ),
                GeometryPoi(
                    poi=Poi(name="Yasha Raman Corporation"),
                    address=Address(freeformAddress="940 Amsterdam Ave, New York, NY 10025"),
                    position=LatLon(lat=40.80076, lon=-73.96556),
                ),
            ],
        )
    )

    assert response
    assert isinstance(response, GeometryFilterResponse)
    assert response.results
    assert len(response.results) > 0


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_poi_categories.json"], indirect=True)
async def test_deserialization_get_poi_categories(search_api: SearchApi) -> None:
    """Test the get_poi_categories method."""
    response = await search_api.get_poi_categories(
        params=PoiCategoriesParams(),
    )

    assert response
    assert isinstance(response, PoiCategoriesResponse)
    assert response.poiCategories
    assert len(response.poiCategories) > 500


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_additional_data.json"], indirect=True)
async def test_deserialization_get_additional_data(search_api: SearchApi) -> None:
    """Test the get_additional_data method."""
    response = await search_api.get_additional_data(
        geometries=["00004631-3400-3c00-0000-0000673c4d2e", "00004631-3400-3c00-0000-0000673c42fe"],
    )

    assert response
    assert isinstance(response, AdditionalDataResponse)
