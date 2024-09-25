"""O/D Analysis API."""

from typing import Self

from ..api import BaseApi


class ODAnalysisApi(BaseApi):
    """O/D Analysis API.

    O/D Analysis is a suite of web services designed for developers to create web applications which analyze historical traffic data. These web
    services are RESTful APIs. The O/D Analysis API services are based on the collection of Floating Car Data (FCD), which is a proven and innovative
    method of measuring what is happening on the road.

    For more information, see: https://developer.tomtom.com/od-analysis/documentation/product-information/introduction
    """

    def __init__(self: Self) -> None:  # pylint: disable=super-init-not-called
        """Not implemented.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError
