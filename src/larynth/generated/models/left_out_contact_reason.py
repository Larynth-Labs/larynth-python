from typing import Literal

LeftOutContactReason = Literal["dnc", "no_consent", "no_timezone", "not_us"]

LEFT_OUT_CONTACT_REASON_VALUES: set[LeftOutContactReason] = {
    "dnc",
    "no_consent",
    "no_timezone",
    "not_us",
}


def check_left_out_contact_reason(value: str) -> LeftOutContactReason:
    if value in LEFT_OUT_CONTACT_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LEFT_OUT_CONTACT_REASON_VALUES!r}"
    )
