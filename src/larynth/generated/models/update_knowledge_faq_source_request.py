from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_faq_entry import KnowledgeFaqEntry


T = TypeVar("T", bound="UpdateKnowledgeFaqSourceRequest")


@_attrs_define
class UpdateKnowledgeFaqSourceRequest:
    """
    Attributes:
        entries (list[KnowledgeFaqEntry]):
        name (str | Unset):
    """

    entries: list[KnowledgeFaqEntry]
    name: str | Unset = UNSET

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
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

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

        name = d.pop("name", UNSET)

        update_knowledge_faq_source_request = cls(
            entries=entries,
            name=name,
        )

        return update_knowledge_faq_source_request
