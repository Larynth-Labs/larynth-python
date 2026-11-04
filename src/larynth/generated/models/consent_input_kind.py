from typing import Literal

ConsentInputKind = Literal["express", "express_written"]

CONSENT_INPUT_KIND_VALUES: set[ConsentInputKind] = {
    "express",
    "express_written",
}


def check_consent_input_kind(value: str) -> ConsentInputKind:
    if value in CONSENT_INPUT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONSENT_INPUT_KIND_VALUES!r}"
    )
