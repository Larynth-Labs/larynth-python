from typing import Literal

WebhookDeliveryStatus = Literal["failed", "retrying", "succeeded"]

WEBHOOK_DELIVERY_STATUS_VALUES: set[WebhookDeliveryStatus] = {
    "failed",
    "retrying",
    "succeeded",
}


def check_webhook_delivery_status(value: str) -> WebhookDeliveryStatus:
    if value in WEBHOOK_DELIVERY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_STATUS_VALUES!r}"
    )
