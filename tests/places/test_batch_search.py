"""EV Search test"""

import pytest

from tests.const import API_KEY
from tomtom_api.api import ApiOptions
from tomtom_api.places import BatchSearchApi
from tomtom_api.places.models import AsynchronousBatchDownloadParams, BatchItem, BatchPostData


@pytest.fixture(name="batch_search_api")
async def fixture_batch_search_api():
    """Fixture for BatchSearchApi."""
    options = ApiOptions(api_key=API_KEY)
    async with BatchSearchApi(options) as batch_search_api:
        yield batch_search_api


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/batch_search/post_synchronous_batch.json"], indirect=True)
async def test_deserialization_post_synchronous_batch(batch_search_api: BatchSearchApi):
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

    await batch_search_api.close()

    assert response


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/batch_search/get_asynchronous_batch_download.json"], indirect=True)
async def test_deserialization_get_asynchronous_batch_download(batch_search_api: BatchSearchApi):
    """Test the get_asynchronous_batch_download method."""
    response = await batch_search_api.get_asynchronous_batch_download(
        batch_id="45e0909c-625a-4822-a060-8f7f88498c0e",
        params=AsynchronousBatchDownloadParams(
            waitTimeSeconds=10,
        ),
    )

    await batch_search_api.close()

    assert response
