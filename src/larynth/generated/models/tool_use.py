from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolUse")


@_attrs_define
class ToolUse:
    """
    Attributes:
        assistant_id (UUID):
        live (bool): true when the published version uses it; false when only the open draft does
        name (str):
        pinned_revision (int | Unset): HTTP tools: the revision the version pins
    """

    assistant_id: UUID
    live: bool
    name: str
    pinned_revision: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        live = self.live

        name = self.name

        pinned_revision = self.pinned_revision

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "live": live,
                "name": name,
            }
        )
        if pinned_revision is not UNSET:
            field_dict["pinned_revision"] = pinned_revision

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        live = d.pop("live")

        name = d.pop("name")

        pinned_revision = d.pop("pinned_revision", UNSET)

        tool_use = cls(
            assistant_id=assistant_id,
            live=live,
            name=name,
            pinned_revision=pinned_revision,
        )

        return tool_use
