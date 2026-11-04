from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.order_numbers_request_kind import (
    OrderNumbersRequestKind,
    check_order_numbers_request_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_numbers_item import OrderNumbersItem
    from ..models.routing_plan import RoutingPlan


T = TypeVar("T", bound="OrderNumbersRequest")


@_attrs_define
class OrderNumbersRequest:
    """
    Attributes:
        items (list[OrderNumbersItem]):
        kind (OrderNumbersRequestKind):
        label (str | Unset):
        routing (RoutingPlan | Unset):
        spam_screening (bool | Unset):
    """

    items: list[OrderNumbersItem]
    kind: OrderNumbersRequestKind
    label: str | Unset = UNSET
    routing: RoutingPlan | Unset = UNSET
    spam_screening: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        kind: str = self.kind

        label = self.label

        routing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.routing, Unset):
            routing = self.routing.to_dict()

        spam_screening = self.spam_screening

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "kind": kind,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if routing is not UNSET:
            field_dict["routing"] = routing
        if spam_screening is not UNSET:
            field_dict["spam_screening"] = spam_screening

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.order_numbers_item import OrderNumbersItem
        from ..models.routing_plan import RoutingPlan

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderNumbersItem.from_dict(items_item_data)

            items.append(items_item)

        kind = check_order_numbers_request_kind(d.pop("kind"))

        label = d.pop("label", UNSET)

        _routing = d.pop("routing", UNSET)
        routing: RoutingPlan | Unset
        if isinstance(_routing, Unset):
            routing = UNSET
        else:
            routing = RoutingPlan.from_dict(_routing)

        spam_screening = d.pop("spam_screening", UNSET)

        order_numbers_request = cls(
            items=items,
            kind=kind,
            label=label,
            routing=routing,
            spam_screening=spam_screening,
        )

        return order_numbers_request
