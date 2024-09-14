"""Automotive APIs."""

from .autostream import AutoStreamApi
from .fuel_prices import FuelPricesApi
from .parking_availability import ParkingAvailabilityApi

__all__ = [
    "AutoStreamApi",
    "FuelPricesApi",
    "ParkingAvailabilityApi",
]
