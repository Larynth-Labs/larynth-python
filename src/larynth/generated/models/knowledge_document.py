from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeDocument")


@_attrs_define
class KnowledgeDocument:
    """
    Attributes:
        excluded (bool): Left out of the next build; for pages the choice survives a re-crawl
        fetched_at (datetime.datetime):
        id (UUID):
        source_id (UUID):
        title (str):
        words (int):
        file_name (str | Unset):
        url (str | Unset):
    """

    excluded: bool
    fetched_at: datetime.datetime
    id: UUID
    source_id: UUID
    title: str
    words: int
    file_name: str | Unset = UNSET
    url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        excluded = self.excluded

        fetched_at = self.fetched_at.isoformat()

        id = str(self.id)

        source_id = str(self.source_id)

        title = self.title

        words = self.words

        file_name = self.file_name

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "excluded": excluded,
                "fetched_at": fetched_at,
                "id": id,
                "source_id": source_id,
                "title": title,
                "words": words,
            }
        )
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        excluded = d.pop("excluded")

        fetched_at = datetime.datetime.fromisoformat(d.pop("fetched_at"))

        id = UUID(d.pop("id"))

        source_id = UUID(d.pop("source_id"))

        title = d.pop("title")

        words = d.pop("words")

        file_name = d.pop("file_name", UNSET)

        url = d.pop("url", UNSET)

        knowledge_document = cls(
            excluded=excluded,
            fetched_at=fetched_at,
            id=id,
            source_id=source_id,
            title=title,
            words=words,
            file_name=file_name,
            url=url,
        )

        return knowledge_document
