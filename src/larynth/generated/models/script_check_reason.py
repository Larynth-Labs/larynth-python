from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScriptCheckReason")


@_attrs_define
class ScriptCheckReason:
    """
    Attributes:
        code (str):
        excerpt (str | Unset):
    """

    code: str
    excerpt: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        excerpt = self.excerpt

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        excerpt = d.pop("excerpt", UNSET)

        script_check_reason = cls(
            code=code,
            excerpt=excerpt,
        )

        return script_check_reason
