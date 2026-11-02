from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.assistant_status import AssistantStatus, check_assistant_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="Assistant")


@_attrs_define
class Assistant:
    """
    Attributes:
        created_at (datetime.datetime):
        id (UUID):
        latest_version (int):
        name (str):
        status (AssistantStatus):
        updated_at (datetime.datetime):
        archived_at (datetime.datetime | Unset):
        published_version (int | Unset):
    """

    created_at: datetime.datetime
    id: UUID
    latest_version: int
    name: str
    status: AssistantStatus
    updated_at: datetime.datetime
    archived_at: datetime.datetime | Unset = UNSET
    published_version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        latest_version = self.latest_version

        name = self.name

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        published_version = self.published_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "latest_version": latest_version,
                "name": name,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if published_version is not UNSET:
            field_dict["published_version"] = published_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        latest_version = d.pop("latest_version")

        name = d.pop("name")

        status = check_assistant_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        published_version = d.pop("published_version", UNSET)

        assistant = cls(
            created_at=created_at,
            id=id,
            latest_version=latest_version,
            name=name,
            status=status,
            updated_at=updated_at,
            archived_at=archived_at,
            published_version=published_version,
        )

        return assistant
