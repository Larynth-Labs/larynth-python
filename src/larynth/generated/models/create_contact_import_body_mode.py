from typing import Literal

CreateContactImportBodyMode = Literal["commit", "validate"]

CREATE_CONTACT_IMPORT_BODY_MODE_VALUES: set[CreateContactImportBodyMode] = {
    "commit",
    "validate",
}


def check_create_contact_import_body_mode(value: str) -> CreateContactImportBodyMode:
    if value in CREATE_CONTACT_IMPORT_BODY_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_IMPORT_BODY_MODE_VALUES!r}"
    )
