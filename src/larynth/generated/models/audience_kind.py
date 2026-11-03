from typing import Literal

AudienceKind = Literal["contacts", "import", "tags"]

AUDIENCE_KIND_VALUES: set[AudienceKind] = {
    "contacts",
    "import",
    "tags",
}


def check_audience_kind(value: str) -> AudienceKind:
    if value in AUDIENCE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUDIENCE_KIND_VALUES!r}"
    )
