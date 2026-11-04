from typing import Literal

CreateWebhookReplayRequestStatus = Literal["all", "failed"]

CREATE_WEBHOOK_REPLAY_REQUEST_STATUS_VALUES: set[CreateWebhookReplayRequestStatus] = {
    "all",
    "failed",
}


def check_create_webhook_replay_request_status(
    value: str,
) -> CreateWebhookReplayRequestStatus:
    if value in CREATE_WEBHOOK_REPLAY_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBHOOK_REPLAY_REQUEST_STATUS_VALUES!r}"
    )
