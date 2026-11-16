from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.issue_event_type import IssueEventType, check_issue_event_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_event_data import IssueEventData


T = TypeVar("T", bound="IssueEvent")


@_attrs_define
class IssueEvent:
    """
    Attributes:
        at (datetime.datetime):
        by_user_id (None | UUID):
        data (IssueEventData):
        id (UUID):
        type_ (IssueEventType):
        by_name (str | Unset):
        note (str | Unset):
    """

    at: datetime.datetime
    by_user_id: None | UUID
    data: IssueEventData
    id: UUID
    type_: IssueEventType
    by_name: str | Unset = UNSET
    note: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        by_user_id: None | str
        if isinstance(self.by_user_id, UUID):
            by_user_id = str(self.by_user_id)
        else:
            by_user_id = self.by_user_id

        data = self.data.to_dict()

        id = str(self.id)

        type_: str = self.type_

        by_name = self.by_name

        note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "by_user_id": by_user_id,
                "data": data,
                "id": id,
                "type": type_,
            }
        )
        if by_name is not UNSET:
            field_dict["by_name"] = by_name
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.issue_event_data import IssueEventData

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        def _parse_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                by_user_id_type_0 = UUID(data)

                return by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        by_user_id = _parse_by_user_id(d.pop("by_user_id"))

        data = IssueEventData.from_dict(d.pop("data"))

        id = UUID(d.pop("id"))

        type_ = check_issue_event_type(d.pop("type"))

        by_name = d.pop("by_name", UNSET)

        note = d.pop("note", UNSET)

        issue_event = cls(
            at=at,
            by_user_id=by_user_id,
            data=data,
            id=id,
            type_=type_,
            by_name=by_name,
            note=note,
        )

        return issue_event
