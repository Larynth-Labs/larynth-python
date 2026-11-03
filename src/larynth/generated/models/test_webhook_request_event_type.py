from typing import Literal

TestWebhookRequestEventType = Literal[
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
    "notification.billing.auto_top_up_failed",
    "notification.billing.balance_low",
    "notification.billing.top_up_succeeded",
    "notification.call.summary",
    "notification.campaign.completed",
    "notification.campaign.paused",
    "notification.compliance.optout_alert",
    "notification.number.provisioned",
    "notification.number.released",
    "notification.spending_request.created",
    "number.provisioned",
    "number.released",
]

TEST_WEBHOOK_REQUEST_EVENT_TYPE_VALUES: set[TestWebhookRequestEventType] = {
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
    "notification.billing.auto_top_up_failed",
    "notification.billing.balance_low",
    "notification.billing.top_up_succeeded",
    "notification.call.summary",
    "notification.campaign.completed",
    "notification.campaign.paused",
    "notification.compliance.optout_alert",
    "notification.number.provisioned",
    "notification.number.released",
    "notification.spending_request.created",
    "number.provisioned",
    "number.released",
}


def check_test_webhook_request_event_type(value: str) -> TestWebhookRequestEventType:
    if value in TEST_WEBHOOK_REQUEST_EVENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TEST_WEBHOOK_REQUEST_EVENT_TYPE_VALUES!r}"
    )
