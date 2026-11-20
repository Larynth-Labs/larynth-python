from typing import Literal

CatalogVoiceLatencyBasis = Literal["lab", "live"]

CATALOG_VOICE_LATENCY_BASIS_VALUES: set[CatalogVoiceLatencyBasis] = {
    "lab",
    "live",
}


def check_catalog_voice_latency_basis(value: str) -> CatalogVoiceLatencyBasis:
    if value in CATALOG_VOICE_LATENCY_BASIS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_VOICE_LATENCY_BASIS_VALUES!r}"
    )
