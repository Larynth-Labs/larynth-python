from typing import Literal

ContactImportMode = Literal["commit", "validate"]

CONTACT_IMPORT_MODE_VALUES: set[ContactImportMode] = {
    "commit",
    "validate",
}


def check_contact_import_mode(value: str) -> ContactImportMode:
    if value in CONTACT_IMPORT_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_IMPORT_MODE_VALUES!r}"
    )
