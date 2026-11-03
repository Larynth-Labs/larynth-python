from typing import Literal

DncImportStatus = Literal["done", "failed", "queued", "running"]

DNC_IMPORT_STATUS_VALUES: set[DncImportStatus] = {
    "done",
    "failed",
    "queued",
    "running",
}


def check_dnc_import_status(value: str) -> DncImportStatus:
    if value in DNC_IMPORT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNC_IMPORT_STATUS_VALUES!r}"
    )
