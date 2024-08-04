"""Exceptions for the TomTom API."""


class TomTomAPIError(Exception):
    """Base exception for all errors raised by the TomTom SDK."""


class TomTomAPIClientError(TomTomAPIError):
    """Exception raised for client-side errors (4xx)."""


class TomTomAPIServerError(TomTomAPIError):
    """Exception raised for server-side errors (5xx)."""


class TomTomAPIConnectionError(TomTomAPIError):
    """Exception raised for connection errors."""


class TomTomAPIRequestTimeout(TomTomAPIError):
    """Exception raised for request timeouts."""
