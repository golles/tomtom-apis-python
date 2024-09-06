"""Location History API"""

from ..api import BaseApi


class LocationHistoryApi(BaseApi):
    """
    TomTom's Location History API is intended to keep track and manage the locations of multiple objects. It can share data with TomTom's Geofencing
    service to enhance it with the history of object transitions through fence borders.

    See: https://developer.tomtom.com/location-history-api/documentation/product-information/introduction
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError
