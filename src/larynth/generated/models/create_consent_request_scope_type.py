from typing import Literal

CreateConsentRequestScopeType = Literal["campaign", "tenant"]

CREATE_CONSENT_REQUEST_SCOPE_TYPE_VALUES: set[CreateConsentRequestScopeType] = {
    "campaign",
    "tenant",
}


def check_create_consent_request_scope_type(
    value: str,
) -> CreateConsentRequestScopeType:
    if value in CREATE_CONSENT_REQUEST_SCOPE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONSENT_REQUEST_SCOPE_TYPE_VALUES!r}"
    )
