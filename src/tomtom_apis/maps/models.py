"""Models for the TomTom Maps API."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-many-lines

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

from mashumaro.mixins.orjson import DataClassORJSONMixin

from ..api import BaseParams
from ..models import AdrCategoryType, Language, TileSizeType, TravelModeType, ViewType
from ..utils import serialize_list_brackets


class DangerousGoodsLoadType(StrEnum):
    """Supported dangerous good types."""

    EXPLOSIVES = "Explosives"
    GASES = "Gases"
    FLAMMABLE_LIQUIDS = "Flammable_Liquids"
    FLAMMABLE_SOLIDS = "Flammable_Solids"
    OXIDIZING_AND_ORGANIC_SUBSTANCE = "Oxidizing_And_Organic_Substance"
    TOXIC_AND_INFECTIOUS_SUBSTANCE = "Toxic_And_Infectious_Substance"
    RADIOACTIVE_MATERIAL = "Radioactive_Material"
    CORROSIVES = "Corrosives"
    MISCELLANEOUS_DANGEROUS_GOODS = "Miscellaneous_Dangerous_Goods"


class EmissionClassType(StrEnum):
    """Supported emission class types."""

    EMISSIONCLASS0 = "EmissionClass0"
    EMISSIONCLASS1 = "EmissionClass1"
    EMISSIONCLASS2 = "EmissionClass2"
    EMISSIONCLASS3 = "EmissionClass3"
    EMISSIONCLASS4 = "EmissionClass4"
    EMISSIONCLASS5 = "EmissionClass5"
    EMISSIONCLASS6 = "EmissionClass6"
    EMISSIONCLASS7 = "EmissionClass7"
    EMISSIONCLASS8 = "EmissionClass8"
    EMISSIONCLASS9 = "EmissionClass9"
    EMISSIONCLASS10 = "EmissionClass10"


class EngineType(StrEnum):
    """Supported engine types."""

    LPG = "LPG"
    CNG = "CNG"
    LNG = "LNG"
    DIESEL = "Diesel"
    PETROL = "Petrol"
    HYDROGEN = "Hydrogen"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"
    PLUGIN_HYBRID = "Plugin_Hybrid"


class GeneralLoadType(StrEnum):
    """Supported general load types."""

    GENERAL_HAZARDOUS_MATERIALS = "General_Hazardous_Materials"
    EXPLOSIVE_MATERIALS = "Explosive_Materials"
    GOODS_HARMFUL_TO_WATER = "Goods_Harmful_To_Water"


class IncludeType(StrEnum):
    """Supported include types."""

    ROAD_RESTRICTIONS = "road_restrictions"


class LayerType(StrEnum):
    """Supported layer types."""

    BASIC = "basic"
    HYBRID = "hybrid"
    LABELS = "labels"


class LayerTypeWithPoiType(StrEnum):
    """Supported layer types."""

    BASIC = "basic"
    HYBRID = "hybrid"
    LABELS = "labels"
    POI = "poi"


@dataclass(kw_only=True)
class MapServiceCopyrightsResponse(DataClassORJSONMixin):
    """Represents the map service copyrights response."""

    formatVersion: str
    copyrightsCaption: str


@dataclass(kw_only=True)
class MapTileParams(BaseParams):
    """Parameters for the map tile API."""

    tileSize: TileSizeType | None = None
    view: ViewType | None = None
    language: Language | None = None


@dataclass(kw_only=True)
class MapTileV1Params(BaseParams):
    """Parameters for the map tile API."""

    view: ViewType | None = None
    language: Language | None = None


@dataclass(kw_only=True)
class MapTileV2Params(BaseParams):
    """Parameters for the map tile API."""

    view: ViewType | None = None
    include: list[IncludeType] | None = field(default=None, metadata={"serialize": serialize_list_brackets})
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    numberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    generalLoadType: list[GeneralLoadType] | None = field(default=None, metadata={"serialize": serialize_list_brackets})
    dangerousGoodsLoadType: list[DangerousGoodsLoadType] | None = field(default=None, metadata={"serialize": serialize_list_brackets})
    adrCategory: AdrCategoryType | None = None
    commercialVehicle: bool | None = None
    travelMode: TravelModeType | None = None
    emissionClass: list[EmissionClassType] | None = field(default=None, metadata={"serialize": serialize_list_brackets})
    engineType: list[EngineType] | None = field(default=None, metadata={"serialize": serialize_list_brackets})
    travelModeProfile: str | None = None


@dataclass(kw_only=True)
class StaticImageParams(BaseParams):
    """Parameters for the map tile API."""

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


class StyleType(StrEnum):
    """Supported style types."""

    MAIN = "main"
    NIGHT = "night"


class TileFormatType(StrEnum):
    """Supported tile formats."""

    PNG = "png"
    JPG = "jpg"
