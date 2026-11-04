from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookReplay")


@_attrs_define
class WebhookReplay:
    """
    Attributes:
        count (int):
        id (UUID):
    """

    count: int
    id: UUID

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        id = str(self.id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        id = UUID(d.pop("id"))

        webhook_replay = cls(
            count=count,
            id=id,
        )

        return webhook_replay
