"""Auto Stream API"""

from ..api import BaseApi


class AutoStreamApi(BaseApi):
    """
    AutoStream is a map data delivery platform, optimized for on-demand and over-the-air cloud-to-device and cloud-to-cloud data streaming.

    In general, AutoStream only takes in and delivers data already present in the respective source. In other words, AutoStream does not add or
    create any new map features or attributes but prepares the data for its hosting and delivery. By structuring the data into a special tile and
    layering format AutoStream allows the minimizing of cellular data consumption and works with a download-only-what-is-needed principle.

    Essentially, this means the application consuming the map via AutoStream is in full control as to which map data is requested and when;
    AutoStream does not proactively send any data.

    See: https://developer.tomtom.com/autostream-sdk/documentation/product-information/introduction
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError

    # There are no methods defined on the developer portal.
