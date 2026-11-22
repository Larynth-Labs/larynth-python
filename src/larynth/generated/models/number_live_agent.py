from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NumberLiveAgent")


@_attrs_define
class NumberLiveAgent:
    """
    Attributes:
        assistant_id (UUID):
        version (int):
        version_id (UUID):
        published_at (datetime.datetime | Unset):
    """

    assistant_id: UUID
    version: int
    version_id: UUID
    published_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        version = self.version

        version_id = str(self.version_id)

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "version": version,
                "version_id": version_id,
            }
        )
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        version = d.pop("version")

        version_id = UUID(d.pop("version_id"))

        _published_at = d.pop("published_at", UNSET)
        published_at: datetime.datetime | Unset
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = datetime.datetime.fromisoformat(_published_at)

        number_live_agent = cls(
            assistant_id=assistant_id,
            version=version,
            version_id=version_id,
            published_at=published_at,
        )

        return number_live_agent
