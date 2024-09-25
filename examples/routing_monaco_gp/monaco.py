"""Monaco GP routing example."""

# pylint: disable=duplicate-code

import asyncio
import os

from tomtom_apis import ApiOptions
from tomtom_apis.models import LatLon, LatLonList, TravelModeType
from tomtom_apis.routing import RoutingApi
from tomtom_apis.routing.models import CalculateRouteParams, RouteType


async def plan_monaco_gp_route(api_key: str) -> None:
    """Plan Monaco GP route."""
    options = ApiOptions(api_key=api_key)
    async with RoutingApi(options) as routing_api:
        response = await routing_api.get_calculate_route(
            locations=LatLonList(
                locations=[
                    LatLon(lat=43.735053716368, lon=7.4212753772736),
                    LatLon(lat=43.736654495285, lon=7.4214953184128),
                    LatLon(lat=43.737361847639, lon=7.4241694808006),
                    LatLon(lat=43.737974233613, lon=7.4272459745407),
                    LatLon(lat=43.739218365576, lon=7.4273908138275),
                    LatLon(lat=43.740999250921, lon=7.4286353588104),
                    LatLon(lat=43.740235743995, lon=7.4295258522034),
                    LatLon(lat=43.740819033159, lon=7.4293032288551),
                    LatLon(lat=43.741088390688, lon=7.4302071332932),
                    LatLon(lat=43.740410149989, lon=7.4303358793259),
                    LatLon(lat=43.737226191671, lon=7.4255266785622),
                    LatLon(lat=43.736790152549, lon=7.4223375320435),
                    LatLon(lat=43.735567288116, lon=7.4218171834946),
                    LatLon(lat=43.73259432495, lon=7.4234801530838),
                    LatLon(lat=43.732390824682, lon=7.4230295419693),
                    LatLon(lat=43.73454595431, lon=7.4213665723801),
                ]
            ),
            params=CalculateRouteParams(
                maxAlternatives=0,
                routeType=RouteType.FASTEST,
                travelMode=TravelModeType.CAR,
            ),
        )

        # Monaco GP route statistics, source: https://en.wikipedia.org/wiki/Circuit_de_Monaco
        official_track_length = 3337
        lap_record_time = "1:12.909"
        lap_record_seconds = 73
        public_route_length = response.routes[0].summary.lengthInMeters
        driving_time_seconds = response.routes[0].summary.travelTimeInSeconds

        # Format driving time into minutes and seconds
        driving_time_minutes = driving_time_seconds // 60
        driving_time_remaining_seconds = driving_time_seconds % 60

        # Enhanced output
        print("=== Monaco Grand Prix Route Stats ===\n")
        print(f"🏁 Official F1 Track Length:  {official_track_length:,} meters")
        print(f"🚗 Street Driving Length:     {public_route_length:,} meters")
        print(
            f"⏱️  Estimated Driving Time:    {int(driving_time_minutes)} minutes {int(driving_time_remaining_seconds)}"
            f"seconds ({driving_time_seconds:,} seconds)"
        )
        print(f"🏎️  F1 Lap Record:             {lap_record_time} ({lap_record_seconds} seconds)\n")
        print("Can you beat the record? Give it a try and see how close you can get!")


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()
    asyncio.run(plan_monaco_gp_route(api_key=user_api_key))
