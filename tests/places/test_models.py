"""Test for places models."""

from tomtom_apis.places.models import Connector


def test_connector_post_deserialize() -> None:
    """Test the Connector __post_deserialize__ method."""
    connector1 = {"id": "1", "currentA": 32, "currentType": "AC3", "ratedPowerKW": 22.0, "type": "IEC62196Type2Outlet", "voltageV": 400}
    connector2 = {"id": "1", "currentA": 32, "currentType": "AC3", "ratedPowerKW": 22.0, "connectorType": "IEC62196Type2Outlet", "voltageV": 400}

    assert Connector.from_dict(connector1) == Connector.from_dict(connector2)
