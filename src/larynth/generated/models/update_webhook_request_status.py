from typing import Literal

UpdateWebhookRequestStatus = Literal["active", "disabled"]

UPDATE_WEBHOOK_REQUEST_STATUS_VALUES: set[UpdateWebhookRequestStatus] = {
    "active",
    "disabled",
}


def check_update_webhook_request_status(value: str) -> UpdateWebhookRequestStatus:
    if value in UPDATE_WEBHOOK_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WEBHOOK_REQUEST_STATUS_VALUES!r}"
    )
