from typing import Literal

LaunchPriceAppliesToItem = Literal["call_minute"]

LAUNCH_PRICE_APPLIES_TO_ITEM_VALUES: set[LaunchPriceAppliesToItem] = {
    "call_minute",
}


def check_launch_price_applies_to_item(value: str) -> LaunchPriceAppliesToItem:
    if value in LAUNCH_PRICE_APPLIES_TO_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LAUNCH_PRICE_APPLIES_TO_ITEM_VALUES!r}"
    )
