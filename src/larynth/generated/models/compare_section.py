from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.compare_section_key import CompareSectionKey, check_compare_section_key

if TYPE_CHECKING:
    from ..models.compare_change import CompareChange


T = TypeVar("T", bound="CompareSection")


@_attrs_define
class CompareSection:
    """
    Attributes:
        changes (list[CompareChange]):
        key (CompareSectionKey):
    """

    changes: list[CompareChange]
    key: CompareSectionKey

    def to_dict(self) -> dict[str, Any]:
        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        key: str = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "changes": changes,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.compare_change import CompareChange

        d = dict(src_dict)
        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = CompareChange.from_dict(changes_item_data)

            changes.append(changes_item)

        key = check_compare_section_key(d.pop("key"))

        compare_section = cls(
            changes=changes,
            key=key,
        )

        return compare_section
