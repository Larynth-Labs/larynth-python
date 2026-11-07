from typing import Literal

PaymentKind = Literal["auto_top_up", "bundle", "top_up"]

PAYMENT_KIND_VALUES: set[PaymentKind] = {
    "auto_top_up",
    "bundle",
    "top_up",
}


def check_payment_kind(value: str) -> PaymentKind:
    if value in PAYMENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAYMENT_KIND_VALUES!r}"
    )
