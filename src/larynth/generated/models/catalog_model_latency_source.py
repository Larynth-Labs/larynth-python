from typing import Literal

CatalogModelLatencySource = Literal["lab", "live"]

CATALOG_MODEL_LATENCY_SOURCE_VALUES: set[CatalogModelLatencySource] = {
    "lab",
    "live",
}


def check_catalog_model_latency_source(value: str) -> CatalogModelLatencySource:
    if value in CATALOG_MODEL_LATENCY_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_MODEL_LATENCY_SOURCE_VALUES!r}"
    )
