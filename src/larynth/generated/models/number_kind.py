from typing import Literal

NumberKind = Literal["local", "toll_free"]

NUMBER_KIND_VALUES: set[NumberKind] = {
    "local",
    "toll_free",
}


def check_number_kind(value: str) -> NumberKind:
    if value in NUMBER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_KIND_VALUES!r}"
    )
