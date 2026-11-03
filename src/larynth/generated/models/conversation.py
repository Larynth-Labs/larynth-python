from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_item import ConversationItem


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        call_id (str):
        duration_ms (int):
        items (list[ConversationItem]):
        latency_target_ms (int):
        live (bool):
        next_cursor (None | str):
        answered_at (datetime.datetime | Unset):
    """

    call_id: str
    duration_ms: int
    items: list[ConversationItem]
    latency_target_ms: int
    live: bool
    next_cursor: None | str
    answered_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        duration_ms = self.duration_ms

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        latency_target_ms = self.latency_target_ms

        live = self.live

        next_cursor: None | str
        next_cursor = self.next_cursor

        answered_at: str | Unset = UNSET
        if not isinstance(self.answered_at, Unset):
            answered_at = self.answered_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "duration_ms": duration_ms,
                "items": items,
                "latency_target_ms": latency_target_ms,
                "live": live,
                "next_cursor": next_cursor,
            }
        )
        if answered_at is not UNSET:
            field_dict["answered_at"] = answered_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.conversation_item import ConversationItem

        d = dict(src_dict)
        call_id = d.pop("call_id")

        duration_ms = d.pop("duration_ms")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ConversationItem.from_dict(items_item_data)

            items.append(items_item)

        latency_target_ms = d.pop("latency_target_ms")

        live = d.pop("live")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        _answered_at = d.pop("answered_at", UNSET)
        answered_at: datetime.datetime | Unset
        if isinstance(_answered_at, Unset):
            answered_at = UNSET
        else:
            answered_at = datetime.datetime.fromisoformat(_answered_at)

        conversation = cls(
            call_id=call_id,
            duration_ms=duration_ms,
            items=items,
            latency_target_ms=latency_target_ms,
            live=live,
            next_cursor=next_cursor,
            answered_at=answered_at,
        )

        return conversation
