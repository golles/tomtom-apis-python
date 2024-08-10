"""Client for the TomTom API"""

from __future__ import annotations

import asyncio
import logging
import socket
import uuid
from dataclasses import dataclass
from importlib import metadata
from typing import Any, Literal, Type, TypeVar

import orjson
from aiohttp import ClientResponse
from aiohttp.client import ClientConnectionError, ClientError, ClientResponseError, ClientSession
from aiohttp.hdrs import ACCEPT_ENCODING, CONTENT_TYPE, USER_AGENT
from mashumaro import DataClassDictMixin
from mashumaro.config import BaseConfig
from mashumaro.mixins.orjson import DataClassORJSONMixin

from tomtom_api.const import TRACKING_ID

from .exceptions import TomTomAPIClientError, TomTomAPIConnectionError, TomTomAPIError, TomTomAPIRequestTimeout, TomTomAPIServerError
from .utils import serialize_bool, serialize_list

logger = logging.getLogger(__name__)


@dataclass(kw_only=True)
class BaseParams(DataClassDictMixin):
    """Base class for any params data class"""

    key: str | None = None

    def __post_serialize__(self, d: dict[Any, Any]) -> dict[str, str]:
        return {k: v for k, v in d.items() if v is not None}

    class Config(BaseConfig):  # pylint: disable=too-few-public-methods
        """
        Config for the BaseParams
        Not setting omit_none=True, because that runs before serialization, while in serialization empty lists are set to None.
        Manually omitting None values in __post_serialize__ to fix this.
        """

        serialization_strategy = {
            bool: {
                "serialize": serialize_bool,
            },
            float: {
                "serialize": str,
            },
            int: {
                "serialize": str,
            },
            list: {
                "serialize": serialize_list,
            },
        }


@dataclass
class BasePostData(DataClassDictMixin):
    """Base class for any post data class"""


class Response:
    """Response class for the TomTom API"""

    T = TypeVar("T", bound=DataClassORJSONMixin)

    def __init__(self, response: ClientResponse):
        self.response = response
        self.headers: dict[str, str] = dict(response.headers)
        self.status = response.status

    async def deserialize(self, model: Type[T]) -> T:
        """Deserialize the response using the provided model"""
        logger.info("Deserializing response to %s", model)
        try:
            text = await self.response.text()
            return model.from_json(text)
        except Exception as e:
            logger.error("Failed to deserialize response: %s", e)
            raise

    async def dict(self) -> dict:
        """Deserialize the response to a dictionary"""
        logger.info("Deserializing response to dictionary")
        try:
            text = await self.response.text()
            return orjson.loads(text)  # pylint: disable=maybe-no-member
        except orjson.JSONDecodeError as e:  # pylint: disable=maybe-no-member
            logger.error("Failed to decode JSON response: %s", e)
            raise

    async def text(self) -> str:
        """Return the response as text"""
        logger.info("Returning response as text")
        return await self.response.text()

    async def bytes(self) -> bytes:
        """Return the response as bytes"""
        logger.info("Returning response as bytes")
        return await self.response.read()


@dataclass(kw_only=True)
class ApiOptions:
    """
    Options to configure the TomTom API client.

    Attributes
    ----------
    api_key : str
        An API key valid for the requested service.
    base_url : str
        The base URL for the TomTom API. Default is "https://api.tomtom.com".
    gzip_compression : bool, optional
        Enables response compression. Default is False.
    request_timeout : int, optional
        The timeout for the request in seconds. Default is 10.
    tracking_id : bool, optional
        Specifies an identifier for each request. Default is False.
    """

    api_key: str
    base_url: Literal[
        "https://api.tomtom.com",
        "https://kr-api.tomtom.com",
    ] = "https://api.tomtom.com"
    gzip_compression: bool = False
    request_timeout: int = 10
    tracking_id: bool = False


class BaseApi:
    """
    Client for the TomTom API.

    Attributes
    ----------
    options : ApiOptions
        The options for the client.
    """

    _version: str = metadata.version(__package__)

    def __init__(
        self,
        options: ApiOptions,
        session: ClientSession | None = None,
    ):
        self.options = options
        self.session = ClientSession(options.base_url) if session is None else session

        self._default_headers: dict[str, str] = {
            CONTENT_TYPE: "application/json",
            USER_AGENT: f"TomTomApiPython/{self._version}",
        }

        self._default_params: dict[str, str] = {
            "key": self.options.api_key,
        }

    async def _request(  # pylint: disable=too-many-arguments
        self,
        method: Literal["DELETE", "GET", "POST", "PUT"],
        endpoint: str,
        *,
        params: BaseParams | None = None,
        headers: dict[str, str] | None = None,
        data: dict | None = None,
    ) -> Response:
        """Make a request to the TomTom API"""
        request_params = {**self._default_params, **(params.to_dict() if params else {})}
        request_headers = {**self._default_headers, **(headers if headers else {})}

        if self.options.gzip_compression:
            request_headers[ACCEPT_ENCODING] = "gzip"
        if self.options.tracking_id:
            tracking_id = str(uuid.uuid4())
            request_headers[TRACKING_ID] = tracking_id
        else:
            tracking_id = "not tracked"

        logger.info("%s %s (%s)", method, endpoint, tracking_id)

        try:
            async with asyncio.timeout(self.options.request_timeout):
                response = await self.session.request(
                    method,
                    endpoint,
                    params=request_params,
                    json=data,
                    headers=request_headers,
                )

                logger.info("%s %s returns: %s", method, endpoint, response.status)

                # Log headers starting with 'x-tomtom' and the tracking id
                for header, value in response.headers.items():
                    if header.lower().startswith("x-tomtom") or header.lower() == TRACKING_ID.lower():
                        logger.info("Response header %s: %s", header, value)

                response.raise_for_status()

        except asyncio.TimeoutError as exception:
            msg = "Timeout occurred while connecting to the API"
            raise TomTomAPIRequestTimeout(msg) from exception
        except ClientConnectionError as exception:
            msg = "Connection error"
            raise TomTomAPIConnectionError(msg) from exception
        except ClientResponseError as exception:
            if 400 <= exception.status < 500:
                msg = "Client error"
                raise TomTomAPIClientError(msg) from exception
            if exception.status >= 500:
                msg = "Server error"
                raise TomTomAPIServerError(msg) from exception
            msg = "Response error"
            raise TomTomAPIError(msg) from exception
        except (
            ClientError,
            socket.gaierror,
        ) as exception:
            msg = "Error occurred while communicating with the API"
            raise TomTomAPIConnectionError(exception) from exception

        return Response(response)

    async def delete(
        self,
        endpoint: str,
        *,
        params: BaseParams | None = None,
        headers: dict | None = None,
    ) -> Response:
        """Make a DELETE request"""
        return await self._request(
            "DELETE",
            endpoint,
            params=params,
            headers=headers,
        )

    async def get(
        self,
        endpoint: str,
        *,
        params: BaseParams | None = None,
        headers: dict | None = None,
    ) -> Response:
        """Make a GET request"""
        return await self._request(
            "GET",
            endpoint,
            params=params,
            headers=headers,
        )

    async def post(  # pylint: disable=too-many-arguments
        self,
        endpoint: str,
        *,
        params: BaseParams | None = None,
        headers: dict | None = None,
        data: BasePostData | None = None,
    ) -> Response:
        """Make a POST request"""
        return await self._request(
            "POST",
            endpoint,
            params=params,
            data=(data.to_dict() if data else None),
            headers=headers,
        )

    async def put(  # pylint: disable=too-many-arguments
        self,
        endpoint: str,
        *,
        params: BaseParams | None = None,
        headers: dict | None = None,
        data: BasePostData | None = None,
    ) -> Response:
        """Make a PUT request"""
        return await self._request(
            "PUT",
            endpoint,
            params=params,
            data=(data.to_dict() if data else None),
            headers=headers,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()  # Close the session when exiting the context
            self.session = None

    async def close(self):
        """Close the client"""

        if self.session:
            await self.session.close()  # Close the session if manually closing
            self.session = None
