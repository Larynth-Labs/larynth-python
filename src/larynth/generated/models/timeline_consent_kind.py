from typing import Literal

TimelineConsentKind = Literal["express", "express_written"]

TIMELINE_CONSENT_KIND_VALUES: set[TimelineConsentKind] = {
    "express",
    "express_written",
}


def check_timeline_consent_kind(value: str) -> TimelineConsentKind:
    if value in TIMELINE_CONSENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TIMELINE_CONSENT_KIND_VALUES!r}"
    )
