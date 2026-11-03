from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssistantPublished")


@_attrs_define
class AssistantPublished:
    """
    Attributes:
        at (datetime.datetime):
        version (int):
        by_name (str | Unset):
        by_user_id (UUID | Unset):
    """

    at: datetime.datetime
    version: int
    by_name: str | Unset = UNSET
    by_user_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        version = self.version

        by_name = self.by_name

        by_user_id: str | Unset = UNSET
        if not isinstance(self.by_user_id, Unset):
            by_user_id = str(self.by_user_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "version": version,
            }
        )
        if by_name is not UNSET:
            field_dict["by_name"] = by_name
        if by_user_id is not UNSET:
            field_dict["by_user_id"] = by_user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        version = d.pop("version")

        by_name = d.pop("by_name", UNSET)

        _by_user_id = d.pop("by_user_id", UNSET)
        by_user_id: UUID | Unset
        if isinstance(_by_user_id, Unset):
            by_user_id = UNSET
        else:
            by_user_id = UUID(_by_user_id)

        assistant_published = cls(
            at=at,
            version=version,
            by_name=by_name,
            by_user_id=by_user_id,
        )

        return assistant_published
