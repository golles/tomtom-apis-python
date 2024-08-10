"""Route Monitoring API"""

from tomtom_api.api import BaseApi


class RouteMonitoringApi(BaseApi):
    """
    The TomTom Route Monitoring API service provides an intuitive and powerful way to monitor strategic routes in real-time. Customers have the ability to pre-define routes important to their businesses getting detailed information on current travel time, current delay time and percentage delay, route distance, live data coverage, and data confidence level. The overall route information can also be checked on a segment level, providing accurate and detailed information of traffic flow dynamics down to short length extensions.

    See: https://developer.tomtom.com/route-monitoring/documentation/product-information/introduction
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError

    # There are no methods defined on the developer portal.
