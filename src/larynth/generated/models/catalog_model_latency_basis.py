from typing import Literal

CatalogModelLatencyBasis = Literal["measured", "seeded"]

CATALOG_MODEL_LATENCY_BASIS_VALUES: set[CatalogModelLatencyBasis] = {
    "measured",
    "seeded",
}


def check_catalog_model_latency_basis(value: str) -> CatalogModelLatencyBasis:
    if value in CATALOG_MODEL_LATENCY_BASIS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_MODEL_LATENCY_BASIS_VALUES!r}"
    )
