from typing import Literal

CreateConsentRequestSource = Literal["api", "other", "verbal_recorded", "web_form"]

CREATE_CONSENT_REQUEST_SOURCE_VALUES: set[CreateConsentRequestSource] = {
    "api",
    "other",
    "verbal_recorded",
    "web_form",
}


def check_create_consent_request_source(value: str) -> CreateConsentRequestSource:
    if value in CREATE_CONSENT_REQUEST_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONSENT_REQUEST_SOURCE_VALUES!r}"
    )
