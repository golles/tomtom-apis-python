"""Models for the TomTom Automotive API."""
# pylint: disable=invalid-name, too-many-instance-attributes, too-many-lines

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

from mashumaro.mixins.orjson import DataClassORJSONMixin

from ..api import BaseParams


@dataclass(kw_only=True)
class Current(DataClassORJSONMixin):
    """Represents a Current."""

    available: bool
    emptySpots: int
    availabilityTrend: str
    updatedAt: datetime


@dataclass(kw_only=True)
class Fuel(DataClassORJSONMixin):
    """Represents a Fuel."""

    type: FuelType
    price: list[Price]
    updatedAt: datetime


@dataclass(kw_only=True)
class FuelPricesResponse(DataClassORJSONMixin):
    """Represents a FuelPrices response."""

    fuelPrice: str
    fuels: list[Fuel]


@dataclass(kw_only=True)
class FuelPrizeParams(BaseParams):
    """Parameters for the get_fuel_prize method."""

    fuelPrice: str


class FuelType(StrEnum):
    """Supported fuel types."""

    BIODIESEL = "biodiesel"
    CNG = "cng"
    DIESEL = "diesel"
    DIESEL_PLUS = "dieselPlus"
    DIESEL_PLUS_WITHOUT_ADDITIVES = "dieselPlusWithoutAdditives"
    DIESEL_WITHOUT_ADDITIVES = "dieselWithoutAdditives"
    E100 = "e100"
    E80 = "e80"
    E85 = "e85"
    ETHANOL_WITHOUT_ADDITIVES = "ethanolWithoutAdditives"
    LPG = "lpg"
    REGULAR = "regular"
    SP100 = "sp100"
    SP91 = "sp91"
    SP91_E10 = "sp91_e10"
    SP92 = "sp92"
    SP92_PLUS = "sp92Plus"
    SP93 = "sp93"
    SP95 = "sp95"
    SP95_E10 = "sp95_e10"
    SP95_PLUS = "sp95Plus"
    SP95_WITHOUT_ADDITIVES = "sp95WithoutAdditives"
    SP97 = "sp97"
    SP98 = "sp98"
    SP98_PLUS = "sp98Plus"
    SP99 = "sp99"


@dataclass(kw_only=True)
class ParkingAvailabilityParams(BaseParams):
    """Parameters for the get_parking_availability method."""

    parkingAvailability: str


@dataclass(kw_only=True)
class ParkingAvailabilityResponse(DataClassORJSONMixin):
    """Represents a ParkingAvailability response."""

    parkingAvailability: str
    statuses: list[Status]


@dataclass(kw_only=True)
class Price(DataClassORJSONMixin):
    """Represents a Price."""

    value: float
    currency: str
    currencySymbol: str
    volumeUnit: str


@dataclass(kw_only=True)
class Status(DataClassORJSONMixin):
    """Represents a Status."""

    current: Current
