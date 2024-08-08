"""MapDisplay tests"""

import pytest

from tests.const import API_KEY
from tomtom_api.api import ApiOptions
from tomtom_api.maps import MapDisplayApi
from tomtom_api.maps.models import (
    AdrCategoryType,
    LayerType,
    LayerTypeWithPoiType,
    MapTileV1Params,
    MapTileV2Params,
    StaticImageParams,
    StyleType,
    TileFormatType,
    TravelModeType,
    ViewType,
)
from tomtom_api.models import Language


@pytest.fixture(name="map_display_api")
async def fixture_map_display_api():
    """Fixture for MapDisplayApi."""
    options = ApiOptions(api_key=API_KEY)
    async with MapDisplayApi(options) as map_display:
        yield map_display


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["maps/get_map_tile.png"], indirect=True)
async def test_get_map_tile(map_display_api: MapDisplayApi):
    """Test the get_map_tile method."""
    response = await map_display_api.get_map_tile(
        layer=LayerType.BASIC,
        style=StyleType.MAIN,
        x=0,
        y=0,
        zoom=0,
        image_format=TileFormatType.PNG,
    )

    await map_display_api.close()

    assert response


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["maps/get_satellite_tile.jpg"], indirect=True)
async def test_get_satellite_tile(map_display_api: MapDisplayApi):
    """Test the get_satellite_tile method."""
    response = await map_display_api.get_satellite_tile(
        x=0,
        y=0,
        zoom=0,
        image_format=TileFormatType.PNG,
    )

    await map_display_api.close()

    assert response


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["maps/get_hillshade_tile.png"], indirect=True)
async def test_get_hillshade_tile(map_display_api: MapDisplayApi):
    """Test the get_hillshade_tile method."""
    response = await map_display_api.get_hillshade_tile(
        x=0,
        y=0,
        zoom=0,
        image_format=TileFormatType.PNG,
    )

    await map_display_api.close()

    assert response


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["maps/get_static_image.png"], indirect=True)
async def test_get_static_image(map_display_api: MapDisplayApi):
    """Test the get_static_image method."""
    response = await map_display_api.get_static_image(
        params=StaticImageParams(
            layer=LayerType.BASIC,
            style=StyleType.MAIN,
            format=TileFormatType.PNG,
            zoom=12,
            center=[4.899886, 52.379031],
            width=512,
            height=512,
            view=ViewType.UNIFIED,
        ),
    )

    await map_display_api.close()

    assert response


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["maps/get_tile_v1.pbf"], indirect=True)
async def test_get_tile_v1(map_display_api: MapDisplayApi):
    """Test the get_tile_v1 method."""
    response = await map_display_api.get_tile_v1(
        layer=LayerTypeWithPoiType.BASIC,
        x=0,
        y=0,
        zoom=0,
        params=MapTileV1Params(
            view=ViewType.UNIFIED,
            language=Language.NGT,
        ),
    )

    await map_display_api.close()

    assert response


@pytest.mark.usefixtures("image_response")
@pytest.mark.parametrize("image_response", ["maps/get_tile_v2.pbf"], indirect=True)
async def test_get_tile_v2(map_display_api: MapDisplayApi):
    """Test the get_tile_v2 method."""
    response = await map_display_api.get_tile_v2(
        layer=LayerTypeWithPoiType.BASIC,
        x=0,
        y=0,
        zoom=0,
        params=MapTileV2Params(
            view=ViewType.UNIFIED,
            include="[road_restrictions]",
            vehicleWeight=2000,
            vehicleAxleWeight=1000,
            numberOfAxles=2,
            vehicleLength=2.5,
            vehicleWidth=2.5,
            vehicleHeight=2.5,
            generalLoadType="[General_Hazardous_Materials]",
            dangerousGoodsLoadType="[Explosives]",
            adrCategory=AdrCategoryType.B,
            commercialVehicle=True,
            travelMode=TravelModeType.TAXI,
            emissionClass="[EmissionClass]",
            engineType="[Diesel]",
            travelModeProfile="0,1500,,,5.5,,2.2,,,,,,",
        ),
    )

    await map_display_api.close()

    assert response


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["maps/get_map_copyrights.txt"], indirect=True)
async def test_get_map_copyrights(map_display_api: MapDisplayApi):
    """Test the get_map_copyrights method."""
    response = await map_display_api.get_map_copyrights()

    await map_display_api.close()

    assert response
    assert "TomTom. All rights reserved." in response


@pytest.mark.usefixtures("json_response")
@pytest.mark.parametrize("json_response", ["maps/get_map_service_copyrights.json"], indirect=True)
async def test_get_map_service_copyrights(map_display_api: MapDisplayApi):
    """Test the get_map_copyrights method."""
    response = await map_display_api.get_map_service_copyrights()

    await map_display_api.close()

    assert response
    assert "©TomTom" == response.copyrightsCaption
