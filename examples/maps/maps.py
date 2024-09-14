"""Examples of some maps API calls."""

# pylint: disable=duplicate-code

import asyncio
import os

from tomtom_apis import ApiOptions
from tomtom_apis.maps.map_display import MapDisplayApi


async def map_copyrights(api_key: str) -> None:
    """Example for map_copyrights."""
    async with MapDisplayApi(ApiOptions(api_key=api_key, gzip_compression=True, tracking_id=True)) as map_display_api:
        response = await map_display_api.get_map_copyrights()

        print(f"\nMap copyrights: \n{response}")


async def get_map_service_copyrights(api_key: str) -> None:
    """Example for get_map_service_copyrights."""
    async with MapDisplayApi(ApiOptions(api_key=api_key, gzip_compression=True, tracking_id=True)) as map_display_api:
        response = await map_display_api.get_map_service_copyrights()

        print(f"\nMap service copyrights: \n{response}")


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()

    asyncio.run(map_copyrights(user_api_key))
    asyncio.run(get_map_service_copyrights(user_api_key))
