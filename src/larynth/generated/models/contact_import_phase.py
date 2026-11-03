from typing import Literal

ContactImportPhase = Literal["done", "failed", "importing", "validated", "validating"]

CONTACT_IMPORT_PHASE_VALUES: set[ContactImportPhase] = {
    "done",
    "failed",
    "importing",
    "validated",
    "validating",
}


def check_contact_import_phase(value: str) -> ContactImportPhase:
    if value in CONTACT_IMPORT_PHASE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_IMPORT_PHASE_VALUES!r}"
    )
