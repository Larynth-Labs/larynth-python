from typing import Literal

ListCatalogModelsSort = Literal["latency", "price", "quality"]

LIST_CATALOG_MODELS_SORT_VALUES: set[ListCatalogModelsSort] = {
    "latency",
    "price",
    "quality",
}


def check_list_catalog_models_sort(value: str) -> ListCatalogModelsSort:
    if value in LIST_CATALOG_MODELS_SORT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_MODELS_SORT_VALUES!r}"
    )
