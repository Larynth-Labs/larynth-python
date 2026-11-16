from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.update_issue_request_resolution import (
    UpdateIssueRequestResolution,
    check_update_issue_request_resolution,
)
from ..models.update_issue_request_status import (
    UpdateIssueRequestStatus,
    check_update_issue_request_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIssueRequest")


@_attrs_define
class UpdateIssueRequest:
    """
    Attributes:
        assignee_user_id (str | Unset): A member's user id; an empty string unassigns
        ignored_until (datetime.datetime | Unset): With status ignored: when it comes back; omit to ignore for good
        note (str | Unset): Written to the history; do not paste caller details
        resolution (UpdateIssueRequestResolution | Unset):
        status (UpdateIssueRequestStatus | Unset): resolved needs resolution fixed or not_a_problem; open reopens by
            hand
    """

    assignee_user_id: str | Unset = UNSET
    ignored_until: datetime.datetime | Unset = UNSET
    note: str | Unset = UNSET
    resolution: UpdateIssueRequestResolution | Unset = UNSET
    status: UpdateIssueRequestStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assignee_user_id = self.assignee_user_id

        ignored_until: str | Unset = UNSET
        if not isinstance(self.ignored_until, Unset):
            ignored_until = self.ignored_until.isoformat()

        note = self.note

        resolution: str | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if assignee_user_id is not UNSET:
            field_dict["assignee_user_id"] = assignee_user_id
        if ignored_until is not UNSET:
            field_dict["ignored_until"] = ignored_until
        if note is not UNSET:
            field_dict["note"] = note
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assignee_user_id = d.pop("assignee_user_id", UNSET)

        _ignored_until = d.pop("ignored_until", UNSET)
        ignored_until: datetime.datetime | Unset
        if isinstance(_ignored_until, Unset):
            ignored_until = UNSET
        else:
            ignored_until = datetime.datetime.fromisoformat(_ignored_until)

        note = d.pop("note", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: UpdateIssueRequestResolution | Unset
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = check_update_issue_request_resolution(_resolution)

        _status = d.pop("status", UNSET)
        status: UpdateIssueRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_issue_request_status(_status)

        update_issue_request = cls(
            assignee_user_id=assignee_user_id,
            ignored_until=ignored_until,
            note=note,
            resolution=resolution,
            status=status,
        )

        return update_issue_request
