"""Long Distance EV Routing API"""

from ..api import BaseApi
from ..models import LatLonList
from .models import CalculatedLongDistanceEVRouteResponse, CalculateLongDistanceEVRouteParams, CalculateLongDistanceEVRoutePostData


class LongDistanceEVRoutingApi(BaseApi):
    """
    The Long Distance EV Routing service endpoint calculates a route between a given origin and destination, passing through waypoints if they are
    specified. The route contains charging stops that have been added automatically based on the vehicle's consumption and charging model.

    See: https://developer.tomtom.com/long-distance-ev-routing-api/documentation/tomtom-maps/product-information/introduction
    """

    async def post_calculate_long_distance_ev_route(
        self,
        *,
        locations: LatLonList,
        params: CalculateLongDistanceEVRouteParams | None = None,
        data: CalculateLongDistanceEVRoutePostData,
    ) -> CalculatedLongDistanceEVRouteResponse:
        """
        The Long Distance EV Routing service endpoint calculates a route between a given origin and destination, passing through waypoints if they
        are specified. The route contains charging stops that have been added automatically based on the vehicle's consumption and charging model.

        See: https://developer.tomtom.com/long-distance-ev-routing-api/documentation/tomtom-maps/product-information/introduction
        """

        response = await self.post(
            endpoint=f"/routing/1/calculateLongDistanceEVRoute/{locations.to_colon_seperate()}/json",
            params=params,
            data=data,
        )

        return await response.deserialize(CalculatedLongDistanceEVRouteResponse)
