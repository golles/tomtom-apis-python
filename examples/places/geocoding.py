"""Examples of geocoding API calls."""

# pylint: disable=duplicate-code

import asyncio
import os

from tomtom_apis import ApiOptions
from tomtom_apis.places import GeocodingApi


async def get_geocode(api_key: str) -> None:
    """Example for get_geocode."""
    query = "De Ruijterkade 154 Amsterdam"
    async with GeocodingApi(ApiOptions(api_key=api_key)) as geo_coding_api:
        response = await geo_coding_api.get_geocode(query=query)

        print(f"\nGeocode for '{query}' = {response.results[0].type} @ {response.results[0].position.lat},{response.results[0].position.lon}")


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()

    asyncio.run(get_geocode(user_api_key))
