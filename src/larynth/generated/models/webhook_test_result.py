from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookTestResult")


@_attrs_define
class WebhookTestResult:
    """
    Attributes:
        event_id (UUID):
    """

    event_id: UUID

    def to_dict(self) -> dict[str, Any]:
        event_id = str(self.event_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event_id": event_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        event_id = UUID(d.pop("event_id"))

        webhook_test_result = cls(
            event_id=event_id,
        )

        return webhook_test_result
