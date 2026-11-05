from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.create_webhook_replay_request_status import (
    CreateWebhookReplayRequestStatus,
    check_create_webhook_replay_request_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookReplayRequest")


@_attrs_define
class CreateWebhookReplayRequest:
    """
    Attributes:
        since (datetime.datetime): At most 7 days ago
        status (CreateWebhookReplayRequestStatus | Unset):  Default: 'failed'.
    """

    since: datetime.datetime
    status: CreateWebhookReplayRequestStatus | Unset = "failed"

    def to_dict(self) -> dict[str, Any]:
        since = self.since.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "since": since,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        since = datetime.datetime.fromisoformat(d.pop("since"))

        _status = d.pop("status", UNSET)
        status: CreateWebhookReplayRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_create_webhook_replay_request_status(_status)

        create_webhook_replay_request = cls(
            since=since,
            status=status,
        )

        return create_webhook_replay_request
