from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.order_number_request_route_type import (
    OrderNumberRequestRouteType,
    check_order_number_request_route_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderNumberRequest")


@_attrs_define
class OrderNumberRequest:
    """
    Attributes:
        e164 (str):
        assistant_id (UUID | Unset): Required when route_type is assistant
        forward_to_e164 (str | Unset): Required when route_type is forward
        route_type (OrderNumberRequestRouteType | Unset):
    """

    e164: str
    assistant_id: UUID | Unset = UNSET
    forward_to_e164: str | Unset = UNSET
    route_type: OrderNumberRequestRouteType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        assistant_id: str | Unset = UNSET
        if not isinstance(self.assistant_id, Unset):
            assistant_id = str(self.assistant_id)

        forward_to_e164 = self.forward_to_e164

        route_type: str | Unset = UNSET
        if not isinstance(self.route_type, Unset):
            route_type = self.route_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
            }
        )
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if forward_to_e164 is not UNSET:
            field_dict["forward_to_e164"] = forward_to_e164
        if route_type is not UNSET:
            field_dict["route_type"] = route_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164 = d.pop("e164")

        _assistant_id = d.pop("assistant_id", UNSET)
        assistant_id: UUID | Unset
        if isinstance(_assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = UUID(_assistant_id)

        forward_to_e164 = d.pop("forward_to_e164", UNSET)

        _route_type = d.pop("route_type", UNSET)
        route_type: OrderNumberRequestRouteType | Unset
        if isinstance(_route_type, Unset):
            route_type = UNSET
        else:
            route_type = check_order_number_request_route_type(_route_type)

        order_number_request = cls(
            e164=e164,
            assistant_id=assistant_id,
            forward_to_e164=forward_to_e164,
            route_type=route_type,
        )

        return order_number_request
