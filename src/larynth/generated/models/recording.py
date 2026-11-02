from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.recording_state import RecordingState, check_recording_state
from ..types import UNSET, Unset

T = TypeVar("T", bound="Recording")


@_attrs_define
class Recording:
    """
    Attributes:
        call_id (str):
        created_at (datetime.datetime):
        format_ (str):
        id (UUID):
        retention_until (datetime.datetime):
        source (str):
        state (RecordingState):
        bytes_ (int | Unset):
        dropped (int | Unset):
        frames (int | Unset):
        plaintext_sha256 (str | Unset):
        purged_at (datetime.datetime | Unset):
        verified_at (datetime.datetime | Unset):
    """

    call_id: str
    created_at: datetime.datetime
    format_: str
    id: UUID
    retention_until: datetime.datetime
    source: str
    state: RecordingState
    bytes_: int | Unset = UNSET
    dropped: int | Unset = UNSET
    frames: int | Unset = UNSET
    plaintext_sha256: str | Unset = UNSET
    purged_at: datetime.datetime | Unset = UNSET
    verified_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        created_at = self.created_at.isoformat()

        format_ = self.format_

        id = str(self.id)

        retention_until = self.retention_until.isoformat()

        source = self.source

        state: str = self.state

        bytes_ = self.bytes_

        dropped = self.dropped

        frames = self.frames

        plaintext_sha256 = self.plaintext_sha256

        purged_at: str | Unset = UNSET
        if not isinstance(self.purged_at, Unset):
            purged_at = self.purged_at.isoformat()

        verified_at: str | Unset = UNSET
        if not isinstance(self.verified_at, Unset):
            verified_at = self.verified_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "created_at": created_at,
                "format": format_,
                "id": id,
                "retention_until": retention_until,
                "source": source,
                "state": state,
            }
        )
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if dropped is not UNSET:
            field_dict["dropped"] = dropped
        if frames is not UNSET:
            field_dict["frames"] = frames
        if plaintext_sha256 is not UNSET:
            field_dict["plaintext_sha256"] = plaintext_sha256
        if purged_at is not UNSET:
            field_dict["purged_at"] = purged_at
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        call_id = d.pop("call_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        format_ = d.pop("format")

        id = UUID(d.pop("id"))

        retention_until = datetime.datetime.fromisoformat(d.pop("retention_until"))

        source = d.pop("source")

        state = check_recording_state(d.pop("state"))

        bytes_ = d.pop("bytes", UNSET)

        dropped = d.pop("dropped", UNSET)

        frames = d.pop("frames", UNSET)

        plaintext_sha256 = d.pop("plaintext_sha256", UNSET)

        _purged_at = d.pop("purged_at", UNSET)
        purged_at: datetime.datetime | Unset
        if isinstance(_purged_at, Unset):
            purged_at = UNSET
        else:
            purged_at = datetime.datetime.fromisoformat(_purged_at)

        _verified_at = d.pop("verified_at", UNSET)
        verified_at: datetime.datetime | Unset
        if isinstance(_verified_at, Unset):
            verified_at = UNSET
        else:
            verified_at = datetime.datetime.fromisoformat(_verified_at)

        recording = cls(
            call_id=call_id,
            created_at=created_at,
            format_=format_,
            id=id,
            retention_until=retention_until,
            source=source,
            state=state,
            bytes_=bytes_,
            dropped=dropped,
            frames=frames,
            plaintext_sha256=plaintext_sha256,
            purged_at=purged_at,
            verified_at=verified_at,
        )

        return recording
