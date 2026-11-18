from typing import Literal

AlertDeliveryStatus = Literal["failed", "sent", "skipped"]

ALERT_DELIVERY_STATUS_VALUES: set[AlertDeliveryStatus] = {
    "failed",
    "sent",
    "skipped",
}


def check_alert_delivery_status(value: str) -> AlertDeliveryStatus:
    if value in ALERT_DELIVERY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_DELIVERY_STATUS_VALUES!r}"
    )
