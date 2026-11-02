from typing import Literal

CatalogVoiceStatus = Literal["deprecated", "enabled"]

CATALOG_VOICE_STATUS_VALUES: set[CatalogVoiceStatus] = {
    "deprecated",
    "enabled",
}


def check_catalog_voice_status(value: str) -> CatalogVoiceStatus:
    if value in CATALOG_VOICE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_VOICE_STATUS_VALUES!r}"
    )
