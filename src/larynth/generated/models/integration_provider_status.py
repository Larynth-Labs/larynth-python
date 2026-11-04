from typing import Literal

IntegrationProviderStatus = Literal["disabled", "enabled"]

INTEGRATION_PROVIDER_STATUS_VALUES: set[IntegrationProviderStatus] = {
    "disabled",
    "enabled",
}


def check_integration_provider_status(value: str) -> IntegrationProviderStatus:
    if value in INTEGRATION_PROVIDER_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INTEGRATION_PROVIDER_STATUS_VALUES!r}"
    )
