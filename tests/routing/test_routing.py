"""Routing tests"""

from datetime import datetime

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import LatLonList
from tomtom_apis.routing import RoutingApi
from tomtom_apis.routing.models import CalculateReachableRangePostData, CalculateReachableRouteParams, CalculateRouteParams, CalculateRoutePostData

from ..const import LOC_AMSTERDAM, LOC_ROTTERDAM


@pytest.fixture(name="routing_api")
async def fixture_routing_api():
    """Fixture for RoutingApi"""
    options = ApiOptions(api_key=API_KEY)
    async with RoutingApi(options) as long_distance_ev_routing:
        yield long_distance_ev_routing


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/get_calculate_route.json"], indirect=True)
async def test_deserialization_get_calculate_route(routing_api: RoutingApi):
    """Test the get_calculate_route method"""
    response = await routing_api.get_calculate_route(
        locations=LatLonList(locations=[LOC_AMSTERDAM, LOC_ROTTERDAM]),
        params=CalculateRouteParams(
            maxAlternatives=0,
            routeType="fastest",
            traffic=True,
            travelMode="car",
        ),
    )

    await routing_api.close()

    assert response is not None
    assert len(response.routes) == 1
    assert response.routes[0].summary is not None
    assert response.routes[0].summary.lengthInMeters > 1000
    assert response.routes[0].summary.travelTimeInSeconds > 30
    assert isinstance(response.routes[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].summary.arrivalTime, datetime)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/post_calculate_route.json"], indirect=True)
async def test_deserialization_post_calculate_route(routing_api: RoutingApi):
    """Test the post_calculate_route method"""
    response = await routing_api.post_calculate_route(
        locations=LatLonList(locations=[LOC_AMSTERDAM, LOC_ROTTERDAM]),
        params=CalculateRouteParams(
            maxAlternatives=0,
            routeType="fastest",
            traffic=True,
            travelMode="car",
        ),
        data=CalculateRoutePostData.from_dict(
            {
                "supportingPoints": [{"latitude": 52.5093, "longitude": 13.42936}, {"latitude": 52.50844, "longitude": 13.42859}],
                "avoidVignette": ["AUS", "CHE"],
                "avoidAreas": {
                    "rectangles": [
                        {
                            "southWestCorner": {"latitude": 48.81851, "longitude": 2.26593},
                            "northEastCorner": {"latitude": 48.90309, "longitude": 2.41115},
                        }
                    ]
                },
            }
        ),
    )

    await routing_api.close()

    assert response is not None
    assert len(response.routes) == 1
    assert response.routes[0].summary is not None
    assert response.routes[0].summary.lengthInMeters > 1000
    assert response.routes[0].summary.travelTimeInSeconds > 30
    assert isinstance(response.routes[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].summary.arrivalTime, datetime)
    assert isinstance(response.routes[0].legs[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].legs[0].summary.arrivalTime, datetime)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/get_calculate_reachable_range.json"], indirect=True)
async def test_deserialization_get_calculate_reachable_range(routing_api: RoutingApi):
    """Test the get_calculate_reachable_range method"""
    reponse = await routing_api.get_calculate_reachable_range(
        origin=LOC_AMSTERDAM,
        params=CalculateReachableRouteParams(
            energyBudgetInkWh=43,
            avoid="unpavedRoads",
            vehicleEngineType="electric",
            constantSpeedConsumptionInkWhPerHundredkm="50,8.2:130,21.3",
        ),
    )

    await routing_api.close()

    assert reponse is not None
    assert reponse.reachableRange is not None
    assert reponse.reachableRange.center is not None
    assert reponse.reachableRange.center.latitude == 52.50931
    assert reponse.reachableRange.center.longitude == 13.42937
    assert len(reponse.reachableRange.boundary) > 1


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/post_calculate_reachable_range.json"], indirect=True)
async def test_deserialization_post_calculate_reachable_range(routing_api: RoutingApi):
    """Test the post_calculate_reachable_range method"""
    reponse = await routing_api.post_calculate_reachable_range(
        origin=LOC_AMSTERDAM,
        params=CalculateReachableRouteParams(
            energyBudgetInkWh=43,
            avoid="unpavedRoads",
            vehicleEngineType="electric",
            constantSpeedConsumptionInkWhPerHundredkm="50,8.2:130,21.3",
        ),
        data=CalculateReachableRangePostData.from_dict(
            {
                "avoidVignette": ["AUS", "CHE"],
                "avoidAreas": {
                    "rectangles": [
                        {
                            "southWestCorner": {"latitude": 48.81851, "longitude": 2.26593},
                            "northEastCorner": {"latitude": 48.90309, "longitude": 2.41115},
                        }
                    ]
                },
            }
        ),
    )

    await routing_api.close()

    assert reponse is not None
    assert reponse.reachableRange is not None
    assert reponse.reachableRange.center is not None
    assert reponse.reachableRange.center.latitude == 52.50931
    assert reponse.reachableRange.center.longitude == 13.42937
    assert len(reponse.reachableRange.boundary) > 1
