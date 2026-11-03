from typing import Literal

CatalogModelTier = Literal["balanced", "best", "fast"]

CATALOG_MODEL_TIER_VALUES: set[CatalogModelTier] = {
    "balanced",
    "best",
    "fast",
}


def check_catalog_model_tier(value: str) -> CatalogModelTier:
    if value in CATALOG_MODEL_TIER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_MODEL_TIER_VALUES!r}"
    )
