"""Traffic API"""

from tomtom_apis.utils import serialize_list

from ..api import BaseApi, BaseParams
from .models import (
    BBoxParam,
    BoudingBoxParam,
    FlowSegmentDataParams,
    FlowSegmentDataResponse,
    FlowStyleType,
    FlowType,
    IncidentDetailsParams,
    IncidentDetailsPostData,
    IncidentDetailsResponse,
    IncidentStyleType,
    IncidentViewportResponse,
    RasterFlowTilesParams,
    RasterIncidentTilesParams,
    VectorFlowTilesParams,
    VectorIncidentTilesParams,
)


class TrafficApi(BaseApi):
    """
    The Traffic API is a suite of web services designed for developers to create web and mobile applications around real-time traffic. These web
    services can be used via RESTful APIs. The TomTom Traffic team offers a wide range of solutions to enable you to get the most out of your
    applications. Make use of the real-time traffic products or the historical traffic analytics to create applications and analysis that fits the
    needs of your end-users.

    See: https://developer.tomtom.com/traffic-api/documentation/product-information/introduction
    """

    async def get_incident_details(
        self,
        *,
        bbox: BBoxParam | None = None,
        ids: list[str] | None = None,
        params: IncidentDetailsParams | None = None,
    ) -> IncidentDetailsResponse:
        """
        The Incident Details service provides information on traffic incidents which are inside a given bounding box or whose geometry intersects
        with it. The freshness of data is based on the provided Traffic Model ID (t). The data obtained from this service can be used as standalone
        or as an extension to other Traffic Incident services.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-details
        """

        if bbox and not ids:
            mutually_exclusive_parameters = f"bbox={bbox.to_comma_seperate()}"
        elif ids and not bbox:
            mutually_exclusive_parameters = f"ids={serialize_list(list(ids))}"
        else:
            raise ValueError("bbox and ids are mutually exclusive parameters")

        response = await self.get(
            endpoint=f"/traffic/services/5/incidentDetails?{mutually_exclusive_parameters}",
            params=params,
        )

        return await response.deserialize(IncidentDetailsResponse)

    async def post_incident_details(
        self,
        *,
        params: IncidentDetailsParams | None = None,
        data: IncidentDetailsPostData,
    ) -> IncidentDetailsResponse:
        """
        The Incident Details service provides information on traffic incidents which are inside a given bounding box or whose geometry intersects
        with it. The freshness of data is based on the provided Traffic Model ID (t). The data obtained from this service can be used as standalone
        or as an extension to other Traffic Incident services.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-details
        """

        response = await self.post(
            endpoint="/traffic/services/5/incidentDetails",
            params=params,
            data=data,
        )

        return await response.deserialize(IncidentDetailsResponse)

    async def get_incident_viewport(  # pylint: disable=too-many-arguments
        self,
        *,
        bounding_box: BoudingBoxParam,
        bounding_zoom: int,
        overview_box: BoudingBoxParam,
        overview_zoom: int,
        copyright_information: bool,
        params: BaseParams | None = None,  # No extra params.
    ) -> IncidentViewportResponse:
        """
        This service returns legal and technical information for the viewport described in the request. It should be called by client applications
        whenever the viewport changes (for instance, through zooming, panning, going to a location, or displaying a route).

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-viewport
        """
        response = await self.get(
            endpoint=(
                f"/traffic/services/4/incidentViewport/{bounding_box.to_comma_seperate()}/"
                f"{bounding_zoom}/{overview_box.to_comma_seperate()}/"
                f"{overview_zoom}/{copyright_information}/json"
            ),
            params=params,
        )

        return await response.deserialize(IncidentViewportResponse)

    async def get_raster_incident_tile(  # pylint: disable=too-many-arguments
        self,
        *,
        style: IncidentStyleType,
        x: int,
        y: int,
        zoom: int,
        params: RasterIncidentTilesParams | None = None,
    ) -> bytes:
        """
        The TomTom Traffic Tile service serves 256 x 256 pixel or 512 x 512 pixel tiles showing traffic incidents. All tiles use the same grid
        system. Because the traffic tiles use transparent images, they can be layered on top of map tiles to create a compound display. Traffic tiles
        render graphics to indicate traffic on the roads in the specified area. The Traffic incidents tiles use colors to indicate the magnitude of
        delay associated with the particular incident on a road segment. The magnitude of delay is determined based on the severity of traffic
        congestion associated with the particular incident.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/raster-incident-tiles
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/incidents/{style.value}/{zoom}/{x}/{y}.png",
            params=params,
        )

        return await response.bytes()

    async def get_vector_incident_tile(
        self,
        *,
        x: int,
        y: int,
        zoom: int,
        params: VectorIncidentTilesParams | None = None,
    ) -> bytes:
        """
        The Traffic Vector Incidents Tiles API provides data on zoom levels ranging from 0 to 22. For zoom level 0, the world is displayed on a
        single tile, while at zoom level 22, the world is divided into 244 tiles. See: Zoom Levels and Tile Grid.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/vector-incident-tiles
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/incidents/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()

    async def get_flow_segment_data(
        self,
        *,
        style: FlowStyleType,
        zoom: int,
        point: str,
        params: FlowSegmentDataParams | None = None,
    ) -> FlowSegmentDataResponse:
        """
        This service provides information about the speeds and travel times of the road fragment closest to the given coordinates. It is designed to
        work alongside the Flow Tiles to support clickable flow data visualizations. With this API, the client side can connect any place in the map
        with flow data on the closest road and present it to the user.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-flow/flow-segment-data
        """
        response = await self.get(
            endpoint=f"/traffic/services/4/flowSegmentData/{style}/{zoom}/json?point={point}",
            params=params,
        )

        return await response.deserialize(FlowSegmentDataResponse)

    async def get_raster_flow_tiles(  # pylint: disable=too-many-arguments
        self,
        *,
        style: FlowStyleType,
        zoom: int,
        x: int,
        y: int,
        params: RasterFlowTilesParams | None = None,
    ) -> bytes:
        """
        The TomTom Traffic Raster Flow Tile service serves 256 x 256 pixel or 512 x 512 pixel tiles showing traffic flow. All tiles use the same grid
        system. Because the traffic tiles use transparent images, they can be layered on top of map tiles to create a compound display. The Raster
        Flow tiles use colors to indicate either the speed of traffic on different road segments, or the difference between that speed and the
        free-flow speed on the road segment in question.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-flow/raster-flow-tiles
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/flow/{style}/{zoom}/{x}/{y}.png",
            params=params,
        )

        return await response.bytes()

    async def get_vector_flow_tiles(  # pylint: disable=too-many-arguments
        self,
        *,
        flow_type: FlowType,
        zoom: int,
        x: int,
        y: int,
        params: VectorFlowTilesParams | None = None,
    ) -> bytes:
        """
        The Traffic Vector Flow Tiles API endpoint provides data on zoom levels ranging from 0 to 22. For zoom level 0, the world is displayed on a
        single tile. At zoom level 22, the world is divided into 244 tiles. See the Zoom Levels and Tile Grid.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-flow/vector-flow-tiles
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/flow/{flow_type}/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()
