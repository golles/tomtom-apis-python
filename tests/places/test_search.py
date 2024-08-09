"""Routing tests"""

import pytest

from tests.const import API_KEY
from tomtom_api.api import ApiOptions, BaseParams, BasePostData
from tomtom_api.places import SearchApi
from tomtom_api.places.models import PlaceByIdParams, PoiCategoriesParams


@pytest.fixture(name="search_api")
async def fixture_search_api():
    """Fixture for SearchApi."""
    options = ApiOptions(api_key=API_KEY)
    async with SearchApi(options) as search:
        yield search


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_search.json"], indirect=True)
async def test_deserialization_get_search(search_api: SearchApi):
    """Test the get_search method."""
    params = BaseParams().from_dict(
        {
            "lat": "37.337",
            "lon": "-121.89",
            "categorySet": "7315",
            "view": "Unified",
            "relatedPois": "off",
            "minFuzzyLevel": "1",
            "maxFuzzyLevel": "2",
        }
    )

    response = await search_api.get_search(
        query="pizza",
        params=params,
    )

    await search_api.close()

    assert response
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_poi_search.json"], indirect=True)
async def test_deserialization_get_poi_search(search_api: SearchApi):
    """Test the get_poi_search method."""
    params = BaseParams().from_dict(
        {
            "lat": "37.337",
            "lon": "-121.89",
            "categorySet": "7315",
            "view": "Unified",
            "relatedPois": "off",
        }
    )

    response = await search_api.get_poi_search(
        query="pizza",
        params=params,
    )

    await search_api.close()

    assert response
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_category_search.json"], indirect=True)
async def test_deserialization_get_category_search(search_api: SearchApi):
    """Test the get_category_search method."""
    params = BaseParams().from_dict(
        {
            "lat": "37.337",
            "lon": "-121.89",
            "categorySet": "7315",
            "view": "Unified",
            "relatedPois": "off",
        }
    )

    response = await search_api.get_category_search(
        query="pizza",
        params=params,
    )

    await search_api.close()

    assert response
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_geometry_search.json"], indirect=True)
async def test_deserialization_get_geometry_search(search_api: SearchApi):
    """Test the get_geometry_search method."""
    params = BaseParams().from_dict(
        {
            "geometryList": '[{"type":"POLYGON", "vertices":["37.7524152343544, -122.43576049804686", "37.70660472542312, -122.43301391601562", "37.712059855877314, -122.36434936523438", "37.75350561243041, -122.37396240234374"]}, {"type":"CIRCLE", "position":"37.71205, -121.36434", "radius":6000}, {"type":"CIRCLE", "position":"37.31205, -121.36434", "radius":1000}]',
            "categorySet": "7315",
            "view": "Unified",
            "relatedPois": "off",
        }
    )

    response = await search_api.get_geometry_search(
        query="pizza",
        params=params,
    )

    await search_api.close()

    assert response
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_nearby_search.json"], indirect=True)
async def test_deserialization_get_nearby_search(search_api: SearchApi):
    """Test the get_nearby_search method."""
    params = BaseParams().from_dict(
        {
            "lat": "48.872263",
            "lon": "2.299541",
            "radius": "1000",
            "limit": "100",
        }
    )

    response = await search_api.get_nearby_search(
        params=params,
    )

    await search_api.close()

    assert response
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/post_search_along_route.json"], indirect=True)
async def test_deserialization_post_search_along_route(search_api: SearchApi):
    """Test the post_search_along_route method."""
    params = BaseParams().from_dict(
        {
            "maxDetourTime": "600",
            "categorySet": "7315",
            "view": "Unified",
            "sortBy": "detourOffset",
            "relatedPois": "off",
        }
    )
    data = BasePostData().from_dict(
        {
            "route": {
                "points": [
                    {"lat": 37.52768, "lon": -122.30082},
                    {"lat": 37.52952, "lon": -122.29365},
                    {"lat": 37.52987, "lon": -122.2883},
                    {"lat": 37.52561, "lon": -122.28219},
                    {"lat": 37.52091, "lon": -122.27661},
                    {"lat": 37.52277, "lon": -122.27334},
                    {"lat": 37.52432, "lon": -122.26833},
                    {"lat": 37.5139, "lon": -122.25621},
                    {"lat": 37.49881, "lon": -122.2391},
                    {"lat": 37.49426, "lon": -122.2262},
                    {"lat": 37.48792, "lon": -122.20905},
                    {"lat": 37.48425, "lon": -122.18374},
                    {"lat": 37.47642, "lon": -122.1683},
                    {"lat": 37.4686, "lon": -122.15644},
                    {"lat": 37.46981, "lon": -122.15498},
                    {"lat": 37.4718, "lon": -122.15149},
                ]
            }
        }
    )

    response = await search_api.post_search_along_route(
        query="pizza",
        params=params,
        data=data,
    )

    await search_api.close()

    assert response
    assert response.results
    assert len(response.results) > 5


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_place_by_id.json"], indirect=True)
async def test_deserialization_get_place_by_id(search_api: SearchApi):
    """Test the test_get_place_by_id method."""
    response = await search_api.get_place_by_id(
        params=PlaceByIdParams(entityId="528009004256119"),
    )

    await search_api.close()

    assert response
    assert response.results
    assert len(response.results) == 1
    assert response.results[0]
    assert response.results[0].poi
    assert response.results[0].poi.name == "Amsterdam Central"


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/search/get_poi_categories.json"], indirect=True)
async def test_deserialization_get_poi_categories(search_api: SearchApi):
    """Test the get_poi_categories method."""
    response = await search_api.get_poi_categories(
        params=PoiCategoriesParams(),
    )

    await search_api.close()

    assert response
    assert response.poiCategories
    assert len(response.poiCategories) > 500
