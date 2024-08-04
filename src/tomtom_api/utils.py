"""Generic utils"""

import math

from tomtom_api.models import LatLon, MapTile

# Constants
MIN_ZOOM_LEVEL = 0
MAX_ZOOM_LEVEL = 22
MIN_LAT = -85.051128779807
MAX_LAT = 85.051128779806
MIN_LON = -180.0
MAX_LON = 180.0


def lat_lon_to_tile_zxy(lat: float, lon: float, zoom_level: int) -> MapTile:
    """
    Convert a location to a map tile for a given zoom level.

    See: https://developer.tomtom.com/map-display-api/documentation/zoom-levels-and-tile-grid

    Args:
        lat (float): The latitude of the location.
        lon (float): The longitude of the location.
        zoom_level (int): The zoom level.

    Returns:
        MapTile: The corresponding map tile.

    Raises:
        ValueError: If latitude, longitude, or zoom level are out of range.
    """
    if not MIN_ZOOM_LEVEL <= zoom_level <= MAX_ZOOM_LEVEL:
        raise ValueError(f"Zoom level value is out of range [{MIN_ZOOM_LEVEL}, {MAX_ZOOM_LEVEL}]")

    if not MIN_LAT <= lat <= MAX_LAT:
        raise ValueError(f"Latitude value is out of range [{MIN_LAT}, {MAX_LAT}]")

    if not MIN_LON <= lon <= MAX_LON:
        raise ValueError(f"Longitude value is out of range [{MIN_LON}, {MAX_LON}]")

    z = zoom_level
    xy_tiles_count = 2**z
    x = int(((lon + 180.0) / 360.0) * xy_tiles_count)
    y = int(((1.0 - math.log(math.tan(math.radians(lat)) + 1.0 / math.cos(math.radians(lat))) / math.pi) / 2.0) * xy_tiles_count)

    return MapTile(x=x, y=y, zoom=z)


def tile_zxy_to_lat_lon(zoom_level: int, x: int, y: int) -> LatLon:
    """
    Convert a map tile to a location for a given zoom level.

    See: https://developer.tomtom.com/map-display-api/documentation/zoom-levels-and-tile-grid

    Args:
        zoom_level (int): The zoom level.
        x (int): The x coordinate of the map tile.
        y (int): The y coordinate of the map tile.

    Returns:
        LatLon: The corresponding latitude and longitude.

    Raises:
        ValueError: If the zoom level or tile coordinates are out of range.
    """
    if not MIN_ZOOM_LEVEL <= zoom_level <= MAX_ZOOM_LEVEL:
        raise ValueError(f"Zoom level value is out of range [{MIN_ZOOM_LEVEL}, {MAX_ZOOM_LEVEL}]")

    z = zoom_level
    max_xy = 2**z - 1

    if not 0 <= x <= max_xy:
        raise ValueError(f"Tile x value is out of range [0, {max_xy}]")

    if not 0 <= y <= max_xy:
        raise ValueError(f"Tile y value is out of range [0, {max_xy}]")

    lon = (x / 2**z) * 360.0 - 180.0

    n = math.pi - (2.0 * math.pi * y) / 2**z
    lat = (180.0 / math.pi) * math.atan(0.5 * (math.exp(n) - math.exp(-n)))

    return LatLon(lat=lat, lon=lon)
