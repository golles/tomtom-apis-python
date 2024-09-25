"""Geofencing API."""

from typing import Self

from ..api import BaseApi


class GeofencingApi(BaseApi):
    """Geofencing API.

    TomTom's Geofencing API service is intended to define virtual barriers on real geographical locations. Together with the location of an object,
    you can determine whether that object is located within, outside, or close to a predefined geographical area.

    For more information, see: https://developer.tomtom.com/geofencing-api/documentation/product-information/introduction
    """

    def __init__(self: Self) -> None:  # pylint: disable=super-init-not-called
        """Not implemented.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError
