"""Map Display API."""

from typing import Self

from ..api import BaseApi, BaseParams
from .models import (
    LayerType,
    LayerTypeWithPoiType,
    MapServiceCopyrightsResponse,
    MapTileParams,
    MapTileV1Params,
    MapTileV2Params,
    StaticImageParams,
    StyleType,
    TileFormatType,
)


class MapDisplayApi(BaseApi):
    """Map Display API.

    The Map Display API is a suite of web services designed for developers to create web and mobile applications around mapping.

    For more information, see: https://developer.tomtom.com/map-display-api/documentation/product-information/introduction
    """

    async def get_map_tile(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        layer: LayerType,
        style: StyleType,
        x: int,
        y: int,
        zoom: int,
        image_format: TileFormatType,
        params: MapTileParams | None = None,
    ) -> bytes:
        """Get map tile.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/raster/map-tile

        Args:
            layer (LayerType): The type of layer for the map tile.
            style (StyleType): The style of the map tile.
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            image_format (TileFormatType): The format of the image.
            params (MapTileParams | None, optional): Additional parameters for the map tile. Defaults to None.

        Returns:
            bytes: The map tile image data.
        """
        response = await self.get(
            endpoint=f"/map/1/tile/{layer}/{style}/{zoom}/{x}/{y}.{image_format}",
            params=params,
        )

        return await response.bytes()

    async def get_satellite_tile(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        x: int,
        y: int,
        zoom: int,
        image_format: TileFormatType,
        params: BaseParams | None = None,  # No extra params.
    ) -> bytes:
        """Get satellite tile.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/raster/satellite-tile

        Args:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            image_format (TileFormatType): The format of the image.
            params (BaseParams | None, optional): Additional parameters for the tile. Defaults to None.

        Returns:
            bytes: The satellite tile image data.
        """
        response = await self.get(
            endpoint=f"/map/1/tile/sat/main/{zoom}/{x}/{y}.{image_format}",
            params=params,
        )

        return await response.bytes()

    async def get_hillshade_tile(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        x: int,
        y: int,
        zoom: int,
        image_format: TileFormatType,
        params: BaseParams | None = None,  # No extra params.
    ) -> bytes:
        """Get hillshade tile.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/raster/hillshade-tile

        Args:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            image_format (TileFormatType): The format of the image.
            params (BaseParams | None, optional): Additional parameters for the hillshade tile. Defaults to None.

        Returns:
            bytes: The hillshade tile image data.
        """
        response = await self.get(
            endpoint=f"/map/1/tile/hill/main/{zoom}/{x}/{y}.{image_format}",
            params=params,
        )

        return await response.bytes()

    async def get_static_image(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        params: StaticImageParams | None = None,
    ) -> bytes:
        """Get static image.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/raster/static-image

        Args:
            layer (LayerType): The type of layer for the map tile.
            style (StyleType): The style of the map tile.
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            image_format (TileFormatType): The format of the image.
            params (MapTileParams | None, optional): Additional parameters for the map tile. Defaults to None.

        Returns:
            bytes: The map tile image data.
        """
        response = await self.get(
            endpoint="/map/1/staticimage",
            params=params,
        )

        return await response.bytes()

    async def get_tile_v1(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        layer: LayerTypeWithPoiType,
        x: int,
        y: int,
        zoom: int,
        params: MapTileV1Params | None = None,
    ) -> bytes:
        """Get tile version 1.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/vector/tile

        Args:
            layer (LayerTypeWithPoiType): The type of layer for the map tile.
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            params (MapTileV1Params | None, optional): Additional parameters for the map tile. Defaults to None.

        Returns:
            bytes: The map tile data in bytes format.
        """
        response = await self.get(
            endpoint=f"/map/1/tile/{layer}/main/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()

    async def get_tile_v2(  # pylint: disable=too-many-arguments
        self: Self,
        *,
        layer: LayerTypeWithPoiType,
        x: int,
        y: int,
        zoom: int,
        params: MapTileV2Params | None = None,
    ) -> bytes:
        """Get tile version 2.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/vector/tile-v2

        Args:
            layer (LayerTypeWithPoiType): The type of layer for the map tile.
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            zoom (int): The zoom level of the tile.
            params (MapTileV2Params | None, optional): Additional parameters for the map tile. Defaults to None.

        Returns:
            bytes: The map tile data in bytes format.
        """
        response = await self.get(
            endpoint=f"/map/1/tile/{layer}/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()

    async def get_map_copyrights(
        self: Self,
        *,
        params: BaseParams | None = None,  # No extra params.
    ) -> str:
        """Get map copyrights.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/copyrights

        Args:
            params (BaseParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            str: The copyright information as a string.
        """
        response = await self.get(
            endpoint="/map/2/copyrights",
            params=params,
        )

        return await response.text()

    async def get_map_service_copyrights(
        self: Self,
        *,
        params: BaseParams | None = None,  # No extra params.
    ) -> MapServiceCopyrightsResponse:
        """Get map service copyrights.

        For more information, see: https://developer.tomtom.com/map-display-api/documentation/copyrights

        Args:
            params (BaseParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            MapServiceCopyrightsResponse: The copyright information response object.
        """
        response = await self.get(
            endpoint="/map/2/copyrights/caption.json",
            params=params,
        )

        return await response.deserialize(MapServiceCopyrightsResponse)
