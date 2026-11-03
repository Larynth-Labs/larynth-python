from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallFlag")


@_attrs_define
class CallFlag:
    """
    Attributes:
        at (datetime.datetime):
        by_user_id (UUID | Unset):
    """

    at: datetime.datetime
    by_user_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        by_user_id: str | Unset = UNSET
        if not isinstance(self.by_user_id, Unset):
            by_user_id = str(self.by_user_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
            }
        )
        if by_user_id is not UNSET:
            field_dict["by_user_id"] = by_user_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        _by_user_id = d.pop("by_user_id", UNSET)
        by_user_id: UUID | Unset
        if isinstance(_by_user_id, Unset):
            by_user_id = UNSET
        else:
            by_user_id = UUID(_by_user_id)

        call_flag = cls(
            at=at,
            by_user_id=by_user_id,
        )

        return call_flag
