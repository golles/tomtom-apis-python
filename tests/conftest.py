"""Conftest for the tests."""

from pathlib import Path

import pytest
from aresponses import ResponsesMockServer

from .const import DEFAULT_HEADERS


def load_json(filename: str) -> str:
    """Load a fixture."""
    path = Path(__package__) / "fixtures" / filename
    return path.read_text(encoding="utf-8")


def load_png(filename: str) -> bytes:
    """Load a fixture."""
    path = Path(__package__) / "fixtures" / filename
    return path.read_bytes()


@pytest.fixture(name="json_response")
def fixture_json_response(request: pytest.FixtureRequest, aresponses: ResponsesMockServer) -> None:
    """Fixture for adding the aresponses response with a configurable JSON file."""
    fixture_filename = request.param
    aresponses.add(
        response=aresponses.Response(
            status=200,
            headers=DEFAULT_HEADERS,
            text=load_json(fixture_filename),
        ),
    )


@pytest.fixture(name="image_response")
def fixture_image_response(request: pytest.FixtureRequest, aresponses: ResponsesMockServer) -> None:
    """Fixture for adding the aresponses response with a configurable image file."""
    fixture_filename = request.param
    aresponses.add(
        response=aresponses.Response(
            status=200,
            content_type="image/png",
            text=load_png(fixture_filename).decode("latin1"),
        ),
    )
