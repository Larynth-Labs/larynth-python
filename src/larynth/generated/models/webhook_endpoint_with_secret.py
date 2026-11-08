from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.webhook_endpoint_with_secret_status import (
    WebhookEndpointWithSecretStatus,
    check_webhook_endpoint_with_secret_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_stats import WebhookStats


T = TypeVar("T", bound="WebhookEndpointWithSecret")


@_attrs_define
class WebhookEndpointWithSecret:
    """
    Attributes:
        consecutive_failures (int):
        created_at (datetime.datetime):
        event_types (list[str]):
        id (UUID):
        secret (str): Standard Webhooks signing secret (whsec_<base64>); returned only once
        stats_24h (WebhookStats):
        status (WebhookEndpointWithSecretStatus):
        updated_at (datetime.datetime):
        url (str):
        description (str | Unset):
        disabled_reason (str | Unset):
        previous_secret_expires_at (datetime.datetime | Unset):
        secret_hint (str | Unset): Last 4 characters of the current signing secret
    """

    consecutive_failures: int
    created_at: datetime.datetime
    event_types: list[str]
    id: UUID
    secret: str
    stats_24h: WebhookStats
    status: WebhookEndpointWithSecretStatus
    updated_at: datetime.datetime
    url: str
    description: str | Unset = UNSET
    disabled_reason: str | Unset = UNSET
    previous_secret_expires_at: datetime.datetime | Unset = UNSET
    secret_hint: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        consecutive_failures = self.consecutive_failures

        created_at = self.created_at.isoformat()

        event_types = self.event_types

        id = str(self.id)

        secret = self.secret

        stats_24h = self.stats_24h.to_dict()

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        url = self.url

        description = self.description

        disabled_reason = self.disabled_reason

        previous_secret_expires_at: str | Unset = UNSET
        if not isinstance(self.previous_secret_expires_at, Unset):
            previous_secret_expires_at = self.previous_secret_expires_at.isoformat()

        secret_hint = self.secret_hint

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "consecutive_failures": consecutive_failures,
                "created_at": created_at,
                "event_types": event_types,
                "id": id,
                "secret": secret,
                "stats_24h": stats_24h,
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
        if secret_hint is not UNSET:
            field_dict["secret_hint"] = secret_hint

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_stats import WebhookStats

        d = dict(src_dict)
        consecutive_failures = d.pop("consecutive_failures")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_types = cast(list[str], d.pop("event_types"))

        id = UUID(d.pop("id"))

        secret = d.pop("secret")

        stats_24h = WebhookStats.from_dict(d.pop("stats_24h"))

        status = check_webhook_endpoint_with_secret_status(d.pop("status"))

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

        secret_hint = d.pop("secret_hint", UNSET)

        webhook_endpoint_with_secret = cls(
            consecutive_failures=consecutive_failures,
            created_at=created_at,
            event_types=event_types,
            id=id,
            secret=secret,
            stats_24h=stats_24h,
            status=status,
            updated_at=updated_at,
            url=url,
            description=description,
            disabled_reason=disabled_reason,
            previous_secret_expires_at=previous_secret_expires_at,
            secret_hint=secret_hint,
        )

        return webhook_endpoint_with_secret
