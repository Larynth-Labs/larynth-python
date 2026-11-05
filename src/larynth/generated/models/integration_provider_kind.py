from typing import Literal

IntegrationProviderKind = Literal["cal_com", "google_calendar"]

INTEGRATION_PROVIDER_KIND_VALUES: set[IntegrationProviderKind] = {
    "cal_com",
    "google_calendar",
}


def check_integration_provider_kind(value: str) -> IntegrationProviderKind:
    if value in INTEGRATION_PROVIDER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INTEGRATION_PROVIDER_KIND_VALUES!r}"
    )
