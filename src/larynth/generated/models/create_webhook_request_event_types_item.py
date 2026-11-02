from typing import Literal

CreateWebhookRequestEventTypesItem = Literal[
    "billing.auto_top_up.failed",
    "billing.balance.low",
    "billing.top_up.succeeded",
    "call.analyzed",
    "call.answered",
    "call.ended",
    "call.recording.ready",
    "call.started",
    "call.transferred",
    "campaign.completed",
    "campaign.contact.completed",
    "campaign.paused",
    "campaign.started",
    "compliance.opt_out",
    "number.provisioned",
    "number.released",
]

CREATE_WEBHOOK_REQUEST_EVENT_TYPES_ITEM_VALUES: set[
    CreateWebhookRequestEventTypesItem
] = {
    "billing.auto_top_up.failed",
    "billing.balance.low",
    "billing.top_up.succeeded",
    "call.analyzed",
    "call.answered",
    "call.ended",
    "call.recording.ready",
    "call.started",
    "call.transferred",
    "campaign.completed",
    "campaign.contact.completed",
    "campaign.paused",
    "campaign.started",
    "compliance.opt_out",
    "number.provisioned",
    "number.released",
}


def check_create_webhook_request_event_types_item(
    value: str,
) -> CreateWebhookRequestEventTypesItem:
    if value in CREATE_WEBHOOK_REQUEST_EVENT_TYPES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBHOOK_REQUEST_EVENT_TYPES_ITEM_VALUES!r}"
    )
