from typing import Literal

CatalogModelQualityBasis = Literal["eval", "humanness", "wer"]

CATALOG_MODEL_QUALITY_BASIS_VALUES: set[CatalogModelQualityBasis] = {
    "eval",
    "humanness",
    "wer",
}


def check_catalog_model_quality_basis(value: str) -> CatalogModelQualityBasis:
    if value in CATALOG_MODEL_QUALITY_BASIS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_MODEL_QUALITY_BASIS_VALUES!r}"
    )
