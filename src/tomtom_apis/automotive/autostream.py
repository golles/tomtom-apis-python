"""Auto Stream API."""

from typing import Self

from ..api import BaseApi


class AutoStreamApi(BaseApi):
    """AutoStream API.

    AutoStream is a map data delivery platform, optimized for on-demand and over-the-air cloud-to-device and cloud-to-cloud data streaming.

    For more information, see: https://developer.tomtom.com/autostream-sdk/documentation/product-information/introduction
    """

    def __init__(self: Self) -> None:  # pylint: disable=super-init-not-called
        """Not implemented.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError

    # There are no methods defined on the developer portal.
