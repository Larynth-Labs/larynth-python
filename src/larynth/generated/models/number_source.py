from typing import Literal

NumberSource = Literal["byo_sip", "larynth"]

NUMBER_SOURCE_VALUES: set[NumberSource] = {
    "byo_sip",
    "larynth",
}


def check_number_source(value: str) -> NumberSource:
    if value in NUMBER_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_SOURCE_VALUES!r}"
    )
