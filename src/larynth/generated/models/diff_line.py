from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.diff_line_op import DiffLineOp, check_diff_line_op
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffLine")


@_attrs_define
class DiffLine:
    """
    Attributes:
        op (DiffLineOp):
        text (str):
        a (int | Unset): Line number in the older text
        b (int | Unset): Line number in the newer text
    """

    op: DiffLineOp
    text: str
    a: int | Unset = UNSET
    b: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        op: str = self.op

        text = self.text

        a = self.a

        b = self.b

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "op": op,
                "text": text,
            }
        )
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        op = check_diff_line_op(d.pop("op"))

        text = d.pop("text")

        a = d.pop("a", UNSET)

        b = d.pop("b", UNSET)

        diff_line = cls(
            op=op,
            text=text,
            a=a,
            b=b,
        )

        return diff_line
