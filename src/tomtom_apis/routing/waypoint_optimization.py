"""Waypoint optimization API."""

from typing import Self

from ..api import BaseApi, BaseParams
from ..routing.models import WaypointOptimizationPostData, WaypointOptimizedResponse


class WaypointOptimizationApi(BaseApi):
    """Waypoint optimization API.

    TomTom's Waypoint Optimization service is intended to optimize the order of provided waypoints by fastest route. This service uses an heuristic
    algorithm to create an optimized sequence.

    For more information, see: https://developer.tomtom.com/waypoint-optimization/documentation/waypoint-optimization-service
    """

    async def post_waypointoptimization(
        self: Self,
        *,
        params: BaseParams | None = None,  # No extra params.
        data: WaypointOptimizationPostData,
    ) -> WaypointOptimizedResponse:
        """Post waypointoptimization.

        For more information, see: https://developer.tomtom.com/waypoint-optimization/documentation/waypoint-optimization

        Args:
            params (BaseParams | None, optional): Optional parameters for the request. Defaults to None.
            data (WaypointOptimizationPostData): Data specifying the waypoints and any optimization criteria.

        Returns:
            WaypointOptimizedResponse: The response containing the optimized order of waypoints.
        """
        response = await self.post(
            endpoint="/routing/waypointoptimization/1",
            params=params,
            data=data,
        )

        return await response.deserialize(WaypointOptimizedResponse)
