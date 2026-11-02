from typing import Literal

CreateContactImportBodyConsentKind = Literal["express", "express_written"]

CREATE_CONTACT_IMPORT_BODY_CONSENT_KIND_VALUES: set[
    CreateContactImportBodyConsentKind
] = {
    "express",
    "express_written",
}


def check_create_contact_import_body_consent_kind(
    value: str,
) -> CreateContactImportBodyConsentKind:
    if value in CREATE_CONTACT_IMPORT_BODY_CONSENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_IMPORT_BODY_CONSENT_KIND_VALUES!r}"
    )
