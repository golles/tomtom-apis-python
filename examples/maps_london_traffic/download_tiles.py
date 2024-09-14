"""London traffic example."""

# pylint: disable=duplicate-code

import asyncio
import os

from tomtom_apis import ApiOptions
from tomtom_apis.maps import MapDisplayApi
from tomtom_apis.maps.models import LayerType, StyleType, TileFormatType
from tomtom_apis.models import MapTile
from tomtom_apis.traffic import TrafficApi
from tomtom_apis.traffic.models import IncidentStyleType, IncidentTileFormatType

SCRIPT_DIR = os.path.dirname(__file__)
TILES: list[MapTile] = [  # a 3x3 grid of London at zoom level 10.
    MapTile(x=510, y=339, zoom=10),
    MapTile(x=511, y=339, zoom=10),
    MapTile(x=512, y=339, zoom=10),
    MapTile(x=510, y=340, zoom=10),
    MapTile(x=511, y=340, zoom=10),
    MapTile(x=512, y=340, zoom=10),
    MapTile(x=510, y=341, zoom=10),
    MapTile(x=511, y=341, zoom=10),
    MapTile(x=512, y=341, zoom=10),
]


async def download_tiles(api: MapDisplayApi | TrafficApi, tiles: list[MapTile]) -> None:
    """Download tiles for a given api.

    Args:
        api (MapDisplayApi | TrafficApi): The API to use for downloading tiles.
        tiles (list[MapTile]): The tiles to download.

    """
    for tile in tiles:
        if isinstance(api, MapDisplayApi):
            image_bytes = await api.get_map_tile(
                layer=LayerType.BASIC,
                style=StyleType.MAIN,
                x=tile.x,
                y=tile.y,
                zoom=tile.zoom,
                image_format=TileFormatType.PNG,
            )
            file_path = os.path.join(SCRIPT_DIR, "tiles", f"main_{tile.zoom}_{tile.x}_{tile.y}.png")
        elif isinstance(api, TrafficApi):
            image_bytes = await api.get_raster_incident_tile(
                style=IncidentStyleType.S1,
                x=tile.x,
                y=tile.y,
                zoom=tile.zoom,
                image_format=IncidentTileFormatType.PNG,
            )
            file_path = os.path.join(SCRIPT_DIR, "tiles", f"incidents_{tile.zoom}_{tile.x}_{tile.y}.png")
        else:
            raise ValueError("Invalid API type provided.")

        with open(file_path, "wb") as file:
            file.write(image_bytes)


async def download(api_key: str) -> None:
    """Download all tiles."""
    options = ApiOptions(api_key=api_key)

    async with MapDisplayApi(options) as map_display_api, TrafficApi(options) as traffic_api:
        await download_tiles(map_display_api, TILES)
        await download_tiles(traffic_api, TILES)


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()
    asyncio.run(download(user_api_key))
