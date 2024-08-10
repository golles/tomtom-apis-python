"""Parking Availability AP"""

from tomtom_api.api import BaseApi
from tomtom_api.automotive.models import ParkingAvailabilityParams, ParkingAvailabilityResponse


class ParkingAvailabilityApi(BaseApi):
    """
    The Parking Availability API provides information about the current availability status of parking sites. The data is refreshed every 10 minutes and is therefore close to real time. Using this API makes it possible to make better off-street parking decisions based on actual parking availability (including the number of free spaces).

    See: https://developer.tomtom.com/parking-availability-api/documentation/product-information/introduction
    """

    async def get_parking_availability(
        self,
        *,
        params: ParkingAvailabilityParams | None = None,
    ) -> ParkingAvailabilityResponse:
        """
        The Parking Availability service provides information about the current availability status of parking sites.

        See: https://developer.tomtom.com/parking-availability-api/documentation/parking-availability-api/parking-availability
        """

        reponse = await self.get(
            endpoint="/search/2/parkingAvailability.json",
            params=params,
        )

        return await reponse.deserialize(ParkingAvailabilityResponse)
