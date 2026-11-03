from typing import Literal

ListNumbersKind = Literal["local", "toll_free"]

LIST_NUMBERS_KIND_VALUES: set[ListNumbersKind] = {
    "local",
    "toll_free",
}


def check_list_numbers_kind(value: str) -> ListNumbersKind:
    if value in LIST_NUMBERS_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_NUMBERS_KIND_VALUES!r}"
    )
