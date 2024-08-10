"""Geofencing API"""

from tomtom_api.api import BaseApi


class GeofencingApi(BaseApi):
    """
    TomTom's Geofencing API service is intended to define virtual barriers on real geographical locations. Together with the location of an object, you can determine whether that object is located within, outside, or close to a predefined geographical area.

    See: https://developer.tomtom.com/geofencing-api/documentation/product-information/introduction
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError
