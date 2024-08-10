"""Test for the Api"""

import asyncio
import socket
from dataclasses import dataclass
from unittest.mock import AsyncMock, patch

import orjson
import pytest
from aiohttp import ClientConnectionError, ClientError, ClientResponse, ClientResponseError, ClientSession
from mashumaro.mixins.orjson import DataClassORJSONMixin

from tomtom_api.api import ApiOptions, BaseApi, BaseParams, BasePostData, Response
from tomtom_api.const import TRACKING_ID
from tomtom_api.exceptions import TomTomAPIClientError, TomTomAPIConnectionError, TomTomAPIError, TomTomAPIRequestTimeout, TomTomAPIServerError

from .const import API_KEY


@dataclass(kw_only=True)
class MockModel(DataClassORJSONMixin):
    """Mock model"""

    key: str


@pytest.fixture(name="mock_response")
def fixture_mock_response():
    """Fixture for mock response"""
    mock_resp = AsyncMock(spec=ClientResponse)
    mock_resp.status = 200
    mock_resp.headers = {
        "content-type": "application/json;charset=utf-8",
        "Tracking-ID": "1234567890",
        "x-tomtom-processed-by": "westeurope",
    }
    mock_resp.text = AsyncMock(return_value='{"key": "value"}')
    return mock_resp


@pytest.fixture(name="mock_session")
def fixture_mock_session(mock_response):
    """Fixture for mock session"""
    session = AsyncMock(spec=ClientSession)
    session.request = AsyncMock(return_value=mock_response)
    return session


@pytest.fixture(name="base_api")
async def fixture_base_api(mock_session):
    """Fixture for BaseApi"""
    options = ApiOptions(api_key=API_KEY)
    async with BaseApi(options, mock_session) as base:
        yield base


def test_base_params_initialization():
    """
    Test that a BaseParams instance initializes with default values.
    The key should be None initially.
    """
    params = BaseParams()
    assert params.key is None


def test_from_dict_basic():
    """
    Test that from_dict correctly assigns a single value from a dictionary
    to the dataclass attribute.
    """
    params = BaseParams().from_dict({"key": "value"})
    assert params.key == "value"


def test_from_dict_with_extra_keys():
    """
    Test that from_dict can handle dictionaries with extra keys not present
    in the dataclass. Only the relevant attributes should be set.
    """
    params = BaseParams().from_dict({"key": "value", "extra_key": "extra_value"})
    assert params.key == "value"


def test_from_dict_with_missing_attributes():
    """
    Test that from_dict handles cases where the dictionary has no keys
    corresponding to the dataclass attributes. Attributes should remain
    at their default values.
    """
    params = BaseParams().from_dict({})
    assert params.key is None


def test_from_dict_with_none_values():
    """
    Test that from_dict correctly assigns None as a value in the dictionary.
    The attribute should be set to None.
    """
    params = BaseParams().from_dict({"key": None})
    assert params.key is None


def test_from_dict_with_incorrect_value_types():
    """
    Test the method’s behavior when the dictionary contains values of types
    other than strings. The current implementation assigns the value as-is.
    """
    params = BaseParams().from_dict({"key": 123})
    assert params.key == 123


def test_from_dict_with_boolean_strings():
    """
    Test that from_dict correctly assigns boolean-like strings. Although the
    docstring suggests booleans should be lowercase strings, this test checks
    that such values are assigned as-is.
    """
    params = BaseParams().from_dict({"key": "true"})
    assert params.key == "true"


def test_from_dict_with_nested_dictionary():
    """
    Test how from_dict handles nested dictionaries. The nested dictionary
    should be assigned as a value to the attribute.
    """
    params = BaseParams().from_dict({"key": {"nested_key": "nested_value"}})
    assert params.key == {"nested_key": "nested_value"}


async def test_deserialize_success(mock_response):
    """Test the deserialize method"""
    response = Response(mock_response)
    result = await response.deserialize(MockModel)

    assert isinstance(result, MockModel)
    assert result.key == "value"
    mock_response.text.assert_awaited_once()


async def test_deserialize_failure(mock_response):
    """Test the deserialize method"""
    mock_response.text.side_effect = Exception("Deserialization error")
    response = Response(mock_response)

    with pytest.raises(Exception, match="Deserialization error"):
        await response.deserialize(MockModel)

    mock_response.text.assert_awaited_once()


async def test_dict_success(mock_response):
    """Test the dict method"""
    response = Response(mock_response)
    result = await response.dict()

    assert result == {"key": "value"}
    mock_response.text.assert_awaited_once()


async def test_dict_json_decode_error(mock_response):
    """Test the dict method"""
    mock_response.text.return_value = "invalid json"
    response = Response(mock_response)

    with pytest.raises(orjson.JSONDecodeError):  # pylint: disable=maybe-no-member
        await response.dict()

    mock_response.text.assert_awaited_once()


async def test_text(mock_response):
    """Test the text method"""
    mock_response.text.return_value = "response text"
    response = Response(mock_response)
    result = await response.text()

    assert result == "response text"
    mock_response.text.assert_awaited_once()


async def test_get_request(base_api, mock_session):
    """Test the get method"""
    endpoint = "/test/endpoint"
    response = await base_api.get(endpoint)

    mock_session.request.assert_called_once_with(
        "GET",
        endpoint,
        params={"key": API_KEY},
        json=None,
        headers={
            "Content-Type": "application/json",
            "User-Agent": f"TomTomApiPython/{base_api._version}",  # pylint: disable=protected-access
        },
    )
    assert isinstance(response, Response)
    assert response.status == 200


async def test_get_request_with_gzip(base_api, mock_session):
    """Test the get method with gzip"""
    endpoint = "/test/endpoint"
    base_api.options.gzip_compression = True
    response = await base_api.get(endpoint)

    mock_session.request.assert_called_once_with(
        "GET",
        endpoint,
        params={"key": API_KEY},
        json=None,
        headers={
            "Content-Type": "application/json",
            "User-Agent": f"TomTomApiPython/{base_api._version}",  # pylint: disable=protected-access
            "Accept-Encoding": "gzip",
        },
    )
    assert isinstance(response, Response)
    assert response.status == 200


async def test_post_request(base_api, mock_session):
    """Test the post method"""
    endpoint = "/test/endpoint"
    data = BasePostData()
    response = await base_api.post(endpoint, data=data)

    mock_session.request.assert_called_once_with(
        "POST",
        endpoint,
        params={"key": API_KEY},
        json=data.to_dict(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": f"TomTomApiPython/{base_api._version}",  # pylint: disable=protected-access
        },
    )
    assert isinstance(response, Response)
    assert response.status == 200


async def test_delete_request(base_api, mock_session):
    """Test the delete method"""
    endpoint = "/test/endpoint"
    response = await base_api.delete(endpoint)

    mock_session.request.assert_called_once_with(
        "DELETE",
        endpoint,
        params={"key": API_KEY},
        json=None,
        headers={
            "Content-Type": "application/json",
            "User-Agent": f"TomTomApiPython/{base_api._version}",  # pylint: disable=protected-access
        },
    )
    assert isinstance(response, Response)
    assert response.status == 200


async def test_put_request(base_api, mock_session):
    """Test the put method"""
    endpoint = "/test/endpoint"
    data = BasePostData()
    response = await base_api.put(endpoint, data=data)

    mock_session.request.assert_called_once_with(
        "PUT",
        endpoint,
        params={"key": API_KEY},
        json=data.to_dict(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": f"TomTomApiPython/{base_api._version}",  # pylint: disable=protected-access
        },
    )
    assert isinstance(response, Response)
    assert response.status == 200


async def test_request_timeout(base_api, mock_session):
    """Test the request method with a timeout"""
    mock_session.request.side_effect = asyncio.TimeoutError()
    with pytest.raises(TomTomAPIRequestTimeout):
        await base_api.get("/timeout/endpoint")


async def test_request_connection_error(base_api, mock_session):
    """Test the request method with a connection error"""
    mock_session.request.side_effect = ClientConnectionError()
    with pytest.raises(TomTomAPIConnectionError):
        await base_api.get("/connection/error")


async def test_request_client_reponse_error(base_api, mock_session):
    """Test the request method with a client response error"""
    error = ClientResponseError(request_info=None, history=None, status=400)
    mock_session.request.side_effect = error
    with pytest.raises(TomTomAPIClientError):
        await base_api.get("/client/error")


async def test_request_server_response_error(base_api, mock_session):
    """Test the request method with a server response error"""
    error = ClientResponseError(request_info=None, history=None, status=500)
    mock_session.request.side_effect = error
    with pytest.raises(TomTomAPIServerError):
        await base_api.get("/server/error")


async def test_request_unknown_response_error(base_api, mock_session):
    """Test the request method with an unknown response error"""
    error = ClientResponseError(request_info=None, history=None, status=399)
    mock_session.request.side_effect = error
    with pytest.raises(TomTomAPIError):
        await base_api.get("/server/error")


async def test_request_client_error(base_api, mock_session):
    """Test the request method with a client error"""
    error = ClientError()
    mock_session.request.side_effect = error
    with pytest.raises(TomTomAPIConnectionError):
        await base_api.get("/server/error")


async def test_request_socket_error(base_api, mock_session):
    """Test the request method with a socket error"""
    error = socket.gaierror()
    mock_session.request.side_effect = error
    with pytest.raises(TomTomAPIConnectionError):
        await base_api.get("/server/error")


async def test_tracking_id(base_api, mock_session):
    """Test the tracking_id option"""
    base_api.options.tracking_id = True
    with patch("uuid.uuid4", return_value="mock-uuid"):
        endpoint = "/test/endpoint"
        response = await base_api.get(endpoint)

        assert mock_session.request.call_args[1]["headers"][TRACKING_ID] == "mock-uuid"
        assert isinstance(response, Response)
        assert response.status == 200
