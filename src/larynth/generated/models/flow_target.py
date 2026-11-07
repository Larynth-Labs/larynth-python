from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FlowTarget")


@_attrs_define
class FlowTarget:
    """
    Attributes:
        type_ (str):
        value (str):
    """

    type_: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        value = d.pop("value")

        flow_target = cls(
            type_=type_,
            value=value,
        )

        return flow_target
