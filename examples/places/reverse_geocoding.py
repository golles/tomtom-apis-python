"""Examples of reverse geocoding API calls."""

# pylint: disable=duplicate-code

import asyncio
import os

from tomtom_apis import ApiOptions
from tomtom_apis.models import Language, LatLon
from tomtom_apis.places import ReverseGeocodingApi
from tomtom_apis.places.models import ReverseGeocodeParams


async def get_reverse_geocode(api_key: str) -> None:
    """Example for get_reverse_geocode."""
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

    asyncio.run(get_reverse_geocode(user_api_key))
