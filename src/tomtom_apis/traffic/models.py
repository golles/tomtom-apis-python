"""Models for the TomTom Traffic API."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-many-lines

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum, StrEnum
from typing import Self

from geojson import LineString, Point
from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin

from ..api import BaseParams, BasePostData
from ..models import Language, LatitudeLongitude, TileSizeType


@dataclass(kw_only=True)
class Aci:
    """Represents an ACI item."""

    probabilityOfOccurrence: ProbabilityOfOccurrenceType
    numberOfReports: int
    lastReportTime: str


@dataclass(kw_only=True)
class BBoxParam:
    """bbox param."""

    minLon: float
    minLat: float
    maxLon: float
    maxLat: float

    def to_comma_separated(self: Self) -> str:
        """Convert the object into a comma-separated string."""
        return ",".join(map(str, [self.minLon, self.minLat, self.maxLon, self.maxLat]))


@dataclass(kw_only=True)
class BoudingBoxParam:
    """Boudingbox param."""

    minY: float
    minX: float
    maxY: float
    maxX: float

    def to_comma_separated(self: Self) -> str:
        """Convert the object into a comma-separated string."""
        return ",".join(map(str, [self.minY, self.minX, self.maxY, self.maxX]))


class CategoryFilterType(StrEnum):
    """Supported category filter types."""

    UNKNOWN = "Unknown"
    ACCIDENT = "Accident"
    FOG = "Fog"
    DANGEROUS_CONDITIONS = "DangerousConditions"
    RAIN = "Rain"
    ICE = "Ice"
    JAM = "Jam"
    LANE_CLOSED = "LaneClosed"
    ROAD_CLOSED = "RoadClosed"
    ROAD_WORKS = "RoadWorks"
    WIND = "Wind"
    FLOODING = "Flooding"
    BROKEN_DOWN_VEHICLE = "BrokenDownVehicle"


@dataclass(kw_only=True)
class Coordinates:
    """Represents a coordinate item."""

    coordinate: list[LatitudeLongitude]


class DirectionType(StrEnum):
    """Supported direction types."""

    POSITIVE = "positive"
    NEGATIVE = "negative"


@dataclass(kw_only=True)
class Event:
    """Represents an event item."""

    description: str
    code: int
    iconCategory: IconCategoryType


@dataclass(kw_only=True)
class FlowSegmentData:
    """Represents a flow segment data item."""

    version: str = field(metadata=field_options(alias="@version"))
    frc: FrcType
    currentSpeed: int
    freeFlowSpeed: int
    currentTravelTime: int
    freeFlowTravelTime: float
    confidence: float
    coordinates: Coordinates
    openlr: str | None = None
    roadClosure: bool


@dataclass(kw_only=True)
class FlowSegmentDataParams(BaseParams):
    """Parameters for the get_flow_segment_data method."""

    unit: SpeedUnitType | None = None
    thickness: ThicknessType | None = None
    openLr: bool | None = None


@dataclass(kw_only=True)
class FlowSegmentDataResponse(DataClassORJSONMixin):
    """Represents a flow segment data response."""

    flowSegmentData: FlowSegmentData


class FlowStyleType(StrEnum):
    """Supported flow style types."""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    RELATIVE0 = "relative0"
    RELATIVE0_DARK = "relative0-dark"
    RELATIVE_DELAY = "relative-delay"
    REDUCED_SENSITIVITY = "reduced-sensitivity"


class FlowTagType(StrEnum):
    """Supported flow tag types."""

    ROAD_TYPE = "road_type"
    TRAFFIC_LEVEL = "traffic_level"
    TRAFFIC_ROAD_COVERAGE = "traffic_road_coverage"
    LEFT_HAND_TRAFFIC = "left_hand_traffic"
    ROAD_CLOSURE = "road_closure"
    ROAD_CATEGORY = "road_category"
    ROAD_SUBCATEGORY = "road_subcategory"


class FlowType(StrEnum):
    """Supported flow types."""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    RELATIVE_DELAY = "relative-delay"


class FrcType(StrEnum):
    """Supported Functional Road Class types. This indicates the road type."""

    FRC0 = "FRC0"  # Motorway, freeway or other major road
    FRC1 = "FRC1"  # Major road, less important than a motorway
    FRC2 = "FRC2"  # Other major road
    FRC3 = "FRC3"  # Secondary road
    FRC4 = "FRC4"  # Local connecting road
    FRC5 = "FRC5"  # Local road of high importance
    FRC6 = "FRC6"  # Local road


class IconCategoryType(IntEnum):
    """Supported icon category types."""

    UNKNOWN = 0
    ACCIDENT = 1
    FOG = 2
    DANGEROUS_CONDITIONS = 3
    RAIN = 4
    ICE = 5
    JAM = 6
    LANE_CLOSED = 7
    ROAD_CLOSED = 8
    ROAD_WORKS = 9
    WIND = 10
    FLOODING = 11
    BROKEN_DOWN_VEHICLE = 14


@dataclass(kw_only=True)
class Incident:
    """Represents an incident item."""

    type: str
    properties: IncidentProperties
    geometry: Point | LineString


@dataclass(kw_only=True)
class IncidentDetailsParams(BaseParams):
    """Parameters for the get_incident_details method."""

    fields: str | None = None
    language: Language | None = None
    t: str | None = None
    categoryFilter: list[CategoryFilterType] | None = None
    timeValidityFilter: list[TimeValidityFilterType] | None = None


@dataclass(kw_only=True)
class IncidentDetailsPostData(BasePostData):
    """Data for the post incident details API."""

    ids: list[str]


@dataclass(kw_only=True)
class IncidentDetailsResponse(DataClassORJSONMixin):
    """Represents an incident details response."""

    incidents: list[Incident | None]


@dataclass(kw_only=True)
class IncidentProperties:
    """Represents an incidents properties item."""

    id: str | None = None
    iconCategory: IconCategoryType
    magnitudeOfDelay: MagnitudeOfDelayType | None = None
    events: list[Event] | None = None
    startTime: str | None = None
    endTime: str | None = None
    from_: str | None = field(metadata=field_options(alias="from"), default=None)
    to: str | None = None
    length: float | None = None
    delay: int | None = None
    roadNumbers: list[str] | None = None
    timeValidity: str | None = None
    tmc: TMC | None = None
    probabilityOfOccurrence: ProbabilityOfOccurrenceType | None = None
    numberOfReports: int | None = None
    lastReportTime: str | None = None
    aci: Aci | None = None


class IncidentStyleType(StrEnum):
    """Supported incident style types."""

    S0 = "s0"
    S0_DARK = "s0-dark"
    S1 = "s1"
    S2 = "s2"
    S3 = "s3"
    NIGHT = "night"


class IncidentTagType(StrEnum):
    """Supported incident tag types."""

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


class IncidentTileFormatType(StrEnum):
    """Supported incident tile formats."""

    GIF = "gif"
    PNG = "png"


@dataclass(kw_only=True)
class IncidentViewportResponse(DataClassORJSONMixin):
    """Represents an incident viewport response."""

    viewpResp: ViewpResp


class MagnitudeOfDelayType(IntEnum):
    """Supported magnitude of delay types."""

    UNKNOWN = 0
    MINOR = 1
    MODERATE = 2
    MAJOR = 3
    UNDEFINED = 4


class ProbabilityOfOccurrenceType(StrEnum):
    """Supported probability of occurrence types."""

    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "risk_of"
    IMPROBABLE = "improbable"


@dataclass(kw_only=True)
class RasterFlowTilesParams(BaseParams):
    """Parameters for the get_raster_flow_tiles method."""

    thickness: ThicknessType | None = None
    tileSize: TileSizeType | None = None


@dataclass(kw_only=True)
class RasterIncidentTilesParams(BaseParams):
    """Parameters for the get_raster_incident_tile method."""

    t: str | None = None
    tileSize: TileSizeType | None = None


class RoadType(IntEnum):
    """Supported road types."""

    MOTORWAY = 0
    INTERNATIONAL_ROAD = 1
    MAJOR_ROAD = 2
    SECONDARY_ROAD = 3
    CONNECTING_ROAD = 4
    MAJOR_LOCAL_ROAD = 5
    LOCAL_ROAD = 6
    MINOR_LOCAL_ROAD = 7
    OTHER_ROADS = 8  # Non public road, Parking road, etc.


class SpeedUnitType(StrEnum):
    """Supported speed unit types."""

    KMPH = "kmph"
    MPH = "mph"


@dataclass(kw_only=True)
class TMC:
    """Represents a Traffic Message Channel item."""

    countryCode: str | None = None
    tableNumber: str | None = None
    tableVersion: str | None = None
    direction: DirectionType | None = None
    points: list[TmcPoint] | None = None


class ThicknessType(StrEnum):
    """Supported thickness types."""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    RELATIVE_DELAY = "relative-delay"
    REDUCED_SENSITIVITY = "reduced-sensitivity"


class TimeValidityFilterType(StrEnum):
    """Supported time validity filter types."""

    PRESENT = "present"
    FUTURE = "future"


@dataclass(kw_only=True)
class TmcPoint:
    """Represents a TmcPoint item."""

    location: int | None = None
    offset: int


@dataclass(kw_only=True)
class TrafficState:
    """Represents a traffic state item."""

    trafficAge: str = field(metadata=field_options(alias="@trafficAge"))
    trafficModelId: str = field(metadata=field_options(alias="@trafficModelId"))


@dataclass(kw_only=True)
class VectorFlowTilesParams(BaseParams):
    """Parameters for the get_vector_flow_tiles method."""

    roadTypes: RoadType | None = None
    trafficLevelStep: float | None = None
    margin: float | None = None
    tags: list[FlowTagType] | None = None


@dataclass(kw_only=True)
class VectorIncidentTilesParams(BaseParams):
    """Parameters for the get_vector_incident_tile method."""

    t: str | None = None
    tags: list[str] | None = None
    language: Language | None = None


@dataclass(kw_only=True)
class ViewpResp:
    """Represents a view resp item."""

    trafficState: TrafficState
    copyrightIds: str
    version: str = field(metadata=field_options(alias="@version"))
    maps: str = field(metadata=field_options(alias="@maps"))
