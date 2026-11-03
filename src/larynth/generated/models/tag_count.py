from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TagCount")


@_attrs_define
class TagCount:
    """
    Attributes:
        count (int):
        tag (str):
    """

    count: int
    tag: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        tag = self.tag

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        tag = d.pop("tag")

        tag_count = cls(
            count=count,
            tag=tag,
        )

        return tag_count
