from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.knowledge_base_status import (
    KnowledgeBaseStatus,
    check_knowledge_base_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeBase")


@_attrs_define
class KnowledgeBase:
    """
    Attributes:
        chunk_count (int):
        created_at (datetime.datetime):
        description (str):
        id (UUID):
        name (str):
        ready_source_count (int):
        source_count (int):
        status (KnowledgeBaseStatus): ready once every source is indexed; failed carries error
        updated_at (datetime.datetime):
        error (str | Unset):
    """

    chunk_count: int
    created_at: datetime.datetime
    description: str
    id: UUID
    name: str
    ready_source_count: int
    source_count: int
    status: KnowledgeBaseStatus
    updated_at: datetime.datetime
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        chunk_count = self.chunk_count

        created_at = self.created_at.isoformat()

        description = self.description

        id = str(self.id)

        name = self.name

        ready_source_count = self.ready_source_count

        source_count = self.source_count

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "chunk_count": chunk_count,
                "created_at": created_at,
                "description": description,
                "id": id,
                "name": name,
                "ready_source_count": ready_source_count,
                "source_count": source_count,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        chunk_count = d.pop("chunk_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        ready_source_count = d.pop("ready_source_count")

        source_count = d.pop("source_count")

        status = check_knowledge_base_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        error = d.pop("error", UNSET)

        knowledge_base = cls(
            chunk_count=chunk_count,
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            ready_source_count=ready_source_count,
            source_count=source_count,
            status=status,
            updated_at=updated_at,
            error=error,
        )

        return knowledge_base
