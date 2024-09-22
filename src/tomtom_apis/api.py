"""Client for the TomTom API."""

from __future__ import annotations

import logging
import socket
import uuid
from dataclasses import dataclass, field
from importlib import metadata
from typing import Any, Literal, TypeVar

import orjson
from aiohttp import ClientResponse, ClientTimeout
from aiohttp.client import (
    ClientConnectionError,
    ClientError,
    ClientResponseError,
    ClientSession,
)
from aiohttp.hdrs import ACCEPT_ENCODING, CONTENT_TYPE, USER_AGENT
from mashumaro import DataClassDictMixin
from mashumaro.config import BaseConfig
from mashumaro.mixins.orjson import DataClassORJSONMixin

from .const import TOMTOM_HEADER_PREFIX, TRACKING_ID_HEADER
from .exceptions import (
    TomTomAPIClientError,
    TomTomAPIConnectionError,
    TomTomAPIError,
    TomTomAPIRequestTimeout,
    TomTomAPIServerError,
)
from .utils import serialize_bool, serialize_list

logger = logging.getLogger(__name__)


@dataclass(kw_only=True)
class BaseParams(DataClassDictMixin):
    """Base class for any params data class.

    Attributes:
        key (str | None): The api key attribute, defaults to None, can override the key from ApiOptions.
    """

    key: str | None = None

    def __post_serialize__(self, d: dict[Any, Any]) -> dict[str, str]:
        """Removes keys with None values from the serialized dictionary.

        Args:
            d: The dictionary to be processed.

        Returns:
            A new dictionary without keys that have a value of None.
        """
        return {k: v for k, v in d.items() if v is not None}

    class Config(BaseConfig):  # pylint: disable=too-few-public-methods
        """Config for the BaseParams.

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


@dataclass(kw_only=True)
class BasePostData(DataClassDictMixin):
    """Base class for any post data class.

    Attributes:
        DataClassDictMixin: Mixin for converting data classes to dictionaries.
    """


class Response:
    """Response class for the TomTom API.

    Args:
        response: The aiohttp ClientResponse object.

    Methods:
        deserialize(model: type[T]) -> T: Deserialize the response to the given model.
        dict() -> dict: Deserialize the response to a dictionary.
        text() -> str: Return the response as text.
        bytes() -> bytes: Return the response as bytes.
    """

    T = TypeVar("T", bound=DataClassORJSONMixin)

    def __init__(self, response: ClientResponse):
        """Initialize the Response object.

        Args:
            response: The aiohttp ClientResponse object.
        """
        self._response = response
        self.headers: dict[str, str] = dict(response.headers)
        self.status = response.status

    async def deserialize(self, model: type[T]) -> T:
        """Deserialize the response to the given model.

        Args:
            model: The model class to deserialize the response to.

        Returns:
            An instance of the given model class.

        Raises:
            Exception: If the deserialization fails.
        """
        logger.info("Deserializing response to %s", model)
        try:
            text = await self._response.text()
            return model.from_json(text)
        except Exception as e:
            logger.error("Failed to deserialize response: %s", e)
            raise

    async def dict(self) -> dict:
        """Deserialize the response to a dictionary.

        Returns:
            A dictionary representation of the response.

        Raises:
            orjson.JSONDecodeError: If the response is not valid JSON.
        """
        logger.info("Deserializing response to dictionary")
        try:
            text = await self._response.text()
            return orjson.loads(text)  # pylint: disable=maybe-no-member
        except orjson.JSONDecodeError as e:  # pylint: disable=maybe-no-member
            logger.error("Failed to decode JSON response: %s", e)
            raise

    async def text(self) -> str:
        """Return the response as text.

        Returns:
            The response as a string.
        """
        logger.info("Returning response as text")
        return await self._response.text()

    async def bytes(self) -> bytes:
        """Return the response as bytes.

        Returns:
            The response as a bytes object.
        """
        logger.info("Returning response as bytes")
        return await self._response.read()


@dataclass(kw_only=True)
class ApiOptions:
    """Options to configure the TomTom API client.

    Attributes:
        api_key: str
            An API key valid for the requested service.
        base_url: str
            The base URL for the TomTom API. Default is "https://api.tomtom.com".
        gzip_compression: bool, optional
            Enables response compression. Default is False.
        timeout: ClientTimeout, optional
            The timeout object for the request. Default is ClientTimeout(total=10).
        tracking_id: bool, optional
            Specifies an identifier for each request. Default is False.
    """

    api_key: str
    base_url: str = "https://api.tomtom.com"
    gzip_compression: bool = False
    timeout: ClientTimeout = field(default_factory=lambda: ClientTimeout(total=10))
    tracking_id: bool = False


class BaseApi:
    """Client for the TomTom API.

    Attributes:
        options : ApiOptions
            The options for the client.
    """

    _version: str = metadata.version(__package__)

    def __init__(
        self,
        options: ApiOptions,
        session: ClientSession | None = None,
    ):
        """Initializes the BaseApi object.

        Args:
            options: ApiOptions
                The options for the client.
            session: ClientSession, optional
                The client session to use for requests. If not provided, a new session is created.
        """
        self.options = options
        self.session = ClientSession(options.base_url, timeout=options.timeout) if session is None else session

        self._default_headers: dict[str, str] = {
            CONTENT_TYPE: "application/json",
            USER_AGENT: f"TomTomApiPython/{self._version}",
        }

        self._default_params: dict[str, str] = {
            "key": options.api_key,
        }

    async def _request(  # pylint: disable=too-many-arguments
        self,
        method: Literal["DELETE", "GET", "POST", "PUT"],
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
        params: BaseParams | None = None,
        data: BasePostData | None = None,
    ) -> Response:
        """Make a request to the TomTom API.

        Args:
            method: Literal["DELETE", "GET", "POST", "PUT"]
                The HTTP method for the request.
            endpoint: str
                The endpoint to send the request to.
            headers: dict[str, str] | None, optional
                The headers for the request.
            params: BaseParams | None, optional
                The parameters for the request.
            data: BasePostData | None, optional
                The data to be sent in the request body.

        Returns:
            Response
                The response object from the API.

        Raises:
            TomTomAPIRequestTimeout: If a timeout occurs while connecting to the API.
            TomTomAPIConnectionError: If a connection error occurs.
            TomTomAPIClientError: If a client-side error (4xx) occurs.
            TomTomAPIServerError: If a server-side error (5xx) occurs.
            TomTomAPIError: For other errors raised by the TomTom SDK.
        """
        request_params = {
            **self._default_params,
            **(params.to_dict() if params else {}),
        }
        request_headers = {**self._default_headers, **(headers if headers else {})}
        request_data = data.to_dict() if data else None

        if self.options.gzip_compression:
            request_headers[ACCEPT_ENCODING] = "gzip"
        if self.options.tracking_id:
            tracking_id = str(uuid.uuid4())
            request_headers[TRACKING_ID_HEADER] = tracking_id
        else:
            tracking_id = "not tracked"

        logger.info("%s %s (%s)", method, endpoint, tracking_id)

        try:
            response = await self.session.request(
                method,
                endpoint,
                params=request_params,
                json=request_data,
                headers=request_headers,
            )

            logger.info("%s %s returns: %s", method, endpoint, response.status)

            # Log TomTom and the tracking id headers
            for header, value in response.headers.items():
                if header.lower().startswith(TOMTOM_HEADER_PREFIX) or header.lower() == TRACKING_ID_HEADER.lower():
                    logger.info("Response header %s: %s", header, value)

            response.raise_for_status()

        except TimeoutError as exception:
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
        headers: dict[str, str] | None = None,
        params: BaseParams | None = None,
    ) -> Response:
        """Make a DELETE request.

        Args:
            endpoint: str
                The endpoint to send the DELETE request to.
            headers: dict[str, str] | None, optional
                The headers for the request.
            params: BaseParams | None, optional
                The parameters for the request.

        Returns:
            Response
                The response object from the API.
        """
        return await self._request(
            "DELETE",
            endpoint,
            headers=headers,
            params=params,
        )

    async def get(
        self,
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
        params: BaseParams | None = None,
    ) -> Response:
        """Make a GET request.

        Args:
            endpoint: str
                The endpoint to send the GET request to.
            headers: dict[str, str] | None, optional
                The headers for the request.
            params: BaseParams | None, optional
                The parameters for the request.

        Returns:
            Response
                The response object from the API.
        """
        return await self._request(
            "GET",
            endpoint,
            headers=headers,
            params=params,
        )

    async def post(  # pylint: disable=too-many-arguments
        self,
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
        params: BaseParams | None = None,
        data: BasePostData,
    ) -> Response:
        """Make a POST request.

        Args:
            endpoint: str
                The endpoint to send the POST request to.
            headers: dict[str, str] | None, optional
                The headers for the request.
            params: BaseParams | None, optional
                The parameters for the request.
            data: BasePostData
                The data to be sent in the request body.

        Returns:
            Response
                The response object from the API.
        """
        return await self._request(
            "POST",
            endpoint,
            headers=headers,
            params=params,
            data=data,
        )

    async def put(  # pylint: disable=too-many-arguments
        self,
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
        params: BaseParams | None = None,
        data: BasePostData,
    ) -> Response:
        """Make a PUT request.

        Args:
            endpoint: str
                The endpoint to send the PUT request to.
            headers: dict[str, str] | None, optional
                The headers for the request.
            params: BaseParams | None, optional
                The parameters for the request.
            data: BasePostData
                The data to be sent in the request body.

        Returns:
            Response
                The response object from the API.
        """
        return await self._request(
            "PUT",
            endpoint,
            headers=headers,
            params=params,
            data=data,
        )

    async def __aenter__(self):
        """Enter the runtime context related to this object.

        The session used to make requests is created upon entering the context and closed upon exiting.

        Returns:
            self
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object.

        The session used for making requests is closed upon exiting the context.

        Args:
            exc_type: The type of the exception raised in the context.
            exc_val: The value of the exception raised in the context.
            exc_tb: The traceback of the exception raised in the context.
        """
        if self.session:
            await self.session.close()  # Close the session when exiting the context
            self.session = None

    async def close(self):
        """Close the session.

        Manually closes the session. If the session is not closed, it will be closed when exiting the context.

        Note:
            Does not raise an exception if the session is already closed.
        """
        if self.session:
            await self.session.close()  # Close the session if manually closing
            self.session = None
