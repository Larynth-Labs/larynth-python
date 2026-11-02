from typing import Literal

ConsentKind = Literal["express", "express_written"]

CONSENT_KIND_VALUES: set[ConsentKind] = {
    "express",
    "express_written",
}


def check_consent_kind(value: str) -> ConsentKind:
    if value in CONSENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONSENT_KIND_VALUES!r}"
    )
