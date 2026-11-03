from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.timeline_item import TimelineItem


T = TypeVar("T", bound="TimelinePage")


@_attrs_define
class TimelinePage:
    """
    Attributes:
        items (list[TimelineItem]):
        next_cursor (None | str):
    """

    items: list[TimelineItem]
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
        from ..models.timeline_item import TimelineItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = TimelineItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        timeline_page = cls(
            items=items,
            next_cursor=next_cursor,
        )

        return timeline_page
