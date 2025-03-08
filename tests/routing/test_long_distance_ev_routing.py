"""Long Distance EV Routing tests."""

from collections.abc import AsyncGenerator
from datetime import datetime

import pytest

from tests.const import API_KEY, LOC_AMSTERDAM
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import LatLonList
from tomtom_apis.routing import LongDistanceEVRoutingApi
from tomtom_apis.routing.models import (
    CalculatedLongDistanceEVRouteResponse,
    CalculateLongDistanceEVRouteParams,
    CalculateLongDistanceEVRoutePostData,
    ChargingConnection,
    ChargingCurve,
    ChargingMode,
    FacilityType,
    PlugType,
    VehicleEngineType,
)


@pytest.fixture(name="long_distance_ev_routing_api")
async def fixture_long_distance_ev_routing_api() -> AsyncGenerator[LongDistanceEVRoutingApi]:
    """Fixture for LongDistanceEVRoutingApi."""
    options = ApiOptions(api_key=API_KEY)
    async with LongDistanceEVRoutingApi(options) as long_distance_ev_routing:
        yield long_distance_ev_routing


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["routing/long_distance_ev_routing/post_calculate_long_distance_ev_route.json"], indirect=True)
async def test_deserialization_post_calculate_long_distance_ev_route(long_distance_ev_routing_api: LongDistanceEVRoutingApi) -> None:
    """Test the post_calculate_long_distance_ev_route method."""
    params = CalculateLongDistanceEVRouteParams(
        vehicleEngineType=VehicleEngineType.ELECTRIC,
        constantSpeedConsumptionInkWhPerHundredkm="50.0,6.5:100.0,8.5",
        currentChargeInkWh=10,
        maxChargeInkWh=40,
        minChargeAtDestinationInkWh=5.2,
        minChargeAtChargingStopsInkWh=1.5,
    )

    data = CalculateLongDistanceEVRoutePostData(
        chargingModes=[
            ChargingMode(
                chargingConnections=[
                    ChargingConnection(
                        facilityType=FacilityType.CHARGE_380_TO_480V_3_PHASE_AT_32A,
                        plugType=PlugType.IEC_62196_TYPE_2_OUTLET,
                    )
                ],
                chargingCurve=[
                    ChargingCurve(chargeInkWh=6, timeToChargeInSeconds=360),
                    ChargingCurve(chargeInkWh=12, timeToChargeInSeconds=720),
                    ChargingCurve(chargeInkWh=28, timeToChargeInSeconds=1944),
                    ChargingCurve(chargeInkWh=40, timeToChargeInSeconds=4680),
                ],
            ),
            ChargingMode(
                chargingConnections=[
                    ChargingConnection(
                        facilityType=FacilityType.CHARGE_200_TO_240V_1_PHASE_AT_10A,
                        plugType=PlugType.STANDARD_HOUSEHOLD_COUNTRY_SPECIFIC,
                    )
                ],
                chargingCurve=[
                    ChargingCurve(chargeInkWh=6, timeToChargeInSeconds=15624),
                    ChargingCurve(chargeInkWh=12, timeToChargeInSeconds=32652),
                    ChargingCurve(chargeInkWh=28, timeToChargeInSeconds=76248),
                    ChargingCurve(chargeInkWh=40, timeToChargeInSeconds=109080),
                ],
            ),
        ]
    )

    response = await long_distance_ev_routing_api.post_calculate_long_distance_ev_route(
        locations=LatLonList(locations=[LOC_AMSTERDAM]),
        params=params,
        data=data,
    )

    assert response
    assert isinstance(response, CalculatedLongDistanceEVRouteResponse)
    assert len(response.routes) == 1
    assert response.routes[0].summary
    assert response.routes[0].summary.lengthInMeters > 500000
    assert response.routes[0].summary.travelTimeInSeconds > 10000
    assert response.routes[0].summary.batteryConsumptionInkWh > 30
    assert response.routes[0].summary.remainingChargeAtArrivalInkWh > 4
    assert response.routes[0].summary.totalChargingTimeInSeconds > 3000
    assert isinstance(response.routes[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].summary.arrivalTime, datetime)
    assert isinstance(response.routes[0].legs[0].summary.departureTime, datetime)
    assert isinstance(response.routes[0].legs[0].summary.arrivalTime, datetime)
