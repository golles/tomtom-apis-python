"""Intermediate Traffic API."""

from typing import Self

from ..api import BaseApi


class IntermediateTrafficApi(BaseApi):
    """Intermediate Traffic API.

    The mission of TomTom is helping our customers arrive at their destinations faster, more safely and more reliably, regardless of their locations.
    We developed TomTom Intermediate Traffic to deliver detailed, real-time traffic content to business customers who integrate it into their own
    applications. Target customers for TomTom Intermediate Traffic include automotive OEMs, web and application developers, and governments. We
    deliver bulk traffic flow information that provides a comprehensive view of the entire road network.

    For more information, see: https://developer.tomtom.com/intermediate-traffic-service/documentation/product-information/introduction
    """

    def __init__(self: Self) -> None:  # pylint: disable=super-init-not-called
        """Not implemented.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError
