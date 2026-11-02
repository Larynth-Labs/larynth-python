from typing import Literal

ContactImportStatus = Literal["done", "failed", "processing", "uploaded"]

CONTACT_IMPORT_STATUS_VALUES: set[ContactImportStatus] = {
    "done",
    "failed",
    "processing",
    "uploaded",
}


def check_contact_import_status(value: str) -> ContactImportStatus:
    if value in CONTACT_IMPORT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_IMPORT_STATUS_VALUES!r}"
    )
