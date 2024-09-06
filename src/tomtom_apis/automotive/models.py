"""Models for the TomTom Automotive API"""
# pylint: disable=invalid-name, too-many-instance-attributes, too-many-lines

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from mashumaro.mixins.orjson import DataClassORJSONMixin

from ..api import BaseParams


@dataclass(kw_only=True)
class Current(DataClassORJSONMixin):
    """Represents a Current"""

    available: bool
    emptySpots: int
    availabilityTrend: str
    updatedAt: datetime


@dataclass(kw_only=True)
class Fuel(DataClassORJSONMixin):
    """Represents a Fuel"""

    type: list[str]
    price: list[Price]
    updatedAt: datetime


@dataclass(kw_only=True)
class FuelPricesResponse(DataClassORJSONMixin):
    """Represents a FuelPrices response"""

    fuelPrice: str
    fuels: list[Fuel]


@dataclass(kw_only=True)
class FuelPrizeParams(BaseParams):
    """
    Parameters for the get_fuel_prize method.
    """

    fuelPrice: str


@dataclass(kw_only=True)
class ParkingAvailabilityParams(BaseParams):
    """
    Parameters for the get_parking_availability method.
    """

    parkingAvailability: str


@dataclass(kw_only=True)
class ParkingAvailabilityResponse(DataClassORJSONMixin):
    """Represents a ParkingAvailability response"""

    parkingAvailability: str
    statuses: list[Status]


@dataclass(kw_only=True)
class Price(DataClassORJSONMixin):
    """Represents a Price"""

    value: float
    currency: str
    currencySymbol: str
    volumeUnit: str


@dataclass(kw_only=True)
class Status(DataClassORJSONMixin):
    """Represents a Status"""

    current: Current
