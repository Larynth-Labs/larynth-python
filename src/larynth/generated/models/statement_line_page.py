from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.statement_line import StatementLine


T = TypeVar("T", bound="StatementLinePage")


@_attrs_define
class StatementLinePage:
    """
    Attributes:
        closing_balance_micro (int): Customer credit after the last line of the period
        data (list[StatementLine]):
        next_cursor (None | str): Cursor for the next page; null on the last page
        opening_balance_micro (int): Customer credit before the first line of the period
    """

    closing_balance_micro: int
    data: list[StatementLine]
    next_cursor: None | str
    opening_balance_micro: int

    def to_dict(self) -> dict[str, Any]:
        closing_balance_micro = self.closing_balance_micro

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        opening_balance_micro = self.opening_balance_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "closing_balance_micro": closing_balance_micro,
                "data": data,
                "next_cursor": next_cursor,
                "opening_balance_micro": opening_balance_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.statement_line import StatementLine

        d = dict(src_dict)
        closing_balance_micro = d.pop("closing_balance_micro")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = StatementLine.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        opening_balance_micro = d.pop("opening_balance_micro")

        statement_line_page = cls(
            closing_balance_micro=closing_balance_micro,
            data=data,
            next_cursor=next_cursor,
            opening_balance_micro=opening_balance_micro,
        )

        return statement_line_page
