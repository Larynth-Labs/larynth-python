from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.call_quality_check_key import (
    CallQualityCheckKey,
    check_call_quality_check_key,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallQualityCheck")


@_attrs_define
class CallQualityCheck:
    """
    Attributes:
        key (CallQualityCheckKey):
        passed (bool):
        at_ms (int | Unset): Offset of the moment the check refers to
        note (str | Unset):
    """

    key: CallQualityCheckKey
    passed: bool
    at_ms: int | Unset = UNSET
    note: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key: str = self.key

        passed = self.passed

        at_ms = self.at_ms

        note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "passed": passed,
            }
        )
        if at_ms is not UNSET:
            field_dict["at_ms"] = at_ms
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = check_call_quality_check_key(d.pop("key"))

        passed = d.pop("passed")

        at_ms = d.pop("at_ms", UNSET)

        note = d.pop("note", UNSET)

        call_quality_check = cls(
            key=key,
            passed=passed,
            at_ms=at_ms,
            note=note,
        )

        return call_quality_check
