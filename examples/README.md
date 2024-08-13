# Examples

This folder contains various examples of using the APIs, organized into subfolders. Below are some generic use cases illustrated with code snippets.

## Constructing Params and PostData Models

These dataclasses extend the `DataClassDictMixin` from [Mashumaro](https://github.com/Fatal1ty/mashumaro) and can be constructed in several ways.

```python
from tomtom_apis.maps.models import MapTileParams
from tomtom_apis.models import Language, TileSizeType, ViewType


# Instantiating with class attributes
class_instantiation = MapTileParams(
    tileSize=TileSizeType.SIZE_256,
    view=ViewType.UNIFIED,
    language=Language.EN_US,
)

# Instantiating from a dictionary
dict_instantiation = MapTileParams.from_dict({
    "tileSize": 256,
    "view": "Unified",
    "language": "en-US",
})

# Ensuring both instances are equivalent
assert class_instantiation == dict_instantiation
```

## Logging

You can configure the logging for this module as follows:

```python
import logging


# Set the logging level to WARNING
logging.basicConfig(level=logging.WARNING)

# Set the logging level for tomtom_apis to INFO
logging.getLogger("tomtom_apis").setLevel(logging.INFO)
```

## Sharing ClientSession Between APIs

To use the same `aiohttp.client.ClientSession` across multiple APIs, you can inject a session from one API into another:

```python
from tomtom_apis import ApiOptions
from tomtom_apis.maps import MapDisplayApi
from tomtom_apis.traffic import TrafficApi


options = ApiOptions(api_key="secret")

# Create an instance of MapDisplayApi
map_display_api = MapDisplayApi(options)

# Share the session with TrafficApi
traffic_api = TrafficApi(options, map_display_api.session)
```
