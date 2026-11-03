from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompareChange")


@_attrs_define
class CompareChange:
    """
    Attributes:
        path (str): Spec path
        after (Any | Unset):
        before (Any | Unset):
    """

    path: str
    after: Any | Unset = UNSET
    before: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        after = self.after

        before = self.before

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
            }
        )
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path")

        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        compare_change = cls(
            path=path,
            after=after,
            before=before,
        )

        return compare_change
