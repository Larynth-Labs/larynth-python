from typing import Literal

CreateConsentRequestKind = Literal["express", "express_written"]

CREATE_CONSENT_REQUEST_KIND_VALUES: set[CreateConsentRequestKind] = {
    "express",
    "express_written",
}


def check_create_consent_request_kind(value: str) -> CreateConsentRequestKind:
    if value in CREATE_CONSENT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONSENT_REQUEST_KIND_VALUES!r}"
    )
