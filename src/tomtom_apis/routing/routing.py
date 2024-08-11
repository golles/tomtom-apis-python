"""Routing API"""

from ..api import BaseApi
from ..models import LatLon, LatLonList
from .models import (
    CalculatedReachableRangeResponse,
    CalculatedRouteResponse,
    CalculateReachableRangePostData,
    CalculateReachableRouteParams,
    CalculateRouteParams,
    CalculateRoutePostData,
)


class RoutingApi(BaseApi):
    """
    TomTom Routing is a suite of web services designed for developers to use our latest scalable routing engine.
    - Independent tests have established that the TomTom routing engine is the best in the industry.
    - Our routing engine uses IQ Routes™ and TomTom Traffic™.

    See: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/routing-service
    """

    async def get_calculate_route(
        self,
        *,
        locations: LatLonList,
        params: CalculateRouteParams | None = None,
    ) -> CalculatedRouteResponse:
        """
        The Calculate Route service calculates a route between an origin and a destination, passing through waypoints if they are specified.

        See: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route
        """

        response = await self.get(
            endpoint=f"/routing/1/calculateRoute/{locations.to_colon_seperate()}/json",
            params=params,
        )

        return await response.deserialize(CalculatedRouteResponse)

    async def post_calculate_route(
        self,
        *,
        locations: LatLonList,
        params: CalculateRouteParams | None = None,
        data: CalculateRoutePostData,
    ) -> CalculatedRouteResponse:
        """
        The Calculate Route service calculates a route between an origin and a destination, passing through waypoints if they are specified.

        See: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route
        """

        response = await self.post(
            endpoint=f"/routing/1/calculateRoute/{locations.to_colon_seperate()}/json",
            params=params,
            data=data,
        )

        return await response.deserialize(CalculatedRouteResponse)

    async def get_calculate_reachable_range(
        self,
        *,
        origin: LatLon,
        params: CalculateReachableRouteParams | None = None,
    ) -> CalculatedReachableRangeResponse:
        """
        Calculates a set of locations that can be reached from the origin point.

        See: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-reachable-range
        """

        response = await self.get(
            endpoint=f"/routing/1/calculateReachableRange/{origin.to_comma_seperate()}/json",
            params=params,
        )

        return await response.deserialize(CalculatedReachableRangeResponse)

    async def post_calculate_reachable_range(
        self,
        *,
        origin: LatLon,
        params: CalculateReachableRouteParams | None = None,
        data: CalculateReachableRangePostData,
    ) -> CalculatedReachableRangeResponse:
        """
        Calculates a set of locations that can be reached from the origin point.

        See: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-reachable-range
        """

        response = await self.post(
            endpoint=f"/routing/1/calculateReachableRange/{origin.to_comma_seperate()}/json",
            params=params,
            data=data,
        )

        return await response.deserialize(CalculatedReachableRangeResponse)
