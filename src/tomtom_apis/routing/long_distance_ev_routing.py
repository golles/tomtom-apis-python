"""Long Distance EV Routing API."""

from typing import Self

from ..api import BaseApi
from ..models import LatLonList
from .models import CalculatedLongDistanceEVRouteResponse, CalculateLongDistanceEVRouteParams, CalculateLongDistanceEVRoutePostData


class LongDistanceEVRoutingApi(BaseApi):
    """Long Distance EV Routing API.

    The Long Distance EV Routing service endpoint calculates a route between a given origin and destination, passing through waypoints if they are
    specified. The route contains charging stops that have been added automatically based on the vehicle's consumption and charging model.

    For more information, see: https://developer.tomtom.com/long-distance-ev-routing-api/documentation/tomtom-maps/product-information/introduction
    """

    async def post_calculate_long_distance_ev_route(
        self: Self,
        *,
        locations: LatLonList,
        params: CalculateLongDistanceEVRouteParams | None = None,
        data: CalculateLongDistanceEVRoutePostData,
    ) -> CalculatedLongDistanceEVRouteResponse:
        """Get long distance ev route.

        For more information, see:
        https://developer.tomtom.com/long-distance-ev-routing-api/documentation/tomtom-maps/product-information/introduction

        Args:
            locations (LatLonList): A list of locations to include in the route.
            params (CalculateLongDistanceEVRouteParams | None, optional): Additional parameters for the route calculation. Defaults to None.
            data (CalculateLongDistanceEVRoutePostData): Data specifying route details and constraints.

        Returns:
            CalculatedLongDistanceEVRouteResponse: The response containing the calculated long-distance EV route.
        """
        response = await self.post(
            endpoint=f"/routing/1/calculateLongDistanceEVRoute/{locations.to_colon_separated()}/json",
            params=params,
            data=data,
        )

        return await response.deserialize(CalculatedLongDistanceEVRouteResponse)
