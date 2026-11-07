from typing import Literal

PaymentMethodUsedByItem = Literal["auto_top_up", "bundle"]

PAYMENT_METHOD_USED_BY_ITEM_VALUES: set[PaymentMethodUsedByItem] = {
    "auto_top_up",
    "bundle",
}


def check_payment_method_used_by_item(value: str) -> PaymentMethodUsedByItem:
    if value in PAYMENT_METHOD_USED_BY_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAYMENT_METHOD_USED_BY_ITEM_VALUES!r}"
    )
