from typing import Literal

ListCallsBilled = Literal["billed", "not_billed"]

LIST_CALLS_BILLED_VALUES: set[ListCallsBilled] = {
    "billed",
    "not_billed",
}


def check_list_calls_billed(value: str) -> ListCallsBilled:
    if value in LIST_CALLS_BILLED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CALLS_BILLED_VALUES!r}"
    )
