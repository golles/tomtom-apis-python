"""Traffic Stats API"""

from ..api import BaseApi


class TrafficStatsApi(BaseApi):
    """
    Traffic Stats is a suite of web services designed for developers to create web applications which analyse historical traffic data. These web
    services are RESTful APIs. The Traffic Stats APIs are based on the collection of Floating Car Data (FCD), which is a proven and innovative method
    of measuring what is happening on the road.

    See: https://developer.tomtom.com/traffic-stats/documentation/product-information/introduction
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError
