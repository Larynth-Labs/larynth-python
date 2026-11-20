from typing import Literal

CatalogVoiceQualityBasis = Literal["eval", "humanness", "wer"]

CATALOG_VOICE_QUALITY_BASIS_VALUES: set[CatalogVoiceQualityBasis] = {
    "eval",
    "humanness",
    "wer",
}


def check_catalog_voice_quality_basis(value: str) -> CatalogVoiceQualityBasis:
    if value in CATALOG_VOICE_QUALITY_BASIS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_VOICE_QUALITY_BASIS_VALUES!r}"
    )
