from typing import Literal

WebhookMessageStatus = Literal["delivered", "failed", "pending", "retrying"]

WEBHOOK_MESSAGE_STATUS_VALUES: set[WebhookMessageStatus] = {
    "delivered",
    "failed",
    "pending",
    "retrying",
}


def check_webhook_message_status(value: str) -> WebhookMessageStatus:
    if value in WEBHOOK_MESSAGE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_MESSAGE_STATUS_VALUES!r}"
    )
