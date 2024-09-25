"""Routing API."""

from typing import Self

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
    """Routing API.

    TomTom Routing is a suite of web services designed for developers to use our latest scalable routing engine.

    For more information, see: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/routing-service
    """

    async def get_calculate_route(
        self: Self,
        *,
        locations: LatLonList,
        params: CalculateRouteParams | None = None,
    ) -> CalculatedRouteResponse:
        """Get calculate route.

        For more information, see: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route
        """
        response = await self.get(
            endpoint=f"/routing/1/calculateRoute/{locations.to_colon_separated()}/json",
            params=params,
        )

        return await response.deserialize(CalculatedRouteResponse)

    async def post_calculate_route(
        self: Self,
        *,
        locations: LatLonList,
        params: CalculateRouteParams | None = None,
        data: CalculateRoutePostData,
    ) -> CalculatedRouteResponse:
        """Post calculate route.

        For more information, see: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route

        Args:
            locations (LatLonList): A list of locations to include in the route.
            params (CalculateRouteParams | None, optional): Additional parameters for route calculation. Defaults to None.
            data (CalculateRoutePostData): Data specifying route details and constraints.

        Returns:
            CalculatedRouteResponse: The response containing the calculated route details.
        """
        response = await self.post(
            endpoint=f"/routing/1/calculateRoute/{locations.to_colon_separated()}/json",
            params=params,
            data=data,
        )

        return await response.deserialize(CalculatedRouteResponse)

    async def get_calculate_reachable_range(
        self: Self,
        *,
        origin: LatLon,
        params: CalculateReachableRouteParams | None = None,
    ) -> CalculatedReachableRangeResponse:
        """Get calculate reachable range.

        For more information, see: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-reachable-range

        Args:
            origin (LatLon): The origin point from which the reachable range is calculated.
            params (CalculateReachableRouteParams | None, optional): Additional parameters for the calculation. Defaults to None.

        Returns:
            CalculatedReachableRangeResponse: The response containing the details of the reachable range from the origin.
        """
        response = await self.get(
            endpoint=f"/routing/1/calculateReachableRange/{origin.to_comma_separated()}/json",
            params=params,
        )

        return await response.deserialize(CalculatedReachableRangeResponse)

    async def post_calculate_reachable_range(
        self: Self,
        *,
        origin: LatLon,
        params: CalculateReachableRouteParams | None = None,
        data: CalculateReachableRangePostData,
    ) -> CalculatedReachableRangeResponse:
        """Post calculate reachable range.

        For more information, see: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-reachable-range

        Args:
            origin (LatLon): The origin point from which the reachable range is calculated.
            params (CalculateReachableRouteParams | None, optional): Additional parameters for the calculation. Defaults to None.
            data (CalculateReachableRangePostData): Data specifying details for the reachable range calculation.

        Returns:
            CalculatedReachableRangeResponse: The response containing the details of the reachable range from the origin.
        """
        response = await self.post(
            endpoint=f"/routing/1/calculateReachableRange/{origin.to_comma_separated()}/json",
            params=params,
            data=data,
        )

        return await response.deserialize(CalculatedReachableRangeResponse)
