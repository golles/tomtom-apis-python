"""EV Search test."""

from collections.abc import AsyncGenerator

import pytest
from aresponses import ResponsesMockServer

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import LatLon
from tomtom_apis.places import BatchSearchApi
from tomtom_apis.places.models import AsynchronousBatchDownloadParams, BatchItem, BatchPostData, BatchResponse, Geometry, Route


@pytest.fixture(name="batch_search_api")
async def fixture_batch_search_api() -> AsyncGenerator[BatchSearchApi]:
    """Fixture for BatchSearchApi."""
    options = ApiOptions(api_key=API_KEY)
    async with BatchSearchApi(options) as batch_search:
        yield batch_search


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/batch_search/post_synchronous_batch.json"], indirect=True)
async def test_deserialization_post_synchronous_batch(batch_search_api: BatchSearchApi) -> None:
    """Test the post_synchronous_batch method."""
    response = await batch_search_api.post_synchronous_batch(
        data=BatchPostData(
            batchItems=[
                BatchItem(query="/search/lodz.json?limit=10&idxSet=POI,PAD,Str,Xstr,Geo,Addr"),
                BatchItem(query="/search/wroclaw.json?limit=10&idxSet=POI,PAD,Str,Xstr,Geo,Addr"),
                BatchItem(query="/search/berlin.json?limit=10&idxSet=POI,PAD,Str,Xstr,Geo,Addr"),
            ],
        )
    )

    assert response
    assert isinstance(response, BatchResponse)


async def test_post_asynchronous_batch_submission(batch_search_api: BatchSearchApi, aresponses: ResponsesMockServer) -> None:
    """Test the post_asynchronous_batch_submission method."""
    aresponses.add(
        response=aresponses.Response(
            status=202,
            headers={"Location": "check-this-out"},
        ),
    )

    response = await batch_search_api.post_asynchronous_batch_submission(
        data=BatchPostData(
            batchItems=[
                BatchItem(query="/poiSearch/rembrandt museum.json"),
                BatchItem(query='/geometrySearch/parking.json?geometryList=[{"type":"CIRCLE","position":"51.5123443,-0.0909851","radius":1000}]'),
                BatchItem(
                    query="/geometrySearch/pizza.json",
                    post=[Geometry(type="CIRCLE", position="51.5123443,-0.0909851", radius=1000)],
                ),
                BatchItem(
                    query="/searchAlongRoute/restaurant.json?maxDetourTime=300",
                    post=[
                        Route(
                            points=[
                                LatLon(lat=37.7524152, lon=-122.4357604),
                                LatLon(lat=37.7066047, lon=-122.4330139),
                                LatLon(lat=37.7120598, lon=-122.3643493),
                                LatLon(lat=37.7535056, lon=-122.3739624),
                            ]
                        )
                    ],
                ),
                BatchItem(query="/reverseGeocode/crossStreet/52.4829893,4.9247074.json"),
                BatchItem(query="/search/lodz.json?limit=10&idxSet=POI,PAD,Str,Xstr,Geo,Addr&maxFuzzyLevel=2"),
            ],
        )
    )

    assert response == "check-this-out"
    assert isinstance(response, str)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/batch_search/get_asynchronous_batch_download.json"], indirect=True)
async def test_deserialization_get_asynchronous_batch_download(batch_search_api: BatchSearchApi) -> None:
    """Test the get_asynchronous_batch_download method."""
    response = await batch_search_api.get_asynchronous_batch_download(
        batch_id="45e0909c-625a-4822-a060-8f7f88498c0e",
        params=AsynchronousBatchDownloadParams(
            waitTimeSeconds=10,
        ),
    )

    assert response
    assert isinstance(response, BatchResponse)
