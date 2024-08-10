"""Traffic tests"""

import pytest

from tests.const import API_KEY
from tomtom_api.api import ApiOptions
from tomtom_api.models import Language, TileSizeType
from tomtom_api.traffic import TrafficApi
from tomtom_api.traffic.models import BoudingBoxParam, IncidentStyleType, RasterIncidentTilesParams, VectorIncidentTilesParams


@pytest.fixture(name="traffic_display")
async def fixture_traffic_api():
    """Fixture for TrafficApi"""
    options = ApiOptions(api_key=API_KEY)
    async with TrafficApi(options) as traffic_display:
        yield traffic_display


# get_incident_details

# post_incident_details


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["traffic/traffic/get_incident_viewport.json"], indirect=True)
async def test_deserialization_get_incident_viewport(traffic_display: TrafficApi):
    """Test the get_incident_viewport method"""
    response = await traffic_display.get_incident_viewport(
        bounding_box=BoudingBoxParam(minY=-939584.4813015489, minX=-23954526.723651607, maxY=14675583.153020501, maxX=25043442.895825107),
        bounding_zoom=2,
        overview_box=BoudingBoxParam(minY=-939584.4813015489, minX=-23954526.723651607, maxY=14675583.153020501, maxX=25043442.895825107),
        overview_zoom=2,
        copyright_information=True,
    )

    await traffic_display.close()

    assert response


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["traffic/traffic/get_raster_incident_tile.png"], indirect=True)
async def test_deserialization_get_static_image(traffic_display: TrafficApi):
    """Test the get_static_image method"""
    response = await traffic_display.get_raster_incident_tile(
        style=IncidentStyleType.S0,
        x=1207,
        y=1539,
        zoom=12,
        params=RasterIncidentTilesParams(t="-1", tileSize=TileSizeType.SIZE_256),
    )

    await traffic_display.close()

    assert response


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["traffic/traffic/get_vector_incident_tile.pbf"], indirect=True)
async def test_deserialization_get_tile_v1(traffic_display: TrafficApi):
    """Test the get_vector_incident_tile method"""
    response = await traffic_display.get_vector_incident_tile(
        x=1207,
        y=1539,
        zoom=12,
        params=VectorIncidentTilesParams(
            t="-1",
            tags=[
                "icon_category",
                "description",
                "delay",
                "left_hand_traffic",
                "magnitude",
                "traffic_road_coverage",
                "end_date",
                "id",
                "road_category",
                "road_subcategory",
            ],
            language=Language.EN_GB,
        ),
    )

    await traffic_display.close()

    assert response
