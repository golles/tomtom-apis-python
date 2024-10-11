"""EV Search API."""

from typing import Self

from ..api import BaseApi
from .models import (
    EVChargingStationsAvailabilityParams,
    EVChargingStationsAvailabilityResponse,
    EvSearchByIdParams,
    EvSearchNearbyParams,
    SearchResponse,
)


class EVSearchApi(BaseApi):
    """EV Search API.

    EV Search is a REST API limited to and optimized for electric vehicle station POI category. It provides complete EV POI data including static
    location information (lat/long), address, opening hours, access restrictions, technical specs of the charging station (connector type, voltage,
    power, current, current type), etc. as well as dynamic availability status. Wide range of EV specific filters (including dynamic availability)
    allows for narrowing the search results to match the personal preference (like charging power or access type) of the driver or the technical
    specification of the electric vehicle (connector type).

    For more information, see: https://developer.tomtom.com/ev-search-api/documentation/product-information/introduction
    """

    async def get_ev_search_nearby(
        self: Self,
        *,
        params: EvSearchNearbyParams | None = None,
    ) -> SearchResponse:
        """Get EV search nearby.

        For more information, see: https://developer.tomtom.com/ev-search-api/documentation/ev-search-api/ev-search-nearby

        Args:
            params (EvSearchNearbyParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint="/search/2/evsearch",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def get_ev_search_by_id(
        self: Self,
        *,
        params: EvSearchByIdParams | None = None,
    ) -> SearchResponse:
        """Get EV search by id.

        For more information, see: https://developer.tomtom.com/ev-search-api/documentation/ev-search-api/ev-search-by-id

        Args:
            params (EvSearchByIdParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint="/search/2/evbyid",
            params=params,
        )

        return await response.deserialize(SearchResponse)

    async def get_ev_charging_stations_availability(
        self: Self,
        *,
        chargingAvailability: str,
        params: EVChargingStationsAvailabilityParams | None = None,
    ) -> EVChargingStationsAvailabilityResponse:
        """Get EV Charging Stations Availability.

        For more information, see: https://developer.tomtom.com/ev-charging-stations-availability-api/documentation/ev-charging-stations-availability-api/ev-charging-stations-availability  # pylint: disable=line-too-long

        Args:
            chargingAvailability (str): The chargingAvailability ID, previously retrieved from a Search request.
            params (EVChargingStationsAvailabilityParams | None, optional): Additional parameters for the request. Defaults to None.

        Returns:
            SearchResponse: Response containing search results.
        """
        response = await self.get(
            endpoint=f"/search/2/chargingAvailability.json?chargingAvailability={chargingAvailability}",
            params=params,
        )

        return await response.deserialize(EVChargingStationsAvailabilityResponse)
