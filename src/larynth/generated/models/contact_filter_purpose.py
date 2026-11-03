from typing import Literal

ContactFilterPurpose = Literal["informational", "telemarketing"]

CONTACT_FILTER_PURPOSE_VALUES: set[ContactFilterPurpose] = {
    "informational",
    "telemarketing",
}


def check_contact_filter_purpose(value: str) -> ContactFilterPurpose:
    if value in CONTACT_FILTER_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_FILTER_PURPOSE_VALUES!r}"
    )
