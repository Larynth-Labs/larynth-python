from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.tag_count import TagCount


T = TypeVar("T", bound="ListTagCount")


@_attrs_define
class ListTagCount:
    """
    Attributes:
        data (list[TagCount]):
    """

    data: list[TagCount]

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tag_count import TagCount

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TagCount.from_dict(data_item_data)

            data.append(data_item)

        list_tag_count = cls(
            data=data,
        )

        return list_tag_count
