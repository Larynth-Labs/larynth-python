from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.diff_line import DiffLine


T = TypeVar("T", bound="InstructionsDiff")


@_attrs_define
class InstructionsDiff:
    """
    Attributes:
        adds (int):
        dels (int):
        lines (list[DiffLine]): Equal runs longer than 3 lines are elided
    """

    adds: int
    dels: int
    lines: list[DiffLine]

    def to_dict(self) -> dict[str, Any]:
        adds = self.adds

        dels = self.dels

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "adds": adds,
                "dels": dels,
                "lines": lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.diff_line import DiffLine

        d = dict(src_dict)
        adds = d.pop("adds")

        dels = d.pop("dels")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = DiffLine.from_dict(lines_item_data)

            lines.append(lines_item)

        instructions_diff = cls(
            adds=adds,
            dels=dels,
            lines=lines,
        )

        return instructions_diff
