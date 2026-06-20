# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`tomtom-apis` is an asynchronous Python client library for the TomTom APIs. It targets **Python 3.14 only** and uses `uv` for dependency management.

## Common Commands

```sh
# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_api.py

# Run a single test by name
uv run pytest tests/test_api.py::TestClassName::test_method_name

# Linting and formatting
uv run ruff check .
uv run ruff format .
uv run mypy .
uv run pylint src tests

# Run all CI checks locally (requires jq and yq)
./scripts/local_ci_checks.sh

# Update test fixtures from the real API (requires TOMTOM_API_KEY in .env)
uv run python scripts/update_test_fixtures.py
```

## Architecture

### Package layout

```
src/tomtom_apis/
  api.py            # Core: BaseApi, ApiOptions, BaseParams, BasePostData, Response
  models.py         # Shared models (Language enum, GeoJSON types, etc.)
  const.py          # HttpMethod, HttpStatus, header constants
  exceptions.py     # TomTomAPIError and subclasses
  utils.py          # serialize_bool, serialize_list, tile coordinate helpers
  maps/             # Map Display API
  routing/          # Routing, Matrix Routing, Long-Distance EV, Waypoint Optimization
  traffic/          # Traffic, Intermediate Traffic, Junction Analytics, etc.
  places/           # Search, Geocoding, Reverse Geocoding, Batch Search, EV Search
  automotive/       # Autostream, Fuel Prices, Parking Availability
  tracking_logistics/ # Geofencing, Location History, Notifications, Snap to Roads
```

### Core abstractions (`api.py`)

- **`ApiOptions`** — holds `api_key`, `base_url`, `gzip_compression`, `timeout`, and `tracking_id`. Passed to every API class.
- **`BaseApi`** — async context manager with `get/post/put/delete` methods. The `api_key` is injected into every request as a query param automatically by `_prepare_params`.
- **`BaseParams`** — dataclass + `DataClassDictMixin` for query parameters. Serializes `bool → "true"/"false"`, `int/float → str`, `list → comma-separated string`; `None` values are dropped by `__post_serialize__`. Every API-specific params class extends this.
- **`BasePostData`** — dataclass + `DataClassDictMixin` for POST/PUT request bodies.
- **`Response`** — wraps `aiohttp.ClientResponse` and exposes `.deserialize(ModelClass)`, `.dict()`, `.text()`, `.bytes()`.

### Response deserialization

Models use `mashumaro`'s `DataClassORJSONMixin` for fast JSON deserialization. Call `await response.deserialize(SomeResponseModel)` to get a typed model instance.

### Testing pattern

Tests use `aresponses` to mock HTTP responses. Fixtures are JSON/PNG files in `tests/fixtures/`. The `json_response` and `image_response` pytest fixtures (in `conftest.py`) load fixture files and register them with `aresponses`. Test files mirror the `src` structure under `tests/`.

### Adding a new API endpoint

1. Add method to the relevant API class in `src/tomtom_apis/<category>/<api>.py`.
2. Add any new request/response models to the corresponding `models.py`.
3. Add a fixture JSON file to `tests/fixtures/`.
4. Add a test in `tests/<category>/test_<api>.py` using the `json_response` fixture.

## Linting Notes

- **Ruff** is configured with `select = ["ALL"]` — nearly every rule is on. Check `pyproject.toml` for per-file ignores (e.g., `S101` assertions allowed in tests, `T201` prints allowed in examples).
- **Docstrings** follow Google convention (`pydocstyle.convention = "google"`).
- `N803`/`N815` (non-lowercase/mixedCase names) are ignored globally to allow matching TomTom API field names exactly.
- `TC` (type-checking imports) is ignored because `mashumaro` requires types at runtime.
