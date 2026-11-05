from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="KnowledgeBaseUse")


@_attrs_define
class KnowledgeBaseUse:
    """
    Attributes:
        assistant_id (UUID):
        live (bool): true when the published version attaches the base; false when only the open draft does
        name (str):
    """

    assistant_id: UUID
    live: bool
    name: str

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        live = self.live

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "live": live,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        live = d.pop("live")

        name = d.pop("name")

        knowledge_base_use = cls(
            assistant_id=assistant_id,
            live=live,
            name=name,
        )

        return knowledge_base_use
