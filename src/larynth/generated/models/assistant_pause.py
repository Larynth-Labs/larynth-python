from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssistantPause")


@_attrs_define
class AssistantPause:
    """
    Attributes:
        at (datetime.datetime):
        by_user_id (UUID | Unset):
        reason (str | Unset):
    """

    at: datetime.datetime
    by_user_id: UUID | Unset = UNSET
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        by_user_id: str | Unset = UNSET
        if not isinstance(self.by_user_id, Unset):
            by_user_id = str(self.by_user_id)

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
            }
        )
        if by_user_id is not UNSET:
            field_dict["by_user_id"] = by_user_id
        if reason is not UNSET:
            field_dict["reason"] = reason

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

        reason = d.pop("reason", UNSET)

        assistant_pause = cls(
            at=at,
            by_user_id=by_user_id,
            reason=reason,
        )

        return assistant_pause
