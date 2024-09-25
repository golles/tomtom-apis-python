"""Generic models."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, StrEnum
from typing import Self

from mashumaro.mixins.orjson import DataClassORJSONMixin


class AdrCategoryType(StrEnum):
    """Supported ADR category types."""

    B = "B"
    C = "C"
    D = "D"
    E = "E"


class Language(StrEnum):
    """Supported languages for the Places API.

    For more information, see: https://developer.tomtom.com/search-api/documentation/product-information/supported-languages.
    """

    NGT = "NGT"  # Neutral Ground Truth, Official languages for all regions in local scripts if available.
    NGT_LATN = "NGT-Latn"  # Neutral Ground Truth - Latin exonyms, Latin script will be used if available.
    AF_ZA = "af-ZA"  # Afrikaans
    AR = "ar"  # Arabic
    EU_ES = "eu-ES"  # Basque
    BG_BG = "bg-BG"  # Bulgarian
    CA_ES = "ca-ES"  # Catalan (Spain)
    ZH_CN = "zh-CN"  # Chinese (PRC)
    ZH_TW = "zh-TW"  # Chinese (Taiwan)
    CS_CZ = "cs-CZ"  # Czech
    DA_DK = "da-DK"  # Danish
    NL_BE = "nl-BE"  # Dutch (Belgium)
    NL_NL = "nl-NL"  # Dutch
    EN_AU = "en-AU"  # English (Australia)
    EN_NZ = "en-NZ"  # English (New Zealand)
    EN_GB = "en-GB"  # English (Great Britain)
    EN_US = "en-US"  # English (USA)
    ET_EE = "et-EE"  # Estonian
    FI_FI = "fi-FI"  # Finnish
    FR_CA = "fr-CA"  # French (Canada)
    FR_FR = "fr-FR"  # French
    GL_ES = "gl-ES"  # Galician
    DE_DE = "de-DE"  # German
    EL_GR = "el-GR"  # Greek
    HR_HR = "hr-HR"  # Croatian
    HE_IL = "he-IL"  # Hebrew
    HU_HU = "hu-HU"  # Hungarian
    ID_ID = "id-ID"  # Indonesian
    IT_IT = "it-IT"  # Italian
    KK_KZ = "kk-KZ"  # Kazakh
    KO_KR = "ko-KR"  # Korean written in the Hangul script
    KO_LATN_KR = "ko-Latn-KR"  # Korean written in the Latin script
    KO_KORE_KR = "ko-Kore-KR"  # Korean written in the Hangul script
    LV_LV = "lv-LV"  # Latvian
    LT_LT = "lt-LT"  # Lithuanian
    MS_MY = "ms-MY"  # Malay
    NO_NO = "no-NO"  # Norwegian
    NB_NO = "nb-NO"  # Norwegian
    PL_PL = "pl-PL"  # Polish
    PT_BR = "pt-BR"  # Portuguese (Brazil)
    PT_PT = "pt-PT"  # Portuguese (Portugal)
    RO_RO = "ro-RO"  # Romanian
    RU_RU = "ru-RU"  # Russian written in the Cyrillic script
    RU_LATN_RU = "ru-Latn-RU"  # Russian written in the Latin script
    RU_CYRL_RU = "ru-Cyrl-RU"  # Russian written in the Cyrillic script
    SR_RS = "sr-RS"  # Serbian
    SK_SK = "sk-SK"  # Slovak
    SL_SI = "sl-SI"  # Slovenian
    ES_ES = "es-ES"  # Castilian Spanish
    ES_419 = "es-419"  # Latin American Spanish
    SV_SE = "sv-SE"  # Swedish
    TH_TH = "th-TH"  # Thai
    TR_TR = "tr-TR"  # Turkish
    UK_UA = "uk-UA"  # Ukrainian
    VI_VN = "vi-VN"  # Vietnamese


@dataclass(kw_only=True)
class LatLon(DataClassORJSONMixin):
    """Point location with abbreviated names.

    Attributes:
        lat (float): The latitude of the point.
        lon (float): The longitude of the point.

    """

    lat: float
    lon: float

    def to_comma_separated(self: Self) -> str:
        """Return the lat, lon as a comma-separated string.

        Returns:
            str: The lat, lon as a comma-separated string.

        """
        return ",".join(map(str, [self.lat, self.lon]))


@dataclass(kw_only=True)
class LatLonList(DataClassORJSONMixin):
    """Dataclass to handle a list of LatLon objects.

    Attributes:
        locations (list[LatLon]): The list of LatLon objects.

    """

    locations: list[LatLon]

    def to_colon_separated(self: Self) -> str:
        """Return the list of lat, lon as a colon-separated string.

        Returns:
            str: The list of lat, lon as a colon-separated string.

        """
        return ":".join([loc.to_comma_separated() for loc in self.locations])


@dataclass(kw_only=True)
class LatitudeLongitude(DataClassORJSONMixin):
    """Point location with full names.

    Attributes:
        latitude (float): The latitude of the point.
        longitude (float): The longitude of the point.

    """

    latitude: float
    longitude: float


@dataclass(kw_only=True)
class MapTile:
    """Map tile representation.

    Attributes:
        x (int): The x coordinate.
        y (int): The y coordinate.
        zoom (int): The zoom level

    """

    x: int
    y: int
    zoom: int


class TileSizeType(IntEnum):
    """Supported tile sizes."""

    SIZE_256 = 256
    SIZE_512 = 512


class TravelModeType(StrEnum):
    """Supported travel mode types."""

    CAR = "car"
    TRUCK = "truck"
    TAXI = "taxi"
    BUS = "bus"
    VAN = "van"
    MOTORCYCLE = "motorcycle"
    BICYCLE = "bicycle"
    PEDESTRIAN = "pedestrian"
    OTHER = "other"


class ViewType(StrEnum):
    """Geopolitical View.

    The context used to resolve the handling of disputed territories. Views include Unified, along with AR IL, IN, MA, PK, RU, TR, and CN which are
    respectively tailored for Argentina, Israel, India, Morocco, Pakistan, Russia, Turkey, and China.
    """

    UNIFIED = "Unified"
    AR = "AR"  # Argentina
    IL = "IL"  # Israel
    IN = "IN"  # India
    KR = "KR"  # Korea
    MA = "MA"  # Morocco
    PK = "PK"  # Pakistan
    RU = "RU"  # Russia
    TR = "TR"  # Turkey
    CN = "CN"  # China
