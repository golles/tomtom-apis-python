"""Batch Search API."""

from typing import Self

from ..api import BaseApi, BaseParams
from ..places.models import (
    AsynchronousBatchDownloadParams,
    AsynchronousSynchronousBatchParams,
    BatchPostData,
    BatchResponse,
)


class BatchSearchApi(BaseApi):
    """Batch Search API.

    Batch Search sends batches of requests to supported endpoints with ease. You can call Batch Search APIs to run either asynchronously or
    synchronously. The Batch Search service consists of the following endpoints:

    For more information, see: https://developer.tomtom.com/batch-search-api/documentation/product-information/introduction
    """

    async def post_synchronous_batch(
        self: Self,
        *,
        params: BaseParams | None = None,  # No extra params.
        data: BatchPostData,
    ) -> BatchResponse:
        """Post synchronous batch.

        For more information, see: https://developer.tomtom.com/batch-search-api/documentation/synchronous-batch

        Args:
            params (BaseParams, optional): Query parameters for the request. Defaults to None.
            data (BatchPostData): Data for the batch request.

        Returns:
            BatchResponse: The response object for the synchronous batch request.
        """
        response = await self.post(
            endpoint="/search/2/batch/sync.json",
            params=params,
            data=data,
        )

        return await response.deserialize(BatchResponse)

    async def post_asynchronous_batch_submission(
        self: Self,
        *,
        params: AsynchronousSynchronousBatchParams | None = None,
        data: BatchPostData,
    ) -> str | None:
        """Post Asynchronous Batch Submission.

        For more information, see: https://developer.tomtom.com/batch-search-api/documentation/asynchronous-batch-submission

        Args:
            params (AsynchronousSynchronousBatchParams, optional): Query parameters for the request. Defaults to None.
            data (BatchPostData): Data for the batch request.

        Returns:
            str | None: The 'Location' header from the response, if available, otherwise None.
        """
        response = await self.post(
            endpoint="/search/2/batch.json",
            params=params,
            data=data,
        )

        return response.headers.get("Location", None)

    async def get_asynchronous_batch_download(
        self: Self,
        *,
        batch_id: str,
        params: AsynchronousBatchDownloadParams | None = None,
    ) -> BatchResponse:
        """Fetches the result of an asynchronous batch download.

        For more information, see: https://developer.tomtom.com/batch-search-api/documentation/asynchronous-batch-download

        Args:
            batch_id (str): The ID of the batch to download.
            params (AsynchronousBatchDownloadParams, optional): Optional parameters for the download request. Defaults to None.

        Returns:
            BatchResponse: The response object representing the downloaded batch.
        """
        response = await self.get(
            endpoint=f"/search/2/batch/{batch_id}",
            params=params,
        )

        return await response.deserialize(BatchResponse)
