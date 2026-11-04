from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.rate_card_group_key import RateCardGroupKey, check_rate_card_group_key

if TYPE_CHECKING:
    from ..models.rate_card_line import RateCardLine


T = TypeVar("T", bound="RateCardGroup")


@_attrs_define
class RateCardGroup:
    """
    Attributes:
        key (RateCardGroupKey):
        lines (list[RateCardLine]):
    """

    key: RateCardGroupKey
    lines: list[RateCardLine]

    def to_dict(self) -> dict[str, Any]:
        key: str = self.key

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "lines": lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rate_card_line import RateCardLine

        d = dict(src_dict)
        key = check_rate_card_group_key(d.pop("key"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = RateCardLine.from_dict(lines_item_data)

            lines.append(lines_item)

        rate_card_group = cls(
            key=key,
            lines=lines,
        )

        return rate_card_group
