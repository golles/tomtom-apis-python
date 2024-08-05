"""Snap to Roads API"""

from tomtom_api.api import BaseApi


class SnapToRoadsApi(BaseApi):
    """
    The TomTom Snap to Roads API and service offers a solution to enable you to get the most out of your applications, and grants you the ability to use advanced map data. It is a web service designed for developers to create web and mobile applications responsible for matching received points (gathered from GPS devices) to map a road network and reconstruct the road driven by a customer, and provides detailed information about the matched route. These web services can be used via REST APIs.

    See: https://developer.tomtom.com/snap-to-roads-api/documentation/product-information/introduction
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError
