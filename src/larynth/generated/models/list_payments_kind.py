from typing import Literal

ListPaymentsKind = Literal["auto_top_up", "bundle", "top_up"]

LIST_PAYMENTS_KIND_VALUES: set[ListPaymentsKind] = {
    "auto_top_up",
    "bundle",
    "top_up",
}


def check_list_payments_kind(value: str) -> ListPaymentsKind:
    if value in LIST_PAYMENTS_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PAYMENTS_KIND_VALUES!r}"
    )
