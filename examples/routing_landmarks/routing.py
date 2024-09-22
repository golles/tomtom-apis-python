"""Landmark routing example."""

# pylint: disable=duplicate-code

import asyncio
import itertools
import os

from attr import dataclass

from tomtom_apis import ApiOptions
from tomtom_apis.models import LatLon, LatLonList, TravelModeType
from tomtom_apis.routing import RoutingApi
from tomtom_apis.routing.models import CalculateRouteParams, RouteType


@dataclass(kw_only=True)
class Landmark:
    """Representation of a landmark location."""

    name: str
    location: LatLon


# Top 5 US landmarks, according to ChatGPT.
LANDMARKS: list[Landmark] = [
    Landmark(name="Statue of Liberty", location=LatLon(lat=40.6892, lon=-74.0445)),
    Landmark(name="Grand Canyon", location=LatLon(lat=36.1069, lon=-112.1129)),
    Landmark(name="Mount Rushmore National Memorial", location=LatLon(lat=43.8791, lon=-103.4591)),
    Landmark(name="Golden Gate Bridge", location=LatLon(lat=37.8199, lon=-122.4783)),
    Landmark(name="Times Square", location=LatLon(lat=40.7580, lon=-73.9855)),
]


def meters_to_km(meters: int) -> int:
    """Helper function for outputting kilometers."""
    kilometers = meters // 1000
    return int(kilometers)


def seconds_to_minutes(seconds: int) -> int:
    """Helper function for outputting minutes."""
    minutes = round(seconds / 60)
    return int(minutes)


def seconds_to_hours_minutes(seconds: int) -> str:
    """Helper function for outputting travel time."""
    total_minutes = round(seconds / 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} hours {minutes} minutes"


async def plan_route(routing_api: RoutingApi, start: Landmark, destination: Landmark) -> None:
    """Plan a route from one landmark to another."""
    print(f"\nPlanning a route from {start.name} to {destination.name}:")

    response = await routing_api.get_calculate_route(
        locations=LatLonList(locations=[start.location, destination.location]),
        params=CalculateRouteParams(
            maxAlternatives=0,
            routeType=RouteType.FASTEST,
            traffic=True,
            travelMode=TravelModeType.CAR,
        ),
    )

    length = response.routes[0].summary.lengthInMeters
    time = response.routes[0].summary.travelTimeInSeconds
    traffic_time = response.routes[0].summary.trafficDelayInSeconds

    print(f"{meters_to_km(length)}km with a travel time {seconds_to_hours_minutes(time)}, currently {seconds_to_minutes(traffic_time)} minutes delay")


async def routes(api_key: str) -> None:
    """Generate all unique combinations of 2 landmarks and plan a route between them."""
    route_combinations = list(itertools.combinations(LANDMARKS, 2))

    options = ApiOptions(api_key=api_key)
    async with RoutingApi(options) as routing_api:
        for combination in route_combinations:
            await plan_route(routing_api, combination[0], combination[1])


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()
    asyncio.run(routes(user_api_key))
