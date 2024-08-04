"""Test utils."""

import math

import pytest

from tomtom_api.models import LatLon, MapTile
from tomtom_api.utils import lat_lon_to_tile_zxy, tile_zxy_to_lat_lon


def test_lat_lon_to_tile_zxy_valid():
    """Test valid lat_lon_to_tile_zxy input."""
    result = lat_lon_to_tile_zxy(37.7749, -122.4194, 10)
    assert isinstance(result, MapTile)
    assert result.zoom == 10
    assert result.x == 163
    assert result.y == 395


def test_lat_lon_to_tile_zxy_boundary():
    """Test boundary conditions for lat_lon_to_tile_zxy."""
    result = lat_lon_to_tile_zxy(85.051128779806, 180.0, 10)
    assert isinstance(result, MapTile)
    assert result.zoom == 10
    assert result.x == 1024
    assert result.y == 0


def test_lat_lon_to_tile_zxy_invalid_zoom_level():
    """Test invalid zoom level for lat_lon_to_tile_zxy."""
    with pytest.raises(ValueError, match="Zoom level value is out of range"):
        lat_lon_to_tile_zxy(37.7749, -122.4194, 23)


def test_lat_lon_to_tile_zxy_invalid_latitude():
    """Test invalid latitude for lat_lon_to_tile_zxy."""
    with pytest.raises(ValueError, match="Latitude value is out of range"):
        lat_lon_to_tile_zxy(90.0, -122.4194, 10)


def test_lat_lon_to_tile_zxy_invalid_longitude():
    """Test invalid longitude for lat_lon_to_tile_zxy."""
    with pytest.raises(ValueError, match="Longitude value is out of range"):
        lat_lon_to_tile_zxy(37.7749, -200.0, 10)


def test_tile_zxy_to_lat_lon_valid():
    """Test valid tile_zxy_to_lat_lon input."""
    result = tile_zxy_to_lat_lon(10, 163, 395)
    assert isinstance(result, LatLon)
    assert math.isclose(result.lat, 37.7749, rel_tol=1e-2)
    assert math.isclose(result.lon, -122.4194, rel_tol=1e-2)


def test_tile_zxy_to_lat_lon_invalid_zoom_level():
    """Test invalid zoom level for tile_zxy_to_lat_lon."""
    with pytest.raises(ValueError, match="Zoom level value is out of range"):
        tile_zxy_to_lat_lon(23, 163, 395)


def test_tile_zxy_to_lat_lon_invalid_x():
    """Test invalid x coordinate for tile_zxy_to_lat_lon."""
    with pytest.raises(ValueError, match="Tile x value is out of range"):
        tile_zxy_to_lat_lon(10, -1, 395)


def test_tile_zxy_to_lat_lon_invalid_y():
    """Test invalid y coordinate for tile_zxy_to_lat_lon."""
    with pytest.raises(ValueError, match="Tile y value is out of range"):
        tile_zxy_to_lat_lon(10, 163, -1)


def test_tile_zxy_to_lat_lon_boundary():
    """Test boundary conditions for tile_zxy_to_lat_lon."""
    max_tile_index = 2**10 - 1
    result = tile_zxy_to_lat_lon(10, max_tile_index, max_tile_index)
    assert isinstance(result, LatLon)
