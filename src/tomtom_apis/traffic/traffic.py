"""Traffic API."""

from typing import Self

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
    IncidentTileFormatType,
    IncidentViewportResponse,
    RasterFlowTilesParams,
    RasterIncidentTilesParams,
    VectorFlowTilesParams,
    VectorIncidentTilesParams,
)


class TrafficApi(BaseApi):
    """Traffic API.

    The Traffic API is a suite of web services designed for developers to create web and mobile applications around real-time traffic. These web
    services can be used via RESTful APIs. The TomTom Traffic team offers a wide range of solutions to enable you to get the most out of your
    applications. Make use of the real-time traffic products or the historical traffic analytics to create applications and analysis that fits the
    needs of your end-users.

    For more information, see: https://developer.tomtom.com/traffic-api/documentation/product-information/introduction
    """

    async def get_incident_details(
        self: Self,
        *,
        bbox: BBoxParam | None = None,
        ids: list[str] | None = None,
        params: IncidentDetailsParams | None = None,
    ) -> IncidentDetailsResponse:
        """Get incident details.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-details

        Args:
            bbox (BBoxParam | None, optional): The bounding box to filter incidents by location. Defaults to None.
            ids (list[str] | None, optional): A list of incident IDs to retrieve details for. Defaults to None.
            params (IncidentDetailsParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            IncidentDetailsResponse: The response containing details of the traffic incidents.

        Raises:
            ValueError: If both `bbox` and `ids` are provided or neither is provided.
        """
        if bbox and not ids:
            mutually_exclusive_parameters = f"bbox={bbox.to_comma_separated()}"
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
        self: Self,
        *,
        params: IncidentDetailsParams | None = None,
        data: IncidentDetailsPostData,
    ) -> IncidentDetailsResponse:
        """Post incident details.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-details

        Args:
            params (IncidentDetailsParams | None, optional): Additional parameters for the request. Defaults to None.
            data (IncidentDetailsPostData): Data containing the incident details to be posted.

        Returns:
            IncidentDetailsResponse: The response containing the result of the posted incident details.
        """
        response = await self.post(
            endpoint="/traffic/services/5/incidentDetails",
            params=params,
            data=data,
        )

        return await response.deserialize(IncidentDetailsResponse)

    async def get_incident_viewport(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        bounding_box: BoudingBoxParam,
        bounding_zoom: int,
        overview_box: BoudingBoxParam,
        overview_zoom: int,
        copyright_information: bool,
        params: BaseParams | None = None,  # No extra params.
    ) -> IncidentViewportResponse:
        """Get incident viewport.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/incident-viewport

        Args:
            bounding_box (BoudingBoxParam): The bounding box defining the primary viewport for incidents.
            bounding_zoom (int): The zoom level for the primary viewport.
            overview_box (BoudingBoxParam): The bounding box defining the overview viewport.
            overview_zoom (int): The zoom level for the overview viewport.
            copyright_information (bool): Flag to include copyright information in the response.
            params (BaseParams | None, optional): Optional parameters for the request. Defaults to None.

        Returns:
            IncidentViewportResponse: The response containing details of traffic incidents within the defined viewport.
        """
        response = await self.get(
            endpoint=(
                f"/traffic/services/4/incidentViewport/{bounding_box.to_comma_separated()}/"
                f"{bounding_zoom}/{overview_box.to_comma_separated()}/"
                f"{overview_zoom}/{copyright_information}/json"
            ),
            params=params,
        )

        return await response.deserialize(IncidentViewportResponse)

    async def get_raster_incident_tile(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        style: IncidentStyleType,
        x: int,
        y: int,
        zoom: int,
        image_format: IncidentTileFormatType,
        params: RasterIncidentTilesParams | None = None,
    ) -> bytes:
        """Get raster incident tile.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/raster-incident-tiles

        Args:
            style (IncidentStyleType): The style of the incident tile (e.g., default or custom style).
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            image_format (IncidentTileFormatType): The format of the image.
            params (RasterIncidentTilesParams | None, optional): Optional parameters for the request. Defaults to None.

        Returns:
            bytes: The raster image tile in PNG format.
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/incidents/{style}/{zoom}/{x}/{y}.{image_format}",
            params=params,
        )

        return await response.bytes()

    async def get_vector_incident_tile(
        self: Self,
        *,
        x: int,
        y: int,
        zoom: int,
        params: VectorIncidentTilesParams | None = None,
    ) -> bytes:
        """Get vector incident tile.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/vector-incident-tiles

        Args:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            params (VectorIncidentTilesParams | None, optional): Optional parameters for the request. Defaults to None.

        Returns:
            bytes: The vector tile in PBF format.
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/incidents/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()

    async def get_flow_segment_data(
        self: Self,
        *,
        style: FlowStyleType,
        zoom: int,
        point: str,
        params: FlowSegmentDataParams | None = None,
    ) -> FlowSegmentDataResponse:
        """Get flow segment data.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-flow/flow-segment-data

        Args:
            style (FlowStyleType): The style of the flow segment data (e.g., default or custom style).
            zoom (int): The zoom level for the flow segment data.
            point (str): The coordinates of the point of interest, specified as a string.
            params (FlowSegmentDataParams | None, optional): Optional parameters for the request. Defaults to None.

        Returns:
            FlowSegmentDataResponse: The response containing traffic flow segment data.
        """
        response = await self.get(
            endpoint=f"/traffic/services/4/flowSegmentData/{style}/{zoom}/json?point={point}",
            params=params,
        )

        return await response.deserialize(FlowSegmentDataResponse)

    async def get_raster_flow_tiles(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        style: FlowStyleType,
        zoom: int,
        x: int,
        y: int,
        params: RasterFlowTilesParams | None = None,
    ) -> bytes:
        """Get raster flow tiles.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-flow/raster-flow-tiles

        Args:
            style (FlowStyleType): The style of the flow tile (e.g., default or custom style).
            zoom (int): The zoom level of the tile.
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            params (RasterFlowTilesParams | None, optional): Optional parameters for the request. Defaults to None.

        Returns:
            bytes: The raster image tile in PNG format.
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/flow/{style}/{zoom}/{x}/{y}.png",
            params=params,
        )

        return await response.bytes()

    async def get_vector_flow_tiles(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        flow_type: FlowType,
        zoom: int,
        x: int,
        y: int,
        params: VectorFlowTilesParams | None = None,
    ) -> bytes:
        """Get vector flow tiles.

        For more information, see: https://developer.tomtom.com/traffic-api/documentation/traffic-flow/vector-flow-tiles

        Args:
            flow_type (FlowType): The type of flow data to retrieve (e.g., current or historical flow).
            zoom (int): The zoom level of the tile.
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            params (VectorFlowTilesParams | None, optional): Optional parameters for the request. Defaults to None.

        Returns:
            bytes: The vector tile in PBF format.
        """
        response = await self.get(
            endpoint=f"/traffic/map/4/tile/flow/{flow_type}/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()
