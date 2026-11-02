from typing import Literal

ConsentScopeType = Literal["campaign", "tenant"]

CONSENT_SCOPE_TYPE_VALUES: set[ConsentScopeType] = {
    "campaign",
    "tenant",
}


def check_consent_scope_type(value: str) -> ConsentScopeType:
    if value in CONSENT_SCOPE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONSENT_SCOPE_TYPE_VALUES!r}"
    )
