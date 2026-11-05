from typing import Literal

IntegrationProviderAuth = Literal["api_key", "oauth"]

INTEGRATION_PROVIDER_AUTH_VALUES: set[IntegrationProviderAuth] = {
    "api_key",
    "oauth",
}


def check_integration_provider_auth(value: str) -> IntegrationProviderAuth:
    if value in INTEGRATION_PROVIDER_AUTH_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INTEGRATION_PROVIDER_AUTH_VALUES!r}"
    )
