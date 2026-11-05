from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FlowBridge")


@_attrs_define
class FlowBridge:
    """
    Attributes:
        text (str):
    """

    text: str

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        text = d.pop("text")

        flow_bridge = cls(
            text=text,
        )

        return flow_bridge
