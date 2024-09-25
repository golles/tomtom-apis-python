"""Test utils."""

import math
from enum import Enum, IntEnum, StrEnum

import pytest

from tomtom_apis.models import LatLon, MapTile
from tomtom_apis.utils import lat_lon_to_tile_zxy, serialize_bool, serialize_enum, serialize_list, serialize_list_brackets, tile_zxy_to_lat_lon


def test_lat_lon_to_tile_zxy_valid() -> None:
    """Test valid lat_lon_to_tile_zxy input."""
    result = lat_lon_to_tile_zxy(37.7749, -122.4194, 10)
    assert isinstance(result, MapTile)
    assert result.zoom == 10
    assert result.x == 163
    assert result.y == 395


def test_lat_lon_to_tile_zxy_boundary() -> None:
    """Test boundary conditions for lat_lon_to_tile_zxy."""
    result = lat_lon_to_tile_zxy(85.051128779806, 180.0, 10)
    assert isinstance(result, MapTile)
    assert result.zoom == 10
    assert result.x == 1024
    assert result.y == 0


def test_lat_lon_to_tile_zxy_invalid_zoom_level() -> None:
    """Test invalid zoom level for lat_lon_to_tile_zxy."""
    with pytest.raises(ValueError, match="Zoom level value is out of range"):
        lat_lon_to_tile_zxy(37.7749, -122.4194, 23)


def test_lat_lon_to_tile_zxy_invalid_latitude() -> None:
    """Test invalid latitude for lat_lon_to_tile_zxy."""
    with pytest.raises(ValueError, match="Latitude value is out of range"):
        lat_lon_to_tile_zxy(90.0, -122.4194, 10)


def test_lat_lon_to_tile_zxy_invalid_longitude() -> None:
    """Test invalid longitude for lat_lon_to_tile_zxy."""
    with pytest.raises(ValueError, match="Longitude value is out of range"):
        lat_lon_to_tile_zxy(37.7749, -200.0, 10)


def test_tile_zxy_to_lat_lon_valid() -> None:
    """Test valid tile_zxy_to_lat_lon input."""
    result = tile_zxy_to_lat_lon(10, 163, 395)
    assert isinstance(result, LatLon)
    assert math.isclose(result.lat, 37.7749, rel_tol=1e-2)
    assert math.isclose(result.lon, -122.4194, rel_tol=1e-2)


def test_tile_zxy_to_lat_lon_invalid_zoom_level() -> None:
    """Test invalid zoom level for tile_zxy_to_lat_lon."""
    with pytest.raises(ValueError, match="Zoom level value is out of range"):
        tile_zxy_to_lat_lon(23, 163, 395)


def test_tile_zxy_to_lat_lon_invalid_x() -> None:
    """Test invalid x coordinate for tile_zxy_to_lat_lon."""
    with pytest.raises(ValueError, match="Tile x value is out of range"):
        tile_zxy_to_lat_lon(10, -1, 395)


def test_tile_zxy_to_lat_lon_invalid_y() -> None:
    """Test invalid y coordinate for tile_zxy_to_lat_lon."""
    with pytest.raises(ValueError, match="Tile y value is out of range"):
        tile_zxy_to_lat_lon(10, 163, -1)


def test_serialize_bool() -> None:
    """Test cases for test_serialize_bool."""
    # Test with True
    assert serialize_bool(True) == "true"
    # Test with False
    assert serialize_bool(False) == "false"


class Color(Enum):
    """Simple enum for testing."""

    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class StrColor(StrEnum):
    """Simple string enum for testing."""

    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class IntColor(IntEnum):
    """Simple int enum for testing."""

    RED = 1
    GREEN = 2
    BLUE = 3


def test_serialize_enum() -> None:
    """Test cases for serialize_enum."""
    assert serialize_enum(Color.RED) == "red"
    assert serialize_enum(StrColor.RED) == "red"
    assert serialize_enum(IntColor.RED) == "1"


def test_serialize_list() -> None:
    """Test cases for test_serialize_list."""
    # Test with an empty list
    assert serialize_list([]) is None
    # Test with a list of integers
    assert serialize_list([1, 2, 3]) == "1,2,3"
    # Test with a list of strings
    assert serialize_list(["a", "b", "c"]) == "a,b,c"
    # Test with a mixed list
    assert serialize_list([1, "b", 3.0, True]) == "1,b,3.0,true"
    assert serialize_list([False, "yes", 10]) == "false,yes,10"
    assert serialize_list(["True", False]) == "True,false"
    # Test with a list containing Enums
    assert serialize_list([Color.RED, Color.GREEN, Color.BLUE]) == "red,green,blue"
    assert serialize_list([StrColor.RED, StrColor.GREEN, StrColor.BLUE]) == "red,green,blue"
    assert serialize_list([IntColor.RED, IntColor.GREEN, IntColor.BLUE]) == "1,2,3"
    assert serialize_list([Color.RED, StrColor.GREEN, IntColor.BLUE]) == "red,green,3"
    assert serialize_list([StrColor.RED, 1, True]) == "red,1,true"


def test_serialize_list_brackets() -> None:
    """Test cases for test_serialize_list_brackets."""
    # Test with an empty list
    assert serialize_list_brackets([]) is None
    # Test with a list of integers
    assert serialize_list_brackets([1, 2, 3]) == "[1,2,3]"
    # Test with a list of strings
    assert serialize_list_brackets(["a", "b", "c"]) == "[a,b,c]"
    # Test with a mixed list
    assert serialize_list_brackets([1, "b", 3.0, True]) == "[1,b,3.0,true]"
    assert serialize_list_brackets([False, "yes", 10]) == "[false,yes,10]"
    assert serialize_list_brackets(["True", False]) == "[True,false]"
    # Test with a list containing Enums
    assert serialize_list_brackets([Color.RED, Color.GREEN, Color.BLUE]) == "[red,green,blue]"
    assert serialize_list_brackets([StrColor.RED, StrColor.GREEN, StrColor.BLUE]) == "[red,green,blue]"
    assert serialize_list_brackets([IntColor.RED, IntColor.GREEN, IntColor.BLUE]) == "[1,2,3]"
    assert serialize_list_brackets([Color.RED, StrColor.GREEN, IntColor.BLUE]) == "[red,green,3]"
    assert serialize_list_brackets([StrColor.RED, 1, True]) == "[red,1,true]"
