"""Parking Availability API."""

from typing import Self

from ..api import BaseApi
from ..automotive.models import ParkingAvailabilityParams, ParkingAvailabilityResponse


class ParkingAvailabilityApi(BaseApi):
    """Parking Availability API.

    For more information, see: https://developer.tomtom.com/parking-availability-api/documentation/product-information/introduction
    """

    async def get_parking_availability(
        self: Self,
        *,
        params: ParkingAvailabilityParams | None = None,
    ) -> ParkingAvailabilityResponse:
        """Get parking availability.

        For more information, see: https://developer.tomtom.com/parking-availability-api/documentation/parking-availability-api/parking-availability

        Args:
            params (ParkingAvailabilityParams | None, optional): Additional parameters for the parking availability. Defaults to None.

        Returns:
            ParkingAvailabilityResponse: Response containing parking availability data.
        """
        response = await self.get(
            endpoint="/search/2/parkingAvailability.json",
            params=params,
        )

        return await response.deserialize(ParkingAvailabilityResponse)
