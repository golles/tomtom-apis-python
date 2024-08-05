"""Models for the TomTom Automotive API."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from mashumaro.mixins.orjson import DataClassORJSONMixin

from tomtom_api.api import BaseParams


@dataclass(kw_only=True)
class FuelPrizeParams(BaseParams):
    """
    Parameters for the get_fuel_prize method.
    """

    # pylint: disable=invalid-name
    fuelPrice: str


@dataclass(kw_only=True)
class ParkingAvailabilityParams(BaseParams):
    """
    Parameters for the get_parking_availability method.
    """

    # pylint: disable=invalid-name
    parkingAvailability: str


@dataclass(kw_only=True)
class Current(DataClassORJSONMixin):
    """Represents a Current."""

    # pylint: disable=invalid-name
    available: bool
    emptySpots: int
    availabilityTrend: str
    updatedAt: datetime


@dataclass(kw_only=True)
class Status(DataClassORJSONMixin):
    """Represents a Status."""

    current: Current


@dataclass(kw_only=True)
class ParkingAvailabilityResponse(DataClassORJSONMixin):
    """Represents a ParkingAvailability response."""

    # pylint: disable=invalid-name
    parkingAvailability: str
    statuses: list[Status]


@dataclass(kw_only=True)
class Price(DataClassORJSONMixin):
    """Represents a Price."""

    # pylint: disable=invalid-name
    value: float
    currency: str
    currencySymbol: str
    volumeUnit: str


@dataclass(kw_only=True)
class Fuel(DataClassORJSONMixin):
    """Represents a Fuel."""

    # pylint: disable=invalid-name
    type: list[str]
    price: list[Price]
    updatedAt: datetime


@dataclass(kw_only=True)
class FuelPricesResponse(DataClassORJSONMixin):
    """Represents a FuelPrices response."""

    # pylint: disable=invalid-name
    fuelPrice: str
    fuels: list[Fuel]
