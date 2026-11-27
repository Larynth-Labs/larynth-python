from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.catalog_voice import CatalogVoice


T = TypeVar("T", bound="VoicePage")


@_attrs_define
class VoicePage:
    """
    Attributes:
        items (list[CatalogVoice]):
        next_cursor (None | str): Cursor for the next page; null on the last page
    """

    items: list[CatalogVoice]
    next_cursor: None | str

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_voice import CatalogVoice

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = CatalogVoice.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        voice_page = cls(
            items=items,
            next_cursor=next_cursor,
        )

        return voice_page
