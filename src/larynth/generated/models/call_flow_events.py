from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.flow_event import FlowEvent


T = TypeVar("T", bound="CallFlowEvents")


@_attrs_define
class CallFlowEvents:
    """
    Attributes:
        events (list[FlowEvent]): At most 2,000, in seq order
    """

    events: list[FlowEvent]

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_event import FlowEvent

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = FlowEvent.from_dict(events_item_data)

            events.append(events_item)

        call_flow_events = cls(
            events=events,
        )

        return call_flow_events
