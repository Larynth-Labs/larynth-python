from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowSay")


@_attrs_define
class FlowSay:
    """
    Attributes:
        mode (str | Unset):
        text (str | Unset):
    """

    mode: str | Unset = UNSET
    text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode", UNSET)

        text = d.pop("text", UNSET)

        flow_say = cls(
            mode=mode,
            text=text,
        )

        return flow_say
