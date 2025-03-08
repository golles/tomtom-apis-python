"""Traffic tests."""

from collections.abc import AsyncGenerator

import pytest

from tests.const import API_KEY
from tomtom_apis.api import ApiOptions
from tomtom_apis.models import Language, TileSizeType
from tomtom_apis.traffic import TrafficApi
from tomtom_apis.traffic.models import (
    BBoxParam,
    BoudingBoxParam,
    CategoryFilterType,
    FlowSegmentDataParams,
    FlowSegmentDataResponse,
    FlowStyleType,
    FlowTagType,
    FlowType,
    IncidentDetailsParams,
    IncidentDetailsPostData,
    IncidentDetailsResponse,
    IncidentStyleType,
    IncidentTileFormatType,
    IncidentViewportResponse,
    RasterFlowTilesParams,
    RasterIncidentTilesParams,
    SpeedUnitType,
    TimeValidityFilterType,
    VectorFlowTilesParams,
    VectorIncidentTilesParams,
)


@pytest.fixture(name="traffic_api")
async def fixture_traffic_api() -> AsyncGenerator[TrafficApi]:
    """Fixture for TrafficApi."""
    options = ApiOptions(api_key=API_KEY)
    async with TrafficApi(options) as traffic:
        yield traffic


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["traffic/traffic/get_incident_details_bbox.json"], indirect=True)
async def test_deserialization_get_incident_details_bbox(traffic_api: TrafficApi) -> None:
    """Test the get_incident_details method."""
    response = await traffic_api.get_incident_details(
        bbox=BBoxParam(
            minLon=4.8854592519716675,
            minLat=52.36934334773164,
            maxLon=4.897883244144765,
            maxLat=52.37496348620152,
        ),
        params=IncidentDetailsParams(
            fields="{incidents{type,geometry{type,coordinates},properties{iconCategory}}}",
            language=Language.EN_GB,
            categoryFilter=[
                CategoryFilterType.UNKNOWN,
                CategoryFilterType.ACCIDENT,
                CategoryFilterType.FOG,
                CategoryFilterType.DANGEROUS_CONDITIONS,
                CategoryFilterType.RAIN,
                CategoryFilterType.ICE,
                CategoryFilterType.JAM,
                CategoryFilterType.LANE_CLOSED,
                CategoryFilterType.ROAD_CLOSED,
                CategoryFilterType.ROAD_WORKS,
                CategoryFilterType.WIND,
                CategoryFilterType.FLOODING,
                CategoryFilterType.BROKEN_DOWN_VEHICLE,
            ],
            timeValidityFilter=[TimeValidityFilterType.PRESENT],
        ),
    )

    assert response
    assert isinstance(response, IncidentDetailsResponse)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["traffic/traffic/get_incident_details_ids.json"], indirect=True)
async def test_deserialization_get_incident_details_ids(traffic_api: TrafficApi) -> None:
    """Test the get_incident_details method."""
    response = await traffic_api.get_incident_details(
        ids=["string"],
        params=IncidentDetailsParams(
            fields="{incidents{type,geometry{type,coordinates},properties{iconCategory}}}",
            language=Language.EN_GB,
            categoryFilter=[
                CategoryFilterType.UNKNOWN,
                CategoryFilterType.ACCIDENT,
                CategoryFilterType.FOG,
                CategoryFilterType.DANGEROUS_CONDITIONS,
                CategoryFilterType.RAIN,
                CategoryFilterType.ICE,
                CategoryFilterType.JAM,
                CategoryFilterType.LANE_CLOSED,
                CategoryFilterType.ROAD_CLOSED,
                CategoryFilterType.ROAD_WORKS,
                CategoryFilterType.WIND,
                CategoryFilterType.FLOODING,
                CategoryFilterType.BROKEN_DOWN_VEHICLE,
            ],
            timeValidityFilter=[TimeValidityFilterType.PRESENT],
        ),
    )

    assert response
    assert isinstance(response, IncidentDetailsResponse)


async def test_get_incident_details_mutually_exclusive_parameters(traffic_api: TrafficApi) -> None:
    """Test the mutually exclusive parameters from the get_incident_details method."""
    with pytest.raises(ValueError, match="bbox and ids are mutually exclusive parameters"):
        await traffic_api.get_incident_details(
            params=IncidentDetailsParams(),
        )


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["traffic/traffic/post_incident_details.json"], indirect=True)
async def test_deserialization_post_incident_details(traffic_api: TrafficApi) -> None:
    """Test the post_incident_details method."""
    response = await traffic_api.post_incident_details(
        params=IncidentDetailsParams(
            fields="{incidents{type,geometry{type,coordinates},properties{iconCategory}}}",
            language=Language.EN_GB,
            categoryFilter=[
                CategoryFilterType.UNKNOWN,
                CategoryFilterType.ACCIDENT,
                CategoryFilterType.FOG,
                CategoryFilterType.DANGEROUS_CONDITIONS,
                CategoryFilterType.RAIN,
                CategoryFilterType.ICE,
                CategoryFilterType.JAM,
                CategoryFilterType.LANE_CLOSED,
                CategoryFilterType.ROAD_CLOSED,
                CategoryFilterType.ROAD_WORKS,
                CategoryFilterType.WIND,
                CategoryFilterType.FLOODING,
                CategoryFilterType.BROKEN_DOWN_VEHICLE,
            ],
            timeValidityFilter=[TimeValidityFilterType.PRESENT],
        ),
        data=IncidentDetailsPostData(ids=["string"]),
    )

    assert response
    assert isinstance(response, IncidentDetailsResponse)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["traffic/traffic/get_incident_viewport.json"], indirect=True)
async def test_deserialization_get_incident_viewport(traffic_api: TrafficApi) -> None:
    """Test the get_incident_viewport method."""
    response = await traffic_api.get_incident_viewport(
        bounding_box=BoudingBoxParam(minY=-939584.4813015489, minX=-23954526.723651607, maxY=14675583.153020501, maxX=25043442.895825107),
        bounding_zoom=2,
        overview_box=BoudingBoxParam(minY=-939584.4813015489, minX=-23954526.723651607, maxY=14675583.153020501, maxX=25043442.895825107),
        overview_zoom=2,
        copyright_information=True,
    )

    assert response
    assert isinstance(response, IncidentViewportResponse)


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["traffic/traffic/get_raster_incident_tile.png"], indirect=True)
async def test_deserialization_get_static_image(traffic_api: TrafficApi) -> None:
    """Test the get_static_image method."""
    response = await traffic_api.get_raster_incident_tile(
        style=IncidentStyleType.S0,
        x=1207,
        y=1539,
        zoom=12,
        image_format=IncidentTileFormatType.PNG,
        params=RasterIncidentTilesParams(t="-1", tileSize=TileSizeType.SIZE_256),
    )

    assert response
    assert isinstance(response, bytes)


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["traffic/traffic/get_vector_incident_tile.pbf"], indirect=True)
async def test_deserialization_get_tile_v1(traffic_api: TrafficApi) -> None:
    """Test the get_vector_incident_tile method."""
    response = await traffic_api.get_vector_incident_tile(
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

    assert response
    assert isinstance(response, bytes)


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["traffic/traffic/get_flow_segment_data.json"], indirect=True)
async def test_deserialization_get_flow_segment_data(traffic_api: TrafficApi) -> None:
    """Test the get_flow_segment_data method."""
    response = await traffic_api.get_flow_segment_data(
        style=FlowStyleType.RELATIVE0,
        zoom=10,
        point="52.41072,4.84239",
        params=FlowSegmentDataParams(
            unit=SpeedUnitType.KMPH,
            openLr=False,
        ),
    )

    assert response
    assert isinstance(response, FlowSegmentDataResponse)


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["traffic/traffic/get_raster_flow_tiles.pbf"], indirect=True)
async def test_deserialization_get_raster_flow_tiles(traffic_api: TrafficApi) -> None:
    """Test the get_raster_flow_tiles method."""
    response = await traffic_api.get_raster_flow_tiles(
        style=FlowStyleType.RELATIVE0,
        x=1207,
        y=1539,
        zoom=12,
        params=RasterFlowTilesParams(
            tileSize=TileSizeType.SIZE_256,
        ),
    )

    assert response
    assert isinstance(response, bytes)


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["traffic/traffic/get_vector_flow_tiles.pbf"], indirect=True)
async def test_deserialization_get_vector_flow_tiles(traffic_api: TrafficApi) -> None:
    """Test the get_vector_flow_tiles method."""
    response = await traffic_api.get_vector_flow_tiles(
        flow_type=FlowType.RELATIVE,
        x=1207,
        y=1539,
        zoom=12,
        params=VectorFlowTilesParams(
            margin=0.1,
            tags=[
                FlowTagType.TRAFFIC_LEVEL,
                FlowTagType.TRAFFIC_ROAD_COVERAGE,
                FlowTagType.LEFT_HAND_TRAFFIC,
                FlowTagType.ROAD_CLOSURE,
                FlowTagType.ROAD_CATEGORY,
                FlowTagType.ROAD_SUBCATEGORY,
            ],
        ),
    )

    assert response
    assert isinstance(response, bytes)
