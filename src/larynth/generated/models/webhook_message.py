from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.webhook_message_status import (
    WebhookMessageStatus,
    check_webhook_message_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookMessage")


@_attrs_define
class WebhookMessage:
    """
    Attributes:
        attempts (int):
        created_at (datetime.datetime):
        event_id (UUID): Also the webhook-id header
        event_type (str):
        status (WebhookMessageStatus):
        test (bool):
        last_attempt_at (datetime.datetime | Unset):
        last_response_code (int | Unset):
        last_response_ms (int | Unset):
        next_attempt_at (datetime.datetime | Unset):
        redelivered_by_name (str | Unset):
    """

    attempts: int
    created_at: datetime.datetime
    event_id: UUID
    event_type: str
    status: WebhookMessageStatus
    test: bool
    last_attempt_at: datetime.datetime | Unset = UNSET
    last_response_code: int | Unset = UNSET
    last_response_ms: int | Unset = UNSET
    next_attempt_at: datetime.datetime | Unset = UNSET
    redelivered_by_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        created_at = self.created_at.isoformat()

        event_id = str(self.event_id)

        event_type = self.event_type

        status: str = self.status

        test = self.test

        last_attempt_at: str | Unset = UNSET
        if not isinstance(self.last_attempt_at, Unset):
            last_attempt_at = self.last_attempt_at.isoformat()

        last_response_code = self.last_response_code

        last_response_ms = self.last_response_ms

        next_attempt_at: str | Unset = UNSET
        if not isinstance(self.next_attempt_at, Unset):
            next_attempt_at = self.next_attempt_at.isoformat()

        redelivered_by_name = self.redelivered_by_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts": attempts,
                "created_at": created_at,
                "event_id": event_id,
                "event_type": event_type,
                "status": status,
                "test": test,
            }
        )
        if last_attempt_at is not UNSET:
            field_dict["last_attempt_at"] = last_attempt_at
        if last_response_code is not UNSET:
            field_dict["last_response_code"] = last_response_code
        if last_response_ms is not UNSET:
            field_dict["last_response_ms"] = last_response_ms
        if next_attempt_at is not UNSET:
            field_dict["next_attempt_at"] = next_attempt_at
        if redelivered_by_name is not UNSET:
            field_dict["redelivered_by_name"] = redelivered_by_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_id = UUID(d.pop("event_id"))

        event_type = d.pop("event_type")

        status = check_webhook_message_status(d.pop("status"))

        test = d.pop("test")

        _last_attempt_at = d.pop("last_attempt_at", UNSET)
        last_attempt_at: datetime.datetime | Unset
        if isinstance(_last_attempt_at, Unset):
            last_attempt_at = UNSET
        else:
            last_attempt_at = datetime.datetime.fromisoformat(_last_attempt_at)

        last_response_code = d.pop("last_response_code", UNSET)

        last_response_ms = d.pop("last_response_ms", UNSET)

        _next_attempt_at = d.pop("next_attempt_at", UNSET)
        next_attempt_at: datetime.datetime | Unset
        if isinstance(_next_attempt_at, Unset):
            next_attempt_at = UNSET
        else:
            next_attempt_at = datetime.datetime.fromisoformat(_next_attempt_at)

        redelivered_by_name = d.pop("redelivered_by_name", UNSET)

        webhook_message = cls(
            attempts=attempts,
            created_at=created_at,
            event_id=event_id,
            event_type=event_type,
            status=status,
            test=test,
            last_attempt_at=last_attempt_at,
            last_response_code=last_response_code,
            last_response_ms=last_response_ms,
            next_attempt_at=next_attempt_at,
            redelivered_by_name=redelivered_by_name,
        )

        return webhook_message
