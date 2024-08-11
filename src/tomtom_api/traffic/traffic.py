"""Traffic API"""

from ..api import BaseApi, BaseParams, BasePostData
from .models import BBoxParam, BoudingBoxParam, IncidentStyleType, RasterIncidentTilesParams, VectorIncidentTilesParams


class TrafficApi(BaseApi):
    """
    The Traffic API is a suite of web services designed for developers to create web and mobile applications around real-time traffic. These web services can be used via RESTful APIs. The TomTom Traffic team offers a wide range of solutions to enable you to get the most out of your applications. Make use of the real-time traffic products or the historical traffic analytics to create applications and analysis that fits the needs of your end-users.

    See: https://developer.tomtom.com/traffic-api/documentation/product-information/introduction
    """

    async def get_incident_details(
        self,
        *,
        bbox: BBoxParam,
        params: BaseParams | None = None,  # fields, language, t, categoryFilter, timeValidityFilter
    ) -> dict:
        """
        The Incident Details service provides information on traffic incidents which are inside a given bounding box or whose geometry intersects with it. The freshness of data is based on the provided Traffic Model ID (t). The data obtained from this service can be used as standalone or as an extension to other Traffic Incident services.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-details
        """

        response = await self.get(
            endpoint=f"/traffic/services/5/incidentDetails?bbox={bbox.to_comma_seperate()}",
            params=params,
        )

        return await response.dict()

    async def post_incident_details(
        self,
        *,
        params: BaseParams | None = None,
        data: BasePostData,
    ) -> dict:
        """
        The Incident Details service provides information on traffic incidents which are inside a given bounding box or whose geometry intersects with it. The freshness of data is based on the provided Traffic Model ID (t). The data obtained from this service can be used as standalone or as an extension to other Traffic Incident services.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-details
        """

        response = await self.post(
            endpoint="/traffic/services/5/incidentDetails",
            params=params,
            data=data,
        )

        return await response.dict()

    async def get_incident_viewport(  # pylint: disable=too-many-arguments
        self,
        *,
        bounding_box: BoudingBoxParam,
        bounding_zoom: int,
        overview_box: BoudingBoxParam,
        overview_zoom: int,
        copyright_information: bool,
        params: BaseParams | None = None,  # No extra params.
    ) -> dict:
        """
        This service returns legal and technical information for the viewport described in the request. It should be called by client applications whenever the viewport changes (for instance, through zooming, panning, going to a location, or displaying a route).

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-viewport
        """
        response = await self.get(
            endpoint=f"/traffic/services/4/incidentViewport/{bounding_box.to_comma_seperate()}/{bounding_zoom}/{overview_box.to_comma_seperate()}/{overview_zoom}/{copyright_information}/json",
            params=params,
        )

        return await response.dict()

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
        The TomTom Traffic Tile service serves 256 x 256 pixel or 512 x 512 pixel tiles showing traffic incidents. All tiles use the same grid system. Because the traffic tiles use transparent images, they can be layered on top of map tiles to create a compound display. Traffic tiles render graphics to indicate traffic on the roads in the specified area. The Traffic incidents tiles use colors to indicate the magnitude of delay associated with the particular incident on a road segment. The magnitude of delay is determined based on the severity of traffic congestion associated with the particular incident.

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
        The Traffic Vector Incidents Tiles API provides data on zoom levels ranging from 0 to 22. For zoom level 0, the world is displayed on a single tile, while at zoom level 22, the world is divided into 244 tiles. See: Zoom Levels and Tile Grid.

        See: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/vector-incident-tiles
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/incidents/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()
