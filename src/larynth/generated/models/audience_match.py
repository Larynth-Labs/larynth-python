from typing import Literal

AudienceMatch = Literal["all", "any"]

AUDIENCE_MATCH_VALUES: set[AudienceMatch] = {
    "all",
    "any",
}


def check_audience_match(value: str) -> AudienceMatch:
    if value in AUDIENCE_MATCH_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUDIENCE_MATCH_VALUES!r}"
    )
