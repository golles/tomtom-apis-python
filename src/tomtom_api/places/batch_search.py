"""Batch Search API"""

from tomtom_api.api import BaseApi, BaseParams
from tomtom_api.places.models import (
    AsynchronousBatchDownloadParams,
    AsynchronousSynchronousBatchParams,
    BatchPostData,
    BatchResponse,
)


class BatchSearchApi(BaseApi):
    """
    Batch Search sends batches of requests to supported endpoints with ease. You can call Batch Search APIs to run either asynchronously or synchronously. The Batch Search service consists of the following endpoints:

    See: https://developer.tomtom.com/batch-search-api/documentation/product-information/introduction
    """

    async def post_synchronous_batch(
        self,
        *,
        params: BaseParams | None = None,  # No extra params.
        data: BatchPostData,
    ) -> BatchResponse:
        """
        This endpoint allows the submission of a new batch for synchronous processing. It responds with a batch processing result or an HTTP 408 request timeout error, if the processing time exceeds 60 seconds.

        See: https://developer.tomtom.com/batch-search-api/documentation/synchronous-batch
        """

        reponse = await self.post(
            endpoint="/search/2/batch/sync.json",
            params=params,
            data=data,
        )

        return await reponse.deserialize(BatchResponse)

    async def post_asynchronous_synchronous_batch(
        self,
        *,
        params: AsynchronousSynchronousBatchParams | None = None,
        data: BatchPostData,
    ) -> dict:
        """
        This endpoint allows the submission of a new batch for asynchronous processing. It responds with a redirect to the location at which the batch results can be obtained when the batch processing has completed.

        See: https://developer.tomtom.com/batch-search-api/documentation/asynchronous-batch-submission
        """

        reponse = await self.post(
            endpoint="/search/2/batch.json",
            params=params,
            data=data,
        )

        return await reponse.dict()

    async def get_asynchronous_batch_download(
        self,
        *,
        batch_id: str,
        params: AsynchronousBatchDownloadParams | None = None,
    ) -> BatchResponse:
        """
        This endpoint fetches results of the Asynchronous Batch processing. It responds with HTTP 200 and the batch results assuming batch processing has completed, or HTTP 202 Accepted if the batch is still being processed. HTTP 202 "Accepted" will be sent after 120 seconds by default. This behavior can be overridden as needed by passing the waitTimeSeconds parameter with a desired value. The client should then retry the request by following the Location header.

        See: https://developer.tomtom.com/batch-search-api/documentation/asynchronous-batch-download
        """

        reponse = await self.get(
            endpoint=f"/search/2/batch/{batch_id}",
            params=params,
        )

        return await reponse.deserialize(BatchResponse)
