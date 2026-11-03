from typing import Literal

ContactLastCallDirection = Literal["inbound", "outbound", "web_test"]

CONTACT_LAST_CALL_DIRECTION_VALUES: set[ContactLastCallDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_contact_last_call_direction(value: str) -> ContactLastCallDirection:
    if value in CONTACT_LAST_CALL_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_LAST_CALL_DIRECTION_VALUES!r}"
    )
