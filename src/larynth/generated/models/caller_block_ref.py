from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="CallerBlockRef")


@_attrs_define
class CallerBlockRef:
    """
    Attributes:
        created_at (datetime.datetime):
        id (UUID):
    """

    created_at: datetime.datetime
    id: UUID

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        caller_block_ref = cls(
            created_at=created_at,
            id=id,
        )

        return caller_block_ref
