from typing import Literal

IntegrationProviderResourceKind = Literal["calendar", "event_type"]

INTEGRATION_PROVIDER_RESOURCE_KIND_VALUES: set[IntegrationProviderResourceKind] = {
    "calendar",
    "event_type",
}


def check_integration_provider_resource_kind(
    value: str,
) -> IntegrationProviderResourceKind:
    if value in INTEGRATION_PROVIDER_RESOURCE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INTEGRATION_PROVIDER_RESOURCE_KIND_VALUES!r}"
    )
