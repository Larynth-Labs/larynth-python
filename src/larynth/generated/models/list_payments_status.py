from typing import Literal

ListPaymentsStatus = Literal[
    "canceled", "disputed", "failed", "pending", "refunded", "succeeded", "under_review"
]

LIST_PAYMENTS_STATUS_VALUES: set[ListPaymentsStatus] = {
    "canceled",
    "disputed",
    "failed",
    "pending",
    "refunded",
    "succeeded",
    "under_review",
}


def check_list_payments_status(value: str) -> ListPaymentsStatus:
    if value in LIST_PAYMENTS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PAYMENTS_STATUS_VALUES!r}"
    )
