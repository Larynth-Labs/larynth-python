from typing import Literal

AlertDeliveryChannel = Literal[
    "email", "in_app", "push", "slack", "sms", "telegram", "webhook"
]

ALERT_DELIVERY_CHANNEL_VALUES: set[AlertDeliveryChannel] = {
    "email",
    "in_app",
    "push",
    "slack",
    "sms",
    "telegram",
    "webhook",
}


def check_alert_delivery_channel(value: str) -> AlertDeliveryChannel:
    if value in ALERT_DELIVERY_CHANNEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_DELIVERY_CHANNEL_VALUES!r}"
    )
