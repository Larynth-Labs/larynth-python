from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeGapDraftSource")


@_attrs_define
class KnowledgeGapDraftSource:
    """
    Attributes:
        source_id (UUID):
        title (str | Unset):
    """

    source_id: UUID
    title: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_id = str(self.source_id)

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source_id": source_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_id = UUID(d.pop("source_id"))

        title = d.pop("title", UNSET)

        knowledge_gap_draft_source = cls(
            source_id=source_id,
            title=title,
        )

        return knowledge_gap_draft_source
