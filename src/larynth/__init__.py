from .generated import AuthenticatedClient, Client
from .webhooks import (
    DEFAULT_TOLERANCE_SECONDS,
    SECRET_PREFIX,
    WebhookVerificationError,
    sign,
    verify,
)

__all__ = [
    "AuthenticatedClient",
    "Client",
    "DEFAULT_TOLERANCE_SECONDS",
    "SECRET_PREFIX",
    "WebhookVerificationError",
    "authenticated_client",
    "sign",
    "verify",
]


def authenticated_client(api_key: str, base_url: str) -> AuthenticatedClient:
    return AuthenticatedClient(base_url=base_url, token=api_key, raise_on_unexpected_status=True)
