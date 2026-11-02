from typing import Literal

ContactImportConsentKind = Literal["express", "express_written"]

CONTACT_IMPORT_CONSENT_KIND_VALUES: set[ContactImportConsentKind] = {
    "express",
    "express_written",
}


def check_contact_import_consent_kind(value: str) -> ContactImportConsentKind:
    if value in CONTACT_IMPORT_CONSENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_IMPORT_CONSENT_KIND_VALUES!r}"
    )
