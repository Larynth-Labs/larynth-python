from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.webhook_endpoint_status import (
    WebhookEndpointStatus,
    check_webhook_endpoint_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEndpoint")


@_attrs_define
class WebhookEndpoint:
    """
    Attributes:
        consecutive_failures (int):
        created_at (datetime.datetime):
        event_types (list[str]):
        id (UUID):
        status (WebhookEndpointStatus):
        updated_at (datetime.datetime):
        url (str):
        description (str | Unset):
        disabled_reason (str | Unset):
        previous_secret_expires_at (datetime.datetime | Unset):
    """

    consecutive_failures: int
    created_at: datetime.datetime
    event_types: list[str]
    id: UUID
    status: WebhookEndpointStatus
    updated_at: datetime.datetime
    url: str
    description: str | Unset = UNSET
    disabled_reason: str | Unset = UNSET
    previous_secret_expires_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        consecutive_failures = self.consecutive_failures

        created_at = self.created_at.isoformat()

        event_types = self.event_types

        id = str(self.id)

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        url = self.url

        description = self.description

        disabled_reason = self.disabled_reason

        previous_secret_expires_at: str | Unset = UNSET
        if not isinstance(self.previous_secret_expires_at, Unset):
            previous_secret_expires_at = self.previous_secret_expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "consecutive_failures": consecutive_failures,
                "created_at": created_at,
                "event_types": event_types,
                "id": id,
                "status": status,
                "updated_at": updated_at,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if disabled_reason is not UNSET:
            field_dict["disabled_reason"] = disabled_reason
        if previous_secret_expires_at is not UNSET:
            field_dict["previous_secret_expires_at"] = previous_secret_expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        consecutive_failures = d.pop("consecutive_failures")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_types = cast(list[str], d.pop("event_types"))

        id = UUID(d.pop("id"))

        status = check_webhook_endpoint_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        description = d.pop("description", UNSET)

        disabled_reason = d.pop("disabled_reason", UNSET)

        _previous_secret_expires_at = d.pop("previous_secret_expires_at", UNSET)
        previous_secret_expires_at: datetime.datetime | Unset
        if isinstance(_previous_secret_expires_at, Unset):
            previous_secret_expires_at = UNSET
        else:
            previous_secret_expires_at = datetime.datetime.fromisoformat(
                _previous_secret_expires_at
            )

        webhook_endpoint = cls(
            consecutive_failures=consecutive_failures,
            created_at=created_at,
            event_types=event_types,
            id=id,
            status=status,
            updated_at=updated_at,
            url=url,
            description=description,
            disabled_reason=disabled_reason,
            previous_secret_expires_at=previous_secret_expires_at,
        )

        return webhook_endpoint
