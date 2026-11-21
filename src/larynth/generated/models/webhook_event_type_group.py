from typing import Literal

WebhookEventTypeGroup = Literal[
    "agents",
    "billing",
    "bookings",
    "calls",
    "campaigns",
    "compliance",
    "inbox",
    "integrations",
    "issues",
    "knowledge",
    "notifications",
    "numbers",
    "tools",
]

WEBHOOK_EVENT_TYPE_GROUP_VALUES: set[WebhookEventTypeGroup] = {
    "agents",
    "billing",
    "bookings",
    "calls",
    "campaigns",
    "compliance",
    "inbox",
    "integrations",
    "issues",
    "knowledge",
    "notifications",
    "numbers",
    "tools",
}


def check_webhook_event_type_group(value: str) -> WebhookEventTypeGroup:
    if value in WEBHOOK_EVENT_TYPE_GROUP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_EVENT_TYPE_GROUP_VALUES!r}"
    )
