"""Models for the TomTom Routing API."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from mashumaro.mixins.orjson import DataClassORJSONMixin

from tomtom_api.api import BaseParams, BasePostData
from tomtom_api.models import Language, LatitudeLongitude


@dataclass(kw_only=True)
class CalculateRouteParams(BaseParams):
    """Parameters for the calculate route API."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    maxAlternatives: int | None = None
    instructionsType: str | None = None
    language: Language | None = None
    computeBestOrder: bool | None = None
    routeRepresentation: str | None = None
    computeTravelTimeFor: str | None = None
    vehicleHeading: int | None = None
    sectionType: str | None = None
    report: str | None = None
    departAt: str | None = None
    arriveAt: str | None = None
    routeType: str | None = None
    traffic: bool | None = None
    avoid: str | None = None
    travelMode: str | None = None
    hilliness: str | None = None
    windingness: str | None = None
    vehicleMaxSpeed: int | None = None
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    vehicleNumberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    vehicleCommercial: bool | None = None
    vehicleLoadType: str | None = None
    vehicleAdrTunnelRestrictionCode: str | None = None
    vehicleEngineType: str | None = None
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
class CalculateReachableRouteParams(BaseParams):
    """Parameters for the calculate reachable route API."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    fuelBudgetInLiters: float | None = None
    energyBudgetInkWh: float | None = None
    timeBudgetInSec: float | None = None
    report: str | None = None
    departAt: str | None = None
    arriveAt: str | None = None
    routeType: str | None = None
    traffic: bool | None = None
    avoid: str | None = None
    travelMode: str | None = None
    hilliness: str | None = None
    windingness: str | None = None
    vehicleMaxSpeed: int | None = None
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    vehicleNumberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    vehicleCommercial: bool | None = None
    vehicleLoadType: str | None = None
    vehicleAdrTunnelRestrictionCode: str | None = None
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
    vehicleEngineType: str | None = None
    constantSpeedConsumptionInkWhPerHundredkm: str | None = None


@dataclass(kw_only=True)
class CalculateLongDistanceEVRouteParams(BaseParams):
    """Parameters for the calculate long distance EV route API."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    vehicleHeading: int | None = None
    sectionType: str | None = None
    report: str | None = None
    departAt: str | None = None
    routeType: str | None = None
    traffic: bool | None = None
    avoid: str | None = None
    travelMode: str | None = None
    vehicleMaxSpeed: int | None = None
    vehicleWeight: int | None = None
    vehicleAxleWeight: int | None = None
    vehicleNumberOfAxles: int | None = None
    vehicleLength: float | None = None
    vehicleWidth: float | None = None
    vehicleHeight: float | None = None
    vehicleCommercial: bool | None = None
    vehicleLoadType: str | None = None
    vehicleAdrTunnelRestrictionCode: str | None = None
    vehicleEngineType: str
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
class Rectangle:
    """A rectangle defined by its south-west and north-east corners."""

    # pylint: disable=invalid-name
    southWestCorner: LatitudeLongitude
    northEastCorner: LatitudeLongitude


@dataclass(kw_only=True)
class Rectangles:
    """A list of rectangles."""

    rectangles: list[Rectangle]


@dataclass(kw_only=True)
class CalculateRoutePostData(BasePostData):
    """Data for the post calculate route API."""

    # pylint: disable=invalid-name
    supportingPoints: list[LatitudeLongitude] | None = None
    avoidVignette: list[str] | None = None
    allowVignette: list[str] | None = None
    avoidAreas: Rectangles | None = None


@dataclass(kw_only=True)
class CalculateReachableRangePostData(BasePostData):
    """Data for the post calculate reachable range API."""

    # pylint: disable=invalid-name
    avoidVignette: list[str] | None = None
    allowVignette: list[str] | None = None
    avoidAreas: Rectangles | None = None


@dataclass(kw_only=True)
class ChargingConnection(DataClassORJSONMixin):
    """Represents a charging connection."""

    # pylint: disable=invalid-name
    facilityType: str
    plugType: str


@dataclass(kw_only=True)
class ChargingCurve(DataClassORJSONMixin):
    """Represents a charging curve."""

    # pylint: disable=invalid-name
    chargeInkWh: float
    timeToChargeInSeconds: int


@dataclass(kw_only=True)
class ChargingMode(DataClassORJSONMixin):
    """Represents a charging mode."""

    # pylint: disable=invalid-name
    chargingConnections: list[ChargingConnection]
    chargingCurve: list[ChargingCurve]


@dataclass(kw_only=True)
class CalculateLongDistanceEVRoutePostData(BasePostData):
    """Data for the post calculate long distance EV route API."""

    # pylint: disable=invalid-name
    chargingModes: list[ChargingMode]


@dataclass(kw_only=True)
class Summary(DataClassORJSONMixin):
    """Represents the summary of a route."""

    # pylint: disable=invalid-name
    lengthInMeters: int
    travelTimeInSeconds: int
    trafficDelayInSeconds: int
    trafficLengthInMeters: int
    departureTime: datetime
    arrivalTime: datetime


@dataclass(kw_only=True)
class ChargingConnectionInfo(DataClassORJSONMixin):
    """Represents the charging connection info."""

    # pylint: disable=invalid-name
    chargingVoltageInV: int
    chargingCurrentInA: int
    chargingCurrentType: str
    chargingPowerInkW: int
    chargingPlugType: str


@dataclass(kw_only=True)
class ChargingParkLocation(DataClassORJSONMixin):
    """Represents a charging park location."""

    # pylint: disable=invalid-name
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


@dataclass(kw_only=True)
class ChargingInformationAtEndOfLeg(DataClassORJSONMixin):
    """Represents the charging information at the end of a leg."""

    # pylint: disable=invalid-name, too-many-instance-attributes
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
    chargingStopType: str


@dataclass(kw_only=True)
class EVLegSummary(DataClassORJSONMixin):
    """Represents the summary of a EV leg."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    lengthInMeters: int
    travelTimeInSeconds: int
    trafficDelayInSeconds: int
    trafficLengthInMeters: int
    departureTime: str
    arrivalTime: str
    batteryConsumptionInkWh: float
    remainingChargeAtArrivalInkWh: float
    chargingInformationAtEndOfLeg: ChargingInformationAtEndOfLeg


@dataclass(kw_only=True)
class EVSummary(DataClassORJSONMixin):
    """Represents the EV summary of a route."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    lengthInMeters: int
    travelTimeInSeconds: int
    trafficDelayInSeconds: int
    trafficLengthInMeters: int
    departureTime: str
    arrivalTime: str
    batteryConsumptionInkWh: float
    remainingChargeAtArrivalInkWh: float
    totalChargingTimeInSeconds: float


@dataclass(kw_only=True)
class Leg(DataClassORJSONMixin):
    """Represents a leg of a route."""

    summary: Summary
    points: list[LatitudeLongitude]


@dataclass(kw_only=True)
class EVLeg(DataClassORJSONMixin):
    """Represents a leg of a EV route."""

    summary: EVLegSummary | Summary
    points: list[LatitudeLongitude]


@dataclass(kw_only=True)
class Section(DataClassORJSONMixin):
    """Represents a section of a route."""

    # pylint: disable=invalid-name
    startPointIndex: int
    endPointIndex: int
    sectionType: str
    travelMode: str


@dataclass(kw_only=True)
class Route(DataClassORJSONMixin):
    """Represents a route."""

    summary: Summary
    legs: list[Leg]
    sections: list[Section]


@dataclass(kw_only=True)
class EVRoute(DataClassORJSONMixin):
    """Represents a EV route."""

    summary: EVSummary
    legs: list[EVLeg]
    sections: list[Section]


@dataclass(kw_only=True)
class CalculatedRouteResponse(DataClassORJSONMixin):
    """Represents a calculated route response."""

    # pylint: disable=invalid-name
    formatVersion: str
    routes: list[Route]


@dataclass(kw_only=True)
class CalculatedLongDistanceEVRouteResponse(DataClassORJSONMixin):
    """Represents a calculated long distance EV route response."""

    # pylint: disable=invalid-name
    formatVersion: str
    routes: list[EVRoute]


@dataclass(kw_only=True)
class ReachableRange(DataClassORJSONMixin):
    """Represents a reachable range."""

    center: LatitudeLongitude
    boundary: list[LatitudeLongitude]


@dataclass(kw_only=True)
class CalculatedReachableRangeResponse(DataClassORJSONMixin):
    """Represents a calculated reachable range response."""

    # pylint: disable=invalid-name
    formatVersion: str
    reachableRange: ReachableRange


@dataclass(kw_only=True)
class WaypointOptimizationPoint:
    """A waypoint optimization point."""

    point: LatitudeLongitude


@dataclass(kw_only=True)
class WaypointOptimizationOptions:
    """Options for the waypoint optimization API."""

    # pylint: disable=invalid-name, too-many-instance-attributes
    travelMode: str
    vehicleMaxSpeed: int
    vehicleWeight: int
    vehicleAxleWeight: int
    vehicleLength: float
    vehicleWidth: float
    vehicleHeight: float
    vehicleCommercial: bool
    vehicleLoadType: list[str]
    vehicleAdrTunnelRestrictionCode: str


@dataclass(kw_only=True)
class WaypointOptimizationPostData(BasePostData):
    """Data for the post waypoint optimization API."""

    # pylint: disable=invalid-name
    waypoints: list[WaypointOptimizationPoint]
    options: WaypointOptimizationOptions


@dataclass(kw_only=True)
class WaypointOptimizedResponse(DataClassORJSONMixin):
    """Represents a waypoint optimized response."""

    # pylint: disable=invalid-name
    optimizedOrder: list[int]
