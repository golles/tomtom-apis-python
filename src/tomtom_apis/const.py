"""Constants for the TomTom API."""

from enum import IntEnum, StrEnum
from typing import Final

TRACKING_ID_HEADER: Final[str] = "Tracking-ID"
TOMTOM_HEADER_PREFIX: Final[str] = "x-tomtom"


class HttpMethod(StrEnum):
    """HTTP methods used in TomTom API requests."""

    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"


class HttpStatus(IntEnum):
    """HTTP status codes used in TomTom API responses."""

    OK = 200
    UNASSIGNED = 399
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500
