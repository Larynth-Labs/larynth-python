from typing import Literal

ConsentInputSource = Literal[
    "customer_agreement", "other", "paper_form", "verbal_recorded", "web_form"
]

CONSENT_INPUT_SOURCE_VALUES: set[ConsentInputSource] = {
    "customer_agreement",
    "other",
    "paper_form",
    "verbal_recorded",
    "web_form",
}


def check_consent_input_source(value: str) -> ConsentInputSource:
    if value in CONSENT_INPUT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONSENT_INPUT_SOURCE_VALUES!r}"
    )
