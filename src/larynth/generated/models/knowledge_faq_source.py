from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.knowledge_faq_source_kind import (
    KnowledgeFaqSourceKind,
    check_knowledge_faq_source_kind,
)
from ..models.knowledge_faq_source_status import (
    KnowledgeFaqSourceStatus,
    check_knowledge_faq_source_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_faq_entry import KnowledgeFaqEntry
    from ..models.knowledge_resync import KnowledgeResync


T = TypeVar("T", bound="KnowledgeFaqSource")


@_attrs_define
class KnowledgeFaqSource:
    """
    Attributes:
        created_at (datetime.datetime):
        documents (int): Pages or files extracted
        entries (list[KnowledgeFaqEntry]):
        id (UUID):
        kind (KnowledgeFaqSourceKind):
        knowledge_base_id (UUID):
        name (str):
        status (KnowledgeFaqSourceStatus):
        updated_at (datetime.datetime):
        error (str | Unset): Reason when status is failed
        file_bytes (int | Unset):
        file_name (str | Unset):
        last_synced_at (datetime.datetime | Unset):
        max_depth (int | Unset):
        max_pages (int | Unset):
        next_sync_at (datetime.datetime | Unset):
        resync (KnowledgeResync | Unset):
        url (str | Unset):
    """

    created_at: datetime.datetime
    documents: int
    entries: list[KnowledgeFaqEntry]
    id: UUID
    kind: KnowledgeFaqSourceKind
    knowledge_base_id: UUID
    name: str
    status: KnowledgeFaqSourceStatus
    updated_at: datetime.datetime
    error: str | Unset = UNSET
    file_bytes: int | Unset = UNSET
    file_name: str | Unset = UNSET
    last_synced_at: datetime.datetime | Unset = UNSET
    max_depth: int | Unset = UNSET
    max_pages: int | Unset = UNSET
    next_sync_at: datetime.datetime | Unset = UNSET
    resync: KnowledgeResync | Unset = UNSET
    url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        documents = self.documents

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        id = str(self.id)

        kind: str = self.kind

        knowledge_base_id = str(self.knowledge_base_id)

        name = self.name

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        error = self.error

        file_bytes = self.file_bytes

        file_name = self.file_name

        last_synced_at: str | Unset = UNSET
        if not isinstance(self.last_synced_at, Unset):
            last_synced_at = self.last_synced_at.isoformat()

        max_depth = self.max_depth

        max_pages = self.max_pages

        next_sync_at: str | Unset = UNSET
        if not isinstance(self.next_sync_at, Unset):
            next_sync_at = self.next_sync_at.isoformat()

        resync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resync, Unset):
            resync = self.resync.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "documents": documents,
                "entries": entries,
                "id": id,
                "kind": kind,
                "knowledge_base_id": knowledge_base_id,
                "name": name,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if file_bytes is not UNSET:
            field_dict["file_bytes"] = file_bytes
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth
        if max_pages is not UNSET:
            field_dict["max_pages"] = max_pages
        if next_sync_at is not UNSET:
            field_dict["next_sync_at"] = next_sync_at
        if resync is not UNSET:
            field_dict["resync"] = resync
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_faq_entry import KnowledgeFaqEntry
        from ..models.knowledge_resync import KnowledgeResync

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        documents = d.pop("documents")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = KnowledgeFaqEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        id = UUID(d.pop("id"))

        kind = check_knowledge_faq_source_kind(d.pop("kind"))

        knowledge_base_id = UUID(d.pop("knowledge_base_id"))

        name = d.pop("name")

        status = check_knowledge_faq_source_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        error = d.pop("error", UNSET)

        file_bytes = d.pop("file_bytes", UNSET)

        file_name = d.pop("file_name", UNSET)

        _last_synced_at = d.pop("last_synced_at", UNSET)
        last_synced_at: datetime.datetime | Unset
        if isinstance(_last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = datetime.datetime.fromisoformat(_last_synced_at)

        max_depth = d.pop("max_depth", UNSET)

        max_pages = d.pop("max_pages", UNSET)

        _next_sync_at = d.pop("next_sync_at", UNSET)
        next_sync_at: datetime.datetime | Unset
        if isinstance(_next_sync_at, Unset):
            next_sync_at = UNSET
        else:
            next_sync_at = datetime.datetime.fromisoformat(_next_sync_at)

        _resync = d.pop("resync", UNSET)
        resync: KnowledgeResync | Unset
        if isinstance(_resync, Unset):
            resync = UNSET
        else:
            resync = KnowledgeResync.from_dict(_resync)

        url = d.pop("url", UNSET)

        knowledge_faq_source = cls(
            created_at=created_at,
            documents=documents,
            entries=entries,
            id=id,
            kind=kind,
            knowledge_base_id=knowledge_base_id,
            name=name,
            status=status,
            updated_at=updated_at,
            error=error,
            file_bytes=file_bytes,
            file_name=file_name,
            last_synced_at=last_synced_at,
            max_depth=max_depth,
            max_pages=max_pages,
            next_sync_at=next_sync_at,
            resync=resync,
            url=url,
        )

        return knowledge_faq_source
