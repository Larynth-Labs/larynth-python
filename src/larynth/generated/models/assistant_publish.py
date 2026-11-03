from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.assistant_publish_kind import (
    AssistantPublishKind,
    check_assistant_publish_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssistantPublish")


@_attrs_define
class AssistantPublish:
    """
    Attributes:
        at (datetime.datetime):
        kind (AssistantPublishKind):
        version (int):
        by_name (str | Unset):
        by_user_id (UUID | Unset):
        id (UUID | Unset):
        note (str | Unset):
        previous_version (int | Unset):
    """

    at: datetime.datetime
    kind: AssistantPublishKind
    version: int
    by_name: str | Unset = UNSET
    by_user_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    note: str | Unset = UNSET
    previous_version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        kind: str = self.kind

        version = self.version

        by_name = self.by_name

        by_user_id: str | Unset = UNSET
        if not isinstance(self.by_user_id, Unset):
            by_user_id = str(self.by_user_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        note = self.note

        previous_version = self.previous_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "kind": kind,
                "version": version,
            }
        )
        if by_name is not UNSET:
            field_dict["by_name"] = by_name
        if by_user_id is not UNSET:
            field_dict["by_user_id"] = by_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if previous_version is not UNSET:
            field_dict["previous_version"] = previous_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        kind = check_assistant_publish_kind(d.pop("kind"))

        version = d.pop("version")

        by_name = d.pop("by_name", UNSET)

        _by_user_id = d.pop("by_user_id", UNSET)
        by_user_id: UUID | Unset
        if isinstance(_by_user_id, Unset):
            by_user_id = UNSET
        else:
            by_user_id = UUID(_by_user_id)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        note = d.pop("note", UNSET)

        previous_version = d.pop("previous_version", UNSET)

        assistant_publish = cls(
            at=at,
            kind=kind,
            version=version,
            by_name=by_name,
            by_user_id=by_user_id,
            id=id,
            note=note,
            previous_version=previous_version,
        )

        return assistant_publish
