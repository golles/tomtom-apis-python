"""Junction Analytics API"""

from tomtom_api.api import BaseApi


class JunctionAnalyticsApi(BaseApi):
    """
    Our Junction Analytics API provides input for efficient signal operations that makes it possible to allocate green time in a better way and reduce traffic delay. This service is designed for traffic signal hardware and software vendors who want to optimize signal operations and optimize traffic flows at intersections.

    See: https://developer.tomtom.com/junction-analytics/documentation/product-information/introduction
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError
