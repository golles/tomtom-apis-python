"""Exceptions for the TomTom API."""


class TomTomAPIError(Exception):
    """Base exception for all errors raised by the TomTom SDK."""


class TomTomAPIClientError(TomTomAPIError):
    """Exception raised for client-side errors (4xx)."""


class TomTomAPIServerError(TomTomAPIError):
    """Exception raised for server-side errors (5xx)."""


class TomTomAPIConnectionError(TomTomAPIError):
    """Exception raised for connection errors."""


class TomTomAPIRequestTimeoutError(TomTomAPIError):
    """Exception raised for request timeouts."""


class RangeExceptionError(Exception):
    """Exception raised when a value is out of range."""

    def __init__(self, field: str, min_number: float, max_number: float) -> None:
        """Initialize the RangeExceptionError."""
        super().__init__(f"{field} value is out of range [{min_number}, {max_number}]")


class MutualExclusiveParamsError(Exception):
    """Exception raised when mutually exclusive parameters are provided."""

    def __init__(self, params: list[str]) -> None:
        """Initialize the MutualExclusiveParamsError."""
        super().__init__(f"Mutually exclusive parameters provided: {', '.join(params)}")
