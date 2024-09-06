"""Waypoint optimization API"""

from ..api import BaseApi, BaseParams
from ..routing.models import WaypointOptimizationPostData, WaypointOptimizedResponse


class WaypointOptimizationApi(BaseApi):
    """
    TomTom's Waypoint Optimization service is intended to optimize the order of provided waypoints by fastest route. This service uses an heuristic
    algorithm to create an optimized sequence.

    See: https://developer.tomtom.com/waypoint-optimization/documentation/waypoint-optimization-service
    """

    async def post_waypointoptimization(
        self,
        *,
        params: BaseParams | None = None,  # No extra params.
        data: WaypointOptimizationPostData,
    ) -> WaypointOptimizedResponse:
        """
        This endpoint optimizes a provided waypoints sequence based on road network distances. Sequence is ordered to form the fastest route.

        See: https://developer.tomtom.com/waypoint-optimization/documentation/waypoint-optimization
        """

        response = await self.post(
            endpoint="/routing/waypointoptimization/1",
            params=params,
            data=data,
        )

        return await response.deserialize(WaypointOptimizedResponse)
