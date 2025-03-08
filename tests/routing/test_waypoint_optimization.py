"""Waypoint Optimization tests."""

from collections.abc import AsyncGenerator

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.routing import WaypointOptimizationApi
from tomtom_apis.routing.models import WaypointOptimizationPostData, WaypointOptimizedResponse


@pytest.fixture(name="waypoint_optimization_api")
async def fixture_waypoint_optimization_api() -> AsyncGenerator[WaypointOptimizationApi]:
    """Fixture for WaypointOptimizationApi."""
    options = ApiOptions(api_key=API_KEY)
    async with WaypointOptimizationApi(options) as waypoint_optimization:
        yield waypoint_optimization


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/waypoint_optimization/post_waypointoptimization.json"], indirect=True)
async def test_deserialization_post_waypointoptimization(waypoint_optimization_api: WaypointOptimizationApi) -> None:
    """Test the post_waypointoptimization method."""
    response = await waypoint_optimization_api.post_waypointoptimization(
        data=WaypointOptimizationPostData.from_dict(
            {
                "waypoints": [
                    {"point": {"longitude": 16.90497409165738, "latitude": 52.41111094318538}},
                    {"point": {"longitude": 16.90709715173861, "latitude": 52.410666138418065}},
                    {"point": {"longitude": 16.909298155957515, "latitude": 52.410228259481045}},
                    {"point": {"longitude": 16.907319287272202, "latitude": 52.41061316108531}},
                    {"point": {"longitude": 16.910996727064912, "latitude": 52.41041397793927}},
                    {"point": {"longitude": 16.911123756099897, "latitude": 52.41066703462286}},
                    {"point": {"longitude": 16.90941955426868, "latitude": 52.41122957918256}},
                ],
                "options": {
                    "travelMode": "truck",
                    "vehicleMaxSpeed": 110,
                    "vehicleWeight": 36000,
                    "vehicleAxleWeight": 6000,
                    "vehicleLength": 16.2,
                    "vehicleWidth": 2.4,
                    "vehicleHeight": 3.8,
                    "vehicleCommercial": True,
                    "vehicleLoadType": ["USHazmatClass3", "otherHazmatExplosive"],
                    "vehicleAdrTunnelRestrictionCode": "B",
                },
            }
        ),
    )

    assert response
    assert isinstance(response, WaypointOptimizedResponse)
    assert len(response.optimizedOrder) == 7
    assert response.optimizedOrder == [0, 5, 4, 2, 3, 1, 6]
