"""Models for the TomTom Maps API."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from mashumaro.mixins.orjson import DataClassORJSONMixin

from tomtom_api.models import Language, ViewType

from ..api import BaseParams


@dataclass(kw_only=True)
class MapTileParams(BaseParams):
    """Parameters for the map tile API."""

    # pylint: disable=invalid-name
    tileSize: Literal[256, 512] | None = None
    view: ViewType | None = None
    language: Language | None = None


@dataclass(kw_only=True)
class StaticImageParams(BaseParams):
    """Parameters for the map tile API."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    layer: Literal["basic", "hybrid", "labels"] | None = None
    style: Literal["main", "night"] | None = None
    x: int | None = None
    y: int | None = None
    zoom: int | None = None
    center: list[float] | None = None
    format: Literal["png", "jpg"] | None = None
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
    adrCategory: Literal["B", "C", "D", "E"] | None = None
    commercialVehicle: bool | None = None
    travelMode: Literal["Car", "Truck", "Taxi", "Bus", "Van", "Motorcycle", "Bicycle", "Pedestrian", "Other"] | None = None
    emissionClass: str | None = None
    engineType: str | None = None
    travelModeProfile: str | None = None


@dataclass(kw_only=True)
class MapServiceCopyrightsResponse(DataClassORJSONMixin):
    """Represents the map service copyrights response."""

    # pylint: disable=invalid-name
    formatVersion: str
    copyrightsCaption: str
