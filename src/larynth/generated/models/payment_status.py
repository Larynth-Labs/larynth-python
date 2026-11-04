from typing import Literal

PaymentStatus = Literal[
    "canceled", "disputed", "failed", "pending", "refunded", "succeeded", "under_review"
]

PAYMENT_STATUS_VALUES: set[PaymentStatus] = {
    "canceled",
    "disputed",
    "failed",
    "pending",
    "refunded",
    "succeeded",
    "under_review",
}


def check_payment_status(value: str) -> PaymentStatus:
    if value in PAYMENT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAYMENT_STATUS_VALUES!r}"
    )
