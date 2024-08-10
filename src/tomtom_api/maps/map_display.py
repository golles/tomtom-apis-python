"""Map Display AP"""

from tomtom_api.api import BaseApi, BaseParams

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
    """
    The Map Display API is a suite of web services designed for developers to create web and mobile applications around mapping. These web services can be used via RESTful APIs.

    See: https://developer.tomtom.com/map-display-api/documentation/product-information/introduction
    """

    async def get_map_tile(  # pylint: disable=too-many-arguments
        self,
        *,
        layer: LayerType,
        style: StyleType,
        x: int,
        y: int,
        zoom: int,
        image_format: TileFormatType,
        params: MapTileParams | None = None,
    ) -> bytes:
        """
        The Maps Raster Tile API endpoint renders map data that is divided into gridded sections called tiles. Tiles are square images in various sizes which are available at 23 different zoom levels, ranging from 0 to 22. For zoom level 0, the entire earth is displayed on one single tile, while at zoom level 22, the world is divided into 244 tiles. See the Zoom Levels and Tile Grid.

        See: https://developer.tomtom.com/map-display-api/documentation/raster/map-tile
        """

        response = await self.get(
            endpoint=f"/map/1/tile/{layer.value}/{style.value}/{zoom}/{x}/{y}.{image_format.value}",
            params=params,
        )

        return await response.bytes()

    async def get_satellite_tile(  # pylint: disable=too-many-arguments
        self,
        *,
        x: int,
        y: int,
        zoom: int,
        image_format: TileFormatType,
        params: BaseParams | None = None,  # No extra params.
    ) -> bytes:
        """
        The Maps Raster Satellite Tile API endpoint provides satellite map data that is divided into gridded sections called tiles. Tiles are square images with a size of: 256 x 256 pixels. The tiles are available at 20 different zoom levels, ranging from 0 to 19. For zoom level 0, the entire earth is displayed on one single tile, while at zoom level 19, the world is divided into 238 tiles. See the: Zoom Levels and Tile Grid.

        See: https://developer.tomtom.com/map-display-api/documentation/raster/satellite-tile
        """

        response = await self.get(
            endpoint=f"/map/1/tile/sat/main/{zoom}/{x}/{y}.{image_format.value}",
            params=params,
        )

        return await response.bytes()

    async def get_hillshade_tile(  # pylint: disable=too-many-arguments
        self,
        *,
        x: int,
        y: int,
        zoom: int,
        image_format: TileFormatType,
        params: BaseParams | None = None,  # No extra params.
    ) -> bytes:
        """
        The Maps Raster Hillshade Tile API endpoint provides terrain elevation data that is divided into gridded sections called tiles. It can be used for rendering hillshade that shows the topographical shape of hills and mountains. Tiles are square images with a size of: 514 x 514 pixels. The tiles are available at 14 different zoom levels, ranging from 0 to 13. See the: Zoom Levels and Tile Grid.

        See: https://developer.tomtom.com/map-display-api/documentation/raster/hillshade-tile
        """

        response = await self.get(
            endpoint=f"/map/1/tile/hill/main/{zoom}/{x}/{y}.{image_format.value}",
            params=params,
        )

        return await response.bytes()

    async def get_static_image(  # pylint: disable=too-many-arguments
        self,
        *,
        params: StaticImageParams | None = None,
    ) -> bytes:
        """
        The Static Image service renders a user-defined, rectangular image containing a map section. A user can select one of 23 zoom levels ranging from 0 to 22 for it.

        See: https://developer.tomtom.com/map-display-api/documentation/raster/static-image
        """

        response = await self.get(
            endpoint="/map/1/staticimage",
            params=params,
        )

        return await response.bytes()

    async def get_tile_v1(  # pylint: disable=too-many-arguments
        self,
        *,
        layer: LayerTypeWithPoiType,
        x: int,
        y: int,
        zoom: int,
        params: MapTileV1Params | None = None,
    ) -> bytes:
        """
        The Maps Vector Service delivers geographic map data packaged in a vector representation of squared sections called vector tiles. Each tile includes pre-defined collections of map features (points, lines, road shapes, water polygons, building footprints, etc.) delivered in one of the specified vector formats.

        See: https://developer.tomtom.com/map-display-api/documentation/vector/tile
        """
        response = await self.get(
            endpoint=f"/map/1/tile/{layer.value}/main/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()

    async def get_tile_v2(  # pylint: disable=too-many-arguments
        self,
        *,
        layer: LayerTypeWithPoiType,
        x: int,
        y: int,
        zoom: int,
        params: MapTileV2Params | None = None,
    ) -> bytes:
        """
        The Maps Vector Service delivers geographic map data packaged in a vector representation of squared sections called vector tiles.

        See: https://developer.tomtom.com/map-display-api/documentation/vector/tile-v2
        """
        response = await self.get(
            endpoint=f"/map/1/tile/{layer.value}/{zoom}/{x}/{y}.pbf",
            params=params,
        )

        return await response.bytes()

    async def get_map_copyrights(
        self,
        *,
        params: BaseParams | None = None,  # No extra params.
    ) -> str:
        """
        The Copyrights API is designed to serve copyright information for the Map Display services. As an alternative to copyrights for map request, you can receive copyrights for the map service called captions.

        See: https://developer.tomtom.com/map-display-api/documentation/copyrights
        """

        response = await self.get(
            endpoint="/map/2/copyrights",
            params=params,
        )

        return await response.text()

    async def get_map_service_copyrights(
        self,
        *,
        params: BaseParams | None = None,  # No extra params.
    ) -> MapServiceCopyrightsResponse:
        """
        The Copyrights API is designed to serve copyright information for the Map Display services. As an alternative to copyrights for map request, you can receive copyrights for the map service called captions.

        See: https://developer.tomtom.com/map-display-api/documentation/copyrights
        """

        response = await self.get(
            endpoint="/map/2/copyrights/caption.json",
            params=params,
        )

        return await response.deserialize(MapServiceCopyrightsResponse)
