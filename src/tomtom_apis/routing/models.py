"""Models for the TomTom Routing API."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-many-lines

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

from mashumaro.mixins.orjson import DataClassORJSONMixin

from ..api import BaseParams, BasePostData
from ..models import AdrCategoryType, Language, LatitudeLongitude, TravelModeType


class AvoidType(StrEnum):
    """Supported avoid types."""

    TOLL_ROADS = "tollRoads"
    MOTORWAYS = "motorways"
    FERRIES = "ferries"
    UNPAVED_ROADS = "unpavedRoads"
    CARPOOLS = "carpools"
    ALREADY_USED_ROADS = "alreadyUsedRoads"
    BORDER_CROSSINGS = "borderCrossings"
    TUNNELS = "tunnels"
    CAR_TRAINS = "carTrains"
    LOW_EMISSION_ZONES = "lowEmissionZones"


@dataclass(kw_only=True)
class CalculateLongDistanceEVRouteParams(BaseParams):
    """Parameters for the calculate long distance EV route API."""

    vehicleHeading: int | None = None
    sectionType: SectionType | None = None
    report: str | None = None
    departAt: str | None = None
    routeType: RouteType | None = None
    traffic: bool | None = None
    avoid: AvoidType | None = None
    travelMode: TravelModeType | None = None
    vehicleMaxSpeed: int | None = None
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    vehicleNumberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    vehicleCommercial: bool | None = None
    vehicleLoadType: VehicleLoadType | None = None
    vehicleAdrTunnelRestrictionCode: AdrCategoryType | None = None
    vehicleEngineType: VehicleEngineType
    accelerationEfficiency: float | None = None
    decelerationEfficiency: float | None = None
    uphillEfficiency: float | None = None
    downhillEfficiency: float | None = None
    consumptionInkWhPerkmAltitudeGain: float | None = None
    recuperationInkWhPerkmAltitudeLoss: float | None = None
    constantSpeedConsumptionInkWhPerHundredkm: str | None = None
    currentChargeInkWh: float | None = None
    maxChargeInkWh: float | None = None
    auxiliaryPowerInkW: float | None = None
    minChargeAtDestinationInkWh: float | None = None
    minChargeAtChargingStopsInkWh: float | None = None


@dataclass(kw_only=True)
class CalculateLongDistanceEVRoutePostData(BasePostData):
    """Data for the post calculate long distance EV route API."""

    chargingModes: list[ChargingMode]


@dataclass(kw_only=True)
class CalculateReachableRangePostData(BasePostData):
    """Data for the post calculate reachable range API."""

    avoidVignette: list[str] | None = None
    allowVignette: list[str] | None = None
    avoidAreas: Rectangles | None = None


@dataclass(kw_only=True)
class CalculateReachableRouteParams(BaseParams):
    """Parameters for the calculate reachable route API."""

    fuelBudgetInLiters: float | None = None
    energyBudgetInkWh: float | None = None
    timeBudgetInSec: float | None = None
    report: str | None = None
    departAt: str | None = None
    arriveAt: str | None = None
    routeType: RouteType | None = None
    traffic: bool | None = None
    avoid: AvoidType | None = None
    travelMode: TravelModeType | None = None
    hilliness: HillinessType | None = None
    windingness: WindingnessType | None = None
    vehicleMaxSpeed: int | None = None
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    vehicleNumberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    vehicleCommercial: bool | None = None
    vehicleLoadType: VehicleLoadType | None = None
    vehicleAdrTunnelRestrictionCode: AdrCategoryType | None = None
    constantSpeedConsumptionInLitersPerHundredkm: str | None = None
    currentFuelInLiters: float | None = None
    auxiliaryPowerInLitersPerHour: float | None = None
    fuelEnergyDensityInMJoulesPerLiter: float | None = None
    accelerationEfficiency: float | None = None
    decelerationEfficiency: float | None = None
    uphillEfficiency: float | None = None
    downhillEfficiency: float | None = None
    consumptionInkWhPerkmAltitudeGain: float | None = None
    recuperationInkWhPerkmAltitudeLoss: float | None = None
    currentChargeInkWh: float | None = None
    maxChargeInkWh: float | None = None
    auxiliaryPowerInkW: float | None = None
    vehicleEngineType: VehicleEngineType | None = None
    constantSpeedConsumptionInkWhPerHundredkm: str | None = None


@dataclass(kw_only=True)
class CalculateRouteParams(BaseParams):
    """Parameters for the calculate route API."""

    maxAlternatives: int | None = None
    instructionsType: InstructionsType | None = None
    language: Language | None = None
    computeBestOrder: bool | None = None
    routeRepresentation: str | None = None
    computeTravelTimeFor: str | None = None
    vehicleHeading: int | None = None
    sectionType: SectionType | None = None
    report: str | None = None
    departAt: str | None = None
    arriveAt: str | None = None
    routeType: RouteType | None = None
    traffic: bool | None = None
    avoid: AvoidType | None = None
    travelMode: TravelModeType | None = None
    hilliness: HillinessType | None = None
    windingness: WindingnessType | None = None
    vehicleMaxSpeed: int | None = None  # 0-250
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    vehicleNumberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    vehicleCommercial: bool | None = None
    vehicleLoadType: VehicleLoadType | None = None
    vehicleAdrTunnelRestrictionCode: AdrCategoryType | None = None
    vehicleEngineType: VehicleEngineType | None = None
    constantSpeedConsumptionInLitersPerHundredkm: str | None = None
    currentFuelInLiters: float | None = None
    auxiliaryPowerInLitersPerHour: float | None = None
    fuelEnergyDensityInMJoulesPerLiter: float | None = None
    accelerationEfficiency: float | None = None
    decelerationEfficiency: float | None = None
    uphillEfficiency: float | None = None
    downhillEfficiency: float | None = None
    consumptionInkWhPerkmAltitudeGain: float | None = None
    recuperationInkWhPerkmAltitudeLoss: float | None = None
    constantSpeedConsumptionInkWhPerHundredkm: str | None = None
    currentChargeInkWh: float | None = None
    maxChargeInkWh: float | None = None
    auxiliaryPowerInkW: float | None = None


@dataclass(kw_only=True)
class CalculateRoutePostData(BasePostData):
    """Data for the post calculate route API."""

    supportingPoints: list[LatitudeLongitude] | None = None
    avoidVignette: list[str] | None = None
    allowVignette: list[str] | None = None
    avoidAreas: Rectangles | None = None


@dataclass(kw_only=True)
class CalculatedLongDistanceEVRouteResponse(DataClassORJSONMixin):
    """Represents a calculated long distance EV route response."""

    formatVersion: str
    routes: list[EVRoute]


@dataclass(kw_only=True)
class CalculatedReachableRangeResponse(DataClassORJSONMixin):
    """Represents a calculated reachable range response."""

    formatVersion: str
    reachableRange: ReachableRange


@dataclass(kw_only=True)
class CalculatedRouteResponse(DataClassORJSONMixin):
    """Represents a calculated route response."""

    formatVersion: str
    routes: list[Route]


@dataclass(kw_only=True)
class ChargingConnection(DataClassORJSONMixin):
    """Represents a charging connection."""

    facilityType: FacilityType
    plugType: PlugType


@dataclass(kw_only=True)
class ChargingConnectionInfo(DataClassORJSONMixin):
    """Represents the charging connection info."""

    chargingVoltageInV: int
    chargingCurrentInA: int
    chargingCurrentType: ChargingCurrentType
    chargingPowerInkW: int
    chargingPlugType: PlugType


class ChargingCurrentType(StrEnum):
    """Supported charging current types."""

    DIRECT_CURRENT = "Direct_Current"
    ALTERNATING_CURRENT_1_PHASE = "Alternating_Current_1_Phase"
    ALTERNATING_CURRENT_3_PHASE = "Alternating_Current_3_Phase"


@dataclass(kw_only=True)
class ChargingCurve(DataClassORJSONMixin):
    """Represents a charging curve."""

    chargeInkWh: float
    timeToChargeInSeconds: int


@dataclass(kw_only=True)
class ChargingInformationAtEndOfLeg(DataClassORJSONMixin):
    """Represents the charging information at the end of a leg."""

    chargingConnections: list[ChargingConnection]
    chargingConnectionInfo: ChargingConnectionInfo
    targetChargeInkWh: float
    chargingTimeInSeconds: int
    chargingParkUuid: str
    chargingParkExternalId: str
    chargingParkName: str
    chargingParkOperatorName: str
    chargingParkLocation: ChargingParkLocation
    chargingParkPaymentOptions: list[ChargingParkPaymentOption]
    chargingParkPowerInkW: int
    chargingStopType: ChargingStopType


@dataclass(kw_only=True)
class ChargingMode(DataClassORJSONMixin):
    """Represents a charging mode."""

    chargingConnections: list[ChargingConnection]
    chargingCurve: list[ChargingCurve]


@dataclass(kw_only=True)
class ChargingParkLocation(DataClassORJSONMixin):
    """Represents a charging park location."""

    coordinate: LatitudeLongitude
    street: str
    city: str
    postalCode: str
    countryCode: str


@dataclass(kw_only=True)
class ChargingParkPaymentOption(DataClassORJSONMixin):
    """Represents a charging park payment option."""

    method: str
    brands: list[str]


class ChargingStopType(StrEnum):
    """Supported charging stop types."""

    AUTO_GENERATED = "Auto_Generated"
    USER_DEFINED = "User_Defined"


@dataclass(kw_only=True)
class EVLeg(DataClassORJSONMixin):
    """Represents a leg of a EV route."""

    summary: EVLegSummary | Summary
    points: list[LatitudeLongitude]


@dataclass(kw_only=True)
class EVLegSummary(DataClassORJSONMixin):
    """Represents the summary of a EV leg."""

    lengthInMeters: int
    travelTimeInSeconds: int
    trafficDelayInSeconds: int
    trafficLengthInMeters: int
    departureTime: datetime
    arrivalTime: datetime
    batteryConsumptionInkWh: float
    remainingChargeAtArrivalInkWh: float
    chargingInformationAtEndOfLeg: ChargingInformationAtEndOfLeg


@dataclass(kw_only=True)
class EVRoute(DataClassORJSONMixin):
    """Represents a EV route."""

    summary: EVSummary
    legs: list[EVLeg]
    sections: list[Section]


@dataclass(kw_only=True)
class EVSummary(DataClassORJSONMixin):
    """Represents the EV summary of a route."""

    lengthInMeters: int
    travelTimeInSeconds: int
    trafficDelayInSeconds: int
    trafficLengthInMeters: int
    departureTime: datetime
    arrivalTime: datetime
    batteryConsumptionInkWh: float
    remainingChargeAtArrivalInkWh: float
    totalChargingTimeInSeconds: float


class FacilityType(StrEnum):
    """Supported facility types."""

    BATTERY_EXCHANGE = "Battery_Exchange"
    CHARGE_100_TO_120V_1_PHASE_AT_8A = "Charge_100_to_120V_1_Phase_at_8A"
    CHARGE_100_TO_120V_1_PHASE_AT_10A = "Charge_100_to_120V_1_Phase_at_10A"
    CHARGE_100_TO_120V_1_PHASE_AT_12A = "Charge_100_to_120V_1_Phase_at_12A"
    CHARGE_100_TO_120V_1_PHASE_AT_13A = "Charge_100_to_120V_1_Phase_at_13A"
    CHARGE_100_TO_120V_1_PHASE_AT_16A = "Charge_100_to_120V_1_Phase_at_16A"
    CHARGE_100_TO_120V_1_PHASE_AT_32A = "Charge_100_to_120V_1_Phase_at_32A"
    CHARGE_200_TO_240V_1_PHASE_AT_8A = "Charge_200_to_240V_1_Phase_at_8A"
    CHARGE_200_TO_240V_1_PHASE_AT_10A = "Charge_200_to_240V_1_Phase_at_10A"
    CHARGE_200_TO_240V_1_PHASE_AT_12A = "Charge_200_to_240V_1_Phase_at_12A"
    CHARGE_200_TO_240V_1_PHASE_AT_16A = "Charge_200_to_240V_1_Phase_at_16A"
    CHARGE_200_TO_240V_1_PHASE_AT_20A = "Charge_200_to_240V_1_Phase_at_20A"
    CHARGE_200_TO_240V_1_PHASE_AT_32A = "Charge_200_to_240V_1_Phase_at_32A"
    CHARGE_200_TO_240V_1_PHASE_ABOVE_32A = "Charge_200_to_240V_1_Phase_above_32A"
    CHARGE_200_TO_240V_3_PHASE_AT_16A = "Charge_200_to_240V_3_Phase_at_16A"
    CHARGE_200_TO_240V_3_PHASE_AT_32A = "Charge_200_to_240V_3_Phase_at_32A"
    CHARGE_380_TO_480V_3_PHASE_AT_16A = "Charge_380_to_480V_3_Phase_at_16A"
    CHARGE_380_TO_480V_3_PHASE_AT_32A = "Charge_380_to_480V_3_Phase_at_32A"
    CHARGE_380_TO_480V_3_PHASE_AT_63A = "Charge_380_to_480V_3_Phase_at_63A"
    CHARGE_50_TO_500V_DIRECT_CURRENT_AT_62A_25KW = "Charge_50_to_500V_Direct_Current_at_62A_25kW"
    CHARGE_50_TO_500V_DIRECT_CURRENT_AT_125A_50KW = "Charge_50_to_500V_Direct_Current_at_125A_50kW"
    CHARGE_200_TO_450V_DIRECT_CURRENT_AT_200A_90KW = "Charge_200_to_450V_Direct_Current_at_200A_90kW"
    CHARGE_200_TO_480V_DIRECT_CURRENT_AT_255A_120KW = "Charge_200_to_480V_Direct_Current_at_255A_120kW"
    CHARGE_DIRECT_CURRENT_AT_20KW = "Charge_Direct_Current_at_20kW"
    CHARGE_DIRECT_CURRENT_AT_50KW = "Charge_Direct_Current_at_50kW"
    CHARGE_DIRECT_CURRENT_ABOVE_50KW = "Charge_Direct_Current_above_50kW"


class HillinessType(StrEnum):
    """Supported hilliness types."""

    LOW = "low"
    HIGH = "high"


class InstructionsType(StrEnum):
    """Supported instructions types."""

    CODED = "coded"
    TEXT = "text"
    TAGGED = "tagged"


@dataclass(kw_only=True)
class Leg(DataClassORJSONMixin):
    """Represents a leg of a route."""

    summary: Summary
    points: list[LatitudeLongitude]


class PlugType(StrEnum):
    """Supported plug types."""

    SMALL_PADDLE_INDUCTIVE = "Small_Paddle_Inductive"
    LARGE_PADDLE_INDUCTIVE = "Large_Paddle_Inductive"
    IEC_60309_1_PHASE = "IEC_60309_1_Phase"
    IEC_60309_3_PHASE = "IEC_60309_3_Phase"
    IEC_62196_TYPE_1_OUTLET = "IEC_62196_Type_1_Outlet"
    IEC_62196_TYPE_2_OUTLET = "IEC_62196_Type_2_Outlet"
    IEC_62196_TYPE_3_OUTLET = "IEC_62196_Type_3_Outlet"
    IEC_62196_TYPE_1_CONNECTOR_CABLE_ATTACHED = "IEC_62196_Type_1_Connector_Cable_Attached"
    IEC_62196_TYPE_2_CONNECTOR_CABLE_ATTACHED = "IEC_62196_Type_2_Connector_Cable_Attached"
    IEC_62196_TYPE_3_CONNECTOR_CABLE_ATTACHED = "IEC_62196_Type_3_Connector_Cable_Attached"
    COMBO_TO_IEC_62196_TYPE_1_BASE = "Combo_to_IEC_62196_Type_1_Base"
    COMBO_TO_IEC_62196_TYPE_2_BASE = "Combo_to_IEC_62196_Type_2_Base"
    TYPE_E_FRENCH_STANDARD_CEE_7_5 = "Type_E_French_Standard_CEE_7_5"
    TYPE_F_SCHUKO_CEE_7_4 = "Type_F_Schuko_CEE_7_4"
    TYPE_G_BRITISH_STANDARD_BS_1363 = "Type_G_British_Standard_BS_1363"
    TYPE_J_SWISS_STANDARD_SEV_1011 = "Type_J_Swiss_Standard_SEV_1011"
    CHINA_GB_PART_2 = "China_GB_Part_2"
    CHINA_GB_PART_3 = "China_GB_Part_3"
    IEC_309_DC_PLUG = "IEC_309_DC_Plug"
    AVCON_CONNECTOR = "AVCON_Connector"
    TESLA_CONNECTOR = "Tesla_Connector"
    NEMA_5_20 = "NEMA_5_20"
    CHADEMO = "CHAdeMO"
    SAE_J1772 = "SAE_J1772"
    TEPCO = "TEPCO"
    BETTER_PLACE_SOCKET = "Better_Place_Socket"
    MARECHAL_SOCKET = "Marechal_Socket"
    STANDARD_HOUSEHOLD_COUNTRY_SPECIFIC = "Standard_Household_Country_Specific"


@dataclass(kw_only=True)
class ReachableRange(DataClassORJSONMixin):
    """Represents a reachable range."""

    center: LatitudeLongitude
    boundary: list[LatitudeLongitude]


@dataclass(kw_only=True)
class Rectangle:
    """A rectangle defined by its south-west and north-east corners."""

    southWestCorner: LatitudeLongitude
    northEastCorner: LatitudeLongitude


@dataclass(kw_only=True)
class Rectangles:
    """A list of rectangles."""

    rectangles: list[Rectangle]


@dataclass(kw_only=True)
class Route(DataClassORJSONMixin):
    """Represents a route."""

    summary: Summary
    legs: list[Leg]
    sections: list[Section]


class RouteType(StrEnum):
    """Supported route types."""

    FASTEST = "fastest"
    SHORTEST = "shortest"
    SHORT = "short"
    ECO = "eco"
    THRILLING = "thrilling"


@dataclass(kw_only=True)
class Section(DataClassORJSONMixin):
    """Represents a section of a route."""

    startPointIndex: int
    endPointIndex: int
    sectionType: SectionReponseType
    travelMode: TravelModeType


class SectionReponseType(StrEnum):
    """Supported section reponse types."""

    CAR_TRAIN = "CAR_TRAIN"
    COUNTRY = "COUNTRY"
    FERRY = "FERRY"
    MOTORWAY = "MOTORWAY"
    PEDESTRIAN = "PEDESTRIAN"
    TOLL = "TOLL"
    TRAFFIC = "TRAFFIC"
    TRAVEL_MODE = "TRAVEL_MODE"
    TUNNEL = "TUNNEL"
    CARPOOL = "CARPOOL"
    URBAN = "URBAN"
    UNPAVED = "UNPAVED"
    LOW_EMISSION_ZONE = "LOW_EMISSION_ZONE"
    SPEED_LIMIT = "SPEED_LIMIT"


class SectionType(StrEnum):
    """Supported section types."""

    CAR_TRAIN = "carTrain"
    FERRY = "ferry"
    TUNNEL = "tunnel"
    MOTORWAY = "motorway"
    PEDESTRIAN = "pedestrian"
    TOLL_ROAD = "tollRoad"
    TOLL_VIGNETTE = "tollVignette"
    COUNTRY = "country"
    TRAVEL_MODE = "travelMode"
    TRAFFIC = "traffic"


@dataclass(kw_only=True)
class Summary(DataClassORJSONMixin):
    """Represents the summary of a route."""

    lengthInMeters: int
    travelTimeInSeconds: int
    trafficDelayInSeconds: int
    trafficLengthInMeters: int
    departureTime: datetime
    arrivalTime: datetime


class VehicleEngineType(StrEnum):
    """Supported vehicle engine types."""

    COMBUSTION = "combustion"
    ELECTRIC = "electric"


class VehicleLoadType(StrEnum):
    """Supported vehicle load types."""

    US_HAZMAT_CLASS_1 = "USHazmatClass1"  # Explosives (USA)
    US_HAZMAT_CLASS_2 = "USHazmatClass2"  # Compressed gas (USA)
    US_HAZMAT_CLASS_3 = "USHazmatClass3"  # Flammable liquids (USA)
    US_HAZMAT_CLASS_4 = "USHazmatClass4"  # Flammable solids (USA)
    US_HAZMAT_CLASS_5 = "USHazmatClass5"  # Oxidizers (USA)
    US_HAZMAT_CLASS_6 = "USHazmatClass6"  # Poisons (USA)
    US_HAZMAT_CLASS_7 = "USHazmatClass7"  # Radioactive (USA)
    US_HAZMAT_CLASS_8 = "USHazmatClass8"  # Corrosives (USA)
    US_HAZMAT_CLASS_9 = "USHazmatClass9"  # Miscellaneous (USA)
    OTHER_HAZMAT_EXPLOSIVE = "otherHazmatExplosive"  # Explosives (Rest of the world)
    OTHER_HAZMAT_GENERAL = "otherHazmatGeneral"  # Miscellaneous (Rest of the world)
    OTHER_HAZMAT_HARMFUL_TO_WATER = "otherHazmatHarmfulToWater"  # Harmful to water (Rest of the world)


@dataclass(kw_only=True)
class WaypointOptimizationOptions:
    """Options for the waypoint optimization API."""

    travelMode: TravelModeType
    vehicleMaxSpeed: int
    vehicleWeight: int
    vehicleAxleWeight: int
    vehicleLength: float
    vehicleWidth: float
    vehicleHeight: float
    vehicleCommercial: bool
    vehicleLoadType: list[VehicleLoadType]
    vehicleAdrTunnelRestrictionCode: AdrCategoryType


@dataclass(kw_only=True)
class WaypointOptimizationPoint:
    """A waypoint optimization point."""

    point: LatitudeLongitude


@dataclass(kw_only=True)
class WaypointOptimizationPostData(BasePostData):
    """Data for the post waypoint optimization API."""

    waypoints: list[WaypointOptimizationPoint]
    options: WaypointOptimizationOptions


@dataclass(kw_only=True)
class WaypointOptimizedResponse(DataClassORJSONMixin):
    """Represents a waypoint optimized response."""

    optimizedOrder: list[int]


class WindingnessType(StrEnum):
    """Supported windingness types."""

    LOW = "low"
    HIGH = "high"
