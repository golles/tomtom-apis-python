"""Routing tests."""

from collections.abc import AsyncGenerator
from datetime import datetime

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import LatLonList, TravelModeType
from tomtom_apis.routing import RoutingApi
from tomtom_apis.routing.models import (
    AvoidType,
    CalculatedReachableRangeResponse,
    CalculatedRouteResponse,
    CalculateReachableRangePostData,
    CalculateReachableRouteParams,
    CalculateRouteParams,
    CalculateRoutePostData,
    RouteType,
    VehicleEngineType,
)

from ..const import LOC_AMSTERDAM, LOC_ROTTERDAM


@pytest.fixture(name="routing_api")
async def fixture_routing_api() -> AsyncGenerator[RoutingApi]:
    """Fixture for RoutingApi."""
    options = ApiOptions(api_key=API_KEY)
    async with RoutingApi(options) as routing:
        yield routing


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/get_calculate_route.json"], indirect=True)
async def test_deserialization_get_calculate_route(routing_api: RoutingApi) -> None:
    """Test the get_calculate_route method."""
    response = await routing_api.get_calculate_route(
        locations=LatLonList(locations=[LOC_AMSTERDAM, LOC_ROTTERDAM]),
        params=CalculateRouteParams(
            maxAlternatives=0,
            routeType=RouteType.FASTEST,
            traffic=True,
            travelMode=TravelModeType.CAR,
        ),
    )

    assert response
    assert isinstance(response, CalculatedRouteResponse)
    assert len(response.routes) == 1
    assert response.routes[0].summary
    assert response.routes[0].summary.lengthInMeters > 1000
    assert response.routes[0].summary.travelTimeInSeconds > 30
    assert isinstance(response.routes[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].summary.arrivalTime, datetime)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/post_calculate_route.json"], indirect=True)
async def test_deserialization_post_calculate_route(routing_api: RoutingApi) -> None:
    """Test the post_calculate_route method."""
    response = await routing_api.post_calculate_route(
        locations=LatLonList(locations=[LOC_AMSTERDAM, LOC_ROTTERDAM]),
        params=CalculateRouteParams(
            maxAlternatives=0,
            routeType=RouteType.FASTEST,
            traffic=True,
            travelMode=TravelModeType.CAR,
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

    assert response
    assert isinstance(response, CalculatedRouteResponse)
    assert len(response.routes) == 1
    assert response.routes[0].summary
    assert response.routes[0].summary.lengthInMeters > 1000
    assert response.routes[0].summary.travelTimeInSeconds > 30
    assert isinstance(response.routes[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].summary.arrivalTime, datetime)
    assert isinstance(response.routes[0].legs[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].legs[0].summary.arrivalTime, datetime)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/get_calculate_reachable_range.json"], indirect=True)
async def test_deserialization_get_calculate_reachable_range(routing_api: RoutingApi) -> None:
    """Test the get_calculate_reachable_range method."""
    response = await routing_api.get_calculate_reachable_range(
        origin=LOC_AMSTERDAM,
        params=CalculateReachableRouteParams(
            energyBudgetInkWh=43,
            avoid=AvoidType.UNPAVED_ROADS,
            vehicleEngineType=VehicleEngineType.ELECTRIC,
            constantSpeedConsumptionInkWhPerHundredkm="50,8.2:130,21.3",
        ),
    )

    assert response
    assert isinstance(response, CalculatedReachableRangeResponse)
    assert response.reachableRange
    assert response.reachableRange.center
    assert response.reachableRange.center.latitude == 52.50931
    assert response.reachableRange.center.longitude == 13.42937
    assert len(response.reachableRange.boundary) > 1


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/routing/post_calculate_reachable_range.json"], indirect=True)
async def test_deserialization_post_calculate_reachable_range(routing_api: RoutingApi) -> None:
    """Test the post_calculate_reachable_range method."""
    response = await routing_api.post_calculate_reachable_range(
        origin=LOC_AMSTERDAM,
        params=CalculateReachableRouteParams(
            energyBudgetInkWh=43,
            avoid=AvoidType.UNPAVED_ROADS,
            vehicleEngineType=VehicleEngineType.ELECTRIC,
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

    assert response
    assert isinstance(response, CalculatedReachableRangeResponse)
    assert response.reachableRange
    assert response.reachableRange.center
    assert response.reachableRange.center.latitude == 52.50931
    assert response.reachableRange.center.longitude == 13.42937
    assert len(response.reachableRange.boundary) > 1
