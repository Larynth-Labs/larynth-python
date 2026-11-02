from typing import Literal

CatalogModelKind = Literal["embedding", "llm", "s2s", "stt", "tts"]

CATALOG_MODEL_KIND_VALUES: set[CatalogModelKind] = {
    "embedding",
    "llm",
    "s2s",
    "stt",
    "tts",
}


def check_catalog_model_kind(value: str) -> CatalogModelKind:
    if value in CATALOG_MODEL_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_MODEL_KIND_VALUES!r}"
    )
