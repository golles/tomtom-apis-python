"""Models for the TomTom Traffic API"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ..api import BaseParams
from ..models import Language, TileSizeType


@dataclass(kw_only=True)
class BBoxParam:
    """bbox param"""

    # pylint: disable=invalid-name
    minLon: float
    minLat: float
    maxLon: float
    maxLat: float

    def to_comma_seperate(self) -> str:
        """Turn the object into a comma seperated string"""
        return f"{self.minLon},{self.minLat},{self.maxLon},{self.maxLat}"


@dataclass(kw_only=True)
class BoudingBoxParam:
    """Boudingbox param"""

    # pylint: disable=invalid-name
    minY: float
    minX: float
    maxY: float
    maxX: float

    def to_comma_seperate(self) -> str:
        """Turn the object into a comma seperated string"""
        return f"{self.minY},{self.minX},{self.maxY},{self.maxX}"


@dataclass(kw_only=True)
class FlowSegmentDataParams(BaseParams):
    """Parameters for the get_flow_segment_data method"""

    # pylint: disable=invalid-name
    unit: SpeedUnitType | None = None
    thickness: ThicknessType | None = None
    openLr: bool | None = None


class FlowStyleType(Enum):
    """Supported flow style types"""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    RELATIVE0 = "relative0"
    RELATIVE0_DARK = "relative0-dark"
    RELATIVE_DELAY = "relative-delay"
    REDUCED_SENSITIVITY = "reduced-sensitivity"


class FlowTagType(Enum):
    """Supported flow tag types"""

    ROAD_TYPE = "road_type"
    TRAFFIC_LEVEL = "traffic_level"
    TRAFFIC_ROAD_COVERAGE = "traffic_road_coverage"
    LEFT_HAND_TRAFFIC = "left_hand_traffic"
    ROAD_CLOSURE = "road_closure"
    ROAD_CATEGORY = "road_category"
    ROAD_SUBCATEGORY = "road_subcategory"


class FlowType(Enum):
    """Supported flow types"""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    RELATIVE_DELAY = "relative-delay"


class IncidentStyleType(Enum):
    """Supported incident style types"""

    S0 = "s0"
    S0_DARK = "s0-dark"
    S1 = "s1"
    S2 = "s2"
    S3 = "s3"
    NIGHT = "night"


class IncidentTagType(Enum):
    """Supported incident tag types"""

    ICON_CATEGORY = "icon_category"
    DESCRIPTION = "description"
    DELAY = "delay"
    ROAD_TYPE = "road_type"
    LEFT_HAND_TRAFFIC = "left_hand_traffic"
    MAGNITUDE = "magnitude"
    TRAFFIC_ROAD_COVERAGE = "traffic_road_coverage"
    CLUSTERED = "clustered"
    PROBABILITY_OF_OCCURRENCE = "probability_of_occurrence"
    NUMBER_OF_REPORTS = "number_of_reports"
    LAST_REPORT_TIME = "last_report_time"
    END_DATE = "end_date"
    ID = "id"
    ROAD_CATEGORY = "road_category"
    ROAD_SUBCATEGORY = "road_subcategory"


@dataclass(kw_only=True)
class RasterFlowTilesParams(BaseParams):
    """Parameters for the get_raster_flow_tiles method"""

    # pylint: disable=invalid-name
    thickness: ThicknessType | None = None
    tileSize: TileSizeType | None = None


@dataclass(kw_only=True)
class RasterIncidentTilesParams(BaseParams):
    """Parameters for the get_raster_incident_tile method"""

    # pylint: disable=invalid-name
    t: str | None = None
    tileSize: TileSizeType | None = None


class RoadType(Enum):
    """Supported road types"""

    MOTORWAY = 0
    INTERNATIONAL_ROAD = 1
    MAJOR_ROAD = 2
    SECONDARY_ROAD = 3
    CONNECTING_ROAD = 4
    MAJOR_LOCAL_ROAD = 5
    LOCAL_ROAD = 6
    MINOR_LOCAL_ROAD = 7
    OTHER_ROADS = 8  # Non public road, Parking road, etc.


class SpeedUnitType(Enum):
    """Supported speed unit types"""

    KMPH = "kmph"
    MPH = "mph"


class ThicknessType(Enum):
    """Supported thickness types"""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    RELATIVE_DELAY = "relative-delay"
    REDUCED_SENSITIVITY = "reduced-sensitivity"


@dataclass(kw_only=True)
class VectorFlowTilesParams(BaseParams):
    """Parameters for the get_vector_flow_tiles method"""

    # pylint: disable=invalid-name
    roadTypes: RoadType | None = None
    trafficLevelStep: float | None = None
    margin: float | None = None
    tags: list[FlowTagType] | None = None


@dataclass(kw_only=True)
class VectorIncidentTilesParams(BaseParams):
    """
    Parameters for the get_vector_incident_tile method.
    """

    t: str | None = None
    tags: list[str] | None = None
    language: Language | None = None
