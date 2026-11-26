from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishAssistantVersionRequest")


@_attrs_define
class PublishAssistantVersionRequest:
    """
    Attributes:
        note (str | Unset):
        override_reason (str | Unset): Publish although a required practice call did not pass; logged in the audit trail
        practice_run_id (UUID | Unset): The finished publish-trigger practice run for this draft revision; required from
            the dashboard when the agent has required practice calls
    """

    note: str | Unset = UNSET
    override_reason: str | Unset = UNSET
    practice_run_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        note = self.note

        override_reason = self.override_reason

        practice_run_id: str | Unset = UNSET
        if not isinstance(self.practice_run_id, Unset):
            practice_run_id = str(self.practice_run_id)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if override_reason is not UNSET:
            field_dict["override_reason"] = override_reason
        if practice_run_id is not UNSET:
            field_dict["practice_run_id"] = practice_run_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        note = d.pop("note", UNSET)

        override_reason = d.pop("override_reason", UNSET)

        _practice_run_id = d.pop("practice_run_id", UNSET)
        practice_run_id: UUID | Unset
        if isinstance(_practice_run_id, Unset):
            practice_run_id = UNSET
        else:
            practice_run_id = UUID(_practice_run_id)

        publish_assistant_version_request = cls(
            note=note,
            override_reason=override_reason,
            practice_run_id=practice_run_id,
        )

        return publish_assistant_version_request
