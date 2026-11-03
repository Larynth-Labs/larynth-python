from typing import Literal

SearchAvailableNumbersKind = Literal["local", "toll_free"]

SEARCH_AVAILABLE_NUMBERS_KIND_VALUES: set[SearchAvailableNumbersKind] = {
    "local",
    "toll_free",
}


def check_search_available_numbers_kind(value: str) -> SearchAvailableNumbersKind:
    if value in SEARCH_AVAILABLE_NUMBERS_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_AVAILABLE_NUMBERS_KIND_VALUES!r}"
    )
