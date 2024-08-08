"""Models for the TomTom Maps API."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from mashumaro.mixins.orjson import DataClassORJSONMixin

from tomtom_api.models import Language, TileSizeType, ViewType

from ..api import BaseParams


class TravelModeType(Enum):
    """Supported travel mode types"""

    CAR = "Car"
    TRUCK = "Truck"
    TAXI = "Taxi"
    BUS = "Bus"
    VAN = "Van"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"
    PEDESTRIAN = "Pedestrian"
    OTHER = "Other"


class AdrCategoryType(Enum):
    """Supported ADR category types"""

    B = "B"
    C = "C"
    D = "D"
    E = "E"


class TileFormatType(Enum):
    """Supported tile formats"""

    PNG = "png"
    JPG = "jpg"


class LayerType(Enum):
    """Supported layer types"""

    BASIC = "basic"
    HYBRID = "hybrid"
    LABELS = "labels"


class LayerTypeWithPoiType(Enum):
    """Supported layer types"""

    BASIC = "basic"
    HYBRID = "hybrid"
    LABELS = "labels"
    POI = "poi"


class StyleType(Enum):
    """Supported style types"""

    MAIN = "main"
    NIGHT = "night"


@dataclass(kw_only=True)
class MapTileParams(BaseParams):
    """Parameters for the map tile API."""

    # pylint: disable=invalid-name
    tileSize: TileSizeType | None = None
    view: ViewType | None = None
    language: Language | None = None


@dataclass(kw_only=True)
class StaticImageParams(BaseParams):
    """Parameters for the map tile API."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    layer: LayerType | None = None
    style: StyleType | None = None
    x: int | None = None
    y: int | None = None
    zoom: int | None = None
    center: list[float] | None = None
    format: TileFormatType | None = None
    width: int | None = None  # must be a positive integer between 1 and 8192.
    height: int | None = None  # must be a positive integer between 1 and 8192.
    bbox: list[float] | None = None
    view: ViewType | None = None


@dataclass(kw_only=True)
class MapTileV1Params(BaseParams):
    """Parameters for the map tile API."""

    view: ViewType | None = None
    language: Language | None = None


# class BracketStringArray(list):
#     def __init__(self, *args):
#         super().__init__(args)

#     def __str__(self):
#         return f"[{','.join(map(str, self))}]"


@dataclass(kw_only=True)
class MapTileV2Params(BaseParams):
    """Parameters for the map tile API."""

    # TODO: include, generalLoadType, dangerousGoodsLoadType emissionClass and engineType should be a list as string surrounded by [] and separated by a ,

    # pylint: disable=invalid-name, too-many-instance-attributes
    view: ViewType | None = None
    include: str | None = None
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    numberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    generalLoadType: str | None = None
    dangerousGoodsLoadType: str | None = None
    adrCategory: AdrCategoryType | None = None
    commercialVehicle: bool | None = None
    travelMode: TravelModeType | None = None
    emissionClass: str | None = None
    engineType: str | None = None
    travelModeProfile: str | None = None


@dataclass(kw_only=True)
class MapServiceCopyrightsResponse(DataClassORJSONMixin):
    """Represents the map service copyrights response."""

    # pylint: disable=invalid-name
    formatVersion: str
    copyrightsCaption: str
