from typing import Literal

CatalogModelStatus = Literal["deprecated", "enabled"]

CATALOG_MODEL_STATUS_VALUES: set[CatalogModelStatus] = {
    "deprecated",
    "enabled",
}


def check_catalog_model_status(value: str) -> CatalogModelStatus:
    if value in CATALOG_MODEL_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOG_MODEL_STATUS_VALUES!r}"
    )
