from typing import Literal

WebCallRounding = Literal["started_minute"]

WEB_CALL_ROUNDING_VALUES: set[WebCallRounding] = {
    "started_minute",
}


def check_web_call_rounding(value: str) -> WebCallRounding:
    if value in WEB_CALL_ROUNDING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEB_CALL_ROUNDING_VALUES!r}"
    )
