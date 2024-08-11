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


class IncidentStyleType(Enum):
    """Supported incident tyle style types"""

    S0 = "s0"
    S0_DARK = "s0-dark"
    S1 = "s1"
    S2 = "s2"
    S3 = "s3"
    NIGHT = "night"


@dataclass(kw_only=True)
class RasterIncidentTilesParams(BaseParams):
    """
    Parameters for the get_raster_incident_tile method.
    """

    # pylint: disable=invalid-name
    t: str | None = None
    tileSize: TileSizeType | None = None


@dataclass(kw_only=True)
class VectorIncidentTilesParams(BaseParams):
    """
    Parameters for the get_vector_incident_tile method.
    """

    t: str | None = None
    tags: list[str] | None = None
    language: Language | None = None
