from typing import Literal

ContactImportConsentSource = Literal[
    "customer_agreement", "import", "other", "paper_form", "verbal_recorded", "web_form"
]

CONTACT_IMPORT_CONSENT_SOURCE_VALUES: set[ContactImportConsentSource] = {
    "customer_agreement",
    "import",
    "other",
    "paper_form",
    "verbal_recorded",
    "web_form",
}


def check_contact_import_consent_source(value: str) -> ContactImportConsentSource:
    if value in CONTACT_IMPORT_CONSENT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_IMPORT_CONSENT_SOURCE_VALUES!r}"
    )
