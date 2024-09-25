"""Junction Analytics API."""

from typing import Self

from ..api import BaseApi


class JunctionAnalyticsApi(BaseApi):
    """Junction Analytics API.

    Our Junction Analytics API provides input for efficient signal operations that makes it possible to allocate green time in a better way and
    reduce traffic delay. This service is designed for traffic signal hardware and software vendors who want to optimize signal operations and
    optimize traffic flows at intersections.

    For more information, see: https://developer.tomtom.com/junction-analytics/documentation/product-information/introduction
    """

    def __init__(self: Self) -> None:  # pylint: disable=super-init-not-called
        """Not implemented.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError
