from typing import Literal

ContactSource = Literal["api", "import", "inbound_call", "manual"]

CONTACT_SOURCE_VALUES: set[ContactSource] = {
    "api",
    "import",
    "inbound_call",
    "manual",
}


def check_contact_source(value: str) -> ContactSource:
    if value in CONTACT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_SOURCE_VALUES!r}"
    )
