"""Constants for testing."""

from tomtom_apis.models import LatLon

API_KEY: str = "abcdef123456"
DEFAULT_HEADERS: dict[str, str] = {"Content-Type": "application/json", "User-Agent": "TomTomApiPython/0.0.0"}

LOC_AMSTERDAM: LatLon = LatLon(lat=52.377956, lon=4.897070)
LOC_ROTTERDAM: LatLon = LatLon(lat=51.926517, lon=4.462456)
