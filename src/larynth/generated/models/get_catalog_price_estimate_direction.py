from typing import Literal

GetCatalogPriceEstimateDirection = Literal["inbound", "outbound", "web_test"]

GET_CATALOG_PRICE_ESTIMATE_DIRECTION_VALUES: set[GetCatalogPriceEstimateDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_get_catalog_price_estimate_direction(
    value: str,
) -> GetCatalogPriceEstimateDirection:
    if value in GET_CATALOG_PRICE_ESTIMATE_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CATALOG_PRICE_ESTIMATE_DIRECTION_VALUES!r}"
    )
