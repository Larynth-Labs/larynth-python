from typing import Literal

ConsentSource = Literal[
    "api",
    "customer_agreement",
    "import",
    "other",
    "paper_form",
    "verbal_recorded",
    "web_form",
]

CONSENT_SOURCE_VALUES: set[ConsentSource] = {
    "api",
    "customer_agreement",
    "import",
    "other",
    "paper_form",
    "verbal_recorded",
    "web_form",
}


def check_consent_source(value: str) -> ConsentSource:
    if value in CONSENT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONSENT_SOURCE_VALUES!r}"
    )
