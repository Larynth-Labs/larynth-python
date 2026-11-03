from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.check_fix_kind import CheckFixKind, check_check_fix_kind

T = TypeVar("T", bound="CheckFix")


@_attrs_define
class CheckFix:
    """
    Attributes:
        kind (CheckFixKind):
        target (str): Dashboard route or wizard step
    """

    kind: CheckFixKind
    target: str

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        target = self.target

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_check_fix_kind(d.pop("kind"))

        target = d.pop("target")

        check_fix = cls(
            kind=kind,
            target=target,
        )

        return check_fix
