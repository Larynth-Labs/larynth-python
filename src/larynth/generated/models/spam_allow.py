from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpamAllow")


@_attrs_define
class SpamAllow:
    """
    Attributes:
        created_at (datetime.datetime):
        e164 (str):
        id (UUID):
        note (str | Unset):
    """

    created_at: datetime.datetime
    e164: str
    id: UUID
    note: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "e164": e164,
                "id": id,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        note = d.pop("note", UNSET)

        spam_allow = cls(
            created_at=created_at,
            e164=e164,
            id=id,
            note=note,
        )

        return spam_allow
