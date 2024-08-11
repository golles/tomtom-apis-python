"""EV Search test"""

import pytest
from aresponses import ResponsesMockServer

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import LatLon
from tomtom_apis.places import BatchSearchApi
from tomtom_apis.places.models import AsynchronousBatchDownloadParams, BatchItem, BatchPostData, Geometry, Route


@pytest.fixture(name="batch_search_api")
async def fixture_batch_search_api():
    """Fixture for BatchSearchApi"""
    options = ApiOptions(api_key=API_KEY)
    async with BatchSearchApi(options) as batch_search_api:
        yield batch_search_api


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/batch_search/post_synchronous_batch.json"], indirect=True)
async def test_deserialization_post_synchronous_batch(batch_search_api: BatchSearchApi):
    """Test the post_synchronous_batch method"""

    response = await batch_search_api.post_synchronous_batch(
        data=BatchPostData(
            batchItems=[
                BatchItem(query="/search/lodz.json?limit=10&idxSet=POI,PAD,Str,Xstr,Geo,Addr"),
                BatchItem(query="/search/wroclaw.json?limit=10&idxSet=POI,PAD,Str,Xstr,Geo,Addr"),
                BatchItem(query="/search/berlin.json?limit=10&idxSet=POI,PAD,Str,Xstr,Geo,Addr"),
            ],
        )
    )

    await batch_search_api.close()

    assert response


async def test_post_asynchronous_synchronous_batch(batch_search_api: BatchSearchApi, aresponses: ResponsesMockServer):
    """Test the post_asynchronous_synchronous_batch method"""
    aresponses.add(
        response=aresponses.Response(
            status=202,
            headers={"Location": "check-this-out"},
        ),
    )

    response = await batch_search_api.post_asynchronous_synchronous_batch(
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

    await batch_search_api.close()

    assert response == "check-this-out"


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/batch_search/get_asynchronous_batch_download.json"], indirect=True)
async def test_deserialization_get_asynchronous_batch_download(batch_search_api: BatchSearchApi):
    """Test the get_asynchronous_batch_download method"""
    response = await batch_search_api.get_asynchronous_batch_download(
        batch_id="45e0909c-625a-4822-a060-8f7f88498c0e",
        params=AsynchronousBatchDownloadParams(
            waitTimeSeconds=10,
        ),
    )

    await batch_search_api.close()

    assert response
