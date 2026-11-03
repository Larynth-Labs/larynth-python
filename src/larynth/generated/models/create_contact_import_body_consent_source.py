from typing import Literal

CreateContactImportBodyConsentSource = Literal[
    "customer_agreement", "import", "other", "paper_form", "verbal_recorded", "web_form"
]

CREATE_CONTACT_IMPORT_BODY_CONSENT_SOURCE_VALUES: set[
    CreateContactImportBodyConsentSource
] = {
    "customer_agreement",
    "import",
    "other",
    "paper_form",
    "verbal_recorded",
    "web_form",
}


def check_create_contact_import_body_consent_source(
    value: str,
) -> CreateContactImportBodyConsentSource:
    if value in CREATE_CONTACT_IMPORT_BODY_CONSENT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_IMPORT_BODY_CONSENT_SOURCE_VALUES!r}"
    )
