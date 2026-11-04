from typing import Literal

CreateContactImportBodyCoversMarketing = Literal["false", "true"]

CREATE_CONTACT_IMPORT_BODY_COVERS_MARKETING_VALUES: set[
    CreateContactImportBodyCoversMarketing
] = {
    "false",
    "true",
}


def check_create_contact_import_body_covers_marketing(
    value: str,
) -> CreateContactImportBodyCoversMarketing:
    if value in CREATE_CONTACT_IMPORT_BODY_COVERS_MARKETING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_IMPORT_BODY_COVERS_MARKETING_VALUES!r}"
    )
