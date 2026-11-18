from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.issue_kind import IssueKind, check_issue_kind
from ..models.issue_resolution import IssueResolution, check_issue_resolution
from ..models.issue_status import IssueStatus, check_issue_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_action import IssueAction
    from ..models.issue_assignee import IssueAssignee
    from ..models.issue_detail import IssueDetail
    from ..models.issue_latest import IssueLatest
    from ..models.issue_ref import IssueRef


T = TypeVar("T", bound="Issue")


@_attrs_define
class Issue:
    """
    Attributes:
        actions (list[IssueAction]): The server decides which apply; the first is the primary one
        assistant_id (None | UUID):
        created_at (datetime.datetime):
        detail (IssueDetail):
        first_seen_at (datetime.datetime):
        id (UUID):
        ignored_until (datetime.datetime | None): Null with status ignored means ignored for good
        impact (int): Higher is worse; the board is sorted by it
        kind (IssueKind):
        last_seen_at (datetime.datetime):
        occurrences (int):
        reopened_count (int):
        resolution (IssueResolution):
        resolved_at (datetime.datetime | None):
        status (IssueStatus):
        title (str):
        updated_at (datetime.datetime):
        assignee (IssueAssignee | Unset):
        assistant_name (str | Unset):
        latest (IssueLatest | Unset):
        ref (IssueRef | Unset):
    """

    actions: list[IssueAction]
    assistant_id: None | UUID
    created_at: datetime.datetime
    detail: IssueDetail
    first_seen_at: datetime.datetime
    id: UUID
    ignored_until: datetime.datetime | None
    impact: int
    kind: IssueKind
    last_seen_at: datetime.datetime
    occurrences: int
    reopened_count: int
    resolution: IssueResolution
    resolved_at: datetime.datetime | None
    status: IssueStatus
    title: str
    updated_at: datetime.datetime
    assignee: IssueAssignee | Unset = UNSET
    assistant_name: str | Unset = UNSET
    latest: IssueLatest | Unset = UNSET
    ref: IssueRef | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        assistant_id: None | str
        if isinstance(self.assistant_id, UUID):
            assistant_id = str(self.assistant_id)
        else:
            assistant_id = self.assistant_id

        created_at = self.created_at.isoformat()

        detail = self.detail.to_dict()

        first_seen_at = self.first_seen_at.isoformat()

        id = str(self.id)

        ignored_until: None | str
        if isinstance(self.ignored_until, datetime.datetime):
            ignored_until = self.ignored_until.isoformat()
        else:
            ignored_until = self.ignored_until

        impact = self.impact

        kind: str = self.kind

        last_seen_at = self.last_seen_at.isoformat()

        occurrences = self.occurrences

        reopened_count = self.reopened_count

        resolution: str = self.resolution

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        status: str = self.status

        title = self.title

        updated_at = self.updated_at.isoformat()

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        assistant_name = self.assistant_name

        latest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest, Unset):
            latest = self.latest.to_dict()

        ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref, Unset):
            ref = self.ref.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actions": actions,
                "assistant_id": assistant_id,
                "created_at": created_at,
                "detail": detail,
                "first_seen_at": first_seen_at,
                "id": id,
                "ignored_until": ignored_until,
                "impact": impact,
                "kind": kind,
                "last_seen_at": last_seen_at,
                "occurrences": occurrences,
                "reopened_count": reopened_count,
                "resolution": resolution,
                "resolved_at": resolved_at,
                "status": status,
                "title": title,
                "updated_at": updated_at,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if assistant_name is not UNSET:
            field_dict["assistant_name"] = assistant_name
        if latest is not UNSET:
            field_dict["latest"] = latest
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.issue_action import IssueAction
        from ..models.issue_assignee import IssueAssignee
        from ..models.issue_detail import IssueDetail
        from ..models.issue_latest import IssueLatest
        from ..models.issue_ref import IssueRef

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = IssueAction.from_dict(actions_item_data)

            actions.append(actions_item)

        def _parse_assistant_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assistant_id_type_0 = UUID(data)

                return assistant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        assistant_id = _parse_assistant_id(d.pop("assistant_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        detail = IssueDetail.from_dict(d.pop("detail"))

        first_seen_at = datetime.datetime.fromisoformat(d.pop("first_seen_at"))

        id = UUID(d.pop("id"))

        def _parse_ignored_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ignored_until_type_0 = datetime.datetime.fromisoformat(data)

                return ignored_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ignored_until = _parse_ignored_until(d.pop("ignored_until"))

        impact = d.pop("impact")

        kind = check_issue_kind(d.pop("kind"))

        last_seen_at = datetime.datetime.fromisoformat(d.pop("last_seen_at"))

        occurrences = d.pop("occurrences")

        reopened_count = d.pop("reopened_count")

        resolution = check_issue_resolution(d.pop("resolution"))

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))

        status = check_issue_status(d.pop("status"))

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _assignee = d.pop("assignee", UNSET)
        assignee: IssueAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = IssueAssignee.from_dict(_assignee)

        assistant_name = d.pop("assistant_name", UNSET)

        _latest = d.pop("latest", UNSET)
        latest: IssueLatest | Unset
        if isinstance(_latest, Unset):
            latest = UNSET
        else:
            latest = IssueLatest.from_dict(_latest)

        _ref = d.pop("ref", UNSET)
        ref: IssueRef | Unset
        if isinstance(_ref, Unset):
            ref = UNSET
        else:
            ref = IssueRef.from_dict(_ref)

        issue = cls(
            actions=actions,
            assistant_id=assistant_id,
            created_at=created_at,
            detail=detail,
            first_seen_at=first_seen_at,
            id=id,
            ignored_until=ignored_until,
            impact=impact,
            kind=kind,
            last_seen_at=last_seen_at,
            occurrences=occurrences,
            reopened_count=reopened_count,
            resolution=resolution,
            resolved_at=resolved_at,
            status=status,
            title=title,
            updated_at=updated_at,
            assignee=assignee,
            assistant_name=assistant_name,
            latest=latest,
            ref=ref,
        )

        return issue
