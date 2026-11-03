from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.after_hours_target_mode import (
    AfterHoursTargetMode,
    check_after_hours_target_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AfterHoursTarget")


@_attrs_define
class AfterHoursTarget:
    """
    Attributes:
        mode (AfterHoursTargetMode): take_message runs the open-hours agent with the closed-hours instruction and
            business_open = false
        assistant_id (UUID | Unset):
        forward_e164 (str | Unset):
    """

    mode: AfterHoursTargetMode
    assistant_id: UUID | Unset = UNSET
    forward_e164: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str = self.mode

        assistant_id: str | Unset = UNSET
        if not isinstance(self.assistant_id, Unset):
            assistant_id = str(self.assistant_id)

        forward_e164 = self.forward_e164

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if forward_e164 is not UNSET:
            field_dict["forward_e164"] = forward_e164

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = check_after_hours_target_mode(d.pop("mode"))

        _assistant_id = d.pop("assistant_id", UNSET)
        assistant_id: UUID | Unset
        if isinstance(_assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = UUID(_assistant_id)

        forward_e164 = d.pop("forward_e164", UNSET)

        after_hours_target = cls(
            mode=mode,
            assistant_id=assistant_id,
            forward_e164=forward_e164,
        )

        return after_hours_target
