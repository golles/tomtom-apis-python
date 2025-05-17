"""Update test fixtures.

This script downloads and replaces fixtures with the latest content from the real API.
The idea is to do this regularly to keep the fixtures up-to-date and detect breaking changes.
"""

import asyncio
import json
import os
import subprocess
from pathlib import Path
from typing import Any

import aiohttp

BASE_URL = "https://api.tomtom.com"
PROJECT_ROOT = Path(__file__).parent.parent
FIXTURES_PATH = Path(PROJECT_ROOT) / "tests" / "fixtures"
FIXTURE_FILE_PATH = Path(PROJECT_ROOT) / "scripts" / "data" / "fixtures.json"


class ContentExceptionError(Exception):
    """Exception raised when the content is not as expected."""

    def __init__(self) -> None:
        """Initialize the ContentException."""
        super().__init__("Content must be either a string or bytes")


async def read_json(file_path: Path) -> list[dict[str, Any]]:
    """Read a json file and return its content as a dict."""
    with file_path.open(encoding="UTF-8") as file:
        return json.load(file)


async def make_request(session: aiohttp.ClientSession, method: str, url: str, data: dict | None = None) -> str | bytes | None:
    """Make a request to the TomTom API."""
    try:
        async with session.request(method.upper(), url, json=data) as response:
            response.raise_for_status()
            if "image" in response.content_type:
                return await response.read()
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Request failed: {e}")
        return None


async def save_fixture(content: str | bytes, fixture_path: Path) -> None:
    """Save a fixture to the specified path."""
    fixture_path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, str):
        mode = "w"
        encoding = "utf-8"
    elif isinstance(content, bytes):
        mode = "wb"
        encoding = None
    else:
        raise ContentExceptionError

    with fixture_path.open(mode=mode, encoding=encoding) as file:
        file.write(content)


async def process_fixture(session: aiohttp.ClientSession, api_entry: dict, api_key: str) -> None:
    """Process a single fixture."""
    for fixture in api_entry["fixtures"]:
        method = fixture.get("method")
        url = fixture.get("url")
        fixture_filename = fixture.get("fixture")
        post_data = fixture.get("data")

        fixture_path = FIXTURES_PATH / fixture_filename
        full_url = f"{BASE_URL}/{url.replace('{{TT_KEY}}', api_key)}"

        if method and url and fixture_path:
            content = await make_request(session, method, full_url, post_data)
            if content:
                await save_fixture(content, fixture_path)
                print(f"Saved fixture to {fixture_path}")
            else:
                print(f"Failed to get content for {fixture_path}")
        else:
            print(f"Invalid fixture: {fixture}")


async def process_fixtures(file_path: Path, api_key: str) -> None:
    """Process fixtures."""
    data = await read_json(file_path)
    async with aiohttp.ClientSession() as session:
        tasks = [process_fixture(session, api_entry, api_key) for api_entry in data]
        await asyncio.gather(*tasks)


def get_api_key() -> str:
    """Get the API key or ask for user input."""
    apik_key = os.getenv("TOMTOM_API_KEY")

    if apik_key:
        return apik_key

    return input("Please enter your API key: ")


if __name__ == "__main__":
    user_api_key = get_api_key()
    asyncio.run(process_fixtures(FIXTURE_FILE_PATH, user_api_key))

    # Make all fixture files prettier
    subprocess.run(
        [f"{PROJECT_ROOT}/node_modules/.bin/prettier", "--log-level", "silent", "--write", FIXTURES_PATH],
        check=True,
    )
