from typing import Literal

ListCatalogModelsKind = Literal["embedding", "llm", "s2s", "stt", "tts"]

LIST_CATALOG_MODELS_KIND_VALUES: set[ListCatalogModelsKind] = {
    "embedding",
    "llm",
    "s2s",
    "stt",
    "tts",
}


def check_list_catalog_models_kind(value: str) -> ListCatalogModelsKind:
    if value in LIST_CATALOG_MODELS_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_MODELS_KIND_VALUES!r}"
    )
