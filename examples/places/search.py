"""Examples of search API calls."""

# pylint: disable=duplicate-code

import asyncio
import os

from tomtom_apis import ApiOptions
from tomtom_apis.models import ViewType
from tomtom_apis.places import SearchApi
from tomtom_apis.places.models import Geometry, GeometrySearchParams, GeometrySearchPostData, NearbySearchParams, PlaceByIdParams, RelatedPoisType


async def get_place_by_id(api_key: str) -> None:
    """Example for get_place_by_id."""
    search_id = "528009004256119"
    async with SearchApi(ApiOptions(api_key=api_key)) as search_api:
        response = await search_api.get_place_by_id(params=PlaceByIdParams(entityId=search_id))

        if response.results and response.results[0].poi is not None:
            print(f"\nPlace by id: '{search_id}' = {response.results[0].poi.name}")
        else:
            print(f"No POI data found for place id: {search_id}")


async def get_nearby_search(api_key: str) -> None:
    """Example for get_nearby_search."""
    async with SearchApi(ApiOptions(api_key=api_key)) as search_api:
        radius = 10000
        response = await search_api.get_nearby_search(
            lat=29.7604,
            lon=-95.3698,
            params=NearbySearchParams(
                radius=radius,
                brandSet=["McDonald's"],
            ),
        )

        print(f"\nThere are {response.summary.totalResults} McDonald's restaurants in a {radius} meter radius of the centre of Houston")


async def post_geometry_search(api_key: str) -> None:
    """Example for post_geometry_search."""
    async with SearchApi(ApiOptions(api_key=api_key)) as search_api:
        response = await search_api.post_geometry_search(
            query="pizza",
            params=GeometrySearchParams(
                categorySet=["7315"],
                view=ViewType.UNIFIED,
                relatedPois=RelatedPoisType.OFF,
            ),
            data=GeometrySearchPostData(
                geometryList=[
                    Geometry(
                        type="POLYGON",
                        vertices=[
                            "37.7524152343544, -122.43576049804686",
                            "37.70660472542312, -122.43301391601562",
                            "37.712059855877314, -122.36434936523438",
                            "37.75350561243041, -122.37396240234374",
                        ],
                    ),
                    Geometry(
                        type="CIRCLE",
                        position="37.71205, -121.36434",
                        radius=6000,
                    ),
                    Geometry(
                        type="CIRCLE",
                        position="37.31205, -121.36434",
                        radius=1000,
                    ),
                ]
            ),
        )

        print(f"\nThere are {response.summary.totalResults} pizza restaurants in the given geometries")


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()

    asyncio.run(get_place_by_id(user_api_key))
    asyncio.run(get_nearby_search(user_api_key))
    asyncio.run(post_geometry_search(user_api_key))
