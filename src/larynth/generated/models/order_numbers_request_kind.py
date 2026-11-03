from typing import Literal

OrderNumbersRequestKind = Literal["local", "toll_free"]

ORDER_NUMBERS_REQUEST_KIND_VALUES: set[OrderNumbersRequestKind] = {
    "local",
    "toll_free",
}


def check_order_numbers_request_kind(value: str) -> OrderNumbersRequestKind:
    if value in ORDER_NUMBERS_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_NUMBERS_REQUEST_KIND_VALUES!r}"
    )
