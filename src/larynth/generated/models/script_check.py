from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.script_check_status import ScriptCheckStatus, check_script_check_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.script_check_reason import ScriptCheckReason


T = TypeVar("T", bound="ScriptCheck")


@_attrs_define
class ScriptCheck:
    """
    Attributes:
        assistant_id (UUID):
        reasons (list[ScriptCheckReason]):
        status (ScriptCheckStatus): flagged waits for a Larynth review within 1 business day; inbound keeps working
        version (int):
        checked_at (datetime.datetime | Unset):
        reviewed_at (datetime.datetime | Unset):
    """

    assistant_id: UUID
    reasons: list[ScriptCheckReason]
    status: ScriptCheckStatus
    version: int
    checked_at: datetime.datetime | Unset = UNSET
    reviewed_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        reasons = []
        for reasons_item_data in self.reasons:
            reasons_item = reasons_item_data.to_dict()
            reasons.append(reasons_item)

        status: str = self.status

        version = self.version

        checked_at: str | Unset = UNSET
        if not isinstance(self.checked_at, Unset):
            checked_at = self.checked_at.isoformat()

        reviewed_at: str | Unset = UNSET
        if not isinstance(self.reviewed_at, Unset):
            reviewed_at = self.reviewed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "reasons": reasons,
                "status": status,
                "version": version,
            }
        )
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.script_check_reason import ScriptCheckReason

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        reasons = []
        _reasons = d.pop("reasons")
        for reasons_item_data in _reasons:
            reasons_item = ScriptCheckReason.from_dict(reasons_item_data)

            reasons.append(reasons_item)

        status = check_script_check_status(d.pop("status"))

        version = d.pop("version")

        _checked_at = d.pop("checked_at", UNSET)
        checked_at: datetime.datetime | Unset
        if isinstance(_checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = datetime.datetime.fromisoformat(_checked_at)

        _reviewed_at = d.pop("reviewed_at", UNSET)
        reviewed_at: datetime.datetime | Unset
        if isinstance(_reviewed_at, Unset):
            reviewed_at = UNSET
        else:
            reviewed_at = datetime.datetime.fromisoformat(_reviewed_at)

        script_check = cls(
            assistant_id=assistant_id,
            reasons=reasons,
            status=status,
            version=version,
            checked_at=checked_at,
            reviewed_at=reviewed_at,
        )

        return script_check
