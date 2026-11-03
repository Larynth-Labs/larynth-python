from typing import Literal

AvailableNumberKind = Literal["local", "toll_free"]

AVAILABLE_NUMBER_KIND_VALUES: set[AvailableNumberKind] = {
    "local",
    "toll_free",
}


def check_available_number_kind(value: str) -> AvailableNumberKind:
    if value in AVAILABLE_NUMBER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AVAILABLE_NUMBER_KIND_VALUES!r}"
    )
