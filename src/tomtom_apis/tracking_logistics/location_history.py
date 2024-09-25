"""Location History API."""

from typing import Self

from ..api import BaseApi


class LocationHistoryApi(BaseApi):
    """Location History API.

    TomTom's Location History API is intended to keep track and manage the locations of multiple objects. It can share data with TomTom's Geofencing
    service to enhance it with the history of object transitions through fence borders.

    For more information, see: https://developer.tomtom.com/location-history-api/documentation/product-information/introduction
    """

    def __init__(self: Self) -> None:  # pylint: disable=super-init-not-called
        """Not implemented.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError
