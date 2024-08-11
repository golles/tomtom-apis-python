"""Matrix Routing V2 API"""

from ..api import BaseApi


class MatrixRoutingApiV2(BaseApi):
    """
    The Matrix Routing v2 API allows clients to calculate a matrix of route summaries for a set of routes defined with origin and destination locations. For every given origin, this service calculates the cost of routing from that origin to every given destination. The set of origins and the set of destinations can be thought of as the column and row headers of a table, while each cell in the table contains the costs of routing from the origin to the destination for that cell.

    See: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/matrix-routing-v2/matrix-routing-v2-service
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        raise NotImplementedError