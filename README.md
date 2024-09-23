# TomTom APIs Python

[![PyPI version][pypi_badge]][pypi_link]
[![License][license_badge]][license_link]
[![Codecov][codecov_badge]][codecov_link]
[![Sonar quality gate][sonar_badge]][sonar_link]
[![GitHub repo stars][stars_badge]][stars_link]
[![Buy me a coffee][buymecoffee_badge]][buymecoffee_link]

Asynchronous Python client for the TomTom APIs

## API Coverage

This section provides an overview of the APIs implemented by the client and their typing status.

### Automotive APIs

| API                      | Notes           |
| ------------------------ | --------------- |
| Autostream               | Not implemented |
| Fuel Prices API          | Typed           |
| Parking Availability API | Typed           |

### Maps API

| API             | Notes                                                                            |
| --------------- | -------------------------------------------------------------------------------- |
| Map Display API | Typed, `WMS`, `WMTS`, `Map Styles` and `Map Styles v2` have not been implemented |

### Places APIs

| API                   | Notes |
| --------------------- | ----- |
| Batch Search API      | Typed |
| EV Search API         | Typed |
| Geocoding API         | Typed |
| Premium Geocoding API | Typed |
| Reverse Geocoding API | Typed |
| Search API            | Typed |

### Routing APIs

| API                          | Notes           |
| ---------------------------- | --------------- |
| Long Distance EV Routing API | Typed           |
| Matrix Routing v2 API        | Not implemented |
| Routing API                  | Typed           |
| Waypoint Optimization API    | Typed           |

### Tracking & Logistics APIs

| API                  | Notes           |
| -------------------- | --------------- |
| Geofencing API       | Not implemented |
| Location History API | Not implemented |
| Notifications API    | Not implemented |
| Snap to Roads API    | Not implemented |

### Traffic APIs

| API                      | Notes                                                             |
| ------------------------ | ----------------------------------------------------------------- |
| Intermediate Traffic API | Not implemented                                                   |
| Junction Analytics API   | Not implemented                                                   |
| O/D Analytics API        | Not implemented                                                   |
| Route Monitoring API     | Not implemented                                                   |
| Traffic API              | Typed, `Map Styles` and `Map Styles v2` have not been implemented |
| Traffic Stats API        | Not implemented                                                   |

## Installation

You can install this package via your favorite package manager. For example, using pip:

```sh
pip install tomtom-apis
```

## Examples

You can find usage examples in the [examples directory](examples).

## Contributing

Your contributions are welcome! Please familiarize yourself with the [contribution guidelines](CONTRIBUTING.md). This document also helps you set up your development environment.

---

Thank you for your interest in the TomTom API Python client! If you have any questions or need further assistance, feel free to open an issue or submit a pull request.

[pypi_link]: https://pypi.org/project/tomtom-apis/
[pypi_badge]: https://img.shields.io/pypi/v/tomtom-apis?style=for-the-badge
[license_link]: https://github.com/golles/tomtom-apis-python/blob/main/LICENSE
[license_badge]: https://img.shields.io/github/license/golles/tomtom-apis-python.svg?style=for-the-badge
[codecov_link]: https://app.codecov.io/gh/golles/tomtom-apis-python
[codecov_badge]: https://img.shields.io/codecov/c/github/golles/tomtom-apis-python?style=for-the-badge
[sonar_link]: https://sonarcloud.io/project/overview?id=golles_tomtom-apis-python
[sonar_badge]: https://img.shields.io/sonar/quality_gate/golles_tomtom-apis-python?server=https%3A%2F%2Fsonarcloud.io&style=for-the-badge
[stars_link]: https://github.com/golles/tomtom-apis-python/stargazers
[stars_badge]: https://img.shields.io/github/stars/golles/tomtom-apis-python?style=for-the-badge
[buymecoffee_link]: https://www.buymeacoffee.com/golles
[buymecoffee_badge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
