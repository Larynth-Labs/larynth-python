from typing import Literal

ContactConsentSummary = Literal["express", "none", "opted_out", "written"]

CONTACT_CONSENT_SUMMARY_VALUES: set[ContactConsentSummary] = {
    "express",
    "none",
    "opted_out",
    "written",
}


def check_contact_consent_summary(value: str) -> ContactConsentSummary:
    if value in CONTACT_CONSENT_SUMMARY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_CONSENT_SUMMARY_VALUES!r}"
    )
