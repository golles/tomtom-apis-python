"""Models for the TomTom Places API"""
# pylint: disable=too-many-lines

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from geojson import Feature, FeatureCollection, GeometryCollection, LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon
from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin

from tomtom_api.api import BaseParams, BasePostData
from tomtom_api.models import Language, LatLon, ViewType


class AccessType(Enum):
    """Supported access types"""

    PUBLIC = "Public"
    AUTHORIZED = "Authorized"
    RESTRICTED = "Restricted"
    PRIVATE = "Private"


@dataclass(kw_only=True)
class AdditionalDataItem:
    """Represents an additional data response item"""

    # pylint: disable=invalid-name
    providerID: str
    error: str | None = None
    geometryData: (
        Feature | FeatureCollection | GeometryCollection | LineString | MultiLineString | MultiPoint | MultiPolygon | Point | Polygon | None
    ) = None


@dataclass(kw_only=True)
class AdditionalDataParams(BaseParams):
    """Parameters for the get_additional_data method"""

    # pylint: disable=invalid-name
    geometriesZoom: int | None = None


@dataclass(kw_only=True)
class AdditionalDataResponse(DataClassORJSONMixin):
    """Represents a Additional Data response"""

    # pylint: disable=invalid-name
    additionalData: list[AdditionalDataItem]


@dataclass(kw_only=True)
class Address(DataClassORJSONMixin):
    """Represents a Address"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    streetNumber: str | None = None
    streetName: str | None = None
    municipalitySubdivision: str | None = None
    municipalitySecondarySubdivision: str | None = None
    neighbourhood: str | None = None
    municipality: str | None = None
    countrySecondarySubdivision: str | None = None
    countryTertiarySubdivision: str | None = None
    countrySubdivision: str | None = None
    postalCode: str | None = None
    postalName: str | None = None
    extendedPostalCode: str | None = None
    countryCode: str | None = None
    country: str | None = None
    countryCodeISO3: str | None = None
    freeformAddress: str | None = None
    countrySubdivisionName: str | None = None
    countrySubdivisionCode: str | None = None
    localName: str | None = None


@dataclass(kw_only=True)
class AddressRange(DataClassORJSONMixin):
    """Represents a AddressRange"""

    # pylint: disable=invalid-name
    rangeLeft: str
    rangeRight: str
    _from: LatLon = field(metadata=field_options(alias="from"))
    to: LatLon


@dataclass(kw_only=True)
class Addresses(DataClassORJSONMixin):
    """Represents Addresses"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    address: RevGeocodeAddress
    position: str
    roadClass: list[Roadclass] | None = None
    # roadUse:  # Deprecated
    matchType: MatchType | None = None
    dataSources: DataSources | None = None
    entityType: list[EntityType] | None = None
    mapcodes: list[MapCode] | None = None
    id: str | None = None


@dataclass(kw_only=True)
class AsynchronousBatchDownloadParams(BaseParams):
    """Parameters for the get_asynchronous_batch_download method"""

    # pylint: disable=invalid-name
    waitTimeSeconds: int


@dataclass(kw_only=True)
class AsynchronousSynchronousBatchParams(BaseParams):
    """Parameters for the post_asynchronous_synchronous_batch method"""

    # pylint: disable=invalid-name
    redirectMode: RedirectModeType
    waitTimeSeconds: int


@dataclass(kw_only=True)
class AutocompleteParams(BaseParams):
    """Parameters for the get_autocomplete method"""

    # pylint: disable=invalid-name
    limit: int | None = None
    lat: float | None = None
    lon: float | None = None
    radius: int | None = None
    countrySet: list[str] | None = None
    resultSet: list[ResultSetType] | None = None


@dataclass(kw_only=True)
class AutocompleteReponse(DataClassORJSONMixin):
    """Represents an auto complete response"""

    context: Context
    results: list[AutocompleteResult]


@dataclass(kw_only=True)
class AutocompleteResult(DataClassORJSONMixin):
    """Represents an auto complete result"""

    segments: list[Segment]


@dataclass(kw_only=True)
class BatchItem:
    """Represents an BatchItem"""

    query: str
    post: list[Geometry | Route] | None = None


@dataclass(kw_only=True)
class BatchItemResponse(DataClassORJSONMixin):
    """Represents a Batch Item response"""

    # pylint: disable=invalid-name
    statusCode: int
    response: Response


@dataclass(kw_only=True)
class BatchPostData(BasePostData):
    """Data for the post Batch API"""

    # pylint: disable=invalid-name
    batchItems: list[BatchItem]


@dataclass(kw_only=True)
class BatchResponse(DataClassORJSONMixin):
    """Represents a Batch response"""

    # pylint: disable=invalid-name
    formatVersion: str
    batchItems: list[BatchItemResponse]
    summary: BatchResponseSummary


@dataclass(kw_only=True)
class BatchResponseSummary(DataClassORJSONMixin):
    """Represents a batch response summary"""

    # pylint: disable=invalid-name
    successfulRequests: int
    totalRequests: int


@dataclass(kw_only=True)
class BookmarkQueryIntent(DataClassORJSONMixin):
    """Represents a BookmarkQueryIntent"""

    bookmark: BookmarkType


class BookmarkType(Enum):
    """Supported bookmark types"""

    HOME = "HOME"
    WORK = "WORK"


@dataclass(kw_only=True)
class BoundingBox(DataClassORJSONMixin):
    """Represents a BoundingBox"""

    # pylint: disable=invalid-name
    topLeftPoint: LatLon
    btmRightPoint: LatLon


@dataclass(kw_only=True)
class Brand(DataClassORJSONMixin):
    """Represents a Brand"""

    name: str


class CapabilitieType(Enum):
    """Supported capabilities"""

    CHARGING_PROFILE_CAPABLE = "ChargingProfileCapable"
    CHARGING_PREFERENCES_CAPABLE = "ChargingPreferencesCapable"
    CHIP_CARD_SUPPORT = "ChipCardSupport"
    CONTACTLESS_CARD_SUPPORT = "ContactlessCardSupport"
    CREDIT_CARD_PAYABLE = "CreditCardPayable"
    DEBIT_CARD_PAYABLE = "DebitCardPayable"
    PED_TERMINAL = "PedTerminal"
    REMOTE_START_STOP_CAPABLE = "RemoteStartStopCapable"
    RESERVABLE = "Reservable"
    RFID_READER = "RfidReader"
    START_SESSION_CONNECTOR_REQUIRED = "StartSessionConnectorRequired"
    TOKEN_GROUP_CAPABLE = "TokenGroupCapable"
    UNLOCK_CAPABLE = "UnlockCapable"
    PLUG_AND_CHARGE = "PlugAndCharge"


@dataclass(kw_only=True)
class CategorySearchParams(BaseParams):
    """Parameters for the get_category_search method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    typeahead: bool | None = None
    limit: int | None = None
    ofs: int | None = None
    countrySet: list[str] | None = None
    lat: float | None = None
    lon: float | None = None
    radius: int | None = None
    topLeft: str | None = None
    btmRight: str | None = None
    geoBias: str | None = None
    language: Language | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    categorySet: list[str] | None = None
    brandSet: list[str] | None = None
    connectorSet: list[ConnectorType] | None = None
    minPowerKW: float | None = None
    maxPowerKW: float | None = None
    fuelSet: list[FuelType] | None = None
    vehicleTypeSet: list[VehicleType] | None = None
    view: ViewType | None = None
    openingHours: OpeningHoursType | None = None
    mapcodes: list[MapCodeType] | None = None
    timeZone: str | None = None
    relatedPois: RelatedPoisType | None = None


@dataclass(kw_only=True)
class ChargingPark(DataClassORJSONMixin):
    """Represents a ChargingPark"""

    connectors: list[Connector]


@dataclass(kw_only=True)
class ChargingPoint(DataClassORJSONMixin):
    """Represents a ChargingPoint"""

    # pylint: disable=invalid-name
    capabilities: list[CapabilitieType]
    connectors: list[Connector]
    evseId: str
    physicalReference: str | None = None
    status: StatusType


@dataclass(kw_only=True)
class ChargingStation(DataClassORJSONMixin):
    """Represents a ChargingStation"""

    # pylint: disable=invalid-name
    id: str
    chargingPoints: list[ChargingPoint]


@dataclass(kw_only=True)
class Classification(DataClassORJSONMixin):
    """Represents a Classification"""

    code: str
    names: list[Name]


@dataclass(kw_only=True)
class Connector(DataClassORJSONMixin):
    """
    Represents a Connector.
    Note that some API's use the field type while others use connectorType, after deserialization the values for both fields will be the same.
    """

    # pylint: disable=invalid-name
    id: str | None = None
    type: ConnectorType | None = None  # In EV search.
    connectorType: ConnectorType | None = None  # In general search.
    ratedPowerKW: float
    voltageV: int | None = None
    currentA: int | None = None
    currentType: CurrentType

    @classmethod
    def __post_deserialize__(cls, obj: "Connector") -> "Connector":
        # Handle the discrepancy between general search and EV search on connector type.
        if obj.type is not None and obj.connectorType is None:
            obj.connectorType = obj.type
        elif obj.connectorType is not None and obj.type is None:
            obj.type = obj.connectorType
        return obj


class ConnectorType(Enum):
    """Supported connector types"""

    STANDARD_HOUSEHOLD_COUNTRY_SPECIFIC = "StandardHouseholdCountrySpecific"
    IEC62196_TYPE1 = "IEC62196Type1"
    IEC62196_TYPE1_CCS = "IEC62196Type1CCS"
    IEC62196_TYPE2_CABLE_ATTACHED = "IEC62196Type2CableAttached"
    IEC62196_TYPE2_OUTLET = "IEC62196Type2Outlet"
    IEC62196_TYPE2_CCS = "IEC62196Type2CCS"
    IEC62196_TYPE3 = "IEC62196Type3"
    CHADEMO = "Chademo"
    GBT20234_PART2 = "GBT20234Part2"
    GBT20234_PART3 = "GBT20234Part3"
    IEC60309_AC3_PHASE_RED = "IEC60309AC3PhaseRed"
    IEC60309_AC1_PHASE_BLUE = "IEC60309AC1PhaseBlue"
    IEC60309_DC_WHITE = "IEC60309DCWhite"
    TESLA = "Tesla"


@dataclass(kw_only=True)
class Context(DataClassORJSONMixin):
    """Represents an auto complete context"""

    # pylint: disable=invalid-name
    inputQuery: str
    geoBias: GeoBias | None = None


@dataclass(kw_only=True)
class CoordinateQueryIntent(DataClassORJSONMixin):
    """Represents a CoordinateQueryIntent"""

    lat: float
    lon: float


@dataclass(kw_only=True)
class CrossStreetLookupParams(BaseParams):
    """Parameters for the get_cross_street_lookup method"""

    # pylint: disable=invalid-name
    limit: int | None = None
    radius: int | None = None
    language: Language | None = None
    allowFreeformNewLine: bool | None = None
    view: ViewType | None = None


class CurrentType(Enum):
    """Supported current types"""

    AC1 = "AC1"
    AC3 = "AC3"
    DC = "DC"


@dataclass(kw_only=True)
class DataSources(DataClassORJSONMixin):
    """Represents a DataSources"""

    # pylint: disable=invalid-name
    chargingAvailability: IdString


class EntityType(Enum):
    """Supported entity types"""

    COUNTRY = "Country"
    COUNTRY_SUBDIVISION = "CountrySubdivision"
    COUNTRY_SECONDARY_SUBDIVISION = "CountrySecondarySubdivision"
    COUNTRY_TERTIARY_SUBDIVISION = "CountryTertiarySubdivision"
    MUNICIPALITY = "Municipality"
    MUNICIPALITY_SUBDIVISION = "MunicipalitySubdivision"
    MUNICIPALITY_SECONDARY_SUBDIVISION = "MunicipalitySecondarySubdivision"
    NEIGHBOURHOOD = "Neighbourhood"
    POSTAL_CODE_AREA = "PostalCodeArea"


@dataclass(kw_only=True)
class EntryPoint(DataClassORJSONMixin):
    """Represents a EntryPoint"""

    # pylint: disable=invalid-name
    type: EntryPointType
    functions: list[FunctionType] | None = None
    pathToNext: PathToNextType | None = None
    position: LatLon


class EntryPointType(Enum):
    """Supported entry point types"""

    MAIN = "main"
    MINOR = "minor"
    ROUTE = "route"


@dataclass(kw_only=True)
class EvSearchByIdParams(BaseParams):
    """Parameters for the get_ev_search_by_id method"""

    id: str


@dataclass(kw_only=True)
class EvSearchNearbyParams(BaseParams):
    """Parameters for the get_ev_search_nearby method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    lat: float
    lon: float
    radius: int
    limit: int | None = None
    status: list[StatusType] | None = None
    connector: list[ConnectorType] | None = None
    accessType: list[AccessType] | None = None
    restriction: list[RestrictionType] | None = None
    capability: list[CapabilitieType] | None = None
    minPowerKW: float | None = None
    maxPowerKW: float | None = None


class ExtendedPostalCodesForType(Enum):
    """Supported extended postal codes"""

    ADDR = "Addr"
    PAD = "PAD"
    POI = "POI"
    NONE = "None"


class FilterType(Enum):
    """Supported filter types"""

    BACK_ROADS = "BackRoads"


class FuelType(Enum):
    """
    Supported fuel types,
    See: https://developer.tomtom.com/search-api/documentation/product-information/supported-fuel-types
    """

    PETROL = "Petrol"
    LPG = "LPG"
    DIESEL = "Diesel"
    BIO_DIESEL = "Biodiesel"
    DIESEL_FOR_COMMERCIAL_VEHICLES = "DieselForCommercialVehicles"
    E85 = "E85"
    LNG = "LNG"
    CNG = "CNG"
    HYDROGEN = "Hydrogen"
    AD_BLUE = "AdBlue"


class FunctionType(Enum):
    """Represents the type of access for the Address"""

    MAIN = "Main"
    POSTAL = "Postal"
    ROUTING = "Routing"
    EMERGENCY = "Emergency"
    PEDESTRIAN = "Pedestrian"
    DELIVERY = "Delivery"
    AUTHORIZED = "Authorized"
    FRONT_DOOR = "FrontDoor"
    # Premium content:
    PARKING = "PARKING"
    ENTRANCE = "ENTRANCE"
    ELEVATOR = "ELEVATOR"
    STAIR = "STAIR"


@dataclass(kw_only=True)
class GeoBias(DataClassORJSONMixin):
    """Represents a geo bias"""

    position: LatLon
    radius: int


@dataclass(kw_only=True)
class GeocodeParams(BaseParams):
    """Represents the parameters for get_geocode"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    storeResult: bool | None = None  # Deprecated
    typeahead: bool | None = None  # Deprecated
    limit: int | None = None
    ofs: int | None = None
    lat: float | None = None
    lon: float | None = None
    countrySet: str | None = None
    radius: int | None = None
    topLeft: str | None = None
    btmRight: str | None = None
    language: Language | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    view: ViewType | None = None
    mapcodes: list[MapCodeType] | None = None
    entityTypeSet: list[EntityType] | None = None


@dataclass(kw_only=True)
class Geometry:
    """Represents an geometry"""

    type: str
    position: str | None = None
    radius: int | None = None
    vertices: list[str] | None = None


@dataclass(kw_only=True)
class GeometryFilterData(BasePostData):
    """Data for the post geometry filter API"""

    # pylint: disable=invalid-name
    geometryList: list[Geometry]
    poiList: list[GeometryPoi]


@dataclass(kw_only=True)
class GeometryFilterResponse(DataClassORJSONMixin):
    """Represents a Geometry Filter response"""

    summary: Summary
    results: list[GeometryPoi]


@dataclass(kw_only=True)
class GeometryPoi:
    """Represents an geometry poi"""

    poi: Poi | None = None
    address: Address | None = None
    position: LatLon


@dataclass(kw_only=True)
class GeometrySearchParams(BaseParams):
    """Parameters for the get_geometry_search method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    limit: int | None = None
    language: Language | None = None
    lat: float | None = None
    lon: float | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    idxSet: list[IdxSetType] | None = None
    categorySet: list[str] | None = None
    brandSet: list[str] | None = None
    connectorSet: list[ConnectorType] | None = None
    minPowerKW: float | None = None
    maxPowerKW: float | None = None
    fuelSet: list[FuelType] | None = None
    vehicleTypeSet: list[VehicleType] | None = None
    view: ViewType | None = None
    openingHours: OpeningHoursType | None = None
    timeZone: str | None = None
    mapcodes: list[MapCodeType] | None = None
    relatedPois: RelatedPoisType | None = None
    entityTypeSet: list[EntityType] | None = None


@dataclass(kw_only=True)
class Id(DataClassORJSONMixin):
    """Represents an Id"""

    id: int


@dataclass(kw_only=True)
class IdString(DataClassORJSONMixin):
    """Represents an IdString"""

    id: str


class IdxSetType(Enum):
    """
    Supported IdxSet types.
    See: https://developer.tomtom.com/search-api/documentation/search-service/fuzzy-search#indexes-abbreviation-values
    """

    GEO = "Geo"
    PAD = "PAD"
    ADDR = "Addr"
    STR = "Str"
    XSTR = "XStr"
    POI = "POI"


@dataclass(kw_only=True)
class MapCode(DataClassORJSONMixin):
    """Represents a MapCode"""

    # pylint: disable=invalid-name
    type: MapCodeType
    fullMapcode: str
    territory: str
    code: str


class MapCodeType(Enum):
    """
    A mapcode represents a specific location to within a few meters. Every location on Earth can be represented by a mapcode. Mapcodes are designed to be short, easy to recognize, remember, and communicate. Visit the Mapcode project website for more information.
    See: http://www.mapcode.com/
    """

    LOCAL = "Local"
    INTERNATIONAL = "International"
    ALTERNATIVE = "Alternative"


@dataclass(kw_only=True)
class Match(DataClassORJSONMixin):
    """Represents a match"""

    offset: int
    length: int


class MatchType(Enum):
    """Supported match types"""

    ADDRESS_POINT = "AddressPoint"
    HOUSE_NUMBER_RANGE = "HouseNumberRange"
    STREET = "Street"


@dataclass(kw_only=True)
class Matches(DataClassORJSONMixin):
    """Represents a matches"""

    # pylint: disable=invalid-name
    inputQuery: list[Match]


@dataclass(kw_only=True)
class Name(DataClassORJSONMixin):
    """Represents a Name"""

    # pylint: disable=invalid-name
    nameLocale: str
    name: str


@dataclass(kw_only=True)
class NearbyQueryIntent(DataClassORJSONMixin):
    """Represents a NearbyQueryIntent"""

    lat: float
    lon: float
    query: str
    text: str


@dataclass(kw_only=True)
class NearbySearchParams(BaseParams):
    """Parameters for the get_nearby_search method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    limit: int | None = None
    ofs: int | None = None
    countrySet: list[str] | None = None
    radius: int | None = None
    topLeft: str | None = None
    btmRight: str | None = None
    language: Language | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    categorySet: list[str] | None = None
    brandSet: list[str] | None = None
    connectorSet: list[ConnectorType] | None = None
    minPowerKW: float | None = None
    maxPowerKW: float | None = None
    fuelSet: list[FuelType] | None = None
    vehicleTypeSet: list[VehicleType] | None = None
    view: ViewType | None = None
    openingHours: OpeningHoursType | None = None
    mapcodes: list[MapCodeType] | None = None
    timeZone: str | None = None
    relatedPois: RelatedPoisType | None = None


@dataclass(kw_only=True)
class OpeningHour(DataClassORJSONMixin):
    """Represents an OpeningHour"""

    # pylint: disable=invalid-name
    mode: str
    timeRanges: list[TimeRange]


class OpeningHoursType(Enum):
    """Supported opening hours type"""

    NEXT_SEVEN_DAYS = "nextSevenDays"


class PathToNextType(Enum):
    """Supported path to next types"""

    DRIVING = "DRIVING"
    WALKING = "WALKING"
    UNKNOWN = "UNKNOWN"


@dataclass(kw_only=True)
class PaymentOption(DataClassORJSONMixin):
    """Represents a PaymentOption"""

    brands: list[Brand]


@dataclass(kw_only=True)
class PlaceByIdParams(BaseParams):
    """Parameters for the get_place_by_id method"""

    # pylint: disable=invalid-name
    entityId: str
    language: Language | None = None
    openingHours: OpeningHoursType | None = None
    timeZone: str | None = None
    mapcodes: list[MapCodeType] | None = None
    relatedPois: RelatedPoisType | None = None
    view: ViewType | None = None


@dataclass(kw_only=True)
class PlaceByIdResponse(DataClassORJSONMixin):
    """Represents a Place by Id response"""

    summary: Summary
    results: list[Result]


@dataclass(kw_only=True)
class Poi(DataClassORJSONMixin):
    """Represents a Result"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    name: str
    phone: str | None = None
    brands: list[Brand] | None = None
    url: str | None = None
    # categories: list[str]  # Deprecated: Use classifications instead. As of May 1, 2018
    categorySet: list[Id] | None = None
    openingHours: list[OpeningHour] | None = None
    classifications: list[Classification] | None = None
    timeZone: TimeZone | None = None


@dataclass(kw_only=True)
class PoiCategoriesParams(BaseParams):
    """Represents the parameters for get_poi_categories"""

    language: Language | None = None


@dataclass(kw_only=True)
class PoiCategoriesResponse(DataClassORJSONMixin):
    """Represents a Poi Categories response"""

    # pylint: disable=invalid-name
    poiCategories: list[PoiCategory] | None = None


@dataclass(kw_only=True)
class PoiCategory(DataClassORJSONMixin):
    """Represents a PoiCategory"""

    # pylint: disable=invalid-name
    id: int
    name: str
    childCategoryIds: list[int]
    synonyms: list[str]


@dataclass(kw_only=True)
class PoiSearchParams(BaseParams):
    """Parameters for the get_poi_search method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    typeahead: bool | None = None
    limit: int | None = None
    ofs: int | None = None
    countrySet: list[str] | None = None
    lat: float | None = None
    lon: float | None = None
    radius: int | None = None
    topLeft: str | None = None
    btmRight: str | None = None
    geoBias: str | None = None
    language: Language | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    categorySet: list[str] | None = None
    brandSet: list[str] | None = None
    connectorSet: list[ConnectorType] | None = None
    minPowerKW: float | None = None
    maxPowerKW: float | None = None
    fuelSet: list[FuelType] | None = None
    vehicleTypeSet: list[VehicleType] | None = None
    view: ViewType | None = None
    openingHours: OpeningHoursType | None = None
    mapcodes: list[MapCodeType] | None = None
    timeZone: str | None = None
    relatedPois: RelatedPoisType | None = None


@dataclass(kw_only=True)
class Points:
    """Represents route points"""

    points: list[LatLon]


@dataclass(kw_only=True)
class PremiumGeocodeParams(BaseParams):
    """Parameters for the premium get_geocode method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    unit: str | None = None
    limit: int | None = None
    ofs: int | None = None
    lat: float | None = None
    lon: float | None = None
    countrySet: list[str] | None = None
    radius: int | None = None
    topLeft: str | None = None
    btmRight: str | None = None
    language: Language | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    view: ViewType | None = None
    mapcodes: list[MapCodeType] | None = None
    entityTypeSet: list[EntityType] | None = None


@dataclass(kw_only=True)
class QueryIntent(DataClassORJSONMixin):
    """Represents a QueryIntent"""

    type: QueryIntentType
    details: CoordinateQueryIntent | NearbyQueryIntent | W3WQueryIntent | BookmarkQueryIntent


class QueryIntentType(Enum):
    """Supported query intent types"""

    COORDINATE = "COORDINATE"
    NEARBY = "NEARBY"
    W3W = "W3W"
    BOOKMARK = "BOOKMARK"


class QueryType(Enum):
    """Supported query types"""

    NEARBY = "NEARBY"
    NON_NEAR = "NON_NEAR"


class RedirectModeType(Enum):
    """Supported redirect mode types"""

    AUTO = "auto"
    MANUAL = "manual"


@dataclass(kw_only=True)
class RelatedPoi(DataClassORJSONMixin):
    """Represents a RelatedPoi"""

    # pylint: disable=invalid-name
    relationType: RelationType
    id: str


class RelatedPoisType(Enum):
    """Supported related pois type"""

    ALL = "all"
    CHILD = "child"
    OFF = "off"
    PARENT = "parent"


class RelationType(Enum):
    """Supported relation types"""

    CHILD = "child"
    PARENT = "parent"


@dataclass(kw_only=True)
class Response(DataClassORJSONMixin):
    """Represents a Batch Item Response"""

    # pylint: disable=invalid-name
    summary: Summary | None = None
    results: list[Result] | None = None
    errorText: str | None = None
    message: str | None = None
    httpStatusCode: int | None = None


class RestrictionType(Enum):
    """Supported parking restrictions"""

    EV_ONLY = "evOnly"
    PLUGGED = "plugged"
    DISABLED = "disabled"
    CUSTOMERS = "customers"
    MOTORCYCLES = "motorcycles"


@dataclass(kw_only=True)
class Result(DataClassORJSONMixin):
    """Represents a Result"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    type: ResultType | None = None
    id: str
    score: float | None = None
    dist: float | None = None
    info: str | None = None
    entityType: EntityType | None = None
    poi: Poi | None = None
    relatedPois: list[RelatedPoi] | None = None
    address: Address
    position: LatLon
    mapcodes: list[MapCode] | None = None
    viewport: Viewport | None = None
    boundingBox: BoundingBox | None = None
    entryPoints: list[EntryPoint] | None = None
    detourTime: int | None = None
    detourDistance: int | None = None
    detourOffset: int | None = None
    addressRanges: list[AddressRange] | None = None
    chargingPark: ChargingPark | None = None
    dataSources: DataSources | None = None
    fuelTypes: list[FuelType] | None = None
    vehicleTypes: list[VehicleType] | None = None
    chargingStations: list[ChargingStation] | None = None
    openingHours: OpeningHour | None = None
    timeZone: TimeZone | None = None
    paymentOptions: list[PaymentOption] | None = None
    accessType: AccessType | None = None


class ResultSetType(Enum):
    """Supported result set types"""

    CATEGORY = "category"
    BRAND = "brand"


class ResultType(Enum):
    """Supported result types"""

    POI = "POI"
    STREET = "Street"
    GEOGRAPHY = "Geography"
    POINT_ADDRESS = "Point Address"
    ADDRESS = "Address"
    ADDRESS_RANGE = "Address Range"
    CROSS_STREET = "Cross Street"


@dataclass(kw_only=True)
class RevGeoBoundingBox(DataClassORJSONMixin):
    """Represents a BoundingBox for reverse geocode"""

    # pylint: disable=invalid-name
    northEast: str
    southWest: str
    entity: RevGeoEntityType


class RevGeoEntityType(Enum):
    """Supported rev geo entity types"""

    POSITION = "position"


@dataclass(kw_only=True)
class RevGeocodeAddress(DataClassORJSONMixin):
    """Represents a Reverse Geocode Address"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    buildingNumber: str | None = None  # Deprecated
    building: str | None = None
    streetNumber: str | None = None
    routeNumbers: list | None = None
    street: str | None = None  # Deprecated
    streetName: str
    crossStreet: str | None = None
    streetNameAndNumber: str | None = None
    speedLimit: str | None = None
    countryCode: str
    countrySubdivision: str | None = None
    countrySecondarySubdivision: str | None = None
    countryTertiarySubdivision: str | None = None
    municipality: str
    postalName: str | None = None
    postalCode: str | None = None
    municipalitySubdivision: str | None = None
    municipalitySecondarySubdivision: str | None = None
    neighbourhood: str | None = None
    sideOfStreet: str | None = None  # Deprecated
    offsetPosition: str | None = None  # Deprecated
    country: str
    countryCodeISO3: str
    freeformAddress: str
    boundingBox: RevGeoBoundingBox | None = None
    countrySubdivisionName: str | None = None
    countrySubdivisionCode: str | None = None
    localName: str | None = None


@dataclass(kw_only=True)
class ReverseGeocodeParams(BaseParams):
    """Parameters for the get_reverse_geocode method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    returnSpeedLimit: bool | None = None
    heading: float | None = None
    radius: int | None = None
    # number Deprecated: Support for the number parameter will be removed.
    # returnRoadClass Deprecated: Right now, the service supports only a single value, but in future, it may change.
    # returnRoadUse Deprecated: Support for the returnRoadUse parameter will be removed.
    # roadUse Deprecated: Support for the roadUse parameter will be removed.
    entityType: list[EntityType] | None = None
    language: Language | None = None
    allowFreeformNewLine: bool | None = None
    returnMatchType: bool | None = None
    view: ViewType | None = None
    mapcodes: list[MapCodeType] | None = None
    filter: FilterType | None = None


@dataclass(kw_only=True)
class ReverseGeocodeResponse(DataClassORJSONMixin):
    """Represents a reverse geocode response"""

    summary: Summary
    addresses: list[Addresses]


class RoadClassType(Enum):
    """Supported road class types"""

    FUNCTIONAL = "Functional"


class RoadClassTypeValue(Enum):
    """Represents a classification of roads"""

    MOTORWAY = "Motorway"
    TRUNK = "Trunk"
    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    TERTIARY = "Tertiary"
    STREET = "Street"
    FERRY = "Ferry"
    OTHER = "Other"


@dataclass(kw_only=True)
class Roadclass(DataClassORJSONMixin):
    """Represents Roadclass"""

    type: RoadClassType
    values: list[RoadClassTypeValue]


@dataclass(kw_only=True)
class Route:
    """Represents an Route"""

    points: list[LatLon]


@dataclass(kw_only=True)
class SearchAlongRouteData(BasePostData):
    """Data for the post search along route API"""

    route: Points


@dataclass(kw_only=True)
class SearchAlongRouteParams(BaseParams):
    """Parameters for the post_search_along_route method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    typeahead: bool | None = None
    limit: int | None = None
    categorySet: list[str] | None = None
    brandSet: list[str] | None = None
    connectorSet: list[ConnectorType] | None = None
    minPowerKW: float | None = None
    maxPowerKW: float | None = None
    fuelSet: list[FuelType] | None = None
    vehicleTypeSet: list[VehicleType] | None = None
    view: ViewType | None = None
    detourOffset: bool | None = None
    sortBy: SortByType | None = None
    language: Language | None = None
    openingHours: OpeningHoursType | None = None
    spreadingMode: str | None = None
    mapcodes: list[MapCodeType] | None = None
    timeZone: str | None = None
    relatedPois: RelatedPoisType | None = None


@dataclass(kw_only=True)
class SearchParams(BaseParams):
    """Parameters for the get_search method"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    typeahead: bool | None = None
    limit: int | None = None
    ofs: int | None = None
    countrySet: list[str] | None = None
    lat: float | None = None
    lon: float | None = None
    radius: int | None = None
    topLeft: str | None = None
    btmRight: str | None = None
    geoBias: str | None = None
    language: Language | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    minFuzzyLevel: int | None = None
    maxFuzzyLevel: int | None = None
    idxSet: list[IdxSetType] | None = None
    categorySet: list[str] | None = None
    brandSet: list[str] | None = None
    connectorSet: list[ConnectorType] | None = None
    minPowerKW: float | None = None
    maxPowerKW: float | None = None
    fuelSet: list[FuelType] | None = None
    vehicleTypeSet: list[VehicleType] | None = None
    view: ViewType | None = None
    openingHours: OpeningHoursType | None = None
    timeZone: str | None = None
    mapcodes: list[MapCodeType] | None = None
    relatedPois: RelatedPoisType | None = None
    entityTypeSet: list[EntityType] | None = None


@dataclass(kw_only=True)
class SearchResponse(DataClassORJSONMixin):
    """Represents a Search response"""

    summary: Summary
    results: list[Result]


@dataclass(kw_only=True)
class Segment(DataClassORJSONMixin):
    """Represents an auto complete segment"""

    # pylint: disable=invalid-name
    type: str
    value: str
    matches: Matches
    id: str | None = None
    matchedAlternativeName: str | None = None


class SortByType(Enum):
    """Supported sort by type"""

    DETOUR_TIME = "detourTime"
    DETOUR_OFFSET = "detourOffset"


class StatusType(Enum):
    """Supported current types"""

    AVAILABLE = "Available"
    RESERVED = "Reserved"
    OCCUPIED = "Occupied"
    OUT_OF_SERVICE = "OutOfService"
    UNKNOWN = "Unknown"


@dataclass(kw_only=True)
class StructuredGeocodeParams(BaseParams):
    """Represents the parameters for get_structured_geocode"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    limit: int | None = None
    ofs: int | None = None
    streetNumber: str | None = None
    streetName: str | None = None
    crossStreet: str | None = None
    municipality: str | None = None
    municipalitySubdivision: str | None = None
    countryTertiarySubdivision: str | None = None
    countrySecondarySubdivision: str | None = None
    countrySubdivision: str | None = None
    postalCode: str | None = None
    language: Language | None = None
    extendedPostalCodesFor: list[ExtendedPostalCodesForType] | None = None
    view: ViewType | None = None
    entityTypeSet: list[EntityType] | None = None


@dataclass(kw_only=True)
class Summary(DataClassORJSONMixin):
    """Represents a response Summary"""

    # pylint: disable=invalid-name, too-many-instance-attributes
    query: str | None = None
    queryTime: int | None = None
    queryType: QueryType | None = None  # Deprecated
    numResults: int
    offset: int | None = None
    totalResults: int | None = None
    fuzzyLevel: int | None = None
    geoBias: LatLon | None = None
    queryIntent: list[QueryIntent] | None = None


@dataclass(kw_only=True)
class SynchronousBatchPostReponse(DataClassORJSONMixin):
    """Represents a Synchronous Batch Item response"""

    # pylint: disable=invalid-name
    statusCode: int
    response: Response


@dataclass(kw_only=True)
class Time(DataClassORJSONMixin):
    """Represents a Time"""

    date: date
    hour: int
    minute: int


@dataclass(kw_only=True)
class TimeRange(DataClassORJSONMixin):
    """Represents a TimeRange"""

    # pylint: disable=invalid-name
    startTime: Time
    endTime: Time


@dataclass(kw_only=True)
class TimeZone(DataClassORJSONMixin):
    """Represents a TimeZone"""

    # pylint: disable=invalid-name
    ianaId: str


class VehicleType(Enum):
    """Supported vehicle types"""

    CAR = "Car"
    TRUCK = "Truck"


@dataclass(kw_only=True)
class Viewport(DataClassORJSONMixin):
    """Represents a Viewport"""

    # pylint: disable=invalid-name
    topLeftPoint: LatLon
    btmRightPoint: LatLon


@dataclass(kw_only=True)
class W3WQueryIntent(DataClassORJSONMixin):
    """Represents a W3WQueryIntent"""

    address: str
