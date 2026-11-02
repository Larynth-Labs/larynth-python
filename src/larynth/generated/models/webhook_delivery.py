from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.webhook_delivery_status import (
    WebhookDeliveryStatus,
    check_webhook_delivery_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define
class WebhookDelivery:
    """
    Attributes:
        attempt (int):
        created_at (datetime.datetime):
        event_id (UUID):
        event_type (str):
        id (UUID):
        status (WebhookDeliveryStatus):
        error (str | Unset):
        response_code (int | Unset):
        response_excerpt (str | Unset):
        response_ms (int | Unset):
    """

    attempt: int
    created_at: datetime.datetime
    event_id: UUID
    event_type: str
    id: UUID
    status: WebhookDeliveryStatus
    error: str | Unset = UNSET
    response_code: int | Unset = UNSET
    response_excerpt: str | Unset = UNSET
    response_ms: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attempt = self.attempt

        created_at = self.created_at.isoformat()

        event_id = str(self.event_id)

        event_type = self.event_type

        id = str(self.id)

        status: str = self.status

        error = self.error

        response_code = self.response_code

        response_excerpt = self.response_excerpt

        response_ms = self.response_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempt": attempt,
                "created_at": created_at,
                "event_id": event_id,
                "event_type": event_type,
                "id": id,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if response_code is not UNSET:
            field_dict["response_code"] = response_code
        if response_excerpt is not UNSET:
            field_dict["response_excerpt"] = response_excerpt
        if response_ms is not UNSET:
            field_dict["response_ms"] = response_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attempt = d.pop("attempt")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_id = UUID(d.pop("event_id"))

        event_type = d.pop("event_type")

        id = UUID(d.pop("id"))

        status = check_webhook_delivery_status(d.pop("status"))

        error = d.pop("error", UNSET)

        response_code = d.pop("response_code", UNSET)

        response_excerpt = d.pop("response_excerpt", UNSET)

        response_ms = d.pop("response_ms", UNSET)

        webhook_delivery = cls(
            attempt=attempt,
            created_at=created_at,
            event_id=event_id,
            event_type=event_type,
            id=id,
            status=status,
            error=error,
            response_code=response_code,
            response_excerpt=response_excerpt,
            response_ms=response_ms,
        )

        return webhook_delivery
