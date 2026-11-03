from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.live_call_direction import LiveCallDirection, check_live_call_direction
from ..models.live_call_status import LiveCallStatus, check_live_call_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_call_flag import LiveCallFlag
    from ..models.live_call_line import LiveCallLine


T = TypeVar("T", bound="LiveCall")


@_attrs_define
class LiveCall:
    """
    Attributes:
        assistant_id (UUID):
        assistant_version (int):
        call_id (str):
        direction (LiveCallDirection):
        flags (list[LiveCallFlag]):
        started_at (datetime.datetime):
        status (LiveCallStatus):
        answered_at (datetime.datetime | Unset):
        caller_e164 (str | Unset):
        caller_name (str | Unset):
        campaign_id (UUID | Unset):
        last_line (LiveCallLine | Unset):
        number_id (UUID | Unset):
    """

    assistant_id: UUID
    assistant_version: int
    call_id: str
    direction: LiveCallDirection
    flags: list[LiveCallFlag]
    started_at: datetime.datetime
    status: LiveCallStatus
    answered_at: datetime.datetime | Unset = UNSET
    caller_e164: str | Unset = UNSET
    caller_name: str | Unset = UNSET
    campaign_id: UUID | Unset = UNSET
    last_line: LiveCallLine | Unset = UNSET
    number_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        assistant_version = self.assistant_version

        call_id = self.call_id

        direction: str = self.direction

        flags = []
        for flags_item_data in self.flags:
            flags_item = flags_item_data.to_dict()
            flags.append(flags_item)

        started_at = self.started_at.isoformat()

        status: str = self.status

        answered_at: str | Unset = UNSET
        if not isinstance(self.answered_at, Unset):
            answered_at = self.answered_at.isoformat()

        caller_e164 = self.caller_e164

        caller_name = self.caller_name

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        last_line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_line, Unset):
            last_line = self.last_line.to_dict()

        number_id: str | Unset = UNSET
        if not isinstance(self.number_id, Unset):
            number_id = str(self.number_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "assistant_version": assistant_version,
                "call_id": call_id,
                "direction": direction,
                "flags": flags,
                "started_at": started_at,
                "status": status,
            }
        )
        if answered_at is not UNSET:
            field_dict["answered_at"] = answered_at
        if caller_e164 is not UNSET:
            field_dict["caller_e164"] = caller_e164
        if caller_name is not UNSET:
            field_dict["caller_name"] = caller_name
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if last_line is not UNSET:
            field_dict["last_line"] = last_line
        if number_id is not UNSET:
            field_dict["number_id"] = number_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.live_call_flag import LiveCallFlag
        from ..models.live_call_line import LiveCallLine

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        assistant_version = d.pop("assistant_version")

        call_id = d.pop("call_id")

        direction = check_live_call_direction(d.pop("direction"))

        flags = []
        _flags = d.pop("flags")
        for flags_item_data in _flags:
            flags_item = LiveCallFlag.from_dict(flags_item_data)

            flags.append(flags_item)

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        status = check_live_call_status(d.pop("status"))

        _answered_at = d.pop("answered_at", UNSET)
        answered_at: datetime.datetime | Unset
        if isinstance(_answered_at, Unset):
            answered_at = UNSET
        else:
            answered_at = datetime.datetime.fromisoformat(_answered_at)

        caller_e164 = d.pop("caller_e164", UNSET)

        caller_name = d.pop("caller_name", UNSET)

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        _last_line = d.pop("last_line", UNSET)
        last_line: LiveCallLine | Unset
        if isinstance(_last_line, Unset):
            last_line = UNSET
        else:
            last_line = LiveCallLine.from_dict(_last_line)

        _number_id = d.pop("number_id", UNSET)
        number_id: UUID | Unset
        if isinstance(_number_id, Unset):
            number_id = UNSET
        else:
            number_id = UUID(_number_id)

        live_call = cls(
            assistant_id=assistant_id,
            assistant_version=assistant_version,
            call_id=call_id,
            direction=direction,
            flags=flags,
            started_at=started_at,
            status=status,
            answered_at=answered_at,
            caller_e164=caller_e164,
            caller_name=caller_name,
            campaign_id=campaign_id,
            last_line=last_line,
            number_id=number_id,
        )

        return live_call
