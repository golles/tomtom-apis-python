"""EV Search test"""

import pytest

from tests.const import API_KEY
from tomtom_api.api import ApiOptions
from tomtom_api.places import EVSearchApi
from tomtom_api.places.models import EvSearchByIdParams, EvSearchNearbyParams


@pytest.fixture(name="ev_search_api")
async def fixture_ev_search_api():
    """Fixture for EVSearchApi"""
    options = ApiOptions(api_key=API_KEY)
    async with EVSearchApi(options) as ev_search:
        yield ev_search


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/ev_search/get_ev_search_nearby.json"], indirect=True)
async def test_deserialization_get_ev_search_nearby(ev_search_api: EVSearchApi):
    """Test the get_ev_search_nearby method"""
    response = await ev_search_api.get_ev_search_nearby(
        params=EvSearchNearbyParams(
            lat=52.364941,
            lon=4.8935986,
            radius=10,
        )
    )

    await ev_search_api.close()

    assert response

    # Test that the fields Connector.type and Connector.connectorType are set the same after deserialization.
    assert response.results[0].chargingStations
    first_connector = response.results[0].chargingStations[0].chargingPoints[0].connectors[0]
    assert first_connector.type == first_connector.connectorType


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["places/ev_search/get_ev_search_by_id.json"], indirect=True)
async def test_deserialization_get_ev_search_by_id(ev_search_api: EVSearchApi):
    """Test the get_ev_search_by_id method"""
    response = await ev_search_api.get_ev_search_by_id(params=EvSearchByIdParams(id="RS*ORI*E1161"))

    await ev_search_api.close()

    assert response

    # Test that the fields Connector.type and Connector.connectorType are set the same after deserialization.
    assert response.results[0].chargingStations
    first_connector = response.results[0].chargingStations[0].chargingPoints[0].connectors[0]
    assert first_connector.type == first_connector.connectorType
