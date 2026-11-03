from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CallsNotBilled")


@_attrs_define
class CallsNotBilled:
    """
    Attributes:
        blocked (int):
        short_call (int):
        spam (int):
    """

    blocked: int
    short_call: int
    spam: int

    def to_dict(self) -> dict[str, Any]:
        blocked = self.blocked

        short_call = self.short_call

        spam = self.spam

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "blocked": blocked,
                "short_call": short_call,
                "spam": spam,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        blocked = d.pop("blocked")

        short_call = d.pop("short_call")

        spam = d.pop("spam")

        calls_not_billed = cls(
            blocked=blocked,
            short_call=short_call,
            spam=spam,
        )

        return calls_not_billed
