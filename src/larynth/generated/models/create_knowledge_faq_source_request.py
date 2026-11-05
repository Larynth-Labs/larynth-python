from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.knowledge_faq_entry import KnowledgeFaqEntry


T = TypeVar("T", bound="CreateKnowledgeFaqSourceRequest")


@_attrs_define
class CreateKnowledgeFaqSourceRequest:
    """
    Attributes:
        entries (list[KnowledgeFaqEntry]):
        name (str):
    """

    entries: list[KnowledgeFaqEntry]
    name: str

    def to_dict(self) -> dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entries": entries,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_faq_entry import KnowledgeFaqEntry

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = KnowledgeFaqEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        name = d.pop("name")

        create_knowledge_faq_source_request = cls(
            entries=entries,
            name=name,
        )

        return create_knowledge_faq_source_request
