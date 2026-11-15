from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PracticeCheckResult")


@_attrs_define
class PracticeCheckResult:
    """
    Attributes:
        key (str):
        label (str):
        passed (bool):
        evidence (str | Unset): The line or tool call the check looked at
    """

    key: str
    label: str
    passed: bool
    evidence: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        passed = self.passed

        evidence = self.evidence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "label": label,
                "passed": passed,
            }
        )
        if evidence is not UNSET:
            field_dict["evidence"] = evidence

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        passed = d.pop("passed")

        evidence = d.pop("evidence", UNSET)

        practice_check_result = cls(
            key=key,
            label=label,
            passed=passed,
            evidence=evidence,
        )

        return practice_check_result
