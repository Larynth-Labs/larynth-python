from typing import Literal

ListWebhookMessagesStatus = Literal["delivered", "failed", "pending", "retrying"]

LIST_WEBHOOK_MESSAGES_STATUS_VALUES: set[ListWebhookMessagesStatus] = {
    "delivered",
    "failed",
    "pending",
    "retrying",
}


def check_list_webhook_messages_status(value: str) -> ListWebhookMessagesStatus:
    if value in LIST_WEBHOOK_MESSAGES_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOK_MESSAGES_STATUS_VALUES!r}"
    )
