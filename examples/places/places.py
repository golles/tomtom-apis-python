"""Exampels of some places API calls."""

# pylint: disable=duplicate-code

import asyncio
import os

from tomtom_api import ApiOptions
from tomtom_api.models import Language, LatLon
from tomtom_api.places import GeocodingApi, ReverseGeocodingApi, SearchApi
from tomtom_api.places.models import PlaceByIdParams, ReverseGeocodeParams


async def get_place_by_id(api_key: str) -> None:
    """Example for get_place_by_id"""
    search_id = "528009004256119"
    async with SearchApi(ApiOptions(api_key=api_key)) as search_api:
        response = await search_api.get_place_by_id(params=PlaceByIdParams(entityId=search_id))

        print(f"\nPlace by id: '{search_id}' = {response.results[0].poi.name}")


async def get_geocode(api_key: str) -> None:
    """Example for get_geocode"""
    query = "De Ruijterkade 154 Amsterdam"
    async with GeocodingApi(ApiOptions(api_key=api_key)) as geo_coding_api:
        response = await geo_coding_api.get_geocode(query=query)

        print(f"\nGeocode for '{query}' = {response.results[0].type} @ {response.results[0].position.lat},{response.results[0].position.lon}")


async def get_reverse_geocode(api_key: str) -> None:
    """Example for get_reverse_geocode"""
    position = LatLon(lat=48.858093, lon=2.294694)
    async with ReverseGeocodingApi(ApiOptions(api_key=api_key)) as geo_coding_api:
        response = await geo_coding_api.get_reverse_geocode(
            position=position,
            params=ReverseGeocodeParams(language=Language.EN_GB),
        )

        print(f"\nReverse geocode for '{position}' = {response.addresses[0].address.freeformAddress}")


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()

    asyncio.run(get_place_by_id(user_api_key))
    asyncio.run(get_geocode(user_api_key))
    asyncio.run(get_reverse_geocode(user_api_key))
